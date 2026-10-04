"""Download the four frozen public training/validation shards; never fetch test images."""
from __future__ import annotations
import argparse
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path
import requests


def digest(path):
    value = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            value.update(chunk)
    return value.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, required=True)
    args = parser.parse_args()
    args.data_dir.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(Path(__file__).with_name('data_sources.json').read_text())
    verified = []
    for record in manifest['files']:
        target = args.data_dir / record['filename']
        if not (target.exists() and target.stat().st_size == record['bytes'] and digest(target) == record['sha256']):
            partial = target.with_suffix(target.suffix + '.part')
            for attempt in range(6):
                try:
                    offset = partial.stat().st_size if partial.exists() else 0
                    if offset == record['bytes'] and digest(partial) == record['sha256']:
                        partial.replace(target)
                        break
                    if offset >= record['bytes']:
                        partial.unlink()
                        offset = 0
                    headers = {'Range': f'bytes={offset}-'} if offset else {}
                    with requests.get(record['url'], headers=headers, stream=True, timeout=(30, 120)) as response:
                        response.raise_for_status()
                        append = offset > 0 and response.status_code == 206
                        if append:
                            content_range = response.headers.get('Content-Range', '')
                            if not content_range.startswith(f'bytes {offset}-'):
                                raise ValueError(f'Unexpected Content-Range: {content_range}')
                        with partial.open('ab' if append else 'wb') as stream:
                            for chunk in response.iter_content(1024 * 1024):
                                stream.write(chunk)
                    if partial.stat().st_size != record['bytes'] or digest(partial) != record['sha256']:
                        raise ValueError('Size/SHA256 mismatch; do not use these bytes for training')
                    partial.replace(target)
                    break
                except (requests.RequestException, ValueError, OSError) as error:
                    print(f'{target.name}: attempt {attempt + 1}: {error}', flush=True)
                    if attempt == 5:
                        raise
                    time.sleep(min(10 * (attempt + 1), 50))
        verified.append({**record, 'verified_at': datetime.now(timezone.utc).isoformat()})
        print('VERIFIED', target.name, flush=True)
    (args.data_dir / 'verified_sources.json').write_text(json.dumps(verified, indent=2) + '\n')


if __name__ == '__main__':
    main()

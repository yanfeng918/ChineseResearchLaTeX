#!/usr/bin/env python3
"""Verify the final PDF's citation links against BibTeX outputs; emit JSON."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import pymupdf


def main():
    project = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, default=project / "main.pdf")
    parser.add_argument("--aux", type=Path, default=project / ".latex-cache/main.aux")
    parser.add_argument("--bbl", type=Path, default=project / ".latex-cache/main.bbl")
    args = parser.parse_args()
    aux = args.aux.read_text(encoding="utf-8")
    bbl = args.bbl.read_text(encoding="utf-8")
    expected = Counter(
        key.strip()
        for group in re.findall(r"\\citation\{([^}]+)\}", aux)
        for key in group.split(",")
        if key.strip() != "*"
    )
    bibitems = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", bbl)
    labels = dict(re.findall(r"\\bibcite\{([^}]+)\}\{(\d+)\}", aux))
    errors = []
    warnings = []
    destinations = []
    observed = Counter()
    checked_visible_numbers = 0
    total_pdf_links = 0

    if not expected:
        errors.append({"type": "no_aux_citations"})
    if not bibitems:
        errors.append({"type": "no_bibitems"})
    if len(set(bibitems)) != len(bibitems):
        errors.append({"type": "duplicate_bibitems"})
    missing_items = set(expected) - set(bibitems)
    if missing_items:
        errors.append({"type": "cited_keys_missing_from_bbl", "keys": sorted(missing_items)})

    with pymupdf.open(args.pdf) as document:
        names = document.resolve_names()
        for ordinal, key in enumerate(bibitems, 1):
            name = "cite." + key
            destination = names.get(name)
            if destination is None:
                errors.append({"type": "missing_named_destination", "key": key})
                continue
            page_number = destination.get("page", -1)
            if not 0 <= page_number < len(document):
                errors.append({"type": "invalid_destination_page", "key": key,
                               "destination": destination})
                continue
            number = labels.get(key)
            if number != str(ordinal):
                errors.append({"type": "bib_number_mismatch", "key": key,
                               "bbl_ordinal": ordinal, "aux_label": number})
            page = document[page_number]
            point = destination.get("to")
            matched_label = False
            if point is not None and number is not None:
                # resolve_names() retains PDF coordinates; text uses top-left origin.
                anchor = pymupdf.Point(point) * page.transformation_matrix
                matches = page.search_for("[" + number + "]")
                matched_label = any(abs(rect.y0 - anchor.y) <= 30 for rect in matches)
                if not matched_label:
                    errors.append({"type": "destination_not_at_numbered_bibitem",
                                   "key": key, "number": number,
                                   "pdf_page": page_number + 1,
                                   "anchor_y": round(anchor.y, 3),
                                   "number_label_y": [round(rect.y0, 3) for rect in matches]})
            else:
                errors.append({"type": "unverifiable_destination_position", "key": key})
            destinations.append({"key": key, "number": number,
                                 "pdf_page": page_number + 1,
                                 "numbered_item_verified": matched_label})

        for page_number, page in enumerate(document):
            for link in page.get_links():
                total_pdf_links += 1
                name = None
                for path in ("A/D", "Dest"):
                    kind, value = document.xref_get_key(link["xref"], path)
                    if kind in ("string", "name"):
                        candidate = value.lstrip("/") if kind == "name" else value
                        if candidate.startswith("cite."):
                            name = candidate
                            break
                if name is None:
                    continue
                key = name[len("cite."):]
                observed[key] += 1
                target = names.get(name)
                # PyMuPDF reports named /GoTo destinations as LINK_NAMED,
                # even when their page and coordinates are fully resolved.
                action_type, action = document.xref_get_key(link["xref"], "A/S")
                internal_action = action_type == "name" and action == "/GoTo"
                if action_type == "null":
                    direct_type, _ = document.xref_get_key(link["xref"], "Dest")
                    internal_action = direct_type in ("string", "name")
                resolved_page, _, _ = document.resolve_link("#" + name)
                if (target is None or not internal_action
                        or link.get("kind") not in (pymupdf.LINK_GOTO, pymupdf.LINK_NAMED)
                        or resolved_page < 0):
                    errors.append({"type": "unresolved_citation_link", "key": key,
                                   "source_pdf_page": page_number + 1})
                    continue
                if (link.get("page") != target.get("page")
                        or resolved_page != target.get("page")):
                    errors.append({"type": "annotation_destination_mismatch", "key": key,
                                   "source_pdf_page": page_number + 1})
                number = labels.get(key)
                rectangle = pymupdf.Rect(link["from"]) + (-0.5, -0.5, 0.5, 0.5)
                visible = page.get_text("text", clip=rectangle).strip()
                visible_numbers = re.findall(r"\d+", visible)
                if number is not None and number in visible_numbers:
                    checked_visible_numbers += 1
                elif visible_numbers:
                    errors.append({"type": "citation_visible_number_mismatch", "key": key,
                                   "expected_number": number, "visible_text": visible,
                                   "source_pdf_page": page_number + 1})
                else:
                    warnings.append({"type": "citation_number_text_unavailable", "key": key,
                                     "source_pdf_page": page_number + 1})

        for key in sorted(set(expected) | set(observed)):
            if expected[key] != observed[key]:
                errors.append({"type": "citation_link_count_mismatch", "key": key,
                               "expected": expected[key], "observed": observed[key]})

        report = {
            "status": "passed" if not errors else "failed",
            "pdf": str(args.pdf.resolve()),
            "pdf_pages": len(document),
            "bibliography_entries": len(bibitems),
            "unique_cited_keys": len(expected),
            "expected_citation_links": sum(expected.values()),
            "observed_citation_links": sum(observed.values()),
            "total_pdf_links": total_pdf_links,
            "verified_visible_citation_numbers": checked_visible_numbers,
            "verified_bibliography_targets": sum(item["numbered_item_verified"]
                                                 for item in destinations),
            "destinations": destinations,
            "errors": errors,
            "warnings": warnings,
        }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

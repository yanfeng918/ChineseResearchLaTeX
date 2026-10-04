"""复用 CIESM 填写回归，用新项目源码在本测试目录生成隔离夹具。"""
import importlib.util
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
ROOT = TEST_DIR.parents[1]
spec = importlib.util.spec_from_file_location(
    "ciesm_editability", ROOT / "tests/diqiushuzhi-template/verify_editability.py"
)
suite = importlib.util.module_from_spec(spec)
spec.loader.exec_module(suite)
suite.SOURCE = ROOT / "projects/NSFC_2026_CIESM-STSR_final"
suite.TEST_DIR = TEST_DIR

if __name__ == "__main__":
    suite.main()

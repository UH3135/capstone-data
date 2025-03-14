from pathlib import Path


# DIR PATHS
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT_DIR / "assets" / "input"
OUTPUT_DIR = ROOT_DIR / "assets" / "output"
OUTPUT_JSON = OUTPUT_DIR / "output.json"

# 추출할 Ctrl obj
CTRL_TYPES = ["표", "그림", "수식"]

# 유니코드 폰트 문자 → LaTeX 변환 맵
UNICODE_LATEX_MAP = {
    "ℤ": r"\mathbb{Z}",
    "ℝ": r"\mathbb{R}",
    "ℕ": r"\mathbb{N}",
    "ℍ": r"\mathbb{H}",
    "ℚ": r"\mathbb{Q}",
    "ℂ": r"\mathbb{C}",
    "ℙ": r"\mathbb{P}",
    "not=": r"\neq"
}

# LaTex 문자 → 유니코드 폰트 변환맵
LATEX_UNICODE_MAP = {
    "\\text{mathbbZ}" : "ℤ",
    "\\text{mathbbR}" : "ℝ",
    "\\text{mathbbN}" : "ℕ",
    "\\text{mathbbQ}" : "ℚ",
    "\\text{mathbbC}" : "ℂ",
    "\\text{mathbbH}" : "ℍ",
    "\\text{mathbbP}" : "ℙ"
}
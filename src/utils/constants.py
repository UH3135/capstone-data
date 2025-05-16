from pathlib import Path


# DIR PATHS
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT_DIR / "assets" / "input"
OUTPUT_DIR = ROOT_DIR / "assets" / "output"
OUTPUT_PICKLE = OUTPUT_DIR / "output.pickle"
OUTPUT_JSON = OUTPUT_DIR / "output.json"

# 추출할 Ctrl obj
CTRL_TYPES = ["표", "그림", "수식"]

# image 분류 카테고리
IMAGE_CATEGORY = {
    "Graph": [
        'a picture including curve graph',
        'a picture including linear graph',
        'a picture including bar graph',
        'a picture including unexpected data',
    ],

    "Formula": [
        'equilibrium expression for a chemical',
        'formula including fraction or symbols',
    ],
    
    "Text": [
        'a sentence including Hangul',
        'a phrase including Hangul',
        'a photo including Hangul',
        'a sentence including English word',
        'a sentence including korean language',
    ]
}

FORMULA_OCR_MESSAGE = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "Extract mathematical expressions in LaTeX format"}
        ]
    },
]

# capstone-data

Hwp 파일 Json으로 변환

## Code Convention

1. Black

- Black은 PEP 8을 강제하는 자동 코드 포맷터이며, 코드 스타일을 자동으로 정리해줌.

2. Flake8

- Black은 코드를 자동 수정해주지만, Flake8은 코드 스타일을 검사하고 경고 메시지를 출력하는 도구임

3. isort

- import 구문의 순서를 PEP 8 스타일에 맞게 자동 정리해주는 도구.

4. Code Convention 적용
   1. Pre-commit Hook 설치
   ```
   pip install pre-commit
   ```
   2. 적용
   ```
   pre-commit install
   ```

## hwp to Json

1. hwp to html
   - pyhwpx 모듈 사용
   - html tag를 가능한 보존
2. table and LaTeX parsing
   - html tag를 이용하여 Data Parsing
3. Image to Text (with OCR model)
   - Azure OPENAI를 이용하여 Img to Text 작업 진행
4. Data Process
   - 의미없는 괄호, 공백 제거
5. Json
   - Metadata 추가

## File Structure

```
hwp-to-html-parser/
│── assets/                      # HWP 파일 저장 디렉토리
│   ├── input/                   # 원본 HWP 파일 저장
│   │   ├── sample1.hwp
│   │   ├── sample2.hwp
│   ├── output/                  # 변환된 JSON/HTML 파일 저장
│   │   ├── sample1.html
│   │   ├── sample1.json
│── src/
│   ├── parsers/                 # 데이터 파싱 관련 모듈
│   │   ├── hwp_to_html.py       # HWP -> HTML 변환
│   │   ├── table_parser.py      # 테이블 변환
│   │   ├── latex_parser.py.     # LaTeX 변환
│   │   ├── image_ocr.py         # 이미지 → 텍스트 (OCR)
│   │   ├── data_cleaner.py      # 데이터 전처리 (공백/특수문자 제거)
│   │   ├── json_formatter.py    # JSON 변환 및 Metadata 추가
│   │   ├── __init__.py
│   ├── utils/                   # 유틸리티 함수 모음
│   │   ├── file_handler.py      # 파일 입출력 관련 모듈
│   │   ├── logger.py    # 로깅 설정
│   │   ├── constants.py         # 상수 관리
│   │   ├── __init__.py
│   ├── main.py                  # 프로그램 실행 진입점
│── docs/                         # 문서화
│   ├── README.md
│   ├── API_DOCS.md
│── .pre-commit-config.yaml       # 코드 스타일 자동 적용
│── .gitignore                    # Git에서 제외할 파일 목록
│── pyproject.toml                 # 패키지 및 도구 설정
│── requirements.txt              # Python 패키지 의존성 목록
│── LICENSE                       # 라이선스 파일
│── README.md                     # 프로젝트 개요
```

## 실행 방법
1. pyhwpx 설치
```
pip install --pre pyhwpx 
```
2. assets Directory 생성
   - assets 파일 아래에 input 폴더 안에 모든 hwp 파일을 담아둡니다.


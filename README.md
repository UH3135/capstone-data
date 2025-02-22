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

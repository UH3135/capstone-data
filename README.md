# 프로젝트 소개
hwp로 된 강의 자료에 포함된 **복잡한 표나 이미지**를 정보나 순서의 손실이 없도록 **JSON 포맷으로 변환하는 전처리 모듈**입니다.

## Result
- Image parsing
- Table parsing

## Tech Stack
- pyhwpx [https://pypi.org/project/pyhwpx/]
- Paddle OCR [https://github.com/PaddlePaddle/PaddleOCR]
- Google Siglip2 [https://huggingface.co/blog/siglip2]
- Docling [https://github.com/docling-project/docling]

## File Structure

```
hwp-to-html-parser/
│── assets/                      # HWP 파일 저장 디렉토리
│   ├── input/                   # 원본 HWP 파일 저장
│   │   ├── sample1.hwp
│   │   ├── sample2.hwp
│   ├── output/                  # 변환된 JSON/HTML 파일 저장
│   │   ├── sample1.json
│── src/
│   ├── parsers/                 # 데이터 파싱 관련 모듈
│   │   ├── clipboard.py         # hwp에서 clipboard로 이미지, 표 추출(html)
│   │   ├── equ_parser.py        # 한글 수식을 LaTeX 형식으로 변환
│   │   ├── image_ocr.py         # 이미지를 String으로 변환
│   │   ├── process_hwp_docs.py  # hwp automation api 컨트롤
│   │   ├── table_parser.py      # 표를 Dict 형태로 변환
│   ├── utils/                   
│   │   ├── constants.py         # 파일 경로, 라벨, 프롬프트 등 저장
│   │   ├── Exception_Fix.py     # 수식 변환시 생기는 예외 형식 저장
│   │   ├── file_handler.py      # 파일 로드 관련 모듈 (pickling 등) (삭제 예정)
│   │   ├── logger.py            # 로깅 설정
│   │   ├── window_asciimath.py  # py-asciimath 경로 지정
│   ├── main.py                  # 프로그램 실행 진입점
```

### 환경 설명

Windows 기반의 환경에서만 HWP to Json 변환이 가능합니다.

1. pyhwpx 설치

```
pip install --pre pyhwpx
```

2. CUDA/cuDNN 설치
   -  GPU에 맞는 CUDA 버전 설치
   ```
   https://developer.nvidia.com/cuda-downloads
   ```
   -  CUDA 버전에 따라 cuDNN 설치
   ```
   https://developer.nvidia.com/cudnn-downloads
   ```

3. assets Directory 생성
   - assets 파일 아래에 input 폴더 안에 모든 hwp 파일을 담아둡니다.

4. Python 실행

```
python src/main.py
```

## Project Structure
![Image](https://github.com/user-attachments/assets/ea1ecba7-46de-4a48-909f-535fe3df87d9)

## 코드 아키텍쳐
### src/main.py

- 프로그램의 진입점(Entry Point)입니다.
- 전체 파이프라인을 실행하며, 각 파서 및 유틸리티 모듈을 호출합니다.
- 예시 실행:  
  ```bash
  python src/main.py
  ```

### src/parsers/

1. clipboard.py
- HWP 문서에서 이미지, 표를 클립보드 방식으로 추출하여 HTML로 변환합니다.

2. equ_parser.py
- 한글 문서 내 수식을 LaTeX 형식으로 변환합니다.
- 수식 변환 과정에서 발생하는 예외 처리는 utils/Exception_Fix.py에서 관리합니다.

3. image_ocr.py
- 이미지 내 텍스트를 OCR(광학 문자 인식) 기술로 추출하여 문자열로 변환합니다.
- PaddleOCR 등 외부 라이브러리를 활용합니다.

4. process_hwp_docs.py
- pyhwpx 등 HWP 자동화 API를 통해 문서를 제어하고, 각종 데이터 추출을 자동화합니다.

5. table_parser.py
- HWP 문서 내 표를 Dict(딕셔너리) 형태로 변환합니다.
- 추출된 표는 JSON 포맷으로 저장됩니다.

### src/utils/

1. constants.py
- 파일 경로, 라벨, 프롬프트 등 프로젝트 전역에서 사용하는 상수를 정의합니다.

2. Exception_Fix.py
- 수식 변환 등에서 발생하는 예외 케이스를 정의하고 처리합니다.

3. file_handler.py (삭제 예정)
- 파일 로드 및 저장 관련 기능(예: 피클링 등)을 담당합니다.

4. logger.py
- 프로젝트 전반의 로깅 설정 및 로그 출력을 담당합니다.

5. window_asciimath.py
- py-asciimath 경로 지정 등 수식 변환에 필요한 환경 설정을 담당합니다.

### assets/

- input/: 변환할 원본 HWP 파일을 저장합니다.
- output/: 변환된 JSON/HTML 파일이 저장됩니다.

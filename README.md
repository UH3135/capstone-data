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


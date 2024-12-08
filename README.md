# Image-OCR-and-Translation-Project

## 프로젝트 개요
이 프로젝트는 이미지에서 텍스트를 추출(OCR)하고, 추출된 텍스트를 번역하는 기능을 제공합니다.  
**OpenCV**와 **Tesseract OCR**을 사용하여 이미지 전처리 및 텍스트 추출을 진행하며,  
**Hugging Face의 Transformers 모델**을 통해 다국어 번역 기능을 구현합니다.

---

## 데모 및 예시
### 1. 입력 이미지 예시

![sample_image](https://github.com/user-attachments/assets/2b7347e4-c012-46ec-a1de-e41d220f5891)


### 2. OCR 및 번역 결과
- **추출된 텍스트**:But the human tongue can lead to far more devastating outcomes, 
    which are not always apparent in the first instance. We may, in some cases, 
    never know who assaulted us, because they act as if they are your best friends. 
    Especially when you perform in a leadership position, you will encounter people 
    who behave very friendly around you and agree with everything you say. However, 
    these same individuals may engage in badmouthing and backstabbing as soon as 
    they are out of sight. It is, therefore, wise to be friendly with everyone and yet 
    practice healthy detachment by refraining from telling people your innermost 
    secrets. By practicing this method, you can avoid making yourself a potential 
    victim of others' jealousy and hatred. The more people know about you, the more 
    vulnerable you become to their negativity.

- **번역된 텍스트**: 그러나 인간의 혀는 훨씬 더 파괴적인 결과를 초래할 수 있으며,
    처음에는 항상 명백하지 않을 수 있습니다. 우리는 어떤 경우에는
    우리를 공격한 사람이 누구인지 모를 수도 있습니다, 왜냐하면 그들이
    마치 가장 친한 친구인 것처럼 행동하기 때문입니다. 특히 리더십 위치에서
    활동할 때, 당신은 매우 친절하게 행동하며 당신이 말하는 모든 것에 동의하는 사람들을 만날 것입니다.
    그러나 이러한 사람들은 당신이 보지 않을 때 나쁜 말과 배신을 할 수 있습니다.
    따라서 모든 사람에게 친절하게 대하면서도, 자신의 내밀한 비밀을 말하지 않는 건강한
    거리를 두는 연습을 하는 것이 현명합니다. 이 방법을 실천하면 다른 사람들의 질투와 증오의
    잠재적인 피해자가 되는 것을 피할 수 있습니다. 사람들이 당신에 대해 알수록, 그들의 부정적인
    에너지에 더 취약해집니다.

## 사용한 패키지 및 버전
아래는 프로젝트에서 사용된 주요 패키지와 설치 방법입니다.

- **Python 3.10+**
- **OpenCV**: `opencv-python==4.10.0.84`
- **NumPy**: `numpy==2.1.3`
- **Tesseract OCR**: `pytesseract==0.3.13`
- **Transformers**: `transformers==4.33.2`
  

### 설치 방법
1. 프로젝트 루트 디렉토리로 이동:
 cd Image-OCR-and-Translation

2. 가상 환경 생성 (권장):
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
필요한 패키지 설치: pip install -r requirements.txt
Tesseract 설치: Tesseract 설치 가이드 참고

3. 실행 방법
이미지 OCR 및 번역 실행:
프로젝트 루트에서 다음 명령어 실행:
python main.py

4. 결과 확인: 
번역된 텍스트는 translated_text.txt 파일에 저장됩니다.
OCR 및 번역 결과 이미지는 output_images/ 디렉토리에 저장됩니다.

### 참고 자료
OpenCV Documentation
Tesseract OCR GitHub
Hugging Face Transformers
Python 공식 문서
Chat gpt

## 1. 프로젝트 구조

![image](https://github.com/user-attachments/assets/46c8bd79-fc27-4872-afc1-5c1b9f7b94d2)


## 2. 작업 내용 요약

### 2.1. 이미지 전처리
- OpenCV를 사용하여 **이미지에서 불필요한 노이즈 제거** 및 **텍스트 영역 강조**.
- 전처리 작업:
  - **흑백 변환 (Grayscale)**: 컬러 이미지를 흑백으로 변환.
  - **이진화 (Binarization)**: 텍스트 인식률을 높이기 위해 이미지 대비를 조정.
  - **이미지 회전 및 기하학적 변환**: 왜곡된 이미지를 정렬.

### 2.2. 텍스트 추출 (OCR)
- 전처리된 이미지를 **Tesseract OCR**로 입력하여 텍스트를 추출.
- 추출된 텍스트는 **구조화된 데이터**로 저장하여 번역 단계로 전달.
- Tesseract OCR 성능 최적화를 위해 환경 변수 설정 필요:
  ```bash
  # Tesseract 설치 후 경로 추가 (예: Windows)
  setx PATH "%PATH%;C:\Program Files\Tesseract-OCR"

### 2.3. 텍스트 번역
Hugging Face 번역 모델 (Helsinki-NLP/opus-mt-en-ko)을 사용하여 영어 텍스트를 한국어로 번역.
추출된 텍스트는 translate.py에서 번역 처리.

### 2.4. 번역된 텍스트 출력
이미지에 텍스트 오버레이:
번역된 텍스트를 이미지 위에 표시하고 결과 이미지를 저장.
텍스트 파일 출력:
번역된 텍스트를 .txt 파일로 저장.

## 4. 실행 결과
### 4.1. 입력
예제 입력 이미지: sample_image.jpg.
### 4.2. 출력
전처리된 이미지: processed_image.jpg 파일에 저장.
추출된 텍스트: extracted_text.txt 파일에 저장.
번역된 텍스트: translated_text.txt 파일에 저장.
번역된 텍스트가 포함된 이미지: output_image.jpg 파일에 저장.

## 5. 역할 및 브랜치 관리
### 5.1. 역할 1: 이미지 전처리 및 텍스트 추출 담당
이미지 전처리:
OpenCV를 사용하여 노이즈 제거, 흑백 변환, 이진화 등 전처리 작업 수행.
텍스트 추출:Tesseract OCR을 사용하여 텍스트 인식 및 추출.
GitHub 관리:image_processing 브랜치에서 작업 후, Pull Request로 main 브랜치에 병합.
### 5.2. 역할 2: 텍스트 번역 및 결과 출력 담당
텍스트 번역:Hugging Face 번역 모델을 사용하여 텍스트 번역 (예: 영어 → 한국어).
결과 출력:번역된 텍스트를 이미지에 오버레이하거나, 텍스트 파일로 저장.
GitHub 관리:text_translation 브랜치에서 작업 후, Pull Request로 main 브랜치에 병합.

## 6. 공통 GitHub 역할
리더:브랜치 관리 및 Pull Request 병합 담당.
최종적으로 README.md 작성 및 GitHub 리포지토리 설정.
팀원:각자 작업한 코드 커밋 및 푸시.
커밋 메시지를 구체적으로 작성:
예: "Add OCR extraction functionality"

## 7. 예제 커밋 메시지
"Add preprocess.py for image preprocessing"
"Update translate.py to handle multi-language translation"
"Fix bug in output_display.py related to image overlay"

## 8. 추가 참고
Tesseract 설치: Tesseract GitHub
Hugging Face 번역 모델: Helsinki-NLP on Hugging Face
yaml



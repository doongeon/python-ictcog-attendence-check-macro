# 📅 ICTCOG LMS Attendance Checker Macro

### 자동 출석체크 매크로

이 프로젝트는 ICTCOG LMS에서 조교의 출석체크를 자동화하기 위한 매크로입니다.  
아래 단계를 따라 설정하고 실행할 수 있습니다.

---

## ⚙️ 실행 방법

### 1. 설정

리포지토리 다운
```bash
git clone https://github.com/doongeon/python-ictcog-attendence-check-macro.git
```
다운 후 `Utils.py` 파일을 열어 ICT COG 조교 계정의 **ID**와 **비밀번호**를 입력한 후 저장합니다.

### 2. 가상 환경 설정 및 실행
터미널을 열고, 아래 명령어를 실행하세요:

```bash
# 가상 환경 생성
python3 -m venv venv

# 가상 환경 활성화
source venv/bin/activate

# 필요한 패키지 설치
pip install beautifulsoup4
pip install selenium

# 프로그램 실행
python3 App.py
```

### 3. 결석 처리할 이름 입력
터미널에 결석 처리할 이름을 모두 입력합니다.
이름은 공백 없이, **콤마(,)**로 구분해서 입력하세요.

예시:
홍길동,김철수,이영희

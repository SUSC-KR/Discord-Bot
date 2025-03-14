# 기여자 가이드

기여를 하고자 이곳으로 들어온 여러분들 모두 환영하며 감사합니다.  
이 문서는 여러분들이 이 프로젝트에 기여할 수 있도록 도와줄 것입니다. 이 프로젝트에 기여하기 전에 이 문서를 읽어주시기 바랍니다.  


## 시작하기

프로젝트에 새로 참여한 경우 커뮤니티의 프로젝트가 어떻게 작동하는지 이해하는 데 도움이 필요할 수 있으므로 커뮤니티의 다른 구성원(대부분 SUSC 오픈소스 관리자)으로부터 멘토링을 받는 것을 고려할 수 있습니다. 

커뮤니티의 멤버들을 멘토링하는 것은 SUSC의 오픈소스 관리자의 역할 중 일부이므로 도움을 요청하는 것을 두려워하지 않으셔도 괜찮습니다. PR에 댓글을 달거나, GitHub Issues 혹은 GitHub Discussions 에서 질문하거나, Discord를 통해 질문할 수 있습니다. 

## SUSC 오픈소스 프로젝트에서 역할

SUSC의 오픈소스 프로젝트에는 다양한 역할이 존재합니다.  

### Project Manager
이 프로젝트의 Project Manager는 이 프로젝트의 주요 책임자입니다. 이 프로젝트의 모든 측면을 관리하고 프로젝트의 방향을 결정합니다.  


### Committer
Committer 같은 경우에는 이 프로젝트의 쓰기 권한을 가집니다.

- PR을 리뷰하며 검토 및 병합.
- GitHub Issues 관리 및 답변.


### Contributor
Contributor란 SUSC 프로젝트에 코드, 문서, 테스트, 아이디어 또는 무엇이든 기여하고자 하는 사람을 말합니다.

Contributor는 다음과 같은 역할을 가집니다:
- 이슈를 제기하거나 논의에 참여.
- 기능 추가
- 코드, 문서, 테스트, 아이디어 등을 제공.

### SUSC Open Source Manager
SUSC의 Open Source Manager는 SUSC의 오픈소스 프로젝트를 관리하고, 조언을 해주는 역할을 담당합니다.

SUSC의 Open Source Manager는 다음과 같은 역할을 가집니다:
- SUSC에서 생긴 Open Source 프로젝트를 관리.
- SUSC의 Open Source 프로젝트에 대한 조언을 해줌.
- SUSC의 Open Source 프로젝트에 대한 문제를 해결.


## 기여하는 방법
SUSC의 오픈소스 프로젝트에 기여하는 방법은 다양하게 존재합니다. 이 프로젝트에 기여하는 방법은 다음과 같습니다.

### 버그 리포트
GitHub Issues를 통해 버그를 리포트해주시면 감사하겠습니다.  
문제가 있는 정보를 최대한 자세히 제공해주시면 더욱 빠르게 문제를 해결할 수 있습니다.  

### 버그 수정
현재 이 프로젝트에 있는 버그를 GitHub Issues에서 확인하고, 수정하고 싶은 버그가 있다면 수정해주시면 감사하겠습니다.  
이 작업을 해보고 싶은 모든 사람들을 환영합니다.

### 문제 보고 및 해결 프로세스

SUSC의 오픈소스 프로젝트에 기여할 때 간단한 버그에 대한 수정은 PR을 통해 직접 해결 할 수 있습니다. Issue나 Discussion을 먼저 열 필요는 없습니다. 대신 어떤 문제가 있었는지, 어떻게 해결했는지에 대한 설명을 PR에 자세히 적어주시면 감사하겠습니다.

간단한 버그 픽스가 아닌 경우에는 먼저 Issue를 열어 문제에 대해 논의하고, 그 후 PR을 열어 해결할 수 있습니다. 이때 PR에는 Issue 번호를 참조해주시기 바랍니다.


### 기능 제안

기능 추가나 변경을 하고 싶으신 경우에는 먼저 Discussion을 열어 논의하고, 그 후 Issue와 PR을 열어 변경사항을 제안해주시기 바랍니다.



## 프로젝트 실행하기

1. 이 저장소를 fork합니다.
2. fork한 저장소를 clone합니다.

```bash
git clone https://github.com/SUSC-KR/Discord-Bot.git
cd Discord-Bot
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```
4. 봇실행
```bash
python -m discord_bot
```

## 코드 가이드라인

### 목적

이 프로젝트는 Flake8과 Pylint를 활용하여 코드 품질을 유지하고 스타일을 표준화합니다. 위 설정을 준수하여 코드 작성 시 일관성을 유지하고, 자동화된 검사를 통해 코드 품질을 향상시키고 있습니다.

### Flake8 (Linting)

Flake8은 Python 스타일 가이드 준수를 검사하는 도구입니다.

```sh
flake8 ./discord_bot --count --show-source --statistics --max-line-length=120
```

#### 주요 검사 항목
- 최대 줄 길이는 120자로 제한됩니다.
- 사용되지 않는 변수를 허용하지 않습니다.
- 들여쓰기나 공백 관련 스타일 오류를 방지합니다.

#### 주로 실패하는 사례

- 너무 긴 줄 (E501): 한 줄에 120자를 초과하는 경우
- 사용되지 않는 변수 (F841): 정의했지만 사용하지 않은 변수
- 들여쓰기 오류 (E111, E114): 잘못된 들여쓰기

### Pylint (Static Analysis)

Pylint는 코드의 품질을 분석하고 잠재적인 오류를 찾는 정적 분석 도구입니다.

```sh
pylint ./discord_bot --disable=C0114,C0115,C0116,C0301,W0718,R0913,R0917
```

#### 설정 설명
- 허용 항목
  - `C0114`: 모듈에 docstring이 없음
  - `C0115`: 클래스에 docstring이 없음
  - `C0116`: 함수 또는 메서드에 docstring이 없음
  - `C0301`: 한 줄에 100자를 초과하는 경우
  - `W0718`: 일반적인 예외(Exception) 사용 경고
  - `R0913`: 너무 많은 인자를 받는 함수 또는 메서드
  - `R0917`: 너무 많은 위치 인자를 받는 함수 또는 메서드

### 정적 분석 및 스타일 검사 실행 방법

터미널에서 다음 명령어를 실행하면 Flake8과 Pylint 검사를 수행할 수 있습니다.

```sh
flake8 ./discord_bot --count --show-source --statistics --max-line-length=120
pylint ./discord_bot --disable=C0114,C0115,C0116,C0301,W0718,R0913,R0917
```

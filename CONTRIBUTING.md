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
git clone https://github.com/[your-github-id]/Discord-Bot.git
cd Discord-Bot
```

3. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate
```

4. 의존성 설치
```bash
pip install -r requirements.txt
```
5. 봇실행
```bash
python -m discord_bot
```

## 프로젝트 실행하기 (`uv` 사용)

1. uv 설치

```bash
# With pip.
pip install uv

# With Homebrew.
brew install uv
```

2. 저장소 포크 && 클론

```bash
git clone https://github.com/[your-github-id]/Discord-Bot.git
cd Discord-Bot
```

3. 가상환경 venv 추가 및 의존성 설치

```bash
uv sync
```

4. 봇 실행

```bash
uv run -m discord_bot
```

## 코드 가이드라인

### 목적

이 프로젝트는 `ruff`를 활용하여 코드 품질을 유지하고 스타일을 표준화합니다.  
`ruff.toml` 설정을 기준으로 일관된 코드를 작성하며, 자동화된 검사를 통해 코드 품질과 유지보수성을 향상시키고 있습니다.

### Ruff (Linting & Formatting)

[Ruff](https://docs.astral.sh/ruff/)는 Python 코드 린팅과 스타일 검사, 포매팅까지 지원하는 빠르고 강력한 도구입니다.  
기존의 `flake8`, `pylint`, `isort`, `pyupgrade` 기능을 통합하여 한 번에 검사할 수 있습니다.

```sh
ruff check ./discord_bot
ruff format ./discord_bot
```

#### 주요 검사 항목 (`ruff.toml` 기준)

| 검사 코드 그룹 | 설명 |
|----------------|------|
| **E (pycodestyle)** | 공백, 줄바꿈, 들여쓰기 등 스타일 관련 규칙 검사 |
| **F (pyflakes)** | 정의되지 않은 변수, 사용되지 않는 변수 등 오류 검사 |
| **B (flake8-bugbear)** | 잠재적 버그, 비효율적인 코드 감지 |
| **I (isort)** | `import` 순서 및 그룹 정렬 |
| **UP (pyupgrade)** | Python 3.12에 맞춰 구식 문법을 최신 문법으로 교체 가능 여부 확인 |

#### 스타일 기준

- **최대 줄 길이**: 120자 (`line-length = 120`)
- **Python 버전**: 3.12 기준 검사 (`target-version = "py312"`)
- **문자열 포맷**: `"double quote"` 사용 (`quote-style = "double"`)

#### 자주 발생하는 검사 실패 예시

- **E501**: 한 줄에 120자를 초과한 경우
- **F841**: 선언만 하고 사용하지 않은 변수
- **B006**: mutable default argument 사용
- **I001**: import 순서가 기준에 맞지 않음
- **UP032**: f-string으로 바꿀 수 있는 `.format()` 문법

### 정적 분석 및 스타일 검사 실행 방법

```bash
# 코드 스타일 및 린팅 검사
ruff check ./discord_bot

# 오류 자동 수정
ruff check ./discord_bot --fix

# 코드 자동 포맷
ruff format ./discord_bot
```
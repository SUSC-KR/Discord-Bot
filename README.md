# SUSC 운영 디스코드 봇(SCSC 쓱쓱 봇)

## SCSC 쓱쓱 봇
이 디스코드 봇은 서버의 카테고리, 역할 및 스터디 룸을 효율적으로 관리하기 위해 설계 되었습니다.  
카테고리와 역할을 생성하고 삭제하는 기능, 스터디 그룹을 관리하는 기능도 포함되어있습니다.  

## 주요 명령어

### 카테고리 관리자(`cogs/admin_palette/category_manager.py`)
| 명령어                          | 설명                                              |
|---------------------------------|--------------------------------------------------|
| `/display_category_list`        | 서버에 있는 모든 카테고리 목록을 표시합니다.       |
| `/create_category <name>`       | 카테고리를 생성하고 역할 및 채널을 만듭니다.       |
| `/delete_category <name>`       | 카테고리와 그 안의 역할 및 채널을 삭제합니다.      |

### 스터디 관리자(`cogs/admin_palette/study_manager.py`)
| 명령어                          | 설명                                              |
|---------------------------------|--------------------------------------------------|
| `/create_study <study_name> <season> [category_name]` | 스터디룸과 역할, 채널을 생성합니다. |
| `/delete_study <study_name> <season>` | 스터디룸을 삭제하고 멤버를 시즌별 참가 역할로 이동시킵니다. |

### 역할 관리자(`cogs/admin_palette/role_manager.py`)
| 명령어                          | 설명                                              |
|---------------------------------|--------------------------------------------------|
| `/add_role <member> <role>`     | 특정 멤버에게 역할을 추가합니다.                  |
| `/remove_role <member> <role>`  | 특정 멤버에게서 역할을 제거합니다.                |

### 서버 관리자(`cogs/server_palette/category_checker.py`)
| 명령어                          | 설명                                              |
|---------------------------------|--------------------------------------------------|
| `/ping`                         | 봇이 살아있는지 확인합니다.                        |
| `/show_categories`              | 구독 가능한 카테고리 목록을 버튼으로 표시합니다.    |

### 엠베서더 관리자(`cogs/server_palette/ambassador_manager.py`)
| 명령어                          | 설명                                              |
|---------------------------------|--------------------------------------------------|
| `/proof_promo <attachment>`     | 엠베서더 프로모션을 증명하는 이미지를 업로드합니다. |
| `/monthly_ranking`			  | 엠베서더의 월간 랭킹을 표시합니다.                |


## 이 프로젝트에 기여하기
만약 이 프로젝트에 기여하고 싶으시다면 [기여자 가이드](CONTRIBUTING.md)를 참고해주세요.  
기여를 하고자 하시는 분들을 언제나 환영하고 있으니 부담없이 참여해주세요.


## 실행 방법
1. 저장소 클론
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


## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.

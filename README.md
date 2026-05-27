# Employee Management System (Python)

> **팀**: D팀 07번 | 3인  
> **과정**: VSCode Python 3 개발자 과정 | 5일 × 8교시  
> **브랜치 전략**: D-07-SPEC | D-07-RED | D-07-GREEN | D-07-REFACTOR

CSV(txt) 파일로 명령을 읽어 사원 DB를 조작한 뒤 결과를 txt 파일로 출력하는 사원 관리 시스템이다.

---

## 팀원 소개

| 이름 | 역할 | 담당 기능 |
|---|---|---|
| 홍길동 | 팀장 | [ADD] 직원 추가 · 파일 I/O |
| 박문수 | 팀원 | [DEL] 직원 삭제 · [CNT] 수 조회 |
| 이순신 | 팀원 | [SCH] 검색 · [MOD] 정보 수정 |

---

## 실행 방법

```bash
python python/main.py input.txt output.txt
```

---

## 가상환경으로 실행하기

### 1. 가상환경 생성

```bash
python -m venv venv
```

### 2. 가상환경 활성화

Windows (CMD):
```cmd
venv\Scripts\activate.bat
```

Windows (PowerShell):
```powershell
venv\Scripts\Activate.ps1
```

Linux / macOS:
```bash
source venv/bin/activate
```

### 3. 의존성 설치

```bash
pip install pytest pytest-cov
```

### 4. 프로그램 실행

```bash
python python/main.py input.txt output.txt
```

### 5. 테스트 실행

```bash
# 전체 테스트
pytest

# 커버리지 포함
pytest --cov=. --cov-report=html
# 커버리지 리포트: htmlcov/index.html
```

### 6. 가상환경 비활성화

```bash
deactivate
```

---

## 프로젝트 구조

```
python/
├── main.py                 # 메인 진입점
├── command_parser.py       # 입력 라인 파싱
├── command_factory.py      # 커맨드 객체 생성
├── commands.py             # 커맨드 클래스 (Add, Delete, Search, Mod, Count)
├── employee.py             # Employee 클래스 (Field 패턴)
├── employee_store.py       # 사원 저장소 구현
├── employee_repository.py  # Repository ABC (인터페이스) — REFACTOR 단계
├── enums.py                # 열거형 (FieldEnum, CombinationEnum 등)
├── field.py                # 필드 클래스 (Name, Birthday, CareerLevel, PhoneNumber, EmployeeNumber, Certi)
├── option_parser.py        # 옵션 파싱 유틸리티
├── result_formatter.py     # 결과 포맷팅
└── token_group.py          # 토큰 그룹

docs/
└── PRD.md                  # 프로젝트 요구사항 정의서

requirement/
├── Base.md                 # 기본 요구사항
└── Further.md              # 추가 요구사항
```

---

## 지원 명령어

| 명령어 | 설명 |
|---|---|
| ADD | 사원 추가 |
| DEL | 사원 삭제 |
| SCH | 사원 검색 |
| MOD | 사원 수정 |
| CNT | 사원 수 조회 |

---

## 옵션

| 옵션 위치 | 옵션 | 설명 | 적용 명령어 |
|---|---|---|---|
| 옵션1 | `-p` | 출력 옵션 (최대 5개 레코드 출력) | SCH / MOD / DEL |
| 옵션2 | `-f` | 성명의 이름(First name)으로 조건 설정 | SCH / DEL / MOD |
| 옵션2 | `-l` | 성명의 성(Last name) 또는 전화번호 뒷자리로 조건 설정 | SCH / DEL / MOD |
| 옵션2 | `-m` | 전화번호 중간자리 또는 생년월일 월로 조건 설정 | SCH / DEL / MOD |
| 옵션2 | `-y` | 생년월일 연도로 조건 설정 | SCH / DEL / MOD |
| 옵션2 | `-d` | 생년월일 일로 조건 설정 | SCH / DEL / MOD |
| 옵션3 | `-g` | 초과 (greater than) | SCH |
| 옵션3 | `-ge` | 이상 (greater than or equal) | SCH |
| 옵션3 | `-s` | 미만 (smaller than) | SCH |
| 옵션3 | `-se` | 이하 (smaller than or equal) | SCH |
| - | `-a` | AND 다중 조건 | SCH / DEL / MOD |
| - | `-o` | OR 다중 조건 | SCH / DEL / MOD |

---

## DB 스키마

| 내부 속성명 | Field 클래스 | 입력 Column명 | 필수 | 설명 | 허용값 |
|---|---|---|---|---|---|
| `employee_number` | `EmployeeNumber` | `employeeNum` | 필수 | 사원번호 · 유일 식별자 | 8자리 숫자 |
| `name` | `Name` | `name` | 필수 | 성명 (이름 성 형식) | 영문 대문자 |
| `career_level` | `CareerLevel` | `cl` | 필수 | 경력개발단계 | CL1 / CL2 / CL3 / CL4 |
| `phone_number` | `PhoneNumber` | `phoneNum` | 필수 | 전화번호 | `010-XXXX-XXXX` |
| `birthday` | `Birthday` | `birthday` | 필수 | 생년월일 | `YYYYMMDD` |
| `certi` | `Certi` | `certi` | 필수 | 자격증 등급 | ADV / PRO / EX |

---

## 요구사항

- Python 3.7 이상
- pytest · pytest-cov

---

## To-Do List

상세 체크리스트는 [TODO.md](.ai/TODO.md)를 기준으로 관리한다.
상태 동기화가 필요할 때는 `python3 .ai/scripts/sync_todo_status.py`를 실행한다.

| 단계 | 브랜치 | 상태 | 주요 작업 |
|---|---|---|---|
| SPEC | D-07-SPEC | 완료| 요구사항 문서화, README/TODO 작성 |
| RED | D-07-RED | 대기| 실패하는 테스트 케이스 작성 및 실패 확인 |
| GREEN | D-07-GREEN | 대기| 실패 테스트를 통과시키는 최소 구현 |
| REFACTOR | D-07-REFACTOR | 대기| 구조 개선, Repository 분리, 네이밍 정리, 커버리지 확인 |
| 최종 제출 | - | 대기| BP.md 작성, 발표 자료 정리, 최종 문서 최신화 |

---

## 브랜치 전략

```
D팀 07번 기준:
  D-07-SPEC      # 요구사항 문서화
  D-07-RED       # 실패하는 테스트 먼저 작성
  D-07-GREEN     # 최소 구현으로 테스트 통과
  D-07-REFACTOR  # Clean Code · 설계 개선
```

> **규칙**: 각 단계 완료 후 PR 생성 → 리뷰 10개 이상 → main 머지

---

## 관련 문서

- [TODO.md](.ai/TODO.md) — 단계별 체크리스트
- [PRD.md](docs/PRD.md) — 프로젝트 요구사항 정의서
- [requirement/Base.md](requirement/Base.md) — 기본 요구사항
- [requirement/Further.md](requirement/Further.md) — 추가 요구사항
- [.ai/CONTEXT.md](.ai/CONTEXT.md) — AI 작업용 프로젝트 컨텍스트
- [.ai/prompts/README.md](.ai/prompts/README.md) — 단계별 AI 프롬프트 목록

# CONTEXT.md — Employee Management System

> **팀**: D팀 07번 | 3인  
> **과정**: VSCode Python 3 개발자 과정 | 5일 × 8교시  
> **작성일**: 2026-05-27  
> **TDD 현황**: SPEC 완료 · RED 대기 · GREEN 대기 · REFACTOR 대기

---

## 1. 프로젝트 개요

CSV(txt) 파일로 명령을 읽어 사원 DB를 조작한 뒤 결과를 txt 파일로 출력하는 CLI 기반 사원 관리 시스템이다.

**실행 방법**:

```bash
python python/main.py input.txt output.txt
```

**처리 흐름**:

```
input.txt 읽기
    → CommandParser  — 입력 라인을 TokenGroup으로 파싱
    → CommandFactory — TokenGroup을 Command 객체로 변환
    → Command.execute(EmployeeStore) — DB 조작
    → ResultFormatter — 출력 문자열 생성
    → output.txt 출력
```

---

## 2. 팀 구성

| 이름 | 역할 | 담당 기능 |
|---|---|---|
| 홍길동 | 팀장 | [ADD] 직원 추가 · 파일 I/O |
| 박문수 | 팀원 | [DEL] 직원 삭제 · [CNT] 수 조회 |
| 이순신 | 팀원 | [SCH] 검색 · [MOD] 정보 수정 |

---

## 3. TDD 단계 현황

| 단계 | 브랜치 | 상태 |
|---|---|---|
| SPEC | D-07-SPEC | 완료|
| RED | D-07-RED | 대기|
| GREEN | D-07-GREEN | 대기|
| REFACTOR | D-07-REFACTOR | 대기|
> **주의**: 현재는 SPEC 단계만 완료된 상태이다. 다음 단계에서는 RED 테스트 케이스를 먼저 작성하고 실패를 확인한 뒤 GREEN 구현으로 진행한다.

---

## 4. 프로젝트 구조

```
python/
├── main.py                 # 메인 진입점 — 파일 I/O · 명령어 루프
├── command_parser.py       # CommandParser — 입력 라인 → TokenGroup
├── command_factory.py      # build_command() — TokenGroup → Command
├── commands.py             # AddCommand / DeleteCommand / SearchCommand / ModCommand / CountCommand
├── employee.py             # Employee 클래스 (Field 패턴)
├── employee_store.py       # EmployeeStore — 사원 저장소 구현
├── employee_repository.py  # EmployeeRepository ABC — REFACTOR 단계 작업
├── enums.py                # FieldEnum / CombinationEnum / PrimaryOptionEnum / SecondaryOptionEnum
├── field.py                # Field 서브클래스 + TertiaryOptionEnum
├── option_parser.py        # OptionParser / get_field_index_from_option()
├── result_formatter.py     # format_employee_list_with_print() / format_employee_list_count()
└── token_group.py          # TokenGroup

docs/
└── PRD.md

requirement/
├── Base.md
└── Further.md
```

---

## 5. DB 스키마

### Employee 클래스

```python
# python/employee.py
class Employee:
    def __init__(self, employee_number: str, name: str, career_level: str,
                 phone_number: str, birthday: str, certi: str):
        self.employee_number = EmployeeNumber(employee_number)
        self.name = Name(name)
        self.career_level = CareerLevel(career_level)
        self.phone_number = PhoneNumber(phone_number)
        self.birthday = Birthday(birthday)
        self.certi = Certi(certi)
```

### 필드 정의

| 내부 속성명 | Field 클래스 | 입력 Column명 | 허용값 |
|---|---|---|---|
| `employee_number` | `EmployeeNumber` | `employeeNum` | 8자리 숫자 |
| `name` | `Name` | `name` | 영문 대문자, `이름 성` 형식 |
| `career_level` | `CareerLevel` | `cl` | CL1 / CL2 / CL3 / CL4 |
| `phone_number` | `PhoneNumber` | `phoneNum` | `010-XXXX-XXXX` |
| `birthday` | `Birthday` | `birthday` | `YYYYMMDD` |
| `certi` | `Certi` | `certi` | ADV / PRO / EX |

### Invariant (불변 규칙)

- `employee_number`는 DB 내에서 유일하다.
- 6개 필드 모두 필수이다.
- `employee_number`는 수정할 수 없다. 위반 시 `ValueError`를 발생시킨다.
- `career_level`은 CL1~CL4 범위만 허용한다. 위반 시 `ValueError`를 발생시킨다.
- 사원번호 앞 두 자리는 입사년도를 의미한다. `90XXXXXX`(1990년) ~ `19XXXXXX`(2019년).

---

## 6. 명령어 및 옵션

### 명령어

| 명령어 | 클래스 | 출력 (-p 없음) | 출력 (-p 있음) | 결과 없음 |
|---|---|---|---|---|
| ADD | `AddCommand` | 없음 | 없음 | 없음 |
| DEL | `DeleteCommand` | `DEL,건수` | 삭제 전 레코드 최대 5건 | `DEL,NONE` |
| SCH | `SearchCommand` | `SCH,건수` | 검색 결과 최대 5건 | `SCH,NONE` |
| MOD | `ModCommand` | `MOD,건수` | 수정 전 레코드 최대 5건 | `MOD,NONE` |
| CNT | `CountCommand` | `CNT,건수` | 미지원 | 없음 |

### 옵션 구조

| 옵션 위치 | 열 위치 (0-based) | 옵션 | 설명 |
|---|---|---|---|
| 옵션1 | tokens[1] | `-p` | 출력 옵션 |
| 옵션2 | tokens[2] | `-f` / `-l` / `-m` / `-y` / `-d` | 서브필드 선택 |
| 옵션3 | tokens[3] | `-g` / `-ge` / `-s` / `-se` | 부등호 비교 (SCH 전용) |
| AND/OR | params 내 | `-a` / `-o` | 다중 조건 |

### 서브필드 인덱스 (get_field_index_from_option 기준)

| Field | 옵션2 | 인덱스 | 설명 |
|---|---|---|---|
| `Name` | (없음) | 0 | 성명 전체 |
| `Name` | `-f` | 1 | 이름(First name) |
| `Name` | `-l` | 2 | 성(Last name) |
| `PhoneNumber` | (없음) | 0 | 전화번호 전체 |
| `PhoneNumber` | `-m` | 2 | 중간자리 |
| `PhoneNumber` | `-l` | 3 | 뒷자리 |
| `Birthday` | (없음) | 0 | 생년월일 전체 |
| `Birthday` | `-y` | 1 | 연도 |
| `Birthday` | `-m` | 2 | 월 |
| `Birthday` | `-d` | 3 | 일 |

---

## 7. 핵심 클래스 인터페이스

### EmployeeStore

```python
store = EmployeeStore()

store.add(employee: Employee) -> None
store.count() -> int
store.search(field: FieldEnum, value: str,
             tertiary_option: TertiaryOptionEnum,
             subfield_index: int = 0) -> List[Employee]
store.search_and_or(field1, value1, tertiary1, subfield_index1,
                    combination: CombinationEnum,
                    field2, value2, tertiary2, subfield_index2) -> List[Employee]
store.delete(field: FieldEnum, value: str,
             subfield_index: int = 0) -> List[Employee]
store.delete_and_or(...) -> List[Employee]
store.modify(field: FieldEnum, value: str,
             modify_field: FieldEnum, modify_value: str,
             subfield_index: int = 0) -> List[Employee]
store.modify_and_or(...) -> List[Employee]
```

> **주의**: `delete()` / `modify()`는 처리된 레코드 목록을 반환한다. 건수는 `len(result)`로 계산한다.

> **주의**: `modify()`는 수정 전 레코드를 반환한다.

### ResultFormatter

```python
# -p 옵션 있음 — 레코드 라인 반환 (건수 라인 없음)
format_employee_list_with_print(employee_list, command_type, count=5) -> List[str]

# -p 옵션 없음 — 건수 또는 NONE 반환
format_employee_list_count(employee_list, command_type) -> List[str]
```

### FieldEnum (TC 작성 시 참조)

```python
FieldEnum.FIELD_EMPLOYEE_NUMBER  # employeeNum
FieldEnum.FIELD_NAME             # name
FieldEnum.FIELD_CAREER_LEVEL     # cl
FieldEnum.FIELD_PHONE_NUMBER     # phoneNum
FieldEnum.FIELD_BIRTH_DAY        # birthday
FieldEnum.FIELD_CERTI            # certi
```

---

## 8. 출력 포맷

### 레코드 출력 형식

```
{명령어},{사원번호},{성명},{경력개발단계},{전화번호},{생년월일},{certi}
```

예시:
```
SCH,90000001,EUGOLQ ZAH,CL3,010-6047-7840,20061016,EX
MOD,15123456,GILDONG HONG,CL3,010-1234-5678,19900101,ADV
```

### 출력 정렬 기준

사원번호 기준 입사년도 오름차순 정렬. `90XXXXXX`(1990년대)가 `00XXXXXX`(2000년대)보다 앞선다.

---

## 9. .ai/ 디렉토리 구조

```
.ai/
├── CONTEXT.md              # 이 파일 — 프로젝트 전체 컨텍스트
├── rules/                  # AI 행동 규칙
├── skills/                 # TC 작성 · BP 작성 · 코드 리뷰 스킬
├── knowledge/              # 스키마 · 명령어 레퍼런스
├── guides/                 # 강의 가이드 문서
├── sessions/               # 세션별 작업 컨텍스트
├── prompts/                # 단계별 프롬프트
└── logs/                   # 세션별 작업 일지
```

---

## 10. 관련 문서

| 파일 | 설명 |
|---|---|
| `docs/PRD.md` | 프로젝트 요구사항 정의서 (실제 코드 기준) |
| `README.md` | 실행 방법 · To-Do List |
| `.ai/TODO.md` | 단계별 체크박스 목록 |
| `requirement/Base.md` | 기본 요구사항 원문 |
| `requirement/Further.md` | 추가 요구사항 원문 |
| `.ai/prompts/README.md` | 프롬프트 파일 목록 |
| `.ai/sessions/README.md` | 세션 컨텍스트 운영 규칙 |
| `.ai/logs/README.md` | 작업 일지 운영 규칙 |

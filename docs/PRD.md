# PRD — Employee Management System

> **프로젝트**: Employee Management System (사원 관리 DB)  
> **팀**: D팀 07번 | 3인  
> **브랜치**: D-07-SPEC  
> **작성일**: 2026-05-27  
> **버전**: 1.1

---

## 목차

1. [프로젝트 목적 및 배경](#1-프로젝트-목적-및-배경)
2. [시스템 개요](#2-시스템-개요)
3. [기능 요구사항](#3-기능-요구사항)
4. [비기능 요구사항](#4-비기능-요구사항)
5. [DB 스키마 정의](#5-db-스키마-정의)
6. [입출력 형식](#6-입출력-형식)
7. [제약사항 및 가정](#7-제약사항-및-가정)

---

## 1. 프로젝트 목적 및 배경

본 시스템은 사원 정보를 파일 기반으로 관리하는 사원 관리 DB이다. CSV 형식의 txt 파일로 명령을 읽어 사원 DB를 조작한 뒤 결과를 txt 파일로 출력하는 CLI 기반 시스템을 구현한다.

**개발 목적**:

- TDD(Test-Driven Development) 실습을 통한 소프트웨어 품질 향상
- RED → GREEN → REFACTOR 사이클 체득
- 팀 협업 및 코드 리뷰 역량 강화

**배경**:

기업 현장에서 사원 정보를 체계적으로 관리하기 위한 최소 기능 시스템을 설계한다. 영속성은 CSV(txt) 파일로 확보하며, 명령어 기반 인터페이스로 조회 · 추가 · 수정 · 삭제 기능을 제공한다.

---

## 2. 시스템 개요

```
입력 (input.txt)          시스템                  출력 (output.txt)
CSV 명령어 파일    →    Employee Management    →    처리 결과 파일
                          System (Python 3)
```

**실행 방법**:

```bash
python python/main.py input.txt output.txt
```

**처리 흐름**:

```
input.txt 읽기
    → 명령어 파싱 (CommandParser)
    → 커맨드 객체 생성 (CommandFactory)
    → DB 조작 (EmployeeStore)
    → 결과 포맷팅 (ResultFormatter)
    → output.txt 출력
```

---

## 3. 기능 요구사항

### 3.1 [ADD] 직원 추가

직원 정보를 DB에 추가한다.

**입력 형식**:

```
ADD,옵션1,옵션2,옵션3,사원번호,성명,경력개발단계,전화번호,생년월일,certi
```

**처리 규칙**:

- 사원번호는 유일 식별자이다. 중복 시 추가하지 않는다.
- 필수 필드 6종(사원번호 · 성명 · 경력개발단계 · 전화번호 · 생년월일 · certi)이 모두 존재해야 한다.
- ADD 명령어는 출력을 사용하지 않는다.

**출력 형식**:

```
# 출력 없음 (ADD는 결과를 출력하지 않는다)
```

**TC 예시**:

```python
def test_add_employee():
    store = EmployeeStore()
    emp = Employee("15123456", "GILDONG HONG", "CL3", "010-1234-5678", "19900101", "ADV")
    store.add(emp)
    result = store.search(FieldEnum.FIELD_EMPLOYEE_NUMBER, "15123456",
                          TertiaryOptionEnum.NONE)
    assert len(result) == 1
    assert result[0].name.to_string() == "GILDONG HONG"
```

---

### 3.2 [DEL] 직원 삭제

조건에 부합하는 직원을 DB에서 삭제한다.

**입력 형식**:

```
DEL,옵션1,옵션2,옵션3,조건 Column명,조건 값
```

**처리 규칙**:

- 조건에 부합하는 레코드를 모두 삭제한다.
- 조건에 맞는 직원이 없을 경우 `DEL,NONE`을 출력한다.
- `-p` 옵션이 없으면 삭제 건수를 출력한다.
- `-p` 옵션이 있으면 삭제된 레코드를 최대 5건 출력한다.
- 출력 순서는 사원번호 기준 입사년도가 빠른 순서로 정렬한다.

**출력 형식**:

```
# -p 옵션 없음 (결과 있음)
DEL,삭제건수

# -p 옵션 있음 (최대 5건)
DEL,사원번호,성명,경력개발단계,전화번호,생년월일,certi

# 조건에 부합하는 레코드 없음 (-p 여부 무관)
DEL,NONE
```

**TC 예시**:

```python
def test_delete_by_employee_number():
    store = EmployeeStore()
    store.add(Employee("15123456", "GILDONG HONG", "CL3", "010-1234-5678", "19900101", "ADV"))
    deleted = store.delete(FieldEnum.FIELD_EMPLOYEE_NUMBER, "15123456")
    assert len(deleted) == 1
    result = store.search(FieldEnum.FIELD_EMPLOYEE_NUMBER, "15123456",
                          TertiaryOptionEnum.NONE)
    assert len(result) == 0

def test_delete_nonexistent():
    store = EmployeeStore()
    deleted = store.delete(FieldEnum.FIELD_EMPLOYEE_NUMBER, "99999999")
    assert len(deleted) == 0
```

---

### 3.3 [SCH] 직원 검색

조건에 부합하는 직원을 검색한다.

**입력 형식**:

```
SCH,옵션1,옵션2,옵션3,조건 Column명,조건 값
SCH,옵션1,옵션2,-g,조건 Column명,조건 값    # 초과 (greater than)
SCH,옵션1,옵션2,-ge,조건 Column명,조건 값   # 이상 (greater than or equal)
SCH,옵션1,옵션2,-s,조건 Column명,조건 값    # 미만 (smaller than)
SCH,옵션1,옵션2,-se,조건 Column명,조건 값   # 이하 (smaller than or equal)

# AND/OR 다중 조건
SCH,옵션1,옵션2-1,옵션3-1,Column1,값1,-a,옵션2-2,옵션3-2,Column2,값2
SCH,옵션1,옵션2-1,옵션3-1,Column1,값1,-o,옵션2-2,옵션3-2,Column2,값2
```

**처리 규칙**:

- 검색 가능한 필드: 사원번호 · 성명 · 경력개발단계 · 전화번호 · 생년월일 · certi
- 부등호 옵션(`-g` / `-ge` / `-s` / `-se`)은 옵션3 위치에서 적용된다.
- `-a`(AND) / `-o`(OR) 다중 조건을 지원한다. OR 조건에서 중복 레코드는 한 번만 출력한다.
- 검색 결과가 없으면 `-p` 옵션 적용 여부에 관계없이 `SCH,NONE`을 출력한다.
- `-p` 옵션이 없으면 검색 건수만 출력한다.
- `-p` 옵션이 있으면 최대 5건의 상세 정보를 출력한다. 5건 초과 시 입사년도가 빠른 상위 5건만 출력한다.

**출력 형식**:

```
# -p 옵션 없음 (결과 있음)
SCH,검색건수

# -p 옵션 있음 (최대 5건)
SCH,사원번호,성명,경력개발단계,전화번호,생년월일,certi

# 검색 결과 없음 (-p 여부 무관)
SCH,NONE
```

**TC 예시**:

```python
@pytest.mark.parametrize("name, expected_count", [
    ("GILDONG HONG", 1),
    ("MUNSU PARK", 1),
    ("UNKNOWN NAME", 0),
])
def test_search_by_name(store_with_data, name, expected_count):
    result = store_with_data.search(FieldEnum.FIELD_NAME, name,
                                    TertiaryOptionEnum.NONE)
    assert len(result) == expected_count

def test_search_by_birthday_greater_than():
    result = store.search(FieldEnum.FIELD_BIRTH_DAY, "19900101",
                          TertiaryOptionEnum.G)
    assert all(e.birthday.to_string() > "19900101" for e in result)
```

---

### 3.4 [MOD] 직원 정보 수정

조건에 부합하는 직원의 정보를 수정한다.

**입력 형식**:

```
MOD,옵션1,옵션2,옵션3,조건 Column명,조건 값,변경할 Column명,변경할 값

# AND/OR 다중 조건
MOD,옵션1,옵션2-1,옵션3-1,Column1,값1,-a,옵션2-2,옵션3-2,Column2,값2,변경Column,변경값
MOD,옵션1,옵션2-1,옵션3-1,Column1,값1,-o,옵션2-2,옵션3-2,Column2,값2,변경Column,변경값
```

**처리 규칙**:

- 조건에 부합하는 레코드를 모두 수정한다.
- 사원번호(`employeeNum`)는 수정할 수 없다 (불변 규칙).
- 한 명령어에 하나의 Column 값만 변경할 수 있다.
- 조건에 맞는 직원이 없으면 `MOD,NONE`을 출력한다.
- `-p` 옵션이 없으면 수정 건수를 출력한다.
- `-p` 옵션이 있으면 수정되기 **전**의 레코드를 최대 5건 출력한다.
- 출력 순서는 사원번호 기준 입사년도가 빠른 순서로 정렬한다.

**출력 형식**:

```
# -p 옵션 없음 (결과 있음)
MOD,수정건수

# -p 옵션 있음 (수정 전 레코드, 최대 5건)
MOD,사원번호,성명,경력개발단계,전화번호,생년월일,certi

# 조건에 부합하는 레코드 없음 (-p 여부 무관)
MOD,NONE
```

**TC 예시**:

```python
def test_modify_phone():
    store = EmployeeStore()
    store.add(Employee("15123456", "GILDONG HONG", "CL3", "010-1234-5678", "19900101", "ADV"))
    modified = store.modify(FieldEnum.FIELD_EMPLOYEE_NUMBER, "15123456",
                            FieldEnum.FIELD_PHONE_NUMBER, "010-9999-0000")
    assert len(modified) == 1
    result = store.search(FieldEnum.FIELD_EMPLOYEE_NUMBER, "15123456",
                          TertiaryOptionEnum.NONE)
    assert result[0].phone_number.to_string() == "010-9999-0000"

def test_modify_immutable_pk():
    store = EmployeeStore()
    store.add(Employee("15123456", "GILDONG HONG", "CL3", "010-1234-5678", "19900101", "ADV"))
    with pytest.raises(ValueError):
        store.modify(FieldEnum.FIELD_EMPLOYEE_NUMBER, "15123456",
                     FieldEnum.FIELD_EMPLOYEE_NUMBER, "99999999")
```

---

### 3.5 [CNT] 수 조회

전체 직원 수를 조회한다.

**입력 형식**:

```
CNT, , ,
```

**처리 규칙**:

- 전체 레코드 수를 반환한다.

**출력 형식**:

```
CNT,조회건수
```

**TC 예시**:

```python
def test_count_all():
    store = EmployeeStore()
    store.add(Employee("15123456", "GILDONG HONG", "CL3", "010-1234-5678", "19900101", "ADV"))
    store.add(Employee("15123457", "MUNSU PARK", "CL2", "010-2222-3333", "19921010", "PRO"))
    assert store.count() == 2

def test_count_empty():
    store = EmployeeStore()
    assert store.count() == 0
```

---

## 4. 비기능 요구사항

### 4.1 성능

- 최소 10만 개의 레코드를 처리할 수 있어야 한다.
- 단일 명령어 처리 시간 제한 없음 (교육 과정 기준)

### 4.2 파일 I/O

- 입력 파일 인코딩: UTF-8
- 출력 파일 인코딩: UTF-8
- 파일 형식: CSV(`,` 구분자) txt
- 줄바꿈: `\n`

### 4.3 입력 유효성 검증

| 필드 | Column명 | 형식 | 검증 규칙 |
|---|---|---|---|
| 사원번호 | `employeeNum` | 8자리 숫자 | `^\d{8}$` |
| 성명 | `name` | `이름 성` | 영문 대문자, 공백 1개로 구분 |
| 경력개발단계 | `cl` | CL1 / CL2 / CL3 / CL4 | 열거형 범위 검증 |
| 전화번호 | `phoneNum` | `010-XXXX-XXXX` | `^010-\d{4}-\d{4}$` |
| 생년월일 | `birthday` | `YYYYMMDD` | `^\d{8}$` |
| 자격증 | `certi` | ADV / PRO / EX | 열거형 범위 검증 |

### 4.4 옵션 목록

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

### 4.5 테스트

- 테스트 프레임워크: `pytest`
- 커버리지 도구: `pytest-cov`
- 목표 커버리지: 80% 이상

---

## 5. DB 스키마 정의

### `Employee` 클래스

각 필드는 `Field` 서브클래스로 구현되어 비교 연산 및 서브필드 접근을 지원한다.

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

| 내부 속성명 | Field 클래스 | 입력 Column명 | 필수 | 설명 | 허용값 |
|---|---|---|---|---|---|
| `employee_number` | `EmployeeNumber` | `employeeNum` | 필수 | 사원번호 · 유일 식별자 | 8자리 숫자 |
| `name` | `Name` | `name` | 필수 | 성명 (이름 성 형식) | 영문 대문자 |
| `career_level` | `CareerLevel` | `cl` | 필수 | 경력개발단계 | CL1 / CL2 / CL3 / CL4 |
| `phone_number` | `PhoneNumber` | `phoneNum` | 필수 | 전화번호 | `010-XXXX-XXXX` |
| `birthday` | `Birthday` | `birthday` | 필수 | 생년월일 | `YYYYMMDD` |
| `certi` | `Certi` | `certi` | 필수 | 자격증 등급 | ADV / PRO / EX |

### 서브필드 인덱스

| Field 클래스 | 옵션2 | 서브필드 인덱스 | 설명 |
|---|---|---|---|
| `Name` | (없음) | 0 | 성명 전체 비교 |
| `Name` | `-f` | 1 | 이름(First name) |
| `Name` | `-l` | 2 | 성(Last name) |
| `PhoneNumber` | (없음) | 0 | 전화번호 전체 비교 |
| `PhoneNumber` | `-m` | 2 | 중간자리 |
| `PhoneNumber` | `-l` | 3 | 뒷자리 |
| `Birthday` | (없음) | 0 | 생년월일 전체 비교 |
| `Birthday` | `-y` | 1 | 연도 |
| `Birthday` | `-m` | 2 | 월 |
| `Birthday` | `-d` | 3 | 일 |

### Invariant (불변 규칙)

- `employee_number`는 DB 내에서 유일하다.
- 필수 필드 6종은 반드시 존재해야 한다.
- `certi` 값은 `ADV` / `PRO` / `EX` 중 하나여야 한다.
- `employee_number`는 수정할 수 없다.
- 사원번호 앞 두 자리는 입사년도를 의미한다. `90XXXXXX`(1990년) ~ `19XXXXXX`(2019년).

---

## 6. 입출력 형식

### 6.1 입력 파일 형식 (`input.txt`)

```
ADD, , , ,15123456,GILDONG HONG,CL3,010-1234-5678,19900101,ADV
ADD, , , ,15123457,MUNSU PARK,CL2,010-2222-3333,19921010,PRO
SCH, , , ,name,GILDONG HONG
SCH,-p, ,-ge,birthday,19900101
MOD, , , ,employeeNum,15123456,phoneNum,010-9999-0000
DEL, , , ,name,MUNSU PARK
CNT, , ,
```

### 6.2 출력 파일 형식 (`output.txt`)

```
# SCH, , , ,name,GILDONG HONG  (-p 없음, 1건)
SCH,1

# SCH,-p, ,-ge,birthday,19900101  (-p 있음, 2건)
SCH,15123456,GILDONG HONG,CL3,010-1234-5678,19900101,ADV
SCH,15123457,MUNSU PARK,CL2,010-2222-3333,19921010,PRO

# MOD, , , ,employeeNum,15123456,phoneNum,010-9999-0000  (-p 없음)
MOD,1

# DEL, , , ,name,MUNSU PARK  (-p 없음)
DEL,1

# CNT, , ,
CNT,1
```

### 6.3 출력 옵션 규칙

| 조건 | `-p` 없음 | `-p` 있음 |
|---|---|---|
| 결과 0건 | `{명령어},NONE` | `{명령어},NONE` |
| 결과 1~5건 | `{명령어},{건수}` | 레코드 전체 출력 |
| 결과 6건 이상 | `{명령어},{건수}` | 입사년도 빠른 순 상위 5건 출력 |

> **주의**: `-p` 옵션 적용 시 건수 라인을 별도로 출력하지 않는다. 레코드 라인만 출력한다.

> **주의**: MOD 명령어에서 `-p` 옵션 적용 시 수정되기 **전**의 레코드를 출력한다.

---

## 7. 제약사항 및 가정

**제약사항**:

- 최소 10만 개의 레코드를 처리할 수 있어야 한다.
- 영속성은 CSV(txt) 파일로만 확보한다. 별도 DB 사용 불가.
- 구현 언어는 Python 3으로 한정한다.
- 테스트는 pytest만 사용한다.

**가정**:

- 입력 파일은 UTF-8 인코딩으로 제공된다.
- 사원번호는 항상 8자리 숫자 형식으로 입력된다.
- 동일 사원번호의 중복 ADD 명령은 무시한다.
- 검색 · 삭제 · 수정 결과가 없는 경우 `NONE`을 출력한다.

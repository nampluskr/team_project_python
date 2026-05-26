# 팀 프로젝트 — Employee Management System

> **대상 과정**: VSCode Python 3 개발자 과정  
> **기간**: 5일 × 8교시  
> **구성**: 1팀 3인 | 팀 내 Code Review 필수 | TDD Practice 필수 | Commit 50줄 이하 권장

---

## 목차

1. [프로젝트 개요](#1-프로젝트-개요)
2. [5일 일정 타임라인](#2-5일-일정-타임라인)
3. [요구사항 및 채점 기준](#3-요구사항-및-채점-기준)
4. [SPEC 단계](#4-spec-단계)
5. [RED 단계](#5-red-단계)
6. [GREEN 단계](#6-green-단계)
7. [REFACTOR 단계](#7-refactor-단계)
8. [요구사항 추적성 (TRACEABILITY)](#8-요구사항-추적성-traceability)
9. [PR 리뷰 가이드 및 커밋 전략](#9-pr-리뷰-가이드-및-커밋-전략)
10. [VSCode 개발 환경 설정 및 핵심 구현](#10-vscode-개발-환경-설정-및-핵심-구현)
11. [BP 문서 작성 및 팀 발표 가이드](#11-bp-문서-작성-및-팀-발표-가이드)
12. [핵심 요약](#12-핵심-요약)

---

## 1. 프로젝트 개요

**프로젝트명**: Employee Management System (사원 관리 DB)

CSV(txt) 파일 형식으로 명령을 읽어 사원 DB를 조작한 뒤 결과를 txt 파일로 출력하는 시스템이다.

**TDD 사이클 구조**:

```
SPEC 단계            RED 단계              GREEN 단계           REFACTOR 단계
요구사항 · PRD  →   실패하는           →   최소 구현으로    →   품질 · 설계
To-Do              테스트 먼저            테스트 통과             개선
```

**추적성 원칙**:

```
Invariant → UI Contract Test → Domain Test → Implementation Unit
```

**채점 구성 (총 500점)**:

| 항목 | 배점 |
|---|---|
| 요구사항 평가 | 100점 |
| S/W 품질 평가 | 400점 |
| BP 발표 | 100점 |
| **총점** | **500점** |

---

## 2. 5일 일정 타임라인

### 전체 일정

| 일차 | 교시 | 내용 |
|---|---|---|
| 1일차 | 1~4교시 | TeamProject OT / 팀 빌딩 및 그라운드 룰 |
| 1일차 | 5~8교시 | Base code 및 요구사항 분배 |
| 1일차 | 5~8교시 | SPEC: PRD.md · README / To-Do List 작성 |
| 2일차 | 1~4교시 | PHASE 1 — RED: 실패하는 테스트 먼저 작성 |
| 2일차 | 4~8교시 | 요구사항별 TC 작성 / Test 커밋 |
| 3일차 | 1~4교시 | PHASE 2 — GREEN: 최소 구현으로 테스트 통과 |
| 3일차 | 4~8교시 | 구현 완성 · PR Review / pytest 통과 확인 |
| 4일차 | 1~4교시 | PHASE 3 — REFACTOR: Clean Code · 설계 개선 |
| 4일차 | 4~8교시 | 통합 · BP 문서 작성 / 최종 빌드 검증 |
| 5일차 | 1~5교시 | 팀 프로젝트 회고 / 발표 자료 정리 |
| 5일차 | 6~8교시 | 팀별 발표 (BP 포함) |

> **결론**: 각 단계를 일차별로 엄격히 구분하여 진행하며, Invariant → UI Contract Test → Domain Test → Implementation Unit 추적성을 유지한다.

---

## 3. 요구사항 및 채점 기준

### 프로젝트 기본 요구사항

**시스템 구현**
- Python 3 사원 관리 DB 구현
- 필수 필드: 직원번호 · 성명 · 직급 · 전화번호 · 생년월일
- CSV(txt) 파일 기반 영속성

**팀 구성**
- 1팀 3인 구성
- 팀 내 코드 리뷰 필수
- GitHub Organization + Repository 사용

**TDD Practice**
- RED → GREEN → REFACTOR 사이클 엄수
- 테스트 프레임워크: pytest

**커밋 규칙**
- 커밋 50줄 이하 권장
- 작은 단위로 자주 커밋
- Conventional Commits 형식 준수
- 여러 커밋 → 하나의 PR 가능

**브랜치 및 제출**
- Release 브랜치 형식: `D팀-07번-RED` / `GREEN` / `REFACTOR`
- 단계별 PR & Review 필수

---

### 채점 항목 (총 500점)

#### 요구사항 평가 — 100점

| 항목 | 배점 |
|---|---|
| `docs/PRD.md` 파일 유/무 | 25점 |
| `README.md` 파일 유/무 | 25점 |
| To-Do List 정리 유/무 | 50점 |

#### S/W 품질 평가 — 400점

| 항목 | 배점 |
|---|---|
| 테스트 코드 유/무 | 100점 |
| 단계별 브랜치 4개 × 50점 | 200점 |
| 단계별 PR 리뷰 10개 이상 × 50점 | 200점 |

#### BP 평가 — 100점

| 항목 | 배점 |
|---|---|
| 프로젝트 내 BP 문서 유/무 | 50점 |
| BP 발표 유/무 | 50점 |

---

## 4. SPEC 단계

**목표**: 요구사항 문서화  
**브랜치**: `팀-번호-SPEC`

### Repository & 브랜치 전략

```bash
# Python 프로젝트 — Git 브랜치 설정
# Organization: TeamProject_D팀
# Description: #7팀, 홍길동, 박문수, 이순신 (3인)

git checkout -b D-07-SPEC      # SPEC 단계
git checkout -b D-07-RED       # RED 단계
git checkout -b D-07-GREEN     # GREEN 단계
git checkout -b D-07-REFACTOR  # REFACTOR 단계

# main merge 시 PR & Review 필수
# PR 당 리뷰 10개 이상 달성 목표
```

---

### 필수 문서 3종 (채점 항목 ① — 100점)

#### `docs/PRD.md` (25점)

- 프로젝트 목적 & 배경
- Python 기능 요구사항 목록
- 비기능 요구사항 (성능 · 보안)
- DB 스키마 정의 (`@dataclass Employee`)

#### `README.md` (25점)

- 프로젝트 개요 · 팀원 소개
- Python 실행 방법 (pytest)
- 디렉토리 구조 & To-Do List

#### To-Do List (50점)

- 요구사항별 체크박스 목록
- 우선순위 & 담당자 배정
- 완료 여부 실시간 갱신
- `README.md` 내 포함 필수

---

### To-Do List 형식 예시 (`README.md`)

```markdown
## To-Do List

| 요구사항        | 담당자 | 단계  | 상태 | 브랜치       |
|---|---|---|---|---|
| [ADD] 직원 추가 | 홍길동 | GREEN |      | D-07-GREEN  |
| [DEL] 직원 삭제 | 박문수 | RED   |      | D-07-RED    |
| [SCH] 이름 검색 | 이순신 | SPEC  |      | -           |
| [MOD] 정보 수정 | 이순신 | SPEC  |      | -           |
| [CNT] 수 조회   | 팀원   | SPEC  |      | -           |
```

**실제 TODO 항목 예시**:

```markdown
- [ ] certi column 추가 구현 & TC
- [ ] -p 출력 옵션: 최대 5개 / NONE
- [ ] MOD 기능 TC & 구현
- [ ] SCH 3옵션 부등호 (-g, -ge, -s, -se)
- [ ] AND/OR 다중 조건 (-a, -o)
```

**SPEC 커밋 메시지 예시**:

```bash
git commit -m "docs: PRD.md Python 요구사항 초안"
git commit -m "docs: README.md To-Do List 추가"
```

---

## 5. RED 단계

**목표**: 구현 없이 테스트 코드만 작성 → 테스트 실패 확인 → 커밋  
**브랜치**: `팀-번호-RED`

> **주의**: 테스트가 실패하는 상태 그대로 커밋하는 것이 TDD의 시작이다.

---

### Python — pytest RED 단계

```python
# test_employee_manager.py (RED — 구현 없이)
import pytest
from employee_manager import EmployeeManager  # <- 미구현 -> ImportError


class TestEmployeeManager:

    def setup_method(self):
        self.manager = EmployeeManager()  # <- ImportError

    # [ADD] TC
    def test_should_find_employee_when_added(self):
        emp = {
            "employee_no": "15123456",
            "name": "홍길동",
            "position": "CL3",
            "phone": "010-1234-5678",
            "birthday": "19900101",
        }
        self.manager.add(emp)
        result = self.manager.find_by_no("15123456")
        assert result is not None
        assert result["name"] == "홍길동"

    # [DEL] TC
    def test_should_not_find_when_deleted(self):
        emp = {
            "employee_no": "15123456",
            "name": "홍길동",
            "position": "CL3",
            "phone": "010-1234-5678",
            "birthday": "19900101",
        }
        self.manager.add(emp)
        deleted = self.manager.delete_by_no("15123456")
        assert deleted == 1
        assert self.manager.find_by_no("15123456") is None

    # [SCH] TC
    def test_should_find_by_name(self):
        self.manager.add({"employee_no": "15123456", "name": "홍길동",
                          "position": "CL3", "phone": "010-1234-5678", "birthday": "19900101"})
        result = self.manager.find_by_name("홍길동")  # <- 미구현 -> FAIL
        assert len(result) == 1

    # [MOD] TC
    def test_should_modify_phone(self):
        self.manager.add({"employee_no": "15123456", "name": "홍길동",
                          "position": "CL3", "phone": "010-1234-5678", "birthday": "19900101"})
        count = self.manager.modify_phone("15123456", "010-9999-0000")  # <- 미구현 -> FAIL
        assert count == 1

    # [CNT] TC
    def test_should_count_all(self):
        self.manager.add({"employee_no": "15123456", "name": "홍길동",
                          "position": "CL3", "phone": "010-1234-5678", "birthday": "19900101"})
        self.manager.add({"employee_no": "15123457", "name": "박문수",
                          "position": "CL2", "phone": "010-2222-3333", "birthday": "19921010"})
        assert self.manager.count() == 2  # <- 미구현 -> FAIL

# pytest -> FAIL -> 커밋
```

**`@pytest.mark.parametrize` 활용 — SCH 다중 조건 TC**:

```python
# test_employee_search.py (RED — parametrize 활용)
import pytest
from employee_manager import EmployeeManager


@pytest.fixture
def manager_with_data():
    manager = EmployeeManager()
    manager.add({"employee_no": "15123456", "name": "홍길동",
                 "position": "CL3", "phone": "010-1234-5678", "birthday": "19900101"})
    manager.add({"employee_no": "15123457", "name": "박문수",
                 "position": "CL2", "phone": "010-2222-3333", "birthday": "19921010"})
    return manager


@pytest.mark.parametrize("name, expected_count", [
    ("홍길동", 1),
    ("박문수", 1),
    ("없는사람", 0),
])
def test_find_by_name(manager_with_data, name, expected_count):
    result = manager_with_data.find_by_name(name)  # <- 미구현 -> FAIL
    assert len(result) == expected_count

# pytest -> FAIL -> 커밋
```

**RED 커밋 메시지 예시**:

```bash
git commit -m "test: [ADD] 직원 추가 TC — RED"
git commit -m "test: [DEL] 직원 삭제 TC — RED"
git commit -m "test: [SCH] 이름 검색 TC — RED"
git commit -m "test: [MOD] 정보 수정 TC — RED"
git commit -m "test: [CNT] 수 조회 TC — RED"
```

---

## 6. GREEN 단계

**목표**: 테스트가 통과하는 최소한의 코드 작성 — 품질보다 통과 우선, 중복·하드코딩 허용  
**브랜치**: `팀-번호-GREEN`

---

### Python — 최소 구현 GREEN

#### `employee.py`

```python
# employee.py
from dataclasses import dataclass, field


@dataclass
class Employee:
    employee_no: str
    name: str
    position: str
    phone: str
    birthday: str
    certi: str = ""  # certi 필드 (README TODO 반영)
```

#### `employee_manager.py`

```python
# employee_manager.py
from typing import Optional
from employee import Employee


class EmployeeManager:
    def __init__(self):
        self._db: list[dict] = []

    # [ADD]
    def add(self, emp: dict) -> None:
        self._db.append(emp)

    def find_by_no(self, employee_no: str) -> Optional[dict]:
        for e in self._db:
            if e["employee_no"] == employee_no:
                return e
        return None

    # [DEL]
    def delete_by_no(self, employee_no: str) -> int:
        prev = len(self._db)
        self._db = [e for e in self._db if e["employee_no"] != employee_no]
        return prev - len(self._db)

    # [SCH]
    def find_by_name(self, name: str) -> list[dict]:
        return [e for e in self._db if e["name"] == name]

    def find_by_birthday(self, birthday: str) -> list[dict]:
        return [e for e in self._db if e["birthday"] == birthday]

    # [MOD]
    def modify_phone(self, employee_no: str, phone: str) -> int:
        for e in self._db:
            if e["employee_no"] == employee_no:
                e["phone"] = phone
                return 1
        return 0

    def modify_position(self, employee_no: str, position: str) -> int:
        for e in self._db:
            if e["employee_no"] == employee_no:
                e["position"] = position
                return 1
        return 0

    # [CNT]
    def count(self) -> int:
        return len(self._db)

    def find_all(self) -> list[dict]:
        return list(self._db)

# pytest -> GREEN -> 커밋
```

**GREEN 커밋 메시지 예시**:

```bash
git commit -m "feat: [ADD] 직원 추가 최소 구현 — GREEN"
git commit -m "feat: [DEL] 직원 삭제 최소 구현 — GREEN"
git commit -m "feat: [SCH] 이름/생년월일 검색 최소 구현 — GREEN"
git commit -m "feat: [MOD] 정보 수정 최소 구현 — GREEN"
git commit -m "feat: [CNT] 수 조회 최소 구현 — GREEN"
```

> **결론**: 테스트가 모두 통과하는 상태에서 커밋한다. `pytest → GREEN`.

---

## 7. REFACTOR 단계

**목표**: 테스트 Green 유지하면서 코드 품질 개선 — 중복 제거 · 네이밍 · SRP · OCP 적용  
**브랜치**: `팀-번호-REFACTOR`

---

### Python — 리팩토링 포인트

#### `employee_repository.py` (Repository 패턴 — SRP)

```python
# employee_repository.py (SRP)
from abc import ABC, abstractmethod
from typing import Optional
from employee import Employee


class EmployeeRepository(ABC):

    @abstractmethod
    def save(self, emp: Employee) -> None: ...

    @abstractmethod
    def find_by_no(self, employee_no: str) -> Optional[Employee]: ...

    @abstractmethod
    def find_all(self) -> list[Employee]: ...

    @abstractmethod
    def delete_by_no(self, employee_no: str) -> int: ...

    @abstractmethod
    def find_by_name(self, name: str) -> list[Employee]: ...
```

#### `in_memory_employee_repository.py`

```python
# in_memory_employee_repository.py
from typing import Optional
from employee import Employee
from employee_repository import EmployeeRepository


class InMemoryEmployeeRepository(EmployeeRepository):

    def __init__(self):
        self._store: dict[str, Employee] = {}

    def save(self, emp: Employee) -> None:
        self._store[emp.employee_no] = emp

    def find_by_no(self, employee_no: str) -> Optional[Employee]:
        return self._store.get(employee_no)

    def find_all(self) -> list[Employee]:
        return list(self._store.values())

    def delete_by_no(self, employee_no: str) -> int:
        if employee_no in self._store:
            del self._store[employee_no]
            return 1
        return 0

    def find_by_name(self, name: str) -> list[Employee]:
        return [e for e in self._store.values() if e.name == name]

# pytest -> GREEN 유지 -> 커밋
```

**REFACTOR 커밋 메시지 예시**:

```bash
git commit -m "refactor: Repository 패턴 적용으로 저장소 분리"
```

### `@pytest.mark.parametrize` 적용 — 테스트 품질 개선

REFACTOR 단계에서 중복 TC를 `@pytest.mark.parametrize`로 통합한다.

```python
# test_employee_search_refactored.py (REFACTOR)
import pytest
from in_memory_employee_repository import InMemoryEmployeeRepository
from employee import Employee


@pytest.fixture
def repo():
    r = InMemoryEmployeeRepository()
    r.save(Employee("15123456", "홍길동", "CL3", "010-1234-5678", "19900101"))
    r.save(Employee("15123457", "박문수", "CL2", "010-2222-3333", "19921010"))
    r.save(Employee("15123458", "이순신", "CL3", "010-3333-4444", "19881231"))
    return r


@pytest.mark.parametrize("name, expected_count", [
    ("홍길동", 1),
    ("박문수", 1),
    ("이순신", 1),
    ("없는사람", 0),
])
def test_find_by_name(repo, name, expected_count):
    assert len(repo.find_by_name(name)) == expected_count


@pytest.mark.parametrize("employee_no, new_phone, expected_count", [
    ("15123456", "010-9999-0000", 1),   # 존재하는 직원
    ("99999999", "010-9999-0000", 0),   # 미존재 직원
])
def test_modify_phone(repo, employee_no, new_phone, expected_count):
    assert repo.modify_phone(employee_no, new_phone) == expected_count

# pytest -> GREEN 유지 -> 커밋
```

> **주의**: 리팩토링 후 반드시 `pytest` Green을 확인한다.

---

## 8. 요구사항 추적성 (TRACEABILITY)

**원칙**: `Invariant → UI Contract Test → Domain Test → Implementation Unit`

---

### 추적성 단계별 설명

#### Invariant (불변 규칙)

- 직원번호: 유일 식별자
- 필수 필드: 5종 모두 존재
- certi: ADV / PRO / EX / 없음

```python
# Python
MAX_REC = 100
```

#### UI Contract Test

- 입력 형식 검증 (phone)
- 출력 포맷 일관성
- 에러 메시지 계약

```python
# pytest
def test_phone_format(): ...
```

#### Domain Test

- ADD / DEL / SCH / MOD / CNT
- 경계값: 최대 레코드
- 예외: 미존재 직원 삭제

```python
# pytest
def test_delete_count(): ...
```

#### Implementation Unit

- Repository 메서드
- 파일 I/O 파싱 (txt)
- 문자열 검색 로직

```python
# pytest
def test_csv_parse(): ...
```

---

### 요구사항 추적 매트릭스 (To-Do List 기반)

| 요구사항 | Invariant | Contract | Domain Test | Unit |
|---|---|---|---|---|
| [ADD] 직원 추가 | 유일성 검증 | 입력 형식 | `add()` TC | `save()` 메서드 |
| [DEL] 직원 삭제 | PK 존재 확인 | 에러 메시지 | `delete_by_no()` TC | `del` 로직 |
| [SCH] 검색 + 3옵션 | 필드 범위 | 출력 포맷 | `find_by_name()` TC | 파싱 로직 |
| [MOD] 수정 | 불변 PK | 변경 계약 | `modify_phone()` / `modify_position()` TC | `update()` 메서드 |
| [CNT] 수 조회 | 전체 레코드 범위 | 출력 포맷 | `count()` / `find_all()` TC | 리스트 반환 로직 |

---

## 9. PR 리뷰 가이드 및 커밋 전략

**채점 기준**: S/W 품질 400점 (단계별 PR 리뷰 10개 이상 × 50점)

---

### PR 리뷰 10개 이상 달성 전략

**코드 정확성**
요구사항 충족 · 로직 오류 · 경계값 처리 확인

**캡슐화 · 접근 제어**
`_` 접두사로 private 필드 표현 · 불필요한 전역 변수 방지

**네이밍 컨벤션**
`snake_case` PEP8 준수 · 함수명 동사 시작 원칙

**테스트 품질**
`pytest` 픽스처 명확성 · 경계값 포함 · `@pytest.mark.parametrize` 활용

**중복 코드 DRY**
추출 가능한 공통 함수 제안

**성능 · 메모리**
제너레이터 활용 · 불필요한 리스트 복사 방지 · 메모리 효율

**docstring**
public API 문서화 여부 확인 (Google style docstring 권장)

**리뷰 예시**:

> "find_by_name이 O(n)인데 dict 인덱싱 구조 고려 어떨까요?"

---

### 커밋 전략 (50줄 이하 권장)

```bash
# Conventional Commits 형식

# SPEC 단계
git commit -m "docs: PRD.md Python 요구사항 초안"
git commit -m "docs: README.md To-Do List 추가"

# RED 단계
git commit -m "test: [ADD] 직원추가 TC — RED"
git commit -m "test: [DEL] 직원삭제 TC — RED"
git commit -m "test: [SCH] 이름검색 TC — RED"
git commit -m "test: [MOD] 정보수정 TC — RED"
git commit -m "test: [CNT] 수조회 TC — RED"

# GREEN 단계
git commit -m "feat: [ADD] 직원추가 구현"
git commit -m "feat: [DEL] 직원삭제 구현"
git commit -m "feat: [SCH] 이름/생년월일 검색 구현"
git commit -m "feat: [MOD] 정보수정 구현"
git commit -m "feat: [CNT] 수조회 구현"

# REFACTOR 단계
git commit -m "refactor: EmployeeRepository ABC 분리"
git commit -m "refactor: InMemoryEmployeeRepository 구현"
git commit -m "style: snake_case 네이밍 통일"
git commit -m "test: parametrize — SCH/MOD 경계값 TC 통합"
```

**50줄 분할 예시** — ADD 기능을 4개 커밋으로 분할:

1. 데이터 클래스 정의
2. 구현 코드
3. TC 작성
4. 문서 갱신

---

### 브랜치 규칙 (채점 200점)

```
D팀 07번 기준:
  D-07-SPEC
  D-07-RED
  D-07-GREEN
  D-07-REFACTOR
```

---

## 10. VSCode 개발 환경 설정 및 핵심 구현

### `.vscode/settings.json`

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "editor.formatOnSave": true,
    "editor.tabSize": 4
}
```

---

### Python pytest 빌드 및 테스트

```bash
# 가상환경 설정
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 의존성 설치
pip install pytest pytest-cov

# 테스트 실행
pytest

# 커버리지 포함 실행
pytest --cov=. --cov-report=html
# 커버리지: htmlcov/index.html

# 실행
python main.py input.txt output.txt
```

---

### 핵심 요구사항 구현 — Python 인터페이스 (`EmployeeRepository`)

```python
# employee_repository.py (ABC 기반 순수 추상 인터페이스)
from abc import ABC, abstractmethod
from typing import Optional
from employee import Employee


class EmployeeRepository(ABC):

    @abstractmethod
    def save(self, emp: Employee) -> None:           # [ADD]
        ...

    @abstractmethod
    def delete_by_no(self, employee_no: str) -> int: # [DEL]
        ...

    @abstractmethod
    def find_by_name(self, name: str) -> list[Employee]:    # [SCH]
        ...

    @abstractmethod
    def find_by_birthday(self, birthday: str) -> list[Employee]:  # [SCH]
        ...

    @abstractmethod
    def modify_phone(self, employee_no: str, phone: str) -> int:  # [MOD]
        ...

    @abstractmethod
    def modify_position(self, employee_no: str, pos: str) -> int: # [MOD]
        ...

    @abstractmethod
    def find_all(self) -> list[Employee]:            # [CNT/PRINT]
        ...

# 각 메서드 -> RED TC 먼저 -> GREEN 구현 -> REFACTOR
```

---

## 11. BP 문서 작성 및 팀 발표 가이드

**채점 기준**: BP 평가 100점

---

### BP(Best Practice) 문서 (50점) — `bp/BP.md`

#### 1장 TDD 적용 경험

- RED → GREEN → REFACTOR 사이클에서 배운 점
- pytest 픽스처 설계 경험
- `@pytest.mark.parametrize` 활용 사례

#### 2장 Clean Code 사례

- Before / After 코드 비교 + 개선 근거
- Python: `@dataclass` · ABC · `Optional` 타입 힌트 활용

#### 3장 팀 협업 경험

- PR 리뷰 효과적 사례 · 그라운드 룰 성과
- Offline 리뷰 → GitHub PR 온라인 기록

#### 4장 AI 활용

- 프롬프트 엔지니어링 우수 사례
- Gemini CLI / Cursor AI (Python 중심)

#### 5장 트러블슈팅

- 가장 어려웠던 버그 & 해결 과정
- pytest import 오류 / 파일 I/O 인코딩 이슈

#### 6장 현업 적용 계획

- 팀원별 3개월 액션 아이템
- Clean Code → 실무 코드베이스 적용

---

### 발표 구성 (50점) — 팀별 발표

```
① Python 프로젝트 데모 (2분)
    ->
② TDD 과정 시연 (2분)
    ->
③ 우수 프롬프트 공유
    ->
④ 팀 회고
```

---

### Gemini CLI / Cursor AI — BP 문서 자동 생성 프롬프트

```
# Cursor Chat (Ctrl+L) 또는 Gemini CLI
@Codebase @bp/BP.md

[P] 시니어 Python 개발자 관점의 기술 문서 작성자
[C] Python 3 팀 프로젝트
    5일 TDD + Clean Code + Refactoring 실습
[T] 팀 BP 문서를 6장 구조로 작성:
    - Python Before/After 코드 비교 포함
    - pytest 픽스처 및 parametrize 활용 사례 포함
    - Gemini CLI 활용 프롬프트 우수 사례
[F] Markdown + 코드 블록 | bp/BP.md 저장
```

---

### 팀 그라운드 룰 (1일차 수립)

- 매일 스탠드업 미팅 (15분): 어제 / 오늘 / 블로커
- PR 리뷰 24시간 이내 응답 | 코멘트 최소 2개 이상
- 커밋 전 `pytest` 실행 의무
- Cursor AI / Gemini CLI 제안 코드 함께 공유
- Offline 리뷰 → GitHub PR 코멘트 온라인 기록

---

### 최종 제출 체크리스트

- [ ] Release 브랜치 생성 (D팀-07번-RED 형식)
- [ ] `bp/BP.md` 커밋 완료
- [ ] `README.md` To-Do List 갱신
- [ ] `docs/PRD.md` 최신화
- [ ] `pytest` 전체 통과 확인 후 제출

---

## 12. 핵심 요약

**TDD 사이클**

SPEC → RED → GREEN → REFACTOR: 각 단계 브랜치 & PR 리뷰 10개 이상이 핵심 점수 (400점)이다.

**문서**

`PRD.md` + `README.md` + To-Do List 3종 문서를 먼저 완성하면 방향이 잡힌다 (100점).

**커밋**

커밋 50줄 이하 + Conventional Commits: 작은 단위로 자주 커밋해야 히스토리가 살아있다.

**Python TDD**

`@pytest.mark.parametrize` — 언어가 달라도 TDD 사이클은 동일하다. Python에서는 pytest가 그 중심이다.

**BP**

BP 문서와 발표로 팀의 성장 스토리를 기록한다 (100점) — 과정이 곧 결과물이다.

> **결론**: Python 3 중심 팀 프로젝트. 팀 프로젝트 파이팅!

# Employee Management System (Python)

사원 관리 시스템입니다.

## 실행 방법

```bash
python python/main.py input.txt output.txt
```

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

### 3. 프로그램 실행

```bash
python python/main.py input.txt output.txt
```

### 4. 가상환경 비활성화

```bash
deactivate
```

## 프로젝트 구조

```
python/
├── main.py                 # 메인 진입점
├── command_parser.py       # 입력 라인 파싱
├── command_factory.py      # 커맨드 객체 생성
├── commands.py             # 커맨드 클래스 (Add, Delete, Search, Mod, Count)
├── employee.py             # Employee 클래스
├── employee_store.py       # 사원 저장소 구현
├── enums.py                # 열거형 (FieldEnum, CombinationEnum 등)
├── field.py                # 필드 클래스 (Name, Birthday, CareerLevel, PhoneNumber, EmployeeNumber, Certi)
├── option_parser.py        # 옵션 파싱 유틸리티
├── result_formatter.py     # 결과 포맷팅
└── token_group.py          # 토큰 그룹

requirement/
├── Base.md                 # 기본 요구사항
└── Further.md              # 추가 요구사항
```

## 지원 명령어

| 명령어 | 설명 |
|--------|------|
| ADD | 사원 추가 |
| DEL | 사원 삭제 |
| SCH | 사원 검색 |
| MOD | 사원 수정 |
| CNT | 사원 수 조회 |

## 옵션

- **옵션1 (-p)**: 출력 옵션 (최대 5개 레코드 출력)
- **옵션2**: 필드 세부 선택 (-f, -l, -m, -y, -d)
- **옵션3**: 부등호 비교 (-g, -ge, -s, -se) - SCH 전용
- **AND/OR**: 다중 조건 검색 (-a, -o)

## 요구사항

- Python 3.7 이상

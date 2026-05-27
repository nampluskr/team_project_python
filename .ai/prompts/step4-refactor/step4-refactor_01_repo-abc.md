# step4-refactor_01_repo-abc

## 단계
step4-refactor

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_repository.py`
- `python/employee_store.py`

## 작업
- `EmployeeRepository` ABC를 분리한다.
- 저장, 삭제, 검색, 전체 조회 등 `EmployeeStore`가 필요로 하는 저장소 계약을 정의한다.
- 기존 테스트가 통과하는 범위에서 인터페이스를 작게 유지한다.

## 제약
- 동작 변경 없이 구조 개선만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `refactor: extract employee repository abc`

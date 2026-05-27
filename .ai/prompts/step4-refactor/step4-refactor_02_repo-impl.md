# step4-refactor_02_repo-impl

## 단계
step4-refactor

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_repository.py`
- `python/in_memory_employee_repository.py`

## 작업
- `InMemoryEmployeeRepository`를 구현한다.
- 기존 `EmployeeStore` 내부 저장소 동작을 repository 구현으로 옮긴다.
- 사원번호 유일성 및 정렬 기준이 기존 테스트와 동일하게 유지되는지 확인한다.

## 제약
- 동작 변경 없이 구조 개선만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `refactor: add in-memory employee repository`

# step4-refactor_05_test-invariant

## 단계
step4-refactor

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `tests/`

## 작업
- 직원번호 유일성과 불변 규칙에 대한 invariant 테스트를 보강한다.
- 중복 직원번호 추가 실패와 `employeeNum` 수정 실패를 명확히 검증한다.
- 실패 시 데이터가 오염되지 않는지 확인한다.

## 제약
- 테스트 보강 후 필요한 최소 수정만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add employee number invariant cases`

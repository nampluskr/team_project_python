# step2-red_01_test-add

## 단계
step2-red

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `python/employee.py`

## 작업
- `[ADD] EmployeeStore.add()`의 실패 테스트를 작성한다.
- 정상 직원 추가 후 `count()` 또는 검색 가능한 상태가 되는지 검증한다.
- 중복 직원번호 등 핵심 invariant가 있다면 RED 범위에서 필요한 최소 케이스만 추가한다.

## 제약
- RED 단계이므로 제품 코드는 수정하지 않는다.
- pytest 실패를 확인하고 실패 원인을 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add employee store add red case`

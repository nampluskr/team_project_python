# step2-red_07_test-mod-immutable

## 단계
step2-red

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `python/enums.py`

## 작업
- `[MOD] 직원번호 불변 규칙` 실패 테스트를 작성한다.
- `employeeNum` 수정을 시도하면 `ValueError`가 발생하는지 검증한다.
- 예외 발생 후 기존 직원 데이터가 변경되지 않는지 확인한다.

## 제약
- RED 단계이므로 제품 코드는 수정하지 않는다.
- pytest 실패를 확인하고 실패 원인을 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add employee number immutable red case`

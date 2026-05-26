# step2-red_06_test-mod

## 단계
step2-red

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `python/enums.py`

## 작업
- `[MOD] EmployeeStore.modify()`의 실패 테스트를 작성한다.
- 조건에 맞는 직원의 필드가 수정되고, 반환값은 수정 전 레코드인지 검증한다.
- 전화번호 또는 경력개발단계처럼 변경 결과가 명확한 필드를 우선 사용한다.

## 제약
- RED 단계이므로 제품 코드는 수정하지 않는다.
- pytest 실패를 확인하고 실패 원인을 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add employee store modify red case`

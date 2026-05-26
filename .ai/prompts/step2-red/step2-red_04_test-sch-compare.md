# step2-red_04_test-sch-compare

## 단계
step2-red

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `python/field.py`

## 작업
- `[SCH] TertiaryOptionEnum` 부등호 옵션 실패 테스트를 작성한다.
- `-g`, `-ge`, `-s`, `-se`에 해당하는 초과, 이상, 미만, 이하 검색을 검증한다.
- 생년월일 또는 사원번호처럼 비교 의미가 명확한 필드를 우선 사용한다.

## 제약
- RED 단계이므로 제품 코드는 수정하지 않는다.
- pytest 실패를 확인하고 실패 원인을 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add search compare red case`

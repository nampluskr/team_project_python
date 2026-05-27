# step2-red_05_test-sch-and-or

## 단계
step2-red

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `python/enums.py`

## 작업
- `[SCH] CombinationEnum` AND/OR 다중 조건 실패 테스트를 작성한다.
- `search_and_or()`가 AND 조건에서는 교집합, OR 조건에서는 합집합 결과를 반환하는지 검증한다.
- 중복 결과가 생기지 않는지 최소 케이스로 확인한다.

## 제약
- RED 단계이므로 제품 코드는 수정하지 않는다.
- pytest 실패를 확인하고 실패 원인을 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add search and-or red case`

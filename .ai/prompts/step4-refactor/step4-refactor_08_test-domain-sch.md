# step4-refactor_08_test-domain-sch

## 단계
step4-refactor

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `tests/`

## 작업
- `EmployeeStore.search()` 이름/생년월일 도메인 테스트를 보강한다.
- 전체 필드 검색과 서브필드 검색의 기대 결과를 명확히 분리한다.
- 결과 없음, 단일 결과, 다중 결과 케이스를 필요한 만큼 포함한다.

## 제약
- 테스트 보강 후 필요한 최소 수정만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add search domain cases`

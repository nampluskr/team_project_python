# step4-refactor_07_test-domain-del

## 단계
step4-refactor

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `tests/`

## 작업
- `EmployeeStore.delete()` 도메인 테스트를 보강한다.
- 존재하지 않는 직원 삭제 시 빈 목록을 반환하고 저장소 상태가 유지되는지 검증한다.
- 단일 조건과 필요한 경우 AND/OR 조건의 삭제 결과를 확인한다.

## 제약
- 테스트 보강 후 필요한 최소 수정만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add delete domain cases`

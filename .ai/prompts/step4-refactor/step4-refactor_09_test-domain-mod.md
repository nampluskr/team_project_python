# step4-refactor_09_test-domain-mod

## 단계
step4-refactor

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `tests/`

## 작업
- `EmployeeStore.modify()` 전화번호/직급 도메인 테스트를 보강한다.
- 수정 전 레코드 반환과 수정 후 저장소 상태를 함께 검증한다.
- 대상 없음 케이스와 잘못된 수정값 케이스를 필요한 범위에서 포함한다.

## 제약
- 테스트 보강 후 필요한 최소 수정만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add modify domain cases`

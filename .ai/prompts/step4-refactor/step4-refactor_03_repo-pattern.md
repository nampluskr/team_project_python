# step4-refactor_03_repo-pattern

## 단계
step4-refactor

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/employee_store.py`
- `python/employee_repository.py`

## 작업
- `EmployeeStore`에 Repository 패턴을 적용한다.
- 저장소 접근 책임을 repository로 위임하고, 도메인 명령 책임은 `EmployeeStore`에 남긴다.
- 기존 public API가 깨지지 않도록 유지한다.

## 제약
- 동작 변경 없이 구조 개선만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `refactor: apply repository pattern`

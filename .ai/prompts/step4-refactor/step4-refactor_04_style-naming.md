# step4-refactor_04_style-naming

## 단계
step4-refactor

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/`
- `tests/`

## 작업
- Python 코드의 네이밍을 PEP8 `snake_case` 중심으로 정리한다.
- 외부 입력 Column명(`employeeNum`, `phoneNum`)은 파싱/출력 계약을 깨지 않는 범위에서만 매핑한다.
- 테스트 코드의 fixture, helper 이름도 읽기 쉽게 정리한다.

## 제약
- 동작 변경 없이 스타일 개선만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `style: normalize python naming`

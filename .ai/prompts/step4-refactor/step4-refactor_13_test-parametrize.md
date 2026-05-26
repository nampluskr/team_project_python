# step4-refactor_13_test-parametrize

## 단계
step4-refactor

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `tests/`

## 작업
- `@pytest.mark.parametrize`로 SCH/MOD 경계값 테스트를 통합한다.
- 반복되는 fixture와 기대값을 읽기 쉬운 테이블 형태로 정리한다.
- 기존 테스트 의미를 잃지 않도록 케이스 이름 또는 ids를 추가한다.

## 제약
- 동작 변경 없이 테스트 구조 개선을 우선한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: parametrize boundary cases`

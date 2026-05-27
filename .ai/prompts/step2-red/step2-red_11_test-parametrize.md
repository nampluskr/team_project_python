# step2-red_11_test-parametrize

## 단계
step2-red

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- 기존 `tests/` 테스트 파일

## 작업
- `@pytest.mark.parametrize`를 사용해 SCH 다중 조건 실패 테스트를 정리한다.
- 필드, 옵션, 기대 결과가 반복되는 케이스를 파라미터화한다.
- 기존 RED 테스트와 중복이 과도하지 않도록 테스트 의도를 분리한다.

## 제약
- RED 단계이므로 제품 코드는 수정하지 않는다.
- pytest 실패를 확인하고 실패 원인을 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: parametrize search red cases`

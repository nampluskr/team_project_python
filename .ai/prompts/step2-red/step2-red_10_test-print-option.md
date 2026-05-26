# step2-red_10_test-print-option

## 단계
step2-red

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/result_formatter.py`
- `python/employee.py`

## 작업
- `-p` 출력 옵션의 `ResultFormatter` 실패 테스트를 작성한다.
- 검색/삭제/수정 결과를 최대 5개 레코드 라인으로 포맷하는지 검증한다.
- 결과가 없을 때 `{명령어},NONE` 형식이 되는지 검증한다.

## 제약
- RED 단계이므로 제품 코드는 수정하지 않는다.
- pytest 실패를 확인하고 실패 원인을 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add print option formatter red case`

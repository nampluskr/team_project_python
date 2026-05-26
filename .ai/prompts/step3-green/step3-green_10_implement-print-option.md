# step3-green_10_implement-print-option

## 단계
step3-green

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- RED 단계 `-p` 출력 옵션 실패 테스트
- `python/result_formatter.py`

## 작업
- `-p` 출력 옵션의 `ResultFormatter`를 실패 테스트 통과에 필요한 만큼 최소 구현한다.
- 레코드 출력은 최대 5개로 제한한다.
- 결과가 없을 때 `{명령어},NONE`을 반환한다.

## 제약
- 실패한 RED 테스트를 통과시키는 최소 구현만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `feat: implement print option formatter`

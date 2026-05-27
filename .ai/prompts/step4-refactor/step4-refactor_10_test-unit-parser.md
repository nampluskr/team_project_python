# step4-refactor_10_test-unit-parser

## 단계
step4-refactor

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/command_parser.py`
- `python/token_group.py`

## 작업
- `CommandParser` CSV 파싱 unit 테스트를 보강한다.
- ADD/DEL/SCH/MOD/CNT 입력 라인이 기대하는 `TokenGroup`으로 변환되는지 검증한다.
- 옵션 위치와 파라미터 분리가 PRD와 일치하는지 확인한다.

## 제약
- 테스트 보강 후 필요한 최소 수정만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add command parser unit cases`

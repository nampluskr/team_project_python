# step4-refactor_12_test-unit-formatter

## 단계
step4-refactor

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/result_formatter.py`
- `tests/`

## 작업
- `ResultFormatter` 출력 포맷 unit 테스트를 보강한다.
- `-p` 출력, count 출력, NONE 출력, 최대 5개 제한을 검증한다.
- 정렬 기준이 formatter 책임인지 store 책임인지 현재 설계에 맞춰 테스트 범위를 정한다.

## 제약
- 테스트 보강 후 필요한 최소 수정만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add result formatter unit cases`

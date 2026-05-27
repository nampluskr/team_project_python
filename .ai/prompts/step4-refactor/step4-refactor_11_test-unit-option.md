# step4-refactor_11_test-unit-option

## 단계
step4-refactor

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/option_parser.py`
- `tests/`

## 작업
- `OptionParser` 옵션 파싱 unit 테스트를 보강한다.
- 옵션1 `-p`, 옵션2 서브필드, 옵션3 부등호, AND/OR 옵션을 각각 검증한다.
- 잘못된 옵션 입력의 처리 방식도 현재 설계에 맞게 확인한다.

## 제약
- 테스트 보강 후 필요한 최소 수정만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add option parser unit cases`

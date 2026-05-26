# step4-refactor_06_test-contract

## 단계
step4-refactor

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/field.py`
- `python/result_formatter.py`

## 작업
- phoneNum 입력 형식과 출력 포맷 contract 테스트를 보강한다.
- 전화번호는 `010-XXXX-XXXX` 형식을 검증한다.
- 출력 라인은 `{명령어},{사원번호},{성명},{cl},{phoneNum},{birthday},{certi}` 형식을 검증한다.

## 제약
- 테스트 보강 후 필요한 최소 수정만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add phone and output contract cases`

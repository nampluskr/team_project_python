# step3-green_13_implement-subfield

## 단계
step3-green

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- RED 단계 서브필드 실패 테스트
- `python/option_parser.py`
- `python/employee_store.py`

## 작업
- 옵션2 서브필드 `-f`, `-l`, `-m`, `-y`, `-d`를 실패 테스트 통과에 필요한 만큼 최소 구현한다.
- 이름, 전화번호, 생년월일의 서브필드 인덱스를 PRD 기준과 맞춘다.
- 검색/삭제/수정 조건에서 서브필드 인덱스를 사용할 수 있게 한다.

## 제약
- 실패한 RED 테스트를 통과시키는 최소 구현만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `feat: implement subfield options`

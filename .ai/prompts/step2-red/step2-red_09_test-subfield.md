# step2-red_09_test-subfield

## 단계
step2-red

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- `python/option_parser.py`
- `python/employee_store.py`

## 작업
- 옵션2 서브필드 `-f`, `-l`, `-m`, `-y`, `-d` 실패 테스트를 작성한다.
- 이름, 전화번호, 생년월일의 서브필드 인덱스가 PRD와 일치하는지 검증한다.
- 서브필드 검색이 필요한 경우 `EmployeeStore.search()` 호출까지 최소 범위에서 확인한다.

## 제약
- RED 단계이므로 제품 코드는 수정하지 않는다.
- pytest 실패를 확인하고 실패 원인을 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `test: add subfield option red case`

# step3-green_04_implement-sch-name

## 단계
step3-green

## 참조
- `.ai/TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- RED 단계 이름 검색 실패 테스트
- `python/employee_store.py`
- `python/enums.py`

## 작업
- `[SCH]` 이름 검색을 실패 테스트 통과에 필요한 만큼 최소 구현한다.
- `FieldEnum.FIELD_NAME` 기준의 전체 이름 일치 검색을 지원한다.
- 검색 결과 정렬은 테스트가 요구하는 기준만 우선 적용한다.

## 제약
- 실패한 RED 테스트를 통과시키는 최소 구현만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `feat: implement name search`

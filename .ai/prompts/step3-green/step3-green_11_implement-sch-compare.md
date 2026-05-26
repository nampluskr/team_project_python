# step3-green_11_implement-sch-compare

## 단계
step3-green

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `docs/PRD.md`
- RED 단계 부등호 검색 실패 테스트
- `python/field.py`
- `python/employee_store.py`

## 작업
- `[SCH]` 부등호 옵션 `-g`, `-ge`, `-s`, `-se`를 실패 테스트 통과에 필요한 만큼 최소 구현한다.
- `TertiaryOptionEnum` 또는 대응 비교 로직을 구현한다.
- 비교 기준은 테스트가 사용하는 필드의 문자열/숫자 의미에 맞춘다.

## 제약
- 실패한 RED 테스트를 통과시키는 최소 구현만 수행한다.
- pytest를 실행하고 통과 여부를 기록한다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `feat: implement search compare options`

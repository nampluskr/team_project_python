# step4-refactor_15_chore-coverage

## 단계
step4-refactor

## 참조
- `TODO.md`
- `.ai/CONTEXT.md`
- `README.md`
- `tests/`

## 작업
- `pytest --cov` 커버리지 리포트를 확인한다.
- 목표 커버리지 80% 이상 달성 여부와 부족한 모듈을 기록한다.
- 커버리지 보강이 필요하면 위험도가 높은 누락 영역부터 테스트를 추가한다.

## 제약
- 리포트 확인 결과와 추가 테스트 여부를 명확히 기록한다.
- pytest와 pytest-cov 실행 결과를 남긴다.
- 커밋은 가능한 50줄 이하 단위로 분리한다.
- 커밋 메시지 형식: `chore: verify pytest coverage`

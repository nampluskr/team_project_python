# TODO — Employee Management System (D팀 07번)

---

## 1. SPEC 단계

- [x] D-07-SPEC 브랜치 생성
- [x] SPEC PR 생성

- [x] chore: 개발 환경 설정 — 가상환경 생성 및 pytest pytest-cov 설치
- [x] chore: .vscode/settings.json 작성
- [x] chore: 팀 그라운드 룰 수립 (스탠드업 미팅 · PR 리뷰 규칙 · 커밋 전 pytest 의무)

- [x] docs: PRD.md Python 요구사항 초안 — docs/PRD.md 작성
- [x] docs: README.md 프로젝트 개요 및 팀원 소개 — README.md 작성
- [x] docs: README.md To-Do List 추가 — To-Do List 작성 (요구사항별 체크박스 · 담당자 · 우선순위)

- [x] SPEC PR 승인
- [x] D-07-SPEC 브랜치 머지

---

## 2. RED 단계

- [ ] D-07-RED 브랜치 생성
- [ ] RED PR 생성

- [ ] test: [ADD] 직원 추가 TC — RED (pytest FAIL 확인)
- [ ] test: [DEL] 직원 삭제 TC — RED (pytest FAIL 확인)
- [ ] test: [SCH] 이름/생년월일 검색 TC — RED (pytest FAIL 확인)
- [ ] test: [SCH] 부등호 옵션 (-g/-ge/-s/-se) TC — RED (pytest FAIL 확인)
- [ ] test: [SCH] AND/OR 다중 조건 TC — RED (pytest FAIL 확인)
- [ ] test: [MOD] 정보 수정 TC — RED (pytest FAIL 확인)
- [ ] test: [MOD] 직원번호 불변 규칙 TC — RED (pytest FAIL 확인)
- [ ] test: [CNT] 수 조회 TC — RED (pytest FAIL 확인)
- [ ] test: 옵션2 서브필드 (-f/-l/-m/-y/-d) TC — RED (pytest FAIL 확인)
- [ ] test: -p 출력 옵션 TC — RED (pytest FAIL 확인)
- [ ] test: @pytest.mark.parametrize — SCH 다중 조건 TC — RED (pytest FAIL 확인)

- [ ] RED PR 승인
- [ ] D-07-RED 브랜치 머지

---

## 3. GREEN 단계

- [ ] D-07-GREEN 브랜치 생성
- [ ] GREEN PR 생성

- [ ] feat: Employee 클래스 정의 — employee.py (Field 패턴)
- [ ] feat: Field 서브클래스 구현 — field.py (EmployeeNumber, Name, CareerLevel, PhoneNumber, Birthday, Certi)
- [ ] feat: FieldEnum / CombinationEnum 정의 — enums.py
- [ ] feat: [ADD] 직원 추가 구현 — EmployeeStore.add()
- [ ] feat: [DEL] 직원 삭제 구현 — EmployeeStore.delete() / delete_and_or()
- [ ] feat: [SCH] 검색 구현 — EmployeeStore.search() / search_and_or()
- [ ] feat: [SCH] 부등호 옵션 구현 — TertiaryOptionEnum (-g/-ge/-s/-se)
- [ ] feat: [SCH] AND/OR 다중 조건 구현 — CombinationEnum (-a/-o)
- [ ] feat: [MOD] 정보 수정 구현 — EmployeeStore.modify() / modify_and_or()
- [ ] feat: [CNT] 수 조회 구현 — EmployeeStore.count()
- [ ] feat: 옵션2 서브필드 구현 — option_parser.py (-f/-l/-m/-y/-d)
- [ ] feat: -p 출력 옵션 구현 — result_formatter.py (최대 5개 / NONE)
- [ ] feat: CSV(txt) 파일 입출력 구현 — main.py
- [ ] feat: 명령어 파싱 구현 — command_parser.py / command_factory.py
- [ ] feat: 커맨드 클래스 구현 — commands.py (Add, Delete, Search, Mod, Count)

- [ ] GREEN PR 승인
- [ ] D-07-GREEN 브랜치 머지

---

## 4. REFACTOR 단계

- [ ] D-07-REFACTOR 브랜치 생성
- [ ] REFACTOR PR 생성

- [ ] refactor: EmployeeRepository ABC 분리 — employee_repository.py 작성
- [ ] refactor: InMemoryEmployeeRepository 구현 — in_memory_employee_repository.py 작성
- [ ] refactor: Repository 패턴 적용으로 저장소 분리
- [ ] style: snake_case 네이밍 통일 (PEP8)

- [ ] test: Invariant — 직원번호 유일성 TC
- [ ] test: Invariant — 직원번호 불변 규칙 TC (modify employeeNum → ValueError)
- [ ] test: Contract — phoneNum 입력 형식 검증 TC
- [ ] test: Contract — 출력 포맷 일관성 TC
- [ ] test: Domain — EmployeeStore.delete() 미존재 직원 TC
- [ ] test: Domain — EmployeeStore.search() 이름/생년월일 TC
- [ ] test: Domain — EmployeeStore.modify() 전화번호/직급 TC
- [ ] test: Unit — CommandParser CSV 파싱 TC
- [ ] test: Unit — OptionParser 옵션 파싱 TC
- [ ] test: Unit — ResultFormatter 출력 포맷 TC
- [ ] test: @pytest.mark.parametrize — SCH/MOD 경계값 TC 통합

- [ ] docs: public API docstring 작성 (Google style)
- [ ] chore: pytest --cov 커버리지 리포트 확인 (목표 80% 이상)

- [ ] REFACTOR PR 승인
- [ ] D-07-REFACTOR 브랜치 머지

---

## 5. 최종 제출

- [ ] docs: bp/BP.md 작성 (6장 구조)
  - 1장 TDD 적용 경험 — RED/GREEN/REFACTOR 사이클 · pytest 픽스처 설계
  - 2장 Clean Code 사례 — Before/After 코드 비교 · Field 패턴 · ABC · Optional
  - 3장 팀 협업 경험 — PR 리뷰 사례 · 그라운드 룰 성과
  - 4장 AI 활용 — 프롬프트 우수 사례
  - 5장 트러블슈팅 — 버그 & 해결 과정 · pytest import 오류 · 파일 I/O 인코딩 이슈
  - 6장 현업 적용 계획 — 팀원별 3개월 액션 아이템
- [ ] bp/BP.md 커밋 완료
- [ ] 발표 자료 정리 (팀 프로젝트 회고 포함)
- [ ] 팀별 발표 준비 — 데모(2분) · TDD 시연(2분) · 프롬프트 공유 · 팀 회고
- [ ] Release 브랜치 생성 (D-07-RED 형식)
- [ ] README.md To-Do List 갱신
- [ ] docs/PRD.md 최신화
- [ ] pytest 전체 통과 확인 후 제출

# prompts/README.md

## 개요

각 TODO 항목에 1대1 대응하는 AI CLI 프롬프트 파일 목록이다.
"{프롬프트 파일명} 진행" 형식으로 해당 작업을 시작한다.
프롬프트 실행이 끝나면 아래 명령으로 session / logs / TODO를 자동 업데이트한다.

```bash
python3 .ai/scripts/complete_prompt.py .ai/prompts/{단계}/{프롬프트파일명}.md --summary "작업 요약"
```

---

## 프롬프트 파일 생성 요청

아래 프롬프트를 AI CLI 에 입력하여 프롬프트 파일 전체를 생성한다.

```
.ai/prompts/ 디렉토리 하위에 아래 목록의 프롬프트 파일을 생성한다.

각 파일은 다음 구조를 따른다.
- 단계: 해당 TDD 단계명
- 참조: 관련 소스 파일 및 PRD 섹션
- 작업: 수행할 작업 내용
- 제약: 커밋 50줄 이하 / pytest 통과 여부 / 커밋 메시지 형식

프로젝트 정보:
- 프로젝트: Employee Management System (Python 3)
- 소스 경로: python/
- 테스트 프레임워크: pytest
- 요구사항: docs/PRD.md / requirement/Base.md / requirement/Further.md
- TODO 목록: .ai/TODO.md

생성 대상 파일 목록은 이 파일의 ## 프롬프트 파일 목록 섹션을 참조한다.
```

---

## 프롬프트 파일 목록

### step1-spec/

| 파일명 | 작업 내용 |
|---|---|
| step1-spec_01_prd.md | docs: PRD.md 작성 |
| step1-spec_02_readme.md | docs: README.md 작성 |
| step1-spec_03_todo.md | docs: To-Do List 작성 |

### step2-red/

| 파일명 | 작업 내용 |
|---|---|
| step2-red_01_test-add.md | test: [ADD] EmployeeStore.add() TC — RED |
| step2-red_02_test-del.md | test: [DEL] EmployeeStore.delete() TC — RED |
| step2-red_03_test-sch.md | test: [SCH] EmployeeStore.search() 이름/생년월일 TC — RED |
| step2-red_04_test-sch-compare.md | test: [SCH] TertiaryOptionEnum 부등호 옵션 TC — RED |
| step2-red_05_test-sch-and-or.md | test: [SCH] CombinationEnum AND/OR 다중 조건 TC — RED |
| step2-red_06_test-mod.md | test: [MOD] EmployeeStore.modify() TC — RED |
| step2-red_07_test-mod-immutable.md | test: [MOD] 직원번호 불변 규칙 TC — RED |
| step2-red_08_test-cnt.md | test: [CNT] EmployeeStore.count() TC — RED |
| step2-red_09_test-subfield.md | test: 옵션2 서브필드 (-f/-l/-m/-y/-d) TC — RED |
| step2-red_10_test-print-option.md | test: -p 출력 옵션 ResultFormatter TC — RED |
| step2-red_11_test-parametrize.md | test: @pytest.mark.parametrize SCH 다중 조건 TC — RED |

### step3-green/

> **주의**: GREEN 단계는 RED 테스트 실패 확인 이후 진행한다. 각 프롬프트는 실패한 TC를 통과시키기 위한 최소 구현과 동작 검증을 목적으로 한다.

| 파일명 | 작업 내용 |
|---|---|
| step3-green_01_implement-employee.md | implement: Employee 클래스 및 Field 패턴 최소 구현 |
| step3-green_02_implement-add.md | implement: [ADD] EmployeeStore.add() 최소 구현 |
| step3-green_03_implement-del.md | implement: [DEL] EmployeeStore.delete() 최소 구현 |
| step3-green_04_implement-sch-name.md | implement: [SCH] 이름 검색 최소 구현 |
| step3-green_05_implement-sch-birthday.md | implement: [SCH] 생년월일 검색 최소 구현 |
| step3-green_06_implement-mod-phone.md | implement: [MOD] 전화번호 수정 최소 구현 |
| step3-green_07_implement-mod-career.md | implement: [MOD] 경력개발단계 수정 최소 구현 |
| step3-green_08_implement-cnt.md | implement: [CNT] EmployeeStore.count() 최소 구현 |
| step3-green_09_implement-certi.md | implement: certi 필드 최소 구현 |
| step3-green_10_implement-print-option.md | implement: -p 출력 옵션 ResultFormatter 최소 구현 |
| step3-green_11_implement-sch-compare.md | implement: SCH 부등호 옵션 TertiaryOptionEnum 최소 구현 |
| step3-green_12_implement-and-or.md | implement: AND/OR 다중 조건 CombinationEnum 최소 구현 |
| step3-green_13_implement-subfield.md | implement: 옵션2 서브필드 (-f/-l/-m/-y/-d) 최소 구현 |
| step3-green_14_implement-csv-io.md | implement: CSV(txt) 파일 입출력 main.py 최소 구현 |

### step4-refactor/

| 파일명 | 작업 내용 |
|---|---|
| step4-refactor_01_repo-abc.md | refactor: EmployeeRepository ABC 분리 |
| step4-refactor_02_repo-impl.md | refactor: InMemoryEmployeeRepository 구현 |
| step4-refactor_03_repo-pattern.md | refactor: Repository 패턴 적용 |
| step4-refactor_04_style-naming.md | style: snake_case 네이밍 통일 (PEP8) |
| step4-refactor_05_test-invariant.md | test: Invariant — 직원번호 유일성 · 불변 규칙 TC |
| step4-refactor_06_test-contract.md | test: Contract — phoneNum 입력 형식 · 출력 포맷 TC |
| step4-refactor_07_test-domain-del.md | test: Domain — EmployeeStore.delete() 미존재 직원 TC |
| step4-refactor_08_test-domain-sch.md | test: Domain — EmployeeStore.search() 이름/생년월일 TC |
| step4-refactor_09_test-domain-mod.md | test: Domain — EmployeeStore.modify() 전화번호/직급 TC |
| step4-refactor_10_test-unit-parser.md | test: Unit — CommandParser CSV 파싱 TC |
| step4-refactor_11_test-unit-option.md | test: Unit — OptionParser 옵션 파싱 TC |
| step4-refactor_12_test-unit-formatter.md | test: Unit — ResultFormatter 출력 포맷 TC |
| step4-refactor_13_test-parametrize.md | test: @pytest.mark.parametrize 경계값 TC 통합 |
| step4-refactor_14_docs-docstring.md | docs: public API docstring 작성 (Google style) |
| step4-refactor_15_chore-coverage.md | chore: pytest --cov 커버리지 리포트 확인 |

### step5-final/

| 파일명 | 작업 내용 |
|---|---|
| step5-final_01_bp-tdd.md | docs: BP.md 1장 TDD 적용 경험 |
| step5-final_02_bp-cleancode.md | docs: BP.md 2장 Clean Code 사례 |
| step5-final_03_bp-collaboration.md | docs: BP.md 3장 팀 협업 경험 |
| step5-final_04_bp-ai.md | docs: BP.md 4장 AI 활용 |
| step5-final_05_bp-troubleshoot.md | docs: BP.md 5장 트러블슈팅 |
| step5-final_06_bp-action-plan.md | docs: BP.md 6장 현업 적용 계획 |
| step5-final_07_presentation.md | 발표 자료 정리 |

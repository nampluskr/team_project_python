# knowledge/README.md

## 개요

프로젝트 도메인 지식과 요구사항 레퍼런스를 모아두는 디렉토리이다.
코드 작성이나 테스트 작성 시 반복해서 참조하는 스키마, 명령어, 출력 포맷, 옵션 규칙을 정리한다.

---

## 예정 문서

| 파일 | 목적 |
|---|---|
| `schema.md` | Employee 필드, 유효값, 불변 규칙 정리 |
| `commands.md` | ADD/DEL/SCH/MOD/CNT 명령어 동작 정리 |
| `options.md` | `-p`, `-f`, `-l`, `-m`, `-y`, `-d`, `-g`, `-ge`, `-s`, `-se`, `-a`, `-o` 옵션 정리 |
| `output-format.md` | 출력 포맷, 정렬 기준, NONE 처리 규칙 정리 |
| `test-data.md` | 테스트용 사원 데이터와 경계값 정리 |

---

## 참조 우선순위

1. `requirement/Base.md`
2. `requirement/Further.md`
3. `docs/PRD.md`
4. `.ai/CONTEXT.md`
5. `.ai/TODO.md`

요구사항 원문과 프로젝트 문서가 충돌하면 먼저 사용자에게 확인하거나, 이미 합의된 내용이 `.ai/TODO.md`와 `.ai/CONTEXT.md`에 반영되어 있는지 확인한다.

---

## 작성 규칙

- 코드 구현 세부사항보다 요구사항과 도메인 규칙을 우선 기록한다.
- 테스트에서 반복 사용하는 값은 근거와 함께 남긴다.
- 추측한 내용은 확정 규칙으로 쓰지 않고 `확인 필요`로 표시한다.


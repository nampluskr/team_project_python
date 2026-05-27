#!/usr/bin/env python3
"""Finalize a prompt execution and auto-update TODO/session/log context files."""

from __future__ import annotations

import argparse
import re
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AI_DIR = ROOT / ".ai"
TODO_PATH = AI_DIR / "TODO.md"
SESSIONS_DIR = AI_DIR / "sessions"
LOGS_DIR = AI_DIR / "logs"
PROMPTS_DIR = AI_DIR / "prompts"
SYNC_SCRIPT = AI_DIR / "scripts" / "sync_todo_status.py"

STAGE_TODO_PATTERNS = {
    "step1-spec": [
        r"docs:\s*PRD\.md",
        r"docs:\s*README\.md 프로젝트 개요 및 팀원 소개",
        r"docs:\s*README\.md To-Do List 추가",
    ],
    "step2-red": [
        r"test:\s*\[ADD\]",
        r"test:\s*\[DEL\]",
        r"test:\s*\[SCH\]\s*이름/생년월일",
        r"test:\s*\[SCH\]\s*부등호 옵션",
        r"test:\s*\[SCH\]\s*AND/OR",
        r"test:\s*\[MOD\]\s*정보 수정",
        r"test:\s*\[MOD\]\s*직원번호 불변 규칙",
        r"test:\s*\[CNT\]",
        r"test:\s*옵션2 서브필드",
        r"test:\s*-p 출력 옵션",
        r"test:\s*@pytest\.mark\.parametrize",
    ],
    "step3-green": [
        r"feat:\s*Employee 클래스 정의",
        r"feat:\s*Field 서브클래스 구현",
        r"feat:\s*FieldEnum / CombinationEnum 정의",
        r"feat:\s*\[ADD\]",
        r"feat:\s*\[DEL\]",
        r"feat:\s*\[SCH\]\s*검색 구현",
        r"feat:\s*\[SCH\]\s*부등호 옵션 구현",
        r"feat:\s*\[SCH\]\s*AND/OR",
        r"feat:\s*\[MOD\]",
        r"feat:\s*\[CNT\]",
        r"feat:\s*옵션2 서브필드 구현",
        r"feat:\s*-p 출력 옵션 구현",
        r"feat:\s*CSV\(txt\) 파일 입출력 구현",
        r"feat:\s*명령어 파싱 구현",
    ],
    "step4-refactor": [
        r"refactor:\s*EmployeeRepository ABC 분리",
        r"refactor:\s*InMemoryEmployeeRepository 구현",
        r"refactor:\s*Repository 패턴 적용",
        r"style:\s*snake_case",
        r"test:\s*Invariant\s*—\s*직원번호 유일성",
        r"test:\s*Contract\s*—\s*phoneNum 입력 형식",
        r"test:\s*Domain\s*—\s*EmployeeStore\.delete",
        r"test:\s*Domain\s*—\s*EmployeeStore\.search",
        r"test:\s*Domain\s*—\s*EmployeeStore\.modify",
        r"test:\s*Unit\s*—\s*CommandParser",
        r"test:\s*Unit\s*—\s*OptionParser",
        r"test:\s*Unit\s*—\s*ResultFormatter",
        r"test:\s*@pytest\.mark\.parametrize",
        r"docs:\s*public API docstring 작성",
        r"chore:\s*pytest --cov",
    ],
    "step5-final": [
        r"docs:\s*bp/BP\.md 작성",
        r"bp/BP\.md 커밋 완료",
        r"발표 자료 정리",
        r"팀별 발표 준비",
        r"Release 브랜치 생성",
        r"README\.md To-Do List 갱신",
        r"docs/PRD\.md 최신화",
    ],
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("prompt_file", help="Path to prompt markdown file")
    p.add_argument(
        "--summary",
        default="프롬프트 작업 완료",
        help="Short summary used in sessions/logs",
    )
    return p.parse_args()


def extract_stage_and_index(prompt_path: Path) -> tuple[str, int]:
    m = re.search(r"(step\d-[a-z]+)_(\d+)_", prompt_path.name)
    if not m:
        raise ValueError(f"Unsupported prompt filename format: {prompt_path.name}")
    return m.group(1), int(m.group(2))


def mark_todo_complete(stage: str, task_index: int) -> str:
    patterns = STAGE_TODO_PATTERNS.get(stage)
    if not patterns or task_index < 1 or task_index > len(patterns):
        return ""

    pattern = re.compile(patterns[task_index - 1])
    lines = TODO_PATH.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.lstrip().startswith("- [ ]") and pattern.search(line):
            lines[i] = line.replace("- [ ]", "- [x]", 1)
            TODO_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return line.strip()
    return ""


def next_session_number(stage: str) -> int:
    stage_dir = SESSIONS_DIR / stage
    stage_dir.mkdir(parents=True, exist_ok=True)
    nums = []
    for p in stage_dir.glob(f"{stage}_session_*.md"):
        m = re.search(r"_session_(\d+)\.md$", p.name)
        if m:
            nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


def find_next_prompt(stage: str, current_idx: int) -> str:
    stage_prompts = sorted((PROMPTS_DIR / stage).glob(f"{stage}_*.md"))
    for p in stage_prompts:
        m = re.search(rf"{re.escape(stage)}_(\d+)_", p.name)
        if m and int(m.group(1)) > current_idx:
            return f"\"{p.as_posix()} 진행\""
    return "\"다음 단계 프롬프트 진행\""


def write_session_and_log(
    stage: str,
    seq: int,
    prompt_rel: str,
    summary: str,
    todo_line: str,
    next_prompt: str,
) -> None:
    today = datetime.now().strftime("%Y-%m-%d")
    session_name = f"{stage}_session_{seq:02d}.md"
    log_name = f"{stage}_session_log_{seq:02d}.md"

    session_dir = SESSIONS_DIR / stage
    log_dir = LOGS_DIR / stage
    session_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)

    session_content = (
        f"# {stage}_session_{seq:02d} | {today}\n\n"
        "## 단계\n"
        f"{stage}\n\n"
        "## 완료 항목\n"
        f"- [x] `{prompt_rel} 진행` 완료\n"
        f"- [x] {summary}\n"
        + (f"- [x] TODO 반영: `{todo_line}`\n\n" if todo_line else "\n")
        + "## 미완료 항목\n"
        "- [ ] 후속 프롬프트 작업 진행\n\n"
        "## 다음 시작 프롬프트\n"
        f"{next_prompt}\n\n"
        "## 파일 변경 내역\n"
        "- 수정: `.ai/TODO.md`\n"
        "- 수정: `README.md` (상태 동기화)\n"
        "- 수정: `.ai/CONTEXT.md` (상태 동기화)\n"
        f"- 신규: `.ai/sessions/{stage}/{session_name}`\n"
        "- 수정: `.ai/sessions/current.md`\n"
        f"- 신규: `.ai/logs/{stage}/{log_name}`\n\n"
        "## 커밋 메시지 목록\n"
        "- 제안: `docs: complete prompt workflow update`\n\n"
        "## 이슈 및 메모\n"
        "- 프롬프트 완료 후 세션/로그/TODO 자동 업데이트를 수행했다.\n"
    )

    log_content = (
        f"# {stage}_session_log_{seq:02d} | {today}\n\n"
        "## 단계\n"
        f"{stage}\n\n"
        "## 사용자 요청 이력\n"
        f"- `{prompt_rel}` 실행 완료 후 session / logs / TODO 자동 업데이트 요청\n\n"
        "## 의사결정 내역\n"
        "- 완료 프롬프트 기준으로 세션/로그 파일을 생성하고 current.md를 최신 내용으로 갱신했다.\n"
        "- TODO 체크 반영 후 상태 동기화 스크립트를 실행했다.\n\n"
        "## AI 제안 채택/거부 내역\n"
        "- 채택: 자동 업데이트 스크립트 기반 운영\n\n"
        "## 시도 및 폐기 내역\n"
        "- 없음\n\n"
        "## 생성물 목록\n"
        f"- `.ai/sessions/{stage}/{session_name}`\n"
        "- `.ai/sessions/current.md`\n"
        f"- `.ai/logs/{stage}/{log_name}`\n"
        "- `.ai/TODO.md`\n"
        "- `README.md`\n"
        "- `.ai/CONTEXT.md`\n\n"
        "## 주요 컨텍스트\n"
        f"- 이번 완료 프롬프트: `{prompt_rel}`\n"
        f"- 후속 시작 프롬프트: {next_prompt}\n"
    )

    session_path = session_dir / session_name
    log_path = log_dir / log_name
    current_path = SESSIONS_DIR / "current.md"

    session_path.write_text(session_content, encoding="utf-8")
    current_path.write_text(session_content, encoding="utf-8")
    log_path.write_text(log_content, encoding="utf-8")


def run_sync_status() -> None:
    subprocess.run(["python3", str(SYNC_SCRIPT)], check=True, cwd=str(ROOT))


def main() -> None:
    args = parse_args()
    prompt_path = (ROOT / args.prompt_file).resolve() if not Path(args.prompt_file).is_absolute() else Path(args.prompt_file)
    prompt_rel = prompt_path.relative_to(ROOT).as_posix()

    stage, idx = extract_stage_and_index(prompt_path)
    todo_line = mark_todo_complete(stage, idx)
    seq = next_session_number(stage)
    next_prompt = find_next_prompt(stage, idx)

    write_session_and_log(stage, seq, prompt_rel, args.summary, todo_line, next_prompt)
    run_sync_status()

    print(f"Completed workflow for: {prompt_rel}")
    if todo_line:
        print(f"Checked TODO: {todo_line}")


if __name__ == "__main__":
    main()

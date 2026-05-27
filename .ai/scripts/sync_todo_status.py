#!/usr/bin/env python3
"""Sync stage status from .ai/TODO.md into README.md and .ai/CONTEXT.md."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TODO_PATH = ROOT / ".ai" / "TODO.md"
README_PATH = ROOT / "README.md"
CONTEXT_PATH = ROOT / ".ai" / "CONTEXT.md"

STAGES = ["SPEC", "RED", "GREEN", "REFACTOR", "최종 제출"]


def parse_todo_status(todo_text: str) -> dict[str, str]:
    status_map: dict[str, str] = {}

    for idx, stage in enumerate(STAGES):
        heading_pattern = rf"^##\s+\d+\.\s+{re.escape(stage)}\s*단계?\s*$|^##\s+\d+\.\s+{re.escape(stage)}\s*$"
        start_match = re.search(heading_pattern, todo_text, flags=re.MULTILINE)
        if not start_match:
            continue

        start = start_match.end()
        if idx + 1 < len(STAGES):
            next_stage = STAGES[idx + 1]
            next_pattern = rf"^##\s+\d+\.\s+{re.escape(next_stage)}\s*단계?\s*$|^##\s+\d+\.\s+{re.escape(next_stage)}\s*$"
            next_match = re.search(next_pattern, todo_text[start:], flags=re.MULTILINE)
            end = start + next_match.start() if next_match else len(todo_text)
        else:
            end = len(todo_text)

        block = todo_text[start:end]
        checked = len(re.findall(r"^\s*-\s+\[x\]\s+", block, flags=re.MULTILINE))
        unchecked = len(re.findall(r"^\s*-\s+\[\s\]\s+", block, flags=re.MULTILINE))

        if checked > 0 and unchecked == 0:
            status_map[stage] = "완료"
        elif checked == 0 and unchecked > 0:
            status_map[stage] = "대기"
        elif checked > 0 and unchecked > 0:
            status_map[stage] = "진행중"
        else:
            status_map[stage] = "대기"

    return status_map


def update_readme(readme_text: str, status_map: dict[str, str]) -> str:
    for stage, status in status_map.items():
        row_pattern = rf"^(\|\s*{re.escape(stage)}\s*\|\s*[^|]+\|\s*)([^|]+)(\s*\|.*)$"
        readme_text = re.sub(
            row_pattern,
            lambda m: f"{m.group(1)}{status}{m.group(3)}",
            readme_text,
            flags=re.MULTILINE,
        )
    return readme_text


def update_context(context_text: str, status_map: dict[str, str]) -> str:
    # Update headline summary.
    summary = (
        f"SPEC {status_map.get('SPEC', '대기')} · "
        f"RED {status_map.get('RED', '대기')} · "
        f"GREEN {status_map.get('GREEN', '대기')} · "
        f"REFACTOR {status_map.get('REFACTOR', '대기')}"
    )
    context_text = re.sub(
        r"(\*\*TDD 현황\*\*:\s*)(.+)$",
        rf"\1{summary}",
        context_text,
        flags=re.MULTILINE,
    )

    # Update status table rows for 4 TDD stages.
    for stage in ["SPEC", "RED", "GREEN", "REFACTOR"]:
        status = status_map.get(stage, "대기")
        row_pattern = rf"^(\|\s*{re.escape(stage)}\s*\|\s*[^|]+\|\s*)([^|]+)(\s*\|)\s*$"
        context_text = re.sub(
            row_pattern,
            lambda m: f"{m.group(1)}{status}{m.group(3)}",
            context_text,
            flags=re.MULTILINE,
        )
    return context_text


def main() -> None:
    todo_text = TODO_PATH.read_text(encoding="utf-8")
    readme_text = README_PATH.read_text(encoding="utf-8")
    context_text = CONTEXT_PATH.read_text(encoding="utf-8")

    status_map = parse_todo_status(todo_text)
    README_PATH.write_text(update_readme(readme_text, status_map), encoding="utf-8")
    CONTEXT_PATH.write_text(update_context(context_text, status_map), encoding="utf-8")

    print("Synced statuses:", ", ".join(f"{k}={v}" for k, v in status_map.items()))


if __name__ == "__main__":
    main()

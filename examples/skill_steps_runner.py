"""
Kỹ năng: đọc “skill” dạng JSON — checklist có thứ tự (pattern gần với skill AI / runbook).

Chạy:
  python skill_steps_runner.py --json data/skill_steps.sample.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_steps(path: Path) -> tuple[str, list[str]]:
    data: Any = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("JSON phải là object")
    name = str(data.get("name", "unnamed"))
    steps = data.get("steps")
    if not isinstance(steps, list) or not all(isinstance(s, str) for s in steps):
        raise ValueError("steps phải là list[str]")
    return name, steps


def main() -> None:
    parser = argparse.ArgumentParser(description="In checklist từ JSON (mô phỏng skill).")
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    try:
        name, steps = load_steps(args.json)
    except (OSError, json.JSONDecodeError, ValueError) as e:
        print(f"Lỗi: {e}", file=sys.stderr)
        raise SystemExit(2) from e

    print(f"Skill: {name}")
    for i, step in enumerate(steps, start=1):
        print(f"  {i}. {step}")


if __name__ == "__main__":
    main()

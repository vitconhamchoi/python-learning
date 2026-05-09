"""
Kỹ năng: JSON config + validate — pattern dùng trong app thật (thiếu key là báo lỗi rõ).

Chạy:
  python config_validate.py --config data/app_config.sample.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_KEYS = ("app_name", "version", "api_base")


def load_config(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"Không đọc được file: {e}", file=sys.stderr)
        raise SystemExit(2) from e
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"JSON không hợp lệ: {e}", file=sys.stderr)
        raise SystemExit(2) from e
    if not isinstance(data, dict):
        print("JSON gốc phải là object {}", file=sys.stderr)
        raise SystemExit(2)
    return data


def validate(cfg: dict[str, Any]) -> None:
    missing = [k for k in REQUIRED_KEYS if k not in cfg]
    if missing:
        print(f"Thiếu key bắt buộc: {', '.join(missing)}", file=sys.stderr)
        raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Đọc và kiểm tra config JSON.")
    parser.add_argument("--config", type=Path, required=True)
    args = parser.parse_args()

    cfg = load_config(args.config)
    validate(cfg)
    print("OK — các key bắt buộc đủ.")
    print(f"app_name={cfg['app_name']!r}, version={cfg['version']!r}")


if __name__ == "__main__":
    main()

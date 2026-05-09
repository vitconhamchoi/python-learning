"""
Kỹ năng: thống kê nhanh codebase — đếm file theo phần mở rộng (ứng dụng: báo cáo repo).

Chạy:
  python report_extensions.py --root ..
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Đếm số file theo extension.")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--top", type=int, default=15)
    args = parser.parse_args()

    root = args.root.resolve()
    counter: Counter[str] = Counter()

    for path in root.rglob("*"):
        if path.is_file():
            ext = path.suffix.lower() or "(no_ext)"
            counter[ext] += 1

    print(f"Root: {root}")
    for ext, n in counter.most_common(args.top):
        print(f"{n:6d}  {ext}")


if __name__ == "__main__":
    main()

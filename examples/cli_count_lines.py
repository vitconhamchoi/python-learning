"""
Kỹ năng: CLI + pathlib — quét project, đếm dòng code .py (ứng dụng: audit nhanh quy mô).

Chạy:
  python cli_count_lines.py --root .. --ext .py
  python cli_count_lines.py --root . --ext .md --top 5
"""

from __future__ import annotations

import argparse
from pathlib import Path


def count_lines(path: Path) -> int:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return -1
    return len(text.splitlines())


def main() -> None:
    parser = argparse.ArgumentParser(description="Đếm dòng theo phần mở rộng trong cây thư mục.")
    parser.add_argument("--root", type=Path, default=Path("."), help="Thư mục gốc")
    parser.add_argument("--ext", default=".py", help="Phần mở rộng, ví dụ .py hoặc .md")
    parser.add_argument("--top", type=int, default=10, help="In N file nhiều dòng nhất")
    args = parser.parse_args()

    root: Path = args.root.resolve()
    ext: str = args.ext if args.ext.startswith(".") else f".{args.ext}"

    rows: list[tuple[Path, int]] = []
    for path in root.rglob(f"*{ext}"):
        if path.is_file():
            n = count_lines(path)
            if n >= 0:
                rows.append((path, n))

    rows.sort(key=lambda x: x[1], reverse=True)
    total_files = len(rows)
    total_lines = sum(n for _, n in rows)

    print(f"Root: {root}")
    print(f"Tổng file {ext}: {total_files}, tổng dòng: {total_lines}")
    print(f"Top {args.top}:")
    for path, n in rows[: args.top]:
        rel = path.relative_to(root) if path.is_relative_to(root) else path
        print(f"  {n:6d}  {rel}")


if __name__ == "__main__":
    main()

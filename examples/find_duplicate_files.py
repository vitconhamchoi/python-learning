"""
Kỹ năng: hash file + quét cây thư mục — tìm file trùng nội dung (ứng dụng: dọn dữ liệu).

Chạy:
  python find_duplicate_files.py --root . --min-size 1
"""

from __future__ import annotations

import argparse
import hashlib
from collections import defaultdict
from pathlib import Path


def file_digest(path: Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Nhóm file trùng nội dung (SHA-256).")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--min-size", type=int, default=1, help="Bỏ qua file nhỏ hơn (bytes)")
    args = parser.parse_args()

    root = args.root.resolve()
    by_hash: dict[str, list[Path]] = defaultdict(list)

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            st = path.stat()
        except OSError:
            continue
        if st.st_size < args.min_size:
            continue
        try:
            d = file_digest(path)
        except OSError:
            continue
        by_hash[d].append(path)

    dup_groups = [paths for paths in by_hash.values() if len(paths) > 1]
    print(f"Nhóm trùng: {len(dup_groups)}")
    for paths in sorted(dup_groups, key=lambda ps: len(ps), reverse=True):
        print("-")
        for p in paths:
            print(f"  {p}")


if __name__ == "__main__":
    main()

"""
Kỹ năng: nén backup có chọn lọc — zipfile (ứng dụng: backup cấu hình / artifact nhỏ).

Chạy:
  python backup_folder_zip.py --src data --out backup-data.zip
"""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Zip một thư mục (không theo dõi symlink).")
    parser.add_argument("--src", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    src = args.src.resolve()
    if not src.is_dir():
        raise SystemExit("--src phải là thư mục")

    out = args.out.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(src.rglob("*")):
            if path.is_file():
                arc = path.relative_to(src)
                zf.write(path, arcname=str(Path(src.name) / arc))

    print(f"Đã tạo: {out}")


if __name__ == "__main__":
    main()

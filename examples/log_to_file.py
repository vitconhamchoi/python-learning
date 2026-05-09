"""
Kỹ năng: logging ra file — thay print trong script chạy định kỳ / server nhỏ.

Chạy:
  python log_to_file.py --log-dir ./logs
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path


def setup_logging(log_dir: Path) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "app.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Demo logging ghi file + console.")
    parser.add_argument("--log-dir", type=Path, default=Path("logs"))
    args = parser.parse_args()

    setup_logging(args.log_dir)
    logging.info("Bắt đầu job")
    logging.warning("Cảnh báo giả lập")
    logging.info("Kết thúc job")
    print(f"Đã ghi log vào: {(args.log_dir / 'app.log').resolve()}")


if __name__ == "__main__":
    main()

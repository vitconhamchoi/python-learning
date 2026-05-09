"""
Kỹ năng: CSV + aggregate — báo cáo doanh thu theo sản phẩm (ứng dụng: sales ops).

Chạy:
  python csv_sales_summary.py --csv data/sales.csv
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Tổng hợp doanh thu theo product từ CSV.")
    parser.add_argument("--csv", type=Path, required=True)
    args = parser.parse_args()

    revenue_by_product: dict[str, float] = defaultdict(float)
    with args.csv.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["product"].strip()
            qty = int(row["qty"])
            unit = float(row["unit_price"])
            revenue_by_product[product] += qty * unit

    for product in sorted(revenue_by_product, key=lambda p: revenue_by_product[p], reverse=True):
        total = revenue_by_product[product]
        print(f"{product:12s}  {total:,.0f} VND")


if __name__ == "__main__":
    main()

# Bài 07 — Thư viện chuẩn, CLI, môi trường

## 1. `argparse` — chương trình dòng lệnh

```python
import argparse

parser = argparse.ArgumentParser(description="Demo CLI")
parser.add_argument("--name", required=True, help="Tên hiển thị")
parser.add_argument("--times", type=int, default=1)
args = parser.parse_args()

for _ in range(args.times):
    print(f"Chào {args.name}")
```

Chạy thử: `python cli_demo.py --name An --times 2`

## 2. Biến môi trường `os.environ`

```python
import os

api_key = os.environ.get("API_KEY")
if not api_key:
    raise SystemExit("Thiếu biến môi trường API_KEY")
```

## 3. `datetime` và timezone

```python
from datetime import datetime, timezone

now_utc = datetime.now(timezone.utc)
print(now_utc.isoformat())
```

## 4. `collections`: `Counter`, `defaultdict`

```python
from collections import Counter, defaultdict

print(Counter("banana"))

dd = defaultdict(list)
dd["fruits"].append("apple")
print(dict(dd))
```

## 5. Virtual environment và pip (khái niệm bắt buộc)

Tạo môi trường riêng cho project (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -U pip
```

Cài package: `pip install httpx` (ví dụ). Liệt kê: `pip freeze > requirements.txt`.

## Bài tập nhanh

1. CLI nhận `--path` (thư mục), in danh sách file `.py` (gợi ý: `Path(path).rglob("*.py")`).
2. In ra giờ UTC hiện tại theo ISO 8601.

## Bài tiếp theo

→ [08 — Async & generator](./08-async-va-generator.md)

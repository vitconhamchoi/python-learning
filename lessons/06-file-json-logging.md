# Bài 06 — File, JSON, logging

## 1. `pathlib` — đường dẫn đa nền tảng

```python
from pathlib import Path

p = Path("data") / "note.txt"
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("xin chào\n", encoding="utf-8")
print(p.read_text(encoding="utf-8"))
```

## 2. `with` và file cổ điển

```python
with open("note.txt", "w", encoding="utf-8") as f:
    f.write("dòng 1\n")

with open("note.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

## 3. JSON

```python
import json
from pathlib import Path

cfg = {"theme": "dark", "lang": "vi"}
Path("cfg.json").write_text(
    json.dumps(cfg, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

loaded = json.loads(Path("cfg.json").read_text(encoding="utf-8"))
print(loaded["theme"])
```

## 4. Logging (thay `print` khi script lớn)

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(message)s",
)
logging.debug("ít quan trọng")
logging.info("bắt đầu xử lý")
logging.warning("có gì đó lạ")
```

## Bài tập nhanh

1. Đọc `cfg.json`; nếu thiếu key `theme` thì in lỗi rõ và thoát với mã khác 0 (`raise SystemExit(1)`).
2. Ghi log vào file `app.log` (tra cứu `logging.FileHandler`).

## Bài tiếp theo

→ [07 — Thư viện chuẩn & CLI](./07-thu-vien-chuan-va-cli.md)

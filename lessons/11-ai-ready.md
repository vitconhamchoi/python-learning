# Bài 11 — AI-ready: đọc skill, pipeline, gợi ý gọi LLM

Mục tiêu: sau bài này bạn **tự đọc** được tài liệu dạng hướng dẫn (skill, rule, checklist) và **viết script** hỗ trợ agent/tooling.

## 1. Đọc YAML an toàn (metadata / bước quy trình)

Cài: `pip install pyyaml`

```python
import yaml

text = """
name: summarize_folder
steps:
  - list markdown files
  - read each file
  - write summary
"""
doc = yaml.safe_load(text)
for i, step in enumerate(doc["steps"], start=1):
    print(f"{i}. {step}")
```

## 2. Pipeline: quét file → xử lý

```python
from pathlib import Path

def list_markdown(root: Path) -> list[Path]:
    return sorted(root.rglob("*.md"))

for p in list_markdown(Path("."))[:10]:
    print(p)
```

## 3. JSON là “hợp đồng” giữa các bước

```python
import json
from pathlib import Path

report = {"files": 3, "ok": True}
Path("report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
```

Thói quen: mỗi tool nhận/ trả **một schema rõ** (key bắt buộc, kiểu dữ liệu).

## 4. Gợi ý gọi API LLM (OpenAI SDK)

Cài: `pip install openai`

Đặt biến môi trường `OPENAI_API_KEY` (không đưa key vào git).

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Bạn là trợ lý code Python."},
        {"role": "user", "content": "Viết hàm kiểm tra palindrome, có type hints."},
    ],
)
print(resp.choices[0].message.content)
```

## 5. Cách **đọc một skill AI** hiệu quả

Tự hỏi nhanh:

1. **Khi nào** dùng skill này? (điều kiện kích hoạt)
2. **Input** là gì? (file, thư mục, biến môi trường)
3. **Output** mong đợi? (file nào, format nào)
4. **Cấm** gì? (không sửa X, không commit secret)
5. **Bước** thứ tự ra sao? — chuyển thành checklist hoặc vòng lặp trong script.

Ví dụ checklist in ra terminal:

```python
steps = ["Đọc SKILL.md", "Liệt kê input", "Chạy script thử", "Ghi report.json"]
for s in steps:
    print(f"[ ] {s}")
```

## Bài tập nhanh

1. Viết script: nhận `--root`, liệt kê tối đa 50 file `.md`, ghi `files.txt`.
2. Đọc một file skill bất kỳ trên máy bạn, viết `steps.yaml` với 5 bước bạn tự tóm.

## Kết thúc seri

Quay lại [mục lục](./README.md) và chọn **bài tập tổng hợp** để khóa kiến thức.

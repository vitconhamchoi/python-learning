# Bài 10 — Thực chiến: HTTP client và API nhỏ

## 1. HTTP client với `httpx`

Cài: `pip install httpx`

```python
import httpx

r = httpx.get("https://httpbin.org/get", timeout=10.0)
r.raise_for_status()
data = r.json()
print(data["url"])
```

POST JSON:

```python
r = httpx.post(
    "https://httpbin.org/post",
    json={"hello": "world"},
    timeout=10.0,
)
print(r.json()["json"])
```

## 2. API với FastAPI (gợi ý)

Cài: `pip install fastapi uvicorn`

`app.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ok": True}

@app.get("/add")
def add(a: int, b: int):
    return {"sum": a + b}
```

Chạy server:

```bash
uvicorn app:app --reload
```

Thử: mở trình duyệt `http://127.0.0.1:8000/ping` hoặc dùng `httpx.get("http://127.0.0.1:8000/add?a=2&b=3")`.

## 3. CSV nhanh (stdlib)

```python
import csv
from io import StringIO

raw = "name,age\nAn,20\nBình,22\n"
rows = list(csv.DictReader(StringIO(raw)))
print(rows[0]["name"])
```

## Bài tập nhanh

1. Viết script lấy JSON từ một public API (tra cứu API miễn phí), in 3 trường bạn quan tâm.
2. Thêm endpoint FastAPI `GET /hello?name=...` trả lời chào tên.

## Bài tiếp theo

→ [11 — AI-ready](./11-ai-ready.md)

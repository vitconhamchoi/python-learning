# Bài 09 — Kiểm thử và chất lượng code

## 1. `pytest` — test tối giản

Cài: `pip install pytest`

`cart.py`:

```python
class Cart:
    def __init__(self):
        self.items: list[tuple[str, int]] = []

    def add(self, name: str, qty: int = 1) -> None:
        if qty <= 0:
            raise ValueError("qty phải dương")
        self.items.append((name, qty))

    def total_qty(self) -> int:
        return sum(q for _, q in self.items)
```

`test_cart.py`:

```python
import pytest
from cart import Cart

def test_add_and_total():
    c = Cart()
    c.add("apple", 2)
    c.add("banana", 1)
    assert c.total_qty() == 3

def test_bad_qty():
    c = Cart()
    with pytest.raises(ValueError):
        c.add("x", 0)
```

Chạy: `pytest -q`

## 2. Type hints

```python
def mean(xs: list[float]) -> float:
    return sum(xs) / len(xs)
```

Công cụ tĩnh: `mypy` (cài riêng) để bắt lỗi kiểu sớm.

## 3. Định dạng và lint (vận hành dự án)

- **Ruff** hoặc **Flake8**: phát hiện lỗi phong cách / bug tiềm ẩn.
- **Black**: format thống nhất (hoặc dùng Ruff format).

Không cần thuộc lòng mọi rule ngay — quan trọng là **cùng team cùng một chuẩn**.

## Bài tập nhanh

1. Viết hàm `unique_sorted(words: list[str]) -> list[str]` và 3 test.
2. Chạy `pytest` và sửa cho đến khi xanh.

## Bài tiếp theo

→ [10 — HTTP & API](./10-thuc-chien-http-api.md)

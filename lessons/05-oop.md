# Bài 05 — Lập trình hướng đối tượng (OOP)

## 1. Class, `__init__`, method

```python
class User:
    def __init__(self, name: str):
        self.name = name

    def hello(self) -> str:
        return f"Hi {self.name}"

u = User("An")
print(u.hello())
```

## 2. Biến class vs biến instance

```python
class Counter:
    species = "counter"     # dùng chung (cẩn thận với mutable)

    def __init__(self):
        self.n = 0          # riêng từng object

    def inc(self):
        self.n += 1
```

## 3. Kế thừa đơn giản

```python
class Admin(User):
    def hello(self) -> str:
        return f"[ADMIN] {super().hello()}"

a = Admin("Bình")
print(a.hello())
```

## 4. `@dataclass` (Python hiện đại, ít boilerplate)

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p.x, p.y)
```

## 5. Ngoại lệ: EAFP (*Easier to Ask Forgiveness than Permission*)

```python
def to_int(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return None

print(to_int("42"), to_int("abc"))
```

`finally` luôn chạy; `else` chạy khi khối `try` không ném lỗi.

```python
try:
    r = 1 / 1
except ZeroDivisionError:
    r = None
else:
    print("Không chia 0")
finally:
    print("Xong")
```

## Bài tập nhanh

1. Class `BankAccount` với `deposit`, `withdraw` (không cho âm), `balance`.
2. Dùng `@dataclass` mô tả `Book(title, author, pages)`.

## Bài tiếp theo

→ [06 — File, JSON, logging](./06-file-json-logging.md)

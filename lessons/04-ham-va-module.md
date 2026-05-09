# Bài 04 — Hàm và module

## 1. Định nghĩa hàm, `return`

```python
def double(x):
    return x * 2

print(double(5))
```

## 2. Tham số mặc định và type hints

```python
def greet(name: str, loud: bool = False) -> str:
    msg = f"Hello {name}"
    return msg.upper() if loud else msg

print(greet("An"))
print(greet("An", loud=True))
```

**Lưu ý:** đừng dùng đối tượng thay đổi được (list, dict) làm giá trị mặc định — dùng `None` rồi gán trong hàm.

```python
def add_item(item, bag=None):
    if bag is None:
        bag = []
    bag.append(item)
    return bag
```

## 3. `*args` và `**kwargs`

```python
def show(*args, **kwargs):
    print("vị trí:", args)
    print("tên=", kwargs)

show(1, 2, a=3, b=4)
```

## 4. Lambda (hàm một dòng)

```python
square = lambda x: x * x
print(square(4))
```

Trong code thực tế, thường ưu tiên `def` hoặc comprehension cho dễ đọc.

## 5. Module và `import`

File `math_util.py`:

```python
def add(a, b):
    return a + b
```

File khác:

```python
import math_util
print(math_util.add(2, 3))

from math_util import add
print(add(2, 3))
```

## 6. `if __name__ == "__main__"`

Cho phép file vừa là **thư viện** vừa **chạy trực tiếp**.

```python
def main():
    print("Chạy như script")

if __name__ == "__main__":
    main()
```

## Bài tập nhanh

1. Viết hàm `clamp(x, low, high)` trả về `x` bị “kẹp” trong khoảng `[low, high]`.
2. Tách hàm tính BMI ra file `bmi.py` và gọi từ `main.py`.

## Bài tiếp theo

→ [05 — OOP](./05-oop.md)

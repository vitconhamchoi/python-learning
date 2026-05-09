# Bài 01 — Nền tảng: chạy Python, biến, kiểu dữ liệu

## 1. Chạy Python: file `.py` và REPL

**File script** — tạo `hello.py`:

```python
print("Xin chào, Python")
```

Chạy:

```bash
python hello.py
```

**REPL** (đọc–thực thi từng dòng): gõ `python` rồi Enter, thoát bằng `exit()` hoặc Ctrl+Z (Windows).

## 2. Biến và kiểu cơ bản

Python **không** khai báo kiểu bắt buộc ở biến (nhưng nên ghi **type hint** sau này).

```python
name = "An"        # str
age = 20           # int
height = 1.72      # float
active = True      # bool
```

Kiểm tra kiểu:

```python
print(type(name), type(age))
```

## 3. Chuỗi và f-string

```python
user = "Bình"
print(f"Chào {user}, năm sau {age + 1} tuổi")
```

## 4. Nhập từ bàn phím (`input`)

`input` luôn trả về **chuỗi**. Muốn số thì ép kiểu.

```python
ten = input("Tên bạn? ")
tuoi_str = input("Tuổi? ")
tuoi = int(tuoi_str)
print(f"{ten} năm sau {tuoi + 1} tuổi")
```

## 5. Toán tử và so sánh

```python
x, y = 10, 3
print(x + y, x // y, x % y)   # chia nguyên, dư
print(x > y, x == y, x != y)
print(x > 5 and y > 0)
print(x > 5 or y > 5)
```

## 6. Hàm có sẵn hay dùng

```python
nums = [3, 1, 4, 1, 5]
print(len(nums), sum(nums), min(nums), max(nums))
print(sorted(nums))
```

## Bài tập nhanh

1. Viết script in ra diện tích hình chữ nhật khi nhập `chieu_dai` và `chieu_rong`.
2. Nhập một số, in `True` nếu số đó chia hết cho 3.

## Bài tiếp theo

→ [02 — Điều khiển luồng](./02-dieu-khien-luong.md)

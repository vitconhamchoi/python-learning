# Bài 02 — Điều khiển luồng: `if`, vòng lặp

## 1. `if` / `elif` / `else`

Python dùng **thụt dòng** (indent, thường 4 space) để khối lệnh thuộc `if`.

```python
score = 7.5

if score >= 8:
    grade = "Giỏi"
elif score >= 5:
    grade = "Đạt"
else:
    grade = "Chưa đạt"

print(grade)
```

**Toán tử ba ngôi** (rút gọn một dòng):

```python
label = "lớn" if score >= 5 else "nhỏ"
```

## 2. Vòng lặp `for` và `range`

```python
for i in range(3):      # 0, 1, 2
    print(i)

for i in range(2, 5):   # 2, 3, 4
    print(i)

for ch in "abc":
    print(ch)
```

## 3. `while`

```python
n = 0
while n < 3:
    print(n)
    n += 1
```

## 4. `break` và `continue`

```python
for i in range(10):
    if i == 2:
        continue    # bỏ qua lần này
    if i == 5:
        break       # thoát vòng lặp
    print(i)
```

## 5. `for`–`else` (ít dùng nhưng hữu ích)

Khối `else` của `for` chạy khi vòng lặp **không** bị `break`.

```python
for x in [1, 2, 3]:
    if x == 0:
        break
else:
    print("Không gặp 0, không break")
```

## Bài tập nhanh

1. In bảng cửu chương 5 (1→10).
2. Nhập `n`, tính tổng `1 + 2 + ... + n` bằng vòng lặp.

## Bài tiếp theo

→ [03 — Cấu trúc dữ liệu](./03-cau-truc-du-lieu.md)

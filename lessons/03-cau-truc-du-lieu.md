# Bài 03 — Cấu trúc dữ liệu: list, tuple, dict, set

## 1. List (danh sách, có thứ tự, đổi được)

```python
a = [1, 2, 3]
a.append(4)
a[0] = 10
print(a[1:])    # cắt từ index 1 tới hết
print(a[-1])    # phần tử cuối
```

## 2. Tuple (bất biến, thường dùng cho “bản ghi” nhỏ)

```python
point = (3, 4)
# point[0] = 1  # Lỗi: tuple không đổi được
x, y = point    # unpack
```

## 3. Dict (ánh xạ key → value)

```python
user = {"name": "An", "role": "dev"}
user["email"] = "an@example.com"
print(user.get("phone", "không có"))   # tránh KeyError
```

Lặp dict:

```python
for key, value in user.items():
    print(key, value)
```

## 4. Set (tập hợp, không trùng, không thứ tự cố định)

```python
seen = {1, 2, 2, 3}
seen.add(4)
print(seen)
```

## 5. List / dict comprehension

```python
squares = [x * x for x in range(6) if x % 2 == 0]
word_len = {w: len(w) for w in ["a", "bb", "ccc"]}
print(squares, word_len)
```

## 6. Chuỗi: `split`, `join`, `strip`

```python
s = "  a, b, c  "
parts = [p.strip() for p in s.split(",")]
print("|".join(parts))
```

## Bài tập nhanh

1. Đếm số lần xuất hiện mỗi chữ cái trong một chuỗi (gợi ý: dùng dict).
2. Cho list số, tạo list mới chỉ gồm số chẵn, bình phương từng phần tử.

## Bài tiếp theo

→ [04 — Hàm & module](./04-ham-va-module.md)

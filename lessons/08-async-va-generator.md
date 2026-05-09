# Bài 08 — Bất đồng bộ (`asyncio`) và generator

## 1. Vì sao cần `async`?

Khi chương trình **chờ I/O** (mạng, đĩa, DB), `async` giúp **không chặn** toàn bộ luồng xử lý như code đồng bộ đơn giản (trong một process — chi tiết runtime phức tạp hơn, nhưng ý tưởng là vậy).

## 2. `async` / `await` cơ bản

```python
import asyncio

async def job(n: int) -> int:
    await asyncio.sleep(0.1)   # giả lập tác vụ chờ
    return n * 2

async def main():
    a, b = await asyncio.gather(job(1), job(2))
    print(a, b)

asyncio.run(main())
```

## 3. Generator và `yield`

Generator **lười** — tạo từng giá trị khi cần, tiết kiệm bộ nhớ.

```python
def countdown(n: int):
    while n > 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)
```

## 4. Generator expression

```python
squares = (x * x for x in range(5))
print(sum(squares))
```

## Bài tập nhanh

1. Viết `async def fetch_all()` gọi `asyncio.gather` với 3 `job` khác nhau, in tổng kết quả.
2. Generator đọc file lớn theo dòng (yield từng dòng) thay vì `readlines()` một lần.

## Bài tiếp theo

→ [09 — Kiểm thử & chất lượng](./09-test-va-chat-luong.md)

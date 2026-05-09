# Seri học Python — từ zero tới thực chiến

Chào mừng. Các bài được sắp **từ cơ bản tới nâng cao**; trong mỗi phần lớn bạn có thể **nhảy có chủ đích** nếu đã biết phần trước.

## Cách học hiệu quả

1. Cài [Python 3.11+](https://www.python.org/downloads/).
2. Mỗi bài: đọc → **gõ lại** ví dụ → sửa một dòng xem kết quả thay đổi thế nào.
3. Chạy file: `python ten_file.py` hoặc thử nhanh: `python` (REPL).

## Mục lục

| STT | Bài | Nội dung chính |
|-----|-----|----------------|
| 00 | [Giới thiệu & lộ trình](./00-gioi-thieu-lo-trinh.md) | Mục tiêu, công cụ, thứ tự học |
| 01 | [Nền tảng: chạy Python, biến, kiểu](./01-nen-tang-bien-va-kieu.md) | Script, REPL, `str/int/float/bool`, f-string |
| 02 | [Điều khiển luồng](./02-dieu-khien-luong.md) | `if`, `for`, `while`, `range`, `break/continue` |
| 03 | [Cấu trúc dữ liệu](./03-cau-truc-du-lieu.md) | List, tuple, dict, set, comprehension |
| 04 | [Hàm & module](./04-ham-va-module.md) | Định nghĩa hàm, `*args/**kwargs`, `import`, `__main__` |
| 05 | [Lập trình hướng đối tượng](./05-oop.md) | Class, dataclass, ngoại lệ |
| 06 | [File, JSON, logging](./06-file-json-logging.md) | `pathlib`, JSON, `logging` |
| 07 | [Thư viện chuẩn & CLI](./07-thu-vien-chuan-va-cli.md) | `argparse`, `datetime`, `collections`, venv/pip |
| 08 | [Bất đồng bộ & generator](./08-async-va-generator.md) | `asyncio`, `yield` |
| 09 | [Kiểm thử & chất lượng](./09-test-va-chat-luong.md) | `pytest`, type hints, lint/format |
| 10 | [Thực chiến: HTTP & API](./10-thuc-chien-http-api.md) | `httpx`, FastAPI gợi ý |
| 11 | [AI-ready: đọc skill, tooling](./11-ai-ready.md) | YAML/JSON, pipeline file, gợi ý API LLM |

## Ví dụ ứng dụng thật (file `.py`)

**[Danh sách kỹ năng → script Python](../examples/README.md)** — CLI, JSON config, HTTP, CSV, hash trùng file, logging, zip backup, checklist skill, gọi LLM (tùy chọn).

## Bài tập tổng hợp (làm dần)

- Viết CLI đếm dòng từng file `.py` trong thư mục.
- Đọc/ghi `config.json` và báo lỗi rõ nếu thiếu key.
- Class `ShoppingCart` + vài test `pytest`.
- API nhỏ (FastAPI) + gọi bằng `httpx`.

Chúc bạn học vững và code được ngay sau mỗi bài.

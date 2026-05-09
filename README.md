# 🐍 Python Learning

Seri học Python thực chiến — từ cơ bản đến ứng dụng thật, viết bằng tiếng Việt.

---

## Giới thiệu

Repo này gồm hai phần:

| Phần | Mô tả |
|------|-------|
| 📖 [`lessons/`](./lessons/) | 12 bài Markdown, từ cú pháp cơ bản đến async, testing, HTTP API và AI tooling |
| ⚙️ [`examples/`](./examples/) | 10+ script Python chạy được ngay, minh họa các kỹ năng thực tế |

---

## Yêu cầu

- **Python 3.11+** — tải tại [python.org](https://www.python.org/downloads/)
- Trình soạn thảo (VS Code, Cursor, v.v.) và terminal

Kiểm tra phiên bản:

```bash
python --version
```

---

## Bắt đầu nhanh

```bash
# 1. Clone repo
git clone https://github.com/vitconhamchoi/python-learning.git
cd python-learning

# 2. Đọc bài học (Markdown)
# Mở lessons/00-gioi-thieu-lo-trinh.md trong trình soạn thảo hoặc xem trên GitHub

# 3. Chạy thử ví dụ
cd examples
python cli_count_lines.py .
```

---

## Lộ trình học

| Giai đoạn | Bài |
|-----------|-----|
| Tuần 1–2 | 01 → 03 (cú pháp, luồng điều khiển, cấu trúc dữ liệu) |
| Tuần 3–4 | 04 → 06 (hàm, OOP, file & JSON) |
| Tuần 5–6 | 07 → 09 (stdlib, CLI, testing) |
| Tùy chọn | 10 (HTTP/API), 11 (AI tooling) |

---

## Mục lục bài học

| STT | Bài | Nội dung chính |
|-----|-----|----------------|
| 00 | [Giới thiệu & lộ trình](./lessons/00-gioi-thieu-lo-trinh.md) | Mục tiêu, công cụ, thứ tự học |
| 01 | [Nền tảng: biến & kiểu](./lessons/01-nen-tang-bien-va-kieu.md) | Script, REPL, `str/int/float/bool`, f-string |
| 02 | [Điều khiển luồng](./lessons/02-dieu-khien-luong.md) | `if`, `for`, `while`, `range`, `break/continue` |
| 03 | [Cấu trúc dữ liệu](./lessons/03-cau-truc-du-lieu.md) | List, tuple, dict, set, comprehension |
| 04 | [Hàm & module](./lessons/04-ham-va-module.md) | Định nghĩa hàm, `*args/**kwargs`, `import` |
| 05 | [Lập trình hướng đối tượng](./lessons/05-oop.md) | Class, dataclass, ngoại lệ |
| 06 | [File, JSON, logging](./lessons/06-file-json-logging.md) | `pathlib`, JSON, `logging` |
| 07 | [Thư viện chuẩn & CLI](./lessons/07-thu-vien-chuan-va-cli.md) | `argparse`, `datetime`, `collections`, venv/pip |
| 08 | [Bất đồng bộ & generator](./lessons/08-async-va-generator.md) | `asyncio`, `yield` |
| 09 | [Kiểm thử & chất lượng](./lessons/09-test-va-chat-luong.md) | `pytest`, type hints, lint/format |
| 10 | [Thực chiến: HTTP & API](./lessons/10-thuc-chien-http-api.md) | `httpx`, FastAPI |
| 11 | [AI-ready](./lessons/11-ai-ready.md) | YAML/JSON, pipeline file, gọi LLM |

---

## Ví dụ thực tế

Script trong [`examples/`](./examples/) chạy được ngay, phần lớn chỉ cần Python chuẩn (stdlib):

| File | Kỹ năng |
|------|---------|
| [`cli_count_lines.py`](./examples/cli_count_lines.py) | CLI với `argparse`, đếm dòng code |
| [`config_validate.py`](./examples/config_validate.py) | Đọc & validate cấu hình JSON |
| [`fetch_json_stdlib.py`](./examples/fetch_json_stdlib.py) | HTTP GET, parse JSON (không cần package ngoài) |
| [`fetch_parallel_stdlib.py`](./examples/fetch_parallel_stdlib.py) | Tải song song URL với `ThreadPoolExecutor` |
| [`csv_sales_summary.py`](./examples/csv_sales_summary.py) | Đọc CSV, gom nhóm, xuất báo cáo |
| [`find_duplicate_files.py`](./examples/find_duplicate_files.py) | Hash SHA-256, tìm file trùng nội dung |
| [`log_to_file.py`](./examples/log_to_file.py) | Ghi log ra file & console |
| [`report_extensions.py`](./examples/report_extensions.py) | Thống kê file theo extension |
| [`backup_folder_zip.py`](./examples/backup_folder_zip.py) | Backup thư mục ra `.zip` |
| [`skill_steps_runner.py`](./examples/skill_steps_runner.py) | Đọc runbook JSON, in checklist |
| [`openai_chat_minimal.py`](./examples/openai_chat_minimal.py) | Gọi OpenAI Chat API *(cần `pip install openai`)* |

---

## Cách học hiệu quả

1. Đọc bài Markdown → **gõ lại** ví dụ (không copy-paste).
2. Thay đổi một dòng nhỏ và quan sát kết quả thay đổi như thế nào.
3. Khi gặp lỗi: đọc **traceback từ dưới lên** — dòng cuối thường chỉ rõ nguyên nhân.

---

## Giấy phép

Dự án mở — tự do học, fork, và chia sẻ.

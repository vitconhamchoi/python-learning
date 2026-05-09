# Ví dụ `.py` — kỹ năng & ứng dụng thật

Các script chạy được; phần lớn **chỉ cần Python chuẩn** (stdlib). Chạy trong thư mục `examples/` để đường dẫn `data/` đúng mặc định:

```bash
cd examples
python ten_script.py ...
```

## Danh sách kỹ năng → file

| Kỹ năng / tình huống thật | File | Ghi chú |
|---------------------------|------|---------|
| CLI với `argparse`, quét cây thư mục, thống kê quy mô code | [`cli_count_lines.py`](./cli_count_lines.py) | Đếm dòng theo `.py` / `.md`, in top N file |
| Đọc cấu hình JSON, validate key bắt buộc, thoát mã lỗi chuẩn | [`config_validate.py`](./config_validate.py) | Dùng mẫu [`data/app_config.sample.json`](./data/app_config.sample.json) |
| HTTP GET + parse JSON không cài thêm package | [`fetch_json_stdlib.py`](./fetch_json_stdlib.py) | `urllib` + `httpbin` |
| Đọc CSV, gom nhóm, báo cáo (sales / ops) | [`csv_sales_summary.py`](./csv_sales_summary.py) | Dữ liệu mẫu [`data/sales.csv`](./data/sales.csv) |
| Hash SHA-256, tìm file trùng nội dung | [`find_duplicate_files.py`](./find_duplicate_files.py) | Dọn duplicate, kiểm tra backup |
| `logging` ghi file + console | [`log_to_file.py`](./log_to_file.py) | Job định kỳ / daemon nhỏ |
| Thống kê repo: đếm file theo extension | [`report_extensions.py`](./report_extensions.py) | Báo cáo nhanh cấu trúc project |
| “Skill” / runbook dạng JSON, đọc và in checklist | [`skill_steps_runner.py`](./skill_steps_runner.py) | Mẫu [`data/skill_steps.sample.json`](./data/skill_steps.sample.json) |
| Tải song song URL, xử lý lỗi mạng | [`fetch_parallel_stdlib.py`](./fetch_parallel_stdlib.py) | `ThreadPoolExecutor` + `urllib` |
| Backup thư mục ra `.zip` có chọn file | [`backup_folder_zip.py`](./backup_folder_zip.py) | `zipfile` |
| Gọi Chat API (OpenAI SDK), biến môi trường API key | [`openai_chat_minimal.py`](./openai_chat_minimal.py) | Cần `pip install openai`, xem [`requirements-optional.txt`](./requirements-optional.txt) |

## Phụ thuộc tùy chọn

```bash
pip install -r requirements-optional.txt
```

Chỉ bắt buộc nếu bạn chạy `openai_chat_minimal.py`.

## Liên hệ với các bài Markdown

| Bài học | Ví dụ gợi ý |
|---------|-------------|
| 07 — CLI & stdlib | `cli_count_lines.py`, `report_extensions.py`, `config_validate.py` |
| 06 — File & JSON | `config_validate.py`, `skill_steps_runner.py`, `log_to_file.py` |
| 10 — HTTP | `fetch_json_stdlib.py`, `fetch_parallel_stdlib.py` |
| 11 — AI-ready | `skill_steps_runner.py`, `openai_chat_minimal.py` |

Quay lại [mục lục bài học](../lessons/README.md).

"""
Kỹ năng: HTTP GET + JSON — chỉ dùng thư viện chuẩn (urllib), không cần pip thêm.

Chạy:
  python fetch_json_stdlib.py
  python fetch_json_stdlib.py --url https://httpbin.org/uuid
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from typing import Any


def fetch_json(url: str, timeout: float = 15.0) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": "python-learning-examples/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        body = resp.read().decode(charset, errors="replace")
    return json.loads(body)


def main() -> None:
    parser = argparse.ArgumentParser(description="GET JSON bằng urllib (stdlib).")
    parser.add_argument(
        "--url",
        default="https://httpbin.org/get",
        help="Endpoint trả JSON",
    )
    args = parser.parse_args()

    try:
        data = fetch_json(args.url)
    except urllib.error.HTTPError as e:
        print(f"HTTP lỗi: {e.code} {e.reason}", file=sys.stderr)
        raise SystemExit(1) from e
    except urllib.error.URLError as e:
        print(f"Mạng/URL lỗi: {e.reason}", file=sys.stderr)
        raise SystemExit(1) from e
    except json.JSONDecodeError as e:
        print(f"Phản hồi không phải JSON: {e}", file=sys.stderr)
        raise SystemExit(1) from e

    print(json.dumps(data, ensure_ascii=False, indent=2)[:2000])


if __name__ == "__main__":
    main()

"""
Kỹ năng: tải song song (I/O) — concurrent.futures + urllib (ứng dụng: crawl nhẹ, kiểm tra URL).

Chạy:
  python fetch_parallel_stdlib.py
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed


URLS = (
    "https://httpbin.org/status/200",
    "https://httpbin.org/bytes/1024",
    "https://httpbin.org/json",
)


def fetch_bytes(url: str, timeout: float = 20.0) -> tuple[str, int, str | None]:
    req = urllib.request.Request(url, headers={"User-Agent": "python-learning-examples/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
        return url, len(body), None
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
        return url, -1, str(e)


def main() -> None:
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(fetch_bytes, u) for u in URLS]
        for fut in as_completed(futures):
            url, size, err = fut.result()
            if err:
                print(f"FAIL {url}  ({err})", file=sys.stderr)
            else:
                print(f"OK   {url}  bytes={size}")

    # Một endpoint JSON minh họa parse nhanh
    req = urllib.request.Request(
        "https://httpbin.org/json",
        headers={"User-Agent": "python-learning-examples/1.0"},
    )
    with urllib.request.urlopen(req, timeout=20.0) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    slideshow = data.get("slideshow", {})
    print("Sample JSON title:", slideshow.get("title"))


if __name__ == "__main__":
    main()

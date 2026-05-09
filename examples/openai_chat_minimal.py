"""
Kỹ năng: gọi LLM qua API — pattern thật (biến môi trường, lỗi thiếu package/key).

Cài thêm:
  pip install openai

Chạy:
  set OPENAI_API_KEY=...   (Windows)
  python openai_chat_minimal.py --prompt "Viết hàm is_even(n:int)->bool"
"""

from __future__ import annotations

import argparse
import os
import sys


def main() -> None:
    try:
        from openai import OpenAI
    except ImportError:
        print("Thiếu package: pip install openai", file=sys.stderr)
        raise SystemExit(2)

    parser = argparse.ArgumentParser(description="Gọi Chat Completions (OpenAI SDK).")
    parser.add_argument("--model", default="gpt-4o-mini")
    parser.add_argument("--prompt", required=True)
    args = parser.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        print("Thiếu biến môi trường OPENAI_API_KEY", file=sys.stderr)
        raise SystemExit(1)

    client = OpenAI(api_key=key)
    resp = client.chat.completions.create(
        model=args.model,
        messages=[{"role": "user", "content": args.prompt}],
    )
    print(resp.choices[0].message.content or "")


if __name__ == "__main__":
    main()

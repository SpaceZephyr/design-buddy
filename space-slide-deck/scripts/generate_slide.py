#!/usr/bin/env python3
"""
Slide Image Generator - 使用 LabNana GPT-image-2 生成演示文稿幻灯片

Usage:
    python3 generate_slide.py --prompt "..." --output /path/to/output.png

Env:
    LABNANA_API_KEY - LabNana API key (自动从 .labnana.env 读取)
"""

import argparse
import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error

# LabNana 配置
LABNANA_API_URL = "https://api.labnana.com"
LABNANA_MODEL = "gpt-image-2"
LABNANA_PROVIDER = "openai"

DEFAULT_ASPECT_RATIO = "16:9"
DEFAULT_RESOLUTION = "2K"
MAX_RETRIES = 3
RETRY_DELAY = 5


def _save_image_from_base64(base64_data, output_path):
    """Save base64 image data to file."""
    img_data = base64.b64decode(base64_data)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(img_data)
    return len(img_data)


def _do_http_request(endpoint, payload, headers, timeout=120):
    """Execute HTTP request with retry logic."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")

    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8")), None
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            error = {"code": e.code, "message": body[:500]}
            if e.code == 429 or e.code >= 500:
                if attempt < MAX_RETRIES - 1:
                    wait = RETRY_DELAY * (attempt + 1)
                    print(f"[INFO] 限流或服务器错误，{wait}秒后重试...", file=sys.stderr)
                    time.sleep(wait)
                    continue
            return None, error
        except Exception as e:
            error = {"code": -1, "message": str(e)}
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
                continue
            return None, error
    return None, {"code": -1, "message": "Max retries exceeded"}


def generate_slide(prompt, output_path, api_key, api_url=LABNANA_API_URL,
                   model=LABNANA_MODEL, provider=LABNANA_PROVIDER,
                   aspect_ratio=DEFAULT_ASPECT_RATIO, resolution=DEFAULT_RESOLUTION):
    """Call LabNana API to generate a slide image."""
    endpoint = f"{api_url}/openapi/v1/images/generation"

    payload = {
        "provider": provider,
        "model": model,
        "prompt": prompt,
        "imageConfig": {
            "aspectRatio": aspect_ratio,
            "imageSize": resolution
        }
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    print(f"[INFO] 正在调用 LabNana API 生成幻灯片...", file=sys.stderr)
    result, error = _do_http_request(endpoint, payload, headers)

    if error:
        print(f"[ERROR] LabNana API 错误: {error}", file=sys.stderr)
        return None

    # Extract image from response
    candidates = result.get("candidates", [])
    if not candidates:
        print(f"[WARN] API 响应中没有图片数据", file=sys.stderr)
        return None

    content = candidates[0].get("content", {})
    parts = content.get("parts", [])

    for part in parts:
        if "inlineData" in part:
            inline = part["inlineData"]
            base64_data = inline.get("data", "")
            if base64_data:
                size = _save_image_from_base64(base64_data, output_path)
                print(f"[OK] 幻灯片已保存: {output_path} ({size} bytes)", file=sys.stderr)
                return output_path

    print(f"[WARN] 响应中没有找到图片数据", file=sys.stderr)
    return None


def load_api_key():
    """Load API key from .labnana.env file."""
    # 首先检查环境变量
    env_key = os.environ.get("LABNANA_API_KEY")
    if env_key:
        return env_key

    # 然后尝试从 .labnana.env 文件读取
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_file = os.path.join(script_dir, "..", ".labnana.env")

    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                if line.startswith("LABNANA_API_KEY="):
                    return line.strip().split("=", 1)[1]

    return None


def main():
    parser = argparse.ArgumentParser(description="使用 GPT-image-2 生成演示文稿幻灯片")
    parser.add_argument("--prompt", "-p", required=True, help="幻灯片内容描述")
    parser.add_argument("--output", "-o", required=True, help="输出文件路径")
    parser.add_argument("--api-key", help="LabNana API key (可选，默认从 .labnana.env 读取)")
    parser.add_argument("--aspect-ratio", default=DEFAULT_ASPECT_RATIO,
                        help="宽高比: 1:1, 16:9, 21:9 (默认: 16:9)")
    parser.add_argument("--resolution", default=DEFAULT_RESOLUTION,
                        help="分辨率: 1K, 2K, 4K (默认: 2K)")
    args = parser.parse_args()

    # 获取 API key
    api_key = args.api_key
    if not api_key:
        api_key = load_api_key()
    if not api_key:
        print("[ERROR] 无法获取 LabNana API Key。请设置 LABNANA_API_KEY 环境变量或在 .labnana.env 中配置。", file=sys.stderr)
        sys.exit(1)

    # 生成图片
    result = generate_slide(
        prompt=args.prompt,
        output_path=args.output,
        api_key=api_key,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution
    )

    if result:
        print(f"[OK] 完成: {result}", file=sys.stderr)
        sys.exit(0)
    else:
        print("[ERROR] 幻灯片生成失败。", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

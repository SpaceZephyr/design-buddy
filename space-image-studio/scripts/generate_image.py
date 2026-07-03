#!/usr/bin/env python3
"""
Image Generator - 支持 Gemini API 和 LabNana API 生成图片

Usage:
    python3 generate_image.py --prompt "..." --output /path/to/output.png [--provider gemini|labnana] [--aspect-ratio 16:9] [--resolution 2K]

Env:
    GEMINI_API_KEY - Gemini API key
    LABNANA_API_KEY - LabNana API key (for gpt-image-2)
"""

import argparse
import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error

# Gemini 默认配置
GEMINI_API_URL = "https://generativelanguage.googleapis.com"
GEMINI_MODEL = "gemini-3-pro-image-preview"

# LabNana 默认配置
LABNANA_API_URL = "https://api.labnana.com"
LABNANA_MODEL = "gpt-image-2"
LABNANA_PROVIDER = "openai"

DEFAULT_ASPECT_RATIO = "16:9"
DEFAULT_RESOLUTION = "2K"
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds


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
                    print(f"[INFO] Retrying in {wait}s...", file=sys.stderr)
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


def generate_image_labnana(prompt, output_path, api_key, api_url=LABNANA_API_URL,
                           model=LABNANA_MODEL, provider=LABNANA_PROVIDER,
                           aspect_ratio=DEFAULT_ASPECT_RATIO, resolution=DEFAULT_RESOLUTION):
    """Call LabNana API to generate an image from prompt and save to output_path."""
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

    result, error = _do_http_request(endpoint, payload, headers)
    if error:
        print(f"[ERROR] LabNana API error: {error}", file=sys.stderr)
        return None

    # Extract image from LabNana response (format compatible with Gemini)
    candidates = result.get("candidates", [])
    if not candidates:
        print(f"[WARN] No candidates in LabNana response", file=sys.stderr)
        return None

    content = candidates[0].get("content", {})
    parts = content.get("parts", [])

    for part in parts:
        if "inlineData" in part:
            inline = part["inlineData"]
            base64_data = inline.get("data", "")
            if base64_data:
                size = _save_image_from_base64(base64_data, output_path)
                print(f"[OK] LabNana image saved: {output_path} ({size} bytes)")
                return output_path

    print(f"[WARN] No image data in LabNana response", file=sys.stderr)
    return None


def generate_image_gemini(prompt, output_path, api_key, api_url=GEMINI_API_URL,
                          model=GEMINI_MODEL, aspect_ratio=DEFAULT_ASPECT_RATIO,
                          resolution=DEFAULT_RESOLUTION):
    """Call Gemini API to generate an image from prompt and save to output_path."""
    endpoint = f"{api_url}/v1beta/models/{model}:generateContent"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {
                "aspectRatio": aspect_ratio,
                "imageSize": resolution
            }
        }
    }

    headers = {
        "x-goog-api-key": api_key,
        "Content-Type": "application/json"
    }

    result, error = _do_http_request(endpoint, payload, headers)
    if error:
        print(f"[ERROR] Gemini API error: {error}", file=sys.stderr)
        return None

    # Extract image from Gemini response
    candidates = result.get("candidates", [])
    if not candidates:
        print(f"[WARN] No candidates in Gemini response", file=sys.stderr)
        return None

    content = candidates[0].get("content", {})
    parts = content.get("parts", [])

    for part in parts:
        if "inlineData" in part and not part.get("thought"):
            inline = part["inlineData"]
            base64_data = inline.get("data", "")
            if base64_data:
                size = _save_image_from_base64(base64_data, output_path)
                print(f"[OK] Gemini image saved: {output_path} ({size} bytes)")
                return output_path

    print(f"[WARN] No image data in Gemini response", file=sys.stderr)
    return None


def generate_image(prompt, output_path, api_key, api_url=None,
                   model=None, aspect_ratio=DEFAULT_ASPECT_RATIO,
                   resolution=DEFAULT_RESOLUTION, provider="gemini"):
    """
    Generate image using specified provider (gemini or labnana).

    Args:
        prompt: Image generation prompt
        output_path: Output file path
        api_key: API key for the provider
        api_url: Optional custom API URL
        model: Optional custom model name
        aspect_ratio: Aspect ratio (default: 16:9)
        resolution: Image resolution (default: 2K)
        provider: 'gemini' or 'labnana' (default: gemini)
    """
    if provider == "labnana":
        if api_url is None:
            api_url = LABNANA_API_URL
        if model is None:
            model = LABNANA_MODEL
        return generate_image_labnana(
            prompt=prompt,
            output_path=output_path,
            api_key=api_key,
            api_url=api_url,
            model=model,
            aspect_ratio=aspect_ratio,
            resolution=resolution
        )
    else:  # gemini
        if api_url is None:
            api_url = GEMINI_API_URL
        if model is None:
            model = GEMINI_MODEL
        return generate_image_gemini(
            prompt=prompt,
            output_path=output_path,
            api_key=api_key,
            api_url=api_url,
            model=model,
            aspect_ratio=aspect_ratio,
            resolution=resolution
        )


def main():
    parser = argparse.ArgumentParser(description="Generate image via Gemini or LabNana API")
    parser.add_argument("--prompt", "-p", required=True, help="Image generation prompt")
    parser.add_argument("--output", "-o", required=True, help="Output file path")
    parser.add_argument("--api-key", help="API key (overrides env var)")
    parser.add_argument("--provider", choices=["gemini", "labnana"], default="labnana",
                        help="API provider (default: labnana)")
    parser.add_argument("--api-url", help="Custom API base URL")
    parser.add_argument("--model", help="Model name")
    parser.add_argument("--aspect-ratio", default=DEFAULT_ASPECT_RATIO,
                        help="Aspect ratio: 1:1, 2:3, 3:2, 3:4, 4:3, 9:16, 16:9, 21:9")
    parser.add_argument("--resolution", default=DEFAULT_RESOLUTION,
                        help="Resolution: 1K, 2K, 4K")
    args = parser.parse_args()

    # Determine API key based on provider
    api_key = args.api_key
    if not api_key:
        if args.provider == "labnana":
            api_key = os.environ.get("LABNANA_API_KEY", "")
            if not api_key:
                # Try loading from .env file
                env_file = os.path.join(os.path.dirname(__file__), "..", ".labnana.env")
                if os.path.exists(env_file):
                    with open(env_file) as f:
                        for line in f:
                            if line.startswith("LABNANA_API_KEY="):
                                api_key = line.strip().split("=", 1)[1]
                                break
            if not api_key:
                print("[ERROR] No LabNana API key provided. Use --api-key or set LABNANA_API_KEY.", file=sys.stderr)
                sys.exit(1)
        else:  # gemini
            api_key = os.environ.get("GEMINI_API_KEY", "")
            if not api_key:
                print("[ERROR] No Gemini API key provided. Use --api-key or set GEMINI_API_KEY.", file=sys.stderr)
                sys.exit(1)

    result = generate_image(
        prompt=args.prompt,
        output_path=args.output,
        api_key=api_key,
        api_url=args.api_url,
        model=args.model,
        aspect_ratio=args.aspect_ratio,
        resolution=args.resolution,
        provider=args.provider
    )

    if result:
        print(f"[OK] Done: {result}")
        sys.exit(0)
    else:
        print("[ERROR] Failed to generate image.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

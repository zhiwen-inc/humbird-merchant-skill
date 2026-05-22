#!/usr/bin/env python3
"""
Humbird API Client Script
Handles REST API requests to Humbird platform with proper authentication
"""
import json
import os
import sys
import base64
from pathlib import Path
import argparse
import requests

def main():
  parser = argparse.ArgumentParser(description='Humbird API Client')
  parser.add_argument('--method', '-m', required=True, choices=['GET', 'POST'],
                      help='HTTP request method (GET/POST)')

  parser.add_argument('--params', '-p', default='{}',
                      help='Additional JSON parameters for the request (default: {})')

  args = parser.parse_args()

  # Get API key from environment variable
  api_key = os.environ.get('HUMBIRD_API_KEY')

  if not api_key:
    print("ERROR: HUMBIRD_API_KEY environment variable not set",
          file=sys.stderr)
    sys.exit(1)



  # API endpoint (hardcoded as requested)
  api_url = "https://open.hihumbird.com/api/router"

  # Prepare headers
  headers = {
    'x-api-key': api_key,
    'Content-Type': 'application/json',
    'Accept-Language': 'zh'
  }

  # Prepare request data - api_type is always included as a required parameter
  request_data = {
    **json.loads(args.params)
  }


  if 'api_type' not in request_data:
    print(f"ERROR: Request failed: api_type is missing", file=sys.stderr)


  if request_data['api_type'] == 'gallery.picture.upload':
    request_data['image_data'] = image_to_base64(request_data['image_path'])
    del request_data['image_path']

  try:
    if args.method == 'GET':
      response = requests.get(api_url, headers=headers, params=request_data)
    else:  # POST
      response = requests.post(api_url, headers=headers, json=request_data)

    print(json.dumps(response.json(), indent=2, ensure_ascii=False))

  except requests.exceptions.RequestException as e:
    print(f"ERROR: Request failed: {e}", file=sys.stderr)
    sys.exit(1)
  except json.JSONDecodeError as e:
    print(f"ERROR: Failed to parse response JSON: {e}", file=sys.stderr)
    sys.exit(1)

def image_to_base64(
    image_path: str
) -> str:
  """
  将图片转换为 Base64 编码字符串。

  Args:
      image_path: 本地/网络图片路径

  Returns:
      Base64 编码的字符串（或 Data URL 字符串）

  """

  if image_path.startswith('http'):
    resp = requests.get(image_path, timeout=100)
    resp.raise_for_status()
    raw_bytes = resp.content
    # 从 Content-Type 头部获取 MIME
    content_type = resp.headers.get('Content-Type', '')
    if 'image' in content_type:
      mime_type = content_type.split(';')[0].strip()
    else:
      mime_type = None
  else:
    path = Path(image_path)
    if not path.exists():
      raise FileNotFoundError(f"文件不存在: {path}")
    if not path.is_file():
      raise ValueError(f"路径不是文件: {path}")
    raw_bytes = path.read_bytes()
    # 根据扩展名推测 MIME
    ext = path.suffix.lower()
    mime_map = {
      '.jpg': 'image/jpeg',
      '.jpeg': 'image/jpeg',
      '.png': 'image/png',
      '.gif': 'image/gif',
      '.bmp': 'image/bmp',
      '.webp': 'image/webp'
    }
    mime_type = mime_map.get(ext)

  if raw_bytes is None:
    raise ValueError("未能读取到图片数据")
  if mime_type is None:
    raise ValueError("未知的图片格式")

  # Base64 编码
  b64_str = base64.b64encode(raw_bytes).decode('utf-8')

  return f"data:{mime_type};base64,{b64_str}"

if __name__ == '__main__':
  main()

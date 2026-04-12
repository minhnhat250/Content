#!/usr/bin/env python3
"""
push-to-notion.py
Đẩy nội dung từ Claude vào Notion qua API Notion chính chủ.
Không cần MCP — chạy trực tiếp bằng Python.

Cách dùng:
  python push-to-notion.py --token <TOKEN> --parent <PAGE_ID> --content "<NỘI DUNG>"
  python push-to-notion.py --token <TOKEN> --parent <PAGE_ID> --file <FILE_PATH>
  python push-to-notion.py --interactive

Yêu cầu:
  pip install requests

Cài đặt:
  pip install requests
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from typing import Optional


# ─── Cấu hình ────────────────────────────────────────────────────────────────

NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION  = "2022-06-28"


# ─── Notion API Helpers ─────────────────────────────────────────────────────

def notion_headers(token: str) -> dict:
    return {
        "Authorization":   f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type":   "application/json",
    }


def notion_get(endpoint: str, token: str) -> dict:
    url = f"{NOTION_API_BASE}/{endpoint}"
    req = urllib.request.Request(url, headers=notion_headers(token))
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        raise RuntimeError(f"Notion API {e.code}: {body}") from e


def notion_post(endpoint: str, payload: dict, token: str) -> dict:
    url  = f"{NOTION_API_BASE}/{endpoint}"
    data = json.dumps(payload).encode()
    req  = urllib.request.Request(
        url, data=data, headers=notion_headers(token), method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        raise RuntimeError(f"Notion API {e.code}: {body}") from e


def notion_patch(endpoint: str, payload: dict, token: str) -> dict:
    url  = f"{NOTION_API_BASE}/{endpoint}"
    data = json.dumps(payload).encode()
    req  = urllib.request.Request(
        url, data=data, headers=notion_headers(token), method="PATCH"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        raise RuntimeError(f"Notion API {e.code}: {body}") from e


# ─── Xác minh token ─────────────────────────────────────────────────────────

def verify_token(token: str) -> dict:
    """Gọi /users/me để xác minh token hợp lệ."""
    result = notion_get("users/me", token)
    if result.get("object") == "error":
        raise RuntimeError(f"Token không hợp lệ: {result}")
    return result


# ─── Search pages / databases ──────────────────────────────────────────────

def search(token: str, query: str = "", filter_type: str = "") -> list[dict]:
    """
    Tìm pages/databases trong workspace.
    filter_type: "page" | "database" | "" (cả hai)
    """
    payload: dict = {"query": query, "page_size": 50}
    if filter_type:
        payload["filter"] = {"value": filter_type, "property": "object"}
    result = notion_post("search", payload, token)
    return result.get("results", [])


def list_pages(token: str, query: str = "") -> list[dict]:
    """Tìm chỉ pages."""
    return search(token, query, "page")


def list_databases(token: str, query: str = "") -> list[dict]:
    """Tìm chỉ databases."""
    return search(token, query, "database")


# ─── Markdown → Notion Blocks ───────────────────────────────────────────────

def md_to_notion_blocks(markdown: str) -> list[dict]:
    """
    Convert raw markdown string → danh sách Notion block objects.
    Xử lý: heading, code block, bulleted list, numbered list,
           quote, divider, paragraph (với inline formatting).
    """
    blocks: list[dict] = []
    lines  = markdown.splitlines()

    i = 0
    while i < len(lines):
        line = lines[i]

        # ── Code block ```...```
        if re.match(r"^```(\w*)", line):
            lang = re.match(r"^```(\w*)", line).group(1) or "plain text"
            code_lines: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            blocks.append({
                "object": "block",
                "type": "code",
                "code": {
                    "language": lang,
                    "rich_text": [{"type": "text", "text": {"content": "\n".join(code_lines)}}],
                },
            })
            i += 1
            continue

        # ── Heading 1 # ...
        if re.match(r"^# ", line):
            blocks.append(paragraph_block(line[2:], "heading_1"))
            i += 1
            continue

        # ── Heading 2 ## ...
        if re.match(r"^## ", line):
            blocks.append(paragraph_block(line[3:], "heading_2"))
            i += 1
            continue

        # ── Heading 3 ### ...
        if re.match(r"^### ", line):
            blocks.append(paragraph_block(line[4:], "heading_3"))
            i += 1
            continue

        # ── Divider ---
        if re.match(r"^---*$", line):
            blocks.append({"object": "block", "type": "divider", "divider": {}})
            i += 1
            continue

        # ── Blockquote > ...
        if re.match(r"^> ", line):
            content = line[2:]
            # collect continuation lines (no prefix)
            while i + 1 < len(lines) and not lines[i + 1].startswith(("#", "-", ">", "```", "1.")):
                if lines[i + 1].strip() == "":
                    break
                content += "\n" + lines[i + 1]
                i += 1
            blocks.append(paragraph_block(content, "quote"))
            i += 1
            continue

        # ── Bulleted list - ...
        if re.match(r"^- ", line):
            items = []
            while i < len(lines) and re.match(r"^- ", lines[i]):
                text = lines[i][2:]
                items.append(paragraph_block(text, "bulleted_list_item"))
                i += 1
            blocks.extend(items)
            continue

        # ── Numbered list 1. ...
        if re.match(r"^\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
                text = re.sub(r"^\d+\. ", "", lines[i])
                items.append(paragraph_block(text, "numbered_list_item"))
                i += 1
            blocks.extend(items)
            continue

        # ── Empty line → skip
        if line.strip() == "":
            i += 1
            continue

        # ── Paragraph (với inline formatting)
        para_lines = [line]
        while i + 1 < len(lines) and lines[i + 1].strip() != "":
            if re.match(r"^#{1,3} |^```|^---|^> |^- |\d+\. ", lines[i + 1]):
                break
            para_lines.append(lines[i + 1])
            i += 1
        blocks.append(paragraph_block("\n".join(para_lines), "paragraph"))
        i += 1

    return blocks


def paragraph_block(text: str, block_type: str = "paragraph") -> dict:
    """
    Tạo một Notion block với inline formatting support:
    **bold**, *italic*, `code`, [text](url)
    """
    if not text.strip():
        return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": []}}

    parts = parse_inline_formatting(text)

    block: dict = {
        "object": "block",
        "type":   block_type,
        block_type: {"rich_text": parts},
    }
    return block


def parse_inline_formatting(text: str) -> list[dict]:
    """
    Parse inline formatting trong text:
    - **bold**
    - *italic*
    - `code`
    - [text](url)
    Trả về danh sách rich_text objects.
    """
    # Regex: **bold**, *italic*, `code`, [text](url)
    pattern = re.compile(
        r"\*\*([^*]+)\*\*|\*([^*]+)\*|`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)"
    )

    segments = []
    last_end = 0

    for match in pattern.finditer(text):
        # Text trước match
        before = text[last_end : match.start()]
        if before:
            segments.append({"type": "text", "text": {"content": before}})

        bold, italic, code, link_text, link_url = match.groups()

        if bold is not None:
            segments.append({
                "type": "text",
                "text": {"content": bold},
                "annotations": {"bold": True, "italic": False, "code": False,
                               "strikethrough": False, "underline": False},
            })
        elif italic is not None:
            segments.append({
                "type": "text",
                "text": {"content": italic},
                "annotations": {"bold": False, "italic": True, "code": False,
                               "strikethrough": False, "underline": False},
            })
        elif code is not None:
            segments.append({
                "type": "text",
                "text": {"content": code},
                "annotations": {"bold": False, "italic": False, "code": True,
                               "strikethrough": False, "underline": False},
            })
        elif link_text is not None and link_url is not None:
            segments.append({
                "type": "text",
                "text": {"content": link_text, "link": {"url": link_url}},
            })

        last_end = match.end()

    # Text còn lại
    remaining = text[last_end:]
    if remaining:
        segments.append({"type": "text", "text": {"content": remaining}})

    if not segments:
        segments.append({"type": "text", "text": {"content": text}})

    return segments


# ─── Tạo Page / Block trong Notion ─────────────────────────────────────────

def create_page(
    token: str,
    parent_page_id: str,
    title: str,
    content_blocks: list[dict],
    icon: Optional[str] = None,
) -> dict:
    """
    Tạo một page mới trong parent_page_id.
    parent_page_id: ID của page cha (hoặc workspace = database_id).
    """
    payload = {
        "parent": {"page_id": parent_page_id},
        "properties": {
            "title": {
                "title": [
                    {"type": "text", "text": {"content": title}}
                ]
            }
        },
        "children": content_blocks,
    }
    if icon:
        payload["icon"] = {"emoji": icon}

    result = notion_post("pages", payload, token)
    return result


def append_blocks(token: str, page_id: str, blocks: list[dict]) -> dict:
    """
    Thêm blocks vào cuối page có sằn.
    """
    # Notion giới hạn 100 blocks mỗi request
    results = []
    for i in range(0, len(blocks), 100):
        chunk = blocks[i : i + 100]
        result = notion_patch(f"blocks/{page_id}/children", {"children": chunk}, token)
        results.append(result)
    return results[-1] if results else {}


def create_database_row(
    token: str,
    database_id: str,
    title: str,
    content_blocks: list[dict],
    extra_properties: Optional[dict] = None,
) -> dict:
    """
    Tạo một row mới trong database.
    """
    properties: dict = {
        "title": {
            "title": [
                {"type": "text", "text": {"content": title}}
            ]
        }
    }
    if extra_properties:
        properties.update(extra_properties)

    payload = {
        "parent": {"database_id": database_id},
        "properties": properties,
        "children": content_blocks,
    }
    result = notion_post("pages", payload, token)
    return result


# ─── Preview ─────────────────────────────────────────────────────────────────

def preview_markdown(markdown: str, max_lines: int = 50) -> str:
    """Hiển thị preview nội dung."""
    lines = markdown.splitlines()
    preview_lines = lines[:max_lines]
    preview = "\n".join(preview_lines)
    if len(lines) > max_lines:
        preview += f"\n\n... (+{len(lines) - max_lines} dòng còn lại)"
    return preview


# ─── CLI Interactive ─────────────────────────────────────────────────────────

def interactive(token: str):
    """Chế độ tương tác — hỏi từng bước."""
    print("=" * 60)
    print("  NOTION CONTENT PUSHER — Interactive Mode")
    print("=" * 60)

    # Xác minh token
    print("\n[1/5] Xác minh token...")
    user_info = verify_token(token)
    name = (
        user_info.get("name", "")
        or user_info.get("bot", {}).get("name", "")
        or "Unknown"
    )
    print(f"  ✓ Token hợp lệ — Workspace: {name}")

    # Chọn đích đến
    print("\n[2/5] Tìm page đích...")
    q = input("  Tìm page (Enter = tất cả): ").strip()
    pages = list_pages(token, q)
    if not pages:
        print("  ✗ Không tìm thấy page nào.")
        return
    print(f"  Tìm thấy {len(pages)} page:")
    for idx, page in enumerate(pages[:10], 1):
        title = extract_title(page)
        pid   = page["id"]
        print(f"    [{idx}] {title}")
        print(f"        ID: {pid}")

    choice = input("\n  Chọn số page đích (hoặc nhập ID trực tiếp): ").strip()
    if choice.isdigit():
        parent_id = pages[int(choice) - 1]["id"]
    else:
        parent_id = choice

    # Nhập nội dung
    print("\n[3/5] Nhập nội dung...")
    print("  Cách 1: Dán nội dung trực tiếp (nhập xong gõ Ctrl+D / Ctrl+Z)")
    print("  Cách 2: Nhập đường dẫn file (bắt đầu bằng @): ")
    content_input = input().strip()

    if content_input.startswith("@"):
        file_path = content_input[1:].strip()
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = content_input

    # Preview
    print("\n[4/5] Preview nội dung:")
    print("-" * 60)
    print(preview_markdown(content))
    print("-" * 60)
    confirm = input("\n  Nội dung đúng chứ? (y/n): ").strip().lower()
    if confirm != "y":
        print("  Đã hủy.")
        return

    # Chọn hành động
    print("\n[5/5] Chọn hành động:")
    print("  [1] Tạo page mới")
    print("  [2] Thêm block vào page đã chọn")
    action = input("  Chọn (1/2): ").strip()

    title_input = input("  Tiêu đề page: ").strip() or "Claude Export"
    icon_input   = input("  Icon (emoji, ví dụ 📝, Enter = không): ").strip() or None
    blocks = md_to_notion_blocks(content)

    print("\n  Đang đẩy vào Notion...")
    if action == "1":
        result = create_page(token, parent_id, title_input, blocks, icon_input)
    else:
        result = append_blocks(token, parent_id, blocks)

    if result.get("object") == "error":
        print(f"\n  ✗ Lỗi: {result['message']}")
        return

    page_url = result.get("url", "Không có URL")
    print(f"\n  ✓ Thành công!")
    print(f"  URL: {page_url}")


# ─── Utility ─────────────────────────────────────────────────────────────────

def extract_title(page: dict) -> str:
    """Trích title từ page object."""
    props = page.get("properties", {})
    for key, val in props.items():
        if val.get("type") == "title":
            parts = val.get("title", [])
            if parts:
                return "".join(p.get("plain_text", "") for p in parts)
    return page.get("id", "Untitled")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Đẩy nội dung markdown vào Notion (không cần MCP)."
    )
    parser.add_argument("--token", help="Notion Integration Token (ntn_...)")
    parser.add_argument("--parent", help="Page ID đích (hoặc @file để đọc từ file)")
    parser.add_argument("--content", help="Nội dung markdown trực tiếp")
    parser.add_argument("--file",    help="Đường dẫn file markdown (.md)")
    parser.add_argument("--title",   default="Claude Export", help="Tiêu đề page")
    parser.add_argument("--icon",    help="Emoji icon cho page, ví dụ '📝'")
    parser.add_argument("--action",  choices=["create", "append"],
                        default="create", help="Tạo page mới hay thêm vào page có sẵn")
    parser.add_argument("--interactive", action="store_true",
                        help="Chế độ tương tác")

    args = parser.parse_args()

    # Token: args hoặc env
    token = args.token or os.environ.get("NOTION_TOKEN", "")
    if not token:
        token = input("Nhập Notion Token (ntn_...): ").strip()

    # Interactive mode
    if args.interactive or (not args.parent and not args.content and not args.file):
        interactive(token)
        return

    # Đọc nội dung
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        print("Cần --content hoặc --file. Dùng --help để xem hướng dẫn.")
        sys.exit(1)

    # Parent: args hoặc nhập
    parent = args.parent or input("Nhập Page ID đích: ").strip()

    # Verify token
    print("Xác minh token...")
    verify_token(token)
    print("✓ Token hợp lệ")

    # Convert & push
    print("Convert markdown → Notion blocks...")
    blocks = md_to_notion_blocks(content)
    print(f"  → {len(blocks)} blocks")

    print(f"{'Tạo page mới' if args.action == 'create' else 'Thêm blocks'}...")
    if args.action == "create":
        result = create_page(token, parent, args.title, blocks, args.icon)
    else:
        result = append_blocks(token, parent, blocks)

    if result.get("object") == "error":
        print(f"✗ Lỗi: {result['message']}", file=sys.stderr)
        sys.exit(1)

    print(f"✓ Thành công! URL: {result.get('url', 'N/A')}")


if __name__ == "__main__":
    main()
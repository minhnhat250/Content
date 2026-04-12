---
name: notion-content-pusher
description: >
  Đẩy nội dung từ Claude vào Notion tự động 100%. Kích hoạt khi người dùng nói:
  'đẩy vào notion', 'đưa nội dung vào notion', 'tạo page notion', 'sync vào notion',
  'xuất ra notion', 'gửi sang notion', 'push to notion', 'lưu vào notion',
  'tạo note notion', 'thêm vào workspace notion', 'viết vào notion',
  'export to notion', 'notion cho tôi', 'đẩy page này vào notion'.
  KHÔNG dùng cho: đọc nội dung từ notion, backup notion ra file, tạo database từ đầu,
  lấy token/token bị lỗi xác thực.
---

# Notion Content Pusher

Đẩy nội dung bất kỳ từ Claude vào Notion workspace — tự động hoàn toàn, preview trước khi đẩy,
chọn đúng tài khoản & page đích.

---

## Khi nào dùng

- User nói "đẩy vào notion" kèm nội dung
- User mở file .md và muốn đẩy nguyên file vào Notion
- User chỉ định đoạn text cụ thể muốn tạo page trong Notion
- User muốn tạo page mới hoặc thêm block vào page có sẵn trong Notion

---

## Workflow Routing

| Workflow | Khi nào dùng |
|----------|--------------|
| `workflows/tu-dong.md` | Người dùng đã có token, muốn đẩy nội dung ngay |
| `workflows/cai-dat.md` | Lần đầu dùng, chưa có token hoặc muốn thêm token mới |
| `workflows/chon-tai-khoan.md` | Có nhiều token, muốn chọn workspace/tài khoản khác |

---

## Output

**Loại:** Notion Page / Block
**Tạo ra:**
- Page mới trong workspace Notion (nếu chọn tạo page mới)
- Block mới trong page có sẵn (nếu chọn thêm vào page)
**Hỗ trợ:** Text thuần, Markdown (tự convert sang Notion block), Code blocks

---

## Quick Process (mặc định — tự động)

### Bước 1: Xác nhận token đang dùng
Hỏi người dùng muốn dùng token nào trong danh sách đã lưu.
Nếu chưa có token → chuyển sang `workflows/cai-dat.md`.

**Tại sao:** Mỗi token = 1 workspace Notion khác nhau. Cần chọn đúng trước khi làm gì.

### Bước 2: List pages & databases trong workspace
Dùng `notion-search` (MCP) hoặc `GET /search` (API) để lấy danh sách pages/databases.
Hiển thị cho người dùng chọn đích đến.

**Tại sao:** Người dùng cần biết mình đang đẩy vào đâu trong workspace.

### Bước 3: Preview nội dung sẽ đẩy
Hiển thị nội dung dưới dạng xem trước (raw text, không transform).
Người dùng xác nhận đúng nội dung trước khi đẩy.

**Tại sao:** Nguyên tắc không đưa bừa — người dùng phải thấy chính xác cái gì sẽ được tạo trong Notion.

### Bước 4: Chọn đích đến & hành động
- **Tạo page mới:** Tạo page mới với tiêu đề do người dùng đặt, nội dung bên trong
- **Thêm vào page có sẵn:** Tìm page → thêm block nội dung vào cuối page đó
- **Thêm vào database:** Chọn database → tạo row mới với nội dung

**Tại sao:** Không phải lúc nào cũng muốn tạo page mới — có khi chỉ muốn bổ sung vào page hiện có.

### Bước 5: Đẩy vào Notion
Gọi API tạo page/block:
- **MCP:** Dùng `notion-create-page` hoặc `notion-append-block`
- **API:** Dùng `POST /pages`, `POST /blocks/{block_id}/children`
- **Script:** `python scripts/push-to-notion.py`

**Tại sao:** Đây là bước cuối cùng — thực hiện tạo content thực sự trong Notion.

### Bước 6: Báo kết quả
Hiển thị URL của page vừa tạo cho người dùng. Hỏi có muốn mở không.

---

## Lưu ý quan trọng

1. **Token lưu ở đâu:** Trong `~/.claude/skills/notion-content-pusher/references/tokens.md`
   (đường dẫn tuyệt đối: `~/.claude/.env` hoặc `references/tokens.md`)

2. **Nếu có MCP Notion:** Dùng MCP tool trước (nhanh hơn).
   Nếu MCP không hoạt động → fallback sang API thuần.

3. **Không bao giờ đẩy nếu người dùng chưa xác nhận Bước 3.**

4. **Markdown conversion:** Tự động convert:
   - `# Tiêu đề` → Notion heading_1
   - `## Tiêu đề` → heading_2
   - `**bold**` → bold text
   - `` `code` `` → code block
   - ```` ```lang` → code block with language
   - `- item` → bulleted list item
   - `1. item` → numbered list item
   - `> quote` → quote block
   - `---` → divider

---

## Tiêu chí Chất lượng

Output TỐT vs XẤU khác nhau ở đâu:
- **TỐT:** Người dùng thấy preview đầy đủ, tự chọn page đích, xác nhận trước, nhận URL kết quả
- **XẤU:** Đẩy thẳng không hỏi, không preview, không cho chọn đích, không báo kết quả

---

## References

- `references/tokens.md` — Danh sách token đã lưu (template)
- `references/notion-api-guide.md` — Hướng dẫn cách lấy Notion token
- `references/markdown-to-notion.md` — Bảng convert markdown → Notion blocks
- `references/page-template.md` — 3 template page chuẩn cho Notion

## Scripts

- `scripts/push-to-notion.py` — Script Python gọi API Notion trực tiếp (100% tự động, không cần MCP)

  **Cách chạy:**
  ```bash
  # Interactive mode
  python scripts/push-to-notion.py --interactive

  # Tạo page mới từ file
  python scripts/push-to-notion.py --token ntn_xxx --parent PAGE_ID --file @content.md --title "My Page"

  # Tạo page mới từ text trực tiếp
  python scripts/push-to-notion.py --token ntn_xxx --parent PAGE_ID --content "Nội dung markdown" --title "Title"

  # Thêm block vào page có sẵn
  python scripts/push-to-notion.py --token ntn_xxx --parent PAGE_ID --file @content.md --action append

  # Đọc token từ biến môi trường
  export NOTION_TOKEN=ntn_xxx
  python scripts/push-to-notion.py --interactive
  ```

  **Yêu cầu:** `pip install requests` (hoặc dùng urllib có sẵn trong Python stdlib — script hỗ trợ cả 2)

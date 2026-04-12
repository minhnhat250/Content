# Workflow: Tự động đẩy nội dung (Đã có token)

Dùng khi: người dùng đã có token Notion, đã lưu trong `references/tokens.md`.

## Điều kiện trước

- Token đã lưu trong `references/tokens.md`
- Người dùng chỉ định nội dung muốn đẩy

---

## Các bước

### Bước 1: Xác nhận nội dung muốn đẩy

**Hỏi người dùng:** "Bạn muốn đẩy nội dung nào? (1) File đang mở trong IDE, (2) Đoạn text bạn dán vào đây, (3) Tất cả nội dung trong cuộc trò chuyện"

- Nếu (1): Đọc file đang mở trong IDE bằng `Read` tool
- Nếu (2): Yêu cầu người dùng dán nội dung
- Nếu (3): Thu thập toàn bộ nội dung có trong context

**Tại sao:** Đây là bước chọn nội dung — tuyệt đối không đẩy bừa.

---

### Bước 2: Xác nhận token / workspace

**Hỏi:** "Dùng workspace nào?"
- Hiển thị danh sách token đã lưu trong `references/tokens.md`
- Nếu có 1 token → xác nhận luôn
- Nếu có nhiều token → yêu cầu chọn

**Tại sao:** Token = workspace = tài khoản Notion. Cần chọn đúng.

---

### Bước 3: Preview nội dung

Hiển thị nội dung sẽ đẩy DƯỚI DẠNG RAW TEXT, không transform.

**Format hiển thị:**
```
╔══════════════════════════════════════╗
║  PREVIEW — Nội dung sẽ đẩy vào Notion  ║
╠══════════════════════════════════════╣
║ [Hiển thị nội dung đầy đủ ở đây]      ║
╚══════════════════════════════════════╝

Đúng nội dung này chứ? (Có / Không / Chỉnh sửa)
```

**Nếu người dùng "Chỉnh sửa":** Mở chế độ cho người dùng nhập lại nội dung.

**Tại sao:** Preview trước = không đẩy bừa. Người dùng thấy chính xác cái gì sẽ được tạo.

---

### Bước 4: Chọn đích đến

**Hỏi:** "Bạn muốn đẩy vào đâu?"

| Tùy chọn | Hành động |
|----------|-----------|
| **A. Tạo page mới** | Hỏi tiêu đề page → tạo page mới |
| **B. Thêm vào page có sẵn** | List pages → người dùng chọn → append block |
| **C. Thêm vào database** | List databases → người dùng chọn → tạo row mới |

**Tại sao:** Đích đến khác nhau → API call khác nhau. Người dùng cần chọn.

**List pages (API):**
```
GET https://api.notion.com/v1/search
Headers: Authorization: Bearer <token>
         Notion-Version: 2022-06-28
```

---

### Bước 5: Tạo nội dung trong Notion

**A. Tạo page mới:**
```
POST https://api.notion.com/v1/pages
Body: { parent: { page_id: <parent_page_id> }, properties: { title: <title> }, children: <blocks> }
```

**B. Thêm vào page có sẵn:**
```
PATCH https://api.notion.com/v1/blocks/<page_id>/children
Body: { children: <blocks> }
```

**C. Thêm vào database:**
```
POST https://api.notion.com/v1/databases/<db_id>/query
Body: tạo row mới
```

**Markdown → Notion blocks:** Xem `references/markdown-to-notion.md`

**Tại sao:** Đây là bước thực thi — gọi API thực sự tạo content trong Notion.

---

### Bước 6: Báo kết quả

- Hiển thị URL của page vừa tạo
- Hỏi: "Bạn có muốn mở page trên trình duyệt không?"
- Nếu có: mở bằng `Bash` → `start <url>` (Windows) hoặc `open <url>` (Mac)

**Tại sao:** Kết quả cần rõ ràng, URL để người dùng verify.

---

## Kiểm tra Chất lượng

Trước khi hoàn thành, verify:

- [ ] Người dùng đã xác nhận nội dung ở Bước 3
- [ ] Người dùng đã chọn đích đến ở Bước 4
- [ ] API call trả về thành công (status 200)
- [ ] URL kết quả được hiển thị cho người dùng
- [ ] Không có bước nào tự động đẩy mà chưa hỏi người dùng
# Workflow: Cài đặt — Thêm token Notion mới

Dùng khi: người dùng chưa có token, hoặc muốn thêm token workspace mới.

## Điều kiện trước

- Người dùng có tài khoản Notion (đăng ký tại notion.so)
- Trình duyệt để thao tác trên notion.so

---

## Các bước

### Bước 1: Hướng dẫn tạo Notion Integration

**Đọc:** `references/notion-api-guide.md` để lấy hướng dẫn chi tiết.

**Tóm tắt nhanh cho người dùng:**

```
Để lấy Notion API Token, làm theo 3 bước:

1. Vào https://www.notion.so/my-integrations
2. Nhấn "New integration"
3. Đặt tên (vd: "Claude Content Pusher")
4. Chọn workspace muốn kết nối
5. Copy Internal Integration Secret (bắt đầu bằng "ntn_...")
6. Gửi token đó cho tôi ở đây
```

**Tại sao:** Người dùng cần biết chính xác cách lấy token trước khi nhập.

---

### Bước 2: Nhận & xác minh token

**Hỏi người dùng:** "Gửi token của bạn vào đây"

Nhận token dạng: `ntn_xxxxxxxxxxxxxxxxxxxx`

**Xác minh token bằng cách gọi API:**
```
GET https://api.notion.com/v1/users/me
Headers: Authorization: Bearer <token>
         Notion-Version: 2022-06-28
```

**Nếu thành công (200):** → Token hợp lệ, hiển thị tên workspace
**Nếu lỗi (401/403):** → Token không hợp lệ, yêu cầu người dùng kiểm tra lại

**Tại sao:** Không lưu token chưa xác minh. Phải chắc chắn token hoạt động.

---

### Bước 3: Hỏi tên hiển thị

**Hỏi:** "Bạn muốn đặt tên workspace này là gì?"
(Gợi ý: "Notion Cá Nhân", "Notion Công Việc", "Workspace A"...)

**Tại sao:** Token khó nhớ, cần tên gợi nhớ để chọn khi dùng nhiều tài khoản.

---

### Bước 4: Lưu token

Cập nhật `references/tokens.md` với token mới:

```markdown
# Notion Tokens — KHÔNG commit file này lên GitHub

## Workspace 1: Notion Cá Nhân
- Display name: Notion Cá Nhân
- Token: ntn_xxxxxxxxxxxxxxxxxxxx
- Workspace ID: (lấy từ API response)
- Ngày thêm: 2026-04-11

## Workspace 2: [Tên workspace]
- Display name: [Tên hiển thị]
- Token: [Token]
- ...
```

**Lưu ý bảo mật:**
- Nếu người dùng muốn bảo mật hơn → hỏi có muốn lưu vào 1Password không
- Khuyến nghị: thêm `.gitignore` cho `references/tokens.md`

**Tại sao:** Token cần được lưu trữ an toàn và có tên gợi nhớ.

---

### Bước 5: Chia sẻ page với Integration

**Hướng dẫn người dùng:**

```
Sau khi tạo integration xong, bạn cần cho phép Claude truy cập page:

1. Mở page muốn dùng trong Notion
2. Nhấn "..." (ba chấm) ở góc trên phải
3. Chọn "Connections" → "Connect to" → chọn integration của bạn
4. Lặp lại cho mỗi page muốn dùng
```

**Tại sao:** Notion API chỉ truy cập được page đã được chia sẻ với Integration. Đây là bước dễ bị quên nhất.

---

### Bước 6: Test kết nối

Gọi API search để xác nhận Integration hoạt động:
```
GET https://api.notion.com/v1/search
```

Nếu trả về danh sách pages → Kết nối thành công.
Nếu trả về rỗng → Cần chia sẻ page với Integration ở Bước 5.

---

## Kiểm tra Chất lượng

- [ ] Token đã được xác minh (API trả về 200)
- [ ] Token được lưu với tên gợi nhớ
- [ ] Người dùng đã biết cách chia sẻ page với Integration
- [ ] Test search trả về kết quả
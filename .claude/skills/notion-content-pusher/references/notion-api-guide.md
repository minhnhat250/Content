# Hướng dẫn lấy Notion API Token

## Tổng quan

Notion API sử dụng **Integration Token** (không phải đăng nhập Google).
Mỗi workspace Notion có một integration token riêng.

---

## Cách lấy Token

### Bước 1: Vào trang Integration

Mở trình duyệt, truy cập:
```
https://www.notion.so/my-integrations
```

### Bước 2: Tạo Integration mới

1. Nhấn **"+ New integration"**
2. Điền thông tin:
   - **Name:** `Claude Content Pusher` (hoặc tên bạn tự chọn)
   - **Associated workspace:** Chọn workspace Notion bạn muốn kết nối
   - **Type:** Internal (mặc định)
3. Nhấn **Submit**

### Bước 3: Copy Token

Sau khi tạo xong, bạn sẽ thấy:
- **Internal Integration Secret** — bắt đầu bằng `ntn_`
- Copy toàn bộ dòng đó

```
ntn_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Bước 4: Chia sẻ Page với Integration

**Quan trọng:** Integration không tự động thấy mọi page. Bạn cần chia sẻ từng page:

1. Mở page muốn dùng trong Notion
2. Nhấn **"..."** (ba chấm) ở góc trên bên phải
3. Chọn **"Connections"** → **"Connect to"**
4. Tìm và chọn integration bạn vừa tạo
5. Lặp lại cho mỗi page muốn dùng

---

## Các API endpoints chính

| Mục đích | Method | Endpoint |
|----------|--------|----------|
| Xác minh token | GET | `/v1/users/me` |
| Tìm pages | POST | `/v1/search` |
| Tạo page mới | POST | `/v1/pages` |
| Đọc page | GET | `/v1/pages/{page_id}` |
| Thêm block vào page | PATCH | `/v1/blocks/{block_id}/children` |
| Tạo database | POST | `/v1/databases` |
| Thêm row vào database | POST | `/v1/databases/{database_id}/pages` |

---

## Headers bắt buộc

```http
Authorization: Bearer <YOUR_TOKEN>
Notion-Version: 2022-06-28
Content-Type: application/json
```

---

## Cài đặt Integration (nếu cần nâng cao)

- **Public integration:** Dùng OAuth 2.0 — cho ứng dụng bên thứ ba
- **Internal integration:** Dùng token trực tiếp — cho cá nhân/script riêng
- **Capabilities:** Chọn Read / Insert / Update tùy nhu cầu

---

## Mẹo

- **Token bắt đầu bằng `ntn_`** = Internal Integration (dùng cho cá nhân)
- **Token bắt đầu bằng `oauth_`** = OAuth (cho ứng dụng public)
- Nếu API trả về empty array khi search → kiểm tra lại Bước 4 (chia sẻ page)
- Token có thể bị revoke từ trang `my-integrations`
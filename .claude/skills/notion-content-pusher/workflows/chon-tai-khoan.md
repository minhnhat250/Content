# Workflow: Chọn tài khoản / workspace

Dùng khi: có nhiều token đã lưu, người dùng muốn chọn hoặc đổi workspace.

## Điều kiện trước

- Có từ 2 token trở lên trong `references/tokens.md`
- Hoặc người dùng chủ động muốn đổi workspace

---

## Các bước

### Bước 1: Đọc danh sách token

Đọc `references/tokens.md` để lấy danh sách workspace đã lưu.

**Hiển thị danh sách:**
```
Bạn có các workspace sau:

  [1] Notion Cá Nhân    — thêm ngày 2026-04-01
  [2] Notion Công Việc  — thêm ngày 2026-04-05
  [3] Notion Dự Án X    — thêm ngày 2026-04-10

Chọn số hoặc nhập token mới:
```

### Bước 2: Người dùng chọn

| Lựa chọn | Hành động |
|----------|-----------|
| Chọn số [1-3] | Dùng token của workspace đó |
| Nhập "mới" | Chuyển sang `workflows/cai-dat.md` |
| Nhập token trực tiếp | Dùng token vừa nhập (không lưu) |
| Nhập "xóa" | Xóa token đã lưu (hỏi xác nhận trước) |

**Tại sao:** Nhiều tài khoản = cần cách chọn nhanh, không phải nhập token mỗi lần.

---

### Bước 3: Xác nhận workspace đang dùng

Sau khi chọn, gọi API xác nhận:
```
GET https://api.notion.com/v1/users/me
Headers: Authorization: Bearer <token>
```

Hiển thị: "Đang dùng: **[Tên Workspace]** ✓"

---

## Kiểm tra Chất lượng

- [ ] Danh sách hiển thị đầy đủ, đúng thứ tự
- [ ] Token đã chọn được xác minh (API trả về 200)
- [ ] Tên workspace hiển thị rõ ràng
# Workflow Nhanh — Bảng Chi Phí Cơ Bản

## Mục đích
Tạo bảng chi phí SaaS AI nhanh trong 1 lượt trả lời. Dùng khi người dùng đã có sẵn số liệu hoặc cần kết quả gấp.

## Khi nào dùng
- User đã biết chi phí hosting, API, số user ước tính
- User cần "ước lượng nhanh" trước khi đầu tư
- User muốn test 2–3 mức giá khác nhau

## Điều kiện trước
Cần ít nhất:
- Tên sản phẩm AI
- Tổng chi phí cố định ước tính/tháng (VND)
- Số user ước tính
- Giá bán mong muốn (hoặc "tư vấn giúp tôi")

## Các bước

### Bước 1: Xác nhận thông tin cơ bản
Nhận input từ user, xác nhận nhanh các con số. Nếu thiếu → dùng ước lượng phổ biến và ghi rõ.

### Bước 2: Tính chi phí — 3 dòng cốt lõi

```
1. Chi phí cố định/tháng:      xxx.xxx VND
2. Chi phí biến đổi/user/tháng: xxx VND × yy user = xxx.xxx VND
3. Chi phí nhân sự/tháng:       xxx.xxx VND
────────────────────────────────────────────────
TỔNG CHI PHÍ THÁNG:            xxx.xxx VND
```

### Bước 3: Tính điểm hòa vốn

```
Điểm hòa vốn = Tổng chi phí ÷ Giá gói
             = xxx.xxx ÷ xx.xxx = ~xx user/tháng
```

### Bước 4: Ma trận tỉ giá nhanh

| User | Doanh thu | Chi phí | Thu nhập | /user | OK? |
|------|-----------|---------|----------|-------|------|
| 10 | xxx.xxx | xxx.xxx | xxx.xxx | xx.xxx | ⚠️ |
| 50 | xxx.xxx | xxx.xxx | xxx.xxx | xx.xxx | ✅ |
| 100 | xxx.xxx | xxx.xxx | xxx.xxx | xx.xxx | ✅✅ |

### Bước 5: Đề xuất 3 gói cơ bản

- Starter tuần: xx.xxx VND
- Basic tháng: xx.xxx VND
- Pro tháng: xx.xxx VND

## Output
Bảng chi phí markdown trong chat, 1 lượt trả lời duy nhất.

## Kiểm tra Chất lượng
- [ ] Tổng chi phí được tính đúng
- [ ] Điểm hòa vốn được giải thích bằng lời
- [ ] Có đề xuất gói tuần
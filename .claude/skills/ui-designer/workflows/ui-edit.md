# Sửa UI Page Có Sẵn

## Mục đích
Sửa giao diện page có sẵn — **CHỈ UI, KHÔNG LOGIC**.
Nhìn vào UI cũ → cải thiện đẹp hơn → không đụng đến logic.

## Khi nào dùng
- User nói "sửa giao diện trang X"
- User nói "cải thiện UI page Y"
- User nói "làm đẹp trang này"
- User nói "improve UI", "fix styling"

## Điều kiện trước
- Biết file cần sửa nằm ở đâu
- Biết yêu cầu thẩm mỹ cụ thể của user

## Các bước

### Bước 1: Đọc toàn bộ file trước

**Đọc file UI cần sửa. KHÔNG BAO GIỜ sửa khi chưa đọc hết.**

Sau khi đọc → phân loại từng dòng:

| Loại | Dòng nào | Xử lý |
|------|---------|--------|
| **UI** | className, style, div, h1-h6, button, span | ĐÁNH DẤU → sẽ sửa |
| **Logic** | function, if/else, useState, API calls | ĐÁNH DẤU → KHÔNG ĐỤNG |

### Bước 2: Xác định yêu cầu thẩm mỹ

Hỏi hoặc xác định từ user:
- Style mong muốn: Modern / Minimalist / Bold / Dark / Light / Gradient?
- Màu chủ đạo: cụ thể hay tự chọn?
- Feedback: "Trang này tôi muốn đẹp hơn, chuyên nghiệp hơn"?

Nếu user không rõ → đề xuất: "Tôi sẽ làm theo style Modern + Minimalist, dùng system font, spacing đều, màu xanh dương nhấn — OK không?"

### Bước 3: Kiểm tra code trước khi code

**TRƯỚC KHI VIẾT bất kỳ dòng code nào, kiểm tra:**

1. **Ngôn ngữ/Framework:** React / Vue / Angular / HTML thuần?
2. **CSS approach:** Tailwind / SCSS / CSS modules / Styled Components / Inline?
3. **Tính nhất quán:** File này dùng convention gì? (BEM? Utility-first?)
4. **Lỗi syntax hiện có:** Có lỗi nào không? Báo user nếu có.

### Bước 4: Sửa UI — Bám sát nguyên tắc

**CHỈ sửa những thứ sau:**

#### a) Typography
- Font size: Heading to, body nhỏ hơn (hierarchy rõ)
- Font weight: Đậm cho heading, nhẹ cho body
- Line-height: 1.5 cho body, 1.2 cho heading
- Letter-spacing: h1 có thể âm nhẹ (-0.5px)

#### b) Spacing
- Padding/margin theo scale: 4px base (4, 8, 12, 16, 24, 32, 48, 64)
- Khoảng cách giữa các section: 48px - 64px
- Khoảng cách trong component: 16px - 24px

#### c) Màu sắc
- Primary color cho nút bấm chính
- Secondary cho nút phụ
- Text có 3 cấp: heading (đậm, to), body (thường), muted (nhạt)
- Background: không trắng phẳng → thêm subtle gradient hoặc tone-on-tone

#### d) Border & Shadow
- Border radius: 8px-16px cho cards, 6px cho inputs, 9999px cho pills
- Shadow: `0 4px 6px rgba(0,0,0,0.05)` nhẹ → `0 10px 25px rgba(0,0,0,0.1)` đậm
- Hover shadow: tăng nhẹ khi hover

#### e) Animation & Interaction
- Transition: `transition: all 200ms ease` cho hover
- Hover: scale(1.02) hoặc shadow tăng
- Focus: outline ring cho accessibility
- Loading: skeleton hoặc spinner nếu cần

#### f) Responsive
- Mobile-first approach
- Breakpoints: sm(640), md(768), lg(1024), xl(1280)
- Stack layout trên mobile, grid/flex trên desktop

### Bước 5: Viết code — CHỈ UI

**Quy tắc:**
- Giữ nguyên structure HTML/JSX — không thêm/bớt tag có logic
- CHỈ thay đổi: className, style, thêm CSS class
- Nếu cần thêm wrapper div cho layout → thêm, nhưng đảm bảo không ảnh hưởng logic
- Props truyền vào component → giữ nguyên, không thay đổi

### Bước 6: Review cuối cùng

**KIỂM TRA LẠI toàn bộ thay đổi:**

```
Checklist:
[ ] KHÔNG có dòng logic nào bị thay đổi?
[ ] Tất cả thay đổi chỉ là UI (className, style, spacing)?
[ ] Font sizes tuân thủ hierarchy?
[ ] Spacing đều theo scale?
[ ] Hover states đã thêm?
[ ] Focus states đã thêm?
[ ] Responsive breakpoints đã thêm?
[ ] Màu sắc đọc được (contrast đủ)?
[ ] Animation/transition mượt (không quá nhanh/quá chậm)?
```

**Nếu có dòng logic bị sửa → HOÀN TÁC NGAY và báo user.**

### Bước 7: Báo kết quả

Trình bày:
- File đã sửa
- Tổng số thay đổi
- Trước → Sau (mô tả)
- Cảnh báo nếu có lỗi syntax mới tạo

---

## Output

File UI đã sửa với:
- Chỉ thay đổi UI — LOGIC GIỮ NGUYÊN
- Giao diện đẹp hơn đáng kể

## Kiểm tra Chất lượng

- [ ] Logic file không bị thay đổi?
- [ ] UI đẹp hơn rõ rệt?
- [ ] Responsive hoàn chỉnh?
- [ ] Hover/focus states đầy đủ?
- [ ] Không có lỗi syntax mới?
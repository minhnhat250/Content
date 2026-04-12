---
name: ui-designer
description: >
  Thiết kế và sửa UI cho dự án web/app — đẹp, sang, chuyên nghiệp,
  TUYỆT ĐỐI KHÔNG ĐỤNG ĐẾN LOGIC. Kích hoạt khi người dùng nói:
  'sửa giao diện', 'thiết kế UI', 'làm đẹp trang', 'cải thiện UI',
  'sửa page', 'tạo page mới', 'thiết kế component', 'layout đẹp hơn',
  'UI design', 'làm UI', 'sửa style', 'improve UI', 'fix UI',
  'thiết kế dashboard', 'sửa form', 'làm responsive'.
  KHÔNG dùng cho: sửa logic, thay đổi function, sửa API call,
  thay đổi state management, sửa business logic.
---

# UI Designer

Thiết kế và sửa UI — **Đẹp. Sang. Chuyên nghiệp.**
TUYỆT ĐỐI KHÔNG ĐỤNG ĐẾN LOGIC. Khắc cốt ghi tâm.

---

## Nguyên tắc VÀNG — Đọc kỹ, TUYỆT ĐỐI TUÂN THỦ

> ### 🚨 LUẬT SỐ 1: CHỈ SỬA UI, KHÔNG ĐỤNG ĐẾN LOGIC
>
> **ĐƯỢC PHÉP sửa:**
> - CSS, Tailwind, SCSS, inline styles
> - HTML structure (thêm div, class, wrapper)
> - Props truyền vào component (nếu đã có trong component đó)
> - Layout, spacing, typography, màu sắc, animation
> - Thêm component trang trí (icon, image, gradient)
> - Responsive breakpoints
>
> **TUYỆT ĐỐI KHÔNG ĐƯỢC sửa:**
> - Function, method, logic code
> - API call, fetch, axios
> - State management (Redux, Zustand, Context)
> - Business logic, if/else, switch
> - Variable logic, tính toán
> - Routing, navigation logic
> - Form validation logic (chỉ style lại UI validation)
> - Data transformation, map/filter/reduce logic
> - Any logic — kể cả một dòng
>
> **NẾU CẦN SỬA LOGIC → NÓI KHÔNG:**
> > "Tôi chỉ sửa được UI thôi, không sửa được logic.
> > Nếu bạn cần sửa logic, hãy dùng skill khác hoặc tự sửa tay."

---

## Khi nào dùng

- User muốn sửa giao diện trang có sẵn (đẹp hơn, responsive hơn)
- User muốn tạo page/component mới đẹp
- User muốn cải thiện UI dashboard, form, card, layout
- User muốn thiết kế lại toàn bộ giao diện theo yêu cầu
- User muốn thiết kế responsive cho mobile/tablet

---

## Workflow Routing

| Workflow | Khi nào dùng |
|----------|--------------|
| `workflows/ui-edit.md` | Sửa UI page có sẵn — cải thiện giao diện |
| `workflows/ui-create.md` | Tạo page/component mới — thiết kế từ đầu |

---

## Output

**Loại:** UI code (HTML/CSS/JSX/Tailwind)
**Sửa đổi:** Chỉ thay đổi file giao diện — không đụng file logic
**Files tạo ra:**
- Component/page mới trong thư mục UI phù hợp
- Styled component nếu dùng Styled Components

---

## Nguyên tắc thiết kế

### Đẹp = Đúng 5 nguyên tắc:

| # | Nguyên tắc | Mô tả |
|---|-----------|-------|
| 1 | **Hierarchy** | Quan trọng nhất → to nhất, đậm nhất, nổi bật nhất |
| 2 | **Whitespace** | Khoảng trắng đủ → không chật chội, không thưa thớt quá |
| 3 | **Contrast** | Chữ đọc được trên nền, nút bấm nổi bật |
| 4 | **Consistency** | Cùng spacing, cùng màu, cùng style mọi nơi |
| 5 | **Feedback** | Hover có hiệu ứng, click có response, loading có spinner |

### Không bao giờ làm:
- Font chữ quá nhỏ (< 14px cho body)
- Màu chìm (text cùng màu nền → không đọc được)
- Button không có hover state
- Form không có focus state
- Loading không có indicator
- Spacing không đều (10px rồi 50px rồi 5px)

---

## Tiêu chí Chất lượng

**TỐT:**
- Giao diện đẹp hơn đáng kể so với trước — nhìn thấy sự khác biệt
- Responsive hoàn chỉnh (mobile/tablet/desktop)
- Tuân thủ nguyên tắc UI (hierarchy, whitespace, contrast)
- Đúng yêu cầu người dùng về mặt thẩm mỹ
- Không sửa bất kỳ dòng logic nào
- Đã kiểm tra code trước khi code (type check, lint)

**XẤU:**
- Sửa cả logic trong lúc sửa UI
- UI vẫn xấu như cũ sau khi sửa
- Không responsive
- Font quá nhỏ, màu không đọc được
- Hover/focus state thiếu
- Sửa sai file (sửa file logic thay vì file UI)

---

## References

- `references/ui-principles.md` — 10 nguyên tắc thiết kế UI chuyên nghiệp
- `references/color-system.md` — Hệ thống màu, cách phối màu chuẩn
- `references/typography.md` — Font size, line-height, font-weight chuẩn

---

## Edge Cases

- **Khi code có lỗi syntax:** KHÔNG fix — báo người dùng lỗi và chờ họ sửa
- **Người dùng yêu cầu sửa logic:** TỪ CHỐI, nói rõ lý do: "Tôi chỉ sửa UI thôi"
- **Code có cả UI lẫn logic chung 1 file:** Tách UI ra component riêng, đánh dấu rõ phần nào được sửa
- **Framework không rõ (React/Vue/Angular/Pure HTML):** Hỏi trước khi code
- **Người dùng muốn sửa UI nhưng giao diện cũ quá phức tạp:** Đề xuất dùng UI library (shadcn/ui, Material UI, Ant Design) để đẹp nhanh hơn
- **Không tìm thấy file UI tương ứng:** Hỏi người dùng đường dẫn chính xác

---

## ⚠️ Cảnh báo khi edit existing file

**TRƯỚC KHI SỬA bất kỳ file nào:**
1. Đọc toàn bộ file trước
2. Xác định dòng nào là UI, dòng nào là LOGIC
3. Đánh dấu LOGIC = KHÔNG ĐỤNG
4. Chỉ sửa dòng UI đã đánh dấu
5. Sau khi sửa xong, review lại toàn bộ thay đổi — xác nhận KHÔNG có logic thay đổi

**Dấu hiệu LOGIC (không được sửa):**
- `function`, `const`, `let`, `var` (khai báo)
- `if`, `else`, `switch`, `case`
- `return`, `async`, `await`
- `useState`, `useEffect`, `useReducer`, `useRef`
- `map`, `filter`, `reduce`, `forEach`
- `=>` arrow function body có tính toán
- API calls: `fetch`, `axios.get`, `axios.post`
- Event handlers có xử lý: `onClick={() => doSomething()}`
- props có transform: `<Comp items={items.filter(x => x.active)}>`

**Dấu hiệu UI (được sửa):**
- `className`, `style`, `class`
- `<div>`, `<span>`, `<p>`, `<h1>`-`<h6>`, `<button>`
- CSS properties: `color:`, `margin:`, `padding:`, `width:`, `height:`
- Tailwind classes
- `placeholder`, `alt`, `src` (chỉ khi không liên quan logic)
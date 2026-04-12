# Tạo Page/Component UI Mới

## Mục đích
Tạo page/component UI mới — **đẹp từ đầu**, đúng yêu cầu, chuẩn chuyên nghiệp.

## Khi nào dùng
- User nói "tạo page mới"
- User nói "thiết kế dashboard"
- User nói "tạo component"
- User nói "làm UI cho trang X"

## Điều kiện trước
- Biết yêu cầu cụ thể của user (page gì, chức năng gì, style gì)
- Biết framework (React/Vue/Angular/HTML)
- Biết CSS approach (Tailwind/SCSS/Styled Components)

## Các bước

### Bước 1: Thu thập yêu cầu — 5 câu hỏi bắt buộc

**KHÔNG BAO GIỜ code khi chưa có đủ thông tin này:**

| # | Câu hỏi | Ví dụ |
|---|---------|-------|
| 1 | Page/component gì? | "Trang login", "Dashboard", "Card sản phẩm" |
| 2 | Chức năng cơ bản? | "Form login, forgot password, remember me" |
| 3 | Style mong muốn? | "Modern, dark mode, gradient nhẹ" |
| 4 | Framework/CSS? | "React + Tailwind" / "Vue + SCSS" |
| 5 | Responsive? | "Mobile-first" / "Desktop only" |

Nếu thiếu → hỏi từng câu, không bỏ qua.

### Bước 2: Xác định design system

**Hỏi hoặc xác định:**
- Dự án đã có design system chưa? (colors, spacing, typography)
- Nếu có → dùng system có sẵn
- Nếu chưa → đề xuất system chuẩn:

```
Colors:
- Primary: #3B82F6 (blue-500)
- Secondary: #6366F1 (indigo-500)
- Background: #FFFFFF / #0F172A (dark)
- Text: #1E293B / #F8FAFC (dark)
- Muted: #64748B
- Border: #E2E8F0 / #334155 (dark)

Typography:
- Font: Inter / system-ui
- Heading: 24-32px, font-weight 700
- Subheading: 18-20px, font-weight 600
- Body: 14-16px, font-weight 400
- Small: 12px, font-weight 400

Spacing (Tailwind scale):
- Section: py-12 / py-16 (48px / 64px)
- Card: p-6 (24px)
- Element: gap-4 / space-y-3 (16px)
```

### Bước 3: Thiết kế layout — Bút trước khi code

**Trước khi viết code, mô tả layout bằng text:**

```
Header:
- Logo bên trái
- Navigation bên phải
- Sticky

Main:
- Hero section: headline + subheadline + CTA button
- Grid 3 columns: feature cards
- Testimonial section

Footer:
- Logo + copyright
- Social links
```

**Tại sao:** Có layout trước → code nhanh hơn, không phải sửa nhiều.

### Bước 4: Viết code — Component by Component

**Viết từng phần, theo thứ tự:**

#### a) Container & Layout
```jsx
// Container tiêu chuẩn
<div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  {/* content */}
</div>
```

#### b) Typography Hierarchy
```jsx
<h1 className="text-3xl font-bold tracking-tight text-gray-900">
  Heading
</h1>
<p className="mt-2 text-sm text-gray-600">
  Subtext
</p>
```

#### c) Card Component
```jsx
<div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6
    hover:shadow-md transition-shadow duration-200">
  {/* card content */}
</div>
```

#### d) Button
```jsx
<button className="inline-flex items-center justify-center
    px-5 py-2.5 text-sm font-semibold text-white
    bg-blue-600 rounded-lg
    hover:bg-blue-700
    focus:ring-4 focus:ring-blue-100
    disabled:opacity-50 disabled:cursor-not-allowed
    transition-colors duration-200">
  Button
</button>
```

#### e) Form Input
```jsx
<input
  className="w-full px-4 py-2.5 text-sm
    border border-gray-300 rounded-lg
    placeholder:text-gray-400
    focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent
    disabled:bg-gray-50 disabled:text-gray-500"
  placeholder="Enter text..."
/>
```

### Bước 5: Kiểm tra code trước khi output

**TRƯỚC KHI TRẢ, kiểm tra:**

```
□ Syntax đúng? (đóng tag, đúng cú pháp)
□ Class name đúng? (Tailwind không typo)
□ Responsive? (mobile-first breakpoints)
□ Accessibility? (aria-label, alt text, focus state)
□ Props interface đúng? (TypeScript nếu dùng)
□ Naming convention đúng? (PascalCase cho component)
```

### Bước 6: Trình bày kết quả

Trình bày:
- Component/page đã tạo
- Props cần truyền vào (nếu là component)
- Cách sử dụng
- Preview mô tả

---

## Output

- File component/page mới
- Props interface (nếu TypeScript)
- Hướng dẫn sử dụng

## Kiểm tra Chất lượng

- [ ] Yêu cầu user đã được đáp ứng đầy đủ?
- [ ] Layout có hierarchy rõ ràng?
- [ ] Spacing đều theo scale?
- [ ] Màu sắc đọc được (contrast)?
- [ ] Responsive hoàn chỉnh?
- [ ] Hover/focus states đầy đủ?
- [ ] Code sạch, không duplicate?
- [ ] Không có logic (chỉ UI)?
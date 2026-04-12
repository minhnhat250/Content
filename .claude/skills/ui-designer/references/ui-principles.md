# 10 Nguyên tắc Thiết kế UI Chuyên Nghiệp

## Mục đích
Reference về nguyên tắc thiết kế UI — dùng khi thiết kế mới hoặc cải thiện UI.

---

## 10 Nguyên tắc VÀNG

### 1. Hierarchy — Phân cấp rõ ràng

**Quy tắc:** Thứ gì quan trọng nhất → to nhất, đậm nhất, nổi bật nhất.

```
Quan trọng nhất:  text-3xl, font-bold, text-primary
Quan trọng 2:     text-xl, font-semibold
Quan trọng 3:     text-lg, font-medium
Body:              text-base, font-normal
Muted:             text-sm, text-gray-500
```

### 2. Whitespace — Khoảng trắng đủ

**Quy tắc:** Không chật chội, không thưa thớt.

| Vị trí | Khoảng cách |
|---------|------------|
| Section → Section | 64px - 96px |
| Card → Card | 24px - 32px |
| Element trong Card | 16px - 24px |
| Form field → Form field | 12px - 16px |

### 3. Contrast — Độ tương phản đủ

**Quy tắc:** Đọc được trên mọi nền.

```
✅ Text on White:   text-gray-900  on bg-white     (ratio 15:1)
✅ Text on Gray:   text-white    on bg-gray-900  (ratio 15:1)
✅ Text on Blue:   text-white    on bg-blue-600  (ratio 4.5:1)
❌ Text on White:  text-gray-300 on bg-white     (ratio 1.6:1) ← KHÔNG ĐỌC ĐƯỢC
```

### 4. Consistency — Nhất quán

**Quy tắc:** Cùng màu, cùng spacing, cùng style mọi nơi trong dự án.

```
✅ Primary button:   bg-blue-600, px-6, py-2.5, rounded-lg, font-semibold
✅ Input:           border border-gray-300, px-4, py-2.5, rounded-lg
✅ Card:            bg-white, rounded-2xl, shadow-sm, p-6
❌ Nút primary ở header: bg-blue-600
   Nút primary ở footer: bg-indigo-500  ← KHÔNG NHẤT QUÁN
```

### 5. Feedback — Phản hồi rõ ràng

**Quy tắc:** Mọi tương tác phải có phản hồi.

| Hành động | Feedback |
|-----------|----------|
| Hover button | `hover:bg-blue-700`, `hover:scale-[1.02]` |
| Focus input | `focus:ring-2 focus:ring-blue-500` |
| Click button | `active:scale-[0.98]` |
| Loading | Skeleton hoặc Spinner |
| Error | Border đỏ + text lỗi bên dưới |

### 6. Typography — Chữ rõ ràng

**Quy tắc:**
- Font size: Heading 24-32px, Body 14-16px, Caption 12px
- Line-height: Heading 1.2, Body 1.5
- Font-weight: Heading 600-700, Body 400
- Letter-spacing: Heading -0.5px → -1px (đọc đầm hơn)

### 7. Color — Màu sắc có hệ thống

**Quy tắc:**
- Primary: 1 màu chính (gọi hành động)
- Secondary: 1 màu phụ (bổ sung)
- Neutral: 3-5 tông xám (text, border, background)
- Status: 3 màu (success-green, error-red, warning-amber)

```
Primary:   blue-600
Secondary: indigo-500
Success:  green-500
Error:    red-500
Warning:  amber-500
Neutral:  gray-50 → gray-900
```

### 8. Border & Shadow — Độ sâu

**Quy tắc:**
- Border-radius: 4px (small), 8px (medium), 16px (large), 9999px (pill)
- Shadow: Nhẹ cho elements thường, đậm cho elements nổi bật
- Border: 1px cho subtle, 2px cho emphasis

```
Shadow nhẹ:  shadow-sm / 0 1px 2px rgba(0,0,0,0.05)
Shadow vừa:  shadow-md / 0 4px 6px rgba(0,0,0,0.07)
Shadow đậm:  shadow-lg / 0 10px 15px rgba(0,0,0,0.1)
Border:      border border-gray-100 (subtle) / border-gray-200 (normal)
```

### 9. Responsive — Mọi màn hình

**Quy tắc:** Mobile-first.

```
Mobile (< 640px):     1 column, full width, touch-friendly (min 44px tap target)
Tablet (640-1024px):  2 columns, some spacing
Desktop (> 1024px):   3-4 columns, max-width container

Breakpoints Tailwind: sm:, md:, lg:, xl:, 2xl:
```

### 10. Animation — Chuyển động mượt

**Quy tắc:**
- Duration: 150ms (fast), 200ms (normal), 300ms (slow)
- Easing: ease-in-out cho hầu hết, ease-out cho enter, ease-in cho exit
- Chỉ animate property cần thiết (transform, opacity)

```
Transition nhanh:  transition-all duration-150
Transition bình thường: transition-all duration-200
Hover effect: hover:scale-[1.02] hover:shadow-lg
```

---

## Checklist UI Review

Trước khi trả code, kiểm tra:

```
□ Font size hierarchy đúng? (heading to hơn body)
□ Spacing theo scale (4, 8, 12, 16, 24, 32, 48, 64)?
□ Contrast đủ (đọc được trên nền)?
□ Màu nhất quán toàn dự án?
□ Hover/focus states đầy đủ?
□ Responsive breakpoints đủ?
□ Animation không quá nhanh/quá chậm?
□ Touch target ≥ 44px trên mobile?
□ Không có hardcoded pixel values (dùng scale)?
```
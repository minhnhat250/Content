# Template: Notion Page — Chuẩn Cấu Trúc

Dùng khi: người dùng muốn tạo page Notion có cấu trúc đẹp & chuyên nghiệp.
Có thể áp dụng toàn bộ hoặc chỉ một phần.

---

## Cấu trúc Page Tiêu Chuẩn

Khi tạo page mới trong Notion, áp dụng cấu trúc này:

```
┌─────────────────────────────────────────┐
│  📌 [TIÊU ĐỀ CHÍNH]                     │
│  Status: ● Đang thực hiện | ✅ Hoàn thành│
├─────────────────────────────────────────┤
│  ## Mô tả ngắn                         │
│  [1-3 câu tóm tắt nội dung / mục đích]  │
├─────────────────────────────────────────┤
│  ## 🎯 Tổng quan                         │
│  [Nội dung chính]                       │
│  ├── heading_1: Tổng quan               │
│  │   └── paragraph: mô tả              │
│  ├── heading_1: Chi tiết                │
│  │   ├── heading_2: Phần 1              │
│  │   │   ├── paragraph: nội dung        │
│  │   │   ├── code: ví dụ (nếu có)      │
│  │   │   └── quote: ghi chú quan trọng  │
│  │   └── heading_2: Phần 2              │
│  │       └── ...                        │
│  └── heading_1: Tài nguyên               │
│      ├── bulleted_list: link tài liệu   │
│      └── bulleted_list: video tham khảo │
├─────────────────────────────────────────┤
│  ## 📝 Ghi chú / Bình luận               │
│  [Nơi ghi chú thêm]                     │
├─────────────────────────────────────────┤
│  ## 🔗 Liên kết                         │
│  • Nguồn gốc | • Related Pages          │
└─────────────────────────────────────────┘
```

---

## Các Loại Template

### Template 1: Ghi chú học tập / Nghiên cứu

```
📖 [Chủ đề]

**Ngày:** {{date}}
**Nguồn:** {{source}}
**Tags:** {{tags}}

---

## 🎯 Tóm tắt

[2-3 câu tóm tắt]

## 📚 Nội dung chính

### 1. Khái niệm cơ bản
[Giải thích]

### 2. Ví dụ thực tế
[Ví dụ code / minh họa]

### 3. Ứng dụng
[Ứng dụng trong thực tế]

## 💡 Điểm quan trọng

> **[Quote / insight quan trọng từ nguồn]**

## ❓ Câu hỏi / Thắc mắc

- [Câu hỏi 1]
- [Câu hỏi 2]

## 🔗 Tài nguyên bổ sung

- [Link 1]
- [Link 2]
```

### Template 2: Task / Công việc

```
⚡ [Tên Task]

**Trạng thái:** 🔄 In Progress | ✅ Done | ⏳ Blocked
**Deadline:** {{date}}
**Người phụ trách:** {{assignee}}

---

## Mục tiêu

[Mục tiêu của task]

## Các bước thực hiện

- [ ] Bước 1
- [ ] Bước 2
- [ ] Bước 3

## Tiến độ

| Ngày | Mô tả | Trạng thái |
|------|-------|------------|
| ... | ... | ... |

## Kết quả

[Kết quả / output của task]

## Blocker

[Khó khăn gặp phải]
```

### Template 3: Wiki / Tài liệu tham khảo

```
📘 [Tên tài liệu]

**Loại:** Hướng dẫn | API Reference | Tutorial | Best Practices
**Mức độ:** 🟢 Beginner | 🟡 Intermediate | 🔴 Advanced
**Cập nhật:** {{date}}

---

## Mục lục

1. [Link đến phần 1]
2. [Link đến phần 2]
...

## 1. Giới thiệu

[Mở đầu, context]

## 2. [Phần chính]

### 2.1 [Sub-section]

[Content]

### 2.2 [Sub-section]

[Content]

## 3. Code Examples

```python
# Ví dụ code
```

## 4. FAQ

**Q: [Câu hỏi]**
A: [Trả lời]

## 5. Related Pages

- [Page 1]
- [Page 2]
```

---

## Hướng dẫn áp dụng Template

### Khi nào dùng template?

| Tình huống | Template phù hợp |
|-----------|-----------------|
| Ghi chú học tập / research | Template 1 |
| Công việc / task cá nhân | Template 2 |
| Tài liệu tham khảo / wiki | Template 3 |
| Ghi chú nhanh, không cấu trúc | Không cần template |

### Cách áp dụng:

1. **Tạo page mới** trong Notion
2. **Đặt icon & tiêu đề** (phần properties)
3. **Copy cấu trúc** từ template phù hợp
4. **Điền nội dung** vào các phần

### Tùy chỉnh:

- Thêm/bớt sections tùy nhu cầu
- Thay đổi emoji icons cho phù hợp
- Thêm property fields (Status, Tags, Assignee) nếu dùng Database

---

## Mẹo thiết kế Page đẹp

1. **Dùng heading hierarchy** đúng: H1 → H2 → H3
2. **Dùng Toggle** (▶) cho nội dung dài, collapsible
3. **Dùng Callout** (💡) cho điểm quan trọng
4. **Dùng Table** cho dữ liệu có cấu trúc
5. **Dùng Code block** với language specifier
6. **Thêm dividers** (---) để phân cách sections
7. **Link đến related pages** để tạo wiki liên kết
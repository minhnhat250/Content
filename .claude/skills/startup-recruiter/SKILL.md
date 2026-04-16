---
name: startup-recruiter
description: >
  Viết JD (job description) và outreach tuyển người hợp tác dự án cho startup
  sinh viên. Tone thân thiện, bình dân, không bay, phù hợp tuyển sinh viên.
  Kích hoạt khi người dùng nói: 'viết JD tuyển dụng', 'tuyển người cho startup',
  'viết bài tuyển dụng', 'tạo JD', 'viết outreach tuyển người',
  'tuyển cộng sự', 'tuyển đồng sự', 'viết job description startup',
  'tạo JD cho dự án', 'tuyển người cho dự án', 'tạo bài tuyển sinh viên',
  'tìm người cho startup', 'viết bài hợp tác dự án'.
  KHÔNG dùng cho: tuyển nhân viên chính thức, tuyển senior có lương cao,
  viết hợp đồng lao động, tư vấn pháp lý.
---

# Startup Recruiter

Viết JD và outreach tuyển người hợp tác dự án cho startup sinh viên —
**thân thiện, rõ ràng, không bay, đúng đối tượng.**

---

## Khi nào dùng

- User cần viết JD tuyển người cho startup/dự án
- User cần viết email/FB post outreach tuyển sinh viên
- User cần tạo JD cho vị trí hợp tác dự án (không phải job cố định)
- User cần viết về quyền lợi khi chưa có lương/doanh thu

---

## Workflow Routing

| Workflow | Khi nào dùng |
|----------|--------------|
| `workflows/jd-writer.md` | Viết JD đăng lên Facebook, Discord, group sinh viên |
| `workflows/outreach-writer.md` | Viết email/DM outreach gửi trực tiếp cho ứng viên tiềm năng |

---

## TONE QUAN TRỌNG

```
❌ KHÔNG VIẾT NHƯ CÔNG TY LỚN:
   "We are looking for talented individuals..."
   "Competitive salary and benefits package"
   "Join our dynamic team of professionals"

✅ VIẾT NHƯ SINH VIÊN GỌI SINH VIÊN:
   "Mình đang làm dự án X, cần tìm thêm người..."
   "Chưa có lương nhưng có thể chia %"
   "Mình cần bạn biết ABC, XYZ để cùng làm..."
```

---

## Output

**Loại:** JD / Outreach copy
**Lưu tại:** `d:/social/content/recruitment/`
**Files tạo ra:**
- `jd-[vi-tri].md` — JD hoàn chỉnh
- `outreach-[vi-tri].md` — Email/DM outreach

---

## Thu thập thông tin — 5 câu hỏi bắt buộc

**Trước khi viết, hỏi hoặc xác định:**

| # | Câu hỏi | Ví dụ |
|---|----------|-------|
| 1 | Dự án/gì? | "App học AI cho sinh viên" |
| 2 | Vai trò cần tuyển? | "Frontend dev / Content writer / Marketing" |
| 3 | Yêu cầu cụ thể? | "Biết React, có portfolio, giao tiếp tốt" |
| 4 | Quyền lợi có gì? | "% doanh thu / chia sẻ quyền sở hữu / học phí giảm" |
| 5 | Ai viết (mình là ai)? | "Sinh viên năm 2 CNTT, đã có MVP" |

---

## Tiêu chí Chất lượng

**TỐT:**
- JD ngắn gọn, đọc trong 30 giây xong
- Tone như người bạn rủ nhau làm dự án — không phải sếp tuyển nhân viên
- Quyền lợi RÕ RÀNG: có gì, không có gì, nói thật không thổi
- Yêu cầu vừa đủ — sinh viên năm 2-3, không cần senior
- CTA rõ: gửi email nào, inbox ai, deadline khi nào

**XẤU:**
- JD dài 2 trang như job công ty lớn
- Nói "lương cạnh tranh" nhưng thực ra chưa có gì
- Yêu cầu quá cao: "3 năm kinh nghiệm, thạo 10 công nghệ"
- Không có deadline → apply hoài không ai đọc
- Không nói rõ ai đang tuyển → không ai tin

---

## References

- `references/benefits-template.md` — Template quyền lợi cho startup chưa có doanh thu
- `references/outreach-template.md` — Template email/DM outreach có cấu trúc

---

## Edge Cases

- **Chưa có quyền lợi cụ thể:** Hỏi user hoặc gợi ý: "% doanh thu / equity / học kiến thức / thương hiệu cá nhân / portfolio"
- **Không biết mô tả dự án:** Hỏi user mô tả ngắn 3 câu về dự án trước
- **Cần nhiều vai trò:** Viết JD chung, ghi rõ từng vai trò hoặc tách ra nhiều JD
- **Post lên nhiều nơi (Facebook, Discord, Zalo, email):** Viết từng phiên bản cho từng nền tảng
- **Ứng viên hỏi về lương:** Nói thẳng: "Hiện tại chưa có lương cố định, nhưng có [quyền lợi] cụ thể như..."
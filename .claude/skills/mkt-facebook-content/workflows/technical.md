# Workflow: Technical — Bài viết Kỹ thuật

---

## Mục đích

Viết bài Facebook dạng kỹ thuật — chia sẻ kiến thức, hướng dẫn cách làm, phân tích công nghệ, AI tools, workflow automation.
Kỹ thuật viết KHÔNG giống storytelling — phải LOGIC, RÕ RÀNG, và CÓ THỂ ÁP DỤNG.

---

## Khi nào dùng

- User muốn chia sẻ kiến thức về công nghệ / AI / tools
- User muốn hướng dẫn cách làm (tutorial, how-to)
- User muốn phân tích 1 tool / platform / framework mới
- User muốn so sánh các giải pháp kỹ thuật
- User muốn xây dựng brand CHUYÊN GIA (thay vì chỉ founder)

---

## Điều kiện trước

Thu thập đủ thông tin từ user:

- **Chủ đề kỹ thuật:** Tool gì? Công nghệ gì? Quy trình gì?
- **Góc tiếp cận:**
  - Giới thiệu: "Tool này là gì, dùng làm sao"
  - So sánh: "Tool A vs Tool B — cái nào tốt hơn"
  - Hướng dẫn: "Cách làm X từ đầu đến cuối"
  - Phân tích: "Tại sao X lại quan trọng"
- **Audience kỹ thuật:** Beginner / Intermediate / Advanced?
- **Mục đích:** Chia sẻ kiến thức / xây brand / thu hút khách hàng?
- **Độ dài:** Ngắn / Trung bình / Dài?

---

## 6 Bước Viết Bài Kỹ thuật

### Bước 1 — MỞ ĐẦU BẰNG VẤN ĐỀ THẬT

**Tải `references/emotional-writing.md` — kỹ thuật "khoảnh khắc" vẫn áp dụng cho kỹ thuật.**

Mở đầu kỹ thuật KHÔNG bắt đầu bằng "Hôm nay mình sẽ giới thiệu...".
Mà bắt đầu bằng 1 VẤN ĐỀ THẬT mà audience GẶP PHẢI.

**Mở đầu TỐT:**
> "Mình từng mất 4 tiếng mỗi ngày để reply email. Rồi mình tìm được thứ này."

> "Bạn có biết: 80% thời gian developer là debug, không phải viết code?"

> "Automation là gì? Là thay vì làm 50 lần, bạn làm 1 lần — rồi máy làm 49 lần còn lại."

**Mở đầu SAI:**
> "Hôm nay mình sẽ giới thiệu về Prompt Engineering."
> "Bài viết này sẽ hướng dẫn các bạn cách sử dụng..."

**Tại sao:** Vấn đề thật → audience NHẬN RA MÌNH → có động lực đọc tiếp.

---

### Bước 2 — GIẢI THÍCH LOGIC

**Tải `references/brand-voice.md` — giữ giọng chuyên gia THÂN MẬT.**

Phần giữa kỹ thuật = NƠI LOGIC DIỄN RA.

**3 cấu trúc giải thích:**

#### Cấu trúc WHAT → HOW → WHY
1. **WHAT:** Đây là cái gì?
2. **HOW:** Làm sao để dùng?
3. **WHY:** Tại sao nó quan trọng / tại sao nên dùng?

#### Cấu trúc PROBLEM → SOLUTION → PROOF
1. **PROBLEM:** Vấn đề là gì?
2. **SOLUTION:** Giải pháp (cách làm cụ thể)
3. **PROOF:** Proof = số liệu / kết quả / ví dụ cụ thể

#### Cấu trúc BEFORE → AFTER
1. **BEFORE:** Trước đây làm thế nào?
2. **AFTER:** Bây giờ có tool này, làm thế nào?
3. **DELTA:** Thời gian / tiền bạc / effort tiết kiệm được?

**Lưu ý quan trọng:**
- Dùng ngôn ngữ KỸ THUẬT được GIỮ NGUYÊN tiếng Anh: API, webhook, automation, Prompt Engineering, LLM, deployment...
- Khi dùng thuật ngữ mới → GIẢI THÍCH NGAY bằng tiếng Việt đơn giản
- Có SỐ LIỆU CỤ THỂ: "tiết kiệm 4 tiếng/ngày" không phải "tiết kiệm rất nhiều thời gian"
- Có VÍ DỤ THẬT: không phải "bạn có thể dùng nó để làm X" mà "mình dùng nó để làm X trong 3 giây"

---

### Bước 3 — CHỌN LOẠI BODY

Tùy góc tiếp cận, chọn loại body phù hợp:

#### A. Hướng dẫn (Tutorial/How-to)

**Cấu trúc:**
```
Bước 1: [Hành động cụ thể] → [Kết quả mong đợi]
Bước 2: [Hành động cụ thể] → [Kết quả mong đợi]
...
Lưu ý: [Cảnh báo / mẹo / pitfall thường gặp]
```

**Ví dụ:**
> "Bước 1: Mở Make (trước đây là Integromat). Tạo scenario mới."

> "Bước 2: Kéo trigger 'Webhook' vào. Copy URL đó."

> "Bước 3: Paste vào nơi bạn muốn trigger — có thể là Zapier, n8n, hoặc code của bạn."

#### B. So sánh (Comparison)

**Cấu trúc:**
```
[Tool A] vs [Tool B]

Điểm giống: [list]
Điểm khác: [list]

Giá: [so sánh]
Độ khó: [so sánh]
Phù hợp với: [ai nên dùng cái nào]
```

**Nguyên tắc SO SÁNH KHÔNG CÓ ÂM:**
- KHÔNG nói "Tool A TỆ hơn vì..."
- Mà nói "Tool A PHÙ HỢP HƠN KHI... Tool B PHÙ HỢP HƠN KHI..."

#### C. Phân tích (Analysis)

**Cấu trúc:**
```
Điều [X] đang xảy ra: [mô tả thực trạng]
Tại sao nó quan trọng: [lý do]
Điều [Y] sẽ thay đổi: [dự đoán]
Kết luận: [tổng hợp + hành động gợi ý]
```

---

### Bước 4 — VIẾT BODY

Viết theo nhịp:

```
[HOOK — 1-3 dòng: Vấn đề thật / Số liệu gây sốc]

[ĐOẠN 1 — Context NHANH]
→ Đây là cái gì, tại sao mình viết về nó

[ĐOẠN 2 — Giải thích LOGIC]
→ Theo cấu trúc đã chọn (WHAT/HOW/WHY hoặc PROBLEM/SOLUTION/PROOF)
→ Có số liệu, có ví dụ cụ thể
→ Giữ thuật ngữ Anh, giải thích khi cần

[ĐOẠN 3 — DEMO / Proof]
→ Ví dụ thật, screenshot (mô tả), kết quả cụ thể
→ Nếu là so sánh → table đơn giản

[ĐOẠN 4 — Kết nối với audience]
→ Điều này liên quan đến bạn như thế nào?
→ Nếu audience làm theo, được gì?

[CTA — Hành động rõ ràng]
```

---

### Bước 5 — KIỂM TRA VIRAL CHO KỸ THUẬT

**Tải `references/viral-guide.md` — yếu tố viral vẫn áp dụng cho kỹ thuật.**

Bài kỹ thuật viral = BÀI CÓ SỐ LIỆU THẬT + INSIGHT BẤT NGỜ.

```
□ Hook có số cụ thể không? ("4 tiếng" thay vì "rất nhiều thời gian")
□ Có ít nhất 1 insight / góc nhìn mà audience chưa biết?
□ Có proof (số liệu, kết quả, ví dụ) cho mọi claim?
□ Có ít nhất 1 câu mà audience muốn screenshot / share?
□ Giải thích đủ để BEGINNER hiểu không? (nếu target là beginner)
□ Giữ đủ CHIỀU SÂU để ADVANCED thấy giá trị? (nếu target là advanced)
□ Đọc lại — có thể LÀM THEO không? (bài không có action không viral)
```

---

### Bước 6 — TỐI ƯU FACEBOOK

**Tải `references/facebook-optimization.md` để format.**

```
□ Chia dòng ngắn (dưới 80 ký tự/dòng)?
□ Có dòng trống giữa các đoạn?
□ Độ dài: 200-500 từ cho engagement tốt nhất?
□ Nếu có bảng so sánh → format bảng đơn giản cho Facebook?
□ Thuật ngữ Anh có được GIỮ NGUYÊN không?
□ Có gợi ý hashtags (3-5 cái)?
□ Có CTA rõ ràng (lưu / inbox / comment)?
□ Có gợi ý "Save bài này nếu bạn cần"?
□ Gợi ý thời điểm đăng?
□ Có hình đính kèm (screenshot tool)?
```

---

## Output mẫu hoàn chỉnh

```
[Tiêu đề gợi ý: "Cách mình làm X trong Y" / "X vs Y — cái nào tốt hơn?" / "X là gì? Giải thích đơn giản nhất"]

[VIẾT HOÀN CHỈNH — theo 6 bước trên]

--- GỢI Ý ---

📅 Thời điểm đăng: [gợi ý khung giờ]
🏷️ Hashtags: #[...], #[...], #[...]
🖼️ Hình đính kèm: [gợi ý — screenshot tool / interface]
💬 Kích thích bình luận: [câu hỏi gợi ý]
💾 CTA đặc biệt: "Save bài này nếu bạn cần"
📌 Biến thể B (nếu yêu cầu): [tóm tắt nếu cần]
```

---

## Kiểm tra Chất lượng

Trước khi xong, verify từng câu:

- [ ] Đọc dòng 1 → audience NHẬN RA VẤN ĐỀ của họ?
- [ ] BEGINNER có thể HIỂU không? (nếu target beginner)
- [ ] ADVANCED có thấy GIÁ TRỊ không? (nếu target advanced)
- [ ] Có thể LÀM THEO sau khi đọc không? (bài how-to)
- [ ] Mọi thuật ngữ Anh đều được GIẢI THÍCH hoặc ĐÃ ĐƯỢC GIỮ NGUYÊN ĐÚNG?
- [ ] Có số liệu CỤ THỂ không phải "rất nhiều"?
- [ ] Insight ở cuối CÓ Ý NGHĨA với audience?
- [ ] CTA rõ ràng chưa?

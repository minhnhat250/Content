---
name: mkt-facebook-content
description: >
  Viết bài viết Facebook chuyên nghiệp: storytelling founder story, bài viết kỹ thuật công nghệ,
  viral content, và content lên xu hướng. Kích hoạt khi người dùng nói: 'viết bài facebook',
  'viết bài đăng facebook', 'soạn bài facebook', 'content facebook', 'viết bài viral facebook',
  'viết founder story', 'viết chuyện founder', 'viết bài kỹ thuật cho facebook', 'viết bài công nghệ facebook',
  'viết bài lên xu hướng', 'viết bài trending', 'tạo nội dung facebook', 'viết bài cho fanpage',
  'soạn content facebook chuyên nghiệp'.
  KHÔNG dùng cho: viết kịch bản video YouTube, viết bài blog website, viết email marketing,
  tạo nội dung cho nền tảng khác ngoài Facebook.
---

# Skill: mkt-facebook-content

Viết bài viết Facebook chất lượng cao — storytelling có hồn, kỹ thuật có logic, viral có chiến lược.
Skill này điều khiển 2 workflows chuyên biệt và 4 reference guides.

---

## Khi nào dùng

- User cần viết bài Facebook từ đầu
- User muốn viết founder story / storytelling
- User muốn viết bài kỹ thuật / công nghệ cho Facebook
- User muốn bài lên xu hướng / viral
- User muốn tối ưu bài viết Facebook đã có

---

## Workflow Routing

Trước khi viết, xác định loại bài và chọn workflow phù hợp:

| Workflow | Khi nào dùng |
|----------|-------------|
| `workflows/storytelling.md` | Founder story, storytelling, chia sẻ hành trình, cảm hứng kinh doanh |
| `workflows/technical.md` | Bài viết kỹ thuật, công nghệ, AI tools, hướng dẫn cách làm |

**Tự động luôn luôn làm:**

| Bước | Luôn làm |
|------|---------|
| Hook 3 giây | Dòng đầu tiên phải gây dừng scroll |
| Tải `references/viral-guide.md` | Áp dụng cơ chế viral cho mọi bài |
| Tải `references/facebook-optimization.md` | Tối ưu độ dài, format, thời điểm đăng |
| Tải `references/brand-voice.md` | Giữ giọng văn nhất quán |
| Tải `references/emotional-writing.md` | Kích hoạt cảm xúc phù hợp |

---

## Input cần thu thập

Khi user gọi skill, hỏi đủ thông tin:

### Bắt buộc
- **Chủ đề / chủ điểm:** Bài viết về gì?
- **Loại bài:** Storytelling (founder story) hay Technical (kỹ thuật)?
- **Mục đích:** Chia sẻ kiến thức / xây dựng brand / bán hàng / viral?

### Tùy chọn (hỏi thêm)
- **Audience mục tiêu:** Ai đọc? (SME, developer, marketer, founder...)
- **Độ dài mong muốn:** Ngắn (dưới 500 từ) / Trung bình (500-1000) / Dài (1000+)
- **Hashtags:** Có muốn gợi ý hashtags không?
- **Số biến thể:** User muốn 1 bài hay nhiều phiên bản A/B?
- **Brand voice đặc thù:** Có yêu cầu giọng văn riêng không?

---

## Nguyên tắc VIẾT bắt buộc (mọi bài viết)

### Về LOGIC
- Mỗi câu phải nối được với câu trước — không nhảy cóc
- Mỗi đoạn phải nối được với đoạn trước — không chuyển đề tài đột ngột
- Sử dụng "đồng hồ" logic: câu chuyển tiếp phải nói rõ "trước đó → giờ → sau đó"
- Không viết bừa — mọi từ đều phải phục vụ mục đích

### Về GIỌNG VĂN
- Tiếng Việt có dấu — tuyệt đối không bỏ dấu
- Từ chuyên ngành / kỹ thuật được giữ nguyên tiếng Anh (ví dụ: API, webhook, automation, Prompt Engineering)
- Viết như người thật ngồi nói chuyện — có câu ngắn, có câu dài, có ngắt nghỉ
- Không viết như bài báo khoa học — không "tuy nhiên", "do đó", "theo nghiên cứu"
- Có thể dùng emoji hợp lý (1-3 cái, không spam)

### Về VIRAL
- Tải `references/viral-guide.md` trước khi viết body
- Mọi bài phải có ít nhất 1 trigger cảm xúc mạnh
- Mọi bài phải có ít nhất 1 yếu tố bất ngờ / counter-intuitive
- Mọi bài phải có CTA rõ ràng

### Về FACEBOOK OPTIMIZATION
- Tải `references/facebook-optimization.md` sau khi viết body
- Tối ưu độ dài theo thuật toán (150-300 từ cho reach tốt nhất)
- Format đúng cho Facebook (dòng ngắn, có khoảng trắng)
- Đề xuất thời điểm đăng tối ưu

---

## Output

**Loại:** content
**Vị trí:** `content/facebook/[slug]/`
**Files tạo ra:**
- `[slug].md` - Bài viết hoàn chỉnh
- `[slug]-var-B.md` - Biến thể B (nếu user yêu cầu A/B)
- `[slug]-hashtags.md` - Danh sách hashtags gợi ý (nếu user yêu cầu)

---

## Quick Process (khi chỉ cần viết nhanh)

Nếu user chỉ cần 1 bài đơn lẻ, không cần workflow dài:

### Bước 1 — Xác định
- Loại bài: Storytelling hay Technical?
- Chủ đề cụ thể là gì?
- Mục đích gì?

### Bước 2 — Viết theo template

**Cho Storytelling:**
→ Mở đầu bằng 1 khoảnh khắc cụ thể → Xây drama → Kết thúc bằng insight hoặc CTA

**Cho Technical:**
→ Mở đầu bằng vấn đề thật → Giải thích logic → Demo / ví dụ cụ thể → Kết thúc bằng hành động

### Bước 3 — Viral check
- Đọc lại hook đầu tiên — có gây dừng scroll không?
- Có yếu tố bất ngờ không?
- Có trigger cảm xúc không?
- CTA rõ ràng chưa?

### Bước 4 — Format
- Chia dòng ngắn (dưới 80 ký tự/dòng)
- Có khoảng trắng giữa các đoạn
- Thêm emoji nếu phù hợp

### Bước 5 — Gợi ý
- Thời điểm đăng tốt nhất
- 3-5 hashtags
- (Tùy chọn) Biến thể A/B

---

## Tiêu chí Chất lượng

Bài viết TỐT vs XẤU khác nhau ở đâu:

| Tiêu chí | TỐT | XẤU |
|----------|------|------|
| **Logic** | Câu nối câu, đoạn nối đoạn, không nhảy cóc | Nhảy lung tung, thiếu chuyển tiếp |
| **Giọng văn** | Như người thật, có nhịp, có ngắt | Viết như văn bản hành chính |
| **Hook** | Dòng đầu gây dừng scroll ngay | Dòng đầu nhàm chán, ai cũng viết được |
| **Viral** | Có trigger cảm xúc + yếu tố bất ngờ | Bài khô khan, không có gì thú vị |
| **CTA** | Rõ ràng, người đọc biết phải làm gì | Không có CTA hoặc CTA mơ hồ |
| **Ngôn ngữ** | Tiếng Việt có dấu, từ Anh giữ nguyên | Bỏ dấu, viết tắt lung tung |
| **Platform** | Đúng format Facebook, độ dài tối ưu | Viết như blog, không format |

---

## References

- `references/viral-guide.md` — Cơ chế viral, triggers cảm xúc, cấu trúc viral
- `references/emotional-writing.md` — Kỹ thuật viết có hồn, kích hoạt cảm xúc
- `references/facebook-optimization.md` — Tối ưu thuật toán, độ dài, format, thời điểm đăng
- `references/brand-voice.md` — Giọng văn brand, ví dụ thực tế

## Scripts (nếu có)

- `scripts/` — Dành cho tương lai (auto post, scheduling), hiện tại chỉ viết content.

---

## Edge Cases

- **User gửi topic quá rộng** ("viết bài về AI"): Hỏi cụ thể hơn: "Bạn muốn về khía cạnh nào của AI? (ứng dụng / công nghệ / xu hướng / tool cụ thể?)"
- **User muốn bài quá ngắn nhưng phức tạp**: Báo "Topic này cần ít nhất X từ để truyền tải đủ. Bạn muốn chia thành series không?"
- **User gửi bài viết cũ để sửa**: Xác định vấn đề cốt lõi → sửa có chọn lọc, không viết lại toàn bộ
- **User muốn viết bài bán hàng**: Áp dụng storytelling trước → chuyển nhẹ sang selling → kết thúc bằng CTA rõ ràng
- **User yêu cầu bài về topic nhạy cảm (chính trị, tôn giáo)**: Từ chối nhẹ nhàng: "Mình không viết về topic này để tránh rủi ro. Bạn chọn topic khác nhé."
- **User yêu cầu quá nhiều biến thể (5+)**: Giới hạn 3 biến thể, giải thích: "Mình sẽ viết 3 phiên bản khác nhau (A/B/C), đủ để bạn test rồi."

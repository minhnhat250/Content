---
name: saas-ai-cost-calculator
description: >
  Tính toán chi phí sản phẩm SaaS AI cho sinh viên. Kích hoạt khi người dùng nói:
  'tính chi phí sản phẩm AI', 'phân tích giá thành', 'tính giá bán sản phẩm AI',
  'chi phí vận hành SaaS', 'tỉ giá sản phẩm có hợp lý không', 'tính giá AI cho sinh viên',
  'báo giá sản phẩm AI', 'phân tích lợi nhuận AI', 'tính chi phí thuê hosting AI',
  'so sánh giá gói AI', 'nên bán bao nhiêu', 'lộ trình tăng giá sản phẩm AI'.
  KHÔNG dùng cho: viết code sản phẩm AI, hướng dẫn lập trình, tạo nội dung marketing.
---

# SaaS AI Cost Calculator — Sinh viên

Tính toán chi phí thực và đề xuất giá bán hợp lý cho sản phẩm SaaS AI.
Đầu ra là bảng chi phí markdown, phân tích tỉ giá thu nhập, và lộ trình tăng trưởng.

---

## Khi nào dùng

- User nói "tính chi phí sản phẩm AI"
- User nói "phân tích giá thành sản phẩm SaaS"
- User nói "tỉ giá này có hợp lý không"
- User nói "nên bán bao nhiêu/tháng"
- User nói "lộ trình tăng giá sản phẩm AI"
- User nói "so sánh gói tuần/tháng/năm"
- User muốn biết doanh nghiệp AI có phát triển bền vững không

---

## Workflow Routing

| Workflow | Khi nào dùng |
|----------|--------------|
| `workflows/nhanh.md` | Cần bảng chi phí nhanh, ít thông tin |
| `workflows/phan-tich-day-du.md` | Cần phân tích thị trường, đối thủ, lộ trình tăng trưởng |

---

## Output

**Loại:** data + analysis
**Vị trí:** Hiển thị markdown trong chat (copy được)
**Files tạo ra:**
- Bảng chi phí markdown — trực tiếp trong chat
- File `.csv` tùy chọn — lưu vào thư mục hiện tại nếu user yêu cầu

---

## Quick Process (workflow nhanh)

### Bước 1: Thu thập thông tin sản phẩm

Hỏi người dùng lần lượt từng nhóm chi phí. Đừng hỏi tất cả cùng lúc — điều đó khiến sinh viên bối rối.

**Nhóm 1 — Chi phí cố định hàng tháng (đã biết):**
- Tên sản phẩm AI
- Domain + Hosting/tháng (VND)
- API LLM costs/tháng (VND) — ước lượng nếu chưa biết
- SSL, email, tool quản lý khác/tháng (VND)

**Nhóm 2 — Chi phí biến đổi:**
- Số người dùng ước tính/tháng (hiện tại)
- Mỗi user dùng bao nhiêu lần API/tháng

**Nhóm 3 — Mục tiêu cá nhân (sinh viên):**
- Mức lương mong muốn sau khi ra trường (VND/tháng)
- Số giờ muốn làm việc/tháng cho sản phẩm này
- Mục tiêu mở rộng: giữ nguyên nhóm nhỏ hay scale lớn

**Tại sao tách nhóm:** Sinh viên thường không biết phải nói gì nếu hỏi tất cả cùng lúc. Tách nhóm giúp họ tập trung suy nghĩ từng phần.

**Nếu thiếu số liệu:** Dùng ước lượng phổ biến (ghi rõ đang ước lượng):
- Hosting đơn giản: 100.000–300.000 VND/tháng
- VPS 2GB RAM: 150.000–400.000 VND/tháng
- API OpenAI GPT-4o mini: ~$0.15/1M tokens input, $0.60/1M tokens output
- API Claude Haiku: ~$0.25/1M tokens input, $1.25/1M tokens output
- API Gemini 1.5 Flash: miễn phí đến 1.5M tokens/tháng (Google AI Studio)
- Sinh viên part-time: ưu tiên dùng gói miễn phí hoặc $10–20/tháng

### Bước 2: Phân loại giai đoạn doanh nghiệp

Dựa vào số user và doanh thu ước tính, xác định giai đoạn:

| Giai đoạn | User/tháng | Doanh thu/tháng |
|-----------|-----------|-----------------|
| **Nghiên cứu** | 0–10 | 0–500K VND |
| **Khởi nghiệp** | 10–100 | 500K–5M VND |
| **Tăng trưởng** | 100–1.000 | 5M–50M VND |
| **Ổn định** | 1.000+ | 50M+ VND |

**Tại sao quan trọng:** Chi phí và chiến lược giá khác nhau theo giai đoạn.
Giai đoạn nghiên cứu = tối thiểu chi phí, dùng gói miễn phí. Giai đoạn tăng trưởng = có thể đầu tư công cụ trả phí.

### Bước 3: Tính chi phí thực — Bảng chi phí

Tạo bảng markdown đầy đủ theo format sau. Tính toán từng dòng:

```
## 📊 BẢNG CHI PHÍ SẢN PHẨM: [TÊN SẢN PHẨM]

### 1. Chi phí cố định hàng tháng
| Khoản mục | Chi phí (VND) | Ghi chú |
|-----------|-------------|---------|
| Hosting / Server | xxx.xxx | |
| API LLM (ước lượng) | xxx.xxx | xxx tokens × giá/token |
| Domain / SSL | xxx.xxx | |
| Tool quản lý (email, analytics...) | xxx.xxx | |
| **Tổng cố định** | **xxx.xxx** | |

### 2. Chi phí biến đổi (theo user)
| Khoản mục | Đơn giá | Số user | Thành tiền (VND) |
|-----------|--------|--------|-----------------||
| API cost mỗi user | xxx VND | × xxx | xxx.xxx |
| Support mỗi user | xxx VND | × xxx | xxx.xxx |
| **Tổng biến đổi** | | | **xxx.xxx** |

### 3. Chi phí nhân sự (sinh viên tự đánh giá trung thực)
| Vai trò | Giờ/tháng | Giá thuê thị trường | Chi phí quy đổi |
|--------|----------|-------------------|----------------|
| Lập trình + bảo trì | xxh | xxx.000 VND/h | xxx.xxx VND |
| Hỗ trợ khách hàng | xxh | xxx.000 VND/h | xxx.xxx VND |
| Marketing | xxh | xxx.000 VND/h | xxx.xxx VND |
| **Tổng nhân sự** | | | **xxx.xxx** |

> ⚠️ **Lưu ý cho sinh viên:** Nếu bạn "không tính công mình" → đây là lỗi phổ biến khiến sinh viên bán giá rẻ rồi bỏ cuộc. Tính tối thiểu bằng giá thị trường freelance để biết mình thực sự "lỗ" hay "lãi".

### 4. Tổng chi phí + Điểm hòa vốn

```
Tổng chi phí/tháng = Chi phí cố định + Biến đổi + Nhân sự
                    = xxx.xxx + xxx.xxx + xxx.xxx
                    = xxx.xxx VND

Số user tối thiểu để hòa vốn (nếu bán gói xxx.000/tháng):
  = Tổng chi phí ÷ Giá gói
  = xxx.xxx ÷ xxx.xxx = ~xx user
```

### Bước 4: Phân tích tỉ giá thu nhập

So sánh giá bán hiện tại (hoặc đề xuất) với thị trường:

```
## 💰 PHÂN TÍCH TỈ GIÁ

| Tiêu chí | Giá đề xuất | Thị trường VN | Đánh giá |
|----------|------------|---------------|---------|
| Giá gói tháng | xxx.xxx VND | 50K–500K VND | ✅ Hợp lý / ⚠️ Cao / ❌ Thấp |
| Giá gói tuần | xxx.xxx VND | 20K–150K VND | |
| Giá gói năm | xxx.xxx VND | 300K–3M VND | (giảm 20–30%) |
| Lương mục tiêu | xxx.xxx VND/tháng | — | Cần ≥xx user |

### Ma trận tỉ giá — Bạn có đang bán đúng giá?

| Số user | Doanh thu/tháng | Trừ chi phí | Thu nhập thực | Mỗi user mang lại |
|---------|-----------------|------------|--------------|-------------------|
| 5 | xxx.xxx | -xxx.xxx | xxx.xxx | xxx.xxx |
| 20 | xxx.xxx | -xxx.xxx | xxx.xxx | xxx.xxx |
| 50 | xxx.xxx | -xxx.xxx | xxx.xxx | xxx.xxx |
| 100 | xxx.xxx | -xxx.xxx | xxx.xxx | xxx.xxx |

### Đánh giá:
- [Tỉ giá TỐT nếu: thu nhập/user ≥ 20K VND/tháng ở giai đoạn khởi nghiệp]
- [Tỉ giá XẤU nếu: lỗ tiền thật sau khi trừ chi phí cố định]
```

### Bước 5: Lộ trình phát triển doanh nghiệp

Xác định giai đoạn hiện tại và đề xuất lộ trình 3 bước:

```
## 🚀 LỘ TRÌNH PHÁT TRIỂN

Giai đoạn hiện tại: [X] — [Mô tả ngắn]

### Giai đoạn 1: Xây dựng (0–6 tháng)
Mục tiêu: [x] user, doanh thu [x] VND/tháng
Chiến lược giá:
- Giữ giá thấp hoặc freemium để test thị trường
- Tập trung feedback, sửa bug, cải tiện sản phẩm
- Dùng gói miễn phí của API (Google Gemini, OpenAI free tier)
Chi phí mục tiêu: ≤[x] VND/tháng

### Giai đoạn 2: Tăng trưởng (6–18 tháng)
Mục tiêu: [x] user, doanh thu [x] VND/tháng
Chiến lược giá:
- Tăng giá 20–30% sau khi có 50+ user ổn định
- Thêm gói năm để giữ khách
- Đầu tư công cụ trả phí (analytics, email tự động)
Chi phí mục tiêu: ≤[x] VND/tháng

### Giai đoạn 3: Ổn định (18+ tháng)
Mục tiêu: [x] user, doanh thu [x] VND/tháng
Chiến lược giá:
- Đa dạng gói: Starter / Pro / Enterprise
- Tự động hóa support để giảm chi phí nhân sự
- Tính giá theo mức sử dụng (usage-based pricing)
```

### Bước 6: Đề xuất các gói linh hoạt — Giới hạn tính năng theo chi phí

**QUY TẮC VÀNG khi đặt giới hạn:**
- Giới hạn phải dựa trên **chi phí thực tế**, không phải "cho có con số đẹp"
- Mỗi gói cần có **ít nhất 1 tính năng bị cắt** rõ ràng để khuyến khích upgrade
- Tỉ lệ giá/giới hạn nên tăng dần để upgrade có ý nghĩa kinh tế

**Công thức tính giới hạn (token-based — chính xác hơn request-based):**

```
Bước 1: Tính chi phí/1 request
  = (Input tokens × Giá input/1M) + (Output tokens × Giá output/1M)

Bước 2: Tính giới hạn mỗi gói
  = (Giá gói VND ÷ Tỉ giá USD/VND) ÷ Chi phí/1 request

Ví dụ — App viết email, GPT-4o mini:
  - Input: 500 tokens, Output: 300 tokens/lần
  - Chi phí/lần = (500 × $0.15/1M) + (300 × $0.60/1M) = $0.000255

  Starter 15K VND ÷ 24.000 = $0.000625
    → Giới hạn = $0.000625 ÷ $0.000255 ≈ 2 lần → quá ít, nâng lên 5 lần/tuần
  Basic 49K VND ÷ 24.000 = $0.00204
    → Giới hạn = $0.00204 ÷ $0.000255 ≈ 8 lần → OK thành 10 lần/tháng
  Pro 99K VND ÷ 24.000 = $0.004125
    → Giới hạn = $0.004125 ÷ $0.000255 ≈ 16 lần → OK thành 50 lần/tháng
```

**Loại giới hạn phù hợp cho từng sản phẩm:**

| Loại giới hạn | Phù hợp với | Ví dụ |
|--------------|------------|-------|
| **Requests/giới hạn** | App đơn giản, mỗi lần gọi tương đương nhau | Chatbot đơn giản |
| **Tokens/giới hạn** | App có đầu vào/output thay đổi nhiều | Viết bài, phân tích dài/ngắn |
| **Minutes/giới hạn** | App audio/video | TTS, transcription |
| **Characters/giới hạn** | App dịch thuật, tóm tắt | Dịch, paraphrasing |
| **Soft cap Unlimited** | Gói cao nhất nhưng vẫn có giới hạn ẩn | Tránh abuse, đặt max 5.000 requests/ngày |

**Tính năng bị cắt theo gói — 5 mô hình phổ biến:**

```
Mô hình 1 — Cắt theo số lượng (đơn giản nhất):
  Starter: X requests | Basic: Y requests | Pro: Z requests | Enterprise: Unlimited

Mô hình 2 — Cắt theo loại tính năng (khuyến khích upgrade mạnh):
  Starter: Tính năng A | Basic: A + B | Pro: A + B + C | Enterprise: Tất cả

Mô hình 3 — Cắt theo chất lượng model:
  Starter: GPT-3.5 | Basic: GPT-4o mini | Pro: GPT-4o | Enterprise: Custom fine-tune

Mô hình 4 — Cắt theo tốc độ xử lý:
  Starter: Queue 60s | Basic: Queue 30s | Pro: Priority 10s | Enterprise: Instant

Mô hình 5 — Cắt theo hỗ trợ:
  Starter: Documentation | Basic: +Email | Pro: +Priority | Enterprise: +Live chat + SLA
```

Tạo ít nhất 3 gói, có cả gói tuần cho sinh viên:

```
## 📦 CÁC GÓI ĐỀ XUẤT — Giới hạn & Tính năng

### Tính năng sản phẩm: [Liệt kê tất cả tính năng ở đây]

### Bảng tổng quan

| Gói | Giá | Giới hạn | Tính năng | Phù hợp |
|-----|-----|----------|-----------|---------|
| 🥉 Starter (tuần) | xx.000 VND/tuần | X requests/tuần | A, B | Test thử |
| 🥈 Basic (tháng) | xx.000 VND/tháng | X requests/tháng | A, B, C | Cá nhân |
| 🥇 Pro (tháng) | xx.000 VND/tháng | X requests/tháng | A, B, C, D | Freelancer |
| 🏆 Enterprise (tháng) | xxx.000 VND/tháng | Soft Unlimited | Tất cả + SLA | Doanh nghiệp |

### Chi tiết từng gói

#### 🥉 Starter — "Biết thử"
- **Giá:** xx.000 VND/tuần
- **Giới hạn:** X requests/tuần (≈ x tokens/tuần nếu dùng token)
- **Tính năng:** [A, B]
- **Bị cắt:** [Tính năng C, D], [Giới hạn thấp]
- **Ví dụ thực tế:** 5 email/tuần, 10.000 tokens/tuần, 1 document/tuần

#### 🥈 Basic — "Dùng quen"
- **Giá:** xx.000 VND/tháng
- **Giới hạn:** X requests/tháng (≈ x tokens/tháng)
- **Tính năng:** [A, B, C]
- **Bị cắt:** [Tính năng D], [Không có history], [Không export]
- **Ví dụ thực tế:** 30 email/tháng, 50.000 tokens/tháng, 5 documents/tháng

#### 🥇 Pro — "Dùng nghiêm túc"
- **Giá:** xx.000 VND/tháng
- **Giới hạn:** X requests/tháng (≈ x tokens/tháng)
- **Tính năng:** [A, B, C, D] — đầy đủ
- **Bonus:** Priority support, history 90 ngày, export PDF/Word, API access
- **Ví dụ thực tế:** 200 email/tháng, 500.000 tokens/tháng, unlimited documents

#### 🏆 Enterprise — "Không giới hạn"
- **Giá:** xxx.000 VND/tháng
- **Giới hạn:** Soft cap — max X requests/ngày (tránh abuse)
- **Tính năng:** Tất cả + Custom integration + Dedicated support + SLA 99.9%
- **Ví dụ thực tế:** 5.000 requests/ngày, team 10 người, whitelist IP

### So sánh giá theo chu kỳ:

| Gói | Tuần | Tháng | Quý (giảm 10%) | Năm (giảm 20%) |
|-----|------|-------|----------------|----------------|
| Starter | xxK | — | — | — |
| Basic | — | xxK | xx.xxx | xx.xxx |
| Pro | — | xxK | xx.xxx | xx.xxx |
| Enterprise | — | xxxK | xxx.xxx | xxx.xxx |

> 💡 **Mẹo cho sinh viên:**
> - **Token-based > Request-based** — user biết chính xác mình có bao nhiêu "nguồn lực" thay vì không rõ mỗi request dài/ngắn
> - **4 gói tuần = gói tháng giảm ~10–15%** — khuyến khích cam kết dài hạn
> - **"Unlimited" luôn có soft cap** — đặt max 5.000 requests/ngày để tránh bị abuse
> - **Model tiering là cách tốt để cắt** — Starter dùng GPT-3.5 (rẻ), Pro dùng GPT-4o (đắt hơn 40x) → tự động phân tách chi phí

---

## Quality Checklist

Trước khi trình bày output, tự kiểm tra:

- [ ] Tên sản phẩm được nhắc lại trong tiêu đề
- [ ] Tất cả số liệu có nguồn (thực tế hoặc ước lượng, ghi rõ)
- [ ] Tổng chi phí được tính đúng (cố định + biến đổi + nhân sự)
- [ ] Điểm hòa vốn được tính và giải thích = bao nhiêu user
- [ ] Tỉ giá được so sánh với thị trường VN, không phải giá quốc tế
- [ ] Lộ trình có ít nhất 2 giai đoạn với mục tiêu cụ thể
- [ ] Có gói tuần — phù hợp tài chính sinh viên
- [ ] Lưu ý về "không tính công mình" được nhấn mạnh
- [ ] Mỗi gói có giới hạn tính năng rõ ràng (dựa trên chi phí thực tế)
- [ ] Có ít nhất 1 tính năng bị cắt ở mỗi gói thấp hơn Enterprise
- [ ] Giới hạn tính năng được giải thích bằng công thức, không phải "số đẹp"

---

## References

- `references/bang-gia-api-2024.md` — Bảng giá API LLM phổ biến
- `references/bang-gia-hosting-vn.md` — Bảng giá hosting/server tại VN
- `references/mau-doi-thu.md` — Mẫu so sánh giá với đối thủ cạnh tranh

---

## Negative Boundaries

Skill này KHÔNG làm:
- ❌ Viết code sản phẩm AI
- ❌ Thiết kế UI/UX
- ❌ Tạo nội dung marketing quảng cáo
- ❌ Phân tích kỹ thuật AI (model, prompt engineering)
- ❌ Dự đoán doanh thu chính xác (chỉ ước lượng dựa trên số liệu đầu vào)
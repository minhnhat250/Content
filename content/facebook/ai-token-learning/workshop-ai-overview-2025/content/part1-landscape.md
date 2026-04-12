# PART 1 — BỨC TRANH TOÀN CẢNH AI 2026

**Thời lượng:** 60 phút

Sau phần này, bạn sẽ hiểu AI landscape, biết mình đang đứng ở đâu, và nắm vững 4 tầng: ML → DL → LLM → Agents.

---

## HOOK — "3 Câu Hỏi Trước Khi Bạn Bị Bỏ Lại"

### Ice Breaker (5 phút)

Facilitator hỏi — học viên giơ tay:

**Câu hỏi 1:** "Ai đã dùng ChatGPT hoặc Claude hôm qua?"
*(~80% giơ tay)*

**Câu hỏi 2:** "Ai đã dùng AI để làm việc (không phải để chat chơi)?"
*(~40% giơ tay)*

**Câu hỏi 3:** "Ai biết 'Agentic AI' là gì?"
*(~5-10% giơ tay)*

---

### Pain Point Setup (5 phút)

> "Nhìn thấy đấy — 80% các bạn dùng AI hàng ngày, nhưng chỉ 40% dùng nó để LÀM VIỆC thật sự. Và chỉ 5-10% biết Agentic AI là gì. Đó chính là gap mà hôm nay chúng ta sẽ lấp đầy."

Hôm nay trong 4 tiếng, bạn sẽ:

1. Hiểu AI đang ở đâu — không phải 2022, không phải 2023 — mà là **2026**
2. Biết 4 cấp độ AI: ML → DL → LLM → Agents
3. **Tự tay dùng** cả model ML (train MNIST) lẫn AI Agent (không cần code)
4. Có kế hoạch cá nhân để ứng dụng AI vào công việc **NGAY TUẦN NÀY**

> Không lý thuyết suông. Không ngồi nghe 4 tiếng. Let's build something.

---

### Quick Demo Setup (5 phút)

Facilitator mở demo trên màn hình:

> "Trước khi vào lý thuyết — để tôi cho bạn xem AI đang làm được gì TRONG THỰC TẾ 2026."

- **Demo 1:** GPT-4o / Claude trả lời câu hỏi phức tạp (30 giây)
- **Demo 2:** AI Agent tự tìm kiếm web + viết code + gửi email *(hoặc video demo)*
- **Demo 3:** Image generation *(tùy setup)*

> "Đó không phải tương lai. Đó là HIỆN TẠI. Và hôm nay bạn sẽ biết nó hoạt động thế nào."

---

## PHẦN 1A — AI Ecosystem Map 2026

### Sơ Đồ Toàn Cảnh

AI Ecosystem 2026 gồm 4 tầng xếp chồng lên nhau:

| **Tầng** | **Tên** | **Ý nghĩa** | **Ví dụ** |
|---|---|---|---|
| **4 (Trên)** | Agentic AI | AI không chỉ trả lời — AI **hành động** | Claude Agent, GPTs, AutoGPT |
| **3** | Large Language Models | AI hiểu và sinh ngôn ngữ con người | GPT-4, Claude 3, Gemini, Llama |
| **2** | Deep Learning | Neural network nhiều lớp — tự học đặc trưng | CNN, RNN/LSTM, Transformer |
| **1 (Dưới)** | Machine Learning | Máy học từ dữ liệu — không cần lập trình từng rule | Linear Regression, Random Forest, XGBoost |

**Nền tảng công nghệ:** Python · PyTorch · TensorFlow · scikit-learn · Hugging Face · CUDA

---

### Giải Thích Từng Tầng — "Tòa Nhà AI"

**Tầng 1 — Machine Learning (Móng nhà)**
> ML giống như nền móng nhà. Không thấy được nhưng **RẤT QUAN TRỌNG**.
> Cho máy xem 10,000 email spam → máy tự tìm pattern. Không cần viết rule "nếu có từ X thì là spam."

**Tầng 2 — Deep Learning (Các tầng căn hộ)**
> DL như các tầng căn hộ. Neural network nhiều lớp.
> Điểm khác biệt: DL **tự học đặc trưng** từ dữ liệu thô — không cần con người định nghĩa.

**Tầng 3 — Large Language Models (Tầng penthouse)**
> LLM như tầng penthouse. Model **KHỔNG LỒ** được train trên toàn bộ internet.
> 1 model biết NHIỀU THỨ: dịch thuật, viết code, phân tích pháp lý, y khoa...

**Tầng 4 — Agentic AI (Mái nhà thông minh)**
> Agentic AI như mái nhà thông minh. **KHÔNG chỉ trả lời — mà HÀNH ĐỘNG.**
> AI gọi tool, tìm kiếm web, viết code, gửi email — tự động.

---

### Timeline 2020–2026

| Năm | Sự kiện | Ý nghĩa |
|---|---|---|
| 2020 | GPT-3 (175 tỷ tham số) | LLM bắt đầu |
| 2022 | Deep Learning phổ biến | DL vào production |
| 2023 | ChatGPT ra mắt | LLM bùng nổ |
| 2024 | GPT-4, Multimodal models | LLM đa phương thức |
| 2025 | Agentic AI mainstream | AI bắt đầu HÀNH ĐỘNG |
| 2026 | MCP/A2A Protocol | Tiêu chuẩn cho Multi-Agent 🔬VERIFY |

> **Câu hỏi thảo luận (2 phút):** "Theo bạn, đâu là thời điểm quan trọng nhất trong timeline này? Tại sao?"

---

## PHẦN 1B — Phân Biệt 4 Tầng AI

### So Sánh Chi Tiết

| Tiêu chí | ML | DL | LLM | Agentic AI |
|---|---|---|---|---|
| **Ví dụ** | Gmail spam filter, Netflix recommendation | Nhận diện khuôn mặt, dịch thuật | ChatGPT, Claude, Gemini | AutoGPT, Claude Agent |
| **Input** | Dữ liệu có nhãn | Ảnh, âm thanh, text | Prompt (text) | Task / Goal |
| **Output** | Dự đoán, phân loại | Phân loại, sinh nội dung | Text, code, giải thích | Hành động hoàn chỉnh |
| **Cần dữ liệu** | Ít (1K–100K) | Nhiều (100K–10M) | Rất nhiều (train sẵn) | Kết hợp tools |
| **Cần GPU mạnh?** | Không / nhẹ | Có (training) | Không (dùng API) | Có thể |
| **Cần code?** | Có (Python/Scikit) | Có (PyTorch/TF) | Không (chỉ prompt) | Một chút |
| **Thời gian học** | 1–3 tháng | 3–6 tháng | Vài ngày | Vài tuần |

---

### AI Tốt Nhất 2026 — ⚠️ VERIFY

> Thông tin dưới đây dựa trên knowledge cutoff tháng 8/2025. **Cần verify trước workshop.**

| Category | Model tiêu biểu | Ghi chú |
|---|---|---|
| General LLM | Claude 3.7/4 (Anthropic), GPT-4.5/o4 (OpenAI), Gemini 2.0 (Google) | Verify models mới 2026 |
| Code Generation | Claude (Anthropic), Copilot (GitHub), Cursor | Rất mạnh |
| Image Generation | DALL-E 3, Midjourney v7, Stable Diffusion 3, FLUX | Verify 2026 |
| Video Generation | Sora (OpenAI), Veo (Google), Kling | Verify 2026 |
| Agentic AI | Claude Agent, GPTs, AutoGPT, LangChain agents | Đang phát triển nhanh |
| Multimodal | GPT-4o, Gemini Ultra, Claude 3 | Verify 2026 |
| Open Source | Llama 3/4 (Meta), Mistral, Qwen (Alibaba) | Verify 2026 |

---

### Thống Kê 2026 — ⚠️ VERIFY

Các con số dưới đây từ 2024–2025. **Cần verify trước workshop.**

| Chủ đề | Con số |
|---|---|
| **AI Market** | Thị trường AI toàn cầu: ~$400–600 tỷ USD 🔬VERIFY |
| **Enterprise Adoption** | 92% Fortune 500 dùng AI (2024) 🔬VERIFY |
| **Job Impact** | AI tạo ~4.4 triệu việc làm toàn cầu 🔬VERIFY |
| **ChatGPT Users** | 180+ triệu người dùng hàng tháng 🔬VERIFY |
| **Claude Users** | 10+ triệu người dùng 🔬VERIFY |
| **AI Agent Market** | Doanh thu ~$5–10 tỷ 🔬VERIFY |
| **Developers** | 60% developers đang thử nghiệm Agent 🔬VERIFY |

---

## PHẦN 1C — Q&A + Transition

> "Có câu hỏi gì về AI Landscape không? Đây là nền tảng — nắm vững phần này thì các phần sau sẽ dễ hiểu hơn nhiều."

**Transition:**

> "OK. Giờ chúng ta đi vào **PHẦN 2** — từ ML đến Deep Learning. Tôi sẽ cho bạn thấy TẠI SAO DL mạnh hơn ML thông thường, VÀ bạn sẽ tự tay train model nhận diện chữ số viết tay. Let's go."

---

## CHECKPOINT — PART 1

**Câu 1:** AI Agent khác LLM thông thường ở điểm nào?

- a) LLM trả lời, Agent **HÀNH ĐỘNG** ✅
- b) LLM nhanh hơn
- c) Agent không dùng được text

> ✅ **Đáp án: a)** — Agent có khả năng plan → act → use tools, không chỉ generate text.

---

**Câu 2:** Bạn muốn lọc email spam. Nên dùng ML hay DL?

- a) DL (vì nó mới hơn)
- b) ML cơ bản ✅
- c) LLM

> ✅ **Đáp án: b)** — Không cần dùng DL cho bài toán đơn giản. ML cổ điển (Random Forest, Naive Bayes) là đủ và nhanh.

---

Tiếp theo: [PART 2 — TỪ ML ĐẾN DEEP LEARNING](./part2-ml-dl.md)
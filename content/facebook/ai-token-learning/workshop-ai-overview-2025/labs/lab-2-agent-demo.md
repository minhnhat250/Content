# LAB 2 — AI Agent Hands-on
## "Từ Chatbot → Autonomous Agent"

**Mục tiêu:** Trải nghiệm AI Agent hoạt động như thế nào — không cần code
**Thời gian:** 20–30 phút
**Công cụ:** Claude Web / ChatGPT / Perplexity (tài khoản free)
**Level:** Beginner — không cần biết code

---

## Mục Tiêu Lab

```
Sau lab này, bạn sẽ:
✅ Hiểu AI Agent khác chatbot thế nào
✅ Biết cách dùng Agent với tools (search, code, etc.)
✅ Trải nghiệm "AI tự hành động" — không chỉ trả lời
✅ Hiểu 3 bước: Plan → Act → Reflect
```

---

## Prerequisites

- [ ] Tài khoản Claude (free): [claude.ai](https://claude.ai)
- [ ] Hoặc ChatGPT Plus (optional)
- [ ] 20–30 phút rảnh

---

## Từ Chatbot → Agent — Giải Thích Nhanh

**Chatbot (LLM thường):**
> User: "Research competitors của startup fintech Việt Nam"
> Claude: [Trả lời dựa trên kiến thức có sẵn]

**Agentic AI:**
> User: "Research competitors của startup fintech Việt Nam → gửi summary vào email của tôi"
> Agent: [1. Search web → 2. Tổng hợp → 3. Viết email → 4. Gửi]

**Trong lab này:** Chúng ta sẽ THỰC HÀNH cách dùng Agent features trong Claude.

---

## Option A — Dùng Claude Web (Free — Khuyến nghị)

### Step 1: Mở Claude + Chọn Model Có Tool Use (2 phút)

**Truy cập:** [https://claude.ai](https://claude.ai)

**Chọn model:**

- **Claude 3.7 Sonnet** (có tool use) — Free
- Hoặc **Claude 3 Opus** (nếu có Plus)

> **Lưu ý:** Tool use (search, code) chỉ có trong Claude Sonnet/Opus. Free tier có giới hạn.

---

### Step 2: Agent Task #1 — Research + Write (10 phút)

**Gõ prompt sau vào Claude:**

```
Tôi muốn bạn làm research về:
1. Top 5 AI startups tại Việt Nam năm 2026
2. Funding của họ
3. Sản phẩm chính

Sau đó viết:
- Executive summary (200 từ)
- 3 insights quan trọng
- Định dạng markdown
```

**Bạn sẽ thấy:**

```
Thinking: Claude đang LẬP KẾ HOẠCH research...
Searching: Claude tự tìm kiếm thông tin
Writing: Claude viết báo cáo
```

✅ **Checkpoint:** Nếu Claude trả lời với thông tin CỤ THỂ (không chung chung) → Đang dùng tool search.

---

### Step 3: Agent Task #2 — Code + Execute (10 phút)

**Gõ prompt sau:**

```
Viết Python code để:
1. Đọc file CSV (data mẫu: giá nhà)
2. Vẽ biểu đồ giá theo diện tích
3. Train linear regression model
4. Dự đoán giá cho 1 căn nhà 100m2

Chạy code và cho tôi kết quả.
```

**Bạn sẽ thấy:**

```
Claude VIẾT code
Claude TẠO Python file
Claude CHẠY code
Kết quả hiển thị
```

✅ **Checkpoint:** Claude viết code + chạy + trả kết quả → Bạn đang dùng AI Agent.

---

### Step 4: Agent Task #3 — Multi-Step Reasoning (10 phút)

**Gõ prompt phức tạp:**

```
Tôi đang cân nhắc xây dựng AI chatbot cho dịch vụ khách hàng của công ty bán hàng online.
Ngân sách: 50 triệu VNĐ
Team: 1 developer + 1 designer

Hãy:
1. Phân tích pros/cons của việc dùng:
   a) Build from scratch (LLM API)
   b) Dùng platform có sẵn (Intercom AI, Zendesk AI)
2. Đề xuất giải pháp tối ưu nhất
3. Roadmap 3 tháng đầu tiên
4. Ước tính chi phí chi tiết

Trả lời bằng tiếng Việt, định dạng rõ ràng.
```

✅ **Checkpoint:** Claude đưa ra analysis sâu + pros/cons + roadmap cụ thể → Đang dùng advanced reasoning.

---

## Option B — Dùng Perplexity (AI Search Engine)

### Step 5: Thử Perplexity Agent (5 phút)

**Truy cập:** [https://perplexity.ai](https://perplexity.ai)

Perplexity = AI Agent tích hợp sẵn search. Mỗi câu hỏi = tự động search + tổng hợp.

**Thử prompt:**

```
Research và so sánh: FPT AI, Viettel AI, VNG AI.
Ai có những sản phẩm gì?
Funding/status ra sao?
Output: Bảng so sánh
```

✅ **Checkpoint:** Perplexity trả lời với SOURCES (link) cụ thể → Đây là Agent với tool search.

---

## BONUS — Claude Code (CLI Agent) — Advanced

> **Advanced — Cần cài đặt. Bỏ qua nếu bạn là beginner.**

### Step 6: Claude Code — AI Agent Trong Terminal

**Cài đặt:**

```bash
# macOS
brew install anthropic/formulas/claude-code

# Hoặc: npm install -g @anthropic-ai/claude-code
```

**Dùng:**

```bash
# Mở Claude Code trong thư mục project
claude

# Gõ task
> "Tạo một web app đơn giản bằng HTML/CSS để hiển thị danh sách sản phẩm"
```

Claude Code sẽ:

1. Lập kế hoạch
2. Viết code
3. Tạo files
4. Test
5. Báo cáo kết quả

---

## Challenges Thêm

**Challenge 1: Agent Workflow**
> Thiết kế 1 workflow tự động cho công việc CỦA BẠN:
> - Input → AI Research → AI Draft → Human Review → Output
> - Viết prompt cho từng bước

**Challenge 2: So Sánh Agents**
> Thử cùng 1 prompt trên:
> - Claude
> - ChatGPT
> - Perplexity
> → So sánh chất lượng + tốc độ + nguồn tham khảo

**Challenge 3: Build GPT/Claude Custom**
> Tạo custom GPT (ChatGPT) hoặc Claude Project cho:
> - Task cụ thể của bạn
> - Với instructions, knowledge, actions
> → Đây là cách tạo "Agent" đơn giản nhất

---

## Bài Tập Về Nhà

1. **Thử 3 Agent tasks** khác nhau — ghi lại kết quả
2. **Thiết kế AI workflow** cho 1 task trong công việc của bạn
3. **Tạo custom GPT/Claude Project** cho task thường dùng
4. **Viết blog** về trải nghiệm: "Tôi đã dùng AI Agent thế nào"

---

## Những Điều Bạn Đã Học

| Concept | Tool |
|---|---|
| Chatbot (LLM) | Trả lời câu hỏi |
| Agentic AI | Plan + Act + Reflect |
| Tool Use (Search) | Claude search web |
| Tool Use (Code) | Claude write + run code |
| Multi-step reasoning | Complex analysis → output |
| Custom Agent | GPTs / Claude Projects |

---

## Link Hữu Ích

| Resource | Link |
|---|---|
| Claude.ai | [claude.ai](https://claude.ai) |
| Perplexity | [perplexity.ai](https://perplexity.ai) |
| ChatGPT | [chat.openai.com](https://chat.openai.com) |
| Claude Projects | Hướng dẫn trong Claude Web |
| Custom GPTs | Hướng dẫn trong ChatGPT |

---

## Tổng Kết Lab 2

```
✅ Đã thử AI Agent thật sự (Claude, Perplexity)
✅ Hiểu Plan → Act → Reflect
✅ Biết dùng tool use (search, code)
✅ Biết cách tạo custom agent (GPTs/Projects)
```

**→ Tiếp theo: QUIZ cuối workshop**
# Bảng Giá API LLM Phổ Biến — Cập nhật 2024–2025

## Mục đích
Tham khảo nhanh chi phí API LLM khi tính chi phí sản phẩm AI. Dùng để ước lượng chi phí API nếu sinh viên chưa biết số liệu.

## Khi nào tải
Khi user cần ước lượng chi phí API LLM hoặc cần so sánh giá giữa các provider.

---

## Các Provider Phổ Biến (2024–2025)

### OpenAI

| Model | Input ($/1M tokens) | Output ($/1M tokens) | Phù hợp |
|-------|--------------------|-----------------------|---------|
| GPT-4o | ~$2.50 | ~$10 | Doanh nghiệp, task phức tạp |
| GPT-4o mini | ~$0.15 | ~$0.60 | Startup, sản phẩm production |
| GPT-4 Turbo | ~$10 | ~$30 | Task cần chất lượng cao |
| GPT-3.5 Turbo | ~$0.50 | ~$1.50 | Prototype, test nhanh |

### Anthropic (Claude)

| Model | Input ($/1M tokens) | Output ($/1M tokens) | Phù hợp |
|-------|--------------------|-----------------------|---------|
| Claude 3.5 Sonnet | ~$3 | ~$15 | Doanh nghiệp, writing task |
| Claude 3.5 Haiku | ~$0.25 | ~$1.25 | Production, tốc độ cao |
| Claude 3 Opus | ~$15 | ~$75 | Task cần reasoning mạnh |

### Google Gemini

| Model | Input ($/1M tokens) | Output ($/1M tokens) | Phù hợp |
|-------|--------------------|-----------------------|---------|
| Gemini 1.5 Flash | **Miễn phí** (1.5M tok/tháng) | Miễn phí | Sinh viên, prototype |
| Gemini 1.5 Flash (trả phí) | ~$0.075 | ~$0.30 | Production |
| Gemini 1.5 Pro | ~$1.25 | ~$5 | Task phức tạp, dài |

### Các Provider Khác

| Provider | Model | Giá | Ghi chú |
|----------|-------|-----|---------|
| Groq | Llama 3.1 70B | Miễn phí (rate limit) | Tốc độ cực nhanh, free |
| Groq | Mixtral 8x7B | Miễn phí (rate limit) | Free, production OK |
| Cohere | Command R+ | ~$3/$12 | RAG, enterprise |
| Mistral | Mistral Large | ~$2/$8 | Châu Âu, EU data |

---

## Ước Lượng Token Theo Loại Task

| Loại Task | Prompt trung bình | Output trung bình | Tổng/token/lần |
|----------|-----------------|-------------------|---------------|
| Chat đơn giản | 500 tokens | 200 tokens | 700 |
| Phân tích văn bản | 2.000 tokens | 500 tokens | 2.500 |
| Tạo nội dung dài | 1.000 tokens | 1.500 tokens | 2.500 |
| Viết code | 1.000 tokens | 800 tokens | 1.800 |
| Hỏi đáp tài liệu (RAG) | 3.000 tokens | 300 tokens | 3.300 |

---

## Quy Tắc Ước Lượng Chi Phí API Nhanh

```
Chi phí API/tháng = Số user × Lần gọi/user/tháng × Token/lần × Giá/token

Ví dụ:
- 50 user × 20 lần × 2.000 token × $0.00015
= 50 × 20 × 2.000 × $0.00015
= 50 × 20 × $0.30
= $300/tháng (~7.5M VND)
```

---

## Mẹo Cho Sinh Viên

1. **Bắt đầu với Google Gemini Flash miễn phí** → không tốn gì, học cách đo lường
2. **Khi có 50+ user trả phí** → nâng cấp lên GPT-4o mini hoặc Claude Haiku
3. **Luôn ước lượng 3x** → thực tế thường cao hơn 30–50% vì user không dùng đúng như ước tính
4. **Set cap API spending** → tránh bills bất ngờ cuối tháng
5. **Dùng Groq miễn phí** cho dev/test trước khi production
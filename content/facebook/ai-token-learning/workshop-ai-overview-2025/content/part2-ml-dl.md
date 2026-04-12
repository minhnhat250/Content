# PART 2 — MACHINE LEARNING → DEEP LEARNING
## + VỊ TRÍ CỦA BẠN TRONG THẾ GIỚI AI

**Thời lượng:** 60 phút

Sau phần này, bạn sẽ hiểu ML vs DL, biết mình NÊN đi theo hướng nào, và biết ĐIỂM ĂN TIỀN ở mỗi tầng.

---

## MODULE 1 — MACHINE LEARNING

### Mục tiêu

- Hiểu ML là gì (bằng analogi đơn giản)
- Biết 3 loại ML: Supervised, Unsupervised, Reinforcement
- **QUAN TRỌNG:** Biết ĐIỂM ĂN TIỀN của ML — dùng NGAY trong công việc

---

### 1.1. ML là gì?

**Trước 2012:**
Muốn máy tính nhận diện mèo → phải viết RULES: "Nếu có 2 mắt + 4 chân + lông → đó là mèo." → Lỗi = vô số.

**Từ 2012:**
ML ra đời: "Đây 10,000 ảnh mèo + 10,000 ảnh chó. Tự đi tìm SỰ KHÁC NHAU." → Máy tự học pattern.

**Analogi — Con chó:**

> ML giống như dạy con chó ngồi. Bạn không nói "gập chân trước 15 độ, giữ 3 giây" — bạn **thưởng bánh khi nó ngồi đúng**, không thưởng khi sai. Sau 20 lần, con chó TỰ BIẾT ngồi.
>
> - **ML = con chó**
> - **Dữ liệu = bánh**
> - **Training = quá trình dạy**

---

### 1.2. Ba Loại ML

| Loại | Giải thích | Dùng khi nào | Ví dụ |
|---|---|---|---|
| **Supervised Learning** | Học có GIÁO VIÊN (có label) | Có data có nhãn | Email spam/not spam, dự đoán giá nhà |
| **Unsupervised Learning** | Tự khám phá pattern | Không có label | Phân nhóm khách hàng, tìm anomaly (lừa đảo) |
| **Reinforcement Learning** | Học từ THƯỞNG và PHẠT | Cần tự học qua tương tác | AlphaGo, robot tự đi, game AI |

---

### 1.3. Thuật Toán ML Phổ Biến

| Bài toán | Thuật toán | Độ khó | ĐIỂM ĂN TIỀN |
|---|---|---|---|
| Dự đoán giá nhà, giá cổ phiếu | Linear Regression, XGBoost | ⭐ | Freelance: phân tích dữ liệu tài chính |
| Phân loại email spam, churn | Logistic Regression, Random Forest | ⭐ | Startup: automate workflow, giảm churn |
| Phân nhóm khách hàng | K-Means, DBSCAN | ⭐⭐ | Marketing: customer segmentation |
| Phát hiện gian lận | Anomaly Detection, Isolation Forest | ⭐⭐ | Fintech: fraud detection |
| Gợi ý sản phẩm | Collaborative Filtering, Matrix Factorization | ⭐⭐ | E-commerce: recommendation engine |
| Dự đoán chuỗi thời gian | Prophet, LSTM, LightGBM | ⭐⭐⭐ | Operations: demand forecasting |

---

### 1.4. ĐIỂM ĂN TIỀN #1 — ML Trong Công Việc Hàng Ngày

Facilitator hỏi: *"Ai trong các bạn làm marketing/sales/finance?"*

#### Case 1: Data Analyst → Tự động báo cáo

Bạn làm báo cáo Excel mỗi tuần. ML giúp: **tự động phát hiện anomaly** trong dữ liệu bán hàng → gửi alert cho sếp TRƯỚC KHI vấn đề xảy ra.

- **Công cụ:** scikit-learn + Python, chỉ cần biết copy-paste
- **Thu nhập thêm:** Freelance ML consulting $50–100/giờ 🔬VERIFY

#### Case 2: Content Creator → Biết content nào viral

ML giúp phân tích pattern của các bài viral trên fanpage → **gợi ý chủ đề tiếp theo**.

- **Công cụ:** Hugging Face (không cần code sâu)
- **Điểm ăn tiền:** Tư vấn content strategy cho brand

#### Case 3: Kinh doanh nhỏ → Dự đoán tồn kho

Dùng Linear Regression đơn giản để **dự đoán sản phẩm nào bán chạy tuần tới** → giảm tồn kho 30%.

- **Công cụ:** Google Sheets + Apps Script (không cần Python)
- **Điểm ăn tiền:** Tư vấn inventory optimization cho cửa hàng

---

### 1.5. VỊ TRÍ CỦA BẠN — Hướng Đi ML

Bạn làm gì? Tôi sẽ chỉ bạn đi theo hướng nào:

**Bạn là NHÂN VIÊN VĂN PHÒNG (HR/Finance/Marketing)**

- Đi hướng: ML for Business (không cần code nhiều)
- Tool: Google Sheets ML, no-code tools (Make.com, Zapier AI)
- ĂN TIỀN: Automate công việc nhàm chán, tăng productivity

---

**Bạn LẬP TRÌNH VIÊN**

- Đi hướng: ML Engineer / Data Scientist
- Tool: Python + scikit-learn + XGBoost
- ĂN TIỀN: Junior ML Engineer $60–100K/năm 🔬VERIFY

---

**Bạn là SINH VIÊN / Người mới**

- Đi hướng: Học ML foundations → Kaggle competitions
- Tool: Python + Colab + Kaggle
- ĂN TIỀN: Portfolio ML → xin thực tập ML

---

**Bạn là CHỦ DOANH NGHIỆP / QUẢN LÝ**

- Đi hướng: Hiểu ML để RA QUYẾT ĐỊNH, không cần code
- Tool: Tableau, Power BI, no-code AI platforms
- ĂN TIỀN: Ứng dụng ML vào business — giảm chi phí, tăng doanh thu

---

## MODULE 2 — DEEP LEARNING

### Mục tiêu

- Hiểu DL khác ML ở điểm nào (và KHI NÀO cần dùng DL)
- Biết 3 kiến trúc: CNN, RNN/LSTM, Transformer
- **QUAN TRỌNG:** Biết VỊ TRÍ CỦA BẠN trong thế giới DL

---

### 2.1. Tại Sao Cần Deep Learning?

**Câu chuyện 2012:**

2012: **AlexNet** thắng cuộc thi ImageNet — đánh dấu sự trỗi dậy của DL.

**Tại sao quan trọng?**
- Trước đó, ML thông thường cần con người **TỰ ĐỊNH NGHĨA** đặc trưng (feature engineering)
- DL **TỰ HỌC** đặc trưng từ dữ liệu thô. Không cần giáo viên.

**Điểm khác biệt ML vs DL:**

| | ML Thông Thường | Deep Learning |
|---|---|---|
| Feature Engineering | Con người tự định nghĩa | Tự học từ dữ liệu |
| Dữ liệu cần | Ít (1K–100K) | Nhiều (100K–10M) |
| GPU | Không cần / nhẹ | BẮT BUỘC để train |
| Giải thích được | Có (interpretable) | Khó (black box) |
| Chi phí | Thấp | Cao |

> **QUY TẮC VÀNG:**
> "Nếu bài toán của bạn có thể giải bằng ML thông thường — DÙNG ML. Đừng dùng DL chỉ vì nó 'hot'."
>
> DL chỉ cần thiết khi: ảnh phức tạp, âm thanh, video, text dài, hoặc khi ML không đủ.

---

### 2.2. Ba Kiến Trúc DL

| Kiến trúc | Tên đầy đủ | Dùng cho | Analogi |
|---|---|---|---|
| **CNN** | Convolutional Neural Network | Nhận diện vật thể trong ảnh, phát hiện khuôn mặt, bệnh trên X-quang, xe tự lái | "Như mắt người — quét từng vùng, nhận ra cạnh → hình dạng → đối tượng" |
| **RNN/LSTM** | Recurrent Neural Network | Dịch thuật, chatbot, phân tích cảm xúc, dự đoán giá cổ phiếu, speech recognition | "Như đọc câu — phải nhớ từ TRƯỚC để hiểu từ SAU" |
| **Transformer** | Self-Attention | GPT, Claude, Gemini — tất cả LLM hiện đại, dịch thuật, sinh text/ảnh/video, search, QA | "Đọc câu rất dài — nhìn TẤT CẢ từ cùng lúc để hiểu ngữ cảnh, không cần đọc từ trái sang phải" |

---

### 2.3. Ai Nên Học DL?

**BẠN NÊN học DL NẾU:**

- ✅ Làm Computer Vision (y tế, xe tự lái, quality control)
- ✅ Làm NLP/Text (chatbot, phân tích cảm xúc, translation)
- ✅ Muốn vào ngành AI nghiêm túc (research, senior ML)
- ✅ Có dữ liệu lớn (100K+ samples)
- ✅ Có GPU (hoặc tiền thuê cloud GPU)

**BẠN CHƯA CẦN DL NẾU:**

- ❌ Bài toán tabular đơn giản (XGBoost đủ rồi)
- ❌ Không có nhiều dữ liệu
- ❌ Cần interpretable model (giải thích cho sếp)
- ❌ Mới bắt đầu — học ML trước

---

### 2.4. ĐIỂM ĂN TIỀN #2 — DL Trong Thực Tế Việt Nam 2026 🔬VERIFY

| Hướng | Ví dụ cụ thể | Thu nhập | Độ khó |
|---|---|---|---|
| **Computer Vision cho Sản Xuất** | Kiểm tra sản phẩm lỗi bằng camera + CNN | $30–80K/năm 🔬VERIFY | ⭐⭐⭐ |
| **NLP cho Doanh Nghiệp** | Chatbot tự động, phân tích phản hồi khách hàng | $40–100K/năm 🔬VERIFY | ⭐⭐ |
| **AI Content Creation** | Sinh ảnh, video, text bằng AI cho brand | $20–50K/năm 🔬VERIFY | ⭐⭐ |

> **LỜI KHUYÊN VÀNG:**
> "Đừng cố trở thành researcher DL. Hãy TRỞ THÀNH NGƯỜI BIẾT ÁP DỤNG DL vào bài toán CỤ THỂ của ngành bạn. Người hiểu DL + hiểu business = giá trị cao nhất."

---

### 2.5. VỊ TRÍ CỦA BẠN — Bản Đồ Quyết Định

**"Tôi nên đi hướng nào?" — Trả lời trong 30 giây:**

```
Bạn làm gì?

├─ VĂN PHÒNG / KINH DOANH
│   → Dùng AI tools CÓ SẴN (ChatGPT, Claude, Gemini)
│   → KHÔNG cần học code ML
│   → ĂN TIỀN: Productivity x10

├─ DATA / ANALYTICS
│   → Học: Python → Pandas → ML (scikit-learn) → XGBoost
│   → ĂN TIỀN: Data Scientist / ML Analyst

├─ DEVELOPER / ENGINEER
│   → Học: Python → PyTorch → DL (CNN/RNN/Transformer)
│   → ĂN TIỀN: ML Engineer / AI Engineer

└─ NGHIÊN CỨU / HỌC THUẬT
    → Học: Math (calculus, linear algebra, probability)
        → PyTorch/TensorFlow → Research → Publish paper
    → ĂN TIỀN: AI Researcher / Professor
```

---

## CHECKPOINT — MODULE 1-2

**Câu 1:** Bạn cần dự đoán khách hàng nào sẽ rời bỏ (churn) trong 30 ngày. Nên dùng gì?

- a) Deep Learning (CNN)
- b) Machine Learning cơ bản (Random Forest, XGBoost) ✅
- c) Transformer

> ✅ **Đáp án: b)** — Bài toán tabular có label. ML thông thường đủ tốt.

---

**Câu 2:** Bạn muốn xây chatbot trả lời khách hàng tự động. Nên dùng gì?

- a) CNN
- b) LSTM / Transformer (LLM) ✅
- c) K-Means

> ✅ **Đáp án: b)** — Cần hiểu ngôn ngữ → NLP → RNN/LSTM/Transformer.

---

Tiếp theo: [PART 3 — LLM + AGENTS](./part3-llm-agents.md)
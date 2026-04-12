# 🧠 LỘ TRÌNH HỌC MACHINE LEARNING & DEEP LEARNING

> *Dành cho người mới bắt đầu — Tập trung Ứng dụng*
> *Tất cả tài liệu FREE — Không trả phí*

---

## 📋 TỔNG QUAN

| Phần | Nội dung | Thời gian | Cấp độ |
|:---:|---|---|:---:|
| **1** | Python & Math Foundations | 4–6 tuần | 🟢 Beginner |
| **2** | Classical ML (NB, KNN, DT, RF, XGBoost, K-Means) | 4–6 tuần | 🟡 Beginner–Intermediate |
| **3** | Deep Learning Cơ Bản (LR, Logistic, MLP, CNN) | 4–6 tuần | 🟠 Intermediate |
| **4** | Deep Learning Nâng Cao (RNN, Transformer, NLP, Vision, GenAI, LLM) | 6–8 tuần | 🔴 Advanced |
| **5** | ML Nâng Cao Chuyên Sâu (Time Series, Anomaly, Bayesian, GNN, RL) | 5–7 tuần | 🔴 Advanced |

> **⏱ Tổng thời gian:** 23–31 tuần (~6–8 tháng) học full-time
> **📌 Điều kiện:** Biết Python căn bản, máy có GPU (hoặc dùng Google Colab)

---

## 🛠 BẢNG TRA NHANH THƯ VIỆN

| Thư viện | Phần | Công dụng |
|---|:---:|---|
| **NumPy** | 1 | Đại số tuyến tính |
| **Pandas** | 1 | Xử lý dữ liệu bảng |
| **Matplotlib + Seaborn** | 1 | Trực quan hóa |
| **Scikit-learn** | 2 | Classical ML |
| **PyTorch** | 3–4 | Deep Learning |
| **Hugging Face Transformers** | 4 | NLP, LLM |
| **Ultralytics (YOLO)** | 4 | Object Detection |
| **LangChain** | 4 | LLM App |
| **Prophet / Darts** | 5 | Time Series |
| **PyTorch Geometric** | 5 | Graph ML |
| **Gymnasium + SB3** | 5 | Reinforcement Learning |
| **PyMC** | 5 | Bayesian ML |
| **Optuna + Auto-sklearn** | 5 | AutoML |

---

## 📖 SƯ PHẠM HỌC TẬP

1. **Không đọc quá nhiều lý thuyết** → Mỗi topic chỉ cần hiểu concept + làm project ngay
2. **48h rule** → Chọn 1 project, hoàn thành trong 48h — đừng kéo dài
3. **Mỗi tuần review** → Viết lại bằng ngôn ngữ của mình (blog/copy/notion)
4. **Dùng Git từ đầu** → Mỗi project = 1 repo, commit sau mỗi milestone
5. **Không có GPU?** → Dùng **Google Colab** (free tier có T4 GPU) hoặc **Kaggle Notebooks**

---

## 📚 NGUỒN TÀI LIỆU CHÍNH

| Nguồn | Mô tả | Miễn phí? |
|---|---|:---:|
| **Scaler.com** | Giải thích dễ hiểu, có code mẫu — thay thế Khan Academy / GFG | ✅ |
| **PyTorch Official** | Tài liệu chính thức PyTorch | ✅ |
| **Hugging Face** | Thư viện NLP/GenAI | ✅ |
| **Kaggle** | Dataset + notebooks miễn phí | ✅ |
| **Scikit-learn** | Tài liệu chính thức | ✅ |
| **GitHub** | Dự án open source | ✅ |
| **fast.ai** | Khóa thực hành Deep Learning | ✅ |

### Sách Free:
- **Think Stats** → [greenteapress.com/thinkstats2](https://greenteapress.com/thinkstats2)
- **Deep Learning for Coders with FastAI** → [course.fast.ai](https://course.fast.ai/)

---

## 🔗 DATASET PHỔ BIẾN

| Dataset | Link | Dùng cho |
|---|---|
| **Kaggle House Prices** | [kaggle.com/competitions/house-prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) | Regression |
| **Kaggle Titanic** | [kaggle.com/competitions/titanic](https://www.kaggle.com/competitions/titanic) | Binary classification |
| **Kaggle Wine Quality** | [kaggle.com/datasets/uciml/red-wine-quality](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009) | Classification & Regression |
| **UCI Heart Disease** | [kaggle.com/datasets/johnsmith88/heart-disease](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) | Multi-feature classification |
| **Kaggle Mall Customers** | [kaggle.com/datasets/vjchoudhary7/customer-segmentation](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) | K-Means |
| **Kaggle Airbnb NYC** | [kaggle.com/datasets/dgomonov/new-york-city-airbnb](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data) | XGBoost |
| **MNIST** | PyTorch có sẵn | CNN practice |
| **PhoBERT (Vietnamese)** | [Hugging Face vinai/PhoBERT](https://huggingface.co/vinai/PhoBERT) | Vietnamese NLP |

---

## ⚠️ LỖI THƯỜNG GẶP

| Lỗi | Nguyên nhân | Cách fix |
|---|---|
| `CUDA out of memory` | Model quá lớn | Giảm batch_size hoặc dùng float16 |
| Train acc cao nhưng test thấp | Overfitting | Dropout, regularization, early stopping |
| Loss không giảm | LR sai / data chưa normalize | Thử lr khác, scale dữ liệu |
| `NumPy dimension mismatch` | Matrix shape lệch | Check `.shape` trước khi nhân |

---

## 📂 CẤU TRÚC LỘ TRÌNH

```
PHẦN 1 ── Python & Math ───────────────  4–6 tuần  ── 🟢 Beginner
    ├─ 1.1 Setup môi trường · Python cơ bản
    ├─ 1.2 NumPy · Đại số tuyến tính
    ├─ 1.3 Pandas · Visualization
    ├─ 1.4 Xác suất & Thống kê
    ├─ 1.5 Calculus cơ bản
    └─ 1.6 Project PHẦN 1

PHẦN 2 ── Classical ML ───────────────  4–6 tuần  ── 🟡 Beginner–Intermediate
    ├─ 2.1 Naive Bayes
    ├─ 2.2 KNN
    ├─ 2.3 Decision Tree
    ├─ 2.4 Random Forest · AdaBoost
    ├─ 2.5 XGBoost · LightGBM
    ├─ 2.6 K-Means Clustering
    ├─ 2.7 Evaluation Metrics
    └─ 2.8 Project PHẦN 2

PHẦN 3 ── Deep Learning Cơ Bản ────────  4–6 tuần  ── 🟠 Intermediate
    ├─ 3.1 Perceptron · Neural Network
    ├─ 3.2 Linear Regression (NN approach)
    ├─ 3.3 Logistic Regression · Softmax
    ├─ 3.4 MLP · Backpropagation
    ├─ 3.5 Optimizers & Training
    ├─ 3.6 CNN cơ bản
    └─ 3.7 Project PHẦN 3

PHẦN 4 ── Deep Learning Nâng Cao ─────  6–8 tuần  ── 🔴 Advanced
    ├─ 4.1 RNN · LSTM · GRU
    ├─ 4.2 Transformer · Attention
    ├─ 4.3 NLP Ứng dụng
    ├─ 4.4 Computer Vision Nâng cao
    ├─ 4.5 Generative AI
    ├─ 4.6 LLM & Agent Systems
    └─ 4.7 Project PHẦN 4

PHẦN 5 ── ML Nâng Cao Chuyên Sâu ────  5–7 tuần  ── 🔴 Advanced
    ├─ 5.1 Time Series Forecasting
    ├─ 5.2 Anomaly Detection
    ├─ 5.3 Ensemble Methods Nâng Cao
    ├─ 5.4 Probabilistic ML · Bayesian
    ├─ 5.5 Graph Machine Learning
    ├─ 5.6 Reinforcement Learning
    ├─ 5.7 Meta-Learning · AutoML
    └─ 5.8 Project PHẦN 5
```

---

## ▶️ BẮT ĐẦU TỪ ĐÂY

### PHẦN 1 → Python & Math Foundations
👉 [Xem chi tiết: PHAN1-Python-Math-Foundations.md](./PHAN1-Python-Math-Foundations.md)

- Setup môi trường · Python cơ bản · NumPy · Pandas · Stats · Calculus
- ⏱ 4–6 tuần · 🟢 Beginner
- 💡 Project: Phân tích giá nhà · Cosine Similarity · Streamlit dashboard

---

### PHẦN 2 → Classical Machine Learning
👉 [Xem chi tiết: PHAN2-Classical-ML.md](./PHAN2-Classical-ML.md)

- Naive Bayes · KNN · Decision Tree · Random Forest · XGBoost · LightGBM · K-Means · Metrics
- ⏱ 4–6 tuần · 🟡 Beginner–Intermediate
- 💡 Project: Phân loại bệnh tim · Customer segmentation · Dự đoán giá Airbnb

---

### PHẦN 3 → Deep Learning Cơ Bản
👉 [Xem chi tiết: PHAN3-Deep-Learning-Co-Ban.md](./PHAN3-Deep-Learning-Co-Ban.md)

- Perceptron · Linear Regression (NN) · Logistic · MLP · Backprop · CNN · Transfer Learning
- ⏱ 4–6 tuần · 🟠 Intermediate
- 💡 Project: MNIST CNN · CIFAR-10 · Titanic MLP · House Price NN

---

### PHẦN 4 → Deep Learning Nâng Cao
👉 [Xem chi tiết: PHAN4-Deep-Learning-Nang-Cao.md](./PHAN4-Deep-Learning-Nang-Cao.md)

- RNN/LSTM · Transformer · NLP · Vision Nâng cao · GenAI · LLM · Agent Systems
- ⏱ 6–8 tuần · 🔴 Advanced
- 💡 Project: RAG Chatbot · YOLO custom · Vietnamese NER · Fine-tune SD · Multi-agent

---

### PHẦN 5 → ML Nâng Cao Chuyên Sâu
👉 [Xem chi tiết: PHAN5-ML-Nang-Cao-Production.md](./PHAN5-ML-Nang-Cao-Production.md)

- Time Series · Anomaly Detection · Ensemble Nâng cao · Bayesian · Graph ML · RL · Meta-Learning
- ⏱ 5–7 tuần · 🔴 Advanced
- 💡 Project: Stock Forecaster · Fraud Detector · Stacking Ensemble · GNN Social · RL Trading · AutoML

---

## ✅ CHECKLIST HOÀN THÀNH

```
□ PHẦN 1 ── Python & Math Foundations
□ PHẦN 2 ── Classical Machine Learning  
□ PHẦN 3 ── Deep Learning Cơ Bản
□ PHẦN 4 ── Deep Learning Nâng Cao
□ PHẦN 5 ── ML Nâng Cao Chuyên Sâu
□ Portfolio ── Tối thiểu 10 project (2/pần) trên GitHub
□ Viết blog/copy mỗi tuần
□ Tham gia 2 Kaggle competition
□ Deploy được 1 model lên cloud
```

---

> *Lộ trình tham khảo từ AIO2025 (AI Vietnam — aivietnam.edu.vn), rút gọn & bổ sung cho người mới bắt đầu tập trung vào ứng dụng.*

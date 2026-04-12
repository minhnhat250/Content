# LAB 1 — Train Model Nhận Diện Chữ Số Viết Tay (MNIST)
## "Từ Không Biết Gì → Model Chạy Trong 20 Phút"

**Mục tiêu:** Tự tay train model ML để nhận diện chữ số (0–9) viết tay
**Thời gian:** 20–30 phút
**Công cụ:** Google Colab (miễn phí, không cần cài đặt)
**Level:** Beginner — không cần biết Python trước

---

## Mục Tiêu Lab

```
Sau lab này, bạn sẽ:
✅ Hiểu ML hoạt động như thế nào (qua demo thực tế)
✅ Train model đầu tiên (không cần biết code)
✅ Biết đọc kết quả accuracy — model có TỐT không?
✅ Hiểu concept "training" — máy học bằng cách nào
```

---

## Prerequisites

- [ ] Google Account (để dùng Colab)
- [ ] Mở link Colab: [https://colab.research.google.com](https://colab.research.google.com)
- [ ] Điện thoại/laptop — 20 phút rảnh

---

## Step-by-Step Guide

### Step 1: Mở Notebook MNIST (2 phút)

**Truy cập link bên dưới → Duplicate → Save to Drive:**

**Link Colab:** `https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb`

Hoặc copy-paste code trong Step 2 trực tiếp vào Colab mới.

---

### Step 2: Import Thư Viện (3 phút)

Copy đoạn code dưới → Paste vào Colab → Nhấn **Shift+Enter**:

```python
# ============================================
# LAB 1: MNIST - Nhận diện chữ số viết tay
# Thời gian: 20-30 phút
# ====================================

# Import thư viện
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print("✅ Import thành công!")
print(f"TensorFlow version: {tf.__version__}")
```

✅ **Checkpoint:** Nếu thấy "Import thành công!" → Đúng. Tiếp tục.

---

### Step 3: Load Dữ Liệu MNIST (3 phút)

```python
# Load dataset MNIST — 70,000 ảnh chữ số viết tay
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(f"Training data: {x_train.shape}")
print(f"Test data: {x_test.shape}")
print(f"Labels: {np.unique(y_train)}")
```

**Output mong đợi:**

```
Training data: (60000, 28, 28)
Test data: (10000, 28, 28)
Labels: [0 1 2 3 4 5 6 7 8 9]
```

> **Giải thích:**
> - 60,000 ảnh training (học), 10,000 ảnh test (đánh giá)
> - Mỗi ảnh 28×28 pixels (nhỏ, đen trắng)
> - Labels 0–9 = 10 loại chữ số

✅ **Checkpoint:** Thấy shape + labels → Đúng. Tiếp tục.

---

### Step 4: Xem Ảnh Mẫu (3 phút)

```python
# Hiển thị 6 ảnh đầu tiên
plt.figure(figsize=(10, 4))
for i in range(6):
    plt.subplot(1, 6, i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.suptitle("Mẫu chữ số viết tay từ MNIST dataset")
plt.show()

print("Bạn thấy gì? Mỗi ảnh là một chữ số viết tay (0-9)")
```

✅ **Checkpoint:** Thấy 6 ảnh chữ số hiển thị → Đúng. Model sẽ học nhận diện những ảnh này.

---

### Step 5: Build Model — "Bộ não" Neural Network (5 phút)

```python
# Build model — "bộ não" để nhận diện chữ số
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),      # Ảnh 28x28 → vector 784
    keras.layers.Dense(128, activation='relu'),         # Layer 1: 128 neurons
    keras.layers.Dense(64, activation='relu'),          # Layer 2: 64 neurons
    keras.layers.Dense(10, activation='softmax')        # Output: 10 chữ số (0-9)
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()
```

**Output mong đợi:**

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 flatten (Flatten)          (None, 784)              0
 dense (Dense)               (None, 128)              100480
 dense_1 (Dense)            (None, 64)               8256
 dense_2 (Dense)            (None, 10)               650
=================================================================
Total params: ~109,000
```

> **Giải thích:**
> - **Flatten:** Ảnh 2D (28×28) → vector 1D (784)
> - **Dense Layer 1:** 128 "neuron" — học đặc trưng cơ bản
> - **Dense Layer 2:** 64 "neuron" — học đặc trưng phức tạp hơn
> - **Output Layer:** 10 neurons — xác suất cho mỗi chữ số (0–9)

✅ **Checkpoint:** Thấy model summary → Đúng. Tiếp tục.

---

### Step 6: Train Model — "Dạy" máy nhận diện (5–10 phút)

```python
# Train model — cho máy HỌC từ 60,000 ảnh
print("Bắt đầu train... Đợi 1-2 phút ⏳")

history = model.fit(
    x_train, y_train,
    epochs=5,               # Số lần duyệt qua toàn bộ data
    batch_size=32,         # Mỗi lần học 32 ảnh
    validation_split=0.1,   # Dùng 10% data để validate
    verbose=1
)

print("✅ Train hoàn tất!")
```

**Output mong đợi:**

```
Epoch 1/5
1688/1688 ━━━━━━━━━━━━━━━━━━━  5s  3ms/step - loss: 0.300 - accuracy: 0.910
Epoch 2/5
1688/1688 ━━━━━━━━━━━━━━━━━━━  4s  2ms/step - loss: 0.085 - accuracy: 0.975
...
```

> **Giải thích:**
> - **Epoch:** Một lần duyệt qua toàn bộ 60,000 ảnh
> - **Loss giảm dần:** Model càng ngày càng ít sai
> - **Accuracy tăng dần:** Model nhận diện chính xác hơn

✅ **Checkpoint:** Accuracy > 90% sau 5 epochs → Đúng. Model đã "học" được.

---

### Step 7: Đánh Giá Model (3 phút)

```python
# Đánh giá model trên test data (10,000 ảnh MỚI)
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print(f"\n🎯 KẾT QUẢ TRÊN TEST DATA:")
print(f"   Accuracy: {test_acc:.2%}")
print(f"   Loss: {test_loss:.4f}")
```

**Output mong đợi:**

```
🎯 KẾT QUẢ TRÊN TEST DATA:
   Accuracy: 97-98%
   Loss: 0.08-0.12
```

> **Giải thích:**
> - **Accuracy 97–98%:** Model nhận diện ĐÚNG 97–98/100 ảnh test mới.
> - **Loss thấp:** Model sai ít.
> - **ĐÂY LÀ KHÁ TỐT** cho beginner model.

✅ **Checkpoint:** Accuracy > 95% → Model hoạt động tốt!

---

### Step 8: Dự Đoán Thử (3 phút)

```python
# Test: Cho model dự đoán 5 ảnh test
predictions = model.predict(x_test[:5])

# Show kết quả
plt.figure(figsize=(12, 3))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(x_test[i], cmap='gray')

    predicted = np.argmax(predictions[i])
    actual = y_test[i]
    color = 'green' if predicted == actual else 'red'

    plt.title(f"Pred: {predicted}\nActual: {actual}", color=color)
    plt.axis('off')
plt.suptitle("Model predictions vs Actual (Green=Correct, Red=Wrong)")
plt.show()
```

**Output mong đợi:**

- 4–5/5 ảnh có màu xanh (đúng)
- 0–1 ảnh có màu đỏ (sai — acceptable)

✅ **Checkpoint:** Model dự đoán được chữ số mới → BẠN ĐÃ TRAIN MODEL ĐẦU TIÊN THÀNH CÔNG!

---

## Kết Quả Bạn Có Được

```
✅ Model nhận diện chữ số viết tay
✅ Accuracy: 95-98%
✅ Code hoàn chỉnh chạy trên Google Colab
✅ Hiểu: Data → Model → Train → Predict
```

**Để chia sẻ model:**

1. File → Download → Download .ipynb
2. Upload lên GitHub

---

## Challenges Thêm

**Challenge 1: Tăng Accuracy**

```python
# Thử thêm epochs hoặc layers
# epochs=10 thay vì 5 → Accuracy cao hơn
```

**Challenge 2: Xem Training History**

```python
# Vẽ đồ thị loss/accuracy qua các epochs
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.legend()
plt.show()
```

**Challenge 3: Thử Dataset Khác**
> Tìm dataset CIFAR-10 (10 loại ảnh: airplane, car, bird...) → Train tương tự.

---

## Bài Tập Về Nhà

1. **Chạy lại lab** với `epochs=10` → xem accuracy tăng bao nhiêu?
2. **Research:** Model MNIST này dùng kiến trúc gì? (Dense layers)
3. **Thử thách:** Thay `optimizer='adam'` bằng `optimizer='sgd'` → Kết quả thế nào?

---

## Những Điều Bạn Đã Học

| Concept | Demo |
|---|---|
| Dataset = 60K ảnh train | `MNIST.load_data()` |
| Model = Neural Network | `keras.Sequential()` |
| Train = Học từ data | `model.fit()` |
| Predict = Dự đoán mới | `model.predict()` |
| Accuracy = Độ chính xác | `model.evaluate()` |

---

## Link Hữu Ích

| Resource | Link |
|---|---|
| Google Colab | [colab.research.google.com](https://colab.research.google.com) |
| MNIST Dataset | [keras.io/api/datasets/mnist](https://keras.io/api/datasets/mnist/) |
| TensorFlow Tutorial | [tensorflow.org/tutorials](https://www.tensorflow.org/tutorials) |
| Kaggle MNIST Competition | [kaggle.com/c/digit-recognizer](https://www.kaggle.com/c/digit-recognizer) |

---

Tiếp theo: [LAB 2: AI Agent Hands-on](./lab-2-agent-demo.md)
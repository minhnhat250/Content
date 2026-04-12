# PHẦN 3 — DEEP LEARNING CƠ BẢN

> **Mục tiêu:** Hiểu Neural Network từ trong ra ngoài — Linear, Logistic, MLP, CNN
> **Thời gian:** 4–6 tuần · **Cấp độ:** 🟠 Intermediate

---

## 3.1 — Perceptron & Neural Network Cơ Bản

### Mục đích
Neural Network = mô phỏng cách não bộ hoạt động (cực kỳ simplified). Perceptron = neuron nhân tạo đơn giản nhất. Hiểu Perceptron → hiểu mọi Neural Network phức tạp hơn. Activation functions = cách neuron quyết định "bắn" hay không.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Perceptron — neuron nhân tạo đầu tiên** | [Scaler — Perceptron](https://www.scaler.com/topics/deep-learning/what-is-a-perceptron/) | Perceptron = đơn vị nhỏ nhất của Neural Network. Input x₁, x₂... → weighted sum: z = w₁x₁ + w₂x₂ + b → activation function → output. Frank Rosenblatt 1957. Nếu activation = step function: output = 1 nếu z > 0, else 0. Perceptron có thể học (adjust weights) bằng rule: w = w + η × (y - ŷ) × x. Perceptron chỉ học được linearly separable problems (AND, OR nhưng NOT XOR) |
| **Activation Functions — Sigmoid, ReLU, Tanh** | [Scaler — Activation](https://www.scaler.com/topics/deep-learning/activation-functions-in-deep-learning/) | Activation = nonlinear function sau weighted sum. Không có activation → neural network = linear regression (dù bao nhiêu layers). Sigmoid: σ(z) = 1/(1+e⁻ᶻ) → output 0-1, dùng output layer binary classification. Tanh: tanh(z) = (eᶻ-e⁻ᶻ)/(eᶻ+e⁻ᶻ) → output -1 to 1, zero-centered. ReLU: max(0, z) → output 0 nếu âm, z nếu dương. **ReLU là activation phổ biến nhất trong hidden layers** — đơn giản, fast, không có vanishing gradient cho positive values. Leaky ReLU: max(0.01z, z) → fix "dying ReLU" |
| **Feedforward Neural Network** | [Scaler — Feedforward](https://www.scaler.com/topics/deep-learning/feedforward-neural-networks/) | Signal truyền từ input → hidden layers → output. Không có feedback connections (không có cycle). Layer 1 (input) → Layer 2 (hidden) → Layer 3 (output). Mỗi layer có nhiều neurons. Output của layer i = input của layer i+1. Feedforward = basic architecture. RNN, Transformer = variations |
| **Weights & Biases — ý nghĩa** | [Scaler — Weights](https://www.scaler.com/topics/deep-learning/weights-and-biases-in-deep-learning/) | Weight (w) = độ quan trọng của mỗi input. Weight lớn → input đó influence mạnh. Weight nhỏ → ít ảnh hưởng. Bias (b) = điều chỉnh activation threshold. Không có bias → neuron chỉ activate khi weighted sum = 0. Train = điều chỉnh weights/biases để output gần target. Initial weights: random nhỏ (Gaussian, Xavier, He initialization). Nếu weights quá lớn → gradient explosion. Quá nhỏ → gradient vanishing |
| **PyTorch: Tensor cơ bản** | [PyTorch — Tensor](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) | Tensor = generalization của matrix (1D vector, 2D matrix, 3D+, nD). `torch.tensor([1,2,3])` tạo tensor. `torch.randn(3,4)` tensor ngẫu nhiên 3×4. `tensor.shape`, `tensor.dtype`, `tensor.device`. `tensor.cpu()`, `tensor.cuda()` chuyển CPU↔GPU. NumPy ↔ Tensor: `torch.from_numpy(arr)`, `tensor.numpy()`. GPU training: model + data phải cùng device |
| **PyTorch: autograd — tự tính gradient** | [PyTorch — Autograd](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html) | Autograd = PyTorch tự động tính derivatives. `requires_grad=True` → tensor tracking operations. `loss.backward()` → tính gradients cho toàn bộ parameters. `optimizer.step()` → cập nhật weights. Backward computation = reversed topological order của computation graph. Cách PyTorch train neural networks: forward pass → compute loss → backward pass → update weights |
| **PyTorch: nn.Module — tạo layer** | [PyTorch — nn.Module](https://www.scaler.com/topics/deep-learning/what-is-mlp-in-deep-learning/) | `nn.Module` = base class cho mọi neural network trong PyTorch. Override `__init__` (define layers) + `forward` (define forward pass). Ví dụ: `self.linear = nn.Linear(10, 5)` → fully connected layer (10 inputs → 5 outputs). `self.relu = nn.ReLU()` → activation. Sequential: `nn.Sequential(nn.Linear(10,5), nn.ReLU(), nn.Linear(5,2))` — cách nhanh build network |

---

## 3.2 — Linear Regression (Neural Network)

### Mục đích
Linear Regression = neural network đơn giản nhất (1 layer, 1 neuron, no activation). Dùng LR để hiểu toàn bộ ML workflow: forward → loss → backward → update. Từ đó mở rộng lên neural network phức tạp hơn.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Linear Regression — từ góc nhìn Neural Network** | [Scaler — LR PyTorch](https://www.scaler.com/topics/deep-learning/linear-regression-using-pytorch/) | Neural network: 1 neuron, 1 output, no activation = Linear Regression. Forward: ŷ = X @ w + b. Loss: MSE = mean((ŷ - y)²). Backward: compute ∂L/∂w, ∂L/∂b (PyTorch tự làm). Update: w = w - lr × ∂L/∂w. Gradient Descent = epochs × update. Code PyTorch: `nn.Linear(in_features, out_features)` → `nn.MSELoss()` → training loop |
| **Loss Function — MSE** | [Scaler — Loss Functions](https://www.scaler.com/topics/deep-learning/loss-functions-in-deep-learning/) | Loss = "model tệ đến mức nào" — số càng nhỏ → model càng tốt. MSE (Mean Squared Error): trung bình bình phương sai số. Ưu: differentiable everywhere, penalizes large errors nặng. Nhược: sensitive to outliers (vì bình phương). MAE (L1): less sensitive to outliers. Huber: kết hợp MSE + MAE. BCE (Binary Cross Entropy): cho binary classification. CE (Cross Entropy): cho multi-class |
| **Gradient Descent — cách mạng ML** | [Scaler — Gradient Descent](https://www.scaler.com/topics/calculus/gradient-descent/) | Gradient Descent = tìm minimum của loss function. Gradient = vector của partial derivatives ∂L/∂w. Update rule: w = w - lr × ∇L(w). lr = learning rate = step size. lr quá lớn → overshoot, không hội tụ. lr quá nhỏ → hội tụ quá chậm. Gradient trỏ lên → đi xuống (negative direction) → tìm minimum. Nhiều local minima trong deep networks → initialization important |
| **Learning Rate — tại sao quan trọng** | [Scaler — LR](https://www.scaler.com/topics/deep-learning/learning-rate-in-deep-learning/) | Learning rate = hyperparameter quan trọng nhất. Default LR tốt: 1e-3. LR schedule: giảm LR theo thời gian (step decay, cosine annealing). Adaptive optimizers (Adam) tự điều chỉnh LR per parameter. Warmup: bắt đầu lr nhỏ → tăng dần → giảm. Visualize loss curve: không giảm → LR quá nhỏ. Dao động violent → LR quá lớn |
| **SGD vs Mini-batch vs Batch Gradient Descent** | [Scaler — Batch SGD](https://www.scaler.com/topics/deep-learning/types-of-gradient-descent/) | Batch GD: tính gradient trên ALL samples → update 1 lần/epoch. Chính xác nhưng cực chậm khi data lớn (1M rows). SGD: tính gradient trên 1 sample → update N lần/epoch. Nhanh nhưng noisy → dao động nhiều. **Mini-batch SGD = TRADE-OFF TỐT NHẤT**: batch_size = 32-256. Đủ lớn để gradient stable, đủ nhỏ để noisy (giúp escape local minima). Batch size 32 hoặc 64 là default phổ biến |
| **Thực hành: dự đoán giá nhà bằng PyTorch** | [Scaler — LR Project](https://www.scaler.com/topics/deep-learning/linear-regression-using-pytorch/) | Task: dự đoán giá nhà từ features (area, bedrooms, bathrooms, age). Code: (1) Load data → normalize (StandardScaler). (2) Define model: `nn.Linear(4, 1)`. (3) Loss: MSELoss. (4) Optimizer: SGD(lr=0.01). (5) Training loop 100 epochs. (6) Plot loss curve. (7) Predict on test set → calculate RMSE |

---

## 3.3 — Logistic Regression & Softmax (Classification)

### Mục đích
Classification khác Regression: output = class label (discrete) thay vì continuous value. Logistic Regression = Linear Regression + Sigmoid → output = probability (0-1). Softmax = mở rộng Logistic cho multi-class (nhiều classes).

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Logistic Regression — sigmoid function** | [Scaler — Logistic](https://www.scaler.com/topics/deep-learning/logistic-regression-in-pytorch/) | Linear regression output: -∞ → +∞. Sigmoid: σ(z) = 1/(1+e⁻ᶻ) → compress vào 0-1. Interpretation: probability of class 1. Decision boundary: if σ(z) > 0.5 → predict 1. Loss: Binary Cross Entropy (BCE) = -[y × log(ŷ) + (1-y) × log(1-ŷ)]. BCE được derive từ Maximum Likelihood Estimation (MLE). Log transform giúp gradient stable |
| **Binary Cross Entropy (BCE) Loss** | [Scaler — Cross Entropy](https://www.scaler.com/topics/deep-learning/cross-entropy-loss-function/) | BCE = -Σ [y_i × log(σ(z_i)) + (1-y_i) × log(1-σ(z_i))]. Khi y=1: BCE = -log(ŷ) → ŷ nhỏ → loss lớn. Khi y=0: BCE = -log(1-ŷ) → ŷ lớn → loss lớn. BCE được dùng cho mọi binary classification (spam, fraud, churn). **Không bao giờ dùng MSE cho classification** — gradient saturation, slow convergence |
| **Softmax — cho multi-class** | [Scaler — Softmax](https://www.scaler.com/topics/deep-learning/softmax-regression/) | Multi-class (K classes): softmax = [eᶻ¹/Σeᶻ, eᶻ²/Σeᶻ, ..., eᶻᵏ/Σeᶻ]. Output = probability distribution (sums to 1). Cross Entropy Loss với softmax = standard loss cho multi-class classification. Temperature trong softmax: cao → probabilities uniform (more random), thấp → peaked (more confident). Temperature = 1 → standard softmax |
| **One-vs-All (OvA) Classification** | [Scaler — One vs All](https://www.scaler.com/topics/deep-learning/one-vs-all-classification/) | Khi model chỉ hỗ trợ binary (logistic) nhưng có K classes: train K binary classifiers. Classifier i: class i vs not-i. Prediction: chọn class có highest probability. Phương pháp đơn giản nhưng không tối ưu khi classes overlap. Softmax / multi-class output layer xử lý trực tiếp K classes (tốt hơn OvA) |
| **Thực hành: Titanic Survival Prediction** | [Kaggle Titanic](https://www.kaggle.com/competitions/titanic) | Binary classification: survived (1) vs died (0). Features: Pclass, Sex, Age, SibSp, Parch, Fare, Embarked. Pipeline: load → clean missing values (Age: median, Embarked: mode) → encode categorical (Sex: 0/1, Embarked: one-hot) → split train/test → Logistic Regression (sklearn). Baseline accuracy ~78%. Feature engineering: "Title" extracted from Name, "FamilySize" = SibSp + Parch |
| **Thực hành: MNIST digit classification** | [PyTorch — MNIST](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) | MNIST: 70K images × 28×28 pixels = 784 features. 10 classes (0-9). Code: (1) Load MNIST via `torchvision.datasets.MNIST`. (2) DataLoader (batch_size=64). (3) Simple model: nn.Linear(784, 10) + CrossEntropyLoss. (4) Train 5 epochs. (5) Test accuracy ~92% với linear model (đơn giản). Với MLP/CNN → >98% |

---

## 3.4 — Multi-Layer Perceptron (MLP)

### Mục đích
MLP = nhiều hidden layers giữa input và output. Hidden layers cho phép học nonlinear patterns mà 1 neuron không học được. MLP = kiến trúc cơ bản, tất cả architectures phức tạp hơn (CNN, RNN, Transformer) đều build trên MLP.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **MLP — tại sao cần nhiều layer** | [Scaler — MLP](https://www.scaler.com/topics/deep-learning/what-is-mlp-in-deep-learning/) | 1 hidden layer với đủ neurons có thể approximate BẤT KỲ continuous function nào (Universal Approximation Theorem). NHƯNG cần rất nhiều neurons → inefficient. Nhiều layers (deep) = hierarchical representations: Layer 1 học edges → Layer 2 học shapes → Layer 3 học objects. Shallow (1 layer) vs Deep (many layers): deep cần fewer total neurons để represent cùng function → efficient hơn. Đây là lý do gọi "Deep" Learning |
| **Forward Pass & Backward Pass** | [Scaler — Forward Pass](https://www.scaler.com/topics/deep-learning/forward-pass-in-deep-learning/) | Forward pass: input → Layer1 → activation → Layer2 → ... → output. Tính prediction và loss. Backward pass: loss → LayerN ← ... ← Layer2 ← Layer1 ← compute gradients. Trong backward: chain rule được áp dụng: ∂L/∂w₁ = ∂L/∂ŷ × ∂ŷ/∂a × ∂a/∂w₁. PyTorch autograd tự tính tất cả gradients dựa trên computation graph |
| **Backpropagation — chain rule trong thực tế** | [Scaler — Backprop](https://www.scaler.com/topics/deep-learning/backpropagation/) | Backpropagation = chain rule được áp dụng systematic qua mỗi layer. Step: tính gradient w.r.t. loss → chain qua từng layer. ∂L/∂w_L = ∂L/∂a_L × ∂a_L/∂z_L × ∂z_L/∂w_L (w_L = weights layer cuối). ∂L/∂w_{L-1} = ∂L/∂a_L × ∂a_L/∂z_L × ∂z_L/∂a_{L-1} × ∂a_{L-1}/∂z_{L-1} × ∂z_{L-1}/∂w_{L-1}. Công thức dài nhưng PyTorch tự tính — developer chỉ cần hiểu concept |
| **Vanishing Gradient — vấn đề lớn** | [Scaler — Vanishing](https://www.scaler.com/topics/deep-learning/vanishing-gradient-problem/) | Khi layers sâu, gradient truyền ngược nhỏ dần → weights ở layers đầu几乎 không update → early layers gần như random → model không học được. Nguyên nhân chính: sigmoid/tanh có derivative ≤ 1. Nhiều layers × derivative ≤ 1 → gradient giảm exponential. **Giải pháp: ReLU activation** (derivative = 1 cho z > 0, 0 cho z < 0) → gradient không vanishing. Cách khác: BatchNorm, residual connections (ResNet) |
| **Weight Initialization — Xavier, He** | [Scaler — Init](https://www.scaler.com/topics/deep-learning/weight-initialization-in-deep-learning/) | Initial weights quá lớn → gradient explosion (NaN). Quá nhỏ → gradient vanishing. Xavier/Glorot: `w ~ N(0, sqrt(2/(fan_in + fan_out)))` — tốt cho sigmoid/tanh. He initialization: `w ~ N(0, sqrt(2/fan_in))` — tốt cho ReLU. PyTorch default: `nn.init.kaiming_normal_` (He) cho ReLU, `xavier_uniform_` cho others. Sử dụng đúng initialization giúp training ổn định hơn |
| **PyTorch: nn.Sequential — tạo MLP nhanh** | [PyTorch — Sequential](https://pytorch.org/docs/stable/generated/torch.nn.Sequential.html) | Cách nhanh build MLP: `model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(), nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, 10))`. Đơn giản nhưng không flexible. Cách tốt hơn (class): `class MLP(nn.Module): def __init__(self): super().__init__(); self.net = nn.Sequential(...)`. Đặt tên layers để access riêng: `self.fc1 = nn.Linear(...)` |
| **Dropout — tránh overfitting** | [Scaler — Dropout](https://www.scaler.com/topics/deep-learning/dropout-regularization/) | Dropout: trong training, random bỏ (set = 0) một phần neurons mỗi iteration. Ví dụ: dropout=0.5 → 50% neurons bị tắt. Mỗi iteration "thấy" different network → ensemble effect. Test: tắt dropout (use all neurons). Dropout rate: 0.2-0.5 là common range. Too high → underfitting. Too low → không đủ regularization. PyTorch: `nn.Dropout(p=0.5)` |
| **Batch Normalization** | [Scaler — BatchNorm](https://www.scaler.com/topics/deep-learning/batch-normalization-in-deep-learning/) | BatchNorm: normalize layer inputs to have mean=0, std=1 within each batch. Params: γ (scale) và β (shift) — learnable. Ổn định gradient → cho phép higher learning rate → train nhanh hơn. Regularization effect (less dropout needed). BatchNorm: normalize before activation (thường). Moving average of batch statistics used at test time. Batch size nhỏ → BatchNorm unstable. PyTorch: `nn.BatchNorm1d(num_features)` |
| **Thực hành: MLP cho MNIST** | [PyTorch — MNIST MLP](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) | MLP architecture: 784 → 512 → 256 → 10. ReLU activations. Dropout(0.2). BatchNorm after each hidden layer. Adam optimizer (lr=1e-3). Train 10 epochs → test accuracy ~98%. Features: normalize pixels [0,1]. DataLoader shuffle=True. Evaluate: accuracy = (pred == labels).sum() / len(labels). Plot training/validation loss |

---

## 3.5 — Optimizers & Huấn Luyện Neural Network

### Mục đích
Optimizer = thuật toán cập nhật weights dựa trên gradients. SGD = cơ bản nhất. Adam = mạnh nhất phổ biến. Biết cách optimizer hoạt động giúp debug training issues (loss not decreasing, oscillating).

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **SGD vs Adam vs RMSprop** | [Scaler — Optimizers](https://www.scaler.com/topics/deep-learning/optimizers-in-deep-learning/) | SGD: w = w - lr × ∇L. Simple nhưng noisy → slow convergence, sensitive to lr. SGD with momentum: thêm momentum (giữ previous update direction) → smooth convergence. RMSprop: adaptive lr per parameter — chia lr bởi running average of squared gradients → large gradient → smaller effective lr. Adam = RMSprop + momentum: lr per parameter + momentum = best of both worlds. **Adam (lr=1e-3) là default optimizer cho hầu hết deep learning projects** |
| **Adam Optimizer — tại sao phổ biến** | [Scaler — Adam](https://www.scaler.com/topics/deep-learning/adam-optimizer/) | Adam = Adaptive Moment Estimation. Maintains: m = momentum (first moment), v = RMSprop (second moment). m = β₁ × m + (1-β₁) × g. v = β₂ × v + (1-β₂) × g². Bias correction: m̂ = m/(1-β₁ᵗ), v̂ = v/(1-β₂ᵗ). Update: w = w - lr × m̂/(√v̂ + ε). Default params: lr=1e-3, β₁=0.9, β₂=0.999, ε=1e-8. Hoạt động tốt cho几乎 mọi architecture |
| **Learning Rate Scheduling** | [Scaler — LR Sched](https://www.scaler.com/topics/deep-learning/learning-rate-schedulers/) | LR schedule = thay đổi LR theo thời gian. Step decay: lr = lr × 0.1 every N epochs. Cosine annealing: lr giảm theo cosine curve. Warmup: start lr nhỏ → tăng dần → giảm. OneCycleLR: warmup → max lr → anneal. ReduceLROnPlateau: giảm lr khi metric ngừng cải thiện. Scheduler: `torch.optim.lr_scheduler.CosineAnnealingLR` |
| **Overfitting vs Underfitting** | [Scaler — Overfit](https://www.scaler.com/topics/deep-learning/overfitting-and-underfitting-in-deep-learning/) | Overfitting: train loss thấp, test loss cao → model memorize training data, không generalize. Signs: train acc 99%, test acc 70%. Solutions: more data, dropout, weight decay (L2), data augmentation, early stopping, reduce model size. Underfitting: cả train và test loss đều cao → model không đủ capacity. Solutions: bigger model, more features, train longer, lower regularization |
| **Regularization — L1, L2** | [Scaler — Regularization](https://www.scaler.com/topics/deep-learning/regularization-in-deep-learning/) | L2 regularization (weight decay): thêm λ × Σw² vào loss. Khuyến khích weights nhỏ → less complex model → less overfit. PyTorch: `weight_decay=0.01` in optimizer. L1 regularization: thêm λ × Σ|w| → encourages sparsity (many weights = 0) → feature selection. Elastic net = L1 + L2. Dropout là regularization hiệu quả hơn L2 cho deep networks |
| **Early Stopping** | [Scaler — Early Stop](https://www.scaler.com/topics/deep-learning/early-stopping-in-deep-learning/) | Monitor validation loss. Nếu val loss không cải thiện trong N epochs (patience) → dừng training, restore weights from best epoch. Tránh overfitting tự động. PyTorch: manual implementation hoặc `pytorchtools` library. Patience = 5-10 epochs thường OK |
| **ModelCheckpoint — lưu model tốt nhất** | [PyTorch — Save/Load](https://pytorch.org/tutorials/beginner/saving_loading_models.html) | Lưu toàn bộ model: `torch.save(model, 'model.pt')`. Lưu state_dict (RECOMMENDED): `torch.save(model.state_dict(), 'weights.pt')`. Load: `model.load_state_dict(torch.load('weights.pt'))`. Lưu checkpoint (optimizer, epoch, best_loss): `torch.save({'epoch': e, 'model': model.state_dict(), 'optimizer': optimizer.state_dict()}, 'checkpoint.pt')`. Luôn lưu state_dict, không save cả object |

---

## 3.6 — Convolutional Neural Network (CNN) Cơ Bản

### Mục đích
CNN = kiến trúc chuyên cho ảnh. Fully connected layers xử lý ảnh rất không hiệu quả (784 inputs = fully connected → 784×256 = 200K weights). CNN dùng filters (shared weights) → giảm params драматически, capture spatial patterns tốt hơn.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **CNN — tại sao cần cho ảnh** | [Scaler — CNN](https://www.scaler.com/topics/deep-learning/convolutional-neural-network/) | Ảnh có spatial structure: pixel gần nhau → related. FC layer không hiểu spatial relationships → treat all pixels equally. CNN dùng filters trượt trên ảnh → capture local patterns: edges, textures, shapes. Filter nhỏ (3×3, 5×5) → shared weights → fewer params → less overfitting. Hierarchical: early layers capture low-level (edges) → later layers combine → high-level (object parts) |
| **Convolution Layer — cách hoạt động** | [Scaler — Conv Layer](https://www.scaler.com/topics/deep-learning/convolutional-layer-in-cnn/) | Filter (kernel) = ma trận nhỏ (ví dụ 3×3). Trượt filter trên ảnh (stride = bước nhảy). Tại mỗi vị trí: dot product(filter, patch) → 1 giá trị. Output = feature map. Multiple filters → multiple feature maps. Padding: thêm zeros quanh ảnh → output size = input size (valid padding → smaller). Output size = floor((H - K + 2P) / S) + 1 |
| **Pooling Layer — Max, Avg** | [Scaler — Pooling](https://www.scaler.com/topics/deep-learning/pooling-layers-in-cnn/) | Pooling = giảm spatial resolution (width × height) giữ nguyên channels. MaxPooling (2×2, stride=2): lấy max trong mỗi 2×2 patch → giảm 4× spatial size. AvgPooling: lấy trung bình. MaxPooling giữ features "strongest", phổ biến hơn. Global Average Pooling (GAP): pool toàn bộ feature map → 1 value → dùng thay FC cuối ( ít params hơn) |
| **Feature Maps — output của convolution** | [Scaler — Feature Maps](https://www.scaler.com/topics/deep-learning/feature-maps-in-cnn/) | Feature map = output của 1 filter tại tất cả vị trí trên ảnh. Mỗi feature map highlight 1 type of feature (vertical edges, horizontal edges, textures...). Nhiều filters → nhiều feature maps → capture nhiều patterns. Conv layer sau → kết hợp features từ layer trước → increasingly abstract. Visualization: dùng hooks trong PyTorch để visualize feature maps |
| **PyTorch: nn.Conv2d, nn.MaxPool2d** | [PyTorch — Conv2d](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) | `nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0)`. in_channels=3 (RGB), 1 (grayscale). out_channels=32 (số filters). kernel_size=3 (3×3) hoặc (3,5). `nn.MaxPool2d(2)` = 2×2 max pooling stride 2. Input shape cho Conv2d: (batch, channels, height, width) = (N, C, H, W) |
| **PyTorch: torchvision transforms** | [PyTorch — Transforms](https://pytorch.org/docs/stable/torchvision/transforms.html) | Transform = tiền xử lý ảnh. `transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])`. ToTensor: PIL Image → (0,255) → (0,1). Normalize: (0,1) → (-1,1) bằng mean và std. Data augmentation: RandomCrop, RandomFlip, ColorJitter, RandomRotation → tăng data diversity → less overfit. Augmentation chỉ áp dụng training, không validation/test |
| **Thực hành: CNN cho CIFAR-10** | [PyTorch — CIFAR10](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html) | CIFAR-10: 60K 32×32 images × 10 classes (airplane, car, bird, cat, deer, dog, frog, horse, ship, truck). Architecture: Conv(3,32) → ReLU → MaxPool → Conv(32,64) → ReLU → MaxPool → Conv(64,64) → ReLU → FC(64,10). Train 10 epochs → ~70% accuracy. Với data augmentation + deeper network → 90%+. Transfer learning từ ResNet → >95% |
| **Transfer Learning — dùng pretrained model** | [Scaler — Transfer](https://www.scaler.com/topics/deep-learning/transfer-learning-in-deep-learning/) | Thay vì train từ scratch (random weights), dùng pretrained weights từ ImageNet (1.2M images, 1000 classes). Phổ biến pretrained models: ResNet-50, VGG-16, EfficientNet-B0. Feature Extraction: freeze backbone → train only classifier head. Fine-tuning: unfreeze last few layers → train với lr nhỏ. Khi dataset nhỏ (< 10K) và similar to ImageNet → transfer learning gần như BẮT BUỘC |

---

## 3.7 — Recurrent Neural Network (RNN) Cơ Bản

### Mục đích
RNN = kiến trúc cho sequential data (chuỗi: text, time series, audio). FC và CNN không có memory — không hiểu "thứ tự" của input. RNN có hidden state được cập nhật qua mỗi timestep → có "memory" về previous inputs.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **RNN — tại sao cần cho chuỗi** | [Scaler — RNN](https://www.scaler.com/topics/deep-learning/recurrent-neural-network/) | FC: input → output, không có memory. RNN: tại timestep t, hidden state h_t = f(W_xh × x_t + W_hh × h_{t-1} + b). h_{t-1} = hidden state từ timestep trước → "nhớ" previous context. Unfold RNN: same weights W shared across all timesteps → parameters efficient. Ví dụ: predict next word "The cat sat on the ___": RNN nhớ "cat" (singular) → predict "mat" |
| **Vanishing Gradient trong RNN** | [Scaler — RNN Vanish](https://www.scaler.com/topics/deep-learning/vanishing-gradient-problem-in-rnn/) | Khi unrolling many timesteps, gradient truyền ngược qua many recursions → gradient giảm exponential → early timesteps almost no gradient update → RNN "forgets" early context. Long sequences → context from beginning bị mất. Đây là fundamental limitation của vanilla RNN. **Giải pháp: LSTM và GRU** — architectures với gating mechanisms |
| **LSTM — Long Short-Term Memory** | [Scaler — LSTM](https://www.scaler.com/topics/deep-learning/long-short-term-memory-lstm/) | LSTM = RNN với gating. 3 gates: Input gate (nhập bao nhiêu new info), Forget gate (bỏ bao nhiêu old memory), Output gate (xuất bao nhiêu memory). Cell state c_t = long-term memory được carefully modified. Gating mechanisms = learnable → model tự quyết định khi nào remember, khi nào forget. LSTM có thể handle sequences 1000+ timesteps |
| **GRU — Gated Recurrent Unit** | [Scaler — GRU](https://www.scaler.com/topics/deep-learning/gated-recurrent-unit-gru/) | GRU = simplified LSTM (2 gates instead of 3). Update gate = input + forget gate combined. Reset gate = quyết định nhìn previous context nhiều hay ít. GRU fewer params → faster training → thường comparable or better than LSTM. Cuối cùng: Transformer đã thay thế LSTM cho hầu hết seq2seq tasks (better parallelization, handles long sequences better) |
| **Sequence-to-Sequence (Seq2Seq)** | [Scaler — Seq2Seq](https://www.scaler.com/topics/deep-learning/sequence-to-sequence-models/) | Encoder (RNN/LSTM) encode input sequence → context vector (final hidden state). Decoder (RNN/LSTM) decode từ context → output sequence. Ứng dụng: machine translation, chatbot, text summarization. Bottleneck: entire information phải fit vào 1 context vector → information bottleneck. **Attention mechanism giải quyết bottleneck này** |
| **PyTorch: nn.LSTM, nn.GRU** | [PyTorch — LSTM](https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html) | `nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)`. Input: (batch, seq_len, input_size). Output: (batch, seq_len, hidden_size) + (h_n, c_n). `nn.GRU(input_size, hidden_size, num_layers)`. Bidirectional: `bidirectional=True` → hidden_size × 2. Output: forward + backward hidden states concatenated |

---

## 3.8 — Project Thực Hành PHẦN 3

| # | Project | Mô tả chi tiết | Dataset | Cấp |
|---|---|---|---|:---:|
| **A** | MNIST Digit Recognition — MLP vs CNN | Compare MLP (784→512→10) vs CNN (Conv layers). Visualize feature maps. Tăng accuracy với data augmentation. Deploy lên web bằng Streamlit | PyTorch MNIST có sẵn | 🟡 |
| **B** | CIFAR-10 Image Classification | Train CNN from scratch → accuracy ~70%. Áp dụng Transfer Learning (ResNet-18 pretrained) → accuracy >90%. Fine-tune last layers. Data augmentation: random flip, crop, color jitter | [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) | 🟠 |
| **C** | Titanic Survival — MLP vs Logistic Regression | So sánh Logistic Regression (baseline) vs MLP. Xem deep network có cải thiện không trên small tabular data. Thường deep không cần thiết cho tabular data < 10K rows | [Kaggle Titanic](https://www.kaggle.com/competitions/titanic) | 🟡 |
| **D** | IMDB Sentiment Classification | Text classification (positive/negative). Tokenization → Embedding → LSTM/GRU → FC → Sigmoid. Dùng pretrained embeddings (GloVe) → better performance. Sequence padding → same length. Bidirectional LSTM | [Kaggle IMDB](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) | 🟠 |

---

## ✅ CHECKPOINT PHẦN 3

- [ ] Hiểu Perceptron: weighted sum → activation → output. Tại sao cần activation nonlinear
- [ ] ReLU vs Sigmoid vs Tanh: khi nào dùng cái nào. Vanishing gradient xảy ra thế nào
- [ ] Gradient Descent: update rule, lr, momentum. SGD vs Mini-batch vs Batch
- [ ] Backpropagation = chain rule systematic. PyTorch autograd tự tính gradient
- [ ] MLP: 1 hidden layer có thể approximate anything nhưng deep = efficient hơn
- [ ] Dropout, BatchNorm, Weight Decay: các kỹ thuật tránh overfitting trong deep networks
- [ ] CNN: convolution, pooling, filter. Tại sao CNN tốt cho ảnh hơn FC
- [ ] RNN/LSTM: hidden state, sequential memory. Vanishing gradient → cần gates
- [ ] Transfer Learning: khi nào nên dùng pretrained weights
- [ ] Hoàn thành ít nhất **2 trong 4 projects**
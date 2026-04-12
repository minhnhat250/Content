# PHẦN 1 — PYTHON & MATH FOUNDATIONS

> **Mục tiêu:** Setup môi trường → Python căn bản → Toán cho ML
> **Thời gian:** 4–6 tuần · **Cấp độ:** 🟢 Beginner

---

## 1.1 — Setup Môi Trường & Git Cơ Bản

### Mục đích
Trước khi học ML, bạn cần setup môi trường chạy code. Đây là bước nhiều người bỏ qua rồi khổ khi code không chạy.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Cài Anaconda / Miniconda** | [Anaconda Install](https://docs.anaconda.com/free/anaconda/install/) | Anaconda = Python + 1000+ thư viện đã đóng gói sẵn. Miniconda = phiên bản nhẹ hơn Anaconda, chỉ cài Python cơ bản + conda (package manager). Nên dùng Miniconda vì nhẹ, tự chọn thư viện cần. Sau khi cài: mở terminal → `conda --version` để kiểm tra |
| **Cài PyTorch bằng conda** | [PyTorch Install](https://pytorch.org/get-started/locally/) | PyTorch = thư viện deep learning phổ biến nhất (đối thủ: TensorFlow). Vào trang chủ → chọn OS, CUDA version (nếu có GPU NVIDIA) hoặc CPU only → copy lệnh conda. CUDA = nvidia driver cho phép GPU tính toán. Có GPU → cài CUDA. Không có GPU → cài CPU version. Kiểm tra: `python -c "import torch; print(torch.cuda.is_available())"` |
| **Git cơ bản — clone, commit, push** | [Git Book Ch.1-3](https://git-scm.com/book/en/v2) | Git = hệ thống quản lý phiên bản code. clone = tải code từ internet về. commit = lưu snapshot code hiện tại. push = đẩy lên internet (GitHub). Mỗi ngày bạn cần: `git add .` → `git commit -m "message"` → `git push`. Đây là kỹ năng teamwork bắt buộc |
| **VS Code + Python extension** | [VS Code Python](https://code.visualstudio.com/docs/python/python-tutorial) | VS Code = code editor miễn phí của Microsoft. Extension "Python" cho: IntelliSense (gợi ý code), debugging, linting (báo lỗi). Cách cài: VS Code → Extensions → gõ "Python" → cài Microsoft official. Sau đó chọn interpreter (conda env) để VS Code nhận đúng Python environment |
| **Virtual Environment bằng conda** | [Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) | Mỗi project nên có 1 conda env riêng để thư viện không conflict. Tạo: `conda create -n myproject python=3.11`. Kích hoạt: `conda activate myproject`. Mỗi khi code: activate → làm việc → deactivate. Tránh cài tất cả vào base environment |

---

## 1.2 — Python Cơ Bản

### Mục đích
Python là ngôn ngữ lập trình dễ học nhất, được dùng trong hầu hết các thư viện ML. Phần này giúp bạn đọc và viết được Python để dùng thư viện, không cần trở thành Python expert.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Biến, vòng lặp, hàm** | [Codecademy Python](https://www.codecademy.com/learn/learn-python) | Biến: `x = 5` (gán giá trị). Vòng lặp: `for i in range(10)` và `while True`. Hàm: `def greet(name): return f"Hello {name}"`. Đây là những khối xây dựng cơ bản nhất. Codecademy có bài tập tương tác, gõ code → chạy ngay trên trình duyệt, free tier đủ dùng |
| **List, dict, tuple, file I/O** | [W3Schools Python](https://www.w3schools.com/python/) | List: `[1, 2, 3]` — có thể thay đổi (mutable). Dict: `{"name": "An", "age": 25}` — key-value pairs. Tuple: `(1, 2)` — không thay đổi (immutable). File I/O: `open("file.txt", "r")` đọc, `open("file.txt", "w")` ghi. Đây là data structures phổ biến nhất trong Python |
| **List comprehension, lambda** | [Scaler — Python](https://www.scaler.com/topics/python/python-list-comprehension/) | List comprehension: `[x*2 for x in range(10)]` thay vì vòng for 3 dòng. Lambda: `lambda x: x*2` — hàm không tên, dùng inline. Map/Filter: `list(map(lambda x: x*2, my_list))`. Viết code ngắn gọn hơn. Thường dùng trong Pandas và NumPy |
| **Error handling — try/except** | [Scaler — Python Errors](https://www.scaler.com/topics/python/python-error-handling/) | Khi code chạy lỗi, Python dừng. try/except cho phép bắt lỗi và xử lý graceful: `try: result = x/y` → `except ZeroDivisionError: print("không chia được cho 0")`. Trong ML: xử lý khi model predict fail, khi đọc file lỗi. Quan trọng để code production không crash |
| **OOP — class, inheritance** | [Scaler — Python OOP](https://www.scaler.com/topics/python/python-class-and-objects/) | OOP = lập trình hướng đối tượng. Class = blueprint: `class Dog: def __init__(self, name): self.name = name`. Inheritance: `class Cat(Dog)` — Cat kế thừa Dog. PyTorch dùng OOP rất nhiều: `class MyModel(nn.Module)`. Hiểu OOP giúp đọc được code PyTorch và tự viết model riêng |
| **Decorators & Generators** | [Scaler — Python Advanced](https://www.scaler.com/topics/python/python-decorators/) | Decorator: `@property` hoặc `@staticmethod` — thêm behavior cho function. Generator: `yield` thay vì `return` — trả về từng giá trị một thay vì list. Tiết kiệm memory khi xử lý dữ liệu lớn. Ít dùng trong ngày đầu nhưng cần biết khi đọc code ML |

---

## 1.3 — NumPy & Đại Số Tuyến Tính

### Mục đích
ML là toán trên ma trận. NumPy là thư viện giúp Python tính toán ma trận cực nhanh — nhanh hơn Python thuần hàng trăm lần vì dùng C bên dưới. Không biết NumPy = không làm được ML.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **NumPy array — tạo, reshape, slicing** | [NumPy Quickstart](https://numpy.org/devdocs/user/quickstart.html) | Array = mảng n chiều. `np.array([1,2,3])` tạo 1D. `np.zeros((3,4))` tạo ma trận 3 hàng 4 cột toàn 0. Reshape: `arr.reshape(2,3)` — chuyển 1D → 2D mà không thay đổi dữ liệu. Slicing: `arr[1:3, ::2]` — cắt ma trận lấy phần cần. Đây là những thao tác dùng mỗi ngày trong ML |
| **Vector & Ma trận — phép toán cơ bản** | [Scaler — Linear Algebra](https://www.scaler.com/topics/linear-algebra/) | Vector = mảng 1D. Ma trận = mảng 2D. Phép cộng/trừ: cộng từng phần tử. Phép nhân scalar: `2 * arr`. Transpose: `arr.T` — đảo hàng thành cột. Trace: tổng đường chéo. Determinant: định thức — dùng trong PCA. Inverse: ma trận nghịch đảo — giải hệ phương trình tuyến tính |
| **Dot product, Matmul, Transpose** | [Kaggle NumPy](https://www.kaggle.com/learn/numpy) | Dot product (inner product): `np.dot(a, b)` hoặc `a @ b` — tổng tích từng cặp. Matrix multiplication (matmul): `A @ B` — nhân ma trận. Quy tắc: (m×n) @ (n×p) = (m×p). Đây là phép toán cơ bản nhất của Neural Network: weighted sum = input @ weights |
| **NumPy Broadcasting** | [NumPy Broadcasting](https://numpy.org/devdocs/user/basics.broadcasting.html) | Broadcasting = tự động expand array nhỏ để match array lớn. Ví dụ: `arr + 5` — cộng 5 vào mọi phần tử. `arr1 + arr2` (1×n) + (n×1) → tự expand. Hay gây bug khi shape không match. Hiểu broadcasting tránh lỗi khi code ML |
| **Eigenvalue & Eigenvector** | [Scaler — Eigenvalues](https://www.scaler.com/topics/linear-algebra/eigenvalues-and-eigenvectors/) | eigenvector = vector mà khi nhân ma trận A → chỉ bị scale, không đổi hướng. eigenvalue = cái scale đó (λ). `A @ v = λ * v`. Ứng dụng: PCA dùng eigenvalues để chọn principal components quan trọng nhất. Chỉ cần hiểu ý nghĩa, NumPy tính: `np.linalg.eig(A)` |
| **Cosine Similarity** | [Scaler — Cosine](https://www.scaler.com/topics/nlp/cosine-similarity/) | Đo độ tương tự giữa 2 vectors = cos góc giữa chúng. Range: -1 → 1 (ngược hướng → vuông góc → cùng hướng). Công thức: `cos(A,B) = A·B / (||A|| * ||B||)`. Ứng dụng: recommender system, NLP (embeddings), similarity search |

---

## 1.4 — Pandas & Trực Quan Hóa Dữ Liệu

### Mục đích
Dữ liệu ML thường ở dạng bảng (CSV, Excel). Pandas giúp đọc, lọc, xử lý bảng dữ liệu. Trực quan hóa giúp hiểu dữ liệu trước khi model — bước quan trọng mà nhiều người bỏ qua.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Series & DataFrame** | [Kaggle Pandas](https://www.kaggle.com/learn/pandas) | Series = 1 cột (1D labeled array). DataFrame = bảng 2D (nhiều Series ghép lại). `df["column_name"]` lấy 1 cột. `df.head()` xem 5 dòng đầu. `df.info()` xem kiểu dữ liệu. `df.describe()` xem thống kê (mean, std, min, max). Kaggle Pandas free, có bài tập từng bước |
| **Đọc CSV, Excel, JSON** | [Pandas I/O](https://pandas.pydata.org/docs/user_guide/io.html) | `pd.read_csv("file.csv")` đọc CSV. `pd.read_excel("file.xlsx")` đọc Excel. `pd.read_json("file.json")` đọc JSON. `df.to_csv("output.csv", index=False)` ghi ra file. Trong ML: đọc dataset từ Kaggle. `index=False` quan trọng — không ghi thêm cột index vào file |
| **Loc, Iloc, Boolean Filtering** | [GeeksforGeeks](https://www.geeksforgeeks.org/python-pandas-dataframe-loc/) | `loc` = chọn theo LABEL (tên cột, tên dòng): `df.loc[0:3, "name"]` lấy dòng 0→3, cột "name". `iloc` = chọn theo VỊ TRÍ số (integer location): `df.iloc[0:3, 0:2]` lấy 3 dòng đầu, 2 cột đầu. Boolean filtering: `df[df["age"] > 25]` lọc dòng theo điều kiện. Đây là thao tác dùng mỗi ngày khi khám phá dữ liệu |
| **GroupBy, Pivot Table, Merge** | [Kaggle — Group By](https://www.kaggle.com/learn/pandas) | `groupby("col")` nhóm dữ liệu theo giá trị: `df.groupby("city")["price"].mean()` tính giá trung bình theo thành phố. `pivot_table()` tạo bảng 2 chiều từ dữ liệu. `merge(df1, df2, on="id")` ghép 2 bảng theo cột chung. Đây là bước phân tích khi muốn xem patterns trong dữ liệu |
| **Xử lý missing values** | [Pandas Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html) | `df.isna()` trả về True/False cho mỗi cell. `df.dropna()` xóa dòng có missing. `df.fillna(0)` điền 0. `df.fillna(df.mean())` điền giá trị trung bình. Trong ML: missing values cần xử lý trước khi train. Cách xử lý impact model performance rất nhiều |
| **Matplotlib — đồ thị cơ bản** | [Matplotlib PyPlot](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) | `plt.plot(x, y)` line chart. `plt.scatter(x, y)` scatter plot. `plt.bar(cats, vals)` bar chart. `plt.xlabel()`, `plt.title()` thêm labels. `plt.show()` hiển thị. Matplotlib là nền tảng — Seaborn và các thư viện khác đều dựa trên nó. Vẽ được mọi loại đồ thị |
| **Seaborn — đồ thị thống kê đẹp hơn** | [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html) | Seaborn = wrapper around Matplotlib, đồ thị đẹp hơn, code ngắn hơn. `sns.histplot(df["age"])` histogram. `sns.boxplot(x="gender", y="income", data=df)` box plot so sánh 2 nhóm. `sns.heatmap(df.corr())` correlation heatmap. `sns.pairplot(df)` vẽ tất cả scatter pairs. Quan trọng để EDA (Exploratory Data Analysis) |

---

## 1.5 — Xác Suất & Thống Kê

### Mục đích
ML dựa trên xác suất và thống kê. Khi model predict, nó thực chất đang tính probability. Hiểu toán cơ bản giúp bạn biết model đang làm gì, tại sao dùng metrics này, và debug khi model chạy sai.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Xác suất cơ bản — Bayes, Conditional** | [Think Stats — Ch.1-3](https://greenteapress.com/thinkstats2/html/index.html) | Xác suất: P(A) = số lần A xảy ra / tổng số lần. Conditional: P(A\|B) = xác suất A xảy ra BIẾT B đã xảy ra. Bayes Theorem: P(A\|B) = P(B\|A) * P(A) / P(B). Naive Bayes classifier dựa trên Bayes. Hiểu Bayes = hiểu cách ML suy luận từ evidence |
| **Phân phối Normal (Gaussian), Binomial** | [Scaler — Probability Distribution](https://www.scaler.com/topics/probability/probability-distribution/) | Phân phối Normal = hình chuông, đối xứng. Đặc trưng: mean (μ) và std (σ). Nhiều hiện tượng tự nhiên tuân theo Normal: chiều cao, điểm thi. 68% data nằm trong ±1σ, 95% trong ±2σ. Binomial: xác suất có k lần thành công trong n trials. Central Limit Theorem: tổng nhiều random variables → Normal distribution |
| **Mean, median, Std, Variance** | [Scaler — Descriptive Stats](https://www.scaler.com/topics/statistics/descriptive-statistics/) | Mean (trung bình): tổng / n. Median (trung vị): giá trị giữa khi sort. Std (độ lệch chuẩn): đo độ phân tán của data. Variance = std². Mode: giá trị xuất hiện nhiều nhất. Trong ML: mean-center data (đưa mean về 0), standardize (đưa std về 1) là bước tiền xử lý rất phổ biến |
| **Pearson & Spearman Correlation** | [Scaler — Correlation](https://www.scaler.com/topics/statistics/correlation/) | Correlation = đo mức độ 2 biến liên quan tuyến tính. Pearson: linear relationship (tuyến tính). Spearman: monotonic relationship (đơn điệu). Range: -1 → 1. 1 = cùng hướng hoàn toàn, -1 = ngược hướng hoàn toàn, 0 = không liên quan. Trong ML: dùng correlation để chọn features, loại bỏ features trùng lặp |
| **Độ đo khoảng cách — L1, L2, Cosine** | [Scaler — Distance Metrics](https://www.scaler.com/topics/distance-metrics-in-machine-learning/) | L1 (Manhattan): tổng trị tuyệt đối hiệu từng chiều. Dùng khi có outliers. L2 (Euclidean): căn bình phương tổng hiệu bình phương. Dùng phổ biến nhất. Cosine: đo góc giữa 2 vectors, không quan tâm độ lớn. Dùng trong NLP (embeddings). KNN dùng các metrics này để tính khoảng cách |
| **Entropy — lý thuyết thông tin** | [Scaler — Information Gain](https://www.scaler.com/topics/information-gain-in-decision-tree/) | Entropy = đo mức độ "bất định" / "hỗn loạn" của một phân bố. H(x) = -Σ p(x) * log2(p(x)). Entropy cao = data hỗn loạn (nhiều classes). Entropy thấp = data đồng nhất (1 class chiếm đa số). Decision Tree dùng Entropy/Information Gain để quyết định split tại mỗi node — chọn split giảm entropy nhiều nhất |

---

## 1.6 — Calculus Cơ Bản

### Mục đích
ML training = tìm parameters tối thiểu hóa loss. Tối thiểu hóa = đạo hàm. Gradient Descent = thuật toán dùng đạo hàm để tìm minimum. Không hiểu gradient = không hiểu ML đang làm gì bên trong.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Đạo hàm — ý nghĩa hình học** | [Scaler — Calculus](https://www.scaler.com/topics/calculus/) | Đạo hàm = rate of change = "hàm này thay đổi nhanh chậm bao nhiêu". f'(x) = lim (f(x+h) - f(x)) / h. Ý nghĩa: tại x, đạo hàm = độ dốc tiếp tuyến. Ví dụ: f(x) = x² → f'(x) = 2x. Tại x=3, f'(3) = 6 → hàm tăng với rate 6 khi x tăng. ML: loss function thay đổi thế nào khi thay đổi weight |
| **Chain Rule — đạo hàm hàm hợp** | [Scaler — Chain Rule](https://www.scaler.com/topics/calculus/chain-rule-in-calculus/) | Chain rule: đạo hàm của hàm hợp f(g(x)) = f'(g(x)) * g'(x). Ví dụ: f(x) = (3x + 1)² → f'(x) = 2(3x + 1) * 3 = 18x + 6. ĐÂY LÀ CÔNG THỨC QUAN TRỌNG NHẤT TRONG ML. Backpropagation = chain rule được áp dụng hàng nghìn lần trong neural network. Gradient truyền ngược qua mỗi layer = chain rule |
| **Gradient — vector đạo hàm** | [Scaler — Gradient Descent](https://www.scaler.com/topics/calculus/gradient-descent/) | Gradient = vector của tất cả partial derivatives. ∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]. Gradient trỏ theo hướng TĂNG NHANH NHẤT. Để tìm minimum → đi NGƯỢC hướng gradient (negative gradient). Đây là toàn bộ ý tưởng đằng sau Gradient Descent — thuật toán tối ưu hóa cốt lõi của ML |
| **Partial Derivative** | [Scaler — Partial Derivatives](https://www.scaler.com/topics/calculus/partial-derivatives/) | Partial derivative = đạo hàm theo 1 biến, GIỮ CÁC BIẾN KHÁC CỐ ĐỊNH. Ví dụ: f(x,y) = x² + xy → ∂f/∂x = 2x + y, ∂f/∂y = x. Khi hàm có nhiều biến, ta cần partial derivative cho TỪNG biến. Gradient = vector gồm tất cả partial derivatives |
| **Integration cơ bản** | [Scaler — Integration](https://www.scaler.com/topics/calculus/integration/) | Integration = ngược lại của differentiation. ∫f(x)dx = F(x) + C, trong đó F'(x) = f(x). Dùng trong ML để tính area under curve (AUC), probability (tích phân = xác suất). Chỉ cần hiểu khái niệm, PyTorch tính tự động |

---

## 💻 PROJECT PHẦN 1

| # | Project | Mô tả chi tiết | Dataset | Công cụ |
|---|---|---|---|---|
| **A** | Phân tích giá nhà | Khám phá dataset giá nhà: đọc CSV, vẽ phân phối giá, tìm correlation giữa features, tìm outliers. Trực quan hóa mối quan hệ diện tích ↔ giá bằng scatter plot. Kết thúc: hiểu dataset trước khi model | [Kaggle House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) | Pandas + Seaborn |
| **B** | Cosine Similarity Cocktail Recommender | Tạo dataset cocktail (ingredients + flavor profile). Tính cosine similarity giữa cocktails. Recommend cocktail tương tự dựa trên input. Đây là engine cơ bản của mọi recommender system | Tự tạo JSON file | NumPy + Pandas |
| **C** | Streamlit Dashboard EDA | Build web app để explore dataset: upload CSV → hiển thị head, stats, charts. Thêm filter tương tác: chọn columns, range values. Deploy lên Streamlit Cloud miễn phí | Bất kỳ dataset nào | Streamlit + Pandas + Matplotlib |

---

## ✅ CHECKPOINT PHẦN 1

- [ ] Cài đặt được conda environment, chạy được PyTorch (CPU hoặc GPU)
- [ ] Dùng thành thạo NumPy: reshape, dot product, broadcasting — đây là những thao tác dùng mỗi ngày
- [ ] Đọc dữ liệu bằng Pandas, vẽ đồ thị bằng Seaborn — EDA là bước bắt buộc trước khi model
- [ ] Hiểu Gradient = vector trỏ hướng tăng nhanh nhất — Gradient Descent đi ngược lại để tìm minimum
- [ ] Hiểu Chain Rule = công thức cốt lõi của Backpropagation trong Neural Network
- [ ] Hoàn thành ít nhất **1 trong 3 project** — đây là cách học hiệu quả nhất
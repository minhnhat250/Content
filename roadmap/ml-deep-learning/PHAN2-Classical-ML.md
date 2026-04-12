# PHẦN 2 — CLASSICAL MACHINE LEARNING

> **Mục tiêu:** Hiểu & dùng các thuật toán ML cổ điển phổ biến nhất
> **Thời gian:** 4–6 tuần · **Cấp độ:** 🟡 Beginner–Intermediate

---

## 2.1 — Naive Bayes Classification

### Mục đích
Naive Bayes là thuật toán ML đơn giản nhất nhưng hiệu quả bất ngờ. Nền tảng là Bayes Theorem — cách suy luận từ evidence đến kết luận. Dùng rộng rãi trong spam detection, sentiment analysis.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Bayes Theorem — ý nghĩa** | [Scaler — Bayes](https://www.scaler.com/topics/probability/bayes-theorem/) | P(A\|B) = P(B\|A) × P(A) / P(B). P(A\|B) = posterior (xác suất A biết B xảy ra). P(B\|A) = likelihood (khả năng B xảy ra nếu A đúng). P(A) = prior (xác suất A trước khi thấy B). Ví dụ: B=positive test, A= có bệnh. P(bệnh\|positive) = P(positive\|bệnh) × P(bệnh) / P(positive). Đây là cách suy luận cốt lõi của ML |
| **Naive Bayes — giải thích dễ hiểu** | [Scaler — Naive Bayes](https://www.scaler.com/topics/data-science/naive-bayes-classifier/) | "Naive" = giả định các features độc lập với nhau (thường không đúng trong thực tế nhưng vẫn hoạt động tốt). Mỗi class có prior probability. Với new sample: tính P(class) × ∏ P(feature_i\|class) cho mỗi class → chọn class có probability cao nhất. Tính nhanh, scale tốt, dễ interpret |
| **MultinomialNB vs GaussianNB vs BernoulliNB** | [Sklearn Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html) | MultinomialNB: dùng khi features = counts/frequencies (ví dụ: word counts trong text). GaussianNB: dùng khi features = continuous values, giả định Normal distribution. BernoulliNB: dùng khi features = binary (0/1). Trong spam detection → MultinomialNB. Trong medical diagnosis → GaussianNB |
| **Scikit-learn: MultinomialNB, GaussianNB** | [Sklearn Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html) | Code: `from sklearn.naive_bayes import MultinomialNB` → `model = MultinomialNB()` → `model.fit(X_train, y_train)` → `model.predict(X_test)`. Laplace smoothing (alpha): thêm pseudo-count để tránh probability = 0 khi feature chưa thấy bao giờ. `alpha=1.0` là default |
| **Spam Detection bằng Naive Bayes** | [Scaler — Spam Project](https://www.scaler.com/topics/data-science/spam-detection-project-using-naive-bayes-in-python/) | Pipeline: (1) Đọc emails (spam/ham labels). (2) Text preprocessing: lowercase, remove punctuation, tokenize. (3) TF-IDF vectorization: chuyển text → numbers. (4) Train MultinomialNB. (5) Evaluate: accuracy, confusion matrix. Đây là bài toán ML kinh điển nhất. TF-IDF: trọng số = term frequency × inverse document frequency → đánh giá từ quan trọng |

---

## 2.2 — K-Nearest Neighbors (KNN)

### Mục đích
KNN = "học vẹt" (lazy learning): không có công thức toán học để train. Khi có input mới → tìm K điểm gần nhất trong training data → majority vote. Đơn giản nhưng hiệu quả, dùng làm baseline.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **KNN — giải thích bằng hình** | [Scaler — KNN](https://www.scaler.com/topics/machine-learning/k-nearest-neighbors/) | Algorithm: (1) Choose K (số neighbors). (2) Calculate distance từ new point đến TẤT CẢ training points. (3) Sort distances, chọn K điểm gần nhất. (4) Majority vote → class của new point. K nhỏ (1-3): sensitive to noise, overfit. K lớn: smooth decision boundary, underfit. K=5 hay K=7 thường là default tốt |
| **Distance metrics — Euclidean, Manhattan, Cosine** | [Scaler — Distance](https://www.scaler.com/topics/distance-metrics-in-machine-learning/) | Euclidean (L2): căn[(x₁-x₂)² + (y₁-y₂)²]. Khoảng cách đường thẳng. Dùng phổ biến nhất. Manhattan (L1): \|x₁-x₂\| + \|y₁-y₂\|. Khoảng cách theo grid. Dùng khi có outliers. Cosine: 1 - cos(θ). Đo góc, không phụ thuộc magnitude. Dùng trong NLP, high-dimensional data. Chọn metric dựa trên data type |
| **Chọn K — bias-variance tradeoff** | [Scaler — Choose K](https://www.scaler.com/topics/machine-learning/k-value-in-knn/) | K nhỏ (K=1): model phức tạp, low bias, high variance (overfit). K lớn (K=N): model đơn giản, high bias, low variance (underfit). Optimal K: dùng cross-validation thử K = 1,3,5,7,...,√n → chọn K có accuracy cao nhất trên validation set. Odd K để tránh tie (hòa) trong majority vote |
| **Scikit-learn: KNeighborsClassifier** | [Sklearn KNN](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) | Code: `from sklearn.neighbors import KNeighborsClassifier` → `model = KNeighborsClassifier(n_neighbors=5, metric='euclidean')` → `model.fit(X_train, y_train)` → `model.predict(X_test)`. `weights='distance'` thay vì uniform vote: điểm gần hơn có weight cao hơn. `n_jobs=-1` dùng tất cả CPU cores |
| **KNN cho Regression** | [Scaler — KNN Regression](https://www.scaler.com/topics/machine-learning/k-nearest-neighbors-regression/) | Khác Classification: thay majority vote bằng AVERAGE giá trị của K neighbors. Output = continuous value thay vì class label. Dùng khi predict giá trị liên tục (giá nhà, nhiệt độ). `KNeighborsRegressor` trong sklearn |
| **Thực hành: Iris Classification** | [Scaler — Iris](https://www.scaler.com/topics/machine-learning/iris-classification-using-k-nearest-neighbors/) | Iris dataset: 150 samples × 4 features (sepal/petal length/width), 3 species (setosa, versicolor, virginica). Đây là "Hello World" của ML. Benchmark: KNN đạt ~97% accuracy trên Iris. Dataset nhỏ, chạy nhanh, ideal cho beginners |

---

## 2.3 — Decision Tree

### Mục đích
Decision Tree = cây quyết định. Mỗi node = 1 câu hỏi về feature. Đi xuống theo câu trả lời → đến leaf = kết quả. Dễ interpret: nhìn cây → hiểu model quyết định thế nào. Nền tảng của Random Forest và XGBoost.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Decision Tree — giải thích trực quan** | [Scaler — Decision Tree](https://www.scaler.com/topics/machine-learning/decision-tree-in-machine-learning/) | Mỗi node: "Feature X > value?" → Yes → đi sang trái, No → đi sang phải. Leaf node: chứa class label (classification) hoặc giá trị (regression). Đi từ root → leaf = 1 decision path. Ví dụ: "Age > 30?" → "Income > 50K?" → "Buys product?" → Yes. Tree có thể depth tùy data. Interpretable: non-technical people hiểu được |
| **Entropy & Information Gain** | [Scaler — Info Gain](https://www.scaler.com/topics/information-gain-in-decision-tree/) | Entropy = measure of impurity/disorder trong data. H(S) = -Σ p_i × log2(p_i). Data đồng nhất 1 class → Entropy = 0. Data hỗn loạn nhiều classes → Entropy = 1. Information Gain = Entropy(parent) - weighted_avg(Entropy(children)). Chọn split có IG cao nhất → giảm entropy nhiều nhất → data "sạch" hơn sau split |
| **Gini Impurity** | [Scaler — Gini](https://www.scaler.com/topics/machine-learning/gini-impurity/) | Gini = 1 - Σ p_i². Nhanh hơn Entropy tính toán (không có log). 0 = pure (đồng nhất), 0.5 = maximally impure (50/50). Scikit-learn dùng Gini mặc định (criterion='gini'). Entropy thường cho medical/data-sensitive domains. Cả hai cho kết quả tương tự |
| **Scikit-learn: DecisionTreeClassifier / Regressor** | [Sklearn Tree](https://www.scaler.github.io/stable/modules/tree.html) | Code: `from sklearn.tree import DecisionTreeClassifier` → `model = DecisionTreeClassifier(max_depth=5)` → `model.fit(X, y)` → `model.predict(X_test)`. `export_text(model)` xem cây dạng text. `plot_tree(model)` vẽ cây bằng matplotlib |
| **Hyperparameter: max_depth, min_samples_split** | [Scaler — HP](https://www.scaler.com/topics/machine-learning/decision-tree-hyperparameters/) | `max_depth`: giới hạn độ sâu → tránh overfit. `min_samples_split`: tối thiểu samples để split 1 node → càng lớn → cây đơn giản hơn. `min_samples_leaf`: tối thiểu samples ở leaf → càng lớn → less specific. `max_features`: số features được xem khi split → giảm overfit. Grid search tìm optimal hyperparameters |
| **Thực hành: phân loại chất lượng rượu** | [Kaggle Wine](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009) | Dataset: 1599 samples × 11 features (acid, sugar, pH, alcohol...). Target: quality score (3-8). Binary classification: quality ≥ 7 → good wine. Train Decision Tree → xem feature importance: alcohol, volatile acidity, sulphates thường là features quan trọng nhất. So sánh với KNN |

---

## 2.4 — Ensemble: Random Forest & AdaBoost

### Mục đích
Ensemble = kết hợp nhiều weak learners → strong learner. 1 Decision Tree đơn lẻ thường overfit. Random Forest = train nhiều trees với data/feature subsets khác nhau → vote. AdaBoost = train sequential trees, mỗi tree tập trung vào các samples bị sai trước đó.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Ensemble Learning — tại sao cần** | [Scaler — Ensemble](https://www.scaler.com/topics/machine-learning/ensemble-learning/) | Wisdom of the crowd: 1 expert có thể sai, nhưng nhóm 100 experts vote → sai số giảm đáng kể. Tương tự ML: 1 model overfit, 100 models overfit ít hơn (nếu chúng đa dạng). Bias-Variance decomposition: individual model = high variance (overfit). Ensemble = giảm variance, giữ bias.→ tổng chính xác hơn |
| **Bagging vs Boosting — khác nhau** | [Scaler — Bagging Boosting](https://www.scaler.com/topics/machine-learning/bagging-and-boosting/) | Bagging (Bootstrap Aggregating): train multiple models INDEPENDENTLY trên bootstrap samples (sample có hoàn lại). Random Forest là bagging. Models chạy song song, vote/avg cuối cùng. Boosting: train SEQUENTIALLY, mỗi model tập trung vào errors của model trước. AdaBoost, XGBoost là boosting. Sequential → chậm hơn nhưng thường chính xác hơn |
| **Random Forest — hoạt động thế nào** | [Scaler — Random Forest](https://www.scaler.com/topics/machine-learning/random-forest-algorithm/) | Mỗi tree: (1) Bootstrap sample từ data (sample có hoàn lại). (2) Tại mỗi split: chỉ chọn random subset của features (thay vì tất cả). → Trees đa dạng (decorrelation). Cuối: Classification = majority vote, Regression = average. N=100 trees là default tốt. Random forest thường đạt 85-95% accuracy trên tabular data |
| **Feature Importance trong RF** | [Scaler — Feature Importance](https://www.scaler.com/topics/machine-learning/feature-importance-in-random-forest/) | Mean Decrease in Impurity (MDI): tại mỗi split dùng feature X → tính IG weighted sum. Feature có IG cao → important. Feature Importance giúp chọn features (feature selection). Loại bỏ features importance thấp → model đơn giản hơn, ít overfit. `model.feature_importances_` trong sklearn |
| **AdaBoost — hoạt động thế nào** | [Scaler — AdaBoost](https://www.scaler.com/topics/machine-learning/adaboost-algorithm/) | Step 1: train weak tree (stump = tree depth=1) trên all samples. Step 2: tăng weight cho misclassified samples. Step 3: train stump tiếp theo trên weighted samples → stumps tiếp tục "chú ý" đến hard samples. Step 4: combine weighted stumps. Final = sign(Σ α_t × stump_t). AdaBoost rất nhạy với outliers vì hard samples được boost quá nhiều |
| **Scikit-learn: RandomForestClassifier** | [Sklearn RF](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) | Code: `from sklearn.ensemble import RandomForestClassifier` → `model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)` → fit/predict. `n_estimators`: số trees (100-500). `max_features='sqrt'` = default (dùng √features mỗi split). `bootstrap=True` = bagging. `oob_score=True` = đánh giá trên out-of-bag samples (không cần validation set) |
| **Thực hành: Random Forest cho Heart Disease** | [Kaggle Heart](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) | Dataset: 303 samples × 13 features (age, sex, chest pain type, cholesterol...). Target: 0=không bệnh, 1=bệnh. Train RF → xem feature importance: chest pain, max heart rate, slope thường important. So sánh: Decision Tree vs RF vs XGBoost. Xem accuracy trên test set |

---

## 2.5 — Gradient Boosting: XGBoost & LightGBM

### Mục đích
Gradient Boosting hiện là THUẬT TOÁN MẠNH NHẤT cho tabular data. XGBoost và LightGBM là implementation phổ biến nhất. Kaggle competitions: top solutions gần như luôn dùng XGB/LGBM. Performance vượt trội so với RF, SVM, Neural Networks trên structured data.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Gradient Boosting — giải thích dễ nhất** | [Scaler — Gradient Boosting](https://www.scaler.com/topics/machine-learning/gradient-boosting-algorithm/) | Khác RF: RF train trees độc lập (parallel), Boosting train SEQUENTIALLY. Mỗi tree mới học RESIDUALS (sai số) của tổng trees trước. Prediction = sum of trees: pred = tree₁ + tree₂ + tree₃... Tree 1: fit on original data. Tree 2: fit on (actual - tree1_pred) = residuals. Tree 3: fit on (actual - tree1 - tree2_pred)... Mỗi tree tiến dần về minimum |
| **XGBoost — tại sao phổ biến vậy** | [Scaler — XGBoost](https://www.scaler.com/topics/machine-learning/xgboost-algorithm/) | eXtreme Gradient Boosting = optimized gradient boosting implementation. Regularization tích hợp: L1 (Lasso) + L2 (Ridge) → giảm overfit. Column subsampling = random forest trong mỗi tree. Sparse-aware: xử lý missing values tự động. CPU-optimized + GPU support. Thường đạt top 1 trên Kaggle tabular competitions |
| **XGBoost Hyperparameters quan trọng** | [Scaler — XGBoost HP](https://www.scaler.com/topics/machine-learning/xgboost-hyperparameter-tuning/) | `n_estimators`: số trees (100-1000). `learning_rate` (eta): mỗi tree contribute bao nhiêu. Nhỏ → more trees → better nhưng chậm. Default=0.3. `max_depth`: độ sâu mỗi tree. 3-10. `min_child_weight`: minimum sum of instance weight trong child → tránh overfit. `subsample`: % samples dùng mỗi tree (0.6-0.9). `colsample_bytree`: % features mỗi tree (0.6-1.0). `gamma`: minimum loss reduction để split → regularization |
| **XGBoost cho Classification** | [Scaler — XGB Classification](https://www.scaler.com/topics/machine-learning/xgboost-for-classification/) | `objective='binary:logistic'` → sigmoid output. `objective='multi:softprob'` → probability cho mỗi class. Code: `from xgboost import XGBClassifier` → `model = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=6)` → `model.fit(X_train, y_train)` → `model.predict(X_test)`. Early stopping: `eval_set=[(X_val, y_val)], early_stopping_rounds=10` → tự dừng khi validation loss không cải thiện |
| **XGBoost cho Regression** | [Scaler — XGB Regression](https://www.scaler.com/topics/machine-learning/xgboost-regression/) | `objective='reg:squarederror'` (MSE) hoặc `reg:absoluteerror` (MAE) hoặc `reg:pseudohubererror`. `eval_metric='rmse'` hoặc `mae`. Dùng cho: dự đoán giá nhà, giá cổ phiếu, doanh số. XGB thường outperform Linear Regression, Random Forest trên regression tasks |
| **LightGBM — nhanh hơn XGBoost** | [Scaler — LightGBM](https://www.scaler.com/topics/machine-learning/lightgbm-algorithm/) | Khác XGBoost: dùng Gradient-based One-Side Sampling (GOSS) + Exclusive Feature Bundling (EFB) → 10-20× faster training. GOSS: giữ samples có gradient lớn (important), sample ngẫu nhiên samples có gradient nhỏ. EFB: bundle mutually exclusive features (sparse columns). Dùng LightGBM khi: data > 1M rows, cần fast iteration, production pipeline |
| **GOSS & EFB trong LightGBM** | [Scaler — LightGBM Fast](https://www.scaler.com/topics/machine-learning/lightgbm-algorithm/) | GOSS (Gradient-based One-Side Sampling): keep all samples with large gradients + randomly sample from small gradients. EFB (Exclusive Feature Bundling): features thường mutually exclusive trong sparse data (example: one-hot encoded categories). Bundle chúng thành 1 feature → giảm dimensionality. Hai kỹ thuật này giúp LightGBM xử lý data lớn cực nhanh |
| **Thực hành: Airbnb Price Prediction** | [Kaggle Airbnb](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data) | Dataset: listings NYC × features (room type, neighborhood, reviews, accommodates...). Target: price. Feature engineering quan trọng: extract year/month từ last_review, log-transform price (skewed). Compare: Linear Regression → RF → XGBoost → LightGBM. Xem improvement từ từng model. Hyperparameter tuning bằng cross-validation |
| **Thực hành: Wine Quality Classification** | [Kaggle Wine](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009) | Binary: quality ≥ 7 → good wine. Feature engineering: tạo interaction features (alcohol × acidity). Compare: XGBoost vs LightGBM. Feature importance: xem features nào ảnh hưởng quality nhất. Tune hyperparameters → xem accuracy improvement |

---

## 2.6 — K-Means Clustering (Unsupervised)

### Mục đích
Khác supervised: không có labels. K-Means tự nhóm data thành K clusters dựa trên similarity. Ứng dụng: customer segmentation, image compression, anomaly detection. Không có "đáp án đúng" — đánh giá bằng metrics.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Unsupervised Learning — khác gì Supervised** | [Scaler — Unsupervised](https://www.scaler.com/topics/machine-learning/types-of-machine-learning/) | Supervised: có X (features) + y (labels). Learn mapping X → y. Unsupervised: chỉ có X. Discover structure ẩn trong data. 3 types: Clustering (nhóm), Dimensionality Reduction (giảm chiều), Association (tìm rules). Unsupervised quan trọng vì majority data trong thực tế KHÔNG có labels (expensive để label) |
| **K-Means — giải thích bằng hình** | [Scaler — K-Means](https://www.scaler.com/topics/machine-learning/k-means-clustering/) | Algorithm: (1) Chọn K centroids ngẫu nhiên. (2) E-step: assign mỗi point → centroid gần nhất. (3) M-step: recalculate centroids = mean của points trong cluster. (4) Repeat 2-3 cho đến convergence (centroids không đổi). Output: mỗi point có cluster label + K centroids. Non-convex clusters → K-Means không hoạt động tốt |
| **Elbow Method — chọn số K** | [Scaler — Elbow](https://www.scaler.com/topics/machine-learning/elbow-method-in-k-means/) | K太少 → high inertia (intra-cluster distance cao). K太多 → low inertia → overfit. Elbow Method: plot inertia vs K. Tìm điểm "elbow" = inertia giảm chậm lại. Thường K=3-6 cho customer segmentation. Silhouette score bổ sung để confirm |
| **Silhouette Score** | [Scaler — Silhouette](https://www.scaler.com/topics/machine-learning/silhouette-score/) | Measure how similar 1 point to its own cluster vs other clusters. Range: -1 → 1. 1 = perfectly clustered. 0 = overlapping clusters. -1 = misclassified. Silhouette = (b - a) / max(a, b). a = avg intra-cluster distance. b = avg nearest-cluster distance. > 0.5 = reasonable structure. > 0.7 = strong structure |
| **Scikit-learn: KMeans** | [Sklearn KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) | Code: `from sklearn.cluster import KMeans` → `model = KMeans(n_clusters=3, random_state=42, n_init=10)` → `model.fit(X)` → `labels = model.labels_`. `n_init=10`: chạy 10 lần với init khác nhau → chọn best. `max_iter=300`: max iterations mỗi run. `cluster_centers_`: tọa độ centroids. `inertia_`: total within-cluster sum of squares |
| **PCA — giảm chiều dữ liệu** | [Scaler — PCA](https://www.scaler.com/topics/machine-learning/principal-component-analysis/) | Principal Component Analysis = projection data xuống fewer dimensions mà giữ maximum variance. Components = eigenvectors của covariance matrix, sorted by eigenvalue (lớn → nhỏ). Keep top N components đủ explained variance > 95%. Dùng trước K-Means khi: high-dimensional data (100+ features) → giảm noise, tăng cluster quality. sklearn: `PCA(n_components=2)` |
| **Customer Segmentation bằng K-Means** | [Scaler — Customer Seg](https://www.scaler.com/topics/machine-learning/customer-segmentation-using-k-means/) | Business context: chia customers thành nhóm để target marketing. Features: age, income, spending score, purchase frequency. Pipeline: load data → scale (StandardScaler) → PCA (nếu nhiều features) → Elbow + Silhouette để chọn K → K-Means → analyze cluster profiles → interpret results. Output: Customer persona for each cluster |
| **Thực hành: phân nhóm khách hàng** | [Kaggle Mall](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) | Dataset: 200 customers × 5 features (Gender, Age, Annual Income, Spending Score). Target: phân nhóm tự nhiên → không có label. K-Means với K=5 → 5 customer segments. Profile từng cluster: "Young High Spender", "Old Low Spender"... Visualize bằng scatter plot (PCA 2D) |

---

## 2.7 — Đánh Giá Mô Hình (Evaluation)

### Mục đích
Đánh giá model = biết model có thực sự tốt hay không. Accuracy một mình không đủ — imbalanced data → accuracy 95% nhưng không phát hiện được fraud. Metrics khác nhau phù hợp cho bài toán khác nhau.

### Chi tiết từng bước

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Confusion Matrix — TP, TN, FP, FN** | [Scaler — Confusion](https://www.scaler.com/topics/machine-learning/confusion-matrix/) | Confusion Matrix = 2×2 grid: Rows = actual, Columns = predicted. TN (True Negative) = actual 0, predicted 0 ✓. TP (True Positive) = actual 1, predicted 1 ✓. FP (False Positive) = actual 0, predicted 1 ✗ (Type 1 error). FN (False Negative) = actual 1, predicted 0 ✗ (Type 2 error). Từ confusion matrix → tính tất cả metrics |
| **Accuracy, Precision, Recall, F1-Score** | [Scaler — PR F1](https://www.scaler.com/topics/machine-learning/precision-recall-f1-score/) | Accuracy = (TP+TN) / ALL. Precision = TP / (TP+FP) = "trong các điểm model nói là 1, bao nhiêu đúng". Recall = TP / (TP+FN) = "trong các điểm thực sự là 1, model nói đúng bao nhiêu". F1 = 2×Precision×Recall / (P+R) = harmonic mean. Precision-Recall tradeoff: tăng 1 → giảm kia. F1 balance cả hai |
| **Khi nào dùng Precision vs Recall** | [Scaler — PR F1](https://www.scaler.com/topics/machine-learning/precision-recall-f1-score/) | High Precision: khi FALSE POSITIVE nguy hiểm → spam filter (không muốn mark email thật là spam). High Recall: khi FALSE NEGATIVE nguy hiểm → medical diagnosis (không muốn bỏ sót bệnh nhân). Fraud detection: cần both → F1. Imbalanced dataset → NEVER rely on accuracy |
| **ROC Curve & AUC** | [Scaler — ROC AUC](https://www.scaler.com/topics/machine-learning/auc-roc-curve/) | ROC = True Positive Rate (Recall) vs False Positive Rate (FPR) tại các classification thresholds. AUC = Area Under ROC Curve. 0.5 = random, 1.0 = perfect. AUC không phụ thuộc threshold → đánh giá model quality tổng thể. AUC > 0.9 = excellent, 0.8-0.9 = good, < 0.7 = poor. Dùng khi classes imbalanced |
| **MSE, RMSE, MAE — regression metrics** | [Scaler — Regression Metrics](https://www.scaler.com/topics/machine-learning/regression-metrics/) | MSE (Mean Squared Error) = mean((y_pred - y_actual)²). Penalizes large errors nặng (vì bình phương). Sensitive to outliers. RMSE = √MSE. Same unit as target. MAE = mean(|y_pred - y_actual|). Penalizes equally → less sensitive to outliers. Chọn: có outliers → MAE, muốn penalize big errors → MSE/RMSE |
| **Train/Test Split — tránh overfitting** | [Scaler — Train Test](https://www.scaler.com/topics/machine-learning/train-test-split/) | Never evaluate on training data → overfit indicator. Split: 70-80% train, 20-30% test. `sklearn.model_selection.train_test_split(X, y, test_size=0.2, random_state=42)`. random_state = reproducibility. Stratified split: giữ class proportions bằng nhau trong train/test (important for imbalanced) |
| **K-Fold Cross Validation** | [Scaler — Cross Val](https://www.scaler.com/topics/machine-learning/k-fold-cross-validation/) | Chia data thành K folds (thường K=5 hoặc 10). Train K times: mỗi lần dùng 1 fold làm test, K-1 folds làm train. Report mean ± std accuracy. Robust evaluation: model không overfit vào 1 particular split. K-Fold CV cần thiết khi dataset nhỏ (< 10K rows) |
| **Scikit-learn: classification_report, cross_val_score** | [Sklearn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html) | Code: `from sklearn.model_selection import cross_val_score` → `scores = cross_val_score(model, X, y, cv=5, scoring='f1')` → `print(f"{scores.mean():.3f} ± {scores.std():.3f}")`. `classification_report(y_true, y_pred)` → precision, recall, f1 per class + support. `confusion_matrix(y_true, y_pred)` → matrix |

---

## 💻 PROJECT PHẦN 2

| # | Project | Mô tả chi tiết | Dataset | Cấp |
|---|---|---|---|:---:|
| **A** | Phân loại bệnh tim | Compare KNN, Naive Bayes, Decision Tree, Random Forest, XGBoost trên cùng dataset. Trực quan hóa confusion matrices, ROC curves. Tự chọn best model dựa trên metrics phù hợp | [Kaggle Heart](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset) | 🟡 |
| **B** | Phân loại chủ đề bài báo khoa học | Text classification: đọc abstracts → phân loại topic (CS, Physics, Medical). TF-IDF vectorization + ML models (NB, KNN, RF, XGB). Compare training time vs accuracy | [Kaggle](https://www.kaggle.com/datasets/ten帘inews/cnews) | 🟡 |
| **C** | Customer Segmentation | Phân nhóm khách hàng mall. K-Means + PCA. Elbow + Silhouette chọn K. Profile từng segment. Đề xuất marketing strategy cho từng segment | [Kaggle Mall](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) | 🟡 |
| **D** | Dự đoán giá thuê phòng Airbnb | Tabular regression: clean data, feature engineering, so sánh RF vs XGBoost vs LightGBM. Hyperparameter tuning. Interpret feature importance | [Kaggle Airbnb](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data) | 🟠 |

---

## ✅ CHECKPOINT PHẦN 2

- [ ] Hiểu Bayes Theorem → Naive Bayes hoạt động thế nào — dùng cho spam detection
- [ ] KNN: cách tính khoảng cách, cách chọn K, bias-variance tradeoff
- [ ] Decision Tree: Entropy/Gini → Information Gain → cách split quyết định tại sao feature này trước
- [ ] Random Forest vs AdaBoost: bagging vs boosting — khi nào dùng cái nào
- [ ] XGBoost/LightGBM: gradient boosting — học residuals, tại sao mạnh cho tabular data
- [ ] Phân biệt Precision vs Recall — khi nào cần cái nào, F1 là gì
- [ ] K-Means: thuật toán, Elbow Method chọn K, Silhouette Score đánh giá
- [ ] Hoàn thành ít nhất **2 trong 4 projects**
# PHẦN 4 — DEEP LEARNING NÂNG CAO

> **Mục tiêu:** Nắm kiến trúc DL hiện đại — Transformer, NLP, Vision, GenAI, LLM
> **Thời gian:** 6–8 tuần · **Cấp độ:** 🔴 Advanced

---

## 4.1 — Transformer & Attention

### 4.1.1 — Attention Mechanism

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Attention Mechanism — ý tưởng cốt lõi** | [Scaler — Attention](https://www.scaler.com/topics/deep-learning/attention-mechanism-in-deep-learning/) | Thay vì nhìn toàn bộ input đều như nhau, Attention cho phép model TẬP TRUNG vào phần quan trọng nhất. Cơ chế: Query ("tôi muốn gì?"), Key ("tôi có gì?"), Value ("nội dung thật sự"). Điểm tương đồng Query-Key càng cao → weight cho Value tương ứng càng lớn |
| **Self-Attention — nhìn chính mình** | [Scaler — Self Attention](https://www.scaler.com/topics/deep-learning/self-attention-in-transformers/) | Mỗi token trong câu nhìn MỐI QUAN HỆ với tất cả các tokens khác trong cùng câu. Ví dụ: "con mèo ngồi trên thảm" → từ "ngồi" có attention cao với "mèo" và "thảm", thấp với "con". Không có thứ tự (permutation invariant) |
| **Scaled Dot-Product Attention** | [Scaler — Scaled Attention](https://www.scaler.com/topics/deep-learning/scaled-dot-product-attention/) | Tính similarity giữa Query và Key bằng dot product → chia cho √d_k (scale factor) → softmax → nhân với Value. Scale factor √d_k tránh gradient vanishing khi d_k lớn. Đây là công thức nền tảng của mọi Transformer |
| **Multi-Head Attention** | [Scaler — Multi Head](https://www.scaler.com/topics/deep-learning/multi-head-attention-in-transformers/) | Chạy nhiều attention heads song song, mỗi head học một loại relationship khác nhau (head 1: subject-verb, head 2: noun-adjective, head 3: spatial relations...). Cuối cùng concat outputs của các heads lại, rồi nhân với weight matrix. Thường dùng 8-16 heads |

### 4.1.2 — Transformer Architecture

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Transformer — tổng quan kiến trúc** | [Scaler — Transformer](https://www.scaler.com/topics/deep-learning/what-is-transformer-in-deep-learning/) | "Attention is All You Need" — 2017. Gồm Encoder (xử lý input sequence) và Decoder (sinh output). Không có RNN, không có convolution — chỉ dùng Attention. Có thể parallelize hoàn toàn → train nhanh hơn RNN rất nhiều. Đây là kiến trúc thay đổi toàn bộ NLP |
| **Positional Encoding** | [Scaler — Positional](https://www.scaler.com/topics/deep-learning/positional-encoding-in-transformers/) | Transformer không có khái niệm thứ tự (permutation invariant). Positional Encoding thêm thông tin vị trí vào mỗi token — dùng sin/cos với frequencies khác nhau. Để model phân biệt "con mèo đuổi chó" vs "chó đuổi con mèo". Có thể dùng learned positional encoding thay vì fixed sin/cos |
| **Residual Connection & Layer Normalization** | [Scaler — Residual](https://www.scaler.com/topics/deep-learning/residual-connections-in-transformers/) | Mỗi sub-layer (Attention, FFN) có residual connection: output = SubLayer(x) + x. Giúp gradient flow trực tiếp qua các layers sâu. LayerNorm: normalize trên features (mean=0, std=1) thay vì batch. Ổn định training hơn BatchNorm trong Transformer. Add & Norm = Residual + LayerNorm |
| **Feed Forward Network trong Transformer** | [Scaler](https://www.scaler.com/topics/deep-learning/feedforward-neural-networks/) | Mỗi encoder/decoder layer có một FFN gồm 2 linear layers: expand từ d_model → d_ff (thường gấp 4 lần) → compress lại. Áp dụng cho từng token độc lập. Tương đương attention nhưng học được nonlinear patterns |

### 4.1.3 — BERT & GPT

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **BERT — Bidirectional Encoder Representations** | [Scaler — BERT](https://www.scaler.com/topics/deep-learning/what-is-bert/) | Google 2018. Dùng chỉ Encoder của Transformer. Pre-train bằng 2 tasks: Masked Language Modeling (che 15% tokens rồi predict) và Next Sentence Prediction. Bidirectional: nhìn cả trái lẫn phải cùng lúc. Fine-tune cho downstream tasks: QA, sentiment, NER. State-of-the-art NLP 2018-2020. BERT-base: 110M params |
| **GPT — Generative Pretrained Transformer** | [Scaler — GPT](https://www.scaler.com/topics/deep-learning/gpt-generative-pre-trained-transformer/) | OpenAI. Dùng chỉ Decoder của Transformer. Pre-train bằng Language Modeling (predict next token). Unidirectional: chỉ nhìn tokens trước đó. Auto-regressive: output at step t là input at step t+1. GPT-3: 175B params. ChatGPT/GPT-4 foundation |
| **BERT vs GPT — so sánh cốt lõi** | [Scaler](https://www.scaler.com/topics/deep-learning/what-is-bert/) | BERT = Encoder-only → bidirectional context → tốt cho understanding tasks (classification, NER, QA). GPT = Decoder-only → unidirectional → tốt cho generation tasks (viết, chat). BERT thường fine-tune nhanh hơn với ít data |
| **RoBERTa, DistilBERT, ALBERT — biến thể BERT** | [Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/auto) | RoBERTa: remove NSP, train lâu hơn, data nhiều hơn → tốt hơn BERT. DistilBERT: distill BERT (knowledge transfer) → 60% faster, 97% performance. ALBERT: shared parameters → nhẹ hơn 10×. PhoBERT: BERT fine-tuned cho tiếng Việt |
| **Hugging Face Transformers — library chuẩn** | [HF Docs](https://huggingface.co/docs/transformers/index) | Thư viện Python cực phổ biến nhất cho NLP. 10,000+ pretrained models. Code cực ngắn: `AutoTokenizer + AutoModel`. Pipeline API: `pipeline("sentiment-analysis")` → 3 dòng code có ngay model chạy. Transformers là tiêu chuẩn công nghiệp |

---

## 4.2 — NLP Ứng Dụng

### 4.2.1 — Xử Lý Ngôn Ngữ Cơ Bản

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Tokenization — BPE, WordPiece, SentencePiece** | [Scaler — Tokenization](https://www.scaler.com/topics/nlp/tokenization-in-nlp/) | Token = đơn vị nhỏ nhất mà model "nhìn thấy". WordPiece (BERT): chia từ thành subword ("unbelievable" → "un##believ##able"). BPE (GPT): ghép các cặp subword tần suất cao. Byte-level BPE (GPT-2/3): hoạt động trên bytes thay vì Unicode → xử lý mọi ngôn ngữ. Vocab size: BERT-base = 30,522 tokens |
| **Word Embeddings — Word2Vec, GloVe, FastText** | [Scaler — Embeddings](https://www.scaler.com/topics/nlp/word-embeddings/) | Embedding = map từng từ thành vector số (thường 100-300 chiều). Word2Vec (Mikolov 2013): học embeddings bằng CBOW hoặc Skip-gram. GloVe: học từ co-occurrence matrix. FastText: học trên character n-grams → bắt được từ hiếm, ngôn ngữ ít tài nguyên. Embeddings encode semantic similarity: vector("king") - vector("man") + vector("woman") ≈ vector("queen") |
| **Position-wise Feed Forward trong NLP** | [Scaler](https://www.scaler.com/topics/deep-learning/feedforward-neural-networks/) | Mỗi token sau khi qua Attention được feed vào FFN riêng. FFN thường gồm: Linear(d→4d) → ReLU → Linear(4d→d). Áp dụng cùng weights cho mọi positions nhưng weights này là learnable. FFN học nonlinear transformations mà Attention không học được |

### 4.2.2 — NLP Tasks Thường Gặp

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Sentiment Analysis — phân tích cảm xúc** | [Scaler — Sentiment](https://www.scaler.com/topics/nlp/sentiment-analysis-using-nlp/) | Classification: positive/negative/neutral. Cách tiếp cận cổ điển: lexicon-based (VADER), ML (NB, SVM với TF-IDF). Cách hiện đại: fine-tune BERT → đạt 95%+ accuracy. Ứng dụng: brand monitoring, review analysis, customer feedback |
| **Named Entity Recognition (NER) — trích xuất thực thể** | [Scaler — NER](https://www.scaler.com/topics/nlp/named-entity-recognition/) | Token-level classification: mỗi token được gán label (PER=person, ORG=organization, LOC=location, DATE=ngày tháng...). CRF layer truyền thống dùng để encode dependencies giữa labels liền kề. BERT-based NER đạt F1 > 90% trên standard benchmarks |
| **POS Tagging — gán nhãn từ loại** | [Scaler — POS](https://www.scaler.com/topics/nlp/parts-of-speech-tagging/) | Gán nhãn cho từng token: NN=noun, VB=verb, JJ=adjective... Là bước tiền xử lý cho nhiều NLP tasks: parsing, machine translation, NER. Dùng BiLSTM-CRF truyền thống hoặc BERT token classifier |
| **Question Answering — hỏi đáp** | [Scaler — QA](https://www.scaler.com/topics/nlp/question-answering-system/) | Reading comprehension: đọc đoạn văn → trả lời câu hỏi. Dataset: SQuAD 2.0. Span extraction: predict start/end position trong đoạn văn. Open-domain QA: kết hợp với search engine. RAG (Retrieval-Augmented Generation): retrieve docs → LLM answer |

### 4.2.3 — NLP Nâng Cao

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Text Summarization — tóm tắt văn bản** | [Scaler — Summarization](https://www.scaler.com/topics/nlp/text-summarization-using-nlp/) | Extractive: chọn câu quan trọng nhất từ văn bản gốc (dùng sentence scoring). Abstractive: sinh câu mới tóm tắt nội dung (cần generative model: T5, BART, PEGASUS). BLEU, ROUGE metrics để đánh giá. Ứng dụng: tóm tắt tin tức, tài liệu dài, meeting notes |
| **Machine Translation — dịch máy** | [Scaler](https://www.scaler.com/topics/deep-learning/machine-translation-using-deep-learning/) | Encoder encode câu nguồn thành context vector → Decoder auto-regressive sinh câu đích từng token. BLEU score đánh giá chất lượng. Transformer dịch tốt hơn phrase-based SMT rất nhiều. Mô hình dịch Việt-Anh phổ biến trong các cuộc thi |
| **Text Generation — sinh văn bản** | [Scaler](https://www.scaler.com/topics/deep-learning/gpt-generative-pre-trained-transformer/) | Sampling từ probability distribution của next token. Temperature: cao → random, đa dạng; thấp → deterministic, bảo thủ. Top-k, Top-p sampling kiểm soát diversity. Nucleus sampling (top-p): chọn tokens có cumulative probability > p. Cần kiểm soát toxicity, hallucination khi deploy |
| **Aspect-Based Sentiment Analysis (ABSA)** | [Scaler](https://www.scaler.com/topics/nlp/aspect-based-sentiment-analysis/) | Phân tích sentiment theo TỪNG KHÍA CẠNH. Ví dụ review nhà hàng: "đồ ăn ngon nhưng phục vụ chậm". ABSA: extract aspect "đồ ăn" → positive, aspect "phục vụ" → negative. Phức tạp hơn sentiment thông thường. Tasks con: Aspect Term Extraction + Aspect Sentiment Classification |
| **Thực hành: Vietnamese Sentiment Analysis** | [UIT-VSFC](https://github.com/thinhclaim/VietnameseTextClassification) | Dataset UIT-VSF dành cho tiếng Việt: positive/negative/neutral trên câu. Dùng PhoBERT (BERT cho tiếng Việt) fine-tune. Đạt ~85-90% accuracy. Code có sẵn trên GitHub |
| **Thực hành: Vietnamese NER** | [VLSP 2023](https://vlsp.howafe.vn/) | VLSP (Vietnam Language Processing) là chuẩn benchmark cho tiếng Việt: PER, ORG, LOC, TIME, MISC. Dùng PhoBERT token classifier. Datasets: VLSP 2016, 2018, 2023 |

---

## 4.3 — Computer Vision Nâng Cao

### 4.3.1 — Kiến Trúc CNN Nổi Tiếng

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **LeNet-5 — kiến trúc đầu tiên** | [Scaler — LeNet](https://www.scaler.com/topics/deep-learning/lenet-5-architecture/) | Yann LeCun thiết kế 1998, dùng cho nhận diện chữ số MNIST. 7 layers: Input(32×32) → C1 conv(6) → S2 pool → C3 conv(16) → S4 pool → C5 conv(120) → FC(84) → Output(10). Dùng tanh activation, avg pooling. Tỷ lệ correct ~99% trên MNIST |
| **AlexNet — game changer 2012** | [Scaler — AlexNet](https://www.scaler.com/topics/deep-learning/alexnet-architecture/) | Chiến thắng ImageNet với 60 triệu params, top-5 error 15.3% (kỷ lục). Innovations: ReLU (nhanh hơn tanh 6×), Dropout (tránh overfitting), GPU training (2 GPUs 8 ngày). Đặt nền móng cho Deep Learning boom. Có 5 conv layers + 3 FC layers |
| **VGGNet — đơn giản mà hiệu quả** | [Scaler — VGG](https://www.scaler.com/topics/deep-learning/vggnet-architecture/) | Dùng kernel 3×3 xếp chồng thay vì kernel lớn (7×7, 11×11). VGG-16 (16 layers): 13 conv + 3 FC. VGG-19 (19 layers). Params: 138 triệu. Thường dùng làm backbone cho transfer learning vì weights được public rộng rãi. Đơn giản nhưng tốn memory |
| **ResNet — skip connection giải quyết degradation** | [Scaler — ResNet](https://www.scaler.com/topics/deep-learning/resnet-architecture/) | Mỗi block học phần dư (residual) F(x) thay vì học toàn bộ mapping H(x). Output = F(x) + x (skip connection). Gradient truyền ngược trực tiếp qua skip → train được 1000+ layers. ResNet-50 (50 layers): 25.6 triệu params, 3.6% top-5 error ImageNet. Breakthrough architecture |
| **EfficientNet — cân bằng accuracy vs efficiency** | [Scaler — EfficientNet](https://www.scaler.com/topics/deep-learning/efficientnet-architecture/) | Compound scaling: cân bằng depth (sâu hơn), width (rộng hơn), resolution (lớn hơn) bằng coefficient φ. EfficientNet-B7: 66 triệu params nhưng accuracy tương đương ResNet-200 (115 triệu params). Sử dụng depthwise separable convolution (MobileNet) để giảm computation |

### 4.3.2 — Object Detection

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Object Detection — từ classification đến detection** | [Scaler — Object Detection](https://www.scaler.com/topics/deep-learning/object-detection-in-deep-learning/) | Classification: 1 object trong ảnh → class label. Object Detection: nhiều objects → class + bounding box (x, y, width, height). Metrics: mAP (mean Average Precision), IoU (Intersection over Union). Hai nhóm: Two-stage (accurate, chậm) và One-stage (fast, less accurate) |
| **R-CNN → Fast R-CNN → Faster R-CNN evolution** | [Scaler](https://www.scaler.com/topics/deep-learning/r-cnn-model-in-deep-learning/) | R-CNN (2014): Selective Search (2000 regions) → crop → resize → CNN → SVM. 47s/ảnh vì mỗi region gọi CNN riêng. Fast R-CNN (2015): feed whole image → ROI pooling → classify. 2s/ảnh. Faster R-CNN (2016): thay Selective Search bằng RPN (Region Proposal Network) → end-to-end trainable. 0.2s/ảnh |
| **YOLO — You Only Look Once** | [Scaler — YOLO](https://www.scaler.com/topics/deep-learning/yolo-object-detection/) | Không có region proposal. Chia ảnh thành grid (S×S). Mỗi cell: predict B bounding boxes + confidence + C class probabilities. Non-max suppression loại bỏ overlapping boxes. YOLOv1 (2016): 45 FPS. YOLOv8 (2023): 1200 FPS, object detection + segmentation trong 1 model. Realtime production-ready |
| **YOLOv5 → v8 — hiện tại** | [Ultralytics Docs](https://docs.ultralytics.com/) | Ultralytics YOLOv8: CSPDarknet backbone + PANet + anchor-free detection (YOLOX). API Python cực dễ: `model = YOLO('yolov8n.pt')`. Training custom: dataset format YOLO (txt files) → `model.train(data='coco8.yaml', epochs=100)`. Deployed được sang ONNX, TensorRT, TFLite. Đây là lựa chọn số 1 cho production object detection |

### 4.3.3 — Image Segmentation

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **Semantic Segmentation — phân đoạn pixel** | [Scaler — Segmentation](https://www.scaler.com/topics/deep-learning/image-segmentation-in-deep-learning/) | Phân loại TỪNG PIXEL trong ảnh. Ví dụ: ảnh đường phố → mỗi pixel = class (đường, vỉa hè, xe, cây). Output mask cùng kích thước ảnh gốc. Metrics: IoU per class, mean IoU. Ứng dụng: autonomous driving, medical imaging, satellite imagery |
| **FCN — Fully Convolutional Network** | [Scaler](https://www.scaler.com/topics/deep-learning/fully-convolutional-network/) | Thay FC layers bằng conv layers → output là spatial heatmap thay vì class score. Upsampling bằng transposed convolution (deconvolution) hoặc bilinear interpolation. Nền tảng cho mọi segmentation models |
| **U-Net — encoder-decoder với skip connections** | [Scaler — U-Net](https://www.scaler.com/topics/deep-learning/u-net-architecture/) | Encoder (contracting path): giảm spatial resolution, tăng channels. Decoder (expanding path): tăng resolution lại. Skip connections nối trực tiếp encoder ↔ decoder ở cùng resolution. Đặc biệt hiệu quả cho medical images vì cần segmentation chính xác. Loss: Binary Cross-Entropy + Dice Loss |
| **Mask R-CNN — instance segmentation** | [Scaler](https://www.scaler.com/topics/deep-learning/mask-r-cnn-in-deep-learning/) | Faster R-CNN + thêm branch predict binary mask cho từng instance. Instance segmentation: phân biệt từng đối tượng riêng (chó A vs chó B) thay vì semantic (tất cả pixels "chó"). More computation overhead so với detection thuần |
| **Vision Transformer (ViT)** | [Scaler — ViT](https://www.scaler.com/topics/deep-learning/vision-transformer/) | Chia ảnh thành patches (16×16) → mỗi patch = "token" như trong NLP. Thêm CLS token (như BERT) → classification. Position embedding cho spatial information. Transformer encoders xử lý sequence of patches. ViT cần data lớn (14M-300M images) mới beat CNN. EfficientViT, SwinViT tối ưu cho data nhỏ |

---

## 4.4 — Generative AI (GenAI)

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **GAN — Generative Adversarial Networks** | [Scaler — GAN](https://www.scaler.com/topics/deep-learning/generative-adversarial-networks/) | Gồm 2 networks chơi Claude game: Generator (sinh ảnh giả) cố gắng fool Discriminator (phân biệt giả/thật). Training: G update để maximize D's error; D update để minimize error. Equilibrium: G sinh ảnh mà D không phân biệt được. Mode collapse: G sinh limited variety. Ứng dụng: sinh chân dung, artwork, game assets |
| **DCGAN — Deep Convolutional GAN** | [Scaler — DCGAN](https://www.scaler.com/topics/deep-learning/dcgan-deep-convolutional-gan/) | Thay FC layers bằng conv/deconv layers. Best practices: BatchNorm trong G và D (trừ output layer G, input layer D), LeakyReLU, Adam optimizer. Đây là kiến trúc GAN ổn định đầu tiên có thể train lâu dài. Nhiều GAN variants được build trên DCGAN: WGAN, StyleGAN |
| **Stable Diffusion — latent diffusion model** | [Stable Diffusion GH](https://github.com/Stability-AI/stablediffusion) | Thực hiện diffusion trong LATENT SPACE thay vì pixel space → 100× faster. Gồm 3 components: (1) VAE encode ảnh thành latent → (2) UNet denoise trong latent với text conditioning từ CLIP → (3) VAE decode latent → ảnh. SD v1.5, SDXL, SD3 — các phiên bản. Dùng làm engine cho Midjourney, Leonardo AI |
| **Diffusion Models — giải thích dễ hiểu** | [Scaler — Diffusion](https://www.scaler.com/topics/deep-learning/diffusion-models-in-deep-learning/) | Forward process: thêm noise vào ảnh theo schedule (T steps, T=1000) → ảnh trở thành pure noise. Reverse process: UNet học dần khôi phục ảnh từ noise. Mỗi step: UNet predict noise cần remove. Training: minimize MSE giữa predicted noise và actual noise. Quality vượt trội GAN vì likelihood-based, mode coverage tốt hơn |
| **CLIP — Text-Image alignment** | [Scaler — CLIP](https://www.scaler.com/topics/deep-learning/clip-model/) | OpenAI. Train trên 400M image-text pairs từ internet. Image encoder (ViT) + Text encoder (Transformer). Contrastive learning: maximize similarity giữa matching pairs, minimize non-matching. CLIP có thể: zero-shot image classification, text-to-image retrieval, multimodal understanding. Nền tảng cho Stable Diffusion conditioning |
| **LoRA — Low-Rank Adaptation** | [HF — LoRA](https://huggingface.co/docs/peft/conceptual_guides/lora) | Full fine-tune: train tất cả params (175B = 350GB+ VRAM) → impossible. LoRA: thêm 2 low-rank matrices A (d×r) và B (r×k) song song với attention weights W. Chỉ train A và B (~0.1-5% params). Freeze phần còn lại. r=4-8 cho Stable Diffusion, r=8-64 cho LLM. QLoRA: quantization (4-bit NF4) + LoRA → fine-tune 7B model trên 1 GPU 24GB |
| **Prompt Engineering — craft prompt hiệu quả** | [Scaler — Prompt](https://www.scaler.com/topics/generative-ai/prompt-engineering/) | Zero-shot: hỏi thẳng không examples. Few-shot: cho 2-3 ví dụ trong prompt để model học pattern. Chain-of-Thought: thêm "let me think step by step" → model chia nhỏ vấn đề → reasoning tốt hơn. Constitutional AI: model self-critique. Prompt engineering là skill cần thiết khi dùng LLM |
| **ControlNet — kiểm soát generation** | [ControlNet GH](https://github.com/lllyasviel/ControlNet) | Thêm conditioning (pose, depth map, canny edges, normal map) vào diffusion model. Copy of UNet weights → 2 branches: original + control. Control branch nhận extra input (pose skeleton, depth map). Cho phép tạo ảnh với composition được kiểm soát. Ứng dụng: tạo ảnh theo pose con người, kiểm soát layout |
| **Thực hành: Fine-tune Stable Diffusion bằng DreamBooth** | [HF — DreamBooth](https://huggingface.co/docs/diffusers/training/dreambooth) | DreamBooth: personalize SD để generate ảnh của 1 subject cụ thể (ví dụ: bạn, thú cưng, sản phẩm). Training: ~100 ảnh subject + class images (regularization). Kết hợp with LoRA (DreamBooth-LoRA) để train nhanh hơn |

---

## 4.5 — LLM & Agent Systems

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **LLM — Large Language Models là gì** | [Scaler — LLM](https://www.scaler.com/topics/generative-ai/what-is-llm/) | Transformer-based models với params > 1B. Pre-trained trên text khổng lồ (internet corpus, code, books). Sau đó fine-tune cho downstream tasks. Scale law: model lớn hơn + data nhiều hơn → better performance gần như predictable. GPT-4: rumored ~1.8T params. Claude, Gemini, LLaMA, Mistral, Qwen là các LLM nổi tiếng |
| **Pretraining vs Fine-tuning vs RLHF** | [Scaler — LLM Training](https://www.scaler.com/topics/generative-ai/llm-fine-tuning/) | Pretraining: train next-token prediction trên raw text (internet). Fine-tuning: train trên task-specific data (Q&A, sentiment, instruction). RLHF: train để maximize reward model từ human preferences. SFT → Reward Model → PPO optimization → model cuối cùng. RLHF là cách ChatGPT trở nên helpful, harmless, honest |
| **Instruction Tuning — Alpaca, Vicuna** | [HF](https://huggingface.co/docs/transformers/main/en/peft) | Full fine-tune tốn quá nhiều compute. Instruction tuning: fine-tune trên instruction-response pairs (Alpaca 52K instructions từ Self-Instruct). LoRA fine-tune instruction-tuned models → affordable. Vicuna: fine-tune LLaMA trên ChatGPT conversations → 90% ChatGPT quality |
| **QLoRA — quantize + LoRA fine-tuning** | [HF — QLoRA](https://huggingface.co/blog/4bit-quantization) | 4-bit NormalFloat (NF4) quantization: chia weights thành 16 levels thay vì full precision. Độ chính xác ~16-bit nhưng chỉ tốn 4 bits. Kết hợp LoRA → chỉ train A,B matrices ở 16-bit, rest ở 4-bit. Fine-tune 7B model trên 1 GPU 24GB. Fine-tune 70B model trên 2× A100 (80GB). Công nghệ nền tảng của hầu hết open-source LLM finetuning |
| **Prompt Engineering nâng cao** | [Scaler — Advanced Prompt](https://www.scaler.com/topics/generative-ai/prompt-engineering/) | Chain-of-Thought (CoT): model chia reasoning steps → accuracy tăng đáng kể. Tree-of-Thought: explore nhiều reasoning paths. Self-consistency: sample nhiều responses → majority vote. ReAct: Reasoning + Acting (gọi tools). Automatic Prompt Engineer (APE): tự tìm optimal prompt bằng LLM. Prompt caching: reuse computed KV-cache |
| **RAG — Retrieval Augmented Generation** | [Scaler — RAG](https://www.scaler.com/topics/generative-ai/retrieval-augmented-generation/) | LLM có knowledge cutoff → không biết thông tin mới, private data. RAG giải quyết: (1) Embed user query → vector; (2) Search vector DB → top-k relevant docs; (3) Feed docs + query vào LLM → LLM trả lời dựa trên context. Chunking: chia document thành chunks (~512 tokens, overlap ~128). Embedding models: BGE, E5, multilingual-e5. Vector DB: Chroma, FAISS, Qdrant |
| **LangChain — framework cho LLM apps** | [LangChain Docs](https://python.langchain.com/docs/get_started/introduction) | Components: Prompt templates, Chains (LLMChain, RetrievalQA), Agents (ReAct, Plan-and-Execute), Memory, Tools (search, calculator, API). RAG: DocumentLoader → TextSplitter → Embeddings → VectorStore → Retriever → LLM. Agent: LLM quyết định hành động → gọi tool → observe → act again. LangGraph: stateful, multi-step agent workflows |
| **ReAct Agent — reasoning + action** | [Scaler — ReAct](https://www.scaler.com/topics/generative-ai/reasoning-agent-react/) | Loop: Thought (LLM reasoning) → Action (gọi tool) → Observation (kết quả) → repeat. Khác pure reasoning (CoT): ReAct tương tác với external world (search, calculator, code execution). Khác pure acting (Reflexion): ReAct giải thích WHY trước khi act. Hiệu quả cho multi-step tasks |
| **Tools & Function Calling** | [OpenAI — Function Calling](https://platform.openai.com/docs/guides/function-calling) | LLM chọn gọi function/tool nào khi cần. Schema định nghĩa: function name, parameters, descriptions. LLM trả về structured call (name + args) thay vì free text. Agent gọi actual function → trả kết quả → LLM tiếp tục. Đây là cách Copilot, ChatGPT Plugins hoạt động. Cần structured output + function calling để reliable |
| **MCP — Model Context Protocol** | [MCP Official](https://modelcontextprotocol.io/) | Anthropic đề xuất 2024. Giao thức chuẩn để Agent kết nối external tools/data. Thay vì hardcode mỗi integration: MCP Server cung cấp resources, tools, prompts. MCP Client (Claude Desktop, Agent) kết nối nhiều servers. Đang trở thành standard cho AI ecosystem: Slack, GitHub, Database, File system → AI có thể "plug in" vào mọi thứ |
| **Agentic AI — AI tự hành động** | [Scaler — Agentic AI](https://www.scaler.com/topics/generative-ai/agentic-ai-using-vlm/) | Agent = LLM brain + Tools + Memory + Goals. Loop: perceive → plan → act → reflect → remember. Plan-and-Execute: Planner chia task thành steps → Executor chạy từng step → Planner điều phối. Multi-agent: nhiều agents chuyên biệt (Coder, Reviewer, Tester) phối hợp. Ứng dụng: coding agent (Devin, Claude Code), research agent, autonomous operations |
| **Thực hành: RAG Chatbot với LangChain + ChromaDB** | [Scaler — RAG Project](https://www.scaler.com/topics/generative-ai/retrieval-augmented-generation/) | Build chatbot trả lời từ tài liệu riêng (PDF, Notion, website). Pipeline: PDF → DocumentLoader (PyPDF) → TextSplitter (RecursiveCharacter) → ChromaDB (embedding BGE) → RetrievalQA (chain type="stuff") → LLM (Ollama/local LLM). Kết quả: chatbot trả lời chính xác dựa trên document, kèm citation |

---

## 4.6 — Vision-Language Models (VLM)

| Topic con | Tài liệu | Mô tả chi tiết |
|---|---|---|
| **VLM — Vision Language Model là gì** | [Scaler — VLM](https://www.scaler.com/topics/deep-learning/vision-language-model/) | Model kết hợp hiểu cả hình ảnh và text. Input: ảnh + câu hỏi. Output: text answer. Thường gồm: vision encoder (ViT) + LLM (Vicuna, LLaMA). CLIP-style pretraining: contrastive learning giữa image embeddings và text embeddings. VLM đọc được screenshot, biểu đồ, ảnh chụp |
| **LLaVA — Large Language and Vision Assistant** | [HuggingFace](https://huggingface.co/models?pipeline_tag=visual-question-answering) | LLaVA 1.5: Linear projection mapping ViT features → LLM token space. Trained trên GPT-4V image-text pairs. LLaVA 1.6 (LLaVA-XT): support higher resolution, more languages. Về bản chất: 1 vision encoder + 1 projection + 1 LLM = VLM |
| **Visual Question Answering (VQA)** | [Scaler — VQA](https://www.scaler.com/topics/deep-learning/visual-question-answering/) | Task: nhìn ảnh → trả lời câu hỏi bằng text. VQA dataset (COCO): 265K images × 1M questions. Dùng VLM: encode image → fuse with question → LLM decode answer. Ứng dụng: accessibility (mô tả ảnh cho người mù), document understanding, medical imaging |
| **Image Captioning** | [Scaler — Image Caption](https://www.scaler.com/topics/deep-learning/image-captioning/) | Input: 1 ảnh. Output: câu mô tả bằng text. Encoder (CNN/ViT) → image features → Decoder (LSTM/Transformer) → sinh caption từng token. Beam search: chọn caption có highest probability thay vì greedy decode. CLIPScore đánh giá quality |
| **Agentic AI dùng VLM** | [Scaler — Visual Agent](https://www.scaler.com/topics/generative-ai/agentic-ai-using-vlm/) | VLM là "mắt" của Agent. Agent nhìn screenshot → reasoning → hành động trên UI. Ứng dụng: automation browser tasks, computer use, robotic manipulation. Claude Computer Use, GPT-4V agent, OpenAI Operator. Gần như thay thế GUI testing |
| **Thực hành: VQA Agent với LLaVA** | [HuggingFace](https://huggingface.co/models?pipeline_tag=visual-question-answering) | Dùng LLaVA 1.6 (7B params) qua Ollama hoặc transformers. Task: tự động đọc dashboard/screenshot → trả lời câu hỏi về dữ liệu trong ảnh. Kết hợp với LangChain Agent: Agent nhìn ảnh + suy nghĩ + hành động |

---

## 💻 PROJECT PHẦN 4

| # | Project | Mô tả | Dataset | Cấp |
|---|---|---|---|:---:|
| **A** | RAG Chatbot | Hỏi đáp trên dữ liệu công ty | PDF/Notion tự chọn | 🟠 |
| **B** | YOLO Custom Object Detection | Detect vật thể tự chọn | Tự thu thập + Roboflow | 🟠 |
| **C** | Vietnamese NER System | Trích xuất tên, địa chỉ, tổ chức | VLSP 2023 / UIT-VSF | 🔴 |
| **D** | Fine-tune Stable Diffusion (LoRA) | Tạo model style riêng | 50-100 ảnh style | 🔴 |
| **E** | Multi-Agent System | Planner + Researcher + Executor | LangChain + MCP + A2A | 🔴 |
| **F** | VQA Agent | Hỏi đáp trên ảnh dashboard | Tự tạo screenshots | 🔴 |

---

## ✅ CHECKPOINT PHẦN 4

- [ ] Giải thích được Self-Attention và Multi-Head Attention — tại sao cần multiple heads
- [ ] Vẽ được kiến trúc Transformer (Encoder-Decoder) và vai trò từng component
- [ ] So sánh được BERT (Encoder-only) vs GPT (Decoder-only) — khi nào dùng cái nào
- [ ] Phân biệt được Semantic Segmentation vs Instance Segmentation vs Object Detection
- [ ] Giải thích được Diffusion Model hoạt động thế nào — forward vs reverse process
- [ ] Build được RAG pipeline cơ bản (embed → retrieve → generate)
- [ ] Hiểu được LoRA tối ưu fine-tune LLM bằng cách nào
- [ ] Biết Agent là gì và cách ReAct hoạt động
- [ ] Hoàn thành ít nhất **2 trong 6 project**
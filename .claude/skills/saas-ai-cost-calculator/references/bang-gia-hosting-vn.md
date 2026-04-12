# Bảng Giá Hosting/Server tại Việt Nam — Cập nhật 2024–2025

## Mục đích
Tham khảo nhanh chi phí hosting và server khi tính chi phí SaaS AI tại Việt Nam.

## Khi nào tải
Khi user cần ước lượng chi phí vận hành server hoặc cần so sánh giá hosting VN.

---

## Hosting Chia Sẻ (Shared Hosting)

| Nhà cung cấp | Gói | RAM | SSD | Giá/tháng | Phù hợp |
|-------------|-----|-----|-----|----------|---------|
| HostVN | Starter | 1GB | 5GB | 30K VND | Landing page, API proxy |
| Z.com | Basic | 2GB | 10GB | 60K VND | Web đơn giản |
| Mat Bao | Start | 1GB | 5GB | 50K VND | Website nhỏ |
| PA Vietnam | Basic | 1GB | 5GB | 40K VND | |

> ⚠️ **Hosting chia sẻ KHÔNG phù hợp cho SaaS AI** — vì giới hạn RAM, CPU, không chạy được background process, không cài được Python backend.

---

## VPS (Virtual Private Server) — Phù hợp cho SaaS AI

| Nhà cung cấp | Gói | CPU | RAM | SSD | Giá/tháng | Phù hợp |
|-------------|-----|-----|-----|-----|----------|---------|
| Vultr | $6/mo | 1 core | 1GB | 25GB | ~150K VND | Prototype, test |
| DigitalOcean | $4/mo | 1 core | 512MB | 10GB | ~100K VND | Dev, staging |
| DigitalOcean | $6/mo | 1 core | 1GB | 25GB | ~150K VND | Production nhỏ |
| DigitalOcean | $12/mo | 2 core | 2GB | 50GB | ~300K VND | Production |
| Vultr | $20/mo | 2 core | 4GB | 55GB | ~500K VND | Production vừa |
| Linode (Akamai) | $6/mo | 1 core | 1GB | 25GB | ~150K VND | |
| Contabo | Entry | 4 core | 8GB | 200GB | ~250K VND | |

### So sánh VPS quốc tế vs Việt Nam

| Tiêu chí | VPS quốc tế (Vultr, DO) | VPS Việt Nam |
|---------|------------------------|--------------|
| Giá | Rẻ hơn (~$6–12/mo) | Cao hơn (200K–500K+) |
| Latency (VN) | Cao hơn (100–200ms) | Thấp hơn (5–20ms) |
| Thanh toán | Quốc tế (Visa, PayPal) | Chuyển khoản VN |
| Hỗ trợ | Tiếng Anh | Tiếng Việt |
| Data center | US, SG, JP | Việt Nam |

> 💡 **Khuyến nghị cho sinh viên:** Bắt đầu với Vultr/DigitalOcean $6–12/mo → rẻ, dễ setup, dùng được ngay. Khi có doanh thu → chuyển sang VPS Việt Nam để cải thiện latency.

---

## Cloud Server (Serverless / Pay-per-use)

| Nhà cung cấp | Mô hình | Giá | Phù hợp |
|-------------|---------|-----|---------|
| Render | Free tier | Miễn phí (500MB RAM) | Prototype, Flask/FastAPI |
| Railway | Pay-per-use | ~$5–20/tháng | Startup nhỏ |
| Fly.io | Free tier | Miễn phí (3 shared VMs) | Dev, test |
| Vercel | Hobby | Miễn phí | Frontend SaaS, Next.js |
| Supabase | Free tier | Miễn phí (500MB DB) | Backend + Database |
| Firebase | Spark | Miễn phí (limited) | Mobile SaaS |

> 🚀 **Free tier cho sinh viên:** Render + Vercel + Supabase = 3 dịch vụ miễn phí đủ để chạy 1 sản phẩm SaaS AI nhỏ.

---

## Database

| Dịch vụ | Gói miễn phí | Trả phí từ | Phù hợp |
|---------|-------------|-----------|---------|
| Supabase | 500MB SQL, 2GB file | ~$25/tháng | Startup |
| PlanetScale | 1GB database | ~$29/tháng | Production MySQL |
| MongoDB Atlas | 512MB | ~$9/tháng | NoSQL |
| Redis Cloud | 30MB | ~$0 | Caching |
| Neon (PostgreSQL) | 3GB | Miễn phí | Serverless Postgres |

---

## Email & Tool

| Tool | Gói | Giá/tháng | Thay thế |
|------|-----|----------|---------|
| Resend | Free | 3.000 email/tháng | SendGrid |
| Postmark | Trial | $15/10K emails | |
| Brevo (Sendinblue) | Free | 300 email/day | |
| LogSnag | Free | Miễn phí | Monitoring |
| Sentry | Free | Miễn phí | Bug tracking |
| Plausible | Free | 10K views/tháng | Analytics (privacy) |
| Umami | Self-hosted | Miễn phí | Google Analytics alternative |

---

## Mẹo Cho Sinh Viên

1. **Tháng 1–6:** Dùng Render free tier + Vercel → chi phí = 0
2. **Tháng 6–12:** Nâng lên Render $7/mo + Supabase $0 → chi phí ~$7/tháng (~175K VND)
3. **Tháng 12+:** Chuyển sang VPS $20/mo khi doanh thu ≥ 2M/tháng
4. **Tính chi phí theo user mới:**
   - Nếu 50 user trả phí → mỗi user chịu ~$0.40 chi phí server/tháng (~$10K VND)
   - Nếu 100 user → mỗi user chịu ~$0.20/tháng (~5K VND)
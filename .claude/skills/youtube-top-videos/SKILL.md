---
name: youtube-top-videos
description: >
  Tìm kiếm và phân tích các video YouTube có lượt xem và lượt đăng ký cao nhất dựa trên
  từ khóa. Sử dụng YouTube Data API v3 để truy vấn video, sắp xếp theo lượt view và
  subscriber count, trả về danh sách top video với thông tin chi tiết. Triggers: "tìm
  video YouTube nhiều view nhất", "top video YouTube về [chủ đề]", "video YouTube
  nào hot nhất", "tìm kiếm video YouTube có lượt subscribe cao", "so sánh video YouTube
  theo lượt xem", "video YouTube trending nhất", "phân tích video YouTube", "lọc
  video YouTube theo view count", "youtube top videos", "tìm video nhiều lượt xem nhất
  trên YouTube". KHÔNG dùng cho: phát video, tải video, bình luận, đăng video, thay
  đổi metadata kênh.
---

# Skill: youtube-top-videos

Tìm kiếm và phân tích các video YouTube có lượt xem và subscriber cao nhất theo từ khóa.
Dùng YouTube Data API v3 để trả về danh sách đã sắp xếp kèm thông tin chi tiết.

---

## Input

Người dùng cung cấp một trong các thông tin sau:

- **Từ khóa tìm kiếm** (bắt buộc): chủ đề, tên kênh, hoặc cụm từ cần tìm (ví dụ: "nodejs tutorial", "mèo cute")
- **Số lượng video** (tùy chọn, mặc định: 10): số lượng video muốn hiển thị (tối đa 50)
- **Sắp xếp theo** (tùy chọn, mặc định: view_count): `view_count` hoặc `relevance`

---

## Workflow

### Bước 1 — Xác thực API Key

1. Đọc biến môi trường `YOUTUBE_API_KEY` từ file `.env` trong thư mục dự án.
2. Nếu biến không tồn tại hoặc rỗng: báo lỗi và dừng, yêu cầu người dùng kiểm tra file `.env`.

### Bước 2 — Tìm kiếm video qua YouTube Search API

1. Gọi endpoint `GET https://www.googleapis.com/youtube/v3/search` với các tham số:
   - `part=snippet`
   - `q={từ_khóa}` (mã hóa URL)
   - `type=video`
   - `maxResults={số_lượng}` (mặc định 10)
   - `order={sắp_xếp}` (mặc định viewCount)
   - `relevanceLanguage=vi` (ưu tiên tiếng Việt nếu có)
2. Lưu danh sách `videoId` từ kết quả.

### Bước 3 — Lấy thống kê chi tiết qua Videos API

1. Gọi endpoint `GET https://www.googleapis.com/youtube/v3/videos` với các tham số:
   - `part=statistics,snippet`
   - `id={videoId1},{videoId2},...` (tối đa 50 video)
2. Trích xuất: `viewCount`, `likeCount`, `subscriberCount` (từ snippet channel),
   `title`, `channelTitle`, `publishedAt`, `videoId`, `description`.

### Bước 4 — Lấy thông tin kênh (subscriber count)

1. Trích danh sách `channelId` duy nhất từ kết quả Bước 3.
2. Gọi endpoint `GET https://www.googleapis.com/youtube/v3/channels` với:
   - `part=snippet,statistics`
   - `id={channelId1},{channelId2},...`
3. Map `channelId` → `subscriberCount` (lấy `statistics.subscriberCount`).

### Bước 5 — Sắp xếp và định dạng kết quả

1. Sắp xếp danh sách video theo `viewCount` giảm dần.
2. Gắn `subscriberCount` từ Bước 4 vào mỗi video.
3. Format số lớn: `viewCount` và `subscriberCount` hiển thị dạng `1.2M`, `350K`, v.v.
4. Tạo bảng markdown với các cột: `#`, `Title`, `Channel`, `Views`, `Subs`, `Likes`, `Published`, `URL`.

### Bước 6 — Tính tổng kết (summary)

Thêm phần summary cuối output:
- Tổng số video tìm được
- Tổng lượt xem trung bình
- Kênh có nhiều subscribers nhất trong kết quả
- Video có lượt xem cao nhất (liên kết YouTube)

---

## Output Format

```
## Kết quả tìm kiếm: "{từ khóa}"
Tìm thấy {N} video • Sắp xếp theo lượt xem giảm dần

| # | Title | Channel | Views | Subs | Likes | Published | URL |
|---|-------|---------|-------|------|-------|-----------|-----|
| 1 | ... | ... | ... | ... | ... | ... | https://youtu.be/... |
...

## Summary
- Tổng video: {N}
- Trung bình lượt xem: {avg}
- Top kênh: {top_channel} ({sub_count} subs)
- Video hot nhất: {title} ({view_count} views)
```

---

## Edge Cases

- **API Key không hợp lệ (401/403):** Báo "API Key không hợp lệ hoặc đã bị vô hiệu hóa. Vui lòng kiểm tra YOUTUBE_API_KEY trong file .env."
- **Không tìm thấy kết quả (0 items):** Báo "Không tìm thấy video nào cho từ khóa '{từ_khóa}'. Thử từ khóa khác."
- **API quota exceeded (429):** Báo "Đã vượt giới hạn API. Vui lòng thử lại sau ít phút." và dừng.
- **Lỗi mạng / timeout:** Báo "Không thể kết nối YouTube API. Kiểm tra kết nối internet và thử lại."
- **Video không có viewCount:** Hiển thị "N/A" thay vì số.
- **Channel không có subscriberCount:** Hiển thị "N/A" thay vì số.
- **từ khóa chứa ký tự đặc biệt:** Mã hóa URL trước khi gửi request.
- **Số lượng > 50:** Tự động giới hạn ở 50 và thông báo cho người dùng.

---

## Examples

### Example 1

**Input:** "tìm top 10 video YouTube về lập trình React"

**Expected Output:**
```
## Kết quả tìm kiếm: "React"
Tìm thấy 10 video • Sắp xếp theo lượt xem giảm dần

| # | Title | Channel | Views | Subs | Likes | Published | URL |
|---|-------|---------|-------|------|-------|-----------|-----|
| 1 | React Tutorial for Beginners | Codevolution | 2.5M | 850K | 45K | 2024-01-15 | https://youtu.be/SqcY0GlERu8 |
| 2 | React Crash Course | Traversy Media | 1.8M | 2.1M | 30K | 2023-11-20 | https://youtu.be/w7ejDZ8OCv8 |
...

## Summary
- Tổng video: 10
- Trung bình lượt xem: 1.2M
- Top kênh: Traversy Media (2.1M subs)
- Video hot nhất: React Tutorial for Beginners (2.5M views)
```

### Example 2

**Input:** "top video YouTube về mèo cute"

**Expected Output:**
```
## Kết quả tìm kiếm: "mèo cute"
Tìm thấy 10 video • Sắp xếp theo lượt xem giảm dần

| # | Title | Channel | Views | Subs | Likes | Published | URL |
|---|-------|---------|-------|------|-------|-----------|-----|
| 1 | Funny Cats Compilation | Funniest Animals | 15M | 5.2M | 200K | 2023-06-10 | https://youtu.be/abc123 |
...

## Summary
- Tổng video: 10
- Trung bình lượt xem: 8.5M
- Top kênh: Funniest Animals (5.2M subs)
- Video hot nhất: Funny Cats Compilation (15M views)
```

### Example 3

**Input:** "tìm video có nhiều view nhất về python"

**Expected Output:**
```
## Kết quả tìm kiếm: "python"
Tìm thấy 10 video • Sắp xếp theo lượt xem giảm dần

| # | Title | Channel | Views | Subs | Likes | Published | URL |
|---|-------|---------|-------|------|-------|-----------|-----|
| 1 | Python Tutorial - Full Course for Beginners | freeCodeCamp | 28M | 7.5M | 500K | 2022-01-01 | https://youtu.be/kqtD5dpn9C8 |
...
```
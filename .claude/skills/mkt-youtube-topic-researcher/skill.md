---
name: mkt-youtube-topic-researcher
description: >
  Research YouTube videos by topic/keyword — filter by views, subscriber count, and breakout ratio (views/subs).
  Kích hoạt khi người dùng nói: 'research video theo chủ đề', 'tìm video nhiều views', 'research youtube topic',
  'tìm video theo keyword', 'youtube research', 'tìm video hot theo chủ đề', 'search youtube by topic',
  'video nào nhiều views về', 'research video ideas', 'tìm video breakout theo topic', 'phân tích video theo keyword',
  'tìm video có lượt xem cao', 'phân tích video YouTube theo topic'.
  KHÔNG dùng cho: phát video, tải video, bình luận, đăng video, thay đổi metadata kênh.
---

# YouTube Topic Researcher

Tìm kiếm và phân tích video YouTube theo chủ đề/keyword. Lọc theo số views tối thiểu, tính **breakout ratio** (views ÷ subscribers) để phát hiện video overperform. Giúp nghiên cứu nội dung trước khi sản xuất video.

---

## When to Use

- User muốn research video YouTube theo một chủ đề cụ thể
- User muốn tìm video nhiều views trong một lĩnh vực
- User muốn phân tích video nào đang overperform (breakout) theo topic
- User muốn so sánh performance các video cùng chủ đề

---

## Prerequisites

1. **API Key** trong `.env`:
   ```
   YOUTUBE_API_KEY=your_key_here
   ```

2. **YouTube Data API v3** đã enable tại [Google Cloud Console](https://console.cloud.google.com/apis/library/youtube.googleapis.com)

---

## Usage

### Cú pháp

```bash
uv run .claude/skills/mkt-youtube-topic-researcher/scripts/research_topic.py "KEYWORD" [OPTIONS]
```

### Options

| Option | Mô tả | Mặc định |
|--------|--------|----------|
| `KEYWORD` | Từ khóa tìm kiếm (bắt buộc) | — |
| `--min-views` | Số views tối thiểu | 10000 |
| `--date` | Khoảng thời gian: `today`, `week`, `month`, `year` | `month` |
| `--max-results` | Số kết quả tối đa | 20 |
| `--sort` | Sắp xếp: `views`, `ratio`, `date`, `relevance` | `views` |
| `--lang` | Lọc ngôn ngữ (vd: `vi`, `en`) | không lọc |
| `--output` | Đường dẫn file output | auto: `research/youtube/topics/[slug]/videos.json` |
| `--no-save` | Chỉ in ra terminal, không lưu file | false |

### Ví dụ

```bash
# Tìm video về "claude code" nhiều views nhất tháng này
uv run .claude/skills/mkt-youtube-topic-researcher/scripts/research_topic.py "claude code"

# Tìm video AI agents, ít nhất 50K views, trong tuần
uv run .claude/skills/mkt-youtube-topic-researcher/scripts/research_topic.py "ai agents" --min-views 50000 --date week

# Sắp xếp theo breakout ratio
uv run .claude/skills/mkt-youtube-topic-researcher/scripts/research_topic.py "mcp server" --sort ratio

# Video tiếng Việt về AI
uv run .claude/skills/mkt-youtube-topic-researcher/scripts/research_topic.py "AI automation" --lang vi --min-views 5000

# Chỉ in ra terminal
uv run .claude/skills/mkt-youtube-topic-researcher/scripts/research_topic.py "vibe coding" --no-save
```

---

## Output

### Bảng tóm tắt (terminal)

Script in ra bảng tóm tắt dạng:

```
╔═══════════════════════════════════════════════════════════════════╗
║  YouTube Topic Research: "claude code"                           ║
║  Filters: min 10,000 views | month | sorted by views            ║
║  Found: 15 videos                                                ║
╚═══════════════════════════════════════════════════════════════════╝

 #  | Title                          | Channel        | Views    | Subs     | Ratio | URL
----|--------------------------------|----------------|----------|----------|-------|---------------------------
 1  | Claude Code Changed Everything | @TechGuy       | 245,000  | 50,000   | 4.9x  | youtu.be/abc123
 2  | How I Use Claude Code Daily    | @AIBuilder     | 180,000  | 120,000  | 1.5x  | youtu.be/def456
...
```

### JSON output (`videos.json`)

```json
{
  "metadata": {
    "query": "claude code",
    "date_filter": "month",
    "min_views": 10000,
    "sort_by": "views",
    "language": null,
    "searched_at": "2026-04-03T23:55:00Z",
    "total_results": 15
  },
  "videos": [
    {
      "rank": 1,
      "title": "...",
      "video_id": "abc123",
      "url": "https://www.youtube.com/watch?v=abc123",
      "channel": "TechGuy",
      "channel_id": "UC...",
      "subscriber_count": 50000,
      "view_count": 245000,
      "like_count": 8500,
      "comment_count": 320,
      "breakout_ratio": 4.9,
      "published_at": "2026-03-15T10:00:00Z",
      "duration": "PT12M30S",
      "thumbnail_url": "https://i.ytimg.com/vi/abc123/maxresdefault.jpg"
    }
  ]
}
```

### File location

`research/youtube/topics/[slug]/videos.json`

Slug được tạo từ keyword: `"claude code"` → `claude-code`

---

## API Quota

| API Call | Cost | Per Run (20 results) |
|----------|------|---------------------|
| `search.list` | 100 units | 100 units |
| `videos.list` (stats + details) | 1 unit | 1 unit (batch) |
| `channels.list` (subscriber counts) | 1 unit | ~5-10 units |
| **Total** | | **~110 units** |

Daily quota: 10,000 units → ~90 searches/ngày.

---

## Workflow khi nhận yêu cầu

### Bước 1: Xác định keyword và filters

Hỏi user nếu chưa rõ:
- Keyword/chủ đề muốn research?
- Có yêu cầu gì về minimum views không?
- Khoảng thời gian nào?

### Bước 2: Chạy script

```bash
uv run .claude/skills/mkt-youtube-topic-researcher/scripts/research_topic.py "KEYWORD" --min-views MIN --date DATE --sort SORT
```

### Bước 3: Trình bày kết quả

- Hiển thị bảng tóm tắt
- Highlight top 5 video breakout (ratio cao nhất)
- Gợi ý insights từ kết quả (patterns về title, channel size, timing)

### Bước 4: (Tùy chọn) Phân tích sâu

Nếu user muốn đi sâu hơn:
- Lấy transcript của top videos (dùng skill `youtube-transcript`)
- Phân tích content strategy (dùng skill `mkt-competitor-video-strategy-analyzer`)
- Bóc insight (dùng skill `mkt-insight-extractor`)

---

## Troubleshooting

| Lỗi | Nguyên nhân | Giải pháp |
|-----|-------------|-----------|
| `YOUTUBE_API_KEY not found` | Key chưa set | Thêm vào `.env` |
| `403 Forbidden` | API key sai hoặc quota hết | Kiểm tra Google Cloud Console |
| `No videos found` | Keyword quá specific hoặc min-views quá cao | Hạ min-views, mở rộng date range |
| `quotaExceeded` | Hết quota hàng ngày | Chờ reset (Pacific midnight) hoặc dùng key khác |

## Edge Cases

| Tình huống | Cách xử lý |
|------------|------------|
| **API Key không hợp lệ (401/403)** | Báo lỗi rõ: "API Key không hợp lệ hoặc đã bị vô hiệu hóa. Vui lòng kiểm tra YOUTUBE_API_KEY trong file .env." |
| **Không tìm thấy kết quả (0 items)** | Báo: "Không tìm thấy video nào cho từ khóa '{từ_khóa}'. Thử từ khóa khác, giảm min-views, hoặc tăng date range." |
| **API quota exceeded (429)** | Báo: "Đã vượt giới hạn API. Vui lòng thử lại sau ít phút." và dừng. Không retry ngay lập tức. |
| **Lỗi mạng / timeout** | Báo: "Không thể kết nối YouTube API. Kiểm tra kết nối internet và thử lại." |
| **Video không có viewCount** | Hiển thị "N/A" thay vì số. Vẫn hiển thị video trong kết quả. |
| **Channel không có subscriberCount** | Hiển thị "N/A" thay vì số. Breakout ratio hiển thị "N/A". |
| **Từ khóa chứa ký tự đặc biệt** | Mã hóa URL trước khi gửi request. Thay khoảng trắng bằng `+` hoặc `%20`. |
| **Số lượng yêu cầu > 50** | Tự động giới hạn ở 50. Thông báo cho user: "Giới hạn tối đa 50 video, đã cắt bớt." |
| **Script không tồn tại** | Kiểm tra xem `scripts/research_topic.py` có trong thư mục skill không. Nếu không, thông báo cho user và gợi ý cài đặt lại skill. |
| **Keyword quá ngắn (1-2 ký tự)** | Vẫn chạy, nhưng cảnh báo: "Từ khóa rất ngắn, kết quả có thể không chính xác." |
| **Date filter "today" trả về 0 kết quả** | Tự động fallback sang "week" và thông báo: "Không có video hôm nay, đã mở rộng sang tuần này." |
| **Tất cả video đều có breakout_ratio = 0** | Nguyên nhân: channel có 0 subscriber. Đánh dấu và báo: "Một số kênh không có thông tin subscriber." |

## Examples

### Example 1

**Input:** "tìm top 10 video YouTube về lập trình React, ít nhất 50K views"

**Expected Output:**
```
## Kết quả tìm kiếm: "React"
Tìm thấy 10 video • Filters: min 50,000 views | month | sorted by views

╔═══════════════════════════════════════════════════════════════════╗
║  YouTube Topic Research: "React"                                ║
║  Filters: min 50,000 views | month | sorted by views            ║
║  Found: 10 videos                                               ║
╚═══════════════════════════════════════════════════════════════════╝

 #  | Title                          | Channel        | Views    | Subs     | Ratio | URL
----|--------------------------------|----------------|----------|----------|-------|---------------------------
 1  | React Tutorial for Beginners  | Codevolution   | 2.5M     | 850K     | 2.9x  | https://youtu.be/SqcY0GlERu8
 2  | React Crash Course            | Traversy Media | 1.8M     | 2.1M     | 0.9x  | https://youtu.be/w7ejDZ8OCv8
...

## Top 5 Breakout Videos (ratio cao nhất)
 1. [Video có ratio cao nhất]
 2. [Video có ratio cao thứ 2]
...

## Insights
- Patterns: Tiêu đề dạng "X for Beginners" xuất hiện 3/10 videos
- Timing: 7/10 videos được upload trong 6 tháng gần đây
- Channel size: Mix giữa micro (50K subs) và mega (2M+ subs) đều perform tốt

Saved to: research/youtube/topics/react/videos.json
```

### Example 2

**Input:** "tìm video breakout nhiều nhất về mcp server, chỉ tiếng Việt, trên 5000 views"

**Expected Output:**
```
## Kết quả tìm kiếm: "mcp server"
Tìm thấy 8 video • Filters: min 5,000 views | month | sorted by ratio | lang: vi

╔═══════════════════════════════════════════════════════════════════╗
║  YouTube Topic Research: "mcp server"                           ║
║  Filters: min 5,000 views | month | sorted by ratio | lang: vi  ║
║  Found: 8 videos                                                ║
╚═══════════════════════════════════════════════════════════════════╝

 #  | Title                          | Channel        | Views    | Subs     | Ratio | URL
----|--------------------------------|----------------|----------|----------|-------|---------------------------
 1  | MCP Server là gì?             | AI Vietnam     | 12,000   | 3,000    | 4.0x  | https://youtu.be/xyz789
 2  | Setup MCP Server 2025          | Tech Builder  | 8,500    | 2,200    | 3.9x  | https://youtu.be/abc123
...

## Top 5 Breakout Videos (ratio cao nhất)
 1. MCP Server là gì? (4.0x) - Micro channel overperform rõ rệt
 2. Setup MCP Server 2025 (3.9x)
...

## Insights
- Angle: Giải thích khái niệm (what is) và hướng dẫn setup là 2 angle chính
- Breakout pattern: Micro channel (<5K subs) chiếm ưu thế ratio
- Content gap: Chưa có video "so sánh MCP vs alternatives" → cơ hội

Saved to: research/youtube/topics/mcp-server/videos.json
```

### Example 3

**Input:** "phân tích video youtube về vibe coding, trending tuần này"

**Expected Output:**
```
## Kết quả tìm kiếm: "vibe coding"
Tìm thấy 15 video • Filters: min 10,000 views | week | sorted by views

╔═══════════════════════════════════════════════════════════════════╗
║  YouTube Topic Research: "vibe coding"                         ║
║  Filters: min 10,000 views | week | sorted by views            ║
║  Found: 15 videos                                               ║
╚═══════════════════════════════════════════════════════════════════╝

 #  | Title                          | Channel        | Views    | Subs     | Ratio | URL
----|--------------------------------|----------------|----------|----------|-------|---------------------------
 1  | Vibe Coding Changed Everything | @TechGuy       | 245,000  | 50,000   | 4.9x  | https://youtu.be/abc123
 2  | How I Use Vibe Coding Daily    | @AIBuilder     | 180,000  | 120,000  | 1.5x  | https://youtu.be/def456
...

## Top 5 Breakout Videos (ratio cao nhất)
 1. Vibe Coding Changed Everything (4.9x)
 2. Vibe Coding với Claude Code (3.8x)
...

## Insights
- Trending rõ rệt tuần này — 3/15 videos upload trong 7 ngày
- Pattern: Tiêu đề dạng "X Changed Everything" có breakout ratio cao
- Gap: Chưa có video so sánh Vibe Coding vs truyền thống

Muốn phân tích sâu hơn với NotebookLM không? (y/n)
```

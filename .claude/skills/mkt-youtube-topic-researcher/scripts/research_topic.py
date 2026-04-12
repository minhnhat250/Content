#!/usr/bin/env python3
"""
YouTube Topic Research Script
Fetches and analyzes YouTube videos by keyword using YouTube Data API v3.
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone

# UTF-8 output for Windows compatibility
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ─── CONFIG ───────────────────────────────────────────────────────────────────
API_KEY = os.environ.get("YOUTUBE_API_KEY", "")
BASE_URL = "https://www.googleapis.com/youtube/v3"
DEFAULT_MIN_VIEWS = 10000
DEFAULT_MAX_RESULTS = 20
DEFAULT_SORT = "views"
DATE_FORMATS = ["today", "week", "month", "year"]
SORT_OPTIONS = ["views", "ratio", "date", "relevance"]

# ─── DATE HELPERS ─────────────────────────────────────────────────────────────
def get_published_after(date_filter: str) -> str:
    """Return ISO 8601 publishedAfter timestamp based on date filter."""
    now = datetime.now(timezone.utc)
    if date_filter == "today":
        delta = 0
    elif date_filter == "week":
        delta = 7
    elif date_filter == "month":
        delta = 30
    elif date_filter == "year":
        delta = 365
    else:
        delta = 30
    published_after = now - __import__("datetime").timedelta(days=delta)
    return published_after.strftime("%Y-%m-%dT%H:%M:%SZ")


def format_number(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.0f}K"
    return str(n)


def slugify(text: str) -> str:
    import re
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text)
    return text[:50]


# ─── API HELPERS ───────────────────────────────────────────────────────────────
def api_get(endpoint: str, params: dict) -> dict | None:
    params["key"] = API_KEY
    url = f"{BASE_URL}/{endpoint}?{'&'.join(f'{k}={urllib.parse.quote(str(v))}' for k, v in params.items())}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"  [ERROR] HTTP {e.code}: {e.reason}", file=sys.stderr)
        if e.code == 403:
            print("  -> Quota exceeded hoặc API key bị vô hiệu hóa.", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  [ERROR] {e}", file=sys.stderr)
        return None


def fetch_videos(
    keyword: str,
    min_views: int,
    published_after: str,
    max_results: int,
    sort: str,
    language: str | None,
) -> list[dict]:
    """Search videos and fetch stats + channel subscriber counts."""
    # Step 1: search.list
    search_params = {
        "part": "snippet",
        "q": keyword,
        "type": "video",
        "maxResults": min(max_results, 50),
        "publishedAfter": published_after,
        "order": "viewCount" if sort == "views" else "relevance",
    }
    if language:
        search_params["regionCode"] = language.upper() if len(language) == 2 else "VN"

    search_data = api_get("search", search_params)
    if not search_data or "items" not in search_data:
        return []

    items = search_data["items"]

    # Collect video IDs and channel IDs
    video_ids = [item["id"]["videoId"] for item in items]
    channel_ids = list({item["snippet"]["channelId"] for item in items})

    # Step 2: videos.list (stats)
    video_stats = {}
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        vid_data = api_get(
            "videos",
            {
                "part": "statistics,snippet,contentDetails",
                "id": ",".join(batch),
                "maxResults": len(batch),
            },
        )
        if vid_data and "items" in vid_data:
            for v in vid_data["items"]:
                video_stats[v["id"]] = {
                    "statistics": v.get("statistics", {}),
                    "snippet": v.get("snippet", {}),
                    "contentDetails": v.get("contentDetails", {}),
                }

    # Step 3: channels.list (subscriber counts)
    channel_subs = {}
    for i in range(0, len(channel_ids), 50):
        batch = channel_ids[i : i + 50]
        chan_data = api_get(
            "channels",
            {
                "part": "statistics,snippet",
                "id": ",".join(batch),
                "maxResults": len(batch),
            },
        )
        if chan_data and "items" in chan_data:
            for c in chan_data["items"]:
                cid = c["id"]
                stats = c.get("statistics", {})
                subs = int(stats.get("subscriberCount", 0)) if stats.get("subscriberCount", "0").isdigit() else 0
                channel_subs[cid] = {
                    "subscriberCount": subs,
                    "title": c.get("snippet", {}).get("title", ""),
                }

    # Step 4: Build result list
    results = []
    for item in items:
        vid = item["id"]["videoId"]
        snippet = item["snippet"]
        cid = snippet["channelId"]
        stats = video_stats.get(vid, {}).get("statistics", {})
        video_details = video_stats.get(vid, {}).get("snippet", {})
        channel_info = channel_subs.get(cid, {})

        views_str = stats.get("viewCount", "0")
        views = int(views_str) if views_str.isdigit() else 0
        subs = channel_info.get("subscriberCount", 0)
        ratio = round(views / subs, 1) if subs > 0 else 0.0

        # ── FILTERS ──
        if views < min_views:
            continue
        if subs < 500_000:
            continue

        results.append(
            {
                "rank": len(results) + 1,
                "title": snippet.get("title", ""),
                "video_id": vid,
                "url": f"https://www.youtube.com/watch?v={vid}",
                "channel": snippet.get("channelTitle", ""),
                "channel_id": cid,
                "subscriber_count": subs,
                "view_count": views,
                "like_count": int(stats.get("likeCount", 0)) if stats.get("likeCount", "0").isdigit() else 0,
                "comment_count": int(stats.get("commentCount", 0)) if stats.get("commentCount", "0").isdigit() else 0,
                "breakout_ratio": ratio,
                "published_at": snippet.get("publishedAt", ""),
                "duration": video_stats.get(vid, {})
                .get("contentDetails", {})
                .get("duration", ""),
                "thumbnail_url": f"https://i.ytimg.com/vi/{vid}/maxresdefault.jpg",
                "tags": video_details.get("tags", [])[:10],
                "channel_subscribers": subs,
            }
        )

    # Sort results
    if sort == "ratio":
        results.sort(key=lambda x: x["breakout_ratio"], reverse=True)
    elif sort == "date":
        results.sort(key=lambda x: x["published_at"], reverse=True)
    # Re-rank
    for i, r in enumerate(results):
        r["rank"] = i + 1

    return results[:max_results]


# ─── OUTPUT ───────────────────────────────────────────────────────────────────
def print_table(videos: list[dict], keyword: str, date_filter: str, min_views: int, sort: str):
    total = len(videos)
    bar = "═" * 120

    print(f"\n{bar}")
    print(f"  YouTube Topic Research: \"{keyword}\"")
    print(f"  Filters: min {format_number(min_views)} views | {date_filter} | sorted by {sort} | subs >500K | published ≥ 2026-04-01")
    print(f"  Found: {total} video(s)")
    print(bar)

    if not videos:
        print("\n  Không tìm thấy video nào phù hợp với bộ lọc.")
        print(f"  Thử: giảm min-views, mở rộng date range, hoặc bỏ lọc subscriber.\n")
        return

    # Header
    print(f"\n  {'#':>2}  {'Title':<42} {'Channel':<20} {'Views':>8} {'Subs':>8} {'Ratio':>6}  {'URL'}")
    print(f"  {'-'*2}  {'-'*42} {'-'*20} {'-'*8} {'-'*8} {'-'*6}  {'-'*30}")

    for v in videos:
        title = v["title"][:40] + ".." if len(v["title"]) > 42 else v["title"]
        channel = v["channel"][:18] + ".." if len(v["channel"]) > 20 else v["channel"]
        ratio_str = f"{v['breakout_ratio']}x"
        print(
            f"  {v['rank']:>2}. {title:<42} {channel:<20} {format_number(v['view_count']):>8} "
            f"{format_number(v['subscriber_count']):>8} {ratio_str:>6}  {v['url']}"
        )

    # Top breakout
    top_breakout = sorted(videos, key=lambda x: x["breakout_ratio"], reverse=True)[:5]
    print(f"\n  [TOP] Top 5 Breakout (ratio cao nhất):")
    for i, v in enumerate(top_breakout, 1):
        print(f"     {i}. {v['title'][:60]} — {v['breakout_ratio']}x ratio")

    print()


def save_output(videos: list[dict], keyword: str, date_filter: str, min_views: int, sort: str, output_path: str | None):
    if not videos:
        return
    slug = slugify(keyword)
    base = output_path or f"research/youtube/topics/{slug}/"
    os.makedirs(base, exist_ok=True)
    out_file = os.path.join(base, "videos.json")
    data = {
        "metadata": {
            "query": keyword,
            "date_filter": date_filter,
            "min_views": min_views,
            "sort_by": sort,
            "filters": {
                "min_subscribers": 500_000,
                "min_views": min_views,
                "published_after": "2026-04-01T00:00:00Z",
            },
            "searched_at": datetime.now(timezone.utc).isoformat(),
            "total_results": len(videos),
            "notebook_id": "aacb71f3-f0d7-469f-b6bd-1d560ebe6df1",
        },
        "videos": videos,
    }
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  [OK] Saved: {out_file}")


# ─── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="YouTube Topic Researcher")
    parser.add_argument("keyword", nargs="?", default=None, help="Từ khóa tìm kiếm")
    parser.add_argument("--min-views", type=int, default=1_000_000, help=f"Số views tối thiểu (mặc định: 1,000,000)")
    parser.add_argument("--date", default="month", choices=DATE_FORMATS, help="Khoảng thời gian")
    parser.add_argument("--max-results", type=int, default=18, help="Số kết quả tối đa (mặc định: 18)")
    parser.add_argument("--sort", default="views", choices=SORT_OPTIONS, help="Cách sắp xếp")
    parser.add_argument("--lang", default=None, help="Mã ngôn ngữ (vd: vi, en)")
    parser.add_argument("--output", default=None, help="Đường dẫn output")
    parser.add_argument("--no-save", action="store_true", help="Chỉ in ra, không lưu file")
    parser.add_argument("--published-after", default="2026-04-01", help="Ngày bắt đầu (YYYY-MM-DD)")
    args = parser.parse_args()

    if not API_KEY:
        print("❌ Lỗi: YOUTUBE_API_KEY chưa được set.", file=sys.stderr)
        print("   Thêm vào .env: YOUTUBE_API_KEY=your_key_here", file=sys.stderr)
        sys.exit(1)

    if not args.keyword:
        print("Usage: uv run research_topic.py \"keyword\" [--options]", file=sys.stderr)
        print(" Ví dụ: uv run research_topic.py \"AI 2026\" --min-views 1000000 --max-results 18", file=sys.stderr)
        sys.exit(1)

    # Luôn dùng Apr 1 2026 làm published_after
    published_after = f"{args.published_after}T00:00:00Z"

    print(f"\n[OK] Searching: \"{args.keyword}\" | min {format_number(args.min_views)} views | subs >500K | >= {args.published_after}")

    videos = fetch_videos(
        keyword=args.keyword,
        min_views=args.min_views,
        published_after=published_after,
        max_results=args.max_results,
        sort=args.sort,
        language=args.lang,
    )

    print_table(videos, args.keyword, args.date, args.min_views, args.sort)

    if not args.no_save:
        save_output(videos, args.keyword, args.date, args.min_views, args.sort, args.output)

    if videos:
        urls = [v["url"] for v in videos]
        print(f"\n📋 Video URLs (copy-paste cho NotebookLM):")
        for url in urls:
            print(f"   {url}")


if __name__ == "__main__":
    main()

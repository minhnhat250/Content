# Bảng Convert: Markdown → Notion Blocks

Dùng khi: cần convert nội dung markdown sang Notion API block format.

---

## Block Types Map

| Markdown | Notion Block Type | API JSON |
|----------|------------------|---------|
| `# Tiêu đề` | Heading 1 | `heading_1` |
| `## Tiêu đề` | Heading 2 | `heading_2` |
| `### Tiêu đề` | Heading 3 | `heading_3` |
| `**bold**` | Bold text (inline) | `annotations: { bold: true }` |
| `*italic*` | Italic text (inline) | `annotations: { italic: true }` |
| `` `code` `` | Inline code | `annotations: { code: true }` |
| ```` ```lang` ```` | Code block | `type: "code"` |
| `- item` | Bulleted list | `bulleted_list_item` |
| `1. item` | Numbered list | `numbered_list_item` |
| `> quote` | Quote block | `quote` |
| `---` | Divider | `divider` |
| `[text](url)` | Link | `a` trong rich_text |
| `text` (thường) | Paragraph | `paragraph` |

---

## Ví dụ JSON Output

### Paragraph
```json
{
  "object": "block",
  "type": "paragraph",
  "paragraph": {
    "rich_text": [
      {
        "type": "text",
        "text": { "content": "Đây là đoạn văn." }
      }
    ]
  }
}
```

### Heading 1
```json
{
  "object": "block",
  "type": "heading_1",
  "heading_1": {
    "rich_text": [
      {
        "type": "text",
        "text": { "content": "Tiêu đề chính" }
      }
    ]
  }
}
```

### Code Block
```json
{
  "object": "block",
  "type": "code",
  "code": {
    "language": "python",
    "rich_text": [
      {
        "type": "text",
        "text": { "content": "print('Hello World')" }
      }
    ]
  }
}
```

### Bulleted List Item
```json
{
  "object": "block",
  "type": "bulleted_list_item",
  "bulleted_list_item": {
    "rich_text": [
      {
        "type": "text",
        "text": { "content": "Item 1" }
      }
    ]
  }
}
```

### Quote
```json
{
  "object": "block",
  "type": "quote",
  "quote": {
    "rich_text": [
      {
        "type": "text",
        "text": { "content": "Đây là trích dẫn." }
      }
    ]
  }
}
```

### Divider
```json
{
  "object": "block",
  "type": "divider",
  "divider": {}
}
```

### Bold + Italic Inline
```json
{
  "type": "text",
  "text": { "content": "bold and italic" },
  "annotations": {
    "bold": true,
    "italic": true,
    "code": false,
    "strikethrough": false,
    "underline": false
  }
}
```

---

## Thuật toán Convert

```
Input: raw markdown string
Output: array of Notion block objects

1. Split bằng "\n\n" (các đoạn văn cách nhau bằng dòng trống)
2. Với mỗi đoạn:
   - Strip leading/trailing whitespace
   - Detect type bằng regex:
     • /^#{1,3}\s/ → heading (count # để biết level)
     • /^```/ → code block (cần handle multi-line)
     • /^- / → bulleted_list_item
     • /^[0-9]+\. / → numbered_list_item
     • /^> / → quote
     • /^---$/ → divider
     • default → paragraph
   - Convert inline formatting (bold, italic, code, links)
3. Handle consecutive list items: gộp thành list block cha
4. Return array of blocks
```

---

## Supported Languages cho Code Block

```
plain text, markdown, html, css, clojure, graphql,
json, javascript, bash, python, ruby, go, rust, java,
c, cpp, csharp, php, swift, kotlin, typescript, sql,
yaml, toml, dockerfile, csv, xml
```

---

## Giới hạn của Notion API

- **Block con (children):** Một số block types có giới hạn 100 level nested
- **Tổng blocks:** Một page có thể chứa ~2000 blocks
- **Text length:** Mỗi rich_text segment tối đa ~2000 ký tự
- **Code block:** Language phải nằm trong danh sách supported
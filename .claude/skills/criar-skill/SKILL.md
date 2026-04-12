---
name: criar-skill
description: >
  Tạo file SKILL.md hoàn chỉnh cho Claude Code từ bất kỳ workflow nào, phiên đã thực thi
  hoặc ý tưởng mới. Kích hoạt khi người dùng yêu cầu tạo, lưu, xây dựng hoặc đóng gói thành
  skill — ngay cả khi không dùng từ "skill". Triggers: "tạo một skill", "biến cái này thành
  skill", "muốn tự động hóa quy trình này", "lưu lại những gì bạn vừa làm thành skill",
  "làm skill về...", "làm sao tạo skill cho...", "/criar-skill", "biến phiên này
  thành skill", "muốn lặp lại tự động". Cũng kích hoạt cuối các phiên dài khi người dùng
  yêu cầu ghi lại những gì đã làm. KHÔNG dùng để: chạy skill có sẵn, tạo các loại file
  khác, refactor code, hoặc các tác vụ không liên quan đến xây dựng skill mới.
---

# Skill: criar-skill

Tạo file SKILL.md hoàn chỉnh từ workflow có sẵn hoặc ý tưởng mới. Chạy QA tự động, phát
hiện thông tin xác thực bị lộ, và deploy vào `~/.claude/skills/` kèm backup GitHub tùy chọn.

---

## Trước khi bắt đầu

Skill này yêu cầu:
- **Claude Code** đã cài đặt và đang chạy (`claude` trong terminal)
- Thư mục `~/.claude/skills/` đã tồn tại (Claude Code tự tạo)
- **Tùy chọn:** GitHub CLI (`gh`) đã xác thực, để backup lên GitHub
- **Tùy chọn:** 1Password CLI (`op`) đã xác thực, để bảo vệ thông tin xác thực

Nếu chưa có `~/.claude/skills/`, chạy `claude` một lần — nó sẽ tự tạo thư mục.

---

## Phát hiện Chế độ

Trước bất kỳ hành động nào, xác định chế độ dựa trên ngữ cảnh:

| Điều kiện | Chế độ |
|-----------|--------|
| Gọi không có input VÀ có lịch sử tác vụ đã thực thi trong phiên | Chế độ 1: Ghi lại Phiên |
| Input chứa các bước đánh số, bullets, hoặc từ như "trước/sau/nếu/khi" | Chế độ 2: Phân tích Workflow |
| Input là mô tả chung chung, ý tưởng hoặc ý định không có bước cụ thể | Chế độ 3: Phỏng vấn |
| Không rõ ràng | Hỏi: "Bạn muốn ghi lại những gì chúng ta đã làm trong phiên này, phân tích một workflow sắp dán vào, hay tạo thứ gì đó mới từ đầu?" |

---

## Chế độ 1: Ghi lại Phiên

**Khi nào:** Được gọi không có input sau khi thực hiện tác vụ dài trong cùng phiên.

1. Đọc toàn bộ lịch sử cuộc trò chuyện hiện tại.
2. Trích xuất ba lớp:
   - **Luồng chính:** tất cả hành động đã thực thi theo thứ tự
   - **Điểm quyết định:** các điều kiện đã xác định (vd: "NẾU đăng nhập hết hạn → gia hạn trước khi tiếp tục")
   - **Edge cases:** lỗi đã xảy ra + cách được xử lý
3. Tạo bản nháp SKILL.md theo template trong `references/skill-anatomy.md`.
4. Trình bày bản nháp: "Tôi nhận diện được các bước này. Đúng chưa? Có bước nào cần điều chỉnh trước khi tiếp tục không?"
5. Chờ xác nhận hoặc sửa đổi.
6. Sau khi xác nhận, chuyển sang **QA Tự động**.

---

## Chế độ 2: Phân tích Workflow

**Khi nào:** Người dùng dán text chứa các bước, ghi chú hoặc quy trình được mô tả.

1. Xác định cấu trúc quy trình trong text được dán.
2. Trích xuất:
   - Hành động tuần tự → phần Workflow
   - Điều kiện → các điểm quyết định trong Workflow
   - Tình huống thất bại được đề cập → Edge Cases
3. Nếu bước nào còn mơ hồ, hỏi tối đa 2 câu làm rõ trước khi tạo.
4. Tạo SKILL.md theo `references/skill-anatomy.md`.
5. Chuyển sang **QA Tự động**.

---

## Chế độ 3: Phỏng vấn

**Khi nào:** Người dùng mô tả một ý tưởng không có cấu trúc quy trình cụ thể.

### Giai đoạn 1 — Định nghĩa tác vụ
- Hỏi: "Skill này làm gì? Mô tả input và output cụ thể đi."
- Nếu câu trả lời chung chung (vd: "giúp với email"), yêu cầu: "Có thể mô tả một ví dụ cụ thể không? Cái gì vào, cái gì ra?"
- Xác nhận bằng 1 câu: "Vậy skill này nhận [X] và tạo ra [Y]. Đúng không?"
- Không tiến hành cho đến khi có xác nhận rõ ràng.

### Giai đoạn 2 — Triggers
- Hỏi: "Có 5 cách khác nhau nào bạn sẽ gõ để kích hoạt skill này?"
- Gợi ý thêm 3-5 câu mà người dùng có thể chưa đề cập.
- Hỏi: "Điều gì KHÔNG nên kích hoạt skill này? Những yêu cầu nào tương tự nhưng khác mà nó nên bỏ qua?"

### Giai đoạn 3 — Tiêu chuẩn chất lượng
- Hỏi: "Output hoàn hảo trông như thế nào? Nếu được, hãy cho một ví dụ thực tế."
- Hỏi: "Output thất bại trông như thế nào? Điều gì bạn không muốn thấy?"
- Hỏi: "Input xấu nhất hoặc thiếu nhất mà skill này có thể nhận là gì? Nó nên phản ứng ra sao?"

### Giai đoạn 4 — Xác nhận brief
Tổng hợp và trình bày:
```
Tên gợi ý: [kebab-case]
Mục đích: [1 câu]
Triggers: [danh sách]
Negative boundaries: [danh sách]
Input: [mô tả]
Output: [mô tả]
Edge cases: [danh sách]
```
Hỏi: "Đúng chưa? Có điều chỉnh trường nào trước khi tạo không?"
Sau khi xác nhận, tạo SKILL.md với `references/skill-anatomy.md` và chuyển sang **QA Tự động**.

---

## QA Tự động

Thực hiện TẤT CẢ 10 checks trước khi hiển thị SKILL.md đã tạo. Không bỏ qua bước nào.

```
□ 1. Tên theo kebab-case? (không khoảng trắng, không gạch dưới, không hoa)
□ 2. Description có 50+ từ, ngôi thứ 3, 5+ trigger phrases, negative boundaries?
□ 3. Mỗi bước trong Workflow là một hành động duy nhất, mệnh lệnh, không mơ hồ?
□ 4. Có ít nhất 2 ví dụ cụ thể với input thực → output thực?
□ 5. Edge Cases đã được cover? (input thiếu, mơ hồ, sai định dạng)
□ 6. Output Format được định nghĩa rõ ràng?
□ 7. Không ngôn ngữ chung chung? ("handle appropriately", "format nicely", "as needed" cấm)
□ 8. Negative boundaries được định nghĩa trong YAML?
□ 9. SKILL.md chứa credential, password, token hoặc API key cố định?
□ 10. Có ít nhất 2 evals chuẩn bị cho evals/evals.json? (prompt + expected_output)
```

**Score < 7:** tự động sửa các mục thất bại, không hiển thị cho người dùng.
**Score ≥ 7:** hiển thị SKILL.md kèm "QA: X/10 ✓" và liệt kê những gì có thể cải thiện.

### Nếu check 9 thất bại (phát hiện credential):

1. Chạy `op --version` để kiểm tra 1Password CLI có sẵn không.
2. **Nếu op có sẵn:**
   - Liệt kê vaults: `op vault list --format=json`
   - Nếu có hơn 1 vault: hỏi "Dùng vault nào?" và liệt kê các tùy chọn.
   - Nếu chỉ có 1 vault: dùng tự động.
   - Nếu credential đã tồn tại trong vault: thay thế trong SKILL.md bằng:
     `op item get "{TEN_ITEM}" --vault "{VAULT_CHON}" --field credential --reveal`
   - Nếu chưa có: tạo bằng `op item create --category login --vault "{VAULT_CHON}"`,
     rồi tham chiếu như trên.
3. **Nếu op không có:**
   - Lưu credential vào `.env` của dự án hiện tại (hoặc `~/.claude/.env` nếu không có dự án).
   - Thay thế trong SKILL.md bằng biến môi trường: `$TEN_CREDENTIAL`
   - Thông báo: "Đã lưu credential vào .env với tên $TEN_CREDENTIAL. Không commit file này."

---

## Trình bày và Đánh giá

Sau khi QA đạt:

1. Hiển thị SKILL.md hoàn chỉnh.
2. Hiển thị: "QA: X/10 ✓" và danh sách những gì có thể cải thiện (nếu có).
3. Hỏi: "Muốn điều chỉnh gì trước khi deploy không?"
4. Chờ xác nhận rõ ràng trước khi tiếp tục.

---

## Deploy

Sau khi SKILL.md được xác nhận:

### Deploy Claude Code

1. Tạo thư mục `~/.claude/skills/{ten-skill}/`
2. Lưu SKILL.md vào thư mục đó.
3. Tạo `evals/evals.json` với các ví dụ thu thập được trong quá trình QA (check 10):
   ```json
   {
     "skill_name": "{ten-skill}",
     "evals": [
       {
         "id": 1,
         "prompt": "{input thực từ ví dụ 1}",
         "expected_output": "{output mong đợi từ ví dụ 1}"
       },
       {
         "id": 2,
         "prompt": "{input thực từ ví dụ 2}",
         "expected_output": "{output mong đợi từ ví dụ 2}"
       }
     ]
   }
   ```
4. Xác nhận: "Đã deploy vào ~/.claude/skills/{ten}/ (SKILL.md + evals/evals.json)"

### GitHub (tùy chọn)

Hỏi: "Muốn lưu lên GitHub làm backup không?"

Nếu có:
1. Kiểm tra xác thực: `gh auth status`
   - Nếu chưa xác thực: "Chạy `gh auth login` và thử lại."
2. Hỏi: "Tên repo là gì? (vd: {TEN_NGUOI_DUNG}/skills)"
3. Kiểm tra repo có tồn tại không: `gh repo view {REPO}`
   - Nếu không: `gh repo create {REPO} --public`
4. Tạo SKILL-publico.md: copy SKILL.md xóa:
   - Đường dẫn tuyệt đối nội bộ (vd: `~/.claude/`, `/root/...`)
   - Tham chiếu đến vault hoặc credential cụ thể
   - Logic deploy đặc thù của môi trường
   - Bất kỳ đề cập đến ngữ cảnh cá nhân (tên người, team nội bộ)
   Giữ nguyên: workflow, edge cases, QA checklist, ví dụ, logic của skill.
5. Upload SKILL-publico.md (không phải SKILL.md nội bộ) + evals/evals.json.
6. Commit và push với message: `feat: add {ten} skill`
7. Xác nhận kèm URL file trên GitHub.

---

## Tinh chỉnh Sau Deploy

**Một skill đã deploy không phải là skill hoàn chỉnh. Nó cần được kiểm tra.**

Sau khi deploy, chạy skill với một input thực. Khi có lỗi, đừng bỏ — sửa hướng dẫn trong SKILL.md và test lại. Skills cải thiện qua việc sử dụng.

Hướng dẫn tinh chỉnh đầy đủ với ví dụ thực tế: `references/guia-refinamento.md`

---

## Cấu trúc Skill — 4 Cấp Độ

Mỗi skill có thể được xây dựng ở 4 cấp độ phức tạp khác nhau. Chọn cấp phù hợp dựa trên yêu cầu:

| Cấp độ | Cấu trúc | Khi nào dùng | Ví dụ |
|--------|----------|---------------|-------|
| **Simple** | Chỉ SKILL.md | Một tác vụ duy nhất, không biến thể | Skill format text |
| **Standard** | SKILL.md + workflows/ | Nhiều cách làm cùng mục tiêu | Research skill có quick/deep |
| **Advanced** | SKILL.md + workflows/ + references/ | Cần template hoặc hướng dẫn chi tiết | Content skill có voice guide |
| **Full** | SKILL.md + workflows/ + references/ + scripts/ | Cần script Python/bash tự động | Publishing skill gọi social API |

### Simple Skill

```
.claude/skills/[ten-skill]/
└── SKILL.md
```

### Standard Skill

```
.claude/skills/[ten-skill]/
├── SKILL.md
└── workflows/
    ├── nhanh.md
    └── chi-tiet.md
```

### Advanced Skill

```
.claude/skills/[ten-skill]/
├── SKILL.md
├── workflows/
│   ├── nhanh.md
│   └── chi-tiet.md
└── references/
    ├── template.md
    └── huong-dan.md
```

### Full Skill

```
.claude/skills/[ten-skill]/
├── SKILL.md
├── workflows/
│   ├── nhanh.md
│   └── chi-tiet.md
├── references/
│   └── template.md
└── scripts/
    ├── xu-ly.py
    └── fetch.py
```

### Quy tắc thư mục

| Thư mục | Mục đích | Tải khi nào |
|---------|----------|-------------|
| **SKILL.md** | Điểm vào, định tuyến, tổng quan | Skill được kích hoạt |
| **workflows/** | Hướng dẫn từng bước cho tác vụ cụ thể | Cần workflow cụ thể |
| **references/** | Template, hướng dẫn, ví dụ để follow | Tải vào context khi cần |
| **scripts/** | Script Python/bash để thực thi (KHÔNG tải vào context) | Gọi qua Bash tool |

**Sự khác biệt quan trọng:**
- `references/` = Tải vào context của Claude (tốn tokens)
- `scripts/` = Claude thực thi, không tải vào context (không tốn tokens)

---

## Template SKILL.md

Khi tạo skill mới, dùng template này làm nền:

```markdown
---
name: ten-skill
description: >
  Mô tả skill làm gì. Kích hoạt khi người dùng nói: 'câu trigger 1',
  'câu trigger 2', 'câu trigger 3', 'câu trigger 4', 'câu trigger 5'.
  KHÔNG dùng cho: [negative boundaries].
---

# Skill Name

Mô tả ngắn gọn thành công mà skill mang lại.

---

## Khi nào dùng

- User nói "[trigger 1]"
- User nói "[trigger 2]"
- User muốn [kết quả]

---

## Workflow Routing

| Workflow | Khi nào dùng |
|----------|-------------|
| `workflows/nhanh.md` | Cần overview nhanh |
| `workflows/chi-tiet.md` | Cần phân tích đầy đủ |

---

## Output

**Loại:** [content/research/data/export]
**Vị trí:** `[đường_dẫn]/[dự_an]/`
**Files tạo ra:**
- `[ten_file].md` - [mô tả]

---

## Quick Process (nếu chỉ có 1 workflow)

### Bước 1: [Hành động]
[Hướng dẫn chi tiết — tập trung vào TƯ DUY, không chỉ hành động]

**Tại sao:** [Giải thích tại sao bước này quan trọng]

### Bước 2: [Hành động]
[Hướng dẫn chi tiết]

---

## Tiêu chí Chất lượng

Output TỐT vs XẤU khác nhau ở đâu:
- [Tiêu chí 1]
- [Tiêu chí 2]
- [Tiêu chí 3]

---

## References (nếu có)

- `references/template.md` - Template để follow
- `references/huong-dan.md` - Hướng dẫn chi tiết

---

## Scripts (nếu có)

- `scripts/xu-ly.py` - Chạy qua: `python .claude/skills/[ten-skill]/scripts/xu-ly.py`
```

---

## Template Workflow

Tạo trong `workflows/[ten-workflow].md`:

```markdown
# Tên Workflow

## Mục đích
Workflow này đạt được gì.

## Khi nào dùng
- User nói "[trigger cụ thể]"
- Điều kiện cần workflow này

## Điều kiện trước
Cần gì có sẵn trước khi bắt đầu (files, data, etc.)

## Các bước

### Bước 1: [Hành động]
[Hướng dẫn chi tiết — tập trung vào TƯ DUY, không chỉ hành động]

**Tại sao:** [Tại sao bước này quan trọng]

### Bước 2: [Hành động]
[Hướng dẫn chi tiết]

### Bước 3: [Hành động]
[Hướng dẫn chi tiết]

## Output
Workflow này tạo ra gì:
- `[ten_file]` - [mô tả]

## Kiểm tra Chất lượng
Trước khi hoàn thành, verify:
- [ ] [Tiêu chí 1]
- [ ] [Tiêu chí 2]
```

---

## Template Reference

Tạo trong `references/[ten-reference].md`:

```markdown
# Tên Reference

## Mục đích
Reference này cung cấp gì.

## Khi nào tải
Tải reference này khi [điều kiện].

---
[Nội dung: templates, ví dụ, hướng dẫn, etc.]
```

---

## Quy tắc YAML Frontmatter

**Các trường bắt buộc:**
- `name` — phải trùng với tên thư mục, chữ thường, gạch nối
- `description` — phải có "Kích hoạt khi người dùng nói:" kèm 5-8 trigger phrases

**Các trường tùy chọn:**
- `allowed-tools` — pre-approve tool cụ thể
- `model` — override model (haiku, sonnet, opus)

**Hướng dẫn viết trigger phrases:**
- Bao gồm các biến thể động từ (research/analyze/find/look up)
- Bao gồm cả cách hỏi trực tiếp và gián tiếp
- Bao gồm cả yêu cầu hướng kết quả
- Nghĩ: "5 người khác nhau sẽ hỏi điều này thế nào?"

**Ví dụ YAML đúng:**
```yaml
---
name: youtube-research
description: >
  Research video và channel YouTube. Kích hoạt khi người dùng nói:
  'research video này', 'phân tích channel', 'youtube research', 'tìm video về',
  'ai là ai', 'xem thông tin channel này', 'phân tích đối thủ youtube',
  'những video nào đang perform tốt'.
  KHÔNG dùng cho: phát video, tải video, bình luận, đăng video.
---
```

---

## Các Lỗi Thường Gặp

Tránh những lỗi sau khi tạo skill:

1. **Quá ít triggers** — Cần 5-8 biến thể, không chỉ 2-3
2. **Triggers chung chung** — "do research" là quá mơ hồ; "research youtube competitors" là cụ thể
3. **Không có cấu trúc output** — Luôn định nghĩa file đi đâu
4. **Bước không có tư duy** — Nắm bắt TẠI SAO mỗi bước quan trọng, không chỉ hành động
5. **Tên không khớp** — Tên thư mục phải trùng với `name` trong YAML
6. **Sai cấp độ architecture** — Đừng phức tạp hóa skill đơn giản; đừng đơn giản hóa skill phức tạp
7. **Scripts trong references** — Scripts phải đặt trong `scripts/`, không phải `references/`
8. **Quên cập nhật CLAUDE.md** — Luôn cập nhật routing table sau khi tạo skill

---

## Checklist Tạo Skill

Trước khi hoàn thành skill, verify:

- [ ] Tên trùng với tên thư mục (chữ thường, gạch nối)
- [ ] Description có 5-8 trigger phrases
- [ ] Trigger phrases cover các cách hỏi khác nhau
- [ ] Đã chọn đúng cấp độ architecture (simple/standard/advanced/full)
- [ ] Vị trí output theo tổ chức CLAUDE.md
- [ ] Process nắm bắt expertise, không chỉ các bước
- [ ] Tiêu chí chất lượng được định nghĩa
- [ ] Routing table cho các workflows (nếu có nhiều workflows)
- [ ] References được ghi chú (nếu dùng references/)
- [ ] Scripts được ghi chú với câu lệnh chạy (nếu dùng scripts/)

---

## Edge Cases

- **Chế độ 1 không có lịch sử phù hợp:** "Không tìm thấy workflow nào đã thực thi trong phiên này. Bạn muốn dán một quy trình hay tạo thứ gì đó mới từ đầu?"
- **Skill trùng tên:** "Đã có skill tên {ten}. Bạn muốn ghi đè, đổi tên hay hủy?"
- **Workflow hơn 50 bước:** Gợi ý chia thành 2-3 skill nhỏ hơn trước khi tạo. Trình bày cách chia.
- **Người dùng hủy giữa chừng:** Tạo thư mục `~/.claude/skills/criar-skill/drafts/` nếu chưa có, lưu brief tạm vào `drafts/{ten}-draft.md` và thông báo đường dẫn.
- **GitHub chưa xác thực gh CLI:** "gh CLI chưa xác thực. Chạy `gh auth login` và thử lại."
- **op CLI có sẵn nhưng chưa xác thực:** "1Password CLI có sẵn nhưng chưa đăng nhập. Chạy `op signin` hoặc dùng .env thay thế."

---

## Ví dụ

### Ví dụ 1 — Ghi lại Phiên

**Ngữ cảnh:** Vừa thực hiện xong workflow xuất hóa đơn tại quận.
**Input:** `/criar-skill` (không có text thêm)

**Output mong đợi:**
```
Tôi nhận diện được các bước sau trong phiên:

## Workflow
1. Truy cập cổng thông tin quận
2. NẾU phiên hết hạn → đăng nhập trước khi tiếp tục
3. Nhấn "Xuất hóa đơn"
4. Điền các trường: người mua (MST), dịch vụ (mã), số tiền, mô tả
5. Xác nhận xuất → chờ xử lý (5-10 giây)
6. Tải file PDF đã tạo

## Edge Cases đã xác định
- Nếu cổng trả lỗi 503: chờ 30s rồi thử lại
- Nếu MST người mua không tìm thấy: kiểm tra đăng ký trong hệ thống trước khi xuất

Đúng chưa? Có bước nào cần điều chỉnh trước khi tiếp tục không?
```

### Ví dụ 2 — Chế độ Phỏng vấn (ý tưởng chung chung)

**Input:** "tôi muốn tạo skill giúp tôi trả lời bình luận trên Instagram"

**Output mong đợi (Giai đoạn 1):**
```
Tôi hiểu bạn muốn tự động hóa việc trả lời bình luận trên Instagram.

Để tạo skill đúng, tôi cần biết cái gì vào và cái gì ra.

Cái vào: bạn dán bình luận vào đây và tôi gợi ý trả lời?
Hay bạn muốn tôi truy cập Instagram trực tiếp và trả lời?
```

### Ví dụ 3 — Chế độ Phân tích Workflow

**Input:** "mỗi tuần tôi: 1) vào notion, 2) lấy các card đánh dấu 'xuất bản', 3) export text, 4) format cho linkedin, 5) đặt lịch trên buffer"

**Output mong đợi:**
```
Tôi nhận diện được workflow xuất bản hàng tuần với 5 bước.

Trước khi tạo, 2 câu hỏi nhanh:

1. Ở bước 4 (format cho LinkedIn): bạn có quy tắc format cụ thể nào không? (vd: kích thước tối đa, emoji, cấu trúc đoạn văn)
2. Việc đặt lịch trên Buffer là thủ công hay bạn muốn skill gọi API tự động?
```

# Video YouTube — agy đọc hiểu từng video

Danh sách video lấy từ [report.md](report.md) (01–12), cộng video 13 do người dùng bổ sung. Mỗi video có một file phân tích `NN-<videoId>.md`,
do `agy` (Gemini 3.8 Flash High) viết dựa trên transcript. Thực hiện ngày 2026-10-13.

## Kết luận: agy có đọc hiểu được video không?

- **Đưa thẳng URL YouTube thì không.** YouTube chặn bằng trang "Sign in to confirm you're not a bot".
  agy tự thừa nhận là không truy cập được, chỉ dựa vào metadata, kết quả tìm kiếm và repo đi kèm,
  và từ chối bịa timestamp. Như vậy agy trung thực, nhưng không "xem" được video.
- **Có transcript thì đọc hiểu tốt.** Quy trình: tải transcript bằng `youtube-transcript-api`, rồi để agy đọc file.
  - **65/65 trích dẫn nguyên văn** có thật trong transcript. Khoảng 62/65 timestamp lệch dưới 15 giây,
    vài cái lệch khoảng 2 phút. Kết quả: [quote-check.json](quote-check.json).
  - Kiểm tra ngẫu nhiên các con số trong tóm tắt (vd. video 04: "validation chiếm 40%" ở [12:36],
    "tiết kiệm 50% token" ở [17:17]) đều khớp transcript.
  - Mỗi video mất khoảng 30–60 giây và 40K–150K token.
- **Giới hạn**: agy chỉ đọc lời nói. Những gì chỉ hiện trên màn hình (slide, code, diagram) không có trong transcript.
  Transcript là phụ đề tự động nên có lỗi nghe nhầm, vd. "clot code" thay cho "Claude Code" (video 12).

## Danh sách

| # | Video | Kênh | Dài | Điểm agy* | File |
|---|---|---|---|---|---|
| 01 | Build Your Own AI Software Factory with Claude Code | ZazenCodes | 27' | 3.5 | [01-ctoaIC4LHmI.md](01-ctoaIC4LHmI.md) |
| 02 | I Built A Claude DevOps Agent To Run My Software Factory | Owain Lewis | 16' | 4 | [02-l6GpUvPOVpM.md](02-l6GpUvPOVpM.md) |
| 03 | Build an agentic software factory: deep dive | Steve (Builder.io) | 17' | 4 | [03-pNmfMi-yjZk.md](03-pNmfMi-yjZk.md) |
| 04 | What It Actually Takes to Build a Software Factory | AI Engineer (Factory) | 22' | 3.5 | [04-vGCJ7diEtrw.md](04-vGCJ7diEtrw.md) |
| 05 | Inside OpenAI's Agentic Software Factory | Owain Lewis | 10' | 4.2 | [05-yhLDivVIamQ.md](05-yhLDivVIamQ.md) |
| 06 | Building a Software Factory that actually works (Full Course) | Greg Isenberg | 31' | 4.5 | [06-_LCeJZFIsd4.md](06-_LCeJZFIsd4.md) |
| 07 | I Built A Self-Improving AI Software Factory | Owain Lewis | 14' | 4 | [07-ZDOTYfJBuLw.md](07-ZDOTYfJBuLw.md) |
| 08 | How to Build a Software Factory for AI Coding Agents | Boundary & HumanLayer | 70' | 4.5 | [08-tGbjIvvYuHE.md](08-tGbjIvvYuHE.md) |
| 09 | Google Antigravity Agent Teams | AI Stack Engineer | 8' | 3 | [09-Eyobn1yUfN0.md](09-Eyobn1yUfN0.md) |
| 10 | I Built an Agentic Software Factory with Codex and Claude Code | Owain Lewis | 20' | 4 | [10-AbpyqAfxZ8c.md](10-AbpyqAfxZ8c.md) |
| 11 | My Super Simple Software Factory (For Agentic Engineers) | IndyDevDan | 29' | 4 | [11-haUfb1ievTE.md](11-haUfb1ievTE.md) |
| 12 | Học Claude Code từ con số 0 → Sub-Agents & Automation | Thanh Trần - 5 Phút AI | 130' | 4.5 | [12-g-ZtK5u-iiw.md](12-g-ZtK5u-iiw.md) |
| 13 | Every Claude Code Skill I Use to Drive My Entire Development Process | Cole Medin | 23' | 4.5 | [13-MbiMwgbGdxw.md](13-MbiMwgbGdxw.md) † |

† Transcript của video 13 **không phải phụ đề YouTube**. Khi tải video này, YouTube đã chặn IP của máy
(`IpBlocked`), và cả `yt-dlp` lẫn bảng "Bản chép lời" trong trình duyệt đều trống. Vì vậy transcript được lấy bằng cách
gắn video vào **AI Studio (Gemini 3.1 Pro, ~142K token)** qua Chrome, nhờ model chép nguyên văn kèm [mm:ss]
(383 dòng, 00:00–23:02). Câu chữ có thể khác phụ đề gốc một chút. Gemini app (gemini.google.com) đã từ chối chép transcript đầy đủ.

\* Điểm hữu ích cho team 3–10 kỹ sư (thang 1–5) do agy tự chấm. Đây là ý kiến của model, chưa được kiểm chứng.

## Cấu trúc thư mục

- `quote-check.json`: kết quả đối chiếu trích dẫn với transcript (65/65 khớp)
- **Transcript và log JSON của agy không lưu trong repo**, vì là nội dung có bản quyền của tác giả video và để repo gọn.
  Khi cần, tải lại bằng `scripts/fetch_tr.py` (v01–v12) vào `transcripts/`. Riêng v13 phải lấy lại qua AI Studio (xem chú thích † ở trên).
- `scripts/fetch_tr.py`: tải transcript · `scripts/agy_video.sh`: chạy agy cho 1 video · `scripts/verify.py`: đối chiếu trích dẫn
- `videos.tsv`: danh sách video (số thứ tự, id, tiêu đề, kênh)

## Chạy lại

```bash
python3 -m venv .venv && .venv/bin/pip install youtube-transcript-api
.venv/bin/python scripts/fetch_tr.py transcripts <videoId> ...
tr '\t\n' '\0\0' < videos.tsv | xargs -0 -n4 -P4 scripts/agy_video.sh   # 4 video song song
python3 scripts/verify.py "$PWD"
```

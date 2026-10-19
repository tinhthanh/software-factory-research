# Research Brief — Round 3: Template tài liệu phát triển phần mềm — chọn best practice

Ngày: 2026-10-19. Bối cảnh: một team 3–10 kỹ sư, làm việc cùng AI coding agent, muốn một bộ tài liệu tối thiểu,
theo kiểu docs-as-code (nằm trong repo, review qua PR). Nhiệm vụ: với MỖI loại tài liệu dưới đây, tìm các
template/chuẩn/thực hành đã được dùng rộng rãi, so sánh, và CHỌN best practice phù hợp team nhỏ.

Trả lời bằng **tiếng Việt**, Markdown. Mỗi khẳng định quan trọng kèm nguồn (URL) và năm. Không bịa URL; nếu không chắc
ghi "(chưa xác minh URL)". Đánh dấu `(suy luận)` nếu là ý kiến không có nguồn. Ưu tiên nguồn gốc (repo template chính chủ,
tài liệu chuẩn, handbook kỹ thuật của công ty, paper) hơn bài tổng hợp.

## Các loại tài liệu (D1–D10)
- D1. README dự án
- D2. File hướng dẫn cho AI agent (AGENTS.md / CLAUDE.md / rules)
- D3. Tài liệu kiến trúc tổng quan (vd. arc42, C4, …)
- D4. ADR — Architecture Decision Record (vd. Nygard, MADR, Y-statement, …)
- D5. API contract & quy ước API (OpenAPI, style guide …)
- D6. Spec / design doc / RFC cho một feature (vd. Google design doc, RFC/KEP, spec-driven tools …)
- D7. Test strategy + Definition of Done
- D8. Pull request template
- D9. Runbook + postmortem (vd. Google SRE, PagerDuty, …)
- D10. Chính sách bảo mật + sử dụng AI agent (SECURITY.md, AI usage policy …)
- D11. (Tuỳ chọn) Loại tài liệu nào team nhỏ THƯỜNG THIẾU mà nên có? Loại nào trong D1–D10 KHÔNG đáng làm?

## Với mỗi D1–D10, trả lời theo đúng cấu trúc
1. **Các ứng viên** (2–4 template/chuẩn), mỗi cái: nguồn, mức độ phổ biến/adoption (có dẫn chứng), ưu/nhược.
2. **Chọn**: template nền khuyến nghị cho team 3–10 người + lý do.
3. **Các mục bắt buộc** (danh sách ngắn, tên mục cụ thể) và **mục tuỳ chọn**.
4. **Độ dài / mức chi tiết** hợp lý.
5. **Anti-pattern** (điều nên tránh) — có dẫn chứng nếu được.
6. **Khác biệt khi có AI agent** (agent đọc/viết tài liệu này thế nào; điều gì cần đổi).

## Định dạng đầu ra
- `## D1` … `## D11` theo thứ tự.
- `## Top 10 kết luận` — 10 câu ngắn.
- `## Bảng chọn cuối` — bảng 1 dòng/loại tài liệu: Loại | Template nền chọn | 3–6 mục bắt buộc | Độ dài.
- `## Điều chưa chắc`
- `## Nguồn` — URL kèm năm.
- Độ dài mục tiêu: 3500–6000 từ.

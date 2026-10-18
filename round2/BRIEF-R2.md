# Research Brief — Round 2: AI Software Factory (multi-agent) cho team phát triển

Ngày: 2026-10-18. Bối cảnh: một team 3–10 kỹ sư muốn vận hành "software factory" — quy trình
phát triển phần mềm trong đó con người làm việc cùng NHIỀU AI coding agent. Round này đào sâu
**bằng chứng mới, case study thực chiến và các câu hỏi còn tranh cãi**, không khảo sát thị trường tràn lan.

Trả lời bằng **tiếng Việt**, Markdown. Mỗi khẳng định quan trọng đánh số `[C1]`, `[C2]`…
kèm nguồn (URL) **và tháng/năm của nguồn**. Đánh dấu `(suy luận)` nếu là ý kiến không có nguồn.
**Ưu tiên nguồn từ 04/2026 đến 10/2026**; nguồn cũ hơn chỉ dùng làm bối cảnh và phải ghi rõ năm.
Với số liệu: nêu phương pháp, cỡ mẫu, ai công bố, tự báo cáo hay đo độc lập. Không bịa URL —
nếu không chắc URL đúng thì ghi "(chưa xác minh URL)".

## R1. Cái gì mới trong 6 tháng qua
Sản phẩm, tính năng, practice mới cho multi-agent coding (cloud/background agent, nền tảng
điều phối agent, công cụ spec-driven, review bot, agent trong CI…). Thay đổi nào thực sự làm
thay đổi cách vận hành một software factory, thay đổi nào chỉ là marketing?

## R2. Bằng chứng định lượng mới
Năng suất (RCT, nghiên cứu METR, DORA 2026, Faros, nghiên cứu học thuật), chất lượng
(defect, code churn, lỗ hổng bảo mật trong code AI), tải review của người. Có số liệu nào
mâu thuẫn nhau không? Số liệu nào đáng tin nhất, vì sao?

## R3. Case study thực chiến
Ít nhất 5 tổ chức đã công bố cách họ vận hành coding agent ở quy mô team/công ty: quy trình,
vai trò, gate, công cụ, số đo, bài học, thất bại. Ưu tiên bài blog kỹ thuật / talk có chi tiết
hơn là thông cáo báo chí.

## R4. Ba câu hỏi còn tranh cãi
a. **Auto-merge PR do agent tạo** cho thay đổi rủi ro thấp: ai đang làm, điều kiện/danh mục nào,
   kết quả ra sao, sự cố nào đã xảy ra?
b. **Mức song song hợp lý** (số agent đồng thời mỗi kỹ sư): có dữ liệu nào ngoài giai thoại không?
   Điều gì giới hạn: review, conflict, chi phí, sự chú ý?
c. **Agent chạy trên máy dev hay sandbox/cloud**: trade-off về kiểm chứng (cần môi trường thật)
   so với bảo mật; các team giải quyết thế nào?

## R5. Context engineering
Bằng chứng (nghiên cứu, thí nghiệm) về hiệu quả của file context repo (AGENTS.md, CLAUDE.md…):
độ dài, nội dung nên có/không nên có; skills, memory, spec làm nguồn sự thật, MCP. Khuyến nghị
nào có dữ liệu ủng hộ, khuyến nghị nào chỉ là thói quen?

## R6. Bảo mật & governance
Sự cố thực tế 2025–2026 liên quan coding agent (prompt injection, supply chain qua agent/MCP,
lộ secrets, phá dữ liệu). Framework kiểm soát (OWASP cho agentic AI, NIST, quy định…).
Audit trail, phân quyền, tuân thủ cho code do agent viết.

## R7. Kinh tế
Chi phí thực tế (cost/PR, cost/kỹ sư/tháng, giá model), cách team đặt ngân sách và đo ROI;
khi nào thêm agent/song song không còn đáng tiền.

## R8. Con người & tổ chức
Thay đổi về tuyển dụng, vai trò junior, cấu trúc team, đào tạo kỹ năng, kiệt sức/review fatigue,
quyền sở hữu code. Dẫn chứng.

## Định dạng đầu ra
- `## R1` … `## R8` theo đúng thứ tự trên.
- `## Top 10 kết luận` — 10 câu khẳng định ngắn, mỗi câu 1 dòng, đánh số.
- `## Điều tôi không tìm được / còn chưa chắc` — liệt kê ngắn.
- `## Nguồn` — danh sách URL đã dùng, kèm tháng/năm.
- Độ dài mục tiêu: 3000–5000 từ.

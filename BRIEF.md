# Research Brief — AI Software Factory (multi-agent) cho team phát triển

Ngày: 2026-10-13. Mục tiêu: thiết kế **quy trình phát triển phần mềm cho một team kỹ sư**
làm việc cùng NHIỀU AI coding agent ("software factory"). Không cần khảo sát thị trường
tràn lan — chỉ dẫn chứng framework/sản phẩm khi nó minh hoạ một practice cụ thể.

Trả lời bằng **tiếng Việt**, Markdown. Mỗi khẳng định quan trọng đánh số `[C1]`, `[C2]`…
và kèm nguồn (URL) khi có. Đánh dấu `(suy luận)` nếu là ý kiến không có nguồn.
Ưu tiên nguồn 2025–2026 (blog kỹ thuật của Anthropic, OpenAI, Google, GitHub, Factory.ai,
Cognition, Thoughtworks, Martin Fowler, DORA, paper arXiv, kinh nghiệm thực tế của các team).

## Q1. Quy trình & vai trò
1. Các mô hình quy trình đang nổi: spec-driven development, plan→implement→verify,
   "agent as junior dev", ticket→PR tự động, background/async agents… So sánh ngắn.
2. Vòng đời một tính năng trong software factory: từ ý tưởng → spec → task breakdown →
   implement song song → review → test → merge → deploy. Ở mỗi bước: AI làm gì, người làm gì,
   artifact đầu ra là gì, gate (điều kiện qua cửa) là gì.
3. Vai trò của con người thay đổi thế nào (PM, tech lead, dev, QA, reviewer).
   Vai trò agent nên chia ra sao (planner, coder, reviewer, tester, docs…) — chia vai có thực sự
   giúp ích hay một agent mạnh + công cụ tốt là đủ? Dẫn chứng.
4. Human-in-the-loop: đặt checkpoint ở đâu, granularity của task giao cho agent bao nhiêu là vừa.

## Q2. Kiến trúc điều phối
1. Các pattern điều phối: orchestrator-worker, pipeline, debate/critic, swarm, best-of-N.
   Khi nào dùng cái nào.
2. Cô lập môi trường: git worktree, container/sandbox, ephemeral environment; quản lý xung đột
   khi nhiều agent sửa cùng codebase.
3. Context engineering: tài liệu repo cho agent (CLAUDE.md/AGENTS.md…), memory, spec làm nguồn
   sự thật, chia nhỏ context, MCP/tools.
4. Chi phí & throughput: token cost, giới hạn song song hợp lý, khi nào song song phản tác dụng.

## Q3. Chất lượng & rủi ro
1. Verification: test tự động, agent tự review, review chéo giữa model khác nhau, CI gate,
   eval nội bộ. Benchmark công khai (SWE-bench Verified/Pro, Terminal-bench…) nói gì và giới hạn.
2. Failure modes thường gặp của multi-agent coding (lan truyền lỗi, reward hacking test,
   drift khỏi spec, code bloat, review fatigue của người) và cách giảm.
3. Bảo mật: prompt injection, secrets, quyền của agent, supply chain, sandbox.
4. Metrics đo hiệu quả factory (DORA, throughput PR, defect escape rate, % PR agent merge được,
   cost/PR…). Dữ liệu thực tế (vd. nghiên cứu METR, DORA 2025, báo cáo các công ty).

## Q4. Khuyến nghị
Đề xuất một quy trình cụ thể (5–10 bước) cho một team 3–10 kỹ sư bắt đầu vận hành
software factory trong 3 tháng: lộ trình áp dụng theo giai đoạn, công cụ tối thiểu,
rủi ro chính cần chặn.

## Định dạng đầu ra
- `## Q1` … `## Q4` theo đúng thứ tự trên.
- Cuối cùng: `## Top 10 kết luận` — 10 câu khẳng định ngắn, mỗi câu 1 dòng, đánh số.
- `## Nguồn` — danh sách URL đã dùng.
- Độ dài mục tiêu: 2500–4500 từ.

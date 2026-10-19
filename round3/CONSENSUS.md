# Round 3: chọn best practice cho template tài liệu

Ngày: 2026-10-19. Đầu vào: [BRIEF-R3.md](BRIEF-R3.md). Kết quả áp dụng vào: [../templates/](../templates/).

## Nguồn được chấm

| Mã | Agent | Lăng kính chọn nguồn | URL | 404 |
|---|---|---|---|---|
| claude-T1 | Claude subagent | Handbook công ty và dự án OSS lớn (Google, GitLab, Oxide, Rust/K8s, PagerDuty…) | 54 | 0 |
| claude-T2 | Claude subagent | Chuẩn và framework (arc42, C4, ISO, MADR, OpenAPI, Scrum, NIST, OpenSSF…) | 56 | 0 |
| claude-T3 | Claude subagent | Tài liệu thời AI agent (agents.md, CLAUDE.md, spec-kit, Kiro, chính sách AI của OSS…) | 56 | 0 |
| claude-T4 | Claude subagent | Thực hành team nhỏ và phản biện (doc rot, nghiên cứu MSR/ICSE, cái gì không đáng làm) | 59 | 0 |
| agy-argon | `agy` Gemini 4 Argon (High) | Không chỉ định | 69 | 2 |
| agy-flash | `agy` Gemini 3.8 Flash (High) | Không chỉ định | 41 | 2 |

Các agent chạy song song và cô lập: không đọc kết quả của nhau, cũng không đọc bộ `templates/` đã có.
Mỗi Claude subagent được giới hạn khoảng 35 lượt tìm kiếm để không hết hạn mức chung như round 2.

## Phương pháp

1. **83 claim** (G1, R1–R6, A1–A9, H1–H6, D1–D7, P1–P5, E1–E8, T1–T8, Q1–Q8, O1–O9, X1–X8, M1–M8)
   lấy từ "Bảng chọn cuối", Top 10 và D11 của cả 6 báo cáo. Giữ cả các phương án cạnh tranh, ví dụ H1 (arc42 rút gọn)
   và H2 (ARCHITECTURE.md kiểu matklad) ([scoring/claims.json](scoring/claims.json)).
2. **Ba người chấm độc lập:** `rater-a` và `rater-b` là Claude (rater-b đọc báo cáo theo thứ tự ngược),
   `rater-agy` là Gemini 4 Argon. Thang điểm 2 / 1 / 0 / −1, mỗi ô khác 0 phải kèm trích dẫn nguyên văn.
   Điểm một ô là trung vị của 3 người chấm.
3. **Kiểm tra trích dẫn bằng script:** **1.334/1.334** trích dẫn khớp với văn bản gốc ([scoring/merge.py](scoring/merge.py)).
4. **Phân mức:**
   - **A** (Σ ≥ 10/12 và không báo cáo nào mâu thuẫn): **bắt buộc** trong template. 52 claim.
   - **B** (Σ 7–9): **nên có**. 18 claim.
   - **C** (Σ ≤ 6): **tuỳ chọn hoặc bỏ**. 13 claim.

### Độ tin cậy giữa người chấm

| Cặp | Cùng nhóm | κ (3 nhóm) | Trùng điểm chính xác |
|---|---|---|---|
| rater-a ~ rater-b (Claude ~ Claude) | 97,0% | 0,86 | 91,2% |
| rater-a ~ rater-agy (Claude ~ Gemini) | 95,0% | 0,75 | 89,8% |
| rater-b ~ rater-agy (Claude ~ Gemini) | 94,6% | 0,74 | 87,1% |

κ cao hơn round 2 (0,68–0,77): claim về template cụ thể hơn, nên dễ chấm hơn.

**Thiên vị khi tự chấm:** có, nhưng nhẹ.
- Với 2 báo cáo Gemini: người chấm Gemini cho trung bình 1,42, hai người chấm Claude cho 1,27 (chênh +0,15).
- Với 4 báo cáo Claude: 1,75 so với 1,71 (chênh +0,04).
- Điểm ô là trung vị của 3 người chấm, nên một người chấm lệch không đổi được kết quả.

### Giới hạn

- **Nguồn trùng nhiều hơn round 2.** Jaccard domain giữa các báo cáo là 0,21–0,54 (round 2: 0,12–0,30), vì tài liệu
  chuẩn về template tập trung ở ít nguồn gốc: agents.md, arc42, MADR, Google SRE, GitHub Docs. Một phần đồng thuận
  vì vậy phản ánh việc **cùng đọc một nguồn gốc tốt**, không hoàn toàn là kết luận độc lập.
- **Ít số đo thực nghiệm.** Bằng chứng thực nghiệm chỉ có ở vài điểm:
  - AGENTS.md: ETH arXiv 2602.11988; Lulla 2601.20404; MSR '26 cho thấy 5% repo có context file và 50% số file không bao giờ được sửa;
  - README: Prana 2018, "Why" chỉ có ở 25,7% README;
  - ADR: Buchgeher 2023 và ICSA 2026, khoảng 63% ADR được "accepted" ngay khi tạo;
  - PR description: Pirouzkhah 2026, 80K PR, có giải thích code thì khả năng merge cao hơn 12–20%;
  - tài liệu lỗi thời: GitHub Survey 2017, 93% người gặp tài liệu thiếu hoặc lỗi thời.

  Phần còn lại là chuẩn chính chủ và thực hành của các tổ chức lớn.
- Người chấm `agy` phải chạy 3 lượt: nửa sau bị cắt do giới hạn output token nên được chia nhỏ và chạy lại.

## Ma trận đồng thuận (trung vị 3 người chấm)

T1–T4 = claude-T1…T4. Σ tính trên tối đa 12 điểm (6 báo cáo × 2). In đậm khi Σ = 12 (cả 6 báo cáo khẳng định rõ).

| ID | Claim | T1 | T2 | T3 | T4 | Argon | Flash | Σ/12 | Ủng hộ | Mức |
|---|---|---|---|---|---|---|---|---|---|---|
| G1 | Chung: Tối thiểu hoá: ít tài liệu, nằm trong repo, sửa cùng PR với code; tài liệu chỉ nên tồn tại nếu gắn với quy trình buộc phải chạm vào nó (PR, alert, agent đọc mỗi phiên); xoá tài liệu chết | 2 | 1 | 1 | 2 | 1 | 1 | 8 | 6/6 | B |
| R1 | D1 README: Nền README: khung ngắn kiểu standard-readme (rút gọn) và/hoặc Google docguide | 2 | 2 | 2 | 2 | 1 | 1 | 10 | 6/6 | A |
| R2 | D1 README: README bắt buộc có Quickstart/lệnh cài-chạy-test copy-paste chạy được | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| R3 | D1 README: README bắt buộc có trạng thái dự án (status) và/hoặc owner/đầu mối | 2 | 2 | 2 | 2 | 0 | 0 | 8 | 4/6 | B |
| R4 | D1 README: README có mục 'Why'/mục đích (không chỉ 'What') | 0 | 0 | 0 | 2 | 2 | 1 | 5 | 3/6 | C |
| R5 | D1 README: README ngắn (~1–2 màn hình, ≲150 dòng), là cổng điều hướng: link sang docs/, ADR, AGENTS.md; không chứa hướng dẫn cho agent | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| R6 | D1 README: Lệnh trong README nên được CI chạy lại (smoke test) để chống lỗi thời | 1 | 1 | 2 | 2 | 1 | 0 | 7 | 5/6 | B |
| A1 | D2 Agent: AGENTS.md là nguồn duy nhất cho agent; CLAUDE.md chỉ import @AGENTS.md (+ phần riêng) | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| A2 | D2 Agent: AGENTS.md viết tay; không commit file do LLM//init sinh mà không cắt gọt (ETH 2602.11988: không tăng thành công, +>20% chi phí) | 2 | 2 | 2 | 2 | 2 | 0 | 10 | 5/6 | A |
| A3 | D2 Agent: Độ dài AGENTS.md ≤ ~200 dòng (thường 30–150) | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| A4 | D2 Agent: Mục bắt buộc AGENTS.md: lệnh build/test/lint; quy ước khác mặc định; ranh giới/vùng cấm sửa; cách kiểm chứng 'done' | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| A5 | D2 Agent: AGENTS.md có mục bảo mật/dữ liệu (không đọc .env/secrets, không chạm prod) | 2 | 2 | 2 | 1 | 1 | 2 | 10 | 6/6 | A |
| A6 | D2 Agent: KHÔNG đưa tổng quan kiến trúc / cây thư mục / mô tả từng file vào AGENTS.md (link thay vì chép) | 2 | 2 | 2 | 2 | **-1** | 0 | 7 | 4/6 | B |
| A7 | D2 Agent: Quy tắc bắt buộc phải cưỡng chế bằng hook/CI/permission; file hướng dẫn chỉ là 'advisory' | 2 | 2 | 2 | 2 | 1 | 0 | 9 | 5/6 | B |
| A8 | D2 Agent: Tri thức theo vùng/hiếm dùng tách ra rule theo path (glob), AGENTS.md lồng nhau hoặc skills nạp khi cần | 2 | 1 | 2 | 2 | 2 | 0 | 9 | 5/6 | B |
| A9 | D2 Agent: Cập nhật AGENTS.md khi agent lặp lại một lỗi; review file này qua PR như code | 2 | 1 | 2 | 2 | 2 | 1 | 10 | 6/6 | A |
| H1 | D3 Kiến trúc: Nền kiến trúc: arc42 rút gọn (~6–7 mục) + sơ đồ C4 mức 1–2 | 2 | 2 | 2 | **-1** | **-1** | **-1** | 3 | 3/6 | C |
| H2 | D3 Kiến trúc: Nền kiến trúc: ARCHITECTURE.md kiểu matklad (codemap, invariants, boundaries) + C4 L1–L2 | 0 | 0 | 0 | 2 | 2 | 1 | 5 | 3/6 | C |
| H3 | D3 Kiến trúc: Sơ đồ dạng diagram-as-code (Mermaid/Structurizr/PlantUML) trong repo, không ảnh tĩnh | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| H4 | D3 Kiến trúc: Không điền đủ 12 mục arc42; không vẽ C4 mức Component/Code bằng tay | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| H5 | D3 Kiến trúc: Có mục crosscutting concepts (auth, logging, error handling) và invariants/ranh giới | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| H6 | D3 Kiến trúc: Có mục rủi ro / nợ kỹ thuật; mục 'Decisions' chỉ trỏ sang thư mục ADR | 2 | 2 | 2 | 1 | 0 | 1 | 8 | 5/6 | B |
| D1 | D4 ADR: Nền ADR: MADR 4 bản minimal (≈ Nygard + Considered Options) | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| D2 | D4 ADR: ADR bắt buộc có Considered Options (≥2 phương án) | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| D3 | D4 ADR: ADR đã accepted là bất biến; thay đổi bằng ADR mới supersede | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| D4 | D4 ADR: ADR đi qua PR với status 'proposed' trước khi 'accepted' (tránh accepted ngay) | 1 | 0 | 0 | 2 | 1 | 1 | 5 | 4/6 | C |
| D5 | D4 ADR: Mục Confirmation/cách kiểm chứng tuân thủ nên là check tự động (lint, arch test) | 2 | 1 | 2 | 2 | 1 | 1 | 9 | 6/6 | B |
| D6 | D4 ADR: Y-statement dùng làm dòng tóm tắt quyết định | 0 | 2 | 0 | 0 | 2 | 1 | 5 | 3/6 | C |
| D7 | D4 ADR: ADR ngắn: ≤1–2 trang, mỗi ADR một quyết định | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| P1 | D5 API: OpenAPI 3.1+ contract-first, file trong repo, là nguồn sự thật | 2 | 2 | 2 | 2 | 1 | 1 | 10 | 6/6 | A |
| P2 | D5 API: Style guide API ngắn (1–3 trang) chọn lọc quy tắc MUST từ Zalando (và/hoặc AIP); không chép nguyên bộ guideline lớn | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| P3 | D5 API: Định dạng lỗi theo RFC 9457 (Problem Details / problem+json) | 2 | 2 | 2 | 2 | 2 | 1 | 11 | 6/6 | A |
| P4 | D5 API: Lint contract trong CI (Spectral/Zally/Redocly) làm cổng chặn | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| P5 | D5 API: Style guide bắt buộc có: naming, versioning/breaking change, error format, pagination, auth, idempotency | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| E1 | D6 Spec: Nền spec: Google mini design doc 1–3 trang | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| E2 | D6 Spec: Spec bắt buộc có Goals và Non-goals | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| E3 | D6 Spec: Spec bắt buộc có Alternatives considered | 2 | 2 | 2 | 2 | 1 | 2 | 11 | 6/6 | A |
| E4 | D6 Spec: Spec bắt buộc có Acceptance criteria / Verification máy kiểm chứng được | 2 | 2 | 2 | 2 | 2 | 0 | 10 | 5/6 | A |
| E5 | D6 Spec: Spec có Rollout/rollback | 2 | 2 | 1 | 2 | 2 | 2 | 11 | 6/6 | A |
| E6 | D6 Spec: Vòng đời spec kiểu Oxide RFD: file trong repo, có trạng thái, thảo luận/duyệt qua PR | 2 | 0 | 1 | 2 | 1 | 1 | 7 | 5/6 | B |
| E7 | D6 Spec: Không viết spec cho thay đổi tầm thường; không áp pipeline SDD đầy đủ (spec-kit/Kiro) cho mọi task | 2 | 2 | 2 | 2 | 2 | 1 | 11 | 6/6 | A |
| E8 | D6 Spec: Với agent: để agent phỏng vấn người → viết spec → phiên mới thực thi; spec tự đủ (nêu file/interface, out-of-scope, bước kiểm chứng) | 2 | 2 | 2 | 2 | 1 | 0 | 9 | 5/6 | B |
| T1 | D7 Test+DoD: Test strategy là 1 file ngắn (1–2 trang) theo test pyramid / Google test sizes | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| T2 | D7 Test+DoD: Testing Trophy là lựa chọn hợp lệ (đặc biệt cho web app) | 0 | 0 | 0 | 2 | 2 | 0 | 4 | 2/6 | C |
| T3 | D7 Test+DoD: DoD là checklist ngắn (~5–10 mục) đặt trong PR template, không trên wiki | 2 | 2 | 1 | 2 | 1 | 2 | 10 | 6/6 | A |
| T4 | D7 Test+DoD: Mỗi mục DoD ánh xạ tới lệnh/CI gate máy kiểm được (agent tự chạy được) | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| T5 | D7 Test+DoD: Bug fix bắt buộc có regression test | 2 | 2 | 2 | 2 | 0 | 2 | 10 | 5/6 | A |
| T6 | D7 Test+DoD: Có chính sách test flaky và mock | 2 | 2 | 1 | 2 | 2 | 1 | 10 | 6/6 | A |
| T7 | D7 Test+DoD: Cấm sửa/xoá/skip test để cho pass; agent phải đưa bằng chứng (output test) | 2 | 2 | 1 | 1 | 1 | 0 | 7 | 5/6 | B |
| T8 | D7 Test+DoD: Không lấy % coverage làm mục tiêu tự thân / tránh ice-cream cone | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| Q1 | D8 PR: PR template ngắn (≲25–35 dòng) | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| Q2 | D8 PR: Mô tả PR theo Google CL description (what + why, tự đủ ý, không 'Fix bug') | 2 | 2 | 1 | 2 | 2 | 1 | 10 | 6/6 | A |
| Q3 | D8 PR: PR bắt buộc có cách kiểm chứng kèm bằng chứng (lệnh/output/ảnh) | 2 | 2 | 2 | 2 | 2 | 1 | 11 | 6/6 | A |
| Q4 | D8 PR: PR có mục khai báo AI (công cụ, phạm vi; trailer Assisted-by) | 2 | 2 | 2 | 2 | 1 | 2 | 11 | 6/6 | A |
| Q5 | D8 PR: PR có rủi ro & rollback | 2 | 2 | 2 | 2 | 2 | 1 | 11 | 6/6 | A |
| Q6 | D8 PR: PR có 'ghi chú cho reviewer / feedback mong muốn' | 1 | 1 | 2 | 2 | 2 | 0 | 8 | 5/6 | B |
| Q7 | D8 PR: PR nhỏ (khoảng 100–400 dòng diff; 1000 là quá lớn) | 2 | 2 | 1 | 2 | 1 | 1 | 9 | 6/6 | B |
| Q8 | D8 PR: Tiêu đề PR theo Conventional Commits | 0 | 0 | 0 | 0 | 2 | 2 | 4 | 2/6 | C |
| O1 | D9 Ops: Postmortem theo Google SRE (example postmortem) rút gọn, blameless | 2 | 2 | 2 | 1 | 2 | 2 | 11 | 6/6 | A |
| O2 | D9 Ops: Postmortem dùng 'contributing factors' (PagerDuty) thay vì một root cause duy nhất | 2 | 1 | 1 | 2 | 1 | 0 | 7 | 5/6 | B |
| O3 | D9 Ops: Postmortem có Lessons: went well / went wrong / where we got lucky | 2 | 2 | 1 | 1 | 2 | 2 | 10 | 6/6 | A |
| O4 | D9 Ops: Trigger viết postmortem định nghĩa trước (downtime, mất dữ liệu, on-call can thiệp…); không viết cho mọi sự cố nhỏ | 2 | 2 | 1 | 2 | 2 | 1 | 10 | 6/6 | A |
| O5 | D9 Ops: Action items bắt buộc có owner + ticket + hạn; postmortem phải được review | 2 | 2 | 2 | 2 | 2 | 1 | 11 | 6/6 | A |
| O6 | D9 Ops: Runbook: mỗi alert một mục/file, alert link thẳng tới runbook | 2 | 2 | 2 | 2 | 1 | 2 | 11 | 6/6 | A |
| O7 | D9 Ops: Runbook có ngày 'last verified' / được chạy thử định kỳ | 2 | 1 | 1 | 2 | 0 | 0 | 6 | 4/6 | C |
| O8 | D9 Ops: Bước thay đổi production trong runbook cần người phê duyệt (agent chỉ chẩn đoán) | 2 | 2 | 2 | 2 | 1 | 2 | 11 | 6/6 | A |
| O9 | D9 Ops: Postmortem có trường 'AI agent có liên quan không' | 2 | 2 | 0 | 2 | 0 | 0 | 6 | 3/6 | C |
| X1 | D10 Sec+AI: SECURITY.md theo GitHub: supported versions, kênh báo cáo riêng tư, SLA phản hồi (ngày), phạm vi | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| X2 | D10 Sec+AI: Chính sách AI là file riêng (AI_POLICY.md / docs/ai-policy.md) theo mô hình LLVM/Linux kernel/Ghostty | 2 | 2 | 2 | 2 | **-1** | 1 | 8 | 5/6 | B |
| X3 | D10 Sec+AI: Khai báo AI bằng trailer Assisted-by; agent không được ký Signed-off-by/DCO thay người | 2 | 2 | 2 | 2 | 1 | 0 | 9 | 5/6 | B |
| X4 | D10 Sec+AI: Người submit/merge chịu trách nhiệm hoàn toàn, phải hiểu và giải thích được diff | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| X5 | D10 Sec+AI: Quyền của agent cưỡng chế bằng cấu hình (permissions/sandbox/hook/CI), không chỉ văn xuôi | 2 | 2 | 2 | 2 | 2 | 0 | 10 | 5/6 | A |
| X6 | D10 Sec+AI: Có quy tắc dữ liệu: không đưa secrets/PII/dữ liệu khách hàng vào công cụ chưa duyệt | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| X7 | D10 Sec+AI: Tham chiếu OWASP Top 10 for Agentic Applications 2026 | 2 | 2 | 0 | 2 | 2 | 1 | 9 | 5/6 | B |
| X8 | D10 Sec+AI: Cấm agent tự hành (tự merge/push/deploy/comment) khi chưa có người duyệt | 2 | 2 | 2 | 2 | 1 | 2 | 11 | 6/6 | A |
| M1 | D11 Thêm: Nên có CONTRIBUTING / dev setup (có thể gộp README) | 2 | 2 | 2 | 2 | 1 | 2 | 11 | 6/6 | A |
| M2 | D11 Thêm: Nên có glossary / ngôn ngữ miền (ubiquitous language) | 2 | 2 | 2 | 2 | 2 | 2 | **12** | 6/6 | A |
| M3 | D11 Thêm: Nên có CHANGELOG / release notes (Keep a Changelog) | 2 | 2 | 1 | 2 | 2 | 0 | 9 | 5/6 | B |
| M4 | D11 Thêm: Nên có CODEOWNERS cho file quy tắc agent/ADR/contract | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 1/6 | C |
| M5 | D11 Thêm: Nên có CI kiểm tài liệu (link checker, lệnh README, tham chiếu code lỗi thời) | 0 | 1 | 1 | 2 | 1 | 0 | 5 | 4/6 | C |
| M6 | D11 Thêm: Dùng Diátaxis để phân loại tài liệu (tutorial/how-to/reference/explanation) | 2 | 2 | 0 | 1 | 0 | 0 | 5 | 3/6 | C |
| M7 | D11 Thêm: Quy trình lặp lại đóng gói thành skills cho agent | 2 | 0 | 2 | 1 | 0 | 0 | 5 | 3/6 | C |
| M8 | D11 Thêm: Không đáng làm: test plan IEEE 829/ISO 29119, KEP/PRR đầy đủ, wiki ngoài repo | 2 | 2 | 2 | 2 | 2 | 1 | 11 | 6/6 | A |

## Kết quả: best practice được chọn

| Loại | Template nền | Mục bắt buộc (mức A) | Nên có (mức B) | Bỏ hoặc tuỳ chọn (mức C) |
|---|---|---|---|---|
| D1 README | standard-readme rút gọn + Google docguide (R1, 10) | Quickstart copy-paste chạy được (12); ngắn, là cổng điều hướng, không chứa hướng dẫn cho agent (12) | Status và owner (8); CI chạy lại lệnh Quickstart (7) | Mục "Why" riêng (5): gộp vào câu mô tả |
| D2 Agent | **AGENTS.md là nguồn duy nhất; CLAUDE.md = `@AGENTS.md`** (A1, 12) | Viết tay, không commit file LLM sinh (10); ≤200 dòng (12); lệnh, quy ước, vùng cấm, "done" (12); bảo mật và dữ liệu (10); sửa khi agent lặp lỗi, review qua PR (10) | Luật bắt buộc dùng hook/CI (9); rule theo path / file lồng nhau (9); không có tổng quan kiến trúc (7, Argon mâu thuẫn) | — |
| D3 Kiến trúc | **Hoà:** arc42 rút gọn (H1, 3) và matklad (H2, 5) → **ghép cả hai** | Diagram-as-code (12); không điền đủ 12 mục arc42 và không vẽ C4 Code (12); crosscutting và invariants (12) | Rủi ro / nợ kỹ thuật; mục Decisions trỏ sang ADR (8) | — |
| D4 ADR | **MADR 4 minimal** (D1, 12) | ≥2 Considered Options (12); bất biến, supersede (12); 1 quyết định, ≤1–2 trang (12) | Confirmation tự động (9) | Status "proposed" qua PR (5): vẫn giữ vì không tốn gì; dòng Y-statement (5): bỏ |
| D5 API | **OpenAPI 3.1 contract-first** (P1, 10) | MUST chọn lọc từ Zalando (12); RFC 9457 (11); lint trong CI (12); naming, versioning, lỗi, pagination, auth, idempotency (12) | — | — |
| D6 Spec | **Google mini design doc 1–3 trang** (E1, 12) | Goals/Non-goals (12); Alternatives (11); Acceptance/Verification (10); Rollout/rollback (11); không viết cho việc tầm thường, không chạy SDD đầy đủ (11) | Vòng đời kiểu Oxide RFD (7); agent phỏng vấn → spec → phiên mới (9) | — |
| D7 Test + DoD | **1 file ngắn: test pyramid + Google test sizes** (T1, 12) | DoD ánh xạ sang lệnh/CI (12); DoD nằm trong PR template (10); regression test cho bug fix (10); chính sách mock và flaky (10); không lấy coverage làm mục tiêu (12) | Cấm sửa/xoá test để cho pass (7) | Testing Trophy (4): chỉ ghi chú cho web app |
| D8 PR | **GitHub template + Google CL description** (Q2, 10) | ≤25–35 dòng (12); bằng chứng kiểm chứng (11); khai báo AI (11); rủi ro và rollback (11) | Ghi chú cho reviewer (8); PR ≈100–400 dòng (9) | Conventional Commits (4): bỏ |
| D9 Ops | **Postmortem Google SRE; runbook mỗi alert** (O1, 11; O6, 11) | went well / wrong / lucky (10); trigger định trước (10); action items có owner, ticket, hạn (11); bước thay đổi prod cần người duyệt (11) | Contributing factors (7) | "Last verified" (6) và trường "AI agent tham gia" (6): giữ, vì rẻ và rút từ sự cố round 2 |
| D10 Sec+AI | **SECURITY.md (GitHub)** (X1, 12) + **AI policy riêng** theo LLVM/kernel (X2, 8; Argon muốn gộp) | Người merge chịu trách nhiệm (12); quy tắc dữ liệu (12); quyền agent cưỡng chế bằng cấu hình (10); cấm agent tự hành (11) | `Assisted-by`, agent không ký thay (9); tham chiếu OWASP Agentic (9) | — |
| D11 Thêm | — | **CONTRIBUTING** (11); **glossary** (12); không làm test plan IEEE 829, KEP đầy đủ, wiki ngoài repo (11) | **CHANGELOG** (9) | CODEOWNERS (2); CI kiểm tài liệu (5); Diátaxis (5); skills (5): ghi là tuỳ chọn |

**Quyết định cho D3 (lựa chọn của tôi, không phải đồng thuận).**
Ba báo cáo T1–T3 chọn arc42 rút gọn; T4 và Argon chọn ARCHITECTURE.md của matklad; Flash chọn một tài liệu ngắn gồm C4 + Mermaid.
Template ghép cả hai, dựa trên các điểm cả 6 báo cáo cùng đồng ý (H3, H4, H5):
- từ arc42 lấy mục tiêu chất lượng, ràng buộc, chiến lược giải pháp, rủi ro;
- từ matklad lấy codemap (tuỳ chọn) và mục "bất biến, ranh giới".

## Thay đổi so với bộ template trước

| File | Thay đổi | Claim |
|---|---|---|
| `SECURITY.md` | **Mới**: phiên bản hỗ trợ, kênh báo cáo riêng, thời hạn phản hồi, phạm vi | X1 (6/6) |
| `docs/ai-policy.md` | Tách từ `security-and-ai-policy.md`; thêm `Assisted-by`, agent không ký thay, bot không approve | X2–X8 |
| `CONTRIBUTING.md`, `docs/glossary.md`, `CHANGELOG.md` | **Mới** | M1, M2, M3 |
| `CLAUDE.md` | **Mới**: chỉ `@AGENTS.md` | A1 |
| `AGENTS.md` | Thêm mục "Thế nào là xong", "Bảo mật và dữ liệu", "Git và PR"; ghi chú rule theo path | A4, A5, A8 |
| `docs/architecture.md` | Ghép arc42 rút gọn + codemap/invariants; mục chiến lược giải pháp, rủi ro, link ADR | H3–H6 |
| `docs/adr/0000-template.md` | Chuyển sang MADR 4 (front matter, Considered Options, Confirmation) | D1–D7 |
| `docs/api/` | Lỗi theo **RFC 9457** `application/problem+json` (trước là envelope tự đặt); lint Spectral trong CI | P3, P4 |
| `docs/specs/0000-template.md` | Mục riêng Goals/Non-goals và Alternatives; tiêu chí "khi nào không viết"; luồng agent | E1–E8 |
| `docs/test-strategy.md` | Chuyển DoD sang PR template; thêm chính sách mock | T3, T6 |
| `.github/pull_request_template.md` | Rút gọn còn 30 dòng; What & why theo Google; DoD 6 mục; mục AI | Q1–Q6, T3 |
| `docs/runbooks/` | Tách thành README (deploy, rollback, mức độ, trigger postmortem) + mỗi alert một file có "last verified" | O4, O6, O7 |
| `docs/postmortems/` | Thêm "Diễn biến", "Các yếu tố góp phần", "Điểm may mắn"; một owner; hạn ≤5 ngày | O1–O5 |

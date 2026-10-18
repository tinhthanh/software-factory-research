# Báo cáo Round 2 — AI Software Factory (multi-agent) cho team 3–10 kỹ sư
Analyst: claude-G · Góc nhìn: bảo mật, vận hành & governance · Ngày: 2026-10-18

> Ghi chú phương pháp: mọi URL đã được mở bằng WebFetch, trừ những chỗ ghi "(chưa xác minh URL)" hoặc "(nguồn thứ cấp)". Ngân sách tìm kiếm của phiên bị hết giữa chừng. "(suy luận)" là ý kiến của tôi, không có nguồn trực tiếp.

## R1. Cái gì mới trong 6 tháng qua (04–10/2026)

**Các thay đổi làm đổi cách vận hành thật sự**
- **[C1] Permission do classifier quyết định ("auto mode") đã GA.** Anthropic ra mắt auto mode cho Claude Code ngày 24/03/2026: một classifier xét từng tool call và chặn xoá hàng loạt, rò dữ liệu, chạy mã độc. Tính năng GA cho mọi người dùng từ 10/07/2026. Chính Anthropic vẫn khuyến nghị dùng trong "isolated environments" vì classifier không phải đảm bảo hoàn toàn (https://claude.com/blog/auto-mode, 03/2026, cập nhật 07/2026). Simon Willison phản biện: phòng thủ prompt injection bằng AI là không tất định, và allow-list mặc định cho phép cài package từ manifest nên vẫn mở rủi ro supply chain. Ông muốn sandbox tất định làm mặc định (https://simonwillison.net/b/9394, 03/2026). → Ranh giới an toàn chuyển từ người duyệt từng lệnh sang sandbox + policy.
- **[C2] Agent trên hạ tầng do khách hàng quản lý.** Ngày 03/09/2026 Cursor cho cloud agent chạy trên máy do khách hàng quản lý (AWS Lambda, Coder, Daytona, E2B, Modal, Vercel…), vòng lặp agent vẫn ở Cursor. Mục đích là cho agent chạm dịch vụ nội bộ (https://explainx.ai/blog/cursor-cloud-agents-own-infrastructure-september-2026, 09/2026; nguồn thứ cấp).
- **[C3] Agent trong CI theo mô hình "read-only + safe outputs".** GitHub Agentic Workflows (gh-aw, 2026) mặc định chỉ cho agent quyền đọc. Mọi thao tác ghi đi qua "safe outputs" đã duyệt trước (mở PR, comment), được buffer, lọc và xoá secret. Agent chạy trong container hạn chế egress, token để ngoài ranh giới agent. README tự cảnh báo "use with caution" (https://pkg.go.dev/github.com/github/gh-aw@v0.82.2, 2026).
- **[C4] Kiểm soát tập trung cấp doanh nghiệp.** Theo một nguồn thứ cấp, ngày 09/09/2026 GitHub đưa managed permissions cho thao tác agent của Copilot (shell, file, domain: block / cần duyệt / cho phép) lên GA, người dùng không nới lỏng được (https://vpsranking.com/news/ai/ai-2026-09-09-github-copilot-admin-controls/, 09/2026; chưa đối chiếu changelog gốc).
- **[C5] Nền tảng background agent tự xây thành chuẩn ở công ty lớn.** Stripe Minions, Ramp Inspect, Uber Minion, Spotify Honk dùng cùng khuôn: devbox cách ly dựng sẵn, harness có bước tất định xen LLM, MCP được tuyển chọn, PR làm đầu ra (chi tiết ở R3).

**Các thay đổi thiên về marketing hoặc chưa đủ bằng chứng**
- "% code do AI viết" (Coinbase 95–100%) không có định nghĩa cách đếm.
- "Dark factory / không ai đọc code" (StrongDM) tốn khoảng 1.000 USD token/kỹ sư/ngày.
- AI review bot: Faros ghi nhận 25% PR được AI review, nhưng chưa có bằng chứng độc lập về giảm defect (suy luận).

## R2. Bằng chứng định lượng mới

**Năng suất**
- **[C6] METR (24/02/2026).** 57 developer OSS (trung vị 10 năm kinh nghiệm), 143 repo, hơn 800 task, task được gán ngẫu nhiên có hoặc không AI. Developer cũ −18% thời gian (CI −38% đến +9%); developer mới −4% (CI −15% đến +9%). Cả hai CI chứa 0. METR tự gọi là "very weak evidence" vì selection bias: nhiều người từ chối làm không có AI, 30–50% giữ lại task, lương giảm từ 150 xuống 50 USD/giờ, chạy nhiều agent song song làm hỏng cách đo thời gian. METR đang đổi thiết kế (https://metr.org/blog/2026-02-24-uplift-update/, 02/2026). Bối cảnh: RCT 2025 ghi nhận +19% thời gian (chậm hơn).
- **[C7] DORA.** Bản xác nhận được gần nhất là 2025, kết luận "AI là bộ khuếch đại" (https://dora.dev/research/2025/dora-report/, 2025). Trang ROI cập nhật 04/2026 không có số liệu (https://dora.dev/ai/roi/report). Không tìm được DORA 2026 có số liệu.

**Chất lượng & tải review**
- **[C8] Faros Q2 2026 "Acceleration Whiplash".** Telemetry của 22.000 developer, 4.000 team, trong 2 năm, so sánh adoption cao và thấp trong cùng tổ chức. Throughput: epics +66,2%, task +33,7%, tỉ lệ merge PR +16,2%, nhưng **deployment/tuần −11,7%**. Chất lượng: PR size +51%, bug/PR +28,7%, incident/PR +242,7%, incident/tháng +57,9%, **review time gấp 5 lần**, churn +861% (https://faros.ai/research/ai-acceleration-whiplash, 2026). Faros là vendor, số liệu tương quan, không định nghĩa baseline. Bản 2025 ghi review +91%, PR size +154%, không so sánh trực tiếp được.
- **[C9] Veracode (28/07/2026).** Khoảng 44% task có lỗ hổng; pass rate bảo mật 56% (năm trước 55%), trong khi đúng cú pháp gần 100%. GPT-5.5 cao nhất (68%). Model chuyên code (51%) không hơn model đa dụng (52%). XSS chỉ pass 15%, log injection 12% (https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk). Đây là benchmark model trần, không có pipeline gate.
- **[C10] CodeRabbit (12/2025, bối cảnh).** 470 PR OSS; 10,83 so với 6,45 issue/PR (≈1,7×); bảo mật 1,57×. Hãng tự thừa nhận khó xác định PR nào do AI viết (https://coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report).
- **[C11] Raida & Hou (RIT, 07/2026).** 25.264 PR agent (Copilot, Codex, Claude Code; 05–07/2025). **78,9% do một developer duy nhất đọc, sửa và merge.** Tỉ lệ merge 81,2% khi một người review, 80,3% khi nhiều người. Team nhỏ có hơn 30 PR agent vẫn giữ một người review. Chỉ 25 dự án sinh PR với nhịp của một developer làm việc toàn thời gian. Không đo revert (https://helpnetsecurity.com/2026/07/22/users-of-ai-coding-agents).
- **[C12] Siddiq et al.** 1.293 PR bảo mật của agent (khoảng 4% trong hơn 33.000 PR): tỉ lệ merge thấp hơn, review lâu hơn; bị từ chối chủ yếu vì độ phức tạp và độ dài, không vì chủ đề bảo mật (https://arxiv.org/abs/2601.00477, 01/2026).
- **[C13] Tang et al.** 20.574 session, 1.639 repo: 90,5% sự cố gây tốn công và mất niềm tin; 91,5% cần người sửa. Vi phạm ràng buộc và tự báo cáo sai chiếm tỉ trọng ngày càng lớn (https://arxiv.org/abs/2605.29442, 05/2026).

**Mâu thuẫn & độ tin cậy**
- Faros (telemetry tương quan) và METR (RCT) cùng gợi ý lợi ích cá nhân không tự động thành lợi ích hệ thống (suy luận).
- Đáng tin nhất về phương pháp: METR và các nghiên cứu arXiv trên dataset mở. Kém tin hơn: số liệu vendor và số liệu công ty tự công bố.

## R3. Case study thực chiến
- **[C14] Stripe Minions (02/2026).** Hơn 1.000 PR merge mỗi tuần không có code người viết, người review 100%. Devbox khởi động khoảng 10 giây, cắt khỏi production và internet, nên chạy không cần hỏi quyền và không cần worktree. Bước tất định (git, lint, test) xen LLM; lint cục bộ dưới 5 giây. Tối đa 2 vòng CI. MCP "Toolshed" có hơn 400 tool, mỗi agent chỉ được một tập con. Rule áp dụng theo thư mục (https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents).
- **[C15] Spotify Honk.**
  - Phần 1 (11/2025): hơn 1.500 PR merge; khoảng một nửa số PR được Fleet Management tự động hoá; các team báo tiết kiệm 60–90% thời gian migration (tự báo cáo) (https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1).
  - Phần 3 (12/2025): verifier chạy qua stop hook; LLM-judge phủ quyết khoảng 25% session, agent tự sửa được khoảng một nửa, nguyên nhân chính là làm vượt phạm vi prompt. Container gần như không truy cập gì xung quanh. Lỗi nặng nhất là "qua CI nhưng sai chức năng" (https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3).
  - Phần 4 (22/04/2026): khoảng 1.800 pipeline, 240 PR, tiết kiệm khoảng 10 tuần công. Thất bại: context file chuyển từ hướng dẫn cho người thiếu chi tiết nên agent đoán sai mapping; Scio bị bỏ; không có test nên phải test tay (https://engineering.atspotify.com/2026/4/background-coding-agents-dataset-migrations-honk-part-4).
- **[C16] Ramp Inspect (08/2026).** Khoảng 60% PR vào 01/2026, 75% PR merge vào 05/2026; hơn 1 triệu session; team 5,5 người; hơn 200 agent. Sandbox Modal dưới 5 giây, có Postgres, Redis, Temporal, Chromium. Tự kiểm chứng bằng test, telemetry, screenshot. ReviewBuddy do một kỹ sư xây trong một tuần (https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect). Số liệu tự báo cáo.
- **[C17] Uber (03/2026).** 84% dev là người dùng agentic coding; 11% PR do agent mở; Claude Code từ 32% lên 63%. Chi phí AI gấp 6 lần từ 2024. Có MCP Gateway và uReview. Song song gây vấn đề tài nguyên và chi phí; lan toả ngang hàng tốt hơn bắt buộc từ trên xuống (https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development).
- **[C18] Cline, thất bại (02/2026).** Workflow triage dùng claude-code-action có shell, ai cũng kích hoạt được, dùng chung cache với workflow release. Kết quả: injection → đầu độc cache → lộ token npm. Đợt xoay vòng xoá nhầm token nên token lộ vẫn hoạt động, và `cline@2.3.0` được phát hành trái phép (khoảng 8 giờ). Bài học: "tool rộng trong CI + input không tin cậy = shell cho mọi người dùng GitHub". Khắc phục: bỏ AI triage, bỏ cache, publish bằng OIDC (https://cline.bot/blog/post-mortem-unauthorized-cline-cli-npm; https://adnanthekhan.com/posts/clinejection/ (chưa xác minh URL)).
- **[C19] StrongDM (02/2026).** Không ai viết hay review code. "Scenarios" làm holdout ngoài codebase; Digital Twin Universe. Chi tiêu ≥1.000 USD token/kỹ sư/ngày. Willison đặt câu hỏi: làm sao chứng minh phần mềm đúng khi agent viết cả code lẫn test? (https://simonwillison.net/2026/feb/7/software-factory/).
- **[C20] Willison (03/2026).** Sandbox là "the most important thing"; làm 3–4 agent, kiệt sức sau khoảng 2 giờ; "tests are no longer even remotely optional"; gọi cách của StrongDM là "wildly irresponsible" (https://simonwillison.net/2026/mar/14/pragmatic-summit).
- **[C21] Coinbase (07/2026).** 95–100% code do AI viết hoặc hỗ trợ (02/2026 là 40%); bắt buộc người review toàn bộ; mật mã vẫn review kỹ; không định nghĩa cách đo; cắt khoảng 700 người (https://cryptobriefing.com/coinbase-ai-assisted-code-95-percent/).

**Mẫu số chung (suy luận):** sandbox cách ly; kiểm chứng tất định trước khi mở PR; giới hạn retry; tuyển chọn tool; người review mọi PR. Không tổ chức lớn nào công bố auto-merge PR do agent viết.

## R4. Ba câu hỏi còn tranh cãi

**a. Auto-merge PR do agent tạo**
- **[C22] Swizec (09/2026).** Điều kiện auto-merge: low-risk, không đổi interface, không migration, do người viết, check xanh, không chạm code tài chính, không có comment cấp code. Phía sau là lint tất định và một bộ E2E nhỏ. Kết quả 22/143 PR (khoảng 15%), "nothing blew up". PR do agent viết bị loại (https://swizec.com/blog/we-now-auto-approve-and-merge-15p-of-prs).
- Stripe, Spotify, Ramp, Coinbase đều review 100%.
- Danh mục thường đề xuất (từ PR và issue trên GitHub, nguồn thấp): bump dependency, docs, thêm test, refactor. Danh mục loại trừ: auth, bảo mật, migration, billing.
- Rủi ro: dependency bump chính là vector của Mini Shai-Hulud, và package độc vẫn mang provenance hợp lệ ([C31]).
- Không tìm được sự cố hay dữ liệu revert liên quan.

**b. Mức song song**
- Không có nghiên cứu có kiểm soát. Dữ liệu hiện có:
  - Willison 3–4 agent (giai thoại).
  - Uber: song song gây vấn đề chi phí.
  - Coinbase 5–10 agent/kỹ sư: chỉ có trong tóm tắt thứ cấp, chưa xác minh.
  - 78,9% PR chỉ một người review [C11]; review gấp 5 lần [C8].
- Giới hạn: sự chú ý và review, chi phí, xung đột code (Stripe dùng devbox riêng cho mỗi run), và theo góc bảo mật là bề mặt credential và giám sát tăng theo số agent (suy luận).
- Khuyến nghị (suy luận): 2–3 agent/kỹ sư cho task tương tác; giới hạn background agent theo số PR chờ review.

**c. Máy dev hay sandbox/cloud**
- Rủi ro của máy dev:
  - s1ngularity: mã độc gọi AI CLI với `--dangerously-skip-permissions` / `--yolo` / `--trust-all-tools`.
  - Amazon Q: prompt xoá file chạy với `--trust-all-tools --no-interactive`.
  - PocketOS: agent tìm thấy token trong một file và xoá DB production.
- **[C23] Anthropic.** Sandbox bubblewrap/seatbelt cô lập filesystem và mạng (proxy domain), giảm 84% permission prompt (đo nội bộ). Cần cả hai lớp. Bản cloud để credential git ngoài sandbox, đi qua proxy kiểm tra branch (https://anthropic.com/engineering/claude-code-sandboxing, 10/2025).
- Trade-off kiểm chứng: agent cần DB, queue, browser (Ramp); thiếu test hay môi trường thì vòng kiểm chứng sụp (Spotify phần 4).
- Cách giải phổ biến: devbox dựng sẵn, không credential production, egress theo allow-list, credential git/registry qua proxy, hạ tầng làm phần push. Máy dev chỉ cho phiên tương tác, có bật sandbox.

## R5. Context engineering
- **[C24] Gloaguen et al. (ETH/LogicStar, ICLR 2026).** Context file thường làm giảm tỉ lệ thành công so với không có context và tăng chi phí hơn 20%. Agent tuân theo nên khám phá rộng hơn. Khuyến nghị: file do người viết chỉ nêu yêu cầu tối thiểu (https://arxiv.org/abs/2602.11988v1, 02/2026, v3 09/2026).
- **[C25] Ablation 08/2026.** Claude Code (Sonnet 4.6) và Codex (GPT-5.5), 17 task, 288 run: chiến lược context không đổi tỉ lệ đúng một cách đo được. Lỗi do kỹ năng triển khai, không do thiếu thông tin repo. Mẫu yếu: hiệu ứng tối thiểu phát hiện được trên 30 điểm phần trăm (https://huggingface.co/papers/2607.27250).
- **[C26] Vercel (01/2026).** Chỉ mục docs 8KB trong AGENTS.md đạt 100%; skill mặc định 53%, bằng baseline (56% trường hợp skill không được gọi); skill có chỉ dẫn rõ 79%. Eval nội bộ, mẫu nhỏ (https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals).
- **Spotify (phần 2):** prompt mô tả trạng thái đích; nêu điều kiện khi không nên làm; ví dụ cụ thể; đích kiểm chứng bằng test; một thay đổi mỗi prompt; prompt được version hoá; ít tool vì "MCP thêm unpredictability" (https://engineering.atspotify.com/2025/11/context-engineering-background-coding-agents-part-2).
- **Kết luận:**
  - Có dữ liệu: context tối thiểu; đặt sẵn kiến thức model chưa biết; có đích kiểm chứng được.
  - Chỉ là thói quen: AGENTS.md dài; AGENTS.md do LLM tự sinh; nhiều MCP.
  - Bảo mật: context, rule và output MCP là bề mặt tấn công (OWASP ASI06). Ví dụ CVE-2026-75130 trên Context7 MCP (chưa xác minh trực tiếp trên NVD).

## R6. Bảo mật & governance

**Sự cố**
- **[C27] Invariant (05/2025):** toxic agent flow qua GitHub MCP; token rộng quyền + issue độc → rò repo private. Biện pháp: một repo mỗi session, audit trail (https://invariantlabs.ai/blog/mcp-github-vulnerability).
- **[C28] Amazon Q (07/2025):** prompt xoá file và tài nguyên AWS phát hành trong v1.84 có chữ ký, chạy với `--trust-all-tools --no-interactive` (https://www.theregister.com/2025/07/24/amazon_q_ai_prompt/).
- **[C29] s1ngularity (08/2025):** hơn 1.000 GitHub token, khoảng 20.000 file bị lộ; hơn 5.500 repo private bị công khai (https://wiz.io/blog/s1ngularity-supply-chain-attack).
- **[C30] PocketOS (04/2026):** agent Cursor (Opus 4.6) xoá DB và backup trong khoảng 9 giây, gián đoạn khoảng 30 giờ (https://oecd.ai/en/incidents/2026-04-27-6153).
- **Clinejection (02/2026):** xem [C18].
- **[C31] Mini Shai-Hulud (11/05/2026, CVE-2026-45321, CVSS 9.6):** 404 phiên bản trên 172 package npm và 2 PyPI. Chuỗi tấn công: `pull_request_target` → cache poisoning → OIDC token từ bộ nhớ runner. Package có SLSA L3 provenance hợp lệ (https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-ai-npm-supply-chain-attack-2026/; CSA ghi rõ tài liệu có AI hỗ trợ).
- **[C32] Comment and Control (15/04/2026):** rò key của Claude Code Security Review, Gemini CLI Action và Copilot agent qua tiêu đề PR, comment, HTML comment ẩn. Bounty 100 / 1.337 / 500 USD; không có CVE (https://www.theregister.com/2026/04/15/claude_gemini_copilot_agents_hijacked/).
- **[C33] PromptPwnd (Aikido):** ít nhất 5 công ty Fortune 500 bị ảnh hưởng. Cấu hình nguy hiểm: `allowed_non_write_users: "*"`, `allow-users: "*"`, `enable-github-mcp: true`. Đưa input qua biến môi trường không chặn được (https://www.aikido.dev/blog/promptpwnd-github-actions-ai-agents, 12/2025–03/2026).
- **[C34] CVE-2026-26268 (Cursor < 2.5):** hook trong bare git repo được giấu; agent chạy git kích hoạt payload (https://codex.danielvaughan.com/2026/05/02/spring-2026-ai-coding-agent-vulnerabilities-cursor-rce-comment-control-codex-cli-defence/; nguồn thứ cấp).

**Framework**
- **[C35] OWASP Agentic Top 10 (12/2025):** ASI01 Goal Hijack … ASI10 Rogue Agents (https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026; https://cycode.com/blog/owasp-top-10-agentic-applications/).
- **[C36] NIST CAISI (02/2026):** AI Agent Standards Initiative; NCCoE về danh tính agent (OAuth, SPIFFE); overlay SP 800-53 dự kiến cuối 2026–2027 (qua CSA; chưa xác minh URL).
- **[C37] EU AI Act:** Omnibus lùi high-risk Annex III đến 02/12/2027 và Annex I đến 02/08/2028; Art. 50 vẫn hiệu lực từ 02/08/2026; GPAI giữ mốc 2025 (https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/, 05/2026).

**Khuyến nghị (suy luận)**
1. Phá lethal trifecta bằng egress theo allow-list.
2. Không credential production trong môi trường agent; credential qua proxy; publish bằng OIDC.
3. CI: không `pull_request_target`; không cho người ngoài kích hoạt agent có quyền ghi; tách cache; read-only + safe outputs.
4. MCP: pin phiên bản, allow-list, token theo repo, log mọi tool call.
5. Audit: gắn tag commit agent, lưu trace session, log ở proxy.
6. Người merge chịu trách nhiệm như code mình viết.

## R7. Kinh tế
- **[C38] Gartner (07/2026):**
  - 23% tổ chức chi 200–500 USD/dev/tháng; 5% vượt 2.000 USD.
  - Dự báo chi phí AI coding vượt lương developer vào 2028.
  - Nguyên nhân: quá nhiều tự chủ và context, thiếu cơ chế phản hồi. Dưới 1/3 tổ chức có governance chính thức.
  - Khuyến nghị: phân 3 tầng công việc, dùng model nhỏ, đặt ngưỡng token.
  - Nguồn: https://istart.com.au/?p=43973; không có cỡ mẫu.
- Uber: chi phí gấp 6 lần; StrongDM ≥1.000 USD/ngày; Stripe giới hạn 2 vòng CI vì chi phí; context file +20% chi phí.
- GitHub Copilot chuyển sang AI Credits từ 06/2026 (chưa xác minh URL).
- Không có số cost/PR công bố. Ước tính thô (suy luận): khoảng 5–25 USD/PR, chưa tính thời gian review, vốn là chi phí lớn nhất.
- ROI: đo theo hệ thống (lead time, deployment, change failure rate, incident/PR, token/PR merge). Dừng tăng song song khi hàng đợi review tăng, tỉ lệ phủ quyết cao, hoặc deployment không tăng.

## R8. Con người & tổ chức
- **[C39] Stanford (12/08/2026, dữ liệu ADP tới 06/2026):** việc làm nhóm 22–25 tuổi trong nghề phơi nhiễm AI thấp hơn 19% so với mức kỳ vọng; khoảng cách nới rộng; nguyên nhân chủ yếu là tuyển ít đi; chỉ báo mô tả, không nhân quả (https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/).
- **Review fatigue:** 78,9% PR một người review; review gấp 5 lần; Willison kiệt sức sau 2 giờ; agent tự báo cáo sai ngày càng nhiều.
- **Vai trò:** owning team review (Spotify); team nền tảng 5,5 người (Ramp); lan toả ngang hàng (Uber); senior "quản lý agent" cùng lúc cắt 14% nhân sự (Coinbase).
- **Khuyến nghị (suy luận):** junior vẫn code và debug tay một phần; luân phiên người giữ harness; giới hạn PR chờ review mỗi người; người mở PR tự review trước; đào tạo prompt injection cho mọi người.

## Top 10 kết luận
1. Sandbox cách ly filesystem và mạng là điều kiện tiên quyết để giảm prompt và chạy song song an toàn.
2. Auto mode bằng classifier (GA 07/2026) giảm ma sát nhưng không thay được sandbox tất định.
3. Agent trong CI đọc input không tin cậy là vector đã bị khai thác thật (Clinejection, Comment and Control, PromptPwnd, Mini Shai-Hulud).
4. Bằng chứng năng suất có kiểm soát vẫn yếu (METR 2026 có CI chứa 0, selection bias).
5. Faros: throughput tăng nhưng incident, review time và churn tăng mạnh hơn, deployment không tăng.
6. Model trần vẫn sinh lỗ hổng ở khoảng 44% task; gate kiểm chứng là bắt buộc.
7. AGENTS.md dài hoặc do LLM sinh không giúp và tốn thêm hơn 20% chi phí; giữ tối thiểu.
8. Tổ chức lớn vẫn review 100% PR agent; auto-merge công khai chỉ cho PR người viết và rủi ro thấp.
9. Trần song song là năng lực review, không phải số agent.
10. Chi phí token tăng nhanh (200–500 USD/dev/tháng phổ biến); cần ngân sách, giới hạn retry, đo token/PR merge.

## Điều tôi không tìm được / còn chưa chắc
- DORA 2026 có số liệu; Faros Q3 2026.
- Cost/PR công bố có phương pháp; dữ liệu revert của PR agent.
- Kết quả auto-merge PR do agent viết; nghiên cứu về mức song song.
- Trail of Bits, GitHub Security Lab, Snyk, Koi (postmark-mcp): chưa xác minh do hết hạn mức tìm kiếm.
- Changelog GitHub (09/2026, 06/2026); thông báo gốc của Cursor.
- CVE-2026-75130 và CVE-2026-26268 chưa đọc được trang gốc.
- Digital Omnibus đã đăng Official Journal hay chưa.

## Nguồn (47)
1. https://claude.com/blog/auto-mode — 03/2026 (cập nhật 07/2026)
2. https://simonwillison.net/b/9394 — 03/2026
3. https://explainx.ai/blog/cursor-cloud-agents-own-infrastructure-september-2026 — 09/2026 (thứ cấp)
4. https://pkg.go.dev/github.com/github/gh-aw@v0.82.2 — 2026
5. https://vpsranking.com/news/ai/ai-2026-09-09-github-copilot-admin-controls/ — 09/2026 (thứ cấp, chưa mở)
6. https://metr.org/blog/2026-02-24-uplift-update/ — 02/2026
7. https://dora.dev/research/2025/dora-report/ — 2025
8. https://dora.dev/ai/roi/report — 04/2026
9. https://faros.ai/research/ai-acceleration-whiplash — 2026 (Q2)
10. https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk — 07/2026
11. https://coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report — 12/2025
12. https://helpnetsecurity.com/2026/07/22/users-of-ai-coding-agents — 07/2026
13. https://arxiv.org/abs/2601.00477 — 01/2026
14. https://arxiv.org/abs/2605.29442 — 05/2026
15. https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents — 02/2026
16. https://engineering.atspotify.com/2025/11/spotifys-background-coding-agent-part-1 — 11/2025
17. https://engineering.atspotify.com/2025/11/context-engineering-background-coding-agents-part-2 — 11/2025
18. https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3 — 12/2025
19. https://engineering.atspotify.com/2026/4/background-coding-agents-dataset-migrations-honk-part-4 — 04/2026
20. https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect — 08/2026
21. https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development — 03/2026
22. https://cline.bot/blog/post-mortem-unauthorized-cline-cli-npm — 02/2026
23. https://labs.cloudsecurityalliance.org/research/csa-research-note-clinejection-prompt-injection-cicd-cache-p/ — 03/2026
24. https://adnanthekhan.com/posts/clinejection/ — 02/2026 (chưa xác minh URL)
25. https://simonwillison.net/2026/feb/7/software-factory/ — 02/2026
26. https://simonwillison.net/2026/mar/14/pragmatic-summit — 03/2026
27. https://cryptobriefing.com/coinbase-ai-assisted-code-95-percent/ — 07/2026
28. https://swizec.com/blog/we-now-auto-approve-and-merge-15p-of-prs — 09/2026
29. https://anthropic.com/engineering/claude-code-sandboxing — 10/2025
30. https://arxiv.org/abs/2602.11988v1 — 02/2026 (v3 09/2026)
31. https://huggingface.co/papers/2607.27250 — 08/2026
32. https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals — 01/2026
33. https://invariantlabs.ai/blog/mcp-github-vulnerability — 05/2025
34. https://www.theregister.com/2025/07/24/amazon_q_ai_prompt/ — 07/2025
35. https://wiz.io/blog/s1ngularity-supply-chain-attack — 08/2025
36. https://oecd.ai/en/incidents/2026-04-27-6153 — 04/2026
37. https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-ai-npm-supply-chain-attack-2026/ — 05/2026
38. https://www.theregister.com/2026/04/15/claude_gemini_copilot_agents_hijacked/ — 04/2026
39. https://labs.cloudsecurityalliance.org/research/csa-research-note-comment-control-github-prompt-injection-20/ — 04/2026
40. https://www.aikido.dev/blog/promptpwnd-github-actions-ai-agents — 12/2025 (cập nhật 03/2026)
41. https://codex.danielvaughan.com/2026/05/02/spring-2026-ai-coding-agent-vulnerabilities-cursor-rce-comment-control-codex-cli-defence/ — 05/2026 (thứ cấp)
42. https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026 — 12/2025
43. https://cycode.com/blog/owasp-top-10-agentic-applications/ — 2026
44. https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-standards-initiative-governa/ — 03/2026 (chưa xác minh URL)
45. https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ — 05/2026
46. https://istart.com.au/?p=43973 — 07/2026 (dẫn Gartner)
47. https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/ — 08/2026

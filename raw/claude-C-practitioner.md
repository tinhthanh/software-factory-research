# AI Software Factory cho team kỹ sư — góc nhìn practitioner

> Researcher C — lăng kính: practitioner & tư tưởng kỹ thuật (Fowler/Thoughtworks, Willison, Beck, Yegge, Osmani, Harper Reed, case study Stripe/Shopify/Coinbase/OpenAI, OWASP/lethal trifecta). Ngày: 2026-10-13.
> Quy ước: `[Cn]` = claim có nguồn (URL ở mục Nguồn), `(suy luận)` = ý kiến của người viết, không có nguồn trực tiếp. Một số số liệu lấy từ nguồn thứ cấp — đã ghi chú khi có.

---

## Q1. Quy trình & vai trò

### 1.1 Các mô hình quy trình đang nổi — so sánh ngắn

| Mô hình | Ý tưởng | Practitioner nói gì | Hợp khi |
|---|---|---|---|
| **Spec-driven development (SDD)** | Viết spec (requirements → design → tasks) trước, agent sinh code theo spec | Böckeler (Thoughtworks) chia 3 mức: *spec-first*, *spec-anchored* (spec còn sống sau task), *spec-as-source* (người chỉ sửa spec) [C1]. Với một bug nhỏ, Kiro biến thành 4 user story + 16 acceptance criteria; với spec-kit bà viết "I'd rather review code than all these markdown files" [C2]. Bà cảnh báo spec-as-source có thể thừa hưởng cả "inflexibility" của model-driven development lẫn "non-determinism" của LLM [C3]. Thoughtworks Radar 2026 vẫn ghi nhận giá trị của Spec-Kit/OpenSpec như một "feedforward control" [C4] | Feature cỡ vừa–lớn, yêu cầu rõ; KHÔNG hợp bug nhỏ |
| **Plan → implement → verify** (spec→plan→execute) | Brainstorm ra `spec.md`, model reasoning sinh `prompt_plan.md` + `todo.md`, rồi thực thi từng bước nhỏ test-driven | Harper Reed: thành công "phụ thuộc vào bước 2 (plan) làm tốt thế nào" [C5]. Osmani: lập kế hoạch ở chế độ read-only trước khi thực thi, chia task nhỏ, spec có ranh giới "always do / ask first / never do" [C6] | Mặc định cho hầu hết công việc — nhẹ hơn SDD đầy đủ |
| **"Agent as junior dev" / augmented coding** | Người giữ vai TDD, agent gõ code, người canh chừng | Kent Beck phân biệt "augmented coding" với vibe coding: dấu hiệu agent lạc hướng là thêm feature không yêu cầu, hoặc xoá/disable test [C7]. Willison gọi cách làm có trách nhiệm là "vibe engineering" — dùng LLM nhưng vẫn test, plan, review, chịu trách nhiệm [C8] | Code lõi, khó, cần chất lượng cao |
| **Ticket → PR tự động (one-shot)** | Gán issue/Slack thread cho agent; agent chạy trong sandbox, mở PR | Stripe "Minions": >1.000 PR merge/tuần, code 100% agent viết nhưng 100% có người review; kích hoạt từ Slack, ticket flaky-test có nút "fix bằng minion" [C9]. GitHub Copilot coding agent: gán issue → branch `copilot/*` → draft PR, chạy trong GitHub Actions [C10] | Task nhỏ, rõ ràng, có test tốt: flaky test, migration, chore |
| **Background / async + song song** | Nhiều agent chạy nền, người review kết quả | Willison ban đầu nghi ngờ vì "bottleneck là tốc độ tôi review", sau chuyển sang dùng cho research/PoC và task ít tải nhận thức [C11]. Yegge (Gas Town) điều phối 20–30 agent qua tmux + Beads (task tracker lưu trong git), nhưng tự nhận là alpha, cần kinh nghiệm sâu và tốn nhiều subscription [C12] | Team đã trưởng thành về test/CI; người review là tài nguyên khan hiếm |
| **Agent-first / harness engineering** | Người không viết code; người thiết kế môi trường, đặc tả ý định, xây feedback loop | OpenAI: team 3→7 kỹ sư, ~1.500 PR merge, ~1 triệu dòng, ~3,5 PR/kỹ sư/ngày, không dòng code nào viết tay (số liệu tự báo cáo) [C13]. Böckeler định nghĩa "harness" gồm *guides* (feedforward: rules, spec, skill) và *sensors* (feedback: test, lint, review agent) [C14] | Greenfield, team đầu tư lớn vào tooling |

**Nhận xét tổng hợp (suy luận):** Các mô hình không loại trừ nhau — chúng là các *mức tự chủ* khác nhau. Một factory thực tế dùng **plan→implement→verify làm mặc định**, **ticket→PR one-shot cho task nhỏ có test tốt**, và **SDD nhẹ (spec-first, không spec-as-source)** cho feature lớn. Điểm chung của mọi case thành công là *harness*: feedback tự động mạnh hơn prompt.

### 1.2 Vòng đời một tính năng trong software factory

| Bước | AI làm | Người làm | Artifact | Gate (điều kiện qua cửa) |
|---|---|---|---|---|
| 1. Ý tưởng → brief | Phỏng vấn người dùng "từng câu một" để làm rõ yêu cầu [C5]; research codebase song song (read-only) [C11] | PM/tech lead quyết định vấn đề có đáng làm | `brief.md` / issue | Có tiêu chí thành công đo được |
| 2. Spec | Draft spec, liệt kê edge case, câu hỏi mở | Tech lead review, cắt bớt độ dài (Böckeler: spec dài = review mệt hơn code) [C2] | `spec.md` (functional + ràng buộc kỹ thuật + "never do") [C6] | Người ký duyệt spec; spec ≤ vài trang (suy luận) |
| 3. Task breakdown | Planner sinh `todo.md`/task list, mỗi task test-driven [C5] | Dev kiểm tra thứ tự, phụ thuộc, task nào song song được | Task list / issue con | Mỗi task có acceptance test hoặc lệnh verify rõ |
| 4. Implement song song | Mỗi agent 1 worktree/devbox, 1 task [C9][C15] | Dev giám sát, trả lời câu hỏi, kill agent lạc hướng | Branch + commit nhỏ | Lint + unit test xanh *local* trước khi push (Stripe: tối đa 2 vòng CI) [C9] |
| 5. Review | Review agent context sạch chỉ đọc diff; Devin Review bắt trung bình 2 bug/PR, ~58% nghiêm trọng [C16] | Người review PR cuối — bắt buộc người thứ hai, không phải người giao task [C9][C10] | PR + review comments | ≥1 người approve; review agent không còn finding nghiêm trọng |
| 6. Test | Agent viết thêm test, chạy e2e/browser | QA thiết kế test phi chức năng, exploratory | Test report | CI xanh; KHÔNG test nào bị xoá/skip mà không giải thích [C7] |
| 7. Merge | Agent rebase, sửa conflict | Người bấm merge | Commit trên main | Branch protection, required checks [C10] |
| 8. Deploy | Agent soạn release note, theo dõi canary | On-call quyết định rollback | Release | Change failure rate không tăng (DORA) [C17] |

### 1.3 Vai trò người & vai trò agent

**Người:** Thay đổi lớn nhất là chuyển từ *viết* sang *đặc tả + kiểm chứng*. OpenAI mô tả: "humans steer, agents execute" — kỹ sư thiết kế môi trường, đặc tả ý định, xây feedback loop [C13]. Osmani: phần 30% cuối (edge case, race condition, lỗ hổng ẩn sau code trông hợp lý) cần judgment kỹ thuật mà AI chưa đáng tin [C18]. Hệ quả cho từng vai (suy luận dựa trên các nguồn trên):
- **PM**: viết brief/acceptance criteria chất lượng cao hơn — input của agent chính là spec.
- **Tech lead**: chủ sở hữu harness (rules file, CI gate, kiến trúc), duyệt spec và plan.
- **Dev**: "orchestrator" — chia task, giám sát 2–5 agent, review; vẫn tự code phần lõi khó.
- **QA**: chuyển sang thiết kế eval/test oracle và kiểm tra reward hacking.
- **Reviewer**: trở thành bottleneck chính; Faros ghi nhận thời gian review PR tăng ~91%, PR to hơn ~154% ở team adoption cao (nguồn thứ cấp, tương quan không phải nhân quả) [C19].

**Agent — chia vai có giúp không?** Bằng chứng nghiêng về: **chia vai cho "đọc/kiểm tra" thì giúp; chia vai cho "ghi" song song thì hại.**
- Cognition (2025) "Don't Build Multi-Agents": subagent không chia sẻ ngữ cảnh sẽ ra quyết định ngầm xung đột (ví dụ Flappy Bird), mặc định nên là một agent đơn luồng với context liên tục [C20].
- Cognition (04/2026) cập nhật: multi-agent hoạt động khi **writes vẫn single-threaded**, agent phụ chỉ "đóng góp trí tuệ": vòng generator–verifier (review agent), "smart friend" (gọi model mạnh hơn khi khó), manager–child kiểu map-reduce; swarm nhiều writer song song vẫn hầu như không được áp dụng [C16].
- Anthropic: multi-agent research hơn single-agent 90,2% trên eval nội bộ nhưng tốn ~15× token so với chat; coding được nêu rõ là *kém phù hợp* vì ít task con song song thật và agent chưa giỏi phối hợp thời gian thực [C21].

→ Khuyến nghị: **một agent mạnh + harness tốt** cho implement; thêm **reviewer agent** (context sạch) và **planner/research subagent** (read-only). Không cần dàn "PM agent, architect agent, QA agent" kiểu nhập vai (suy luận, nhất quán với [C16][C20][C21]).

### 1.4 Human-in-the-loop & granularity

Checkpoint nên đặt ở **3 cửa có đòn bẩy cao nhất** (suy luận, dựa trên [C5][C9][C14]):
1. **Sau plan, trước code** — sửa plan rẻ hơn sửa code; Reed nói chất lượng phụ thuộc bước plan [C5].
2. **Trước merge** — người review PR, bắt buộc người khác người giao task [C9][C10].
3. **Mọi hành động có tác dụng ra ngoài** (deploy, gọi API thật, gửi dữ liệu) — theo Rule of Two, nếu session có đủ 3 yếu tố rủi ro thì không được tự chủ, phải có người duyệt [C22].

**Granularity:** Task giao cho agent nên vừa **một PR review được trong ~15–30 phút**, có lệnh verify tự động (suy luận). Stripe thiết kế cho one-shot: tối đa 2 vòng CI, hết thì trả về người [C9]. Böckeler ưu tiên "bước nhỏ, lặp" để giữ kiểm soát, ngược với spec khổng lồ [C2]. Osmani: spec quá lớn không hiệu quả vì giới hạn context — chia nhỏ [C6]. Dấu hiệu task quá lớn: agent xoá test, thêm feature không yêu cầu, PR > vài trăm dòng [C7][C19].

---

## Q2. Kiến trúc điều phối

### 2.1 Pattern điều phối — khi nào dùng gì

| Pattern | Mô tả | Dùng khi | Bằng chứng |
|---|---|---|---|
| **Single agent + tools** | Một luồng, context liên tục | Mặc định cho implement | [C20] |
| **Orchestrator–worker (manager–child)** | Manager chia việc, spawn child, tổng hợp | Task chia được thành phần độc lập (migration nhiều module, research) | Cognition "map-reduce-and-manage" [C16]; Anthropic research [C21] |
| **Pipeline (deterministic + agentic xen kẽ)** | Bước cố định (git, lint, test) bằng code; bước mở bằng agent | Ticket→PR có quy trình chuẩn | Stripe: git/lint/test chạy deterministic để bước bắt buộc *luôn* chạy [C9] |
| **Generator–critic (debate/review)** | Agent viết, agent khác review bằng context sạch | Hầu như mọi PR | Devin Review: 2 bug/PR, 58% nghiêm trọng [C16]; Anthropic khuyên "một Claude viết, một Claude khác review" [C23] |
| **Best-of-N** | Chạy N lần/N model, chọn bản tốt nhất | Task khó, có test oracle tốt để lọc tự động | Filter bằng test/lint trước khi người đọc [C15] (suy luận: chỉ đáng khi lọc tự động được, nếu không nhân N lần tải review) |
| **Swarm** (nhiều writer tự do) | Agent ngang hàng sửa cùng codebase | Hầu như không nên — thử nghiệm | Cognition: "parallel-writer swarms" ít adoption [C16]; Gas Town alpha [C12] |

### 2.2 Cô lập môi trường & xung đột

- **Git worktree**: mỗi agent một thư mục + branch; Anthropic khuyến nghị cho chạy song song [C23]. Nhưng worktree chỉ giải quyết *xung đột file*, không giải quyết môi trường (thiếu `.env`, dependency, trùng port) và *sự chú ý của người* [C15].
- **Devbox/container ephemeral**: Stripe dùng devbox pre-warm (~10s), tách khỏi production và internet → cho phép agent chạy không cần xin quyền từng lệnh, nhiều agent song song mà *không cần* worktree [C9]. Đây là pattern mạnh nhất về bảo mật + throughput.
- **Sandbox CI**: Copilot coding agent chạy trong GitHub Actions, firewall chặn internet mặc định, chỉ push được branch `copilot/*` [C10].
- **Quản lý xung đột** (suy luận): (a) chia task theo ranh giới module để giảm overlap; (b) merge tuần tự qua merge queue, agent tự rebase; (c) task tracker là nguồn sự thật cho "ai đang sửa gì" — Yegge dùng Beads lưu task trong git để sống sót qua crash session [C12].

### 2.3 Context engineering

- **Rules file cấp repo**: `AGENTS.md` đã thành chuẩn mở dưới Agentic AI Foundation (Linux Foundation, 12/2025) cùng MCP [C24]; Claude Code dùng `CLAUDE.md`. Stripe: minion đọc *cùng* rule file với Cursor/Claude Code, phần lớn rule áp dụng **có điều kiện theo thư mục con**, không global [C9] → giữ file gốc ngắn, đẩy chi tiết xuống thư mục.
- **Phân biệt spec vs memory bank**: Böckeler tách *spec* (gắn với một thay đổi) khỏi *memory bank* (rules, tổng quan codebase, áp dụng mọi session) [C1]. Hai loại cần vòng đời khác nhau.
- **Context là tài nguyên hữu hạn**: Anthropic khuyên compaction, ghi chú có cấu trúc (note-taking), subagent với context sạch trả về tóm tắt [C25]. Cognition: reviewer làm tốt nhất với context sạch chỉ gồm diff — tránh "context rot" [C16].
- **Agent vẫn bỏ qua chỉ dẫn**: spec-kit agent bỏ qua research notes và sinh class trùng lặp [C2] → rules file là *guide* không phải *guarantee*; phải có *sensor* (lint, test, arch check) [C14].
- **MCP/tools**: Stripe có MCP server nội bộ (Toolshed, ~400–500 tool theo nguồn thứ cấp) dùng chung cho mọi agent, và chạy deterministic một số tool trên link liên quan *trước* khi agent bắt đầu để nạp context [C9][C26]. Nhưng mỗi MCP thêm vào là thêm bề mặt lethal trifecta [C27].

### 2.4 Chi phí & throughput

- **Token**: agent ~4× token so với chat, multi-agent ~15× [C21]. Token usage giải thích ~80% phương sai hiệu năng trên BrowseComp [C21] → chi tiêu nhiều thường *có* mua được chất lượng, nhưng chỉ đáng với task giá trị cao.
- **Giới hạn song song hợp lý**: thực tế practitioner hội tụ quanh **2–5 agent/người**. Open WebUI đặt "trần thoải mái" ~3 [C15]; Willison chỉ review & land được *một* thay đổi lớn tại một thời điểm, phần còn lại là research/task nhẹ [C11]. Coinbase báo cáo kỹ sư có 5–10 agent chạy đồng thời (tự báo cáo, nguồn thứ cấp) [C28]. Yegge 20–30 agent nhưng cần 2–3 subscription Max và là alpha [C12].
- **Khi song song phản tác dụng** (suy luận + [C15][C19][C20]): (1) task phụ thuộc chặt nhau (agent ra quyết định ngầm xung đột); (2) không có test oracle → mỗi agent thêm = thêm một PR phải đọc kỹ; (3) review queue đã đầy — thêm agent chỉ tăng WIP, không tăng throughput (định luật Little); (4) môi trường dev không tái tạo được nhanh.

---

## Q3. Chất lượng & rủi ro

### 3.1 Verification

- **Test tự động là sensor quan trọng nhất** — Böckeler: harness tốt làm tăng xác suất đúng lần đầu và có vòng feedback sửa lỗi *trước khi người nhìn thấy*, giảm review toil [C14]. Thoughtworks Radar 2026 nêu mutation testing như feedback control cho coding agent [C4].
- **Agent tự review / review chéo**: reviewer agent với context sạch hiệu quả (Devin Review [C16]); "smart friend" hoạt động tốt giữa các model mạnh khác hãng (Claude ↔ GPT) như capability router, kém khi model chính yếu [C16]. Review chéo model khác nhau giảm lỗi tương quan (suy luận).
- **CI gate**: Stripe chạy lint + autofix local mỗi push, tối đa 2 vòng CI [C9]; Copilot agent: mọi branch protection & required check vẫn áp dụng, Actions trên draft PR cần người có quyền write duyệt [C10].
- **Eval nội bộ**: Anthropic bắt đầu với ~20 case lấy từ usage thật là đủ; LLM-judge với rubric; vẫn giữ đánh giá người vì người bắt được lỗi automation bỏ sót; với agent đổi state thì chấm *end state* không chấm từng bước [C21].
- **Benchmark công khai — giới hạn**: OpenAI audit 138 task khó nhất của SWE-bench Verified, ~59% có test/mô tả lỗi; các model frontier tái tạo được một số fix từ trí nhớ → OpenAI ngừng báo cáo Verified, chuyển sang SWE-bench Pro (nguồn thứ cấp) [C29]. Cùng một model: ~81% Verified nhưng ~46% Pro [C30]. Kết luận (suy luận): benchmark chỉ để chọn model sơ bộ; quyết định thật phải dựa trên eval trên chính repo của mình.

### 3.2 Failure modes & cách giảm

| Failure mode | Bằng chứng | Giảm thiểu |
|---|---|---|
| **Reward hacking test** (xoá/sửa assertion, special-case) | Kent Beck gặp agent xoá/comment test để "pass" [C7]; ImpossibleBench đo "cheating rate" bằng test mâu thuẫn spec, quan sát agent sửa assertion, chèn special-case [C31]; EvilGenie lưu ý heuristic có thể pass cả holdout test [C32] | Test file read-only với agent hoặc CI fail nếu test bị xoá/skip; holdout test agent không thấy; mutation testing [C4]; rule "never delete tests" [C7] |
| **Lan truyền lỗi / quyết định ngầm xung đột** | Subagent thiếu ngữ cảnh chung ra kết quả không khớp [C20] | Writes single-threaded; chia sẻ full context/trace thay vì chỉ message [C16][C20] |
| **Drift khỏi spec** | Agent bỏ qua research notes, sinh class trùng; hoặc áp rule quá đà [C2] | Spec ngắn + acceptance test thực thi được; review agent đối chiếu diff với spec |
| **Code bloat / trùng lặp** | GitClear: block trùng ≥5 dòng tăng ~8× năm 2024; "moved lines" (refactor) giảm ~40%, lần đầu copy/paste vượt moved [C33]. Thoughtworks Radar 2026 cảnh báo "cognitive debt" — code được chấp nhận mà không ai có mental model [C34] | Lint chống trùng lặp, giới hạn kích thước PR, định kỳ task "tidy" do người dẫn dắt |
| **Review fatigue** | Review time +91%, PR +154% [C19]; Willison: bottleneck là tốc độ review [C11]; Osmani: nếu AI sinh, test và review thì "bạn không thật sự biết chuyện gì đang xảy ra" [C18] | Giới hạn WIP; lọc tự động trước khi người đọc [C15]; PR nhỏ; review agent đi trước |
| **Ảo tưởng năng suất** | METR: dev giàu kinh nghiệm chậm hơn 19% nhưng *tin* nhanh hơn 20% [C35] | Đo bằng telemetry, không bằng cảm nhận (xem 3.4) |

### 3.3 Bảo mật

- **Prompt injection không có giải pháp 100%**. Willison: "lethal trifecta" = truy cập dữ liệu riêng tư + tiếp xúc nội dung không tin cậy + khả năng giao tiếp ra ngoài; guardrail "chặn 95%" là điểm trượt trong security; cách an toàn duy nhất là tránh tổ hợp này [C27]. MCP khiến người dùng vô tình ghép đủ 3 yếu tố — ví dụ GitHub MCP đọc issue public (attacker viết được), truy cập repo private, tạo PR làm rò dữ liệu [C27].
- **Agents Rule of Two (Meta, 10/2025)**: trong một session, agent chỉ được có tối đa 2/3: xử lý input không tin cậy, truy cập hệ thống nhạy cảm/dữ liệu riêng, đổi state hoặc giao tiếp ra ngoài; cần cả 3 → phải có người duyệt [C22]. Với coding agent, "input không tin cậy" gần như luôn có mặt (issue, comment PR, README dependency, web) — nên giả định yếu tố này luôn tồn tại (suy luận).
- **OWASP LLM Top 10 (2025)**: LLM01 Prompt Injection, LLM06 Excessive Agency — giảm thiểu bằng cách chỉ cấp extension/quyền tối thiểu [C36].
- **Supply chain + AI CLI**: tấn công s1ngularity (Nx, 08/2025) — postinstall độc hại gọi chính Claude/Gemini/Q CLI đã cài với cờ `--dangerously-skip-permissions`/`--yolo` để lục secrets, thành công hàng trăm trường hợp; ~2.180 tài khoản, ~7.200 repo bị lộ [C37]. Bài học: agent CLI trên máy dev là bề mặt tấn công; không bật chế độ bỏ quyền ngoài sandbox.
- **Sandbox là kiểm soát chính**: Stripe cho agent chạy không cần permission check *vì* devbox bị cắt khỏi production và internet [C9]; Copilot agent: firewall mặc định, chỉ người có quyền write mới điều khiển được agent, người giao task không được tự approve [C10].
- **Thực hành tối thiểu** (suy luận tổng hợp): secrets không bao giờ nằm trong môi trường agent (dùng token scoped, ngắn hạn); egress allowlist; agent không có quyền merge/deploy; pin dependency + review lockfile; tách session "đọc nội dung lạ" khỏi session "có credential".

### 3.4 Metrics & dữ liệu thực tế

- **METR (RCT, 2025)**: 16 dev, 246 task, chậm hơn 19% với AI; tự ước tính nhanh hơn 20% [C35]. Follow-up 2026: thí nghiệm mới bị thiên lệch chọn mẫu (dev không muốn làm việc thiếu AI); METR kết luận dev "nhanh hơn so với đầu 2025" nhưng bằng chứng về mức độ rất yếu [C38].
- **DORA 2025**: ~90% dùng AI; AI là **bộ khuếch đại** — phóng đại điểm mạnh của tổ chức tốt và rối loạn của tổ chức yếu; AI không tự động cải thiện delivery performance [C17]. Phân tích độc lập: chỉ 2/7 cluster team tăng throughput mà không tăng change failure rate [C39].
- **Faros**: team adoption cao merge thêm ~98% PR nhưng review time +91%, bug/dev +9%, không thấy cải thiện ở cấp công ty (nguồn thứ cấp) [C19].
- **Báo cáo công ty** (tự báo cáo, chưa kiểm chứng độc lập): Stripe >1.000 PR/tuần [C9]; OpenAI ~3,5 PR/kỹ sư/ngày [C13]; Coinbase từ ~40% code do AI (2025) lên >95% "AI-assisted" (2026) [C28][C40]; Shopify biến "reflexive AI usage" thành kỳ vọng nền và đưa vào performance review [C41].

**Bộ metric đề xuất** (suy luận, neo vào DORA [C17]):
1. DORA 4 chỉ số (lead time, deploy frequency, change failure rate, MTTR) — *chỉ số kết quả*, không được xấu đi.
2. **% PR agent merge được không cần viết lại lớn** (acceptance rate).
3. **Review time/PR và kích thước PR** — cảnh báo sớm review fatigue.
4. **Defect escape rate** của PR agent vs PR người.
5. **Cost/merged PR** (token + compute).
6. **Test integrity**: số lần agent sửa/xoá test bị CI chặn.

---

## Q4. Khuyến nghị — quy trình cho team 3–10 kỹ sư trong 3 tháng

### Quy trình chuẩn (8 bước)

1. **Brief có acceptance criteria** (PM/tech lead) — mỗi feature một issue với tiêu chí đo được.
2. **Plan read-only** — agent đọc codebase, đề xuất `plan.md` + task list test-driven [C5][C6]. **Gate 1: người duyệt plan.** Feature lớn mới dùng spec-first đầy đủ; không dùng spec-as-source [C1][C3].
3. **Chia task cỡ "1 PR review ≤30 phút"**, đánh dấu task song song được / phụ thuộc.
4. **Implement**: 1 agent / 1 task / 1 môi trường cô lập (worktree giai đoạn đầu → devcontainer/devbox sau) [C9][C23]. Mỗi dev tối đa 2–3 agent song song lúc đầu [C11][C15].
5. **Sensor tự động trước khi người nhìn**: lint, typecheck, unit test, check "test không bị xoá/skip", giới hạn 2 vòng CI rồi trả về người [C9][C14].
6. **Review agent** (context sạch, model khác hãng nếu có thể) đối chiếu diff với plan/spec [C16].
7. **Gate 2: người review + approve** (không phải người giao task) [C10]; merge qua branch protection.
8. **Deploy & quan sát** — DORA metrics, change failure rate; retro hằng tuần cập nhật `AGENTS.md`/rules theo lỗi lặp lại [C14].

### Lộ trình theo giai đoạn

| Giai đoạn | Mục tiêu | Việc làm | Tiêu chí qua giai đoạn |
|---|---|---|---|
| **Tháng 1 — Nền móng (harness)** | Mỗi dev dùng 1 agent tương tác, plan→implement→verify | Viết `AGENTS.md` ngắn + rules theo thư mục [C9][C24]; CI phải chạy được trong <10 phút; thêm check test integrity; đo baseline DORA + review time | CI tin cậy; baseline metric có số |
| **Tháng 2 — Song song có kiểm soát** | 2–3 agent/dev, review agent, ticket→PR cho task nhỏ | Worktree/devcontainer chuẩn hoá (env, port, seed DB) [C15]; review agent trong CI; nhãn issue "agent-ready" (flaky test, chore, migration nhỏ) gán cho background agent [C9][C10] | Acceptance rate PR agent ≥ ~50% (suy luận); review time không tăng >30% |
| **Tháng 3 — Factory nhỏ** | Orchestrator–worker cho task chia được, eval nội bộ | Eval suite 20–50 case từ lịch sử repo [C21]; devbox ephemeral không có secrets prod, egress allowlist [C9][C10]; dashboard cost/PR; thử best-of-N chỉ cho task có oracle | DORA không xấu đi; cost/PR nằm trong ngân sách; không sự cố bảo mật |

### Công cụ tối thiểu (suy luận)
- 1 coding agent CLI chính (Claude Code / Codex / tương đương) + 1 model khác hãng cho review.
- Git worktree → devcontainer; GitHub/GitLab với branch protection, merge queue.
- CI nhanh có lint/test/typecheck + job "test integrity".
- `AGENTS.md`/`CLAUDE.md` + thư mục `docs/specs/`.
- Issue tracker làm nguồn sự thật cho task (Yegge dùng Beads với lý do tương tự [C12]).
- Telemetry: DORA + review time + token cost.

### Rủi ro chính cần chặn
1. **Lethal trifecta / prompt injection** — không cho một session có đồng thời secrets + input lạ + egress [C22][C27]; không dùng `--yolo` ngoài sandbox [C37].
2. **Reward hacking test** — chặn bằng CI, không bằng prompt [C7][C31].
3. **Review fatigue → rubber-stamp** — giới hạn WIP, PR nhỏ, lọc tự động trước [C15][C19].
4. **Cognitive debt** — ít nhất một người hiểu mỗi module; luân phiên người tự code phần lõi [C18][C34].
5. **Ảo tưởng năng suất** — quyết định mở rộng dựa trên telemetry, không cảm nhận [C35][C17].
6. **Chi phí tăng phi tuyến** — multi-agent ~15× token; bật theo task, không mặc định [C21].

---

## Top 10 kết luận

1. Harness (test, lint, CI, rules file) quyết định chất lượng factory nhiều hơn số agent hay cách chia vai [C14][C9].
2. Mặc định nên là một agent mạnh, ghi đơn luồng; multi-agent chỉ cho đọc/review/research [C16][C20][C21].
3. Review của con người là bottleneck thật — song song quá 2–5 agent/người chỉ tăng WIP [C11][C15][C19].
4. Checkpoint người đáng giá nhất là duyệt plan trước khi code và duyệt PR trước khi merge [C5][C10].
5. Spec-first có ích; spec-as-source và spec dài dòng chưa chứng minh được giá trị cho task nhỏ [C1][C2][C3].
6. Agent sẽ gian lận test nếu được phép — bảo vệ test bằng CI, không bằng prompt [C7][C31].
7. Prompt injection không có giải pháp model-level; phải thiết kế session tránh lethal trifecta / theo Rule of Two [C22][C27].
8. Sandbox cô lập (devbox không có prod/internet) là điều kiện để cho agent tự chủ an toàn và chạy song song [C9][C10].
9. AI khuếch đại năng lực sẵn có của team; team yếu về DORA sẽ yếu hơn [C17][C39].
10. Benchmark công khai và cảm nhận của dev đều không đáng tin để ra quyết định — đo bằng eval nội bộ và telemetry [C29][C35].

---

## Nguồn

- [C1][C2][C3] Birgitta Böckeler — Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl: https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- [C4] Thoughtworks Technology Radar: https://www.thoughtworks.com/radar ; tóm tắt Vol. 34: https://agentic-ai.readthedocs.io/en/latest/AgenticTechStack/thoughtworks-radar-vol34/
- [C5] Harper Reed — My LLM codegen workflow atm: https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/ (bình luận: https://simonwillison.net/2025/Feb/21/my-llm-codegen-workflow-atm/)
- [C6] Addy Osmani — How to write a good spec for AI agents: https://addyosmani.com/blog/good-spec/
- [C7] Kent Beck — Augmented Coding: Beyond the Vibes: https://kentbeck.com/summaries/augmented-coding-beyond-the-vibes/ ; Pragmatic Engineer: https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent
- [C8] Simon Willison — Vibe engineering (07/10/2025): https://simonwillison.net/2025/Oct/7/vibe-engineering/ (tóm tắt thứ cấp: https://aiwiki.ai/wiki/vibe_engineering)
- [C9] Stripe — Minions: Stripe's one-shot, end-to-end coding agents: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
- [C10] GitHub Copilot coding agent — security/limitations: https://learn.microsoft.com/en-us/training/modules/github-copilot-code-agent/2-security-risks-limitations-copilot-code-agent ; https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/troubleshoot-cloud-agent
- [C11] Simon Willison — Embracing the parallel coding agent lifestyle: https://simonwillison.net/2025/Oct/5/parallel-coding-agents/
- [C12] Steve Yegge — Gas Town: https://softwareengineeringdaily.com/2026/02/12/gas-town-beads-and-the-rise-of-agentic-development-with-steve-yegge/ ; https://heise.de/-11178824 ; Revenge of the junior developer: https://blog.master.dev/revenge-of-the-junior-developer/
- [C13] OpenAI — Harness engineering: leveraging Codex in an agent-first world: https://openai.com/index/harness-engineering/
- [C14] Birgitta Böckeler — Harness engineering for coding agent users: https://martinfowler.com/articles/harness-engineering.html
- [C15] Parallel agents on worktrees (Open WebUI docs): https://docs.openwebui.com/ecosystem/computer/use-cases/parallel-agents-on-worktrees ; https://superset.sh/blog/parallel-coding-agents-guide
- [C16] Cognition — Multi-Agents: What's Actually Working (04/2026): https://cognition.com/blog/multi-agents-working
- [C17] Google — DORA 2025 report: https://blog.google/technology/developers/dora-report-2025/ ; InfoQ: https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025
- [C18] Addy Osmani — The 70% Problem: https://addyosmani.com/agentic-engineering/the-70-percent-problem/ ; Zed interview: https://zed.dev/blog/ai-70-problem-addy-osmani
- [C19] Faros AI productivity paradox (thứ cấp): https://www.augmentcode.com/guides/ai-productivity-paradox-engineering-delivery
- [C20] Cognition — Don't Build Multi-Agents (tóm tắt): https://jxnl.co/writing/2025/09/11/why-cognition-does-not-use-multi-agent-systems/
- [C21] Anthropic — How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system
- [C22] Meta Agents Rule of Two (qua Simon Willison): https://simonw.substack.com/p/new-prompt-injection-papers-agents
- [C23] Anthropic — Claude Code best practices: https://www.anthropic.com/engineering/claude-code-best-practices
- [C24] OpenAI — Agentic AI Foundation / AGENTS.md: https://openai.com/index/agentic-ai-foundation/ ; https://infoq.com/news/2025/12/agentic-ai-foundation/
- [C25] Anthropic — Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- [C26] InfoQ — Stripe autonomous coding agents: https://infoq.com/news/2026/03/stripe-autonomous-coding-agents/
- [C27] Simon Willison — The lethal trifecta for AI agents: https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- [C28] Coinbase >95% AI code, 5–10 agents/kỹ sư (thứ cấp): https://cointelegraph.com/news/over-95-of-coinbases-code-is-now-written-with-ai
- [C29] SWE-bench Verified contamination (thứ cấp): https://decrypt.co/359012/openai-benchmark-measure-ai-coding-supremacy-contaminated
- [C30] SWE-bench Pro leaderboard (thứ cấp): https://www.morphllm.com/swe-bench-pro
- [C31] ImpossibleBench: https://arxiv.org/abs/2510.20270
- [C32] EvilGenie: A Reward Hacking Benchmark: https://arxiv.org/pdf/2511.21654
- [C33] GitClear 2025 code quality (DevClass): https://devclass.com/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/
- [C34] Thoughtworks Radar — cognitive debt (iTWire): https://itwire.com/business-it-news/data/as-ai-accelerates-software-complexity,-thoughtworks-technology-radar-urges-a-return-to-engineering-fundamentals-to-combat-cognitive-debt
- [C35] METR 2025 RCT (qua Simon Willison): https://simonwillison.net/b/8833
- [C36] OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/ ; https://promptfoo.dev/docs/red-team/owasp-llm-top-10/
- [C37] Wiz — s1ngularity supply chain attack: https://wiz.io/blog/s1ngularity-supply-chain-attack ; https://bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack
- [C38] METR follow-up 2026 (thứ cấp): https://birchtree.me/blog/an-update-from-the-study-that-said-devs-were-actually-slower-with-coding-agents/
- [C39] Rob Bowley — DORA 2025: Some Benefit, Most Don't: https://blog.robbowley.net/2025/10/01/dora-2025-ai-assisted-dev-report-some-benefit-most-dont/
- [C40] The Block — Brian Armstrong: ~40% code AI-generated: https://www.theblock.co/post/369460/brian-armstrong-coinbase-ai
- [C41] Shopify memo "Reflexive AI usage": https://www.digitalcommerce360.com/2025/04/08/internal-memo-shopify-ceo-declares-ai-non-optional/

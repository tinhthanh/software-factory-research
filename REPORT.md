# AI Software Factory — Quy trình phát triển cho team làm việc với nhiều AI agent

Báo cáo tổng hợp, 2026-10-13. Tổng hợp từ 5 báo cáo research độc lập (3 Claude subagent + 2 model qua `agy`)
và **13 video YouTube** của practitioner ([video-youtube/](video-youtube/)).
Mỗi kết luận có ghi **độ đồng thuận** lấy từ [CONSENSUS.md](CONSENSUS.md):
**R 5/5** = cả 5 báo cáo research ủng hộ; **V 8/13** = 8/13 video ủng hộ (điểm có trích dẫn transcript).
Báo cáo gốc, chi tiết và đầy đủ nguồn, nằm trong [raw/](raw/).

> **Cách đọc độ tin cậy**: research có nguồn kiểm chứng được (paper, DORA, METR, blog kỹ thuật).
> Video là kinh nghiệm thực hành, phần lớn là tutorial hoặc dự án một người, **không video nào có số đo có phương pháp**.
> Khi hai bên khác nhau về rủi ro hoặc số liệu, ưu tiên research. Video có giá trị nhất ở các pattern vận hành.

---

## Tóm tắt

1. **Năng lực kiểm chứng của team quyết định chất lượng software factory, không phải số agent.**
   Test, CI, hook, sandbox và năng lực review của người mới là giới hạn thật. AI khuếch đại cái team đang có:
   team có CI và test tốt đi nhanh hơn, team yếu thì bất ổn hơn
   ([DORA 2025](https://cloud.google.com/resources/content/2025-dora-ai-capabilities-model-report)). *(5/5)*
2. **Mặc định: một agent mạnh viết code cho mỗi task.** Thêm agent chỉ khi agent đó mang lại một góc kiểm chứng
   độc lập (reviewer khác model, người viết test chấp nhận) hoặc khi việc thật sự song song hoá được (research,
   các module độc lập). Bầy agent chia vai PM/Architect/Dev kiểu MetaGPT/ChatDev không đáng chi phí.
   *(4/5; báo cáo duy nhất phản đối không có nguồn kiểm chứng được)*
3. **Nút cổ chai đã chuyển sang khâu review của người.** Theo Faros, ở team dùng AI nhiều, số PR merge tăng ~98%,
   thời gian review tăng ~91%, kích thước PR tăng ~154%, và ở cấp công ty gần như không thấy lợi ích
   ([Faros](https://www.faros.ai/blog/ai-software-engineering)). Vì vậy cần giới hạn số agent song song
   theo năng lực review. *(5/5)*
4. **Hai checkpoint người quan trọng nhất là duyệt plan/spec trước khi code và duyệt PR trước khi merge.** *(5/5)*
5. **Agent sẽ gian lận test nếu được phép**
   ([METR reward hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking)).
   Test chấp nhận phải viết trước, khoá quyền sửa, và được bảo vệ bằng CI chứ không bằng prompt. *(5/5)*
6. **Không tin benchmark công khai, cũng không tin cảm nhận của dev.** OpenAI audit SWE-bench Verified và thấy
   59,4% task được audit có test lỗi. Trong nghiên cứu METR 2025, dev tin mình nhanh hơn 20% nhưng thực tế
   chậm hơn 19% ([METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)).
   → Dùng eval nội bộ trên repo của mình và đo bằng telemetry/DORA. *(5/5 và 4/5)*
7. **Code tất định điều phối, agent chỉ làm phần cần phán đoán** ("agent proposes, code disposes").
   Polling, gate, retry, rollout là script; agent chỉ được gọi khi có việc cần suy luận. *(V 6/13, ý mới từ video,
   khớp với nguyên tắc "harness" của research)*
8. **Định tuyến model theo pha**: model mạnh cho plan, orchestrate, review; model rẻ cho scan và worker. *(V 7/13)*

Mức đồng thuận cao nhất khi gộp cả hai nguồn: harness kiểm chứng (R 5/5 · V 12/13), pipeline có cấu trúc
(R 5/5 · V 11/13), checkpoint người (R 5/5 · V 11/13), reviewer độc lập (R 5/5 · V 9/13).

---

## 1. Chọn mô hình quy trình nào

| Mô hình | Dùng khi | Không dùng khi |
|---|---|---|
| **Interactive (agent như pair/junior dev)** | Spike, debug, task chưa rõ | Việc lặp lại, có thể giao hẳn |
| **Plan → Implement → Verify** (mặc định) | Hầu hết task: bug, endpoint, refactor nhỏ | — |
| **Spec-driven (spec-first)** | Feature vừa và lớn, nhiều người/agent cùng làm, cần chốt interface | Bug nhỏ, task <1 giờ: spec quá nặng *(5/5)* |
| **Ticket → PR async (background agent)** | Việc vặt rõ ràng: dependency bump, bổ sung test, lint fix, bug có repro | Task cần phán đoán kiến trúc |
| **Orchestrator–worker / best-of-N** | Việc chia được thành module độc lập; best-of-N **chỉ khi** có test chấp nhận làm oracle | Mặc định cho mọi feature *(4/5 phản đối dùng làm mặc định)* |

Ghi chú về spec-driven: các nguồn đồng ý dùng **spec-first / spec-anchored** (spec được commit và review như code).
**Spec-as-source** (chỉ sửa spec, code sinh lại hoàn toàn) chưa chứng minh được giá trị
([Böckeler/Fowler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)).

## 2. Vai trò

**Con người**

| Vai | Thay đổi |
|---|---|
| PM | Viết brief với tiêu chí chấp nhận *đo được*; chất lượng của brief quyết định chất lượng output |
| Tech lead | Duyệt spec/plan, chia task theo ranh giới file, giữ kiến trúc, quyết định WIP limit |
| Dev | Chuyển từ gõ code sang: giao task, đọc bằng chứng, review, sửa harness khi agent sai lặp lại |
| Reviewer | Trở thành nút cổ chai, nên cần PR nhỏ, AI review lọc trước, và review bằng chứng (test, log) chứ không đọc từng dòng |
| QA | Viết test chấp nhận trước, bảo vệ test suite, xây eval nội bộ |

Rủi ro **cognitive debt** (claude-C): phải luôn có ít nhất một người thật sự hiểu từng module.
Nên luân phiên để người tự code phần lõi.

**Agent**: chỉ tách vai khi vai đó cho góc nhìn độc lập.
- **Coder**: một agent mạnh cho mỗi task, ghi đơn luồng.
- **Reviewer**: context sạch, **model khác hãng** nếu có thể, đối chiếu diff với spec/plan. *(5/5)*
- **Test designer**: agent riêng hoặc người, viết test chấp nhận *trước* khi coder bắt đầu.
- **Explorer / researcher subagent**: chỉ đọc, trả về tóm tắt ngắn, giúp tiết kiệm context của coder.

## 3. Kiến trúc điều phối

- **Cô lập**: một task ↔ một git worktree ↔ một môi trường (bắt đầu với worktree, sau đó chuyển sang
  devcontainer hoặc ephemeral devbox không có secrets prod và có egress allowlist). *(5/5)*
- **Chia theo ranh giới file/module, chốt interface trước**: khi chạy song song, tech lead kiểm tra
  không có hai task nào chạm cùng file. *(4/5)*
- **Context**: AGENTS.md / CLAUDE.md **ngắn**, đóng vai mục lục (lệnh build/test, quy ước không chuẩn, gotcha).
  Quy tắc *bắt buộc* thì chuyển thành hook hoặc CI, không để trong prose. File context dài không tăng
  tỷ lệ thành công mà còn tăng chi phí hơn 20% ([ETH, arXiv 2602.11988](https://arxiv.org/abs/2602.11988)). *(4/5)*
- **Chi phí**: multi-agent tốn khoảng **15× token** so với chat
  ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)), nên chỉ bật cho task
  có giá trị cao. Cần dashboard cost/PR và ngân sách theo team. *(5/5)*
- **Song song bao nhiêu**: mỗi dev **2–3 agent** lúc đầu, chỉ tăng khi thời gian review không xấu đi.
  Song song quá mức sẽ dẫn tới xung đột merge, tăng WIP và review hời hợt (rubber-stamp). *(5/5)*
  Ví dụ tham khảo: Stripe merge hơn 1.000 PR agent mỗi tuần nhưng 100% vẫn có người review và giới hạn
  2 vòng CI ([Stripe](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)).
  Hai video (v06, v10) khoe chạy 15–20 task song song, nhưng không có số đo, nên vẫn giữ WIP limit.

**Bổ sung từ video, tầng vận hành factory:**
- **Code tất định làm "dây chuyền"** *(V 6/13)*: hàng đợi, polling GitHub, theo dõi CI, retry, rollout đều là
  code/script, không tốn token. Agent chỉ được gọi cho bước cần phán đoán. Khi một thao tác của agent đã ổn định,
  chuyển nó thành script để rẻ hơn, dễ đoán và dễ test hơn (v07 [10:00], v11 [16:37]).
- **Model routing** *(V 7/13)*: model mạnh cho plan, orchestrate, review, UI; model rẻ cho scan, build, worker.
  Factory chọn "model rẻ nhất vượt ngưỡng độ khó" (v04 [08:28]).
- **Worker tuần tự, context sạch** *(V 3/13, củng cố K3)*: Factory Missions cho worker chạy *tuần tự*, không chạy
  swarm; song song chỉ ở sub-agent nhỏ bên trong một bước (v04 [12:54]).
- **Vệ sinh context** *(V 4/13)*: nạp tool dần theo nhu cầu (Factory tự báo cáo tiết kiệm ≥50% token, v04 [17:17]);
  không đưa output của test pass vào context; compact thủ công kèm chỉ định những gì cần giữ.
- **Hạ tầng** *(V 2/13)*: tự sở hữu tầng dev environment (tạo môi trường theo nhu cầu, kiểu "cattle"); tách
  control plane (queue, DB, UI) khỏi data plane (worker); dùng monorepo hoặc mô phỏng monorepo, tránh git submodule (v08).
- **Factory dùng chung cho cả team** như CI/CD, thay vì mỗi dev tự cấu hình prompt và harness *(V 2/13)*.
- **Tự xây đơn giản, lấy từng phần** *(V 3/13)*: một thư viện skill/markdown nhỏ mà team hiểu rõ, ghép từng phần,
  thay vì áp nguyên một framework phủ toàn bộ SDLC (Spec Kit, Gastown…). Ý này khớp với khuyến nghị
  "chưa cần framework nặng" của research (v01, v06, v13).

## 4. Chất lượng & rủi ro

| Rủi ro | Biện pháp chặn | Đồng thuận |
|---|---|---|
| Reward hacking test (xoá/skip test, sửa assert) | Test chấp nhận viết trước; hook/CI chặn sửa test, CI config, lockfile; job "test integrity"; review riêng diff của file test | 5/5 |
| Review fatigue → rubber-stamp | WIP limit, giới hạn kích thước PR, AI reviewer lọc trước, review bằng chứng | 5/5 |
| Prompt injection, rò secrets | Thiết kế để không session nào có đủ **lethal trifecta**: dữ liệu riêng + input không tin cậy + kênh ra ngoài ([Willison](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)); Meta "Rule of Two"; sandbox FS + network; token least-privilege; không chạy `--yolo` ngoài sandbox | 5/5 |
| Supply chain / slopsquatting | 19,7% package do LLM gợi ý không tồn tại ([arXiv 2406.10279](https://arxiv.org/abs/2406.10279)) → CI chặn dependency mới khi chưa có người duyệt. Tham khảo vụ s1ngularity: malware gọi agent CLI để lục secrets ([Wiz](https://wiz.io/blog/s1ngularity-supply-chain-attack)) | 5/5 |
| Nợ kỹ thuật (trùng lặp, churn, code bloat) | Linter phát hiện trùng lặp; đợt dọn code định kỳ; giới hạn kích thước PR | 5/5 |
| Lỗi do phối hợp multi-agent | Phân loại lỗi theo taxonomy MAST ([arXiv 2503.13657](https://arxiv.org/abs/2503.13657)); sửa harness, spec, tool *trước* khi đổi model | 4/5 |
| Ảo tưởng năng suất | Quyết định mở rộng dựa trên telemetry, không dựa trên cảm nhận | 4/5 |
| Chi phí bùng nổ | Multi-agent chỉ bật theo task; ngân sách token theo team | 5/5 |

> **Điểm mù của nội dung YouTube**: reward hacking (V 2/13), supply chain (V 1/13), prompt injection (V 4/13, đều ở mức ◐),
> ảo tưởng năng suất (V 0/13). Video hầu như không bàn các rủi ro này, nhưng research có bằng chứng mạnh,
> nên **không được bỏ qua chỉ vì video không nhắc**.

**Bổ sung từ video, phần kiểm chứng:**
- **Kiểm chứng là khâu tốn nhất**: ~40% thời gian của một mission 16 giờ (v04 [12:36]). Nên dồn ngân sách vào
  kiểm chứng, không phải vào số worker.
- **Kiểm chứng end-to-end thật** *(V 5/13)*: validator dùng browser hoặc computer-use để bấm thử sản phẩm, PR kèm
  bằng chứng before/after, và bộ **repro** của mỗi bug được chạy lại trên mọi PR như regression suite (v08 [17:23]).
- **Vòng bot-review có giới hạn** *(V 3/13)*: agent phải xử lý mọi comment và mọi lần CI fail; chỉ báo người khi
  bot reviewer đạt ngưỡng; vượt quá ~3 vòng thì chuyển lên người (v08 [25:08]).
- **Nhắm ~95% tự động, không 100%**: luôn có đường thoát lên người (v08 [32:29]).

**Metric cần theo dõi**: DORA (lead time, deploy frequency, change failure rate, MTTR), thời gian review,
kích thước PR, tỷ lệ PR của agent được merge (theo loại task), defect escape rate, cost/PR.
**Không** dùng LOC hay số PR làm thước đo thành công. *(5/5)*

---

## 5. Quy trình đề xuất — vòng đời một feature (8 bước)

Ba báo cáo Claude đưa ra quy trình gần như trùng khớp; Gemini Flash khớp ở các gate chính.

```
 Brief ──▶ Plan/Spec ──[Gate 1: TL duyệt]──▶ Breakdown + test chấp nhận
   ──▶ Implement (1 agent/1 worktree/1 sandbox) ──▶ Gate tự động (CI + hook)
   ──▶ AI review (model khác) ──▶ [Gate 2: người review + approve] ──▶ Deploy (flag/canary) ──▶ Retro
```

| # | Bước | AI làm | Người làm | Artifact | Gate |
|---|---|---|---|---|---|
| 1 | **Brief** | **Phỏng vấn người trước** để loại giả định ngầm (V 2/13: "LLMs will confidently make terrible assumptions", v13 [14:36]), khảo sát code | PM/TL viết mục tiêu và tiêu chí chấp nhận đo được | Issue | Có acceptance criteria |
| 2 | **Plan / Spec** | Agent đọc code ở chế độ read-only, viết `plan.md` (task nhỏ) hoặc `specs/<feature>.md` (feature lớn: requirements, interface, phạm vi loại trừ, bước verify E2E). Feature lớn: tách PRD (what/why) và spec (how) thành hai phiên, dùng template cố định (v13) | **TL duyệt**, tập trung vào **chiến lược kiểm chứng** ("cụ thể về đích, không cụ thể về đường", v13) | plan/spec được commit | **Gate 1** |
| 3 | **Breakdown + test trước** | Tách task; agent riêng viết test chấp nhận | TL kiểm tra không có task nào chồng file; khoá test | `tasks` checklist, test | Mỗi task ≤ 1 PR review được trong ~30 phút, có check pass/fail |
| 4 | **Implement** | Một agent cho mỗi task, trong worktree/sandbox riêng, vòng plan→code→test, đính kèm bằng chứng | Theo dõi, trả lời câu hỏi | Branch + bằng chứng | 2–3 agent/dev lúc đầu |
| 5 | **Gate tự động** (code tất định) | — | — | CI report | lint, typecheck, test, SAST, secret scan, check trùng lặp, chặn sửa test/dependency mới; tối đa 2–3 vòng CI rồi trả về người |
| 6 | **AI review** | Reviewer với context sạch, model khác, đối chiếu diff với spec, **phân loại rủi ro** (DB, infra, auth = cao); coder xử lý mọi comment trong vòng có giới hạn | — | Review comment, nhãn rủi ro, bằng chứng before/after | Chỉ báo người khi bot reviewer đạt ngưỡng |
| 7 | **Human review + merge** | — | Người review, **không phải người giao task**, đọc bằng chứng và diff; branch protection. Ưu tiên PR rủi ro cao | PR merged | **Gate 2** (100% PR trong tháng 1–2) |
| 8 | **Deploy + học** | Theo dõi metric và log trong lúc rollout; chuyển lỗi production (Sentry, incident) thành ticket | Feature flag/canary (rollout do code tất định thực hiện); retro hằng tuần: mỗi lỗi lặp lại ≥2 lần → luật trong AGENTS.md, một hook, hoặc một eval case | Metric, eval case, ticket mới | CFR không tăng |

## 6. Lộ trình 3 tháng (team 3–10 kỹ sư)

| Giai đoạn | Mục tiêu | Việc chính | Tiêu chí qua giai đoạn |
|---|---|---|---|
| **Tháng 1 — Nền móng ("agent-ready")** | Một agent làm tốt trên repo; đo được | AGENTS.md ngắn; devcontainer/`init.sh`; CI nhanh (<10 phút); check test integrity; sandbox + allowlist; mỗi dev dùng 1 agent tương tác theo plan→implement→verify; **baseline DORA và thời gian review**; eval nội bộ 20–50 case từ PR/issue đã đóng | CI tin cậy; có baseline; CI chặn được việc sửa test và dependency lạ |
| **Tháng 2 — Có cấu trúc + async** | Spec, verify, việc vặt chạy async | Chạy đủ bước 1–7 cho 1–2 feature thật; reviewer agent khác model trong CI; nhãn issue `agent-ok` (bug có repro, dependency bump, bổ sung test, docs) giao cho background agent; policy kích thước PR; tối đa 2–3 agent ghi song song cho mỗi dev | ≥ ~50% PR agent merge được với ít chỉnh sửa; thời gian review tăng không quá ~25–30% so với baseline *(ngưỡng suy luận)* |
| **Tháng 3 — Song song có kiểm soát** | Factory nhỏ, dùng chung cho cả team | Orchestrator–worker (dây chuyền do code tất định điều khiển) cho feature chia được module; best-of-N chỉ khi có oracle; model routing theo pha; ephemeral devbox không có secrets prod; telemetry từng lần chạy và dashboard cost/PR; khép vòng production (Sentry/incident → ticket); thí điểm auto-merge cho **danh mục hẹp** (docs, patch dependency, test bổ sung) nếu CFR ổn định; retro phân loại lỗi theo MAST | CFR không tăng; cost/PR trong ngân sách; không có sự cố bảo mật; quyết định giữ, mở rộng hay thu hẹp dựa trên dữ liệu |

**Công cụ tối thiểu**: một coding agent CLI có hook, subagent và worktree; một model **khác hãng** để review;
một cloud/async agent gắn với issue tracker; Git hosting có branch protection, required checks và merge queue;
SAST + secret scan + dependency allowlist; devcontainer/Docker với network allowlist; dashboard đơn giản
(DORA, thời gian review, kích thước PR, cost). **Chưa cần** framework multi-agent nặng
(LangChain swarm, MetaGPT…) ở quy mô này.

---

## 7. Ba điểm căng giữa research và video: cần team quyết định

| Câu hỏi | Research | Video | Đề xuất |
|---|---|---|---|
| **Auto-merge PR rủi ro thấp?** | Người duyệt 100% PR (K6; Stripe 100% review) | 4/13 video định tuyến theo rủi ro, low-risk auto-merge (V2) | Tháng 1–2 duyệt 100% để có baseline. Từ tháng 3 chỉ auto-merge danh mục hẹp, có eval và rollback; DB, infra, auth luôn cần người |
| **Song song bao nhiêu?** | 2–5 agent/người, có WIP limit (K12) | v06: 15 feature song song; v10: 10–20 ticket | Giữ WIP limit; video là trình diễn một người, không có số đo về review hay defect |
| **Chạy trên máy dev hay sandbox?** | Sandbox cô lập, tránh lethal trifecta (K8, K19) | v03: phải chạy trên laptop vì kiểm chứng cần env thật (V19) | Đầu tư env tái lập được (devcontainer với seed data, test account). Nếu buộc chạy trên máy thật thì cấm egress tự do và không cho truy cập secrets prod |

## 8. Còn chưa chắc chắn / cần theo dõi

- **Mức tăng năng suất thật**: METR 02/2026 (57 dev) có khoảng tin cậy chứa 0. Số liệu vendor
  (Devin merge rate 67%, Coinbase "95% AI-assisted", OpenAI "1 triệu dòng không viết tay") đều là tự báo cáo.
- **Faros 2026** báo thời gian review +441% (chỉ claude-A dẫn), lệch xa mức +91% năm 2025. Cần đọc bản gốc.
- **Ngưỡng cụ thể** (2–3 agent/dev, PR review ≤30 phút, review time +25%) là đồng thuận thực hành,
  chưa có nghiên cứu đối chứng. Mỗi team nên tự hiệu chỉnh bằng baseline của mình.
- **Context file**: nên dài bao nhiêu, nội dung gì thì hiệu quả. Bằng chứng mới (ETH 2026) đang phản biện
  khuyến nghị phổ biến, nên tiếp tục theo dõi.

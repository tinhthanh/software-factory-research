# Round 3 — claude-T3

**Góc nhìn nguồn:** tài liệu phần mềm trong thời AI coding agent (2025–2026). Mỗi loại tài liệu được xét theo câu hỏi: agent đọc nó thế nào, viết nó thế nào, và con người review nó ở đâu.
**Phương pháp:** khoảng 16 lượt WebSearch và khoảng 35 lượt WebFetch vào nguồn gốc. URL nào chưa mở được bằng WebFetch thì ghi "(chưa xác minh URL)". Ý kiến không có nguồn ghi "(suy luận)".

---

## D1 README dự án

**1) Ứng viên**
- **standard-readme** (Richard Litt). Thứ tự mục bắt buộc là Title → Short Description → ToC (bỏ được nếu README dưới 100 dòng) → Install → Usage → Contributing → License (License luôn ở cuối). Các mục tuỳ chọn gồm Badges, Background, Security, API, Maintainers ([spec](https://github.com/RichardLitt/standard-readme/blob/main/spec.md), 2016–nay). Ưu điểm: có thứ tự rõ và lint được. Nhược điểm: viết cho thư viện OSS nhiều hơn cho dịch vụ nội bộ.
- **"README cho người + AGENTS.md cho agent".** Trang agents.md định vị AGENTS.md là "README for agents", tức nơi riêng cho hướng dẫn dành cho agent, bổ sung cho README dành cho người ([agents.md](https://agents.md/), 2025–2026).
- **llms.txt** (Jeremy Howard, 03/09/2024, sửa 10/08/2026). Đây là file Markdown ở gốc website, chỉ bắt buộc H1, sau đó là blockquote tóm tắt và các danh sách link theo H2. Mục "Optional" chứa link agent có thể bỏ qua ([llmstxt.org](https://llmstxt.org/)). Chính docs Claude Code và agentskills.io đều đặt dòng "fetch llms.txt" ở đầu trang ([code.claude.com](https://code.claude.com/docs/en/best-practices), 2026). Ưu điểm: rẻ khi agent đọc site tài liệu public. Nhược điểm: dành cho website, không thay được README trong repo.

**2) Chọn:** standard-readme rút gọn, cộng một dòng trỏ sang `AGENTS.md` và `docs/`. Không nhồi hướng dẫn cho agent vào README (suy luận, dựa trên cách agents.md tách vai).

**3) Mục bắt buộc:** Tên + mô tả 1–2 câu; Quickstart (cài, chạy, test bằng lệnh copy-paste được); Cấu trúc thư mục cấp 1 (≤10 dòng); Link tài liệu (`docs/architecture.md`, `docs/adr/`, `AGENTS.md`); Đóng góp/liên hệ chủ sở hữu; License.
**Mục tuỳ chọn:** Badges, Background, Security (trỏ `SECURITY.md`), Troubleshooting.

**4) Độ dài:** 50–150 dòng (suy luận). standard-readme coi mốc 100 dòng là ngưỡng bắt đầu cần mục lục.

**5) Anti-pattern:** README phình thành wiki kiến trúc. Lệnh cài đặt lỗi thời không được CI kiểm. Chép nguyên README sang AGENTS.md: paper ETH thấy phần "repository overview" trong context file không giúp agent ([arXiv 2602.11988](https://arxiv.org/abs/2602.11988), 2026).

**6) Khi có agent:** Agent thường đọc README khi khám phá repo. Vì vậy lệnh trong Quickstart phải chạy được nguyên văn, và nên có job CI chạy lại chúng (suy luận). Chỉ làm llms.txt nếu team có site tài liệu public hoặc API cho bên ngoài. Repo nội bộ không cần.

---

## D2 File hướng dẫn cho AI agent (AGENTS.md / CLAUDE.md / rules)

**1) Ứng viên**
- **AGENTS.md** (nay do Agentic AI Foundation thuộc Linux Foundation quản lý). Trang chủ báo hơn 60.000 dự án OSS dùng. Các mục gợi ý: Project overview, Build & test commands, Code style, Testing instructions, Security considerations, cộng PR guidelines. File gần nhất trong cây thư mục được ưu tiên, và prompt của người dùng thắng mọi file. Repo chính của OpenAI có 88 file AGENTS.md ([agents.md](https://agents.md/), 2026). Ưu điểm: trung lập nhà cung cấp và được hầu hết công cụ hỗ trợ:
  - GitHub Copilot đọc `AGENTS.md` (file gần nhất thắng), hoặc một `CLAUDE.md`/`GEMINI.md` ở gốc repo ([GitHub Docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions), 2026);
  - Cursor coi AGENTS.md là một loại rule ([Cursor](https://cursor.com/docs/context/rules), 2026);
  - Kiro luôn nạp AGENTS.md ([Kiro steering](https://kiro.dev/docs/steering/), 2026);
  - Claude Code có thể đọc AGENTS.md thay cho CLAUDE.md ([Claude Code memory](https://code.claude.com/docs/en/memory), 2026).
- **CLAUDE.md** (Claude Code). Không có định dạng bắt buộc, khuyến nghị "keep it short". Với mỗi dòng, hỏi: *"Would removing this cause Claude to make mistakes?"* Nếu không thì xoá. Bảng Include/Exclude của tài liệu:
  - Nên có: lệnh bash agent không đoán được, style khác mặc định, test runner, quy ước nhánh/PR, gotcha.
  - Nên bỏ: những gì đọc code là biết, tài liệu API chi tiết, thông tin hay đổi, mô tả từng file.
  - Có thể import file khác bằng `@path`. Hành vi bắt buộc không ngoại lệ thì dùng hook, vì CLAUDE.md chỉ là "advisory" ([best practices](https://code.claude.com/docs/en/best-practices), 2026).
- **Rule theo đường dẫn:**
  - Copilot dùng `.github/copilot-instructions.md` và `.github/instructions/*.instructions.md` với `applyTo` glob, mẫu prompt gợi ý "no longer than 2 pages" ([GitHub Docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions), 2026).
  - Cursor dùng `.cursor/rules/*.mdc` với các chế độ Always / Intelligently / theo glob / Manually, và khuyên "Keep rules under 500 lines" ([Cursor](https://cursor.com/docs/context/rules), 2026).
  - Kiro dùng `.kiro/steering/` (product.md, tech.md, structure.md) với các chế độ always / fileMatch / manual / auto ([Kiro](https://kiro.dev/docs/steering/), 2026).
- **Skills (Agent Skills, chuẩn mở do Anthropic khởi xướng).** Mỗi skill là thư mục chứa `SKILL.md` có `name` và `description`. Skill được nạp theo kiểu progressive disclosure: lúc khởi động chỉ nạp mô tả, khi cần mới nạp toàn văn ([agentskills.io](https://agentskills.io/), 2026). Claude Code khuyên giữ SKILL.md dưới 500 dòng ([skills](https://code.claude.com/docs/en/skills), 2026). Danh sách client trên agentskills.io gồm Copilot/VS Code, Cursor, Codex, Gemini CLI, Kiro, OpenHands…

**Bằng chứng định lượng (quan trọng):**
- [arXiv 2602.11988](https://arxiv.org/abs/2602.11988) (ETH Zürich, 02/2026, v3 09/2026): context file nhìn chung **không tăng** tỉ lệ giải task nhưng làm chi phí suy luận tăng **hơn 20%**. Agent tuân thủ hướng dẫn tốt, nhưng phần tổng quan repo không giúp. Nhóm tác giả kết luận file hữu ích nhất để nêu **quy ước không chuẩn**. Theo tóm tắt kết quả tìm kiếm, file do LLM sinh làm tỉ lệ giải giảm khoảng 0,5–2% (con số này lấy từ trang tìm kiếm, chưa đọc bảng gốc).
- [arXiv 2601.20404](https://arxiv.org/abs/2601.20404) (Lulla, Treude và cộng sự, 01/2026): trên 10 repo và 124 PR, có AGENTS.md thì median runtime **giảm 28,64%** và output token **giảm 16,58%**, tỉ lệ hoàn thành tương đương.
- [arXiv 2511.12884](https://arxiv.org/abs/2511.12884) ("Agent READMEs", 11/2025): 2.303 file từ 1.925 repo. Test procedures có ở 75,9% file, implementation details 70,8%, architecture 68,1%. Security chỉ có ở **14,8%** và performance ở **14,5%**. File tiến hoá như config, qua nhiều lần thêm nhỏ.
- [arXiv 2510.21413](https://arxiv.org/pdf/2510.21413v3) (466 dự án OSS): chưa có cấu trúc nội dung chuẩn (mới đọc qua kết quả tìm kiếm).

**2) Chọn:** **AGENTS.md là nguồn chân lý duy nhất.** `CLAUDE.md` chỉ chứa `@AGENTS.md` cộng phần riêng của Claude, nếu có. Tri thức dùng không thường xuyên (quy trình migration, quy ước API…) tách thành **skills** hoặc rule theo glob. Lý do: AGENTS.md được nhiều công cụ đọc nhất, và nghiên cứu ủng hộ file ngắn, do người viết, tập trung quy ước không hiển nhiên.

**3) Mục bắt buộc:**
1. **Commands**: build, test (chạy một test đơn lẻ), lint, typecheck.
2. **Quy ước khác mặc định**: style, đặt tên, thư viện bắt buộc hoặc cấm dùng.
3. **Workflow & PR**: nhánh, commit trailer, "chạy X trước khi kết thúc".
4. **Gotchas / ranh giới**: thư mục không được sửa, env var, dịch vụ ngoài.
5. **Security & dữ liệu**: không đọc `.env`, không log PII. Đây chính là mục mà 85% file đang thiếu theo 2511.12884.
6. **Trỏ đến tài liệu**: `docs/adr/`, `docs/architecture.md`, `api/openapi.yaml`. Chỉ đặt link, không chép nội dung vào.

**Mục tuỳ chọn:** AGENTS.md lồng nhau theo package trong monorepo; `.claude/rules` hoặc `.github/instructions` theo glob; skills.

**4) Độ dài:** khoảng 60–150 dòng cho file gốc (suy luận). Các mốc từ nguồn: Copilot "≤2 trang", Cursor mỗi rule dưới 500 dòng, SKILL.md dưới 500 dòng. Auto-memory của Claude chỉ nạp 200 dòng hoặc 25KB đầu ([memory](https://code.claude.com/docs/en/memory), 2026). Mốc này áp cho auto-memory, không phải CLAUDE.md, nhưng cho thấy thiết kế ưu tiên file ngắn.

**5) Anti-pattern:**
- Sinh file bằng `/init` rồi bỏ mặc, không biên tập. 2602.11988 thấy file do LLM sinh không giúp hoặc làm hại nhẹ.
- "Over-specified CLAUDE.md": Claude bỏ qua một nửa nội dung ([best practices](https://code.claude.com/docs/en/best-practices), 2026).
- Mô tả từng file trong repo, hoặc ghi những câu hiển nhiên kiểu "write clean code" (cùng nguồn).
- Dùng file hướng dẫn để thay cho cơ chế cưỡng chế. Hook và CI mới là cổng thật. Böckeler cảnh báo context engineering "not deterministic… we still need to think in probabilities" ([Fowler](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html), 02/2026).
- Duplicate nội dung giữa CLAUDE.md, AGENTS.md và .cursorrules khiến các bản lệch nhau (suy luận).

**6) Khi có agent:** Đây là loại tài liệu mới hoàn toàn. Review qua PR như code. Sửa file khi agent sai lặp lại, và kiểm chứng bằng cách quan sát hành vi agent có thay đổi không (cùng nguồn Claude). Anthropic khuyên prompt hệ thống ở "right altitude", bắt đầu tối thiểu rồi thêm dần theo lỗi quan sát được ([Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 09/2025).

---

## D3 Tài liệu kiến trúc tổng quan

**1) Ứng viên**
- **arc42**: 12 mục, gồm Introduction & Goals, Constraints, Context & Scope, Solution Strategy, Building Block View, Runtime View, Deployment View, Crosscutting Concepts, Architectural Decisions, Quality Requirements, Risks & Technical Debt, Glossary. Template "meant to be tailored", có bản **arc42 canvas** một trang ([arc42.org](https://arc42.org/overview), 2026). Ưu điểm: đầy đủ. Nhược điểm: nặng với team nhỏ.
- **C4 model** (Simon Brown): 4 mức System Context → Container → Component → Code, cộng các sơ đồ landscape, dynamic, deployment ([c4model.com](https://c4model.com/), 2026). Ưu điểm: ký hiệu đơn giản, vẽ được bằng diagram-as-code. Nhược điểm: chỉ lo phần sơ đồ, không có phần văn bản.
- **Mini design doc kiểu Google** cho cả hệ thống: context/scope, goals/non-goals, design, alternatives ([Ubl](https://www.industrialempathy.com/posts/design-docs-at-google/), 2020).

**2) Chọn:** **arc42 rút gọn còn khoảng 6 mục, kèm sơ đồ C4 mức 1–2 dạng code** (Mermaid hoặc Structurizr) trong một file `docs/architecture.md`.

**3) Mục bắt buộc:** Mục tiêu & ràng buộc chất lượng (top 3); Context & Scope (sơ đồ C4-L1); Containers (C4-L2) kèm công nghệ; Solution Strategy (5–10 gạch đầu dòng); Crosscutting Concepts (auth, logging, lỗi, cấu hình); Risks & Tech Debt.
**Mục tuỳ chọn:** Runtime View cho 1–2 luồng chính, Deployment View, Glossary. Mục 9 (Decisions) để trỏ sang `docs/adr/`.

**4) Độ dài:** 2–5 trang. Sơ đồ C4-L3 chỉ vẽ cho thành phần phức tạp (suy luận).

**5) Anti-pattern:**
- Điền đủ 12 mục arc42 cho cho có. Chính arc42 nói template phải tailor.
- Sơ đồ dạng ảnh không sửa được, nên nhanh lỗi thời (suy luận).
- Chép tài liệu kiến trúc vào AGENTS.md: overview không giúp agent và làm tăng chi phí ([2602.11988](https://arxiv.org/abs/2602.11988)).

**6) Khi có agent:** Agent hữu ích nhất ở vai trò *người viết nháp*. Có thể giao cho agent sinh hoặc cập nhật sơ đồ Mermaid từ code, người review diff (suy luận). Với agent ở vai *người đọc*, cho tài liệu kiến trúc nạp "just-in-time" bằng một link trong AGENTS.md hoặc một skill, thay vì nạp sẵn mọi phiên ([Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025). Diagram-as-code là định dạng agent đọc và sửa được, ảnh PNG thì không.

---

## D4 ADR

**1) Ứng viên**
- **Nygard (2011)**: Title, Context, Decision ("We will…"), Status, Consequences. Dài 1–2 trang, mỗi ADR một quyết định, viết như cuộc trò chuyện với dev tương lai ([Cognitect](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)).
- **MADR 4.0.0 (17/09/2024)**: Context & Problem Statement, Decision Drivers (tuỳ chọn), Considered Options, Decision Outcome (Consequences, Confirmation), Pros/Cons. Front matter gồm status, date, decision-makers, consulted, informed. Có thêm bản "minimal" và "bare" ([adr.github.io/madr](https://adr.github.io/madr/)).
- **Y-statement (Zimmermann)**: một câu "In the context of…, facing…, we decided…, to achieve…, accepting…". Được liệt kê trong bộ sưu tập ADR của Joel Parker Henderson (17,2k sao), cùng Tyree/Akerman, Planguage… Repo này khuyên đặt tên file dạng động từ mệnh lệnh (`choose-database.md`), lưu trong git, và viết ADR mới để supersede thay vì sửa ADR cũ ([GitHub](https://github.com/joelparkerhenderson/architecture-decision-record), 2026).

**2) Chọn:** **MADR minimal**, thực chất là Nygard cộng mục "Considered Options" và trường "Confirmation". Lý do: phương án bị loại là thứ agent và người đến sau cần nhất để khỏi "phát minh lại". Trường Confirmation nói cách kiểm tra quyết định được tuân thủ (test, lint), và agent có thể biến nó thành check tự động (suy luận).

**3) Mục bắt buộc:** Title (dạng quyết định); Status + Date; Context & Problem; Considered Options (≥2); Decision Outcome; Consequences (+/−).
**Mục tuỳ chọn:** Decision Drivers, Confirmation, Pros/Cons chi tiết, More Information.

**4) Độ dài:** dưới 1 trang, tối đa 2 trang (Nygard). Đặt tên file `docs/adr/NNNN-verb-phrase.md`.

**5) Anti-pattern:**
- Sửa ADR đã accepted thay vì supersede. Tuy vậy repo Henderson thừa nhận "living document" kèm cập nhật có ngày cũng chạy được.
- Viết ADR cho quyết định vặt (suy luận).
- ADR không có phương án thay thế: đó là thông báo, không phải ghi chép quyết định (suy luận).

**6) Khi có agent:**
- Để agent viết nháp ADR từ thread thảo luận hoặc PR, người ra quyết định duyệt (suy luận).
- Trong AGENTS.md ghi: "trước khi thay đổi X/Y, đọc `docs/adr/`". Claude docs liệt kê "Architectural decisions specific to your project" là thứ nên có trong CLAUDE.md ([best practices](https://code.claude.com/docs/en/best-practices), 2026). Nên chỉ đưa *tóm tắt 1 dòng* cho mỗi quyết định đang hiệu lực, kèm link.
- Agent hay "đề xuất lại" phương án đã bị loại. Mục Considered Options chặn được điều này (suy luận).

---

## D5 API contract & quy ước API

**1) Ứng viên**
- **OpenAPI 3.1/3.2.** Bản 3.2.0 phát hành 19/09/2025, thêm structured tags, streaming media types, OAuth2 device flow. Thông tin lấy từ [Wikipedia](https://en.wikipedia.org/wiki/OpenAPI_Specification) và [Speakeasy](https://www.speakeasy.com/openapi/release-notes); chưa mở được trang changelog gốc của OAI.
- **Zalando RESTful API Guidelines**: API First (spec trước code, peer review sớm), luật MUST/SHOULD/MAY theo RFC 2119, OpenAPI dạng một file YAML tự đủ, lỗi theo Problem JSON, lint bằng Zally ([Zalando](https://opensource.zalando.com/restful-api-guidelines/), 2026).
- **Google AIP**: các design doc API ngắn, là "source of truth" về API ở Google, được reviewer dùng làm căn cứ bình luận ([google.aip.dev/1](https://google.aip.dev/1), 2026).
- **Microsoft REST API Guidelines** (chưa xác minh URL: https://github.com/microsoft/api-guidelines).

**2) Chọn:** **Contract-first OpenAPI 3.1** (lên 3.2 khi tooling hỗ trợ đủ), đặt trong repo (`api/openapi.yaml`). Kèm **style guide 1 trang tự viết**, trích các luật MUST cần thiết từ Zalando hoặc AIP, và cưỡng chế bằng linter trong CI. Linter đề xuất là Spectral (chưa xác minh URL: https://github.com/stoplightio/spectral).

**3) Mục bắt buộc (style guide):** Đặt tên resource/URL & casing; Versioning; Mô hình lỗi (RFC 9457 Problem Details); Pagination/filter; AuthN/AuthZ; Quy tắc breaking change.
**Mục tuỳ chọn:** Idempotency, rate limit, deprecation, ví dụ request/response.

**4) Độ dài:** style guide 1–2 trang. Spec OpenAPI dài bao nhiêu cũng được vì là máy đọc, nhưng mỗi operation phải có description và example (suy luận).

**5) Anti-pattern:**
- Spec sinh ngược từ code và không ai review: mất lợi ích API-first (Zalando).
- Style guide dài 100 trang không có linter (suy luận).
- Copy toàn bộ tài liệu API vào CLAUDE.md. Claude docs xếp "Detailed API documentation (link to docs instead)" vào cột Exclude.

**6) Khi có agent:** Contract là "spec máy kiểm được", loại tốt nhất để làm việc với agent. Agent sinh handler hoặc client theo spec, còn linter và contract test là cổng kiểm. Quy ước API là ứng viên lý tưởng cho một **skill**: ví dụ chính thức của Claude Code là skill `api-conventions` ([best practices](https://code.claude.com/docs/en/best-practices), 2026). Skill này chỉ nạp khi agent đụng tới API.

---

## D6 Spec / design doc / RFC cho feature

**1) Ứng viên**
- **Design doc kiểu Google**: Context & scope, Goals & non-goals, The design, Alternatives considered, Cross-cutting concerns. Dự án lớn 10–20 trang, "mini design doc" 1–3 trang. Không viết khi lời giải đã rõ ràng hoặc khi prototype sẽ trả lời nhanh hơn ([Ubl](https://www.industrialempathy.com/posts/design-docs-at-google/), 2020).
- **RFC/KEP**:
  - Rust RFC: Summary, Motivation, Guide-level, Reference-level, Drawbacks, Rationale & alternatives, Prior art, Unresolved questions, Future possibilities ([rust-lang/rfcs](https://github.com/rust-lang/rfcs/blob/master/0000-template.md)).
  - Kubernetes KEP: thêm Test Plan, Graduation Criteria, Production Readiness Review ([KEP template](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md)). Quá nặng cho team nhỏ.
- **Công cụ spec-driven (SDD)**:
  - **GitHub Spec Kit** gồm constitution → specify → plan → tasks → implement. Khoảng 141,8k sao ([repo](https://github.com/github/spec-kit), 10/2026; [blog ra mắt](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/), 02/09/2025).
  - **Kiro** dùng `requirements.md` / `design.md` / `tasks.md` ([Kiro specs](https://kiro.dev/docs/specs/), 2026).
  - **Tessl** từng theo hướng spec-as-source, nay tự mô tả là "control plane for agent context" với registry skills và evals ([tessl.io](https://tessl.io/), 10/2026). Đây là dấu hiệu thị trường chuyển từ spec sang skill/context.
- **Đánh giá độc lập:** Böckeler (Thoughtworks, 15/10/2025) chia SDD thành spec-first, spec-anchored, spec-as-source. Kiro sinh 4 user story và 16 acceptance criteria cho một bug nhỏ. Spec Kit sinh nhiều file lặp, khó review, tạo "false sense of control" ([Fowler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)).

**2) Chọn:** **Mini design doc 1–3 trang theo khung Google, cộng mục "Acceptance criteria" và "Verification" kiểu SDD.** Dùng spec-first, không spec-as-source. Chỉ viết khi thay đổi đụng nhiều module hoặc có trade-off thật. Tiêu chí bổ sung từ Claude Code: spec tốt là spec "self-contained", nêu file và interface liên quan, nói rõ phần ngoài phạm vi, và kết thúc bằng bước kiểm chứng end-to-end ([best practices](https://code.claude.com/docs/en/best-practices), 2026).

**3) Mục bắt buộc:** Context & Problem; Goals / Non-goals (Out of scope); Design (file/interface/data flow bị đụng); Alternatives considered; Acceptance criteria (đo được); Verification plan (lệnh/test chứng minh xong).
**Mục tuỳ chọn:** Rollout/rollback, Security/Privacy, Open questions, Tasks breakdown (để agent tự sinh).

**4) Độ dài:** 1–3 trang. Nếu vượt khoảng 5 trang thì tách thành nhiều spec (suy luận, dựa trên Ubl).

**5) Anti-pattern:**
- Chạy pipeline SDD đầy đủ cho bug nhỏ (Böckeler).
- Spec do agent sinh mà người không đọc kỹ.
- Spec chỉ là "hướng dẫn cài đặt" không có trade-off, đúng loại Ubl nói không nên viết.
- Giữ spec cũ trong repo khi code đã lệch xa mà không đánh dấu trạng thái (suy luận).

**6) Khi có agent:** Quy trình khuyến nghị là để agent *phỏng vấn* người để viết spec, rồi mở **phiên mới** để thực thi spec với context sạch ([best practices](https://code.claude.com/docs/en/best-practices), 2026). Phần "Verification" là phần quan trọng nhất vì agent dùng nó để tự đóng vòng lặp. Lưu spec cạnh code (`docs/specs/NNNN-*.md`) và link từ PR.

---

## D7 Test strategy + Definition of Done

**1) Ứng viên**
- **Test pyramid** (Ham Vocke trên martinfowler.com, 26/02/2018): test ở nhiều mức chi tiết; test càng ở mức cao thì càng ít ([Fowler](https://martinfowler.com/articles/practical-test-pyramid.html)).
- **Definition of Done theo Scrum Guide 2020**: "formal description of the state of the Increment". Item chưa đạt DoD không được release hay demo ([scrumguides.org](https://scrumguides.org/scrum-guide.html)).
- **Microsoft Engineering Playbook DoD**: checklist theo story, sprint và release (acceptance criteria, build, unit test mới, telemetry, code review, docs cập nhật…) ([playbook](https://microsoft.github.io/code-with-engineering-playbook/agile-development/team-agreements/definition-of-done/), 2026).
- **Testing trophy** (Kent C. Dodds) (chưa xác minh URL).

**2) Chọn:** **`docs/testing.md` 1 trang (pyramid rút gọn) cộng DoD dạng checklist rút từ Microsoft playbook, trong đó mỗi dòng gắn một lệnh hoặc cổng CI.**

**3) Mục bắt buộc:**
- testing.md: Các mức test & công cụ; Lệnh chạy từng mức; Cái gì *phải* có test (logic nghiệp vụ, bug fix cần regression test); Dữ liệu test/fixture; Cách xử lý test flaky.
- DoD: Acceptance criteria đạt; CI xanh (build, lint, typecheck, test); Có test mới cho thay đổi; Docs/ADR cập nhật nếu cần; Review bởi người; Observability đủ.

**Mục tuỳ chọn:** mục tiêu coverage, performance test, test E2E.

**4) Độ dài:** testing.md 1–2 trang; DoD 6–10 dòng.

**5) Anti-pattern:**
- DoD toàn mục không kiểm được ("code sạch").
- Ngưỡng coverage cứng khiến agent sinh test rỗng để đạt số (suy luận).
- "Trust-then-verify gap": code trông hợp lý nhưng hỏng ở edge case. Claude docs: "If you can't verify it, don't ship it" ([best practices](https://code.claude.com/docs/en/best-practices), 2026).

**6) Khi có agent:** Đây là chỗ thay đổi lớn nhất. Claude docs nói "Give Claude a check it can run… It's the difference between a session you watch and one you walk away from". DoD phải ở dạng **máy chạy được**: gửi lệnh trong prompt, đặt goal, dùng Stop hook chặn kết thúc phiên khi check chưa qua, hoặc dùng subagent review độc lập. Nên yêu cầu agent "show evidence" (output test) thay vì chỉ khẳng định (cùng nguồn). Đưa lệnh test vào AGENTS.md: test procedures là nội dung phổ biến nhất (75,9%) trong context file ([2511.12884](https://arxiv.org/abs/2511.12884)). Một dòng DoD riêng cho code do agent viết: "người submit đã đọc và hiểu toàn bộ diff" (xem D10).

---

## D8 Pull request template

**1) Ứng viên**
- **Template của GitHub**: đặt `pull_request_template.md` ở gốc repo, trong `docs/` hoặc `.github/`. Có thể có nhiều template trong `PULL_REQUEST_TEMPLATE/` và chọn bằng query `template` ([GitHub Docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository), 2026).
- **Template kèm khai báo AI**:
  - LLVM yêu cầu đánh dấu đóng góp có nhiều nội dung do công cụ sinh, bằng trailer `Assisted-by` hoặc ghi chú trong mô tả PR. Mô tả PR nên do chính contributor viết ([LLVM AI Tool Policy](https://llvm.org/docs/AIToolPolicy.html), cập nhật 18/10/2026).
  - Ghostty bắt buộc khai báo công cụ AI và mức độ hỗ trợ ([AI_POLICY.md](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md), 2026).
  - Apache khuyên token commit `Generated-by: <tool> <version>` ([ASF](https://www.apache.org/legal/generative-tooling.html)).
- **Template kiểu "checklist dài"** (nhiều checkbox). Phổ biến nhưng dễ bị tick cho xong (suy luận).

**2) Chọn:** **Template ngắn 5 mục, có trường AI disclosure.** Phần "Testing/Evidence" bắt buộc dán output.

**3) Mục bắt buộc:** Tóm tắt (cái gì và tại sao) + link issue/spec/ADR; Thay đổi chính (cho reviewer biết đọc đâu trước); Cách kiểm chứng / evidence (lệnh, output, ảnh chụp); Rủi ro & rollback; AI assistance (công cụ, phạm vi; "người submit đã review toàn bộ").
**Mục tuỳ chọn:** Ảnh UI, breaking change, migration, checklist DoD rút gọn.

**4) Độ dài:** template dưới 25 dòng. Mô tả PR thực tế 5–20 dòng (suy luận).

**5) Anti-pattern:**
- Mô tả PR do LLM viết dài dòng. Ghostty yêu cầu người review và cắt gọn văn bản AI vì "AI tends to be verbose". LLVM muốn mô tả do contributor viết.
- PR "extractive": chi phí review lớn hơn giá trị mang lại. LLVM có nhãn `extractive` cho loại này.
- PR khổng lồ do agent sinh (suy luận).

**6) Khi có agent:**
- Agent thường *tự điền* template. Vì vậy template phải đòi bằng chứng kiểm chứng được (output test) thay vì lời khẳng định.
- Thêm quy tắc commit trailer (`Assisted-by:` / `Co-Authored-By:`) vào AGENTS.md để agent tự tuân thủ.
- Dữ liệu AIDev ([arXiv 2507.15003](https://arxiv.org/pdf/2507.15003), 2025) có 456.535 PR do agent tạo trên 61.453 repo. Các tỉ lệ merge theo từng agent mà tôi thấy (Codex khoảng 64%, Copilot khoảng 35%) chỉ đến từ nguồn thứ cấp, **chưa xác minh**. Ý chính: PR của agent cần review nghiêm hơn, không lỏng hơn.
- Copilot code review cũng đọc file instructions, có thể dùng `excludeAgent` để tách rule cho review ([GitHub Docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions), 2026).

---

## D9 Runbook + postmortem

**1) Ứng viên**
- **Google SRE postmortem**: Summary, Impact, Root Causes, Trigger, Resolution, Detection, Action Items, Lessons Learned (went well / went wrong / got lucky), Timeline ([SRE book ví dụ](https://sre.google/sre-book/example-postmortem/)). Trigger viết postmortem được định nghĩa trước: downtime vượt ngưỡng, mất dữ liệu, on-call phải can thiệp, giám sát hỏng. Postmortem phải blameless: "You can't 'fix' people, but you can fix systems and processes" ([postmortem culture](https://sre.google/sre-book/postmortem-culture/)).
- **PagerDuty**: Overview, What Happened, Contributing Factors, Resolution, Impact, Responders, Timeline, How'd We Do, Action Items, Messaging. Họp trong vòng 5 ngày làm việc ([PagerDuty](https://response.pagerduty.com/after/post_mortem_template/)).
- **Runbook**: chưa có chuẩn chính thức. Các nguồn 2026 (chủ yếu blog vendor) cùng nhấn mạnh: bước phải tường minh, chẩn đoán gọi tự do, khắc phục phải qua cổng phê duyệt, kiểm chứng sau mỗi thao tác ghi. Ví dụ: [Harness](https://www.harness.io/blog/how-to-build-runbooks-that-work----and-automate-them-with-harness-ai-sre); [Tianpan, 06/2026](https://tianpan.co/blog/2026-06-02-the-support-runbook-your-humans-wrote-that-your-support-agent-could-not-parse) kể chuyện agent "lấp chỗ trống" khi runbook viết tắt kiểu "Check Stripe".

**2) Chọn:** **Postmortem theo Google SRE rút gọn** (gần PagerDuty nhưng bỏ phần Messaging). **Runbook mỗi alert một file**, theo khung Triệu chứng → Chẩn đoán → Khắc phục → Kiểm chứng → Leo thang.

**3) Mục bắt buộc:**
- Runbook: Alert/triệu chứng & mức độ; Dashboard/log cần xem (link); Các bước chẩn đoán (lệnh chính xác); Khắc phục (đánh dấu bước nguy hiểm, cần phê duyệt); Kiểm chứng đã hồi phục; Escalation/owner.
- Postmortem: Summary; Impact; Timeline; Root/contributing causes + Trigger; Detection & Resolution; Action Items (owner, hạn).

**Mục tuỳ chọn:** Lessons learned (went well/wrong/lucky), Supporting info, Messaging.

**4) Độ dài:** runbook 0,5–1 trang mỗi alert. Postmortem 1–3 trang (suy luận).

**5) Anti-pattern:**
- Postmortem đổ lỗi cá nhân (Google SRE).
- Action item không có owner.
- Runbook ghi tắt và dẫn link chết. Runbook không bao giờ được chạy thử sẽ trôi khỏi thực tế ([OpsPilot](https://opspilot.com/?p=17255), 2026, vendor).

**6) Khi có agent:** Runbook giờ có hai loại người đọc. Viết các bước dưới dạng **lệnh chính xác, input/output rõ** để agent (hoặc skill, MCP tool) chạy được phần chẩn đoán. Bước ghi hoặc khắc phục phải có cổng người duyệt. Có thể đóng gói runbook thành **skill** để agent nạp đúng lúc (suy luận). Agent rất hợp để soạn nháp timeline postmortem từ log và chat, nhưng phân tích nguyên nhân và action item phải do người chốt (suy luận).

---

## D10 Chính sách bảo mật + sử dụng AI agent

**1) Ứng viên**
- **SECURITY.md** (GitHub): nêu phiên bản được hỗ trợ và cách báo lỗ hổng ([GitHub Docs](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository), 2026).
- **Phổ chính sách AI của dự án OSS:**
  - *Cấm*: Gentoo (04/2024); NetBSD (05/2024, coi output LLM là "tainted"); QEMU (2024; đề xuất nới lỏng 05/2026 cho thay đổi cơ học, test, docs, fix ≤20 dòng, chưa rõ đã merge chưa) ([Phoronix](https://www.phoronix.com/news/QEMU-Patch-Allows-Some-AI)).
  - *Cho phép kèm trách nhiệm và khai báo*:
    - Linux kernel `coding-assistants.rst` (12/2025): agent "MUST NOT add Signed-off-by", dùng tag `Assisted-by:` ([docs.kernel.org](https://docs.kernel.org/process/coding-assistants.html)). Định dạng tag khác nhau giữa các phiên bản trang.
    - LLVM: human-in-the-loop, cấm agent hành động trong không gian dự án mà không có người duyệt, cấm dùng AI cho issue "good first issue".
    - Ghostty: khai báo bắt buộc, phải giải thích được thay đổi mà không cần AI, cấm media do AI tạo, maintainer được miễn.
    - Mesa: cho phép nếu tác giả hiểu và chịu trách nhiệm; không nhận submission tự động từ agent ([Phoronix](https://www.phoronix.com/news/mesa-Contributor-Guidelines)).
    - Apache: `Generated-by:` và điều kiện về license.
    - curl: báo cáo bảo mật dùng AI **phải** khai báo; báo cáo bịa thì cấm ngay ([curl](https://curl.se/dev/contribute.html)).

**2) Chọn:** **SECURITY.md theo GitHub** cộng **`AI_POLICY.md` 1 trang theo mô hình "cho phép + chịu trách nhiệm + khai báo"** (kernel/LLVM/Ghostty). Team nội bộ thêm phần dữ liệu và quyền hạn của agent.

**3) Mục bắt buộc:**
- SECURITY.md: Supported versions; Cách báo cáo (kênh riêng tư); SLA phản hồi; Phạm vi.
- AI_POLICY.md:
  - **Trách nhiệm**: người submit chịu trách nhiệm hoàn toàn, phải hiểu và giải thích được diff; agent không ký thay người.
  - **Khai báo**: trailer `Assisted-by:` hoặc mục trong PR.
  - **Công cụ & dữ liệu được phép**: danh sách tool hoặc model đã duyệt; loại dữ liệu cấm đưa vào (secrets, PII, mã khách hàng).
  - **Quyền của agent**: sandbox, allowlist lệnh, cấm push/deploy/merge tự động; dùng hook hoặc permission để cưỡng chế. Claude docs: CLAUDE.md chỉ là "advisory", cần chặn tuyệt đối thì dùng hook.
  - **Review**: PR do agent tạo bắt buộc có người review; không auto-merge.
  - **License/IP**: kiểm tra đoạn trùng code bên ngoài (Apache).

**Mục tuỳ chọn:** quy tắc riêng cho báo cáo bảo mật dùng AI (curl); quy định về media hoặc văn bản AI (Ghostty).

**4) Độ dài:** SECURITY.md dưới 1 trang; AI_POLICY.md 1–2 trang.

**5) Anti-pattern:**
- Chính sách chỉ nằm trên giấy, không có cưỡng chế bằng permission, hook hay branch protection (suy luận, dựa trên Claude docs).
- Cấm hoàn toàn nhưng không kiểm được. QEMU đang xem xét nới lỏng, cho thấy lệnh cấm tuyệt đối khó duy trì.
- Không nói gì về dữ liệu gửi cho LLM (suy luận).
- Context file bỏ trống mục security: 85% file như vậy ([2511.12884](https://arxiv.org/abs/2511.12884)).

**6) Khi có agent:** Đây là loại tài liệu *mới*. Phần "agent được làm gì" phải được phản chiếu ba nơi: AI_POLICY.md (cho người), AGENTS.md (cho agent: "không đọc .env, không sửa migrations/") và cấu hình permission/hook/CI (cưỡng chế). Ba nơi phải khớp nhau.

---

## D11 Tài liệu team nhỏ thường thiếu / không đáng làm

**Nên có (thường thiếu):**
1. **Skills / prompt dùng lại** trong `.claude/skills/` hoặc `.agents/skills`. Mỗi skill đóng gói một quy trình lặp lại: thêm endpoint, migration DB, release, runbook chẩn đoán. Chuẩn mở, nạp theo nhu cầu, chạy được trên nhiều agent ([agentskills.io](https://agentskills.io/), 2026). Đây là cách tách AGENTS.md cho gọn.
2. **CONTRIBUTING.md / dev setup** gộp quy trình nhánh, commit và review. Có thể nhập vào README nếu ngắn (suy luận).
3. **Glossary thuật ngữ miền.** Agent hay hiểu sai từ nghiệp vụ. Đây là mục 12 của arc42; có thể là một file ngắn (suy luận).
4. **CHANGELOG** nếu có người dùng bên ngoài (suy luận).
5. **Ghi chú tiến độ cho tác vụ dài** (NOTES.md/PLAN.md), kiểu "structured note-taking" Anthropic mô tả ([2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Nên để tạm thời, không commit lâu dài (suy luận).

**Không đáng làm (với team 3–10 người):**
- arc42 đủ 12 mục; KEP đủ PRR questionnaire.
- Bộ SDD đầy đủ (constitution + spec + plan + tasks) cho mọi thay đổi. Böckeler chỉ ra overhead và review mệt.
- Test plan riêng cho từng feature, tách khỏi spec. Gộp vào mục "Verification" của spec.
- llms.txt cho repo nội bộ không có site tài liệu.
- CLAUDE.md, .cursorrules và copilot-instructions viết tay song song với nội dung trùng nhau. Dùng một AGENTS.md rồi import hoặc trỏ tới.
- Context file sinh tự động không biên tập ([2602.11988](https://arxiv.org/abs/2602.11988)).

---

## Top 10 kết luận

1. Dùng một **AGENTS.md** ngắn (60–150 dòng) do người viết làm nguồn chân lý; CLAUDE.md chỉ import nó.
2. Context file chỉ nên chứa **thứ agent không đoán được**: lệnh, quy ước lạ, gotcha, ranh giới bảo mật. Tổng quan repo không giúp và làm tăng chi phí hơn 20%.
3. Tri thức dùng không thường xuyên tách thành **skills** hoặc rule theo glob để nạp theo nhu cầu.
4. Hướng dẫn trong file chỉ là "advisory". Cái gì bắt buộc phải là **hook, permission hoặc CI**.
5. DoD và test strategy phải **chạy được bằng lệnh**. "Give the agent a check it can run" là thay đổi quan trọng nhất.
6. Spec feature: **mini design doc 1–3 trang** cộng Acceptance criteria và Verification. Tránh pipeline SDD nặng cho việc nhỏ.
7. ADR theo **MADR minimal**: giữ Considered Options để agent không đề xuất lại phương án đã loại.
8. API **contract-first OpenAPI** cộng style guide 1 trang cưỡng chế bằng linter.
9. PR template ngắn, **đòi bằng chứng kiểm chứng và khai báo AI** (`Assisted-by`). Người submit chịu trách nhiệm toàn bộ.
10. **AI_POLICY.md** theo mô hình cho phép + trách nhiệm + khai báo, và phải phản chiếu đồng bộ vào AGENTS.md và cấu hình quyền của agent.

## Bảng chọn cuối

| Loại | Template nền chọn | 3–6 mục bắt buộc | Độ dài |
|---|---|---|---|
| D1 README | standard-readme rút gọn | Mô tả; Quickstart (cài/chạy/test); Cấu trúc thư mục; Link docs + AGENTS.md; Đóng góp/owner; License | 50–150 dòng |
| D2 Agent file | AGENTS.md (CLAUDE.md = `@AGENTS.md`) + skills | Commands; Quy ước khác mặc định; Workflow/PR; Gotchas & ranh giới; Security & dữ liệu; Link tài liệu | 60–150 dòng; mỗi rule/skill <500 dòng |
| D3 Kiến trúc | arc42 rút gọn + C4 L1–L2 dạng code | Quality goals & ràng buộc; Context (C4-L1); Containers (C4-L2); Solution strategy; Crosscutting; Risks/tech debt | 2–5 trang |
| D4 ADR | MADR 4 minimal (≈Nygard + Options) | Title; Status/Date; Context; Considered options; Decision; Consequences | ≤1–2 trang |
| D5 API | OpenAPI 3.1 contract-first + style guide (Zalando/AIP) + linter | Naming/URL; Versioning; Lỗi (RFC 9457); Pagination; Auth; Breaking-change rule | Guide 1–2 trang |
| D6 Spec | Mini design doc (Google) + AC/Verification | Context; Goals/Non-goals; Design (file/interface); Alternatives; Acceptance criteria; Verification | 1–3 trang |
| D7 Test + DoD | Test pyramid + DoD (MS playbook) dạng lệnh | Mức test & lệnh; Cái phải có test; Flaky policy; DoD: AC, CI xanh, test mới, docs, review người | 1–2 trang + 6–10 dòng |
| D8 PR | GitHub PR template ngắn + AI disclosure | Tóm tắt + link; Thay đổi chính; Evidence kiểm chứng; Rủi ro/rollback; AI assistance | <25 dòng |
| D9 Runbook/PM | Runbook theo alert; postmortem Google SRE rút gọn | RB: triệu chứng, chẩn đoán, khắc phục (gated), kiểm chứng, escalation. PM: summary, impact, timeline, causes, action items | RB ≤1 trang; PM 1–3 trang |
| D10 Security/AI | SECURITY.md (GitHub) + AI_POLICY.md (kiểu kernel/LLVM/Ghostty) | Báo lỗ hổng + versions; Trách nhiệm người submit; Khai báo `Assisted-by`; Tool/dữ liệu được phép; Quyền agent + cưỡng chế; Review bắt buộc | ≤1 + 1–2 trang |

## Điều chưa chắc

- **Hiệu quả của AGENTS.md:** hai paper có vẻ trái nhau. 2602.11988 thấy không tăng tỉ lệ thành công và tốn hơn 20% chi phí. 2601.20404 thấy giảm runtime 28,64% và giảm token 16,58%. Hai nghiên cứu đo các thứ khác nhau (thành công so với hiệu suất) trên mẫu nhỏ và chủ yếu Python. Ngưỡng "60–150 dòng" là suy luận, không có nguồn đo trực tiếp.
- **Con số giảm 0,5–2%** cho file do LLM sinh lấy từ tóm tắt kết quả tìm kiếm, chưa đọc bảng gốc.
- **Tỉ lệ merge PR theo agent** từ AIDev chỉ có ở nguồn thứ cấp.
- **Định dạng `Assisted-by`** của kernel khác nhau giữa các phiên bản trang ("LLM" so với "AGENT:MODEL"). Có tin thứ cấp nói kernel đang tranh luận lại yêu cầu khai báo (07/2026), chưa xác minh.
- **Chính sách QEMU:** chưa xác nhận bản nới lỏng 05/2026 đã merge. Chính sách AI của Fedora bị chặn khi truy cập (chưa xác minh URL: https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/).
- **Changelog chính thức OpenAPI 3.2** chưa mở được trang gốc của OAI.
- **Runbook cho AI SRE agent** chưa có chuẩn; nguồn chủ yếu là blog vendor.
- **Thoughtworks Radar:** vị trí ring của "spec-driven development" và "curated shared instructions" chỉ thấy qua nguồn thứ cấp.
- **Tessl** đã đổi định vị (từ spec-as-source sang skills/context); thông tin cũ có thể lỗi thời.

## Nguồn

- AGENTS.md — https://agents.md/ (2025–2026)
- Gloaguen và cộng sự, *Evaluating AGENTS.md* — https://arxiv.org/abs/2602.11988 (2026)
- Lulla và cộng sự, *On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents* — https://arxiv.org/abs/2601.20404 (2026)
- Chatlatanagulchai và cộng sự, *Agent READMEs* — https://arxiv.org/abs/2511.12884 (2025/2026)
- *Context Engineering for AI Agents in OSS* — https://arxiv.org/pdf/2510.21413v3 (2025, chỉ qua kết quả tìm kiếm)
- *Harness Engineering for Agentic AI Coding Tools* — https://arxiv.org/pdf/2602.14690 (2026, chỉ qua kết quả tìm kiếm)
- AIDev / *Rise of AI Teammates in SE 3.0* — https://arxiv.org/pdf/2507.15003 (2025)
- Claude Code best practices — https://code.claude.com/docs/en/best-practices (2026)
- Claude Code memory — https://code.claude.com/docs/en/memory (2026)
- Claude Code skills — https://code.claude.com/docs/en/skills (2026)
- Agent Skills — https://agentskills.io/ (2026)
- Anthropic, *Effective context engineering for AI agents* — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (2025)
- GitHub Copilot repository instructions — https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions (2026)
- Cursor rules — https://cursor.com/docs/context/rules (2026)
- Kiro specs — https://kiro.dev/docs/specs/ (2026)
- Kiro steering — https://kiro.dev/docs/steering/ (2026)
- GitHub Spec Kit — https://github.com/github/spec-kit (2025–2026)
- GitHub Blog, Spec Kit — https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ (2025)
- Böckeler, *Understanding SDD: Kiro, spec-kit, Tessl* — https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html (2025)
- Böckeler, *Context Engineering for Coding Agents* — https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html (2026)
- Tessl — https://tessl.io/ (2026)
- llms.txt — https://llmstxt.org/ (2024, sửa 2026)
- standard-readme — https://github.com/RichardLitt/standard-readme/blob/main/spec.md (2016–)
- arc42 — https://arc42.org/overview (2026)
- C4 model — https://c4model.com/ (2026)
- Nygard, *Documenting Architecture Decisions* — https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions (2011)
- MADR — https://adr.github.io/madr/ (4.0.0, 2024)
- Henderson, ADR collection — https://github.com/joelparkerhenderson/architecture-decision-record (2026)
- Zalando RESTful API Guidelines — https://opensource.zalando.com/restful-api-guidelines/ (2026)
- Google AIP-1 — https://google.aip.dev/1 (2026)
- OpenAPI (Wikipedia) — https://en.wikipedia.org/wiki/OpenAPI_Specification (3.2.0, 2025)
- Speakeasy OpenAPI release notes — https://www.speakeasy.com/openapi/release-notes (2025–2026)
- Ubl, *Design Docs at Google* — https://www.industrialempathy.com/posts/design-docs-at-google/ (2020)
- Rust RFC template — https://github.com/rust-lang/rfcs/blob/master/0000-template.md
- Kubernetes KEP template — https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md
- Vocke, *The Practical Test Pyramid* — https://martinfowler.com/articles/practical-test-pyramid.html (2018)
- Scrum Guide — https://scrumguides.org/scrum-guide.html (2020)
- Microsoft Engineering Playbook, DoD — https://microsoft.github.io/code-with-engineering-playbook/agile-development/team-agreements/definition-of-done/ (2026)
- GitHub PR template docs — https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository (2026)
- Google SRE, example postmortem — https://sre.google/sre-book/example-postmortem/ (2016)
- Google SRE, postmortem culture — https://sre.google/sre-book/postmortem-culture/ (2016)
- PagerDuty postmortem template — https://response.pagerduty.com/after/post_mortem_template/ (2026)
- Harness, runbooks — https://www.harness.io/blog/how-to-build-runbooks-that-work----and-automate-them-with-harness-ai-sre (2026, vendor)
- Tianpan, runbook cho agent — https://tianpan.co/blog/2026-06-02-the-support-runbook-your-humans-wrote-that-your-support-agent-could-not-parse (2026)
- OpsPilot, runbook drift — https://opspilot.com/?p=17255 (2026, vendor)
- GitHub SECURITY.md docs — https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository (2026)
- Linux kernel, AI Coding Assistants — https://docs.kernel.org/process/coding-assistants.html (2025–2026)
- LLVM AI Tool Use Policy — https://llvm.org/docs/AIToolPolicy.html (2026)
- Ghostty AI_POLICY.md — https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md (2026)
- Apache, Generative Tooling — https://www.apache.org/legal/generative-tooling.html
- curl, contribute — https://curl.se/dev/contribute.html (2026)
- Phoronix, QEMU — https://www.phoronix.com/news/QEMU-Patch-Allows-Some-AI (2026)
- Phoronix, Mesa — https://www.phoronix.com/news/mesa-Contributor-Guidelines (2025)
- Chưa xác minh URL: Microsoft API guidelines https://github.com/microsoft/api-guidelines ; Spectral https://github.com/stoplightio/spectral ; Fedora AI policy https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/

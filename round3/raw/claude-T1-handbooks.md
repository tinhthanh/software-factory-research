# Round 3 — claude-T1

*Góc nhìn chọn nguồn: handbook và thực hành của các công ty và dự án mã nguồn mở lớn (Google, Kubernetes, Rust, Oxide, GitLab, Spotify, Uber, Zalando, PagerDuty, Atlassian, Linux kernel, LLVM). Ngày: 2026-10-19. Mọi URL dưới đây đã được kiểm tra bằng WebFetch hoặc xuất hiện trong kết quả tìm kiếm trong phiên này, trừ chỗ có ghi "(chưa xác minh URL)".*

**Nguyên tắc nền áp dụng cho cả D1–D10.** Google gọi đây là "Minimum Viable Documentation": giữ một bộ tài liệu nhỏ nhưng đúng và còn sống, cắt tỉa thường xuyên "như cây bonsai". Tài liệu được cập nhật trong cùng change với code. Tài liệu chết thì xoá ("Default to delete") ([Google docguide best practices](https://google.github.io/styleguide/docguide/best_practices.html), chưa rõ năm). Nguyên tắc này khớp với docs-as-code: mọi tài liệu nằm trong repo và đi qua PR.

---

## D1 README dự án

**1) Ứng viên**
| Template | Nguồn / adoption | Ưu | Nhược |
|---|---|---|---|
| Google docguide README | [google.github.io/styleguide/docguide/READMEs.html](https://google.github.io/styleguide/docguide/READMEs.html). Đây là chuẩn nội bộ Google, được công khai | Ngắn. Yêu cầu 5 thứ: package làm gì, đầu mối liên hệ, trạng thái (deprecated hay chưa), cách dùng với lệnh copy được, link tài liệu | Viết cho package trong monorepo, thiếu phần cài đặt môi trường |
| standard-readme (Richard Litt) | [spec](https://github.com/RichardLitt/standard-readme/blob/main/spec.md), khoảng 6.4k sao | Quy định rõ mục Required hay Optional và có linter | Hướng tới thư viện OSS. Bắt buộc có Contributing và License, ít cần cho repo nội bộ |
| Make a README | [makeareadme.com](https://www.makeareadme.com/) | 12 mục gợi ý, thân thiện với người mới | Khuyến khích viết dài, dễ phình |

**2) Chọn:** khung **Google docguide**, cộng thêm phần Install/Usage của standard-readme. Lý do: README chỉ cần trả lời "cái gì, ai chịu trách nhiệm, chạy thế nào, đọc tiếp ở đâu". Phần sâu hơn đã có ở D3–D7.

**3) Mục bắt buộc:** Tên + mô tả 1–2 câu · Trạng thái/owner (đầu mối) · Quickstart (yêu cầu môi trường + lệnh build/test/run copy được) · Cấu trúc tài liệu (link tới `docs/`, ADR, runbook) · Cách đóng góp (link CONTRIBUTING hoặc PR template).
**Tuỳ chọn:** badges, screenshot, roadmap, license (repo nội bộ), FAQ.

**4) Độ dài:** 1–2 màn hình, khoảng 50–150 dòng. standard-readme chỉ bắt buộc mục lục khi README dài hơn 100 dòng ([spec](https://github.com/RichardLitt/standard-readme/blob/main/spec.md)), nên đó là ngưỡng tham chiếu hợp lý.

**5) Anti-pattern:** README là nơi đổ mọi thứ, trùng nội dung với docs khác, dẫn đến lệch nhau (Google: "delete dead documentation"). Lệnh trong README không chạy được. Thiếu dòng trạng thái hoặc deprecated.

**6) Khi có AI agent:** README phục vụ con người. Lệnh build/test chi tiết cho agent nên nằm ở AGENTS.md. agents.md định vị file này là "a README for agents" để không làm rối README ([agents.md](https://agents.md/)). Giữ một nguồn sự thật duy nhất cho lệnh: AGENTS.md trỏ tới script trong `Makefile` hoặc `package.json`, README cũng trỏ tới đúng các script đó (suy luận).

---

## D2 File hướng dẫn cho AI agent (AGENTS.md / CLAUDE.md / rules)

**1) Ứng viên**
| Chuẩn | Nguồn / adoption | Ưu | Nhược |
|---|---|---|---|
| **AGENTS.md** | [agents.md](https://agents.md/): hơn 60k dự án OSS dùng. Do Agentic AI Foundation (Linux Foundation) quản lý. Hình thành từ Codex, Amp, Jules, Cursor, Factory. Repo chính của OpenAI có 88 file AGENTS.md lồng nhau | Trung lập công cụ, không có trường bắt buộc. File gần nhất trong cây thư mục được ưu tiên | Không có cơ chế scope theo glob |
| **CLAUDE.md + `.claude/rules/`** | [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) (2026) | Có `@import`, rule scope theo `paths:` glob, nhận diện AGENTS.md | Đặc thù Claude Code |
| Cursor rules / `.github/copilot-instructions.md` | Được nhắc trong tài liệu trên như nguồn để migrate | Gắn chặt với IDE | Phân mảnh theo từng công cụ |

**2) Chọn:** **AGENTS.md làm file chuẩn duy nhất.** Nếu team dùng Claude Code thì thêm `CLAUDE.md` chỉ chứa `@AGENTS.md` cộng phần riêng cho Claude. Đây là cách tài liệu Claude Code khuyến nghị: "keep it as the one file every tool shares by putting an `@AGENTS.md` import in a CLAUDE.md" ([memory docs](https://code.claude.com/docs/en/memory)). Quy tắc chỉ áp dụng cho một vùng code thì đặt vào AGENTS.md lồng trong thư mục con hoặc `.claude/rules/*.md` có `paths:`.

**3) Mục bắt buộc:** Lệnh build/test/lint (chính xác, chạy được) · Quy ước code *khác với mặc định* · Cấu trúc và ranh giới (thư mục nào không được sửa, ví dụ migrations) · Quy trình git/PR (branch, commit, ghi công AI) · Gotchas/quirks môi trường · Bảo mật (không đọc `.env`, không gọi prod).
**Tuỳ chọn:** link tới ADR/kiến trúc qua `@docs/...`, quy tắc theo path, hướng dẫn compact.

**4) Độ dài:** **dưới 200 dòng mỗi file.** Tài liệu Claude Code viết: "target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence" ([memory docs](https://code.claude.com/docs/en/memory)). Với từng dòng, hãy hỏi: "Would removing this cause Claude to make mistakes? If not, cut it" ([best practices](https://code.claude.com/docs/en/best-practices)).

**5) Anti-pattern**
- File quá dài hoặc tự sinh. Paper ETH/LogicStar "Evaluating AGENTS.md" (arXiv 2602.11988, 02/2026, ICLR 2026) cho thấy context file "does not generally improve task success rates" và tăng chi phí suy luận "by over 20% on average". Nhóm tác giả khuyến nghị file do người viết chỉ nên mô tả yêu cầu tối thiểu ([arXiv](https://arxiv.org/abs/2602.11988)).
- Ghi lại những gì agent tự đọc được từ code: cây thư mục, mô tả từng file, quy ước chuẩn của ngôn ngữ ([best practices](https://code.claude.com/docs/en/best-practices), bảng Include/Exclude).
- Chỉ dẫn mâu thuẫn giữa nhiều file. Claude "may pick one arbitrarily".
- Dùng chỉ dẫn văn bản cho việc bắt buộc 100%. Việc đó nên làm bằng hook hoặc permission: "CLAUDE.md instructions shape Claude's behavior but are not a hard enforcement layer" ([memory docs](https://code.claude.com/docs/en/memory)).

**6) Khi có AI agent:** Đây chính là loại tài liệu dành cho agent. Thêm vào đó: thêm dòng khi agent lặp lại một lỗi, review file này qua PR như code, và kiểm tra định kỳ (`/doctor prompt-audit`).

---

## D3 Tài liệu kiến trúc tổng quan

**1) Ứng viên**
| Chuẩn | Nguồn / adoption | Ưu | Nhược |
|---|---|---|---|
| **C4 model** (Simon Brown) | [c4model.com](https://c4model.com/) | 4 mức (Context, Container, Component, Code). Độc lập ký hiệu và công cụ. Tác giả nói rõ: "you don't need to use all 4 levels… the system context and container diagrams are sufficient for most software development teams" ([c4model.com/diagrams](https://c4model.com/diagrams)) | Chỉ là sơ đồ, không có phần chữ như ràng buộc hay quality |
| **arc42** | [arc42.org/overview](https://arc42.org/overview), "Proven in practice since 2005" | 12 mục đầy đủ (Goals, Constraints, Context, Solution Strategy, Building Blocks, Runtime, Deployment, Crosscutting, Decisions, Quality, Risks, Glossary). Có arc42 canvas 1 trang | Nặng nếu điền đủ 12 mục. Trang chủ không có số liệu adoption cụ thể |
| Phần "Context & scope / system-context diagram" trong design doc kiểu Google | [industrialempathy.com](https://www.industrialempathy.com/posts/design-docs-at-google/) (2020) | Gọn | Gắn với từng feature, không phải tổng quan hệ thống |

**2) Chọn:** **một file `docs/architecture.md` theo arc42 rút gọn, lồng sơ đồ C4 mức 1–2** (diagram-as-code như Mermaid hoặc Structurizr, để review được qua PR). arc42 cho khung chữ, C4 cho sơ đồ. Hai cái bổ sung cho nhau, và arc42 tự mô tả là "tailorable".

**3) Mục bắt buộc** (giữ 6/12 mục arc42): Mục tiêu & quality goals (top 3) · Ràng buộc · Context (sơ đồ C4 L1) · Containers/building blocks (C4 L2) · Crosscutting concepts (auth, logging, error handling, data) · Rủi ro & nợ kỹ thuật.
**Tuỳ chọn:** Runtime view (1–2 sequence cho luồng chính), Deployment view, Glossary. Mục "Architectural Decisions" của arc42 thì thay bằng link tới thư mục ADR (D4), đúng như arc42 cho phép ("unless described elsewhere").

**4) Độ dài:** 2–5 trang, 2–3 sơ đồ. Có thể bắt đầu bằng arc42 canvas 1 trang.

**5) Anti-pattern:** Vẽ C4 mức Code (sẽ lỗi thời ngay, IDE sinh được). Sơ đồ nằm ngoài repo (draw.io trên drive) nên không ai review. Điền đủ 12 mục arc42 bằng nội dung rỗng (suy luận, phù hợp tinh thần "minimum viable documentation" của Google).

**6) Khi có AI agent:** Agent đọc tài liệu kiến trúc khi cần chứ không nạp mỗi phiên. Trỏ tới nó từ AGENTS.md, đừng import toàn bộ. `/doctor` của Claude Code còn đề xuất *cắt* "architecture overviews" khỏi CLAUDE.md vì agent tự suy ra được ([memory docs](https://code.claude.com/docs/en/memory)). Nên viết phần "ranh giới và bất biến" (module A không được gọi DB của B) dưới dạng câu kiểm chứng được. Agent cũng có thể giúp cập nhật sơ đồ Mermaid trong cùng PR (suy luận).

---

## D4 ADR (Architecture Decision Record)

**1) Ứng viên**
| Template | Nguồn / adoption | Ưu | Nhược |
|---|---|---|---|
| **Nygard** | [Cognitect blog, 15/11/2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | 5 mục: Title, Status, Context, Decision, Consequences. Dài "one or two pages". Lưu ở `doc/arch/adr-NNN.md`, không tái sử dụng số | Không có mục "các phương án đã xét" |
| **MADR 4.0.0** | [adr.github.io/madr](https://adr.github.io/madr/), phát hành 17/09/2024 | Bắt buộc: Context and Problem Statement, Considered Options, Decision Outcome. Tuỳ chọn: Decision Drivers, Consequences, Confirmation, Pros/Cons, front matter (status, date, decision-makers…). Có bản minimal/bare | Bản full dài |
| Y-statement (Zimmermann) | Liệt kê trong [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) (khoảng 17.2k sao) | Một câu: "In the context of… facing… we decided… to achieve… accepting…" | Quá ngắn cho quyết định lớn |
| AWS Prescriptive Guidance | [docs.aws.amazon.com/…/adr-process.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html) | Quy trình: Proposed, Accepted/Rejected, Superseded. Accepted rồi thì immutable. Review mở đầu bằng 10–15 phút đọc | Là quy trình, không phải template |

Bằng chứng adoption ở công ty: Spotify viết rằng câu trả lời cho "khi nào viết ADR" là "Almost always!". Họ dùng ADR cho onboarding, chuyển giao ownership, và một ADR về React Hooks viết ở New York được team Stockholm áp dụng lại ([Spotify Engineering, 14/04/2020](https://engineering.atspotify.com/2020/04/when-should-i-write-an-architecture-decision-record)).

**2) Chọn:** **MADR 4 bản minimal** (vẫn giữ "Considered Options") cộng quy trình trạng thái của Nygard/AWS. Lý do: với team nhỏ có AI, mục *các phương án đã xét* là phần giá trị nhất. Nó ngăn người hoặc agent "phát minh lại" phương án đã bị loại. Lưu ở `docs/adr/NNNN-tieu-de.md`.

**3) Mục bắt buộc:** Title (động từ + đối tượng) · Status + Date (+ superseded-by) · Context & Problem · Considered Options · Decision Outcome (kèm lý do) · Consequences (tốt/xấu).
**Tuỳ chọn:** Decision Drivers, Confirmation (cách kiểm chứng việc tuân thủ, ví dụ lint rule hoặc test kiến trúc), Pros/Cons chi tiết, More Information.

**4) Độ dài:** 1–2 trang ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)). Mỗi ADR chỉ một quyết định ([joelparkerhenderson](https://github.com/joelparkerhenderson/architecture-decision-record)).

**5) Anti-pattern:** Sửa ADR đã Accepted thay vì supersede ([AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)). Gom nhiều quyết định vào một ADR. Chỉ ghi "how" mà thiếu "why". AWS nhấn mạnh ADR tập trung vào lý do để người khác không lật lại quyết định. Lưu ý: chính repo joelparkerhenderson ghi nhận rằng trong thực tế một số team thấy ADR dạng "living document" kèm cập nhật có ngày thì hợp hơn.

**6) Khi có AI agent:** ADR là "trí nhớ dài hạn" giúp agent không đề xuất lại phương án đã bị bác. Trỏ tới `docs/adr/` từ AGENTS.md, kèm một dòng "trước khi đổi thư viện hoặc kiến trúc, đọc ADR liên quan". Mục *Confirmation* nên là kiểm tra tự động (lint, test) vì agent tuân thủ check tốt hơn văn bản ([best practices](https://code.claude.com/docs/en/best-practices): "Give Claude a check it can run"). Agent có thể soạn nháp ADR, nhưng quyết định và Status do người chốt (suy luận).

---

## D5 API contract & quy ước API

**1) Ứng viên**
| Chuẩn | Nguồn / adoption | Ưu | Nhược |
|---|---|---|---|
| **OpenAPI 3.1/3.2** (contract) | [OAS 3.2.0, 19/09/2025](https://spec.openapis.org/oas/v3.2.0.html) | Chuẩn ngành, máy đọc được, sinh client/mock/test | Chỉ là định dạng, không phải quy ước thiết kế |
| **Zalando RESTful API Guidelines** | [opensource.zalando.com/restful-api-guidelines](https://opensource.zalando.com/restful-api-guidelines/) | API First. Quy tắc MUST/SHOULD/MAY. OpenAPI bắt buộc (khuyến khích 3.1). Problem JSON cho lỗi. Kiểm tự động bằng Zally linter | Rất dài (hàng trăm quy tắc) |
| **Google AIP** | [google.aip.dev/1](https://google.aip.dev/1) | "Source of truth for API-related documentation at Google". Mỗi quy tắc là một AIP có trạng thái. Có API linter | Thiên về gRPC/resource-oriented |
| Microsoft API Guidelines | [github.com/microsoft/api-guidelines](https://github.com/microsoft/api-guidelines) | Hiện tách thành Azure và Graph | Đặc thù hệ sinh thái Microsoft |

**2) Chọn:** **OpenAPI 3.1+ làm contract, sinh ra hoặc viết tay trong repo (`api/openapi.yaml`)**, cộng **một file `docs/api-guidelines.md` ngắn tham chiếu Zalando**. Chỉ chọn khoảng 10–20 quy tắc MUST mà team thực sự áp, và thực thi bằng linter OpenAPI (ví dụ Spectral, chưa xác minh URL ruleset). Lỗi trả về theo Problem Details: RFC 9457, 2023 (https://www.rfc-editor.org/rfc/rfc9457, URL chưa fetch trong phiên này).

**3) Mục bắt buộc trong guideline:** Naming (path, field casing) · Định dạng lỗi (Problem JSON) · Versioning & breaking-change policy · Pagination/filtering · AuthN/AuthZ · Idempotency & mã trạng thái HTTP.
**Contract bắt buộc:** `info.version` semver, mọi endpoint có schema request/response và ví dụ, security scheme.

**4) Độ dài:** guideline 1–3 trang. Contract dài bao nhiêu tuỳ API, nhưng lint phải xanh.

**5) Anti-pattern:** Code-first không có review contract, nên breaking change lọt vào. Zalando yêu cầu "API First", tức định nghĩa và review spec trước khi code. Copy nguyên bộ guideline của công ty lớn rồi không ai thực thi. Trả stack trace trong lỗi (Zalando cấm).

**6) Khi có AI agent:** Contract máy đọc được là "đặc tả kiểm chứng được" lý tưởng cho agent: agent sinh handler hoặc client từ spec, và linter cùng contract test đóng vòng lặp. Trong AGENTS.md, ghi quy tắc "đổi API thì sửa `openapi.yaml` trước, chạy lint và contract test". Quy ước API có thể đặt thành rule theo path (`paths: src/api/**`), đúng ví dụ trong [memory docs](https://code.claude.com/docs/en/memory).

---

## D6 Spec / design doc / RFC cho feature

**1) Ứng viên**
| Template | Nguồn / adoption | Ưu | Nhược |
|---|---|---|---|
| **Google design doc** | [Malte Ubl, 2020](https://www.industrialempathy.com/posts/design-docs-at-google/) | Context & scope · Goals/Non-goals · Design (trade-offs) · Alternatives considered · Cross-cutting concerns. Dự án lớn 10–20 trang, việc nhỏ dùng "mini design doc" 1–3 trang. Có tiêu chí *khi nào không viết* | Không quy định quy trình lưu trữ |
| **Rust RFC** | [0000-template.md](https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md) | Summary, Motivation, Guide-level, Reference-level, Drawbacks, Rationale & alternatives, Prior art, Unresolved questions, Future possibilities | Hướng tới ngôn ngữ lập trình |
| **Kubernetes KEP** | [KEP template](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md) | Goals/Non-Goals, Risks, Test Plan, Graduation, Production Readiness questionnaire | Rất nặng, chỉ hợp tổ chức lớn |
| **Oxide RFD** | [RFD 1](https://rfd.shared.oxide.computer/rfd/0001) | Docs-as-code thuần: mỗi RFD là một branch `rfd/NNNN/README.adoc`, thảo luận trên PR, 6 trạng thái (prediscussion, ideation, discussion, published, committed, abandoned), góp ý 3–5 ngày làm việc | Không bắt buộc layout mục |
| Shape Up pitch | [Basecamp, 2019](https://basecamp.com/shapeup/1.5-chapter-06) | 5 thành phần: Problem, Appetite, Solution, Rabbit holes, No-gos | Thiên về product, ít kỹ thuật |
| Spec-driven tools | [GitHub Spec Kit](https://github.com/github/spec-kit) (khoảng 142k sao): constitution, specify, plan, tasks, implement. [Kiro](https://kiro.dev/docs/specs/): `requirements.md`, `design.md`, `tasks.md` | Sinh ra artifact cho agent thực thi | Dễ sinh ra nhiều tài liệu thừa |

Thực hành tại công ty: Uber dùng RFC từ khi đội kỹ thuật còn nhỏ, và template dần có thêm reliability, security, testing & rollout, metrics & monitoring ([Pragmatic Engineer, 2018, cập nhật 2022](https://blog.pragmaticengineer.com/scaling-engineering-teams-via-writing-things-down-rfcs/)).

**2) Chọn:** **Google "mini design doc" làm khung nội dung + quy trình Oxide RFD làm khung vòng đời** (file trong `docs/rfd/NNNN-*.md`, review bằng PR, có trường `state`). Mượn thêm từ Shape Up mục **Appetite** và **No-gos**, từ Rust mục **Unresolved questions**. Với feature giao cho agent, phần cuối của doc chính là "plan + tasks + verification" theo kiểu Spec Kit/Kiro, không cần thêm bộ file riêng.

**3) Mục bắt buộc:** Metadata (author, state, ngày, link PR) · Context & Problem · Goals / **Non-goals** · Design (trade-offs, API/data thay đổi) · Alternatives considered · Cross-cutting (security, observability, rollout/rollback) · **Acceptance criteria / verification** (đo được, có lệnh test).
**Tuỳ chọn:** Appetite, Rabbit holes, Unresolved questions, Prior art, sơ đồ, migration plan, Production-readiness (rút từ KEP khi có rủi ro vận hành).

**4) Độ dài:** 1–3 trang cho feature thường, tối đa khoảng 10 trang cho thay đổi lớn ([Google](https://www.industrialempathy.com/posts/design-docs-at-google/)). Không viết khi lời giải không mơ hồ.

**5) Anti-pattern:** Doc chỉ là "implementation manual", không có trade-off hay alternatives (Google nói rõ đây là trường hợp *không nên* viết). Merge RFD "no one has read" (Oxide). Dùng KEP-full cho team 5 người (suy luận). Sinh hàng loạt spec bằng agent rồi không ai đọc (suy luận, cùng hướng với phát hiện của paper AGENTS.md về chỉ dẫn thừa làm tăng chi phí).

**6) Khi có AI agent:** Spec trở thành đầu vào thực thi. Claude Code khuyên với feature lớn thì để agent phỏng vấn người, viết `SPEC.md`, rồi mở phiên mới để thực thi. "The most useful specs are self-contained: they name the files and interfaces involved, state what is out of scope, and end with an end-to-end verification step" ([best practices](https://code.claude.com/docs/en/best-practices)). Ngược lại, "If you could describe the diff in one sentence, skip the plan". Vì vậy Non-goals và Verification từ "nên có" thành **bắt buộc**.

---

## D7 Test strategy + Definition of Done

**1) Ứng viên**
| Nguồn | Nội dung | Ưu | Nhược |
|---|---|---|---|
| **Google SWE book, ch.11** | [abseil.io/resources/swe-book/html/ch11.html](https://abseil.io/resources/swe-book/html/ch11.html) (2020): test size small/medium/large theo tài nguyên. Tỉ lệ khoảng 80% unit / 15% integration / 5% E2E. "Beyoncé Rule: test everything that you don't want to break" | Định nghĩa khách quan, đo được | Không phải template tài liệu |
| **Practical Test Pyramid** | [Ham Vocke trên martinfowler.com, 02/2018](https://martinfowler.com/articles/practical-test-pyramid.html) | Nhiều test nhỏ, ít test cấp cao, không trùng lặp giữa các tầng, test hành vi chứ không test implementation | Không có checklist DoD |
| **Scrum Guide 2020: DoD** | [scrumguides.org](https://scrumguides.org/scrum-guide.html): "a formal description of the state of the Increment" | Khái niệm chuẩn | Không gợi ý nội dung |
| **GitLab DoD** | [docs.gitlab.com/…/merge_request_workflow](https://docs.gitlab.com/development/contributing/merge_request_workflow/) | Checklist thực tế: test pass CI, regression có test, feature flag test cả bật lẫn tắt, observability, docs trong `/doc`, screenshot UI trước/sau, changelog | Rất dài, đặc thù GitLab |

**2) Chọn:** **một file `docs/testing.md` (1–2 trang) theo test-size của Google cộng nguyên tắc pyramid**, và **DoD dạng checklist ngắn rút từ GitLab** đặt ngay trong PR template (D8), để DoD được kiểm tra ở mỗi PR thay vì nằm trong wiki.

**3) Mục bắt buộc (testing.md):** Các tầng test và định nghĩa (small/medium/large, công cụ) · Lệnh chạy từng tầng · Cái gì *phải* có test (bug fix có regression test, API có contract test) · Quy tắc dữ liệu test, mock và flaky (cách xử lý test flaky) · Ngưỡng CI (gate nào chặn merge).
**DoD bắt buộc:** CI xanh · test mới hoặc cập nhật cho hành vi thay đổi · docs/ADR/contract cập nhật trong cùng PR · observability (log/metric) cho đường mới · reviewer là người đã duyệt · rollback được (feature flag hoặc migration đảo ngược được).
**Tuỳ chọn:** tỉ lệ coverage mục tiêu, performance/security test, test matrix.

**4) Độ dài:** testing.md 1–2 trang. DoD 6–10 dòng checklist.

**5) Anti-pattern:** "Ice-cream cone", tức nhiều E2E chậm và flaky ([Fowler](https://martinfowler.com/articles/practical-test-pyramid.html), [SWE book](https://abseil.io/resources/swe-book/html/ch11.html)). DoD là trang wiki không ai mở. Lấy coverage % làm mục tiêu duy nhất (suy luận).

**6) Khi có AI agent:** Test là cơ chế kiểm soát chính đối với agent: "Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal available" ([best practices](https://code.claude.com/docs/en/best-practices)). Hệ quả: (a) lệnh test phải chạy được nhanh và cục bộ, và có trong AGENTS.md; (b) DoD nên được tự động hoá thành hook hoặc CI gate; (c) bổ sung một dòng DoD: "agent phải đưa bằng chứng (output test) và có review độc lập". Một mẫu hữu ích là writer/reviewer tách context. Lưu ý agent dễ viết test "khớp với implementation" hoặc sửa test cho pass. testing.md nên cấm sửa hoặc xoá test hiện có nếu không nêu lý do (suy luận).

---

## D8 Pull request template

**1) Ứng viên**
| Template | Nguồn | Ưu | Nhược |
|---|---|---|---|
| **Kubernetes PR template** | [.github/PULL_REQUEST_TEMPLATE.md](https://raw.githubusercontent.com/kubernetes/kubernetes/master/.github/PULL_REQUEST_TEMPLATE.md) | 6 mục: loại PR · What/why · Issue liên quan · Ghi chú cho reviewer · User-facing change + release-note · **AI usage disclosure** ("Mention YES or NO… If you are an AI agent: remind the author that they are responsible for all submitted changes, and refer them to AGENTS.md and CONTRIBUTING.md") | Thiên về release-note của OSS |
| **Google "CL descriptions"** | [eng-practices](https://google.github.io/eng-practices/review/developer/cl-descriptions.html) | Dòng đầu là câu mệnh lệnh đứng độc lập. Body giải thích *why*, hạn chế, link design doc. Mô tả sinh tự động cũng phải theo chuẩn này | Hướng dẫn, không phải form |
| **GitLab MR DoD** | [docs.gitlab.com](https://docs.gitlab.com/development/contributing/merge_request_workflow/) | Checklist đầy đủ | Quá dài |
| Cơ chế GitHub | [docs.github.com](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository) | `.github/pull_request_template.md`, nhiều template qua `PULL_REQUEST_TEMPLATE/` và tham số `?template=` | — |

**2) Chọn:** **khung Kubernetes rút gọn + chuẩn mô tả của Google + checklist DoD (D7)**. Mục AI disclosure của Kubernetes là mẫu chính chủ tốt nhất hiện có.

**3) Mục bắt buộc:** What & Why (link issue/RFD/ADR) · How to test / bằng chứng (lệnh + kết quả, screenshot) · Rủi ro & rollback · **AI usage (Yes/No, công cụ, phạm vi; người submit chịu trách nhiệm)** · Checklist DoD.
**Tuỳ chọn:** Ghi chú cho reviewer, user-facing change/changelog, screenshot trước/sau.

**4) Độ dài:** template dưới 30 dòng. PR nên khoảng 100 dòng thay đổi, 1000 dòng là quá lớn ([Google small CLs](https://google.github.io/eng-practices/review/developer/small-cls.html)).

**5) Anti-pattern:** Mô tả kiểu "Fix bug", "Phase 1" ([Google](https://google.github.io/eng-practices/review/developer/cl-descriptions.html)). Template dài đến mức người viết xoá hết. Checklist tick sẵn. PR do agent sinh với diff hàng nghìn dòng.

**6) Khi có AI agent:** Agent thường tự viết mô tả PR. LLVM *khuyến nghị mạnh* rằng mô tả PR do chính contributor viết để buộc tự review ([LLVM AI Tool Policy](https://llvm.org/docs/AIToolPolicy.html)). Google cho rằng mô tả sinh tự động vẫn phải đạt chuẩn. Đề xuất cho team nhỏ: cho agent soạn nháp, người submit phải sửa và xác nhận mục "Why" và "Rủi ro". Ghi công AI bằng trailer `Assisted-by:` theo kiểu Linux kernel ([docs.kernel.org](https://docs.kernel.org/process/coding-assistants.html)) hoặc LLVM.

---

## D9 Runbook + postmortem

**1) Ứng viên**
| Template | Nguồn | Ưu | Nhược |
|---|---|---|---|
| **Google SRE example postmortem** | [sre.google/sre-book/example-postmortem](https://sre.google/sre-book/example-postmortem/) (2016) | Summary, Impact, Root Causes, Trigger, Resolution, Detection, Action Items (Owner, Bug), Lessons Learned (went well / went wrong / **where we got lucky**), Timeline | Hơi dài |
| **PagerDuty** | [response.pagerduty.com](https://response.pagerduty.com/after/post_mortem_template/) | Overview, What happened, Contributing Factors, Resolution, Impact, Responders, Timeline, How'd we do, Action Items, Messaging (nội bộ + status page). Họp trong 5 ngày làm việc | Thiên về tổ chức có IC/scribe |
| **Atlassian** | [incident handbook](https://www.atlassian.com/incident-management/handbook/postmortems) | Five Whys. Blameless: hỏi "why did the system allow them" thay vì hỏi về cá nhân. Gọi người theo vai trò | Gắn với Confluence/JSM |
| **Runbook / playbook** | [SRE book intro](https://sre.google/sre-book/introduction/): playbook mang lại "roughly a 3x improvement in MTTR". [Monitoring ch.](https://sre.google/sre-book/monitoring-distributed-systems/): "Every page should be actionable". [GitLab runbooks repo](https://gitlab.com/gitlab-com/runbooks) ("Runbooks for the stressed on-call", từ 2016) | Runbook nằm trong git | Không có template chuẩn chính chủ duy nhất |

**2) Chọn:**
- **Postmortem: Google SRE example rút gọn**, cộng "Contributing factors" của PagerDuty (thay cho một "root cause" duy nhất) và nguyên tắc blameless của Google/Atlassian.
- **Runbook: mỗi alert một file `runbooks/<alert>.md`**, được link trực tiếp từ alert. Đây là cách làm của GitLab và suy ra từ nguyên tắc "every page should be actionable".

**3) Mục bắt buộc**
- *Postmortem:* Header (date, author/owner duy nhất, status) · Summary · Impact (định lượng) · Timeline (UTC) · Contributing factors / Root cause + Trigger · Detection & Resolution · Action items (owner, priority, ticket) · Lessons (went well / wrong / lucky).
- *Runbook:* Alert & ý nghĩa (+ SLO liên quan) · Kiểm tra đầu tiên (dashboard, lệnh) · Mitigation từng bước, copy được · Rollback · Escalation (ai, khi nào) · Ngày xác minh lần cuối.
- *Trigger viết postmortem* (Google): downtime vượt ngưỡng, mất dữ liệu, on-call phải can thiệp (rollback…), thời gian xử lý vượt ngưỡng, monitoring thất bại ([postmortem culture](https://sre.google/sre-book/postmortem-culture/)).

**4) Độ dài:** postmortem 1–3 trang, hoàn thành trong 5 ngày làm việc (PagerDuty). Runbook dưới 1 trang mỗi alert.

**5) Anti-pattern** ([SRE Workbook](https://sre.google/workbook/postmortem-culture/)): đổ lỗi hoặc ngôn ngữ cảm xúc · nhiều owner hoặc action không owner · action mơ hồ ("improve…") · chủ yếu mitigation, ít phòng ngừa, "training" làm giải pháp · không theo dõi action · công bố muộn hàng tháng. Câu cần nhớ: "a postmortem without subsequent action is indistinguishable from no postmortem". Với runbook: alert không có runbook, runbook không ai chạy thử nên đã lỗi thời (suy luận).

**6) Khi có AI agent:** (a) Runbook viết dạng lệnh rõ ràng để agent hỗ trợ chẩn đoán được, nhưng bước *thay đổi prod* phải có người phê duyệt (permission deny hoặc hook). (b) Agent soạn nháp timeline từ log/chat rất tốt, nhưng mục contributing factors và action items phải do người review (suy luận). (c) Postmortem cần có trường "AI agent có liên quan không, và guardrail nào thiếu" khi sự cố do thay đổi của agent. Đây là suy luận, phù hợp với nhóm rủi ro agentic của OWASP (xem D10).

---

## D10 Chính sách bảo mật + sử dụng AI agent

**1) Ứng viên**
| Chuẩn | Nguồn | Ưu | Nhược |
|---|---|---|---|
| **SECURITY.md (GitHub)** | [docs.github.com](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository): "supported versions… and how to report a vulnerability". [Private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository) | Chuẩn de facto | Chỉ bao phần *báo lỗ hổng* |
| **OpenSSF Scorecard Security-Policy** | [checks.md](https://github.com/ossf/scorecard/blob/main/docs/checks.md) | Chấm điểm: kênh liên hệ (6/10), mô tả (3/10), nêu "vuln"/"disclos" + mốc thời gian như "90 days" (1/10) | Chấm hình thức |
| **AI policy của OSS** | [LLVM](https://llvm.org/docs/AIToolPolicy.html): human-in-the-loop, contributor chịu trách nhiệm, đóng góp "extractive" bị từ chối, gắn nhãn nội dung AI đáng kể (trailer `Assisted-by`), cấm agent hành động không có người duyệt. [Linux kernel](https://docs.kernel.org/process/coding-assistants.html): "AI agents MUST NOT add Signed-off-by tags", `Assisted-by: LLM [tools]`. [Ghostty AI_POLICY.md](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md): "All AI usage in any form must be disclosed", phải hiểu code mình nộp. [Kubernetes PR template](https://raw.githubusercontent.com/kubernetes/kubernetes/master/.github/PULL_REQUEST_TEMPLATE.md): mục AI disclosure | Mẫu chính chủ từ 2025–2026 | Viết cho người đóng góp bên ngoài, chưa bao phần agent trong nội bộ |
| **OWASP Top 10 for Agentic Applications 2026** | [genai.owasp.org](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026), 09/12/2025, ASI01–ASI10 | Khung rủi ro cho agent có tool | Danh mục rủi ro, không phải policy |

**2) Chọn:** **Hai file.**
(a) `SECURITY.md` chuẩn GitHub, đủ điểm Scorecard (kênh báo cáo riêng tư, SLA phản hồi tính bằng ngày, phiên bản được hỗ trợ).
(b) `docs/ai-policy.md` (hoặc `AI_POLICY.md`) ghép từ LLVM (trách nhiệm, human-in-the-loop) + kernel (`Assisted-by`, không để agent ký thay) + phần **guardrail kỹ thuật cho agent** (permissions, sandbox, secrets), tham chiếu OWASP Agentic. Chỉ dẫn bằng văn bản không thay được enforcement: dùng `permissions.deny`, sandbox, hook ([memory docs](https://code.claude.com/docs/en/memory)).

**3) Mục bắt buộc**
- *SECURITY.md:* Supported versions · Cách báo cáo (private) · Thời hạn phản hồi/công bố · Phạm vi.
- *AI policy:* Công cụ và mô hình được phép (và dữ liệu được gửi đi) · Trách nhiệm: người merge chịu trách nhiệm như code tự viết, phải hiểu và giải thích được · Disclosure (`Assisted-by` / mục PR) · Quyền của agent: được làm gì, cấm gì (prod, secrets, force-push, tự merge), cấu hình ở đâu · Dữ liệu nhạy cảm và prompt injection (không cho agent đọc nội dung không tin cậy kèm quyền ghi) · Review bắt buộc của người cho mọi PR do agent tạo.
- *Tuỳ chọn:* license/IP của code sinh ra, danh sách MCP server được duyệt, quy trình thu hồi quyền khi có sự cố.

**4) Độ dài:** SECURITY.md nửa trang. AI policy 1–2 trang.

**5) Anti-pattern:** Gửi output chưa review cho reviewer, tức chuyển gánh nặng kiểm chứng sang người khác (LLVM gọi là "extractive"). Để agent tự hành động trong không gian chung mà không có người phê duyệt (LLVM cấm). Policy chỉ là lời khuyên mà không có permission hoặc sandbox thực thi. Cấm AI hoàn toàn trong khi thực tế vẫn dùng (suy luận).

**6) Khi có AI agent:** Đây là loại tài liệu *mới* do agent sinh ra. Phần của nó trong AGENTS.md nên ngắn (3–5 dòng "không bao giờ…"), còn enforcement nằm trong `.claude/settings.json` hoặc CI.

---

## D11 Loại tài liệu team nhỏ thường thiếu, và loại không đáng làm

**Nên có (thường thiếu):**
1. **`CONTRIBUTING.md` / dev setup**: cách chạy local, quy ước branch/commit, quy trình review. Kubernetes PR template dẫn agent tới AGENTS.md và CONTRIBUTING.md. Có thể gộp vào README nếu ngắn.
2. **Glossary / ngôn ngữ miền**: arc42 có mục Glossary. Google SRE Workbook coi "missing context… no glossary" là anti-pattern của postmortem. Agent hưởng lợi rất nhiều khi thuật ngữ miền được định nghĩa một lần (suy luận).
3. **CHANGELOG / release notes**: Kubernetes bắt buộc release-note block. Keep a Changelog (https://keepachangelog.com, chưa xác minh trong phiên này).
4. **How-to ngắn theo Diátaxis** (tutorial, how-to, reference, explanation; [diataxis.fr](https://diataxis.fr/), có Cloudflare, Gatsby áp dụng). Nó giúp phân loại để tài liệu khỏi trộn lẫn. Với agent, phần how-to lặp lại nên chuyển thành *skill* (`.claude/skills/`), nạp khi cần ([best practices](https://code.claude.com/docs/en/best-practices)).
5. **Ownership / on-call map**: ai sở hữu service nào. Google README yêu cầu "points of contact".

**Không đáng làm (với team 3–10 người):**
- arc42 đủ 12 mục, C4 mức Code, KEP đầy đủ kèm Production Readiness questionnaire: quá nặng ([c4model](https://c4model.com/diagrams) tự nói 2 mức đầu là đủ).
- "Test plan" riêng cho mỗi feature: gộp vào mục Verification của design doc.
- Design doc cho việc không mơ hồ ([Google](https://www.industrialempathy.com/posts/design-docs-at-google/)).
- Bộ spec Spec-Kit/Kiro song song với RFD: chọn một nơi duy nhất (suy luận).
- AGENTS.md do LLM tự sinh rồi để nguyên ([arXiv 2602.11988](https://arxiv.org/abs/2602.11988)).
- Wiki ngoài repo cho tài liệu kỹ thuật: không review được qua PR (suy luận theo docs-as-code).

---

## Top 10 kết luận

1. Tối thiểu hoá bộ tài liệu: ít file, đúng, sống trong repo, sửa cùng PR với code (Google "minimum viable documentation").
2. AGENTS.md là file chỉ dẫn agent duy nhất, dưới 200 dòng. CLAUDE.md chỉ `@AGENTS.md` cộng phần riêng.
3. Đừng để LLM tự sinh AGENTS.md rồi bỏ đó. Bằng chứng 2026 cho thấy file thừa làm tăng chi phí hơn 20% mà không tăng tỉ lệ thành công.
4. Kiến trúc: arc42 rút gọn cộng C4 mức 1–2, diagram-as-code.
5. ADR theo MADR minimal, giữ "Considered Options", immutable và supersede.
6. Design doc: mini design doc của Google trong vòng đời RFD của Oxide, với Non-goals và Verification là bắt buộc.
7. Kiểm thử là guardrail chính với agent: lệnh test nhanh, DoD tự động hoá bằng CI hoặc hook.
8. PR template theo Kubernetes, có mục AI disclosure. Mô tả PR theo chuẩn Google (what + why).
9. Postmortem theo Google SRE và blameless. Mỗi alert có runbook. Action item có owner và ticket.
10. Bảo mật gồm hai lớp: SECURITY.md và AI policy (trách nhiệm người, `Assisted-by`, quyền agent được enforce bằng cấu hình chứ không bằng lời).

## Bảng chọn cuối

| Loại | Template nền chọn | 3–6 mục bắt buộc | Độ dài |
|---|---|---|---|
| D1 README | Google docguide README + Install/Usage của standard-readme | Mô tả; Owner/trạng thái; Quickstart (lệnh); Link docs; Cách đóng góp | 50–150 dòng |
| D2 Agent instructions | AGENTS.md (+ CLAUDE.md `@AGENTS.md`, rules theo path) | Lệnh build/test/lint; Quy ước khác mặc định; Ranh giới/vùng cấm; Git/PR; Gotchas; Bảo mật | dưới 200 dòng/file |
| D3 Kiến trúc | arc42 rút gọn + C4 L1–L2 | Quality goals; Ràng buộc; Context (C4 L1); Containers (C4 L2); Crosscutting; Rủi ro/nợ kỹ thuật | 2–5 trang |
| D4 ADR | MADR 4 minimal + vòng đời Nygard/AWS | Title; Status+Date; Context; Considered Options; Decision+lý do; Consequences | 1–2 trang |
| D5 API | OpenAPI 3.1+ + guideline rút từ Zalando, thực thi bằng linter | Naming; Lỗi (RFC 9457); Versioning/breaking; Pagination; Auth; Idempotency/status code | Guideline 1–3 trang |
| D6 Spec/Design | Google mini design doc + vòng đời Oxide RFD (+ Appetite/No-gos của Shape Up) | Metadata/state; Context; Goals/Non-goals; Design+trade-off; Alternatives; Verification/acceptance | 1–3 trang (lớn ≤10) |
| D7 Test + DoD | Google test sizes + Practical Test Pyramid; DoD rút từ GitLab | Tầng test+lệnh; Cái gì phải có test; Flaky/mock; CI gate; DoD checklist | 1–2 trang + 6–10 dòng DoD |
| D8 PR template | Kubernetes rút gọn + Google CL description | What/Why+link; Cách test/bằng chứng; Rủi ro/rollback; AI usage; DoD checklist | dưới 30 dòng |
| D9 Runbook/Postmortem | Google SRE example postmortem (+PagerDuty); runbook mỗi alert | PM: Summary; Impact; Timeline; Contributing factors; Action items (owner); Lessons. RB: Ý nghĩa alert; Kiểm tra; Mitigation; Escalation | PM 1–3 trang; RB dưới 1 trang |
| D10 Security + AI | SECURITY.md (GitHub/Scorecard) + AI policy theo LLVM/kernel/Ghostty + OWASP Agentic | Kênh báo cáo riêng + SLA; Supported versions; Trách nhiệm người; Disclosure `Assisted-by`; Quyền agent (enforce); Dữ liệu/secrets | 0.5 + 1–2 trang |

## Điều chưa chắc

- **Số liệu adoption:** "hơn 60k dự án" của AGENTS.md là số tự công bố trên agents.md. arc42 không có số liệu adoption độc lập. Số sao GitHub chỉ là proxy.
- **Paper "Evaluating AGENTS.md":** benchmark chủ yếu là Python và SWE-bench. Phần tóm tắt không tách số liệu giữa file do LLM sinh và file do người viết (báo chí nói file LLM sinh làm *giảm* tỉ lệ thành công, nhưng tôi chưa kiểm số liệu trong thân paper). Kết quả có thể không chuyển sang được ngôn ngữ hoặc dự án khác.
- **Linux kernel `Assisted-by`:** các bản tài liệu khác nhau dùng định dạng khác nhau (`LLM [tools]` so với `AGENT:MODEL [tools]`). Cần kiểm tra bản mainline hiện tại.
- **GitLab:** tôi không đọc được nội dung trang "Architecture Design Workflow" của handbook (chỉ lấy được menu), nên không dẫn quy trình design doc của GitLab.
- **Atlassian:** chi tiết template postmortem (Five Whys, gọi người theo vai trò) lấy từ trích đoạn kết quả tìm kiếm. WebFetch trang handbook không trả về thân bài.
- **Chưa fetch trong phiên:** RFC 9457, Keep a Changelog, bài Y-statement trên Medium (fetch lỗi kết nối).
- **Phần suy luận:** các khuyến nghị "khác biệt khi có AI agent" ở D3, D4, D9 phần lớn là suy luận từ nguyên tắc chung (verification, enforcement bằng cấu hình). Chưa có nghiên cứu thực nghiệm cho từng loại tài liệu.
- **Quy mô nguồn:** Microsoft API guidelines hiện chỉ có Azure/Graph. Tôi không xác minh được trạng thái của bộ guideline chung cũ.

## Nguồn

- Google docguide: README (chưa rõ năm): https://google.github.io/styleguide/docguide/READMEs.html
- Google docguide: Best practices (chưa rõ năm): https://google.github.io/styleguide/docguide/best_practices.html
- standard-readme spec: https://github.com/RichardLitt/standard-readme/blob/main/spec.md
- Make a README: https://www.makeareadme.com/
- AGENTS.md (2025–2026): https://agents.md/
- Claude Code: memory / CLAUDE.md (2026): https://code.claude.com/docs/en/memory
- Claude Code: best practices (2026): https://code.claude.com/docs/en/best-practices
- Gloaguen et al., "Evaluating AGENTS.md…" (02/2026): https://arxiv.org/abs/2602.11988
- C4 model: https://c4model.com/ ; https://c4model.com/diagrams
- arc42 overview: https://arc42.org/overview
- Nygard, Documenting Architecture Decisions (2011): https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- MADR 4.0.0 (2024): https://adr.github.io/madr/
- joelparkerhenderson/architecture-decision-record: https://github.com/joelparkerhenderson/architecture-decision-record
- AWS Prescriptive Guidance: ADR process: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
- Spotify Engineering, When Should I Write an ADR (2020): https://engineering.atspotify.com/2020/04/when-should-i-write-an-architecture-decision-record
- OpenAPI 3.2.0 (2025): https://spec.openapis.org/oas/v3.2.0.html
- Zalando RESTful API Guidelines: https://opensource.zalando.com/restful-api-guidelines/
- Google AIP-1: https://google.aip.dev/1
- Microsoft API Guidelines: https://github.com/microsoft/api-guidelines
- Malte Ubl, Design Docs at Google (2020): https://www.industrialempathy.com/posts/design-docs-at-google/
- Rust RFC template: https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md
- Kubernetes KEP template: https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md
- Oxide RFD 1: https://rfd.shared.oxide.computer/rfd/0001
- Basecamp Shape Up, Write the Pitch (2019): https://basecamp.com/shapeup/1.5-chapter-06
- Pragmatic Engineer, Scaling Engineering Teams via RFCs (2018/2022): https://blog.pragmaticengineer.com/scaling-engineering-teams-via-writing-things-down-rfcs/
- GitHub Spec Kit: https://github.com/github/spec-kit
- Kiro Specs: https://kiro.dev/docs/specs/
- Software Engineering at Google, ch.11 Testing Overview (2020): https://abseil.io/resources/swe-book/html/ch11.html
- Vocke, The Practical Test Pyramid (2018): https://martinfowler.com/articles/practical-test-pyramid.html
- Scrum Guide (2020): https://scrumguides.org/scrum-guide.html
- GitLab MR workflow / Definition of done: https://docs.gitlab.com/development/contributing/merge_request_workflow/
- Kubernetes PR template: https://raw.githubusercontent.com/kubernetes/kubernetes/master/.github/PULL_REQUEST_TEMPLATE.md
- Google eng-practices, CL descriptions: https://google.github.io/eng-practices/review/developer/cl-descriptions.html
- Google eng-practices, Small CLs: https://google.github.io/eng-practices/review/developer/small-cls.html
- GitHub, PR template docs: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository
- Google SRE Book, Example Postmortem (2016): https://sre.google/sre-book/example-postmortem/
- Google SRE Book, Postmortem Culture (2016): https://sre.google/sre-book/postmortem-culture/
- Google SRE Workbook, Postmortem Culture (2018): https://sre.google/workbook/postmortem-culture/
- Google SRE Book, Introduction (2016): https://sre.google/sre-book/introduction/
- Google SRE Book, Monitoring Distributed Systems (2016): https://sre.google/sre-book/monitoring-distributed-systems/
- PagerDuty Postmortem Template: https://response.pagerduty.com/after/post_mortem_template/
- Atlassian Incident Handbook, Postmortems: https://www.atlassian.com/incident-management/handbook/postmortems
- GitLab Runbooks repo (2016–): https://gitlab.com/gitlab-com/runbooks
- GitHub, Adding a security policy: https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository
- GitHub, Private vulnerability reporting: https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository
- OpenSSF Scorecard checks: https://github.com/ossf/scorecard/blob/main/docs/checks.md
- LLVM AI Tool Use Policy (2025–2026): https://llvm.org/docs/AIToolPolicy.html
- Linux kernel, AI Coding Assistants (2025–2026): https://docs.kernel.org/process/coding-assistants.html
- Ghostty AI_POLICY.md (2025–2026): https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md
- OWASP Top 10 for Agentic Applications 2026 (12/2025): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026
- Diátaxis: https://diataxis.fr/
- RFC 9457 Problem Details (2023): https://www.rfc-editor.org/rfc/rfc9457 (chưa xác minh URL trong phiên)
- Keep a Changelog: https://keepachangelog.com (chưa xác minh URL trong phiên)

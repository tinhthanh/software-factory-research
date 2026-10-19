# Round 3 — claude-T2

**Góc nhìn chọn nguồn:** ưu tiên chuẩn, framework và template chính chủ (arc42, C4, ISO/IEC/IEEE, Nygard/MADR, OpenAPI, Google AIP/eng-practices/SRE, GitHub Docs, OpenSSF/OWASP/NIST, Scrum Guide). Mỗi ứng viên được đánh giá theo hai trục: **mức chuẩn hoá** (chuẩn quốc tế > đặc tả mở có tổ chức quản lý > template chính chủ của một công ty > bài blog) và **adoption** (số liệu dẫn được). Các URL được dẫn đều đã được mở bằng WebFetch hoặc thấy trong kết quả tìm kiếm ngày 2026-10-19. Riêng các trang iso.org trả về lỗi 403, nên chỉ xác minh được gián tiếp qua catalogue của các cơ quan chuẩn quốc gia.

**Ghi chú chung về chuẩn ISO:** ISO/IEC/IEEE 42010:2022 (mô tả kiến trúc), 29148:2018 (yêu cầu) và 29119-3:2021 (tài liệu kiểm thử) là các chuẩn **mất phí**. Chúng cố ý không quy định template hay định dạng. Ví dụ, 42010:2022 nói rõ chuẩn "does not specify any format or media for recording an AD". Vì vậy với team 3–10 người, ISO chỉ nên làm **khung khái niệm** (stakeholder, concern, viewpoint; yêu cầu phải verifiable), không nên làm template (suy luận).

---

## D1 — README dự án

**1) Ứng viên**
- **Standard Readme** (Richard Litt, GitHub `RichardLitt/standard-readme`). Đây là một spec có thứ tự mục rõ ràng, phân biệt mục Required và Optional, và có linter. Bắt buộc: Title, Short Description, ToC (chỉ khi README dài từ 100 dòng), Install, Usage, Contributing, License (License phải là mục cuối). Ưu điểm: chuẩn hoá cao, kiểm tra tự động được. Nhược điểm: thiên về thư viện/OSS, thiếu mục vận hành nội bộ. Nguồn: https://github.com/RichardLitt/standard-readme/blob/main/spec.md
- **Make a README** (makeareadme.com). Danh sách gợi ý gồm Name, Description, Badges, Visuals, Installation (+Requirements), Usage, Support, Roadmap, Contributing, Authors, License, Project status. Trang có câu "too long is better than too short", nhưng cũng khuyên khi README quá dài thì chuyển chi tiết sang tài liệu khác. Ưu điểm: linh hoạt, dễ hiểu. Nhược điểm: không có mục nào bắt buộc. Nguồn: https://www.makeareadme.com/
- **Diátaxis**, dùng làm nguyên tắc phân loại tài liệu chứ không phải template README. Diátaxis chia tài liệu thành tutorial, how-to, reference và explanation. Trang chính chủ dẫn Gatsby, Cloudflare và Vonage là đơn vị áp dụng. README nên là cổng điều hướng tới bốn loại này thay vì nhồi tất cả vào một file (suy luận từ framework). Nguồn: https://diataxis.fr/
- **GitHub community health files** (CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT…) giúp tách nội dung ra khỏi README. Nguồn: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file

**2) Chọn:** Lấy **Standard Readme làm khung thứ tự**, bổ sung mục "Project status" của makeareadme và một mục "Phát triển cục bộ" cho repo nội bộ. Lý do: đây là template duy nhất có required/optional rõ ràng và lint được. Với team nhỏ, file nào lint được thì sẽ còn được bảo trì (suy luận).

**3) Mục bắt buộc:** Tên + mô tả một câu; Trạng thái dự án; Cài đặt / Yêu cầu môi trường; Chạy & test cục bộ (lệnh copy-paste được); Cấu trúc tài liệu (link tới `docs/`, ADR, AGENTS.md); Đóng góp (link CONTRIBUTING.md); License hoặc chủ sở hữu.
**Mục tuỳ chọn:** Badges, Visuals, Background, API (chỉ link), Roadmap, Maintainers.

**4) Độ dài:** Đọc hết trong khoảng 2–5 phút. Standard Readme lấy mốc 100 dòng để bắt buộc có ToC, nên hợp lý là giữ dưới khoảng 150 dòng; phần dài hơn thì chuyển vào `docs/` theo Diátaxis (suy luận).

**5) Anti-pattern:** README kiêm luôn tutorial, reference và changelog (trộn các loại tài liệu mà Diátaxis tách riêng); lệnh cài đặt đã lỗi thời; thiếu License hoặc Contributing (vi phạm Standard Readme); badge nhiều hơn nội dung.

**6) Khi có AI agent:** Agent đọc README để định hướng, nhưng **lệnh build/test chính thức nên đặt ở AGENTS.md**, README chỉ cần link sang (suy luận dựa trên trang agents.md, nơi mô tả AGENTS.md là "README for agents"). Lệnh trong README nên chạy được nguyên văn, vì agent sẽ thực thi đúng như được viết.

---

## D2 — File hướng dẫn cho AI agent (AGENTS.md / CLAUDE.md / rules)

**1) Ứng viên**
- **AGENTS.md** (agents.md). Trang chính chủ ghi "used by over 60k open-source projects" và "now stewarded by the Agentic AI Foundation under the Linux Foundation". Mục gợi ý: project overview, build & test commands, code style, testing instructions, security considerations, cùng commit/PR guidelines và deployment. Hỗ trợ file lồng nhau: agent đọc file gần nhất trong cây thư mục (repo chính của OpenAI có 88 file). Ưu điểm: trung lập về nhà cung cấp, adoption cao nhất. Nhược điểm: không có schema, không quy định mục bắt buộc. Nguồn: https://agents.md/
- **CLAUDE.md** (Anthropic). Không có format bắt buộc, "keep it short and human-readable". Đi kèm bảng Include/Exclude và phép thử *"Would removing this cause Claude to make mistakes?"*. Hỗ trợ import `@path`, thư mục `.claude/rules/`, và Claude Code có thể đọc AGENTS.md. Tài liệu nói rõ CLAUDE.md chỉ mang tính tư vấn; nếu cần bắt buộc tuyệt đối thì dùng hook. Nguồn: https://code.claude.com/docs/en/best-practices ; https://code.claude.com/docs/en/memory
- **GitHub Copilot custom instructions**: `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` (có `applyTo` glob). Copilot cũng đọc AGENTS.md (file gần nhất được ưu tiên), CLAUDE.md và GEMINI.md. Nguồn: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
- **OpenSSF Security-Focused Guide for AI Code Assistant Instructions** (2025-08-01). Hướng dẫn viết phần bảo mật trong file instructions: secrets, dependency (kiểm tra package có tồn tại thật, đề phòng tên gói do AI bịa ra), supply chain, input validation. Khuyên giữ ngắn và tham chiếu OWASP thay vì chép lại. Nguồn: https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions

**Bằng chứng thực nghiệm:** Gloaguen et al., *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?* (arXiv 2602.11988, 2026). Abstract cho biết context file "does not generally improve task success rates" nhưng làm tăng "inference cost by over 20% on average". Kết luận nghiêng về việc file do người viết chỉ nên chứa yêu cầu tối thiểu. Nguồn: https://arxiv.org/abs/2602.11988

**2) Chọn:** Dùng **AGENTS.md làm nguồn chân lý duy nhất ở root**. `CLAUDE.md` chỉ chứa `@AGENTS.md` cộng phần riêng của Claude, hoặc dùng symlink (cách symlink là suy luận). Nội dung lọc theo bảng Include/Exclude của Anthropic. Lý do: AGENTS.md có tổ chức quản lý trung lập (LF) và được Copilot, Claude, Codex… cùng đọc. Bảng Include/Exclude là tiêu chí lọc nội dung rõ ràng nhất tìm được.

**3) Mục bắt buộc:** Lệnh build/test/lint (chính xác, chạy được); Quy ước khác mặc định (style, đặt tên); Cách kiểm chứng trước khi báo xong (test nào, check nào); Ranh giới (không sửa thư mục nào, không chạy lệnh nào, secrets); Quy ước commit/PR; Gotchas của môi trường.
**Mục tuỳ chọn:** Bản đồ thư mục ngắn, link ADR/kiến trúc, AGENTS.md lồng nhau cho từng package, `.claude/rules/` hoặc `.github/instructions/` theo glob.

**4) Độ dài:** Càng ngắn càng tốt. Thực tế khoảng 30–100 dòng (suy luận). Bộ nhớ tự động của Claude chỉ nạp "first 200 lines or 25KB", và đó là mốc trần hợp lý. Copilot giới hạn file tự sinh ở khoảng 2 trang.

**5) Anti-pattern:** Theo Anthropic: CLAUDE.md quá dài khiến quy tắc bị chìm ("Bloated CLAUDE.md files cause Claude to ignore your actual instructions"); mô tả từng file một; "write clean code"; chép tài liệu API; nhấn "IMPORTANT" ở nhiều dòng. Để LLM tự sinh rồi commit nguyên văn mà không cắt gọt (dựa trên arXiv 2602.11988). Dùng file instructions để thực thi chính sách bảo mật thay vì hook hoặc CI.

**6) Khác biệt khi có AI:** Đây là loại tài liệu chỉ tồn tại vì có agent. Cần review trong PR như code, ghi CODEOWNERS cho file này (suy luận), và cắt gọt định kỳ. Mọi quy tắc "phải luôn đúng" nên chuyển thành hook/CI, vì instructions chỉ là gợi ý.

---

## D3 — Tài liệu kiến trúc tổng quan

**1) Ứng viên**
- **arc42** (Hruschka & Starke). Có 12 mục: Introduction & Goals, Constraints, Context & Scope, Solution Strategy, Building Block View, Runtime View, Deployment View, Crosscutting Concepts, Architectural Decisions, Quality Requirements, Risks & Technical Debt, Glossary. Trang chính chủ ghi "Proven in practice since 2005", giấy phép mở cho cả mục đích thương mại, và có **arc42 canvas** một trang. Ưu điểm: đầy đủ, có hướng dẫn từng mục (docs.arc42.org). Nhược điểm: 12 mục là quá nhiều với team nhỏ. Nguồn: https://arc42.org/overview ; https://docs.arc42.org/tips/1-1/
- **C4 model** (Simon Brown). Phân cấp context → container → component → code, kèm landscape/dynamic/deployment. Trang chính chủ viết: "the system context and container diagrams are sufficient for most software development teams". Khuyến nghị **modelling** hơn là vẽ tay ("Modelling (recommended)"). Ưu điểm: nhẹ, không phụ thuộc ký hiệu. Nhược điểm: chỉ lo phần sơ đồ, không có phần văn bản. Nguồn: https://c4model.com/diagrams ; https://c4model.com/tooling
- **ISO/IEC/IEEE 42010:2022**, ấn bản 2, tháng 11/2022. Định nghĩa stakeholder, concern, viewpoint, view và architecture description framework, nhưng không quy định định dạng. Ưu điểm: mức chuẩn hoá cao nhất. Nhược điểm: mất phí, trừu tượng. Nguồn: https://www.iso.org/standard/74393.html (403 khi tải; xác minh qua https://www.evs.ee/en/iso-iec-ieee-42010-2022)

**2) Chọn:** Dùng **arc42 bản rút gọn, lồng sơ đồ C4 cấp 1–2**. arc42 có hướng dẫn chi tiết cho từng mục, C4 lo phần sơ đồ, và hai bên bổ trợ nhau: Context & Scope dùng sơ đồ C4 Context, Building Block View dùng sơ đồ C4 Container (cách ghép này là suy luận). Mục 9 (Decisions) chỉ trỏ sang thư mục ADR; arc42 tự ghi chú mục này dùng khi quyết định "not described elsewhere".

**3) Mục bắt buộc:** 1. Mục tiêu & quality goals (top 3); 2. Ràng buộc; 3. Context & Scope (C4 Context); 4. Solution Strategy (vài gạch đầu dòng); 5. Building blocks (C4 Container); 8. Crosscutting concepts (auth, logging, error handling); 11. Rủi ro & nợ kỹ thuật.
**Mục tuỳ chọn:** Runtime view (chỉ cho 1–3 luồng quan trọng), Deployment view, Quality scenarios, Glossary, C4 Component.

**4) Độ dài:** Khoảng 3–8 trang. Tip 1-1 của arc42 khuyên phần mục tiêu dài khoảng 1 trang; sơ đồ nên ở dạng code (Structurizr/PlantUML/Mermaid) trong repo (suy luận).

**5) Anti-pattern:** Điền đủ cả 12 mục cho có; sơ đồ hộp-mũi tên không có chú giải (C4 nhấn mạnh phải có key/legend); vẽ C4 cấp Code bằng tay (nhanh lỗi thời); tài liệu kiến trúc nằm trong wiki tách khỏi code.

**6) Khi có AI:** Agent có thể sinh sơ đồ C4 dạng code, nhưng người phải review phần mục tiêu và rủi ro. Nên tách một bản tóm tắt kiến trúc khoảng 10 dòng để AGENTS.md link tới, đừng chép vào (suy luận). Mục Crosscutting concepts là phần agent hay vi phạm nhất, nên viết dưới dạng quy tắc có thể kiểm chứng.

---

## D4 — ADR

**1) Ứng viên**
- **Nygard (2011)**: Title, Context, Decision, Status, Consequences. "One or two pages long"; lưu tại `doc/arch/adr-NNN.md`, số thứ tự không tái sử dụng; quyết định bị đảo ngược thì đánh dấu *superseded* chứ không xoá. Nguồn: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **MADR 4.0.0** (2024-09-17). Bắt buộc: Title, Context and Problem Statement, Considered Options, Decision Outcome. Tuỳ chọn: front-matter status/date/decision-makers/consulted/informed, Decision Drivers, Consequences, Confirmation, Pros and Cons, More Information. Có biến thể "bare" và "minimal". Nguồn: https://adr.github.io/madr/
- **Y-statement** (Zimmermann/Zdun, *Sustainable Architectural Decisions*): một câu dạng "In the context of…, facing…, we decided…, to achieve…, accepting…". Được adr.github.io nhắc tới (https://adr.github.io/). Bài Medium gốc không tải được (chưa xác minh URL `medium.com/olzzio/y-statements…`).
- **Adoption:** Thoughtworks Tech Radar xếp *Lightweight ADRs* ở vòng **Adopt** (2017–2018) và khuyên lưu ADR trong source control thay vì wiki (https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records). Repo `joelparkerhenderson/architecture-decision-record` có khoảng 17.2k sao và tổng hợp khoảng 14 template (https://github.com/joelparkerhenderson/architecture-decision-record).

**2) Chọn:** **MADR 4.0 bản minimal**. Đây là bản kế thừa Nygard, thêm "Considered Options", mục mà Nygard không bắt buộc nhưng rất cần khi agent đề xuất phương án. MADR có front-matter máy đọc được và được duy trì tích cực. Y-statement dùng làm dòng tóm tắt đầu file (suy luận).

**3) Mục bắt buộc:** Title (vấn đề + lựa chọn); Status + Date (front-matter); Context and Problem Statement; Considered Options (ít nhất 2); Decision Outcome (kèm lý do); Consequences (tốt/xấu).
**Mục tuỳ chọn:** Decision Drivers, Pros/Cons chi tiết, Confirmation (cách kiểm chứng tuân thủ), consulted/informed.

**4) Độ dài:** 1–2 trang (Nygard). Thường 40–120 dòng (suy luận).

**5) Anti-pattern:** Sửa ADR đã accepted thay vì viết ADR mới để supersede (trái với Nygard); ADR nằm trong wiki (Thoughtworks); viết ADR cho những quyết định không mang tính kiến trúc; chỉ có một option ("quyết định" mà không có lựa chọn nào khác); không có trạng thái.

**6) Khi có AI:** ADR là "trí nhớ dài hạn" rẻ nhất cho agent. Nên có quy tắc trong AGENTS.md: *trước khi thay thư viện, pattern hay datastore thì đọc `docs/adr/`; nếu đi ngược ADR thì đề xuất ADR mới chứ không tự ý đổi* (suy luận). Agent soạn nháp ADR rất tốt, nhưng Decision Outcome phải do người ký. Mục "Confirmation" của MADR có thể nối với test hoặc linter kiến trúc để kiểm tra tự động.

---

## D5 — API contract & quy ước API

**1) Ứng viên**
- **OpenAPI Specification** (OpenAPI Initiative, Linux Foundation). Bản mới nhất trên spec.openapis.org là **3.2.1, ngày 10/09/2026**. Đây là chuẩn de facto cho mô tả HTTP API. Nguồn: https://spec.openapis.org/oas/latest.html
- **Google AIP**: "the source of truth for API-related documentation at Google"; mỗi AIP là một file Markdown, kèm linter. Nhánh cộng đồng **AEP** (aep.dev) tổng hợp bài học từ Google, Microsoft, Roblox, IBM. Ưu điểm: rất chi tiết (resource-oriented, pagination, errors). Nhược điểm: gắn với gRPC/Google, nặng với team nhỏ. Nguồn: https://google.aip.dev/1 ; https://aep.dev/
- **Zalando RESTful API Guidelines**: API-First; bắt buộc OpenAPI (ưu tiên 3.1) trong một file YAML tự đủ; quy tắc MUST/SHOULD/MAY theo RFC 2119; lint bằng Zally. Ưu điểm: thực dụng cho REST, dễ fork. Nguồn: https://opensource.zalando.com/restful-api-guidelines/
- **RFC 9457 Problem Details for HTTP APIs** (2023, thay thế RFC 7807), chuẩn IETF cho định dạng lỗi. Nguồn: https://www.rfc-editor.org/rfc/rfc9457

**2) Chọn:** **Một file OpenAPI 3.1/3.2 (contract-first) cho mỗi service, cộng một style guide ngắn khoảng 1–2 trang fork từ phần MUST của Zalando.** Lỗi trả về theo RFC 9457, lint tự động trong CI (Spectral hoặc Zally; chưa xác minh trang Spectral). Không chọn AIP làm nền vì quá thiên về gRPC/Google, chỉ nên tham khảo khi thiết kế resource. Lý do: OpenAPI là chuẩn có tổ chức quản lý, máy đọc được (sinh client, test, mock), và style guide dạng MUST/SHOULD dễ chuyển thành lint rule.

**3) Mục bắt buộc (style guide):** Đặt tên URL/field; Versioning & tương thích ngược; Định dạng lỗi (RFC 9457); Pagination/filter; Auth; Idempotency & mã trạng thái.
**Contract bắt buộc:** `info.version`, servers, security schemes, schema cho mọi request/response, ví dụ.
**Tuỳ chọn:** Rate limit, deprecation policy, webhook/event (AsyncAPI).

**4) Độ dài:** Style guide khoảng 1–3 trang theo dạng danh sách quy tắc. Contract dài bao nhiêu tuỳ API, nhưng phải được sinh hoặc kiểm tra tự động.

**5) Anti-pattern:** Viết contract sau khi code xong (code-first) rồi để hai bên lệch nhau; style guide dạng văn xuôi không lint được; mỗi endpoint một kiểu lỗi; breaking change không đổi version.

**6) Khi có AI:** Agent thường bịa field hoặc endpoint. Contract máy đọc được kèm lint trong CI là "hàng rào" chặn việc này (suy luận). Nên ghi quy tắc vào AGENTS.md: *sửa API thì sửa `openapi.yaml` trước, chạy lint và contract test*. Postman 2025 State of the API cho biết khoảng 24% developer đã thiết kế API với AI agent là đối tượng sử dụng (https://secure.businesswire.com/news/home/20251008162423/en/One-in-Four-Developers-Now-Design-APIs-for-AI-Agents-According-to-Postmans-2025-State-of-the-API-Report).

---

## D6 — Spec / design doc / RFC cho feature

**1) Ứng viên**
- **Google design doc** (Malte Ubl, 2020): Context and scope; Goals and non-goals; The actual design (gồm system-context diagram, API, storage, code/pseudo-code); Alternatives considered; Cross-cutting concerns (security, privacy, observability). Dự án lớn 10–20 trang; thay đổi nhỏ dùng "mini design doc" 1–3 trang. Bài viết nêu rõ các trường hợp **không** nên viết: lời giải đã rõ ràng, tài liệu thực chất chỉ là hướng dẫn triển khai, hoặc đang prototype. Nguồn: https://www.industrialempathy.com/posts/design-docs-at-google/
- **Kubernetes KEP**: Summary, Motivation (Goals/Non-Goals), Proposal (User Stories, Risks), Design Details (Test Plan, Graduation, Upgrade/Downgrade, Version Skew), Production Readiness Review, Drawbacks, Alternatives. Rất kỹ nhưng nặng. Nguồn: https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md
- **Rust RFC**: Summary, Motivation, Guide-level explanation, Reference-level explanation, Drawbacks, Rationale and alternatives, Prior art, Unresolved questions, Future possibilities. Nguồn: https://github.com/rust-lang/rfcs/blob/master/0000-template.md
- **Công cụ spec-driven**: GitHub **Spec Kit** (khoảng 141.8k sao), quy trình constitution → specify → plan → tasks → implement (https://github.com/github/spec-kit); **Kiro** sinh `requirements.md` / `design.md` / `tasks.md` (https://kiro.dev/docs/specs/). Ưu điểm: sinh ra artifact mà agent dùng trực tiếp được. Nhược điểm: gắn với công cụ, format thay đổi nhanh.
- Về chuẩn: **ISO/IEC/IEEE 29148:2018** quy định đặc tính của một yêu cầu tốt (verifiable, complete…). Không dùng làm template, nhưng là tiêu chí cho phần acceptance criteria (xác minh qua tóm tắt thứ cấp; trang iso.org trả 403, chưa xác minh URL).

**2) Chọn:** **Google mini design doc (1–3 trang) làm nền**, bổ sung hai mục lấy từ KEP: *Test Plan* và *Rollout/Rollback*, cùng mục *Unresolved questions* của Rust. Lý do: Google design doc là khung ít mục nhất mà vẫn bắt buộc có non-goals và alternatives, hai thứ agent hay bỏ qua. Spec Kit/Kiro có thể dùng như **công cụ sinh nháp** theo cùng khung, nhưng không nên phụ thuộc vào format riêng của chúng (suy luận).

**3) Mục bắt buộc:** Context & scope; Goals / **Non-goals**; Design (interface/API, data, sơ đồ nếu cần); Alternatives considered; Acceptance criteria / Test plan (verifiable theo tinh thần 29148); Rollout & rollback; Open questions.
**Tuỳ chọn:** Security/privacy/observability (bắt buộc nếu chạm dữ liệu người dùng), Prior art, Migration, Task breakdown.

**4) Độ dài:** Feature thường 1–3 trang. Hệ thống mới hoặc thay đổi lớn: tới khoảng 10 trang. Nếu "could describe the diff in one sentence" thì không cần spec (Anthropic best practices).

**5) Anti-pattern:** Design doc thực chất chỉ là hướng dẫn triển khai, không bàn trade-off (Google); không có non-goals, dẫn đến scope creep; spec không được cập nhật sau khi triển khai lệch; viết spec cho thay đổi tầm thường.

**6) Khi có AI:** Spec trở thành **đầu vào thực thi** chứ không chỉ để review. Anthropic khuyên để agent phỏng vấn người dùng rồi viết `SPEC.md`, sau đó mở phiên mới để triển khai. Spec tốt nhất là spec tự đủ: "name the files and interfaces involved, state what is out of scope, and end with an end-to-end verification step" (https://code.claude.com/docs/en/best-practices). Vì vậy acceptance criteria phải là thứ kiểm chứng tự động được.

---

## D7 — Test strategy + Definition of Done

**1) Ứng viên**
- **ISO/IEC/IEEE 29119-3:2021**: các template tài liệu kiểm thử (test plan, test design, test case, test report…), Annex A ánh xạ sang 29119-2; ấn bản 2013 đã bị thu hồi. Ưu điểm: chuẩn quốc tế. Nhược điểm: nặng, mất phí, hướng tới môi trường quy trình hoá (chưa xác minh URL iso.org; thông tin lấy qua kết quả tìm kiếm catalogue).
- **Test Pyramid** (Ham Vocke, *The Practical Test Pyramid*, martinfowler.com, 2018): nhiều unit test, ít test cấp cao; tránh "ice-cream cone". Nguồn: https://martinfowler.com/articles/practical-test-pyramid.html
- **Google, *Software Engineering at Google*, ch.11**: phân loại test theo kích thước small/medium/large; tỉ lệ tham khảo khoảng 80% unit / 15% integration / 5% E2E; "Beyoncé Rule" (muốn hành vi nào giữ được thì phải có test cho nó). Nguồn: https://abseil.io/resources/swe-book/html/ch11.html
- **DoD**: Scrum Guide 2020 định nghĩa "The Definition of Done is a formal description of the state of the Increment" (https://scrumguides.org/scrum-guide.html). Microsoft Code-With Engineering Playbook có checklist DoD mẫu: acceptance criteria, unit test mới/cũ đều pass, logging/telemetry, code review, docs, merge, PO sign-off (https://microsoft.github.io/code-with-engineering-playbook/agile-development/team-agreements/definition-of-done/).

**2) Chọn:** **Một trang `TESTING.md` theo khung Test Pyramid / test size của Google, cộng DoD dạng checklist dựa trên Microsoft Playbook.** Không dùng 29119-3 làm template, chỉ mượn khái niệm entry/exit criteria (suy luận). Lý do: team nhỏ cần quy tắc (test nào, ở đâu, chạy thế nào), không cần test plan theo từng release.

**3) Mục bắt buộc (Test strategy):** Các tầng test và tỉ lệ mục tiêu; Lệnh chạy từng tầng; Cái gì bắt buộc có test (Beyoncé Rule cho bug fix); Quy tắc mock và dữ liệu test; Ngưỡng CI (cái gì chặn merge); Xử lý flaky test.
**DoD bắt buộc:** Acceptance criteria đạt; test mới + cũ pass trong CI; review xong; docs/ADR/contract cập nhật nếu bị ảnh hưởng; observability (log/metric) cho đường đi mới; merge vào nhánh chính.
**Tuỳ chọn:** Performance/security test, coverage target, test matrix theo môi trường.

**4) Độ dài:** Test strategy 1–2 trang. DoD từ 6 đến 12 dòng checklist.

**5) Anti-pattern:** Ice-cream cone, tức quá nhiều E2E (Vocke 2018); DoD chỉ nằm trong đầu mọi người hoặc trên wiki thay vì trong PR template/CI; coverage % thành mục tiêu tự thân (suy luận); test plan dài mà không gắn với CI.

**6) Khi có AI:** DoD phải **kiểm chứng được bằng máy** để agent tự đóng vòng lặp: "Give Claude a check it can run… Without a check… 'looks done' is the only signal available" (Anthropic best practices). Nên thêm vào DoD: *agent phải đính kèm bằng chứng (output lệnh test)*; *cấm xoá hoặc skip test để cho pass* (suy luận, nhưng Anthropic có nhấn mạnh "address the root cause, don't suppress the error").

---

## D8 — Pull request template

**1) Ứng viên**
- **GitHub PULL_REQUEST_TEMPLATE** (chính chủ): đặt ở root, `docs/` hoặc `.github/pull_request_template.md`; có thể dùng nhiều template trong `PULL_REQUEST_TEMPLATE/` và chọn bằng query `?template=`. Gợi ý nội dung: issue liên quan, mô tả thay đổi, @mention reviewer. Nguồn: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository
- **Google eng-practices, CL descriptions**: dòng đầu là tóm tắt ngắn ở thể mệnh lệnh; phần thân giải thích vấn đề, lý do chọn cách làm và hạn chế; mô tả phải tự đủ ý vì link có thể chết; "Fix bug" là ví dụ mô tả không đạt. Nguồn: https://google.github.io/eng-practices/review/developer/cl-descriptions.html
- **Google small CLs**: khoảng 100 dòng thường hợp lý, khoảng 1000 dòng thường quá lớn. Nguồn: https://google.github.io/eng-practices/review/developer/small-cls.html
- **Chính sách AI của OSS** (LLVM: công khai việc dùng AI bằng trailer "Assisted-by:"; Ghostty: khai báo công cụ và mức độ AI hỗ trợ) là nguồn cho mục khai báo AI trong PR.

**2) Chọn:** **Template GitHub ngắn (một file `.github/pull_request_template.md`), nội dung theo nguyên tắc CL description của Google, thêm mục khai báo AI và checklist DoD rút gọn.** Lý do: GitHub là cơ chế chính chủ, tự điền vào mọi PR; Google eng-practices là hướng dẫn công khai rõ nhất về *nội dung* mô tả.

**3) Mục bắt buộc:** Tóm tắt (cái gì + tại sao); Issue/spec/ADR liên quan; Cách kiểm chứng (lệnh, kết quả, ảnh chụp); Rủi ro & rollback; Khai báo AI (công cụ, phạm vi, người đã review); Checklist DoD (3–6 ô).
**Tuỳ chọn:** Screenshots UI, breaking changes, ghi chú cho reviewer (nên đọc file nào trước).

**4) Độ dài:** Template khoảng 15–30 dòng. Mô tả PR ngắn nhưng tự đủ ý; PR nên nhắm khoảng 100–400 dòng diff (mốc 100 và 1000 dòng từ Google; khoảng ở giữa là suy luận).

**5) Anti-pattern:** Mô tả kiểu "Fix bug" (Google); checklist dài mà mọi người tick cho xong (suy luận); PR khổng lồ do agent sinh ra hàng nghìn dòng; template chưa merge vào nhánh mặc định nên không có hiệu lực (GitHub docs).

**6) Khi có AI:** PR là **điểm kiểm soát chính** của người với output của agent. Bắt buộc có "Cách kiểm chứng" kèm bằng chứng và khai báo AI. Người mở PR chịu trách nhiệm và phải giải thích được thay đổi (LLVM, Ghostty, Linux kernel). Có thể thêm một template riêng cho PR do agent mở (`PULL_REQUEST_TEMPLATE/agent.md`) (suy luận).

---

## D9 — Runbook + postmortem

**1) Ứng viên**
- **Google SRE Book, *Postmortem Culture***: blameless; các trigger viết postmortem: "User-visible downtime or degradation beyond a certain threshold", "Data loss of any kind", "On-call engineer intervention", "A resolution time above some threshold", "A monitoring failure"; trigger phải được định nghĩa trước khi có sự cố. Nguồn: https://sre.google/sre-book/postmortem-culture/
- **Google SRE example postmortem**: các trường Date, Authors, Status, Summary, Impact, Root Causes, Trigger, Resolution, Detection, Action Items; Lessons Learned (went well / went wrong / **where we got lucky**); Timeline. Nguồn: https://sre.google/sre-book/example-postmortem/
- **PagerDuty postmortem template**: Overview, What Happened, Contributing Factors, Resolution, Impact, Responders, Timeline, How'd We Do?, Action Items, Messaging. Nguồn: https://response.pagerduty.com/after/post_mortem_template/
- **SRE Workbook, On-call (playbook)**: "Each alert should have a corresponding playbook entry"; nội dung gồm mức độ nghiêm trọng, tác động, gợi ý debug, cách giảm thiểu; on-call cập nhật playbook khi alert kêu; playbook chỉ là chuỗi lệnh cố định thì nên tự động hoá. Nguồn: https://sre.google/workbook/on-call/

**2) Chọn:** **Postmortem theo Google SRE example** (gọn hơn PagerDuty, có mục "where we got lucky"), lấy thêm mục *Contributing Factors* và *Messaging* của PagerDuty nếu có khách hàng bên ngoài. **Runbook theo mô hình mỗi alert một entry của SRE Workbook.** Lý do: đây là nguồn gốc của khái niệm blameless postmortem và là chuẩn de facto mà PagerDuty cũng như các bên khác kế thừa (suy luận về phả hệ).

**3) Mục bắt buộc (postmortem):** Summary & Impact (số liệu); Timeline (UTC); Root causes / contributing factors; Detection & Resolution; Lessons (went well / wrong / lucky); Action items (owner, ticket, hạn).
**Bắt buộc (runbook entry):** Tên alert & ý nghĩa; Severity/impact; Dashboard/log cần xem; Các bước chẩn đoán; Mitigation/rollback; Escalation.
**Tuỳ chọn:** Messaging (internal/external), Responders, Supporting info.

**4) Độ dài:** Postmortem 1–3 trang. Mỗi runbook entry nửa trang đến 1 trang.

**5) Anti-pattern:** Đổ lỗi cho cá nhân (Google); action item không có owner hoặc ticket; runbook lỗi thời (SRE Workbook); runbook là chuỗi lệnh lẽ ra phải tự động hoá; định nghĩa trigger sau khi sự cố đã xảy ra.

**6) Khi có AI:** Agent soạn nháp timeline từ log/chat và gợi ý action item rất hiệu quả. Tuy nhiên **mục root cause phải do người xác nhận**, vì agent dễ tạo ra câu chuyện nhân quả nghe hợp lý nhưng sai (suy luận). Runbook viết dạng lệnh có thể chạy cho phép agent hỗ trợ on-call, nhưng các thao tác phá huỷ phải có cổng phê duyệt của người. Postmortem nên có trường "agent/automation có liên quan không" (suy luận).

---

## D10 — Chính sách bảo mật + sử dụng AI agent

**1) Ứng viên**
- **GitHub SECURITY.md** (community health file): nêu "supported versions" và "how to report a vulnerability". Nguồn: https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository
- **OpenSSF Scorecard, check Security-Policy** (rủi ro Medium): chấm điểm theo nội dung SECURITY.md: có link hoặc email liên hệ (6/10), có văn bản thực chất (3/10), có từ khoá về disclosure và thời hạn tính bằng ngày (1/10). Nguồn: https://github.com/ossf/scorecard/blob/main/docs/checks.md
- **RFC 9116 security.txt** (2022): bắt buộc `Contact` và `Expires`, đặt tại `/.well-known/security.txt`, phù hợp khi team có dịch vụ public. Nguồn: https://www.rfc-editor.org/rfc/rfc9116
- **Khung SDLC bảo mật**: NIST SSDF SP 800-218 v1.1 (tháng 2/2022) và **SP 800-218A** (tháng 7/2024), profile SSDF cho generative AI (https://csrc.nist.gov/pubs/sp/800/218/final ; https://csrc.nist.gov/pubs/sp/800/218/a/final); OWASP ASVS 5.0.0 (https://owasp.org/www-project-application-security-verification-standard/); OWASP Top 10 for Agentic Applications 2026 (ra ngày 09/12/2025; https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
- **Chính sách AI**: **Linux kernel**: agent "MUST NOT add Signed-off-by tags", dùng `Assisted-by:`, người nộp chịu toàn bộ trách nhiệm (https://docs.kernel.org/process/coding-assistants.html). **LLVM**: con người phải nằm trong vòng lặp, cấm agent tự hành hoạt động trong không gian dự án khi chưa có người duyệt, cấm "extractive contributions" (https://llvm.org/docs/AIToolPolicy.html). **Ghostty** AI_POLICY.md: khai báo mọi việc dùng AI, phải hiểu được code mình nộp (https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md). Một khảo sát 1.000 repo phổ biến tìm thấy 118 chính sách AI cho contributor (số liệu từ tóm tắt tìm kiếm; danh mục tổng hợp: https://github.com/melissawm/open-source-ai-contribution-policies).

**2) Chọn:** Dùng **hai file**: (a) `SECURITY.md` theo GitHub và tối ưu theo tiêu chí Scorecard (kênh báo cáo riêng tư, SLA tính theo ngày, phạm vi); (b) `AI_POLICY.md` (hoặc một mục trong CONTRIBUTING) **dựa trên mô hình Linux kernel/LLVM**: con người chịu trách nhiệm, khai báo bằng trailer `Assisted-by:`, không có hành động tự động nào mà không có người duyệt. Phần quy tắc code an toàn cho agent đặt trong AGENTS.md theo OpenSSF guide. Dùng SSDF/ASVS làm checklist tham chiếu, không chép lại. Lý do: hai file mỏng, mỗi file có chuẩn chính chủ hoặc tiền lệ adoption rõ ràng.

**3) Mục bắt buộc (SECURITY.md):** Supported versions; Cách báo cáo riêng tư (email hoặc GitHub private vulnerability reporting); Thời hạn phản hồi (ngày); Phạm vi / ngoài phạm vi; Quy trình disclosure.
**Bắt buộc (AI policy):** Công cụ và dữ liệu được phép (không đưa secrets hay dữ liệu khách hàng vào công cụ chưa được duyệt); Trách nhiệm của người (review, hiểu được code); Khai báo (`Assisted-by:`); Quyền của agent (lệnh hoặc môi trường bị cấm, sandbox, không có quyền prod/secrets); Bắt buộc review và CI trước merge; Xử lý vi phạm.
**Tuỳ chọn:** security.txt, threat model, mức ASVS mục tiêu, SBOM.

**4) Độ dài:** SECURITY.md nửa trang đến 1 trang. AI policy 1–2 trang.

**5) Anti-pattern:** SECURITY.md chỉ ghi "email us" mà không có thời hạn (Scorecard chấm thấp); để agent ký DCO hoặc Signed-off-by (kernel cấm); bật agent tự hành có quyền ghi vào prod hoặc repo chung khi chưa có người duyệt (LLVM cấm); chính sách AI chỉ nói "được dùng" hoặc "cấm dùng" mà không có quy tắc khai báo; chỉ dựa vào instructions để chặn hành vi nguy hiểm thay vì hook hoặc quyền hệ thống.

**6) Khi có AI:** Rủi ro mới gồm prompt injection qua nội dung bên ngoài, tên package do AI bịa ra (OpenSSF), lộ secrets trong context, và agent có quyền quá rộng (OWASP Agentic Top 10). Chính sách phải chuyển thành **cơ chế kỹ thuật**: allowlist quyền, sandbox, hook, secret scanning. File markdown chỉ ghi lại các cơ chế này (Anthropic: CLAUDE.md "advisory", hook "deterministic").

---

## D11 — Loại tài liệu team nhỏ thường thiếu, và loại không đáng làm

**Nên có, thường bị thiếu:**
1. **CONTRIBUTING.md / quy trình làm việc** (branch, commit, review, release). Đây là GitHub community health file, Standard Readme bắt buộc có mục Contributing trỏ tới, và agent cũng cần biết (https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file).
2. **CODEOWNERS** cho `AGENTS.md`, `docs/adr/`, `openapi.yaml` và `SECURITY.md`, để các file "quy tắc cho agent" luôn có người review (suy luận).
3. **CHANGELOG / release notes**. Định dạng Keep a Changelog phổ biến (chưa xác minh URL keepachangelog.com trong phiên này).
4. **Glossary / ngôn ngữ miền**. arc42 có mục 12 dành cho việc này. Với agent, glossary giúp đặt tên nhất quán (suy luận).
5. **Danh mục quyền và lệnh của agent** (settings, hook, MCP server được phép), lưu dưới dạng cấu hình trong repo (suy luận).

**Không đáng làm (với team 3–10 người):**
- Test plan đầy đủ theo **ISO 29119-3** hoặc IEEE 829 cho từng release: quá nặng, nên thay bằng TESTING.md cộng CI (suy luận).
- Tài liệu kiến trúc đủ cả **12 mục arc42** cộng C4 cấp Component/Code vẽ tay: C4 tự nói rằng hai cấp context và container là đủ cho phần lớn team.
- Design doc cho thay đổi tầm thường: Google liệt kê rõ các trường hợp không nên viết.
- File kiểu SRS độc lập theo 29148 bên cạnh spec feature: nên gộp các tiêu chí chất lượng yêu cầu vào phần acceptance criteria của D6 (suy luận).

---

## Top 10 kết luận

1. Với team nhỏ, chuẩn ISO (42010, 29148, 29119) là **khung khái niệm**, không phải template: cả ba đều mất phí và không quy định định dạng.
2. README: dùng **Standard Readme** vì đây là spec duy nhất có mục bắt buộc rõ ràng và lint được; phần dài hơn chuyển sang `docs/` theo Diátaxis.
3. File cho agent: **AGENTS.md làm nguồn chân lý** (có tổ chức LF quản lý, hơn 60k repo); CLAUDE.md và Copilot import hoặc trỏ tới nó.
4. File cho agent càng ngắn càng tốt: bằng chứng 2026 cho thấy context file không tự động tăng tỉ lệ thành công mà làm chi phí tăng hơn 20%.
5. Kiến trúc: **arc42 rút gọn khoảng 7 mục cộng C4 cấp 1–2**, sơ đồ dạng code trong repo.
6. ADR: **MADR 4.0 minimal**, lưu trong repo, không sửa mà supersede (Nygard 2011; Thoughtworks xếp Adopt).
7. API: **OpenAPI contract-first**, style guide ngắn dạng MUST/SHOULD (Zalando), lỗi theo RFC 9457, lint trong CI.
8. Spec feature: **Google mini design doc** cộng Test Plan/Rollout của KEP; acceptance criteria phải kiểm chứng được bằng máy để agent tự đóng vòng lặp.
9. PR/DoD: mô tả theo Google CL description, khai báo AI (`Assisted-by:`), DoD kiểm chứng được bằng máy và đính kèm bằng chứng.
10. Bảo mật và AI: SECURITY.md tối ưu theo Scorecard, AI policy theo mô hình kernel/LLVM (con người chịu trách nhiệm, không có agent tự hành khi chưa duyệt), và luật cứng phải nằm ở hook hoặc quyền hệ thống chứ không ở markdown.

---

## Bảng chọn cuối

| Loại | Template nền chọn | 3–6 mục bắt buộc | Độ dài |
|---|---|---|---|
| D1 README | Standard Readme (+ Project status của makeareadme) | Mô tả 1 câu; Trạng thái; Cài đặt; Chạy & test; Contributing; License | < ~150 dòng |
| D2 Agent instructions | AGENTS.md (CLAUDE.md import nó) + bảng Include/Exclude của Anthropic | Lệnh build/test/lint; Quy ước khác mặc định; Cách kiểm chứng; Ranh giới & secrets; Quy ước commit/PR | 30–100 dòng, trần ~200 |
| D3 Kiến trúc | arc42 rút gọn + C4 Context/Container | Quality goals; Ràng buộc; Context (C4); Solution strategy; Building blocks (C4); Crosscutting; Rủi ro | 3–8 trang |
| D4 ADR | MADR 4.0 minimal | Title; Status+Date; Context/Problem; Considered Options; Decision Outcome; Consequences | 1–2 trang |
| D5 API | OpenAPI 3.1/3.2 + style guide fork Zalando + RFC 9457 | Naming; Versioning; Error format; Pagination; Auth; Lint CI | Guide 1–3 trang |
| D6 Spec/design | Google mini design doc + Test plan/Rollout (KEP) | Context; Goals/Non-goals; Design; Alternatives; Acceptance/Test plan; Rollout/rollback | 1–3 trang (lớn ≤10) |
| D7 Test + DoD | Test Pyramid / Google test sizes + DoD Microsoft Playbook | Tầng test & lệnh; Bắt buộc test gì; Chặn merge khi nào; DoD checklist; Bằng chứng | 1–2 trang + 6–12 dòng DoD |
| D8 PR template | GitHub PR template + Google CL description | Tóm tắt (what/why); Liên kết; Cách kiểm chứng; Rủi ro/rollback; Khai báo AI | 15–30 dòng |
| D9 Runbook/Postmortem | Google SRE example postmortem + playbook mỗi alert (SRE Workbook) | Summary/Impact; Timeline; Root causes; Lessons (incl. lucky); Action items có owner | PM 1–3 trang; runbook ½–1 trang/alert |
| D10 Security + AI | SECURITY.md (GitHub/Scorecard) + AI policy mô hình kernel/LLVM | Kênh báo cáo riêng tư; SLA ngày; Supported versions; Trách nhiệm người; Assisted-by; Quyền agent | ½–1 + 1–2 trang |

---

## Điều chưa chắc

- **Các chuẩn ISO** (42010:2022, 29148:2018, 29119-3:2021): trang iso.org trả 403, chỉ xác minh được qua catalogue của cơ quan chuẩn quốc gia và nguồn thứ cấp; danh mục mục chi tiết của 29119-3 và 29148 chưa đọc được trực tiếp.
- **OpenAPI 3.2.1 ngày 10/09/2026**: lấy từ trang spec.openapis.org/oas/latest. Chưa kiểm tra mức hỗ trợ của tooling (codegen, linter) cho 3.2.x, nên khuyến nghị ghi "3.1 hoặc 3.2".
- **Hiệu quả của AGENTS.md**: abstract arXiv 2602.11988 chỉ đưa con số gộp (chi phí tăng hơn 20%, không cải thiện tỉ lệ thành công). Số liệu tách riêng file LLM-sinh và file do người viết là từ bản tóm tắt thứ cấp, chưa đối chiếu với full paper.
- **Y-statement**: bài gốc trên Medium không tải được (ECONNRESET), mẫu câu ghi lại theo trí nhớ và adr.github.io.
- **Mốc độ dài** cho AGENTS.md (30–100 dòng), README (<150 dòng) và PR (100–400 dòng) là suy luận dựa trên các mốc chính chủ (200 dòng của Claude auto memory, ToC từ 100 dòng của Standard Readme, mốc 100/1000 dòng của Google small CLs), không phải chuẩn.
- **Adoption của AEP**, mức hỗ trợ EARS trong Kiro và tên file artifact của Spec Kit chưa xác minh đủ.
- Con số "118 chính sách AI trong 1.000 repo" đến từ tóm tắt kết quả tìm kiếm, chưa mở được nghiên cứu gốc.
- Định dạng **Spectral**, **Keep a Changelog** và **GitHub private vulnerability reporting** chưa được mở URL trong phiên này.

---

## Nguồn

- AGENTS.md: https://agents.md/ (2025–2026)
- Anthropic, Claude Code best practices: https://code.claude.com/docs/en/best-practices (2026)
- Anthropic, Claude Code memory: https://code.claude.com/docs/en/memory (2026)
- GitHub, Copilot repository instructions: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions (2026)
- Gloaguen et al., Evaluating AGENTS.md: https://arxiv.org/abs/2602.11988 (2026)
- OpenSSF, Security-Focused Guide for AI Code Assistant Instructions: https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions (2025)
- Standard Readme spec: https://github.com/RichardLitt/standard-readme/blob/main/spec.md (cập nhật liên tục; chưa rõ năm)
- Make a README: https://www.makeareadme.com/ (chưa rõ năm)
- Diátaxis: https://diataxis.fr/ (2017–2026)
- GitHub community health files: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file (2026)
- arc42 overview: https://arc42.org/overview (template từ 2005); tip 1-1: https://docs.arc42.org/tips/1-1/
- C4 model: https://c4model.com/ ; https://c4model.com/diagrams ; https://c4model.com/tooling (2026)
- ISO/IEC/IEEE 42010:2022: https://www.iso.org/standard/74393.html (2022; 403 khi tải) và https://www.evs.ee/en/iso-iec-ieee-42010-2022
- ISO/IEC/IEEE 29148:2018: (chưa xác minh URL iso.org); catalogue: https://store.sfs.fi/en/ieee-29148-2018
- ISO/IEC/IEEE 29119-3:2021: (chưa xác minh URL iso.org)
- Nygard, Documenting Architecture Decisions: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (2011)
- MADR 4.0.0: https://adr.github.io/madr/ (2024)
- adr.github.io: https://adr.github.io/ (2026)
- Thoughtworks Radar, Lightweight ADRs: https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records (2018)
- joelparkerhenderson/architecture-decision-record: https://github.com/joelparkerhenderson/architecture-decision-record (2026)
- OpenAPI Specification (3.2.1): https://spec.openapis.org/oas/latest.html (2026)
- Google AIP-1: https://google.aip.dev/1 (chưa rõ năm cập nhật)
- AEP: https://aep.dev/ (2025–2026)
- Zalando RESTful API Guidelines: https://opensource.zalando.com/restful-api-guidelines/ (2026)
- RFC 9457 Problem Details for HTTP APIs: https://www.rfc-editor.org/rfc/rfc9457 (2023)
- Postman 2025 State of the API (press release): https://secure.businesswire.com/news/home/20251008162423/en/One-in-Four-Developers-Now-Design-APIs-for-AI-Agents-According-to-Postmans-2025-State-of-the-API-Report (2025)
- Malte Ubl, Design Docs at Google: https://www.industrialempathy.com/posts/design-docs-at-google/ (2020)
- Kubernetes KEP template: https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md (2026)
- Rust RFC template: https://github.com/rust-lang/rfcs/blob/master/0000-template.md (2026)
- GitHub Spec Kit: https://github.com/github/spec-kit (2025–2026)
- Kiro specs: https://kiro.dev/docs/specs/ (2025–2026)
- Ham Vocke, The Practical Test Pyramid: https://martinfowler.com/articles/practical-test-pyramid.html (2018)
- Software Engineering at Google, ch.11 Testing Overview: https://abseil.io/resources/swe-book/html/ch11.html (2020)
- Scrum Guide 2020: https://scrumguides.org/scrum-guide.html (2020)
- Microsoft Code-With Engineering Playbook, DoD: https://microsoft.github.io/code-with-engineering-playbook/agile-development/team-agreements/definition-of-done/ (2026)
- GitHub PR template docs: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository (2026)
- Google eng-practices, CL descriptions: https://google.github.io/eng-practices/review/developer/cl-descriptions.html ; Small CLs: https://google.github.io/eng-practices/review/developer/small-cls.html (2019–2026)
- Google SRE Book, Postmortem Culture: https://sre.google/sre-book/postmortem-culture/ (2016)
- Google SRE Book, Example Postmortem: https://sre.google/sre-book/example-postmortem/ (2016)
- Google SRE Workbook, On-Call: https://sre.google/workbook/on-call/ (2018)
- PagerDuty postmortem template: https://response.pagerduty.com/after/post_mortem_template/ (chưa rõ năm)
- GitHub, Adding a security policy: https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository (2026)
- OpenSSF Scorecard checks: https://github.com/ossf/scorecard/blob/main/docs/checks.md (2026)
- RFC 9116 security.txt: https://www.rfc-editor.org/rfc/rfc9116 (2022)
- NIST SP 800-218 SSDF v1.1: https://csrc.nist.gov/pubs/sp/800/218/final (2022)
- NIST SP 800-218A: https://csrc.nist.gov/pubs/sp/800/218/a/final (2024)
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/ (5.0.0; 2025)
- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ (2025)
- Linux kernel, AI coding assistants: https://docs.kernel.org/process/coding-assistants.html (2026)
- LLVM AI Tool Use Policy: https://llvm.org/docs/AIToolPolicy.html (cập nhật 2026-10-18)
- Ghostty AI_POLICY.md: https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md (2025–2026)
- Danh mục chính sách AI của OSS: https://github.com/melissawm/open-source-ai-contribution-policies (2025–2026)

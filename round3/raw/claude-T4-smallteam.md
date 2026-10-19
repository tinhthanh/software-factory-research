# Round 3 — claude-T4

**Góc nhìn:** cách team nhỏ và startup làm thực tế, kèm phản biện. Câu hỏi xuyên suốt là: *bộ tài liệu tối thiểu nào vẫn hiệu quả, và cái gì không đáng làm?*
**Ngày:** 2026-10-19. **Phương pháp:** chỉ dùng WebSearch và WebFetch, ưu tiên nguồn gốc. Phần lớn URL đã được mở để kiểm tra. URL nào chỉ thấy qua kết quả tìm kiếm thì ghi "(qua tìm kiếm)". Ý kiến không có nguồn ghi "(suy luận)".

---

## Bối cảnh thực nghiệm: vì sao "tối thiểu" là đúng

- **Tài liệu lỗi thời là vấn đề phổ biến nhất, không phải chuyện hiếm.** GitHub Open Source Survey 2017: 93% người trả lời gặp tài liệu thiếu hoặc lỗi thời, và 60% contributor "hiếm khi hoặc không bao giờ" đóng góp tài liệu (https://opensourcesurvey.org/2017/, 2017).
- **Tài liệu "rot" có thể đo được.** Tan, Wagner, Treude phân tích hơn 3.000 dự án GitHub. Phần lớn dự án từng có ít nhất một tham chiếu tới code element đã bị xoá. Hơn ¼ trong 1.000 dự án phổ biến nhất có ít nhất một tham chiếu lỗi thời (arXiv:2212.01479, 2022; EMSE 2024).
- **Phân loại lỗi tài liệu.** Aghajani et al. phân tích 878 artefact từ mailing list, Stack Overflow, issue và PR để lập taxonomy lỗi tài liệu (ICSE 2019). Nghiên cứu tiếp theo với 146 practitioner cho biết hướng dẫn cài đặt sai là lỗi gặp nhiều nhất (ICSE 2020, qua tìm kiếm).
- **Ba lỗi nặng nhất của tài liệu API** là mơ hồ, thiếu và sai. Nhiều lỗi đủ nặng để lập trình viên bỏ API đó (Uddin & Robillard, IEEE Software 2015).
- **Tài liệu vẫn được dùng nhiều.** Stack Overflow Survey 2024: 83,9% lập trình viên học qua tài liệu kỹ thuật, và tài liệu API/SDK được tham chiếu nhiều nhất, 90,3% (qua tìm kiếm).

**Hệ quả (suy luận):**
- Tài liệu càng nhiều thì càng nhiều bề mặt để lỗi thời.
- Nên giữ những gì *gắn với một quy trình buộc phải chạm vào nó*: PR template chạm mỗi PR, runbook gắn vào alert, ADR gắn vào PR thay đổi kiến trúc, AGENTS.md được agent đọc mỗi phiên.
- Nên bỏ hoặc thu nhỏ những tài liệu "viết một lần rồi để đó".

---

## D1 — README dự án

**1) Ứng viên**
- **standard-readme** (RichardLitt). Đặc tả có thứ tự mục: Title, Background, Install, Usage, Contributing, License… Repo phổ biến trong cộng đồng OSS (https://github.com/RichardLitt/standard-readme). Ưu điểm: có linter và generator. Nhược điểm: thiên về thư viện OSS, thừa với ứng dụng nội bộ.
- **Make a README / mẫu tự do theo kinh nghiệm** (makeareadme.com, chưa xác minh URL). Ưu điểm: nhẹ. Nhược điểm: không chuẩn hoá.
- **Thực tế đo được:** Prana et al. phân loại 4.226 mục README từ 393 repo (EMSE 2018).
  - "What" có trong 97% file, "How" trong 88,5%.
  - "Why" chỉ có trong 25,7% file, "When" (trạng thái dự án) 21,4%, "Contribution" 27,8%.
  - Nghĩa là README thực tế *thiếu mục đích và trạng thái* (https://arxiv.org/abs/1802.06997, 2018).

**2) Chọn:** khung rút gọn từ standard-readme, cộng thêm hai mục "Why" và "Status" mà nghiên cứu cho thấy hay bị thiếu. README dành cho người. Không nhồi quy ước cho agent vào đây, phần đó để ở D2.

**3) Mục bắt buộc**
- Tên + 1–2 câu "What/Why".
- Status (active / beta / deprecated, owner).
- Quickstart: chạy local bằng ≤5 lệnh copy-paste được.
- Test/Dev commands.
- Link tới docs khác: ARCHITECTURE, ADR, runbook.
- License (OSS) hoặc Owner (nội bộ).

Tuỳ chọn: badges, FAQ, roadmap, screenshot.

**4) Độ dài:** 1–2 màn hình. Chi tiết đẩy sang docs/ (suy luận).

**5) Anti-pattern**
- Hướng dẫn cài đặt lỗi thời, là lỗi số 1 theo practitioner (Aghajani 2020).
- Tham chiếu tên hàm hoặc file đã xoá (Tan et al. 2022).
- Gộp tutorial, how-to, reference và explanation vào một file. Diátaxis tách bốn loại này (https://diataxis.fr/).

**6) Khi có AI agent**
- Quickstart phải chạy được không cần người, để agent tự dựng môi trường.
- Lệnh trong README nên được chạy trong CI (vd. job "docs smoke test") để chống lỗi thời (suy luận).
- Agent có thể đọc README qua import: Claude Code cho `@README` trong CLAUDE.md (https://code.claude.com/docs/en/memory, 2026). Vì vậy đừng lặp lại nội dung README trong AGENTS.md.

---

## D2 — File hướng dẫn cho AI agent (AGENTS.md / CLAUDE.md / rules)

**1) Ứng viên**
- **AGENTS.md** (agents.md): "README for agents", định dạng Markdown tự do. Do Agentic AI Foundation thuộc Linux Foundation quản lý. Trang này tự công bố hơn 60k repo dùng. Hỗ trợ file lồng nhau, file gần nhất được ưu tiên (https://agents.md/, 2026).
- **CLAUDE.md + `.claude/rules/`** (Anthropic):
  - Khuyến nghị "target under 200 lines per CLAUDE.md file".
  - Rules giới hạn theo `paths` để chỉ nạp khi agent chạm file khớp mẫu.
  - Claude Code hiện đọc trực tiếp AGENTS.md khi không có CLAUDE.md (từ v2.1.277), hoặc qua `@AGENTS.md` import (https://code.claude.com/docs/en/memory, 2026).
- **`.github/copilot-instructions.md`, `.cursor/rules`**: đặc thù từng công cụ.
- **Adoption thực tế:** chỉ 466/10.000 repo phổ biến (5%) có context file. 50% số file AGENTS.md *chưa từng được sửa* sau khi tạo. Chưa có cấu trúc chuẩn (Mohsenimofidi et al., MSR '26, https://arxiv.org/abs/2510.21413).

**Bằng chứng hiệu quả (quan trọng nhất của mục này)**
- **Gloaguen et al. (ETH, arXiv:2602.11988, 2026):**
  - Context file do LLM sinh ra làm *giảm* tỉ lệ giải task: −0,5% trên SWE-bench Lite, −2% trên AGENTbench. Chi phí tăng khoảng 20–23%.
  - File do người viết chỉ cải thiện "marginal", khoảng +4%, và chi phí tăng tối đa 19%.
  - Khuyến nghị: chỉ mô tả "minimal requirements". Yêu cầu thừa làm task khó hơn vì agent tuân theo chúng.
- **Lulla et al. (arXiv:2601.20404, 2026, qua tìm kiếm):** có AGENTS.md đi kèm runtime trung vị thấp hơn 28,64% và output token thấp hơn 16,58%. Mẫu nhỏ: 10 repo, 124 PR.
- **Anthropic:** với mỗi dòng, hãy hỏi *"Would removing this cause Claude to make mistakes?"* Nếu không thì xoá. File quá dài khiến agent bỏ qua chỉ dẫn (https://code.claude.com/docs/en/best-practices, 2026).

**2) Chọn**
- **Một AGENTS.md ở gốc repo, do người viết tay, làm nguồn duy nhất.**
- CLAUDE.md (nếu cần) chỉ gồm `@AGENTS.md` cộng vài dòng đặc thù Claude.
- Quy tắc theo vùng code để trong `.claude/rules/*.md` có `paths`, hoặc AGENTS.md lồng trong thư mục con.
- **Không** commit file do `/init` hay LLM sinh ra mà không cắt gọt.

**3) Mục bắt buộc**
- Commands: build, test (một test, cả suite), lint, typecheck.
- Conventions khác mặc định (chỉ những gì agent không tự suy ra được).
- Gotchas / env quirks: biến môi trường, service phụ thuộc.
- Boundaries: thư mục hoặc file không được sửa (migrations, generated, secrets).
- Verification: "done" nghĩa là lệnh nào phải xanh.
- PR/commit etiquette (ngắn).

Tuỳ chọn: link ARCHITECTURE.md/ADR (link, không chép lại), skill cho quy trình nhiều bước.

**4) Độ dài:** 30–150 dòng, trần 200 dòng theo Anthropic. Một bài blog tổng hợp từ nghiên cứu còn gợi ý 10–20 dòng (allstacks.com, 2026, nguồn thứ cấp).

**5) Anti-pattern**
- File sinh tự động (Gloaguen 2026).
- Mô tả từng file, cây thư mục, tổng quan kiến trúc: `/doctor` của Claude Code mặc định cắt chính các phần này.
- Nhấn mạnh "IMPORTANT" ở mọi dòng.
- File không ai sửa (50% theo MSR '26).
- Chỉ dẫn mâu thuẫn giữa các file lồng nhau.

**6) Khác biệt khi có AI:** đây là loại tài liệu *duy nhất* chỉ tồn tại vì AI.
- Điều *bắt buộc tuyệt đối* (chặn ghi vào migrations, chạy lint sau mỗi lần sửa) phải chuyển thành **hook / CI gate**. Anthropic nói rõ CLAUDE.md là "advisory", còn hooks là "deterministic".
- Thêm quy tắc mới khi agent mắc cùng một lỗi lần thứ hai (Anthropic memory docs).

---

## D3 — Tài liệu kiến trúc tổng quan

**1) Ứng viên**
- **arc42:** 12 mục (Introduction & Goals … Glossary). Dùng từ 2005, giấy phép CC BY-SA. "tailorable", có bản "arc42 canvas" một trang (https://arc42.org/overview). Ưu điểm: đầy đủ. Nhược điểm: 12 mục là quá nhiều cho team 5 người, dễ rot.
- **C4 model:** System Context, Container, Component, Code, cộng các sơ đồ phụ (https://c4model.com/). Ưu điểm: ngôn ngữ sơ đồ chung. Nhược điểm: C4 *không* tự nói cấp nào là đủ, đã kiểm FAQ (https://c4model.com/faq).
- **ARCHITECTURE.md (matklad, 2021):**
  - Ngắn, chỉ ghi "things that are unlikely to frequently change".
  - Gồm codemap, invariants (nhất là những gì *vắng mặt*), boundaries, cross-cutting.
  - Gọi tên symbol thay vì link, vì link sẽ hỏng.
  - Xem lại vài lần mỗi năm thay vì đồng bộ liên tục.
  - Ví dụ thật: rust-analyzer (https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html).

**2) Chọn:** **ARCHITECTURE.md kiểu matklad, kèm 1–2 sơ đồ C4 (Context + Container) dạng diagram-as-code** (Mermaid/Structurizr) trong cùng file. Dùng arc42 như checklist tham khảo, không làm template phải điền đủ (suy luận dựa trên các nguồn trên).

**3) Mục bắt buộc**
- Bird's-eye overview: bài toán, người dùng.
- Sơ đồ Context + Container.
- Codemap: module, trách nhiệm, chỗ tìm.
- Invariants & boundaries.
- Cross-cutting: auth, logging, error handling.
- Link sang danh sách ADR.

Tuỳ chọn: Deployment view, Quality goals, Risks/Tech debt (các mục arc42 4, 7, 10, 11).

**4) Độ dài:** 1–4 trang. Sơ đồ ≤2. Cấp Component/Code chỉ vẽ khi thật cần, vì code là nguồn sự thật (suy luận).

**5) Anti-pattern**
- Điền đủ 12 mục arc42 cho dự án nhỏ.
- Sơ đồ ảnh PNG không sửa được, nên không ai cập nhật.
- Mô tả "how each module works" trong tài liệu tổng quan (matklad khuyên không).

**6) Khi có AI**
- Agent tự đọc được code. Giá trị còn lại của tài liệu kiến trúc là *invariants và ranh giới không thể suy ra từ code*.
- Đây cũng chính là thứ Anthropic khuyên đưa vào CLAUDE.md ("Architectural decisions specific to your project"), trong khi khuyên *loại* "file-by-file descriptions".
- Nên để AGENTS.md link tới ARCHITECTURE.md thay vì chép lại.

---

## D4 — ADR (Architecture Decision Record)

**1) Ứng viên**
- **Nygard (2011):** Title, Context, Decision, Status, Consequences. "one or two pages". Bất biến, bị thay thế thì đánh dấu superseded. Lưu trong repo `doc/arch/adr-NNN.md` (https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
  - Adoption: nghiên cứu MSR trên GitHub cho thấy *đa số repo dùng mẫu Nygard* (Buchgeher et al., IEEE Access 2023).
- **MADR 4.0.0 (2024-09-17):**
  - Bắt buộc: Context and Problem Statement, Considered Options, Decision Outcome.
  - Tuỳ chọn: Decision Drivers, Consequences, Confirmation, Pros/Cons, More Information. Có bản `adr-template-minimal.md` (https://adr.github.io/madr/).
  - Ưu điểm: bắt buộc liệt kê phương án. Nhược điểm: bản đầy đủ dài.
- **Y-statement (Zdun/Zimmermann, gốc từ Fairbanks):** một câu "In the context of…, facing…, we decided for… to achieve…, accepting…" (https://en.wikipedia.org/wiki/Architectural_decision). Ưu điểm: cực nhẹ, có thể đặt trong comment code. Nhược điểm: thiếu ngữ cảnh khi cần tranh luận.
- **Danh mục biến thể:** Tyree/Akerman, Alexandrian, ITD… Lời khuyên: một ADR cho một quyết định, ghi ngày cho các giả định dễ lỗi thời (https://github.com/joelparkerhenderson/architecture-decision-record).

**Bằng chứng phản biện**
- Adoption ADR "still low". Khoảng một nửa repo có ADR chỉ có 1–5 bản ghi, tức là thử rồi bỏ (Buchgeher 2023).
- Trong khoảng 5.800 ADR, khoảng 63% được tạo với trạng thái "accepted" ngay từ đầu, bỏ qua bước thảo luận. Tương quan giữa thuộc tính ADR và chất lượng dự án chỉ yếu (ICSA 2026, https://conf.researchr.org/details/icsa-2026/icsa-2026-papers/34/…).
- Spotify (2020) khuyên viết ADR "almost always", kể cả để ghi bù quyết định cũ. Quyết định lớn thì qua RFC trước, rồi chốt bằng ADR (https://engineering.atspotify.com/2020/04/when-should-i-write-an-architecture-decision-record).

**2) Chọn:** **MADR minimal** (4 mục). Chấp nhận ADR dạng Nygard rút gọn nếu team thích. Quy tắc: ADR đi qua **PR với status = proposed**, merge thì mới accepted. Như vậy tránh được lỗi "63% accepted ngay".

**3) Mục bắt buộc**
- Title (quyết định, không phải vấn đề).
- Status + Date.
- Context & Problem.
- Considered Options (≥2).
- Decision Outcome.
- Consequences (gồm cả mặt xấu).

Tuỳ chọn: Decision Drivers, Confirmation (cách kiểm chứng: fitness test, lint rule), More Information.

**4) Độ dài:** ≤1 trang, trần 2 trang theo Nygard. Kỳ vọng thực tế 5–20 ADR/năm cho team nhỏ (suy luận).

**5) Anti-pattern**
- Viết ADR sau khi đã code xong, status accepted luôn (ICSA 2026).
- Sửa ADR cũ thay vì supersede.
- Gộp nhiều quyết định vào một bản ghi.
- Ghi những quyết định tầm thường, gây "nghi lễ hoá".
- Có thư mục adr/ với 3 bản ghi rồi bỏ (Buchgeher 2023).

**6) Khi có AI**
- ADR là nguồn "why" cho agent, nên AGENTS.md trỏ tới `docs/adr/`.
- Agent dễ viết nháp ADR (đã có nghiên cứu sinh ADR bằng LLM: arXiv:2604.03826, 2026, qua tìm kiếm). Nhưng người phải viết mục Options/Consequences, nếu không sẽ thành lời biện hộ hậu kiểm (suy luận).
- Mục "Confirmation" nên là check tự động (lint, arch test) để agent không vi phạm.

---

## D5 — API contract & quy ước API

**1) Ứng viên**
- **OpenAPI 3.x (contract-first):**
  - Postman State of API: JSON Schema là spec được dùng nhiều nhất. Swagger 2.0 và OpenAPI 3.x xếp sau, gần ngang nhau (2023, qua tìm kiếm; số 2020: Swagger 2.0 43,9%, OAS3 27,8%).
  - Ưu điểm: sinh client, sinh mock, kiểm thử contract. Nhược điểm: viết tay YAML dài.
- **Zalando RESTful API Guidelines:**
  - Quy tắc dạng MUST/SHOULD/MAY theo RFC 2119.
  - API-first với OpenAPI 3.1. Lỗi dùng `application/problem+json`.
  - Ưu tiên tránh versioning; nếu cần thì versioning qua media type, không qua URL.
  - Ưu tiên phân trang bằng cursor (https://opensource.zalando.com/restful-api-guidelines/).
  - Ưu điểm: rất đầy đủ, có linter (Zally). Nhược điểm: quá dài, hơn 360k ký tự.
- **Google AIP:** khoảng 73 AIP, mỗi AIP là một tài liệu ngắn, có linter (https://google.aip.dev/1). Ưu điểm: mô-đun. Nhược điểm: thiên về gRPC/resource-oriented.
- **Microsoft REST API Guidelines** (chưa xác minh URL).

**2) Chọn**
- **File `openapi.yaml` là contract (nguồn sự thật, lint trong CI bằng Spectral/Redocly).**
- Thêm **`docs/api-guidelines.md` 1–2 trang** gồm ~10–15 quy tắc MUST chọn lọc từ Zalando: naming, lỗi problem+json, phân trang, versioning, idempotency, auth.
- Không chép nguyên style guide lớn (suy luận).

**3) Mục bắt buộc (guideline)**
- Naming (path, field casing).
- Error format (RFC 9457 / problem+json).
- Pagination.
- Versioning & breaking change policy.
- AuthN/AuthZ.
- Idempotency / retry.

Contract bắt buộc có: schemas, error responses, examples.

**4) Độ dài:** guideline ≤2 trang. Contract dài bao nhiêu tuỳ API, nhưng phải được sinh/kiểm tự động.

**5) Anti-pattern**
- Spec viết sau code và lệch dần khỏi code. Đây là dạng doc rot, và lỗi "incorrectness" nằm trong ba lỗi nặng nhất (Uddin & Robillard 2015).
- Style guide 100 quy tắc không có linter.
- Tài liệu API trên wiki tách khỏi repo.

**6) Khi có AI**
- Contract máy đọc được là đầu vào lý tưởng cho agent: sinh handler, sinh test contract.
- Quy tắc API nên nằm trong rule có `paths: src/api/**` (Anthropic có ví dụ đúng loại rule này), kèm **linter làm gate**. Agent hay "quên" quy ước văn xuôi, còn linter thì không quên (suy luận).

---

## D6 — Spec / design doc / RFC cho feature

**1) Ứng viên**
- **Google design doc (Malte Ubl, 2020):**
  - Mục: Context and scope, Goals/Non-goals, The actual design, Alternatives considered, Cross-cutting concerns.
  - "sweet spot… 10–20ish pages" cho dự án lớn. "Mini design doc" 1–3 trang cho thay đổi nhỏ.
  - **Không viết** khi bài toán không mơ hồ, hoặc khi doc chỉ là "implementation manual" không có trade-off.
  - Thừa nhận "we humans are bad at updating documents" (https://www.industrialempathy.com/posts/design-docs-at-google/).
- **Rust RFC:** Summary, Motivation, Guide-level, Reference-level, Drawbacks, Rationale & alternatives, Prior art, Unresolved questions, Future possibilities. **Kubernetes KEP:** cộng Production Readiness Review, mẫu trống khoảng 4–5k từ.
  - Ưu điểm: chặt chẽ. Nhược điểm: quá nặng cho team nhỏ. KEP là chuẩn cho dự án hàng nghìn contributor.
- **Oxide RFD:** trạng thái prediscussion → ideation → discussion → published → committed / abandoned. Thảo luận trên PR, merge là publish. "timely rather than polished" (https://rfd.shared.oxide.computer/rfd/0001). Đây là mô hình docs-as-code tốt nhất cho startup.
- **Spec-driven tools** (GitHub spec-kit khoảng 142k sao: constitution → specify → plan → tasks → implement; Kiro; Tessl):
  - **Phản biện của Böckeler (martinfowler.com, 15/10/2025):** spec-kit sinh nhiều markdown "verbose and tedious to review". Kiro biến một bug một dòng thành 4 user story với 16 acceptance criteria, như "sledgehammer to crack a nut". Với story 3–5 điểm, tác giả bỏ dở, và agent vẫn bỏ qua chỉ dẫn hoặc tạo class trùng lặp (https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).
- **Thực tế ở công ty:** Pragmatic Engineer: RFC phổ biến (Uber, Stripe, Spotify…). Nhưng incident.io *không bắt buộc* RFC. Nhiều nơi dùng ADR/decision record làm dạng nhẹ (https://blog.pragmaticengineer.com/rfcs-and-design-docs/, 2022, cập nhật 2024).

**2) Chọn:** **"Mini design doc" 1–3 trang theo khung Google, quy trình kiểu Oxide RFD** (file `docs/rfd/NNNN-*.md`, thảo luận trên PR, có trạng thái).
- Ngưỡng kích hoạt: thay đổi mơ hồ, nhiều trade-off, ảnh hưởng nhiều module hoặc dữ liệu/API công khai, hoặc ước tính hơn 1 tuần (suy luận; ghi chú sách của Larson nói tới mốc "longer than a month", qua tìm kiếm).
- Dưới ngưỡng: mô tả trong issue/PR là đủ.

**3) Mục bắt buộc**
- Context & Problem.
- Goals / **Non-goals**.
- Proposed design: API/data model sketch, sơ đồ nếu cần.
- Alternatives considered.
- Risks & rollout/rollback.
- **Verification**: cách chứng minh feature chạy end-to-end.

Tuỳ chọn: Security/privacy, Observability, Open questions, Milestones.

**4) Độ dài:** 1–3 trang. Hơn 5 trang thì tách nhỏ (suy luận, theo Ubl).

**5) Anti-pattern**
- Design doc cho thay đổi không mơ hồ.
- "Implementation manual" không có phương án thay thế (Ubl).
- Doc không được cập nhật sau khi triển khai. Oxide xử lý bằng trạng thái "committed", Google bằng doc sửa đổi đi kèm.
- Spec do AI sinh dài hơn code cần review (Böckeler 2025).

**6) Khi có AI**
- Spec giờ là *prompt dài hạn*. Anthropic khuyên spec tốt là "self-contained": nêu tên file/interface, nêu out-of-scope, kết thúc bằng bước kiểm chứng end-to-end.
- Có thể để agent phỏng vấn người viết spec, rồi thực thi trong phiên mới (https://code.claude.com/docs/en/best-practices).
- **Tránh** áp toàn bộ pipeline spec-kit cho mọi task. Chỉ dùng cho feature cỡ trung trở lên, và để người viết mục Non-goals và Verification.

---

## D7 — Test strategy + Definition of Done

**1) Ứng viên**
- **Practical Test Pyramid** (Ham Vocke, martinfowler.com, 2018):
  - Nhiều unit test, ít E2E. Tránh "ice-cream cone".
  - Đẩy test xuống tầng thấp nhất có thể, xoá test trùng giữa các tầng.
  - E2E chỉ cho hành trình người dùng quan trọng (https://martinfowler.com/articles/practical-test-pyramid.html).
- **Testing Trophy** (Kent C. Dodds, 2018/2021): static → unit → **integration (lớn nhất)** → E2E. "Write tests. Not too many. Mostly integration." Hợp với frontend/web app (https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications).
- **Test plan kiểu IEEE 829/ISO 29119** (chưa xác minh URL): nặng, phù hợp môi trường có quy định chặt. Không phù hợp team nhỏ (suy luận).
- **DoD (Scrum Guide 2020):** "formal description of the state of the Increment when it meets the quality measures required" (https://scrumguides.org/scrum-guide.html).

**2) Chọn:** **`docs/testing.md` một trang**, chọn pyramid (backend/lib) hoặc trophy (web app), cộng **DoD dạng checklist ngắn nằm ngay trong PR template**. DoD sống ở nơi mỗi PR phải chạm vào, không để trên wiki.

**3) Mục bắt buộc**

*Test strategy:*
- Các tầng test + tỉ lệ mong muốn.
- Cái gì mock / không mock.
- Lệnh chạy từng tầng.
- Test bắt buộc cho bug fix (regression test).
- Flaky test policy.

*DoD (5–7 dòng):*
- CI xanh (lint, types, tests).
- Có test cho hành vi mới.
- Docs/ADR cập nhật nếu đổi hành vi hoặc kiến trúc.
- Có review.
- Feature flag / rollback được.
- Không có secret trong diff.

**4) Độ dài:** test strategy ≤1 trang. DoD ≤7 mục, mỗi mục kiểm chứng được.

**5) Anti-pattern**
- Ice-cream cone (Vocke 2018).
- DoD dài để "đánh dấu cho có". Scrum.org cảnh báo "cheating" DoD bằng cách chấp nhận "good enough" (https://www.scrum.org/node/101, chưa xác định tác giả/năm).
- DoD có mục không kiểm được ("code sạch") (suy luận).
- Coverage % làm mục tiêu tự thân (suy luận).

**6) Khi có AI**
- Đây là thay đổi lớn nhất. Anthropic coi "give Claude a way to verify its work" là thực hành đòn bẩy cao nhất. Không có check chạy được thì "looks done" là tín hiệu duy nhất.
- Mỗi mục DoD nên **ánh xạ tới một lệnh/CI job** để agent tự chạy, hoặc thành Stop hook.
- Thêm vào DoD: "bằng chứng" (output test) trong PR, và review độc lập (subagent hoặc người) cho thay đổi của agent (https://code.claude.com/docs/en/best-practices).

---

## D8 — Pull request template

**1) Ứng viên**
- **GitHub `.github/pull_request_template.md`** (tài liệu GitHub "Using issue and pull request templates", qua tìm kiếm). Thực tế mỗi team tự viết.
- **Google eng-practices (CL descriptions):**
  - Dòng đầu là câu mệnh lệnh đứng độc lập. Thân mô tả vấn đề, lý do chọn cách làm, hạn chế đã biết.
  - Tránh "Fix bug". Đọc lại mô tả trước khi merge (https://google.github.io/eng-practices/review/developer/cl-descriptions.html).
  - Kích thước: "100 lines is usually a reasonable size… 1000 lines is usually too large" (…/small-cls.html).
- **Template dài kiểu checklist doanh nghiệp:** nhiều checkbox (chưa xác minh nguồn cụ thể).

**Bằng chứng thực nghiệm**
- Template chỉ có ở khoảng 1,2% repo GitHub. Template đi kèm ít PR trùng hơn, review nhanh hơn, ít comment hơn, *đặc biệt khi template hỏi mô tả và thông tin test* (Zhang et al. 2022, trích trong Pirouzkhah et al.).
- Li et al. (IEEE TSE 2022): sau khi áp dụng template, số issue/PR mới hằng tháng giảm. Người dùng phàn nàn về "excessive and irrelevant information request" (DOI 10.1109/TSE.2022.3224053, qua tìm kiếm).
- Pirouzkhah, Wurzel Gonçalves & Bacchelli (2026), 80K PR, 156 dự án:
  - "Code explanation" đi kèm khả năng merge cao hơn 12–20%.
  - Nêu rõ *loại feedback mong muốn* là yếu tố dự báo nhất quán nhất.
  - Đa số yếu tố khác có hiệu ứng nhỏ (https://arxiv.org/abs/2602.14611).

**2) Chọn:** **Template ngắn 4–5 mục theo Google CL description**, cộng checklist DoD (D7). Không quá 5 checkbox.

**3) Mục bắt buộc**
- **What & Why**: tóm tắt + link issue/spec/ADR.
- **How to verify**: lệnh, ảnh chụp, output test.
- **Risk / rollback**.
- **Feedback wanted**: chỗ cần reviewer nhìn kỹ, thứ tự review.
- **AI disclosure**: agent/công cụ dùng, phần nào do agent sinh.
- DoD checklist (≤5).

**4) Độ dài:** template ≤25 dòng. PR mục tiêu khoảng 100–400 dòng diff (dựa trên Google: 100 hợp lý, 1000 quá lớn).

**5) Anti-pattern**
- Template dài, hỏi thông tin không liên quan, khiến người ta xoá trắng hoặc tick bừa (Li et al. 2022).
- Mô tả "Fix bug" (Google).
- PR khổng lồ, đặc biệt PR do agent sinh (suy luận).
- Mô tả không cập nhật sau khi code đổi trong review (Google).

**6) Khi có AI**
- Agent viết mô tả PR rất dễ, nên rủi ro chuyển sang *mô tả dài, trơn tru nhưng không đúng*. Google nói mô tả do công cụ sinh vẫn phải đạt chuẩn như mô tả người viết.
- Bắt buộc "How to verify" có *bằng chứng thực*.
- Trailer `Assisted-by:`: LLVM yêu cầu ghi nhãn đóng góp có nhiều nội dung từ công cụ (https://llvm.org/docs/AIToolPolicy.html). Linux kernel quy định định dạng `Assisted-by: LLM [TOOL…]` và cấm agent tự thêm `Signed-off-by` (https://docs.kernel.org/process/coding-assistants.html).

---

## D9 — Runbook + postmortem

**1) Ứng viên**
- **Google SRE Book, Postmortem Culture (2017):**
  - Kích hoạt khi: downtime vượt ngưỡng, mất dữ liệu, on-call phải can thiệp, thời gian xử lý vượt ngưỡng, lỗi monitoring.
  - Blameless. "An unreviewed postmortem might as well never have existed" (https://sre.google/sre-book/postmortem-culture/).
  - Về runbook: ghi sẵn playbook cho "roughly a 3x improvement in MTTR" so với "winging it" (https://sre.google/sre-book/introduction/).
- **PagerDuty postmortem template:** Overview, What Happened, Contributing Factors, Resolution, Impact, Responders, Timeline (UTC), How'd We Do, Action Items, Messaging. Họp trong vòng 5 ngày làm việc (https://response.pagerduty.com/after/post_mortem_template/). Ưu điểm: rõ. Nhược điểm: nhiều phần dành cho tổ chức có Incident Commander và scribe.
- **Phản biện, Lorin Hochstein (USENIX 2020; SREcon 2026):** template chuẩn đánh mất chi tiết mà câu chuyện sự cố mang lại. Ông đề xuất mô tả dạng tường thuật (https://www.usenix.org/presentation/hochstein, qua tìm kiếm).
- **Lý do action item thất bại** (incident.io, blog của vendor): không có owner, sai công cụ theo dõi, mơ hồ ("Improve monitoring is a wish, not an action"), không có nhịp follow-up (qua tìm kiếm).

**2) Chọn**
- **Runbook:** mỗi alert một mục ngắn, *alert link thẳng tới runbook*. Một file `docs/runbooks/<service>.md`, các mục theo tên alert.
- **Postmortem:** khung PagerDuty rút gọn còn 6 mục, phần "What happened" viết dạng tường thuật (theo Hochstein). Chỉ viết khi chạm ngưỡng kích hoạt kiểu Google.

**3) Mục bắt buộc**

*Runbook / alert:*
- Ý nghĩa alert + mức nghiêm trọng.
- Dashboard/log link.
- Các bước chẩn đoán (lệnh copy-paste).
- Mitigation / rollback.
- Escalation (ai).
- Last verified (ngày).

*Postmortem:*
- Summary + Impact (số liệu).
- Timeline (UTC).
- Contributing factors (blameless).
- What went well / poorly.
- Action items (owner + hạn + ticket).
- Follow-up review date.

**4) Độ dài:** mỗi mục runbook ≤1 màn hình. Postmortem 1–2 trang. Sự cố nhỏ thì ghi 5 dòng trong ticket là đủ (suy luận).

**5) Anti-pattern**
- Postmortem không được review (Google).
- Action item không có owner (incident.io).
- Runbook lỗi thời. Một runbook lỗi thời khi môi trường thay đổi mà quy trình không đổi theo, không phải vì thời gian trôi qua (bài tổng hợp, qua tìm kiếm).
- Viết postmortem cho mọi sự cố, gây mệt mỏi (suy luận).
- Đổ lỗi cá nhân (Google).

**6) Khi có AI**
- Runbook có lệnh copy-paste chuẩn hoá cũng là đầu vào cho agent hỗ trợ on-call. Nhưng mọi hành động thay đổi production phải có người duyệt (suy luận).
- Agent tốt ở việc dựng timeline từ log/chat. Người phải viết contributing factors.
- Sự cố do agent gây ra (lệnh phá huỷ, secret lộ) nên có trường "agent involvement" trong postmortem (suy luận).

---

## D10 — Chính sách bảo mật + sử dụng AI agent

**1) Ứng viên**
- **SECURITY.md (GitHub):** nêu supported versions và cách báo cáo lỗ hổng. Bật **private vulnerability reporting** cho repo public (https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository).
- **OpenSSF oss-vulnerability-guide:** có template SECURITY.md. URL template cụ thể trả 404 khi kiểm tra, chưa xác minh đường dẫn mới.
- **Chính sách AI của dự án OSS (mẫu tốt để chép cho nội bộ):**
  - **LLVM AI Tool Use Policy** (cập nhật 2026-10-18):
    - Người phải đọc và review toàn bộ output của LLM trước khi xin review, và chịu trách nhiệm như tác giả.
    - Ghi nhãn `Assisted-by`.
    - Khái niệm "extractive contribution": đóng góp tốn công review hơn giá trị mang lại.
    - **Cấm agent hành động không có người duyệt**, ví dụ `@claude` GitHub agent, và cấm bot review tự post comment (https://llvm.org/docs/AIToolPolicy.html).
  - **Linux kernel:** AI không được thêm Signed-off-by. Có tag `Assisted-by: LLM …`. Người submit chịu trách nhiệm về giấy phép (https://docs.kernel.org/process/coding-assistants.html).
  - **Fedora (thông qua 22/10/2025):** người đóng góp là tác giả và chịu trách nhiệm. Phải công khai khi phần đáng kể do AI sinh mà không sửa. AI không được làm "sole or final arbiter" trong đánh giá đóng góp (https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/; trang bị Anubis chặn khi fetch, nội dung xác minh qua kết quả tìm kiếm).
  - **curl:** không dán "massive, AI-generated explanations" vào báo cáo lỗ hổng (https://curl.se/dev/vuln-disclosure.html).
- **Khung rủi ro:** OWASP Top 10 for Agentic Applications (công bố 9/12/2025, ASI01–ASI10) (https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026).

**2) Chọn:** hai file ngắn.
- **SECURITY.md** theo GitHub + private vulnerability reporting.
- **`docs/ai-policy.md` (hoặc một mục trong CONTRIBUTING)** dựa trên LLVM/kernel/Fedora: trách nhiệm con người, ghi nhãn, giới hạn quyền agent.
- Phần *thực thi* (deny list, sandbox, secret scanning) nằm trong **cấu hình** (settings/permissions, hooks, CI), không trong văn xuôi. Anthropic phân biệt rõ: settings là "technical enforcement", CLAUDE.md là "behavioral guidance" (https://code.claude.com/docs/en/memory).

**3) Mục bắt buộc**

*SECURITY.md:*
- Supported versions.
- Cách báo cáo (kênh riêng, không qua issue công khai).
- Thời gian phản hồi kỳ vọng.
- Scope.

*AI policy:*
- **Accountability**: người merge chịu trách nhiệm.
- **Disclosure**: trailer `Assisted-by:` / mục trong PR.
- **Data**: không đưa secret, dữ liệu khách hàng hay mã độc quyền vào công cụ chưa được duyệt.
- **Agent permissions**: được làm gì tự động, cái gì cần người duyệt (push main, migration, prod, xoá dữ liệu).
- **Review**: mọi PR do agent tạo phải có người review.
- **Allowed tools list**.

**4) Độ dài:** SECURITY.md ≤1 trang. AI policy 1–2 trang. LLVM và kernel đều chỉ khoảng 1 trang web.

**5) Anti-pattern**
- Chính sách AI chỉ là văn xuôi, không có rào kỹ thuật. Agent có thể bỏ qua chỉ dẫn (Böckeler 2025; Anthropic gọi CLAUDE.md là "advisory").
- Cấm hoàn toàn rồi bị lách ngầm (suy luận).
- Để agent tự trả lời hoặc tự review mà không có người (LLVM cấm).
- Báo cáo bảo mật do AI sinh không kiểm chứng (curl).

**6) Khi có AI:** loại tài liệu này *mới xuất hiện* vì AI.
- Thêm rủi ro prompt injection qua nội dung repo hoặc web: AGENTS.md hay file do người ngoài commit cũng là đầu vào. Claude Code hỏi duyệt import ngoài repo vì lý do này (memory docs).
- Nên tham chiếu OWASP Agentic Top 10 trong mục "threats" (1 đoạn).

---

## D11 — Team nhỏ thường thiếu gì, và cái gì không đáng làm

**Nên có (thường thiếu)**
1. **CONTRIBUTING/dev-setup chạy được.** Lỗi cài đặt là vấn đề số 1 (Aghajani 2020). Có thể gộp vào README nếu ngắn.
2. **Decision log nhẹ** (ADR, D4). Nghiên cứu cho thấy team thử rồi bỏ, nên cần quy tắc kích hoạt rõ.
3. **Glossary/domain terms** 1 trang (arc42 mục 12). Rất có ích cho agent vì tên miền nghiệp vụ không suy ra được từ code (suy luận).
4. **Ownership/"last verified"** trên mỗi tài liệu vận hành, và một CI check tài liệu: link checker, lệnh trong README chạy được, detector tham chiếu code lỗi thời kiểu Tan et al. (đã có GitHub Action, ICSME 2023, qua tìm kiếm).
5. **CHANGELOG / release notes** sinh tự động từ commit (suy luận).

**Không đáng làm (hoặc thu nhỏ triệt để)**
- **arc42 đầy đủ 12 mục.** Thay bằng ARCHITECTURE.md + C4 L1–L2.
- **Sơ đồ C4 cấp Component/Code** vẽ tay. Code và agent đọc code tốt hơn.
- **KEP-style RFC + PRR** cho team 3–10 người. Dùng mini design doc.
- **Test plan theo IEEE 829.**
- **Pipeline spec-driven đầy đủ cho mọi task nhỏ** (Böckeler 2025).
- **AGENTS.md do LLM sinh** (Gloaguen 2026), và CLAUDE.md riêng chép lại AGENTS.md.
- **Postmortem cho mọi sự cố nhỏ**, và **wiki tách khỏi repo** cho tài liệu kỹ thuật.

---

## Top 10 kết luận

1. Tài liệu lỗi thời là lỗi phổ biến nhất (93% theo GitHub 2017). Mỗi tài liệu phải gắn với một quy trình buộc phải chạm vào nó, nếu không thì đừng viết.
2. AGENTS.md viết tay, ngắn (≤200 dòng), chỉ ghi điều agent không tự suy ra. File do LLM sinh làm giảm hiệu quả và tăng khoảng 20% chi phí.
3. Quy tắc bắt buộc với agent phải là hook, CI hay permission. Văn xuôi chỉ là gợi ý.
4. README cần Why, Status và Quickstart chạy được. Đây là các phần README thực tế hay thiếu hoặc sai.
5. Dùng ARCHITECTURE.md kiểu matklad với C4 Context + Container thay cho arc42 đầy đủ.
6. Dùng MADR minimal, ≤1 trang, qua PR với status proposed. Phần lớn ADR thực tế bị "accepted" ngay, bỏ mất bước thảo luận.
7. API: OpenAPI là contract được lint trong CI, kèm 10–15 quy tắc MUST chọn từ Zalando.
8. Design doc chỉ viết khi có trade-off thật: mini doc 1–3 trang, quy trình RFD trên PR. Đừng áp spec-kit cho bug nhỏ.
9. DoD tối đa 5–7 mục, mỗi mục là một lệnh kiểm được, đặt trong PR template. PR template ngắn, có "How to verify" và "AI disclosure".
10. Runbook gắn vào alert. Postmortem có ngưỡng kích hoạt, phải được review, action item có owner. Chính sách AI 1 trang theo LLVM/kernel: người chịu trách nhiệm, `Assisted-by`, agent không tự merge.

## Bảng chọn cuối

| Loại | Template nền chọn | 3–6 mục bắt buộc | Độ dài |
|---|---|---|---|
| D1 README | standard-readme rút gọn + Why/Status | What/Why; Status & owner; Quickstart ≤5 lệnh; Dev/Test commands; Links docs; License/Owner | 1–2 màn hình |
| D2 Agent file | AGENTS.md viết tay (CLAUDE.md = `@AGENTS.md`) + `.claude/rules` theo paths | Commands; Conventions khác mặc định; Gotchas/env; Boundaries (không được sửa); Verification ("done" = lệnh nào xanh) | 30–150 dòng, trần 200 |
| D3 Kiến trúc | ARCHITECTURE.md (matklad) + C4 L1–L2 dạng code | Overview; Context+Container diagram; Codemap; Invariants & boundaries; Cross-cutting; Link ADR | 1–4 trang |
| D4 ADR | MADR 4 minimal (qua PR, status proposed) | Title+Status+Date; Context & Problem; Considered Options (≥2); Decision Outcome; Consequences (+/−) | ≤1 trang |
| D5 API | OpenAPI 3.1 (lint CI) + guideline rút từ Zalando | Naming; Error format (problem+json); Pagination; Versioning/breaking policy; Auth; Idempotency | Guideline ≤2 trang |
| D6 Spec/RFC | Mini design doc (Google) + quy trình Oxide RFD | Context; Goals/Non-goals; Design; Alternatives; Risks/rollout; Verification | 1–3 trang |
| D7 Test + DoD | Pyramid hoặc Trophy (1 trang) + DoD trong PR template | Tầng test & tỉ lệ; Mock policy; Lệnh chạy; Regression test cho bug; DoD ≤7 mục kiểm được | ≤1 trang + ≤7 dòng |
| D8 PR template | Google CL description + DoD checklist | What & Why + link; How to verify (bằng chứng); Risk/rollback; Feedback wanted; AI disclosure | ≤25 dòng |
| D9 Runbook + PM | Runbook theo alert; PagerDuty rút gọn + tường thuật | Runbook: ý nghĩa, chẩn đoán, mitigation, escalation, last verified. PM: impact, timeline, factors, action items (owner+hạn) | 1 màn hình/alert; PM 1–2 trang |
| D10 Security + AI | SECURITY.md (GitHub) + AI policy theo LLVM/kernel/Fedora | Supported versions; Kênh báo cáo riêng; Accountability; Disclosure `Assisted-by`; Data rules; Agent permissions (enforce bằng config) | 1 + 1–2 trang |

## Điều chưa chắc

- **Hiệu quả AGENTS.md:** hai nghiên cứu 2026 đo khác nhau (tỉ lệ thành công trên benchmark so với runtime/token trên PR thật) và mẫu nhỏ. Mức +4% của file người viết là "marginal". Kết quả có thể đổi theo model và agent; theo bài báo, file người viết giúp mọi agent trừ Claude Code. Một bài tóm tắt cũng ghi phần mở đầu là −3% nhưng các mục chi tiết là −0,5% và −2%: số liệu nội bộ bài báo không thống nhất.
- **PR template:** số liệu của Zhang et al. 2022 (1,2% adoption, review nhanh hơn) tôi chỉ đọc qua trích dẫn thứ cấp trong Pirouzkhah 2026, chưa đọc bản gốc. Tất cả đều là tương quan, không phải nhân quả.
- **Mốc 10–20 dòng cho AGENTS.md** đến từ blog thứ cấp. Mốc 200 dòng của Anthropic là khuyến nghị của nhà cung cấp, không phải kết quả thực nghiệm.
- **Số liệu OpenAPI mới nhất (2024–2026)** chưa xác minh. Postman 2023 không đưa phần trăm.
- **Chưa xác minh trực tiếp:** trang Fedora (bị chặn bot), trang gốc Y-statement của Zimmermann, template SECURITY.md của OpenSSF (404), bài báo Aghajani ICSE 2020 (chỉ qua kết quả tìm kiếm).
- **Ngưỡng kích hoạt design doc, kích thước PR và DoD ≤7 mục** là suy luận dựa trên các nguồn trên, chưa có nghiên cứu thực nghiệm cho team 3–10 người.
- **Spec-driven development** thay đổi rất nhanh. Phản biện của Böckeler là tháng 10/2025, công cụ có thể đã cải thiện.

## Nguồn

**Nghiên cứu thực nghiệm**
- GitHub Open Source Survey (2017): https://opensourcesurvey.org/2017/
- Aghajani et al., "Software Documentation Issues Unveiled", ICSE (2019): https://2019.icse-conferences.org/event/icse-2019-technical-papers-software-documentation-issues-unveiled
- Aghajani et al., practitioners' perspective, ICSE (2020) (qua tìm kiếm): https://www.inf.usi.ch/faculty/lanza/PUBS/P/Agha2020a.pdf
- Uddin & Robillard, "How API Documentation Fails", IEEE Software (2015): https://www.cs.mcgill.ca/~martin/papers/ieeesw2015.pdf
- Prana et al., "Categorizing the Content of GitHub README Files", EMSE (2018): https://arxiv.org/abs/1802.06997
- Tan, Wagner, Treude, outdated code element references (2022; EMSE 2024): https://arxiv.org/abs/2212.01479
- Stack Overflow Developer Survey (2024) (qua tìm kiếm): https://survey.stackoverflow.co/2024/developer-profile/
- Gloaguen et al., "Evaluating AGENTS.md" (2026): https://arxiv.org/abs/2602.11988
- Lulla et al., AGENTS.md efficiency (2026) (qua tìm kiếm): https://arxiv.org/html/2601.20404v2
- Mohsenimofidi et al., "Context Engineering for AI Agents in OSS", MSR '26 (2026): https://arxiv.org/abs/2510.21413
- Buchgeher et al., ADRs in OSS, IEEE Access (2023): https://research.jku.at/en/publications/using-architecture-decision-records-in-open-source-projects-an-ms/
- de Santana Junior et al., ADR Adoption Impact, ICSA (2026): https://conf.researchr.org/details/icsa-2026/icsa-2026-papers/34/Architecture-Decision-Records-Adoption-Impact-and-Developer-Engagement-in-Open-Sou
- Pirouzkhah, Wurzel Gonçalves, Bacchelli, "The Value of Effective Pull Request Description" (2026): https://arxiv.org/abs/2602.14611
- Li et al., issue/PR templates, IEEE TSE (2022) (qua tìm kiếm): https://unpaywall.org/10.1109%2FTSE.2022.3224053
- Postman State of the API (2023) (qua tìm kiếm): https://getpostman.com/state-of-api/api-technologies/

**Chuẩn, template, hướng dẫn**
- standard-readme: https://github.com/RichardLitt/standard-readme
- Diátaxis: https://diataxis.fr/
- AGENTS.md (2026): https://agents.md/
- Anthropic, Claude Code best practices (2026): https://code.claude.com/docs/en/best-practices
- Anthropic, Claude Code memory / CLAUDE.md (2026): https://code.claude.com/docs/en/memory
- matklad, ARCHITECTURE.md (2021): https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html
- C4 model: https://c4model.com/ và https://c4model.com/faq
- arc42: https://arc42.org/overview
- Nygard, Documenting Architecture Decisions (2011): https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- MADR 4.0.0 (2024): https://adr.github.io/madr/ và https://github.com/adr/madr
- ADR template collection: https://github.com/joelparkerhenderson/architecture-decision-record
- Spotify, When should I write an ADR (2020): https://engineering.atspotify.com/2020/04/when-should-i-write-an-architecture-decision-record
- Architectural decision / Y-statement: https://en.wikipedia.org/wiki/Architectural_decision
- Zalando RESTful API Guidelines: https://opensource.zalando.com/restful-api-guidelines/
- Google AIP-1: https://google.aip.dev/1
- Malte Ubl, Design Docs at Google (2020): https://www.industrialempathy.com/posts/design-docs-at-google/
- Rust RFC template: https://raw.githubusercontent.com/rust-lang/rfcs/master/0000-template.md
- Kubernetes KEP template: https://raw.githubusercontent.com/kubernetes/enhancements/master/keps/NNNN-kep-template/README.md
- Oxide RFD 1: https://rfd.shared.oxide.computer/rfd/0001
- Gergely Orosz, RFCs and design docs (2022, cập nhật 2024): https://blog.pragmaticengineer.com/rfcs-and-design-docs/
- Birgitta Böckeler, Understanding SDD (2025): https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- GitHub spec-kit (2026): https://github.com/github/spec-kit
- Ham Vocke, The Practical Test Pyramid (2018): https://martinfowler.com/articles/practical-test-pyramid.html
- Kent C. Dodds, Testing Trophy (2021): https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications
- Scrum Guide (2020): https://scrumguides.org/scrum-guide.html
- Scrum.org, DoD (năm chưa rõ): https://www.scrum.org/node/101
- Google eng-practices, CL descriptions và small CLs (2019+): https://google.github.io/eng-practices/review/developer/cl-descriptions.html và https://google.github.io/eng-practices/review/developer/small-cls.html
- Google SRE Book, Postmortem Culture và Introduction (2016/2017): https://sre.google/sre-book/postmortem-culture/ và https://sre.google/sre-book/introduction/
- PagerDuty postmortem template: https://response.pagerduty.com/after/post_mortem_template/
- Lorin Hochstein, Telling Stories About Incidents (2020) (qua tìm kiếm): https://www.usenix.org/presentation/hochstein
- incident.io, why post-mortem action items fail (vendor blog, qua tìm kiếm): https://incident.io/blog/why-do-post-mortem-action-items-fail-how-to-make-incident-follow-ups-actually-get-done

**Bảo mật và chính sách AI**
- GitHub, Adding a security policy: https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository
- GitHub, Private vulnerability reporting: https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/configuring-private-vulnerability-reporting-for-a-repository
- LLVM AI Tool Use Policy (2026): https://llvm.org/docs/AIToolPolicy.html
- Linux kernel, coding assistants (2025–2026): https://docs.kernel.org/process/coding-assistants.html
- Fedora AI-Assisted Contributions Policy (2025) (qua tìm kiếm): https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/
- curl vulnerability disclosure policy: https://curl.se/dev/vuln-disclosure.html
- OWASP Top 10 for Agentic Applications (12/2025): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026

**Thứ cấp**
- Allstacks blog về AGENTS.md (2026): https://www.allstacks.com/blog/agents-md-files-the-research-says-youre-probably-doing-them-wrong

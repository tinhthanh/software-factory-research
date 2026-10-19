# Báo cáo Nghiên cứu: Chuẩn hóa Bộ Tài liệu Phát triển Phần mềm (Docs-as-Code) cho Team 3–10 Kỹ sư kết hợp AI Coding Agent

**Ngày thực hiện:** 2026-10-19  
**Phạm vi:** Đánh giá, so sánh và lựa chọn template chuẩn (best practice) cho 10 loại tài liệu kỹ thuật cốt lõi (D1–D10) và khuyến nghị mở rộng/cắt giảm (D11) trong mô hình docs-as-code cho nhóm quy mô nhỏ (3–10 kỹ sư) cộng tác cùng AI coding agent.

---

## D1. README dự án (`README.md`)

### 1. Các ứng viên
* **Make a README (`dguo/makeareadme`):**
  * **Nguồn:** Danny Guo, `https://www.makeareadme.com/` và `https://github.com/dguo/makeareadme` (2018–2024).
  * **Mức độ phổ biến:** Tài liệu tham chiếu kinh điển cho cộng đồng phần mềm, được GitHub Docs và GitLab Docs dẫn lại làm hướng dẫn khởi tạo repo cơ bản (`https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes`, 2024).
  * **Ưu điểm:** Cực kỳ gọn nhẹ, thực dụng, tập trung vào khả năng đọc lướt nhanh của kỹ sư mới; không ép buộc cấu trúc cứng nhắc.
  * **Nhược điểm:** Thiếu tính chuẩn hóa máy đọc (machine-readablelinter) và thiếu các mục dành cho quản trị hệ thống nội bộ (như biến môi trường hoặc kiến trúc).
* **Standard Readme (`RichardLitt/standard-readme`):**
  * **Nguồn:** Richard Littauer, `https://github.com/RichardLitt/standard-readme` (2016–2024).
  * **Mức độ phổ biến:** Đạt hơn 6.400+ GitHub stars (`https://github.com/RichardLitt/standard-readme`, 2026), được áp dụng rộng rãi trong hệ sinh thái IPFS, Protocol Labs và hàng trăm thư viện npm thông qua công cụ kiểm tra tự động `standard-readme-linter`.
  * **Ưu điểm:** Quy định chặt chẽ thứ tự các đề mục (Title, Short Description, Table of Contents, Security, Background, Install, Usage, API, Maintainers, Contributing, License), hỗ trợ kiểm tra tuân thủ qua CI.
  * **Nhược điểm:** Thiên về thư viện mã nguồn mở (open-source packages) hơn là ứng dụng sản phẩm (product monorepo/microservices) của team nội bộ; nhiều mục như `API` hay `License` dư thừa với repo private `(suy luận)`.
* **Best-README-Template (`othneildrew/Best-README-Template`):**
  * **Nguồn:** Othneil Drew, `https://github.com/othneildrew/Best-README-Template` (2019–2025).
  * **Mức độ phổ biến:** Hơn 16.400+ GitHub stars và hàng nghìn bản fork (`https://github.com/othneildrew/Best-README-Template`, 2026), là một trong những template README được gắn sao nhiều nhất trên GitHub.
  * **Ưu điểm:** Trực quan, có sẵn khung trình bày cho sản phẩm ứng dụng (Prerequisites, Installation, Usage, Roadmap, Acknowledgments).
  * **Nhược điểm:** Chứa nhiều HTML/CSS inline, shields.io badges, banner đồ họa và mục lục thủ công gây nhiễu (noise) khi đọc dưới dạng văn bản thuần hoặc khi nạp vào context của AI agent `(suy luận)`.

### 2. Chọn
* **Template nền khuyến nghị:** Lai ghép giữa **Make a README** và cấu trúc cốt lõi của **Standard Readme** (tập trung vào 3 trụ cột *What – Why – How* được chứng minh qua nghiên cứu thực nghiệm của Prana et al. trên 4.226 mục README tại `https://arxiv.org/abs/1811.06959`,發表 trên *Empirical Software Engineering*, 2019).
* **Lý do:** Với team 3–10 người, `README.md` cần đóng vai trò là **Điểm khởi đầu dự án (Landing Page & Quickstart)** giúp kỹ sư mới (hoặc dev quay lại repo sau 3 tháng) chạy được hệ thống ở local trong dưới 10 phút, đồng thời dẫn link tới các tài liệu chuyên sâu khác mà không biến thành bãi rác chứa mọi thứ `(suy luận)`.

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc (5 mục):**
  1. `# <Tên dự án> + Mô tả 1 đoạn ngắn` (What & Why: hệ thống giải quyết bài toán gì, thuộc domain nào).
  2. `## Tech Stack & Prerequisites` (Ngôn ngữ, runtime version, Docker, công cụ bắt buộc).
  3. `## Quickstart / Local Setup` (Các câu lệnh copy-paste để cài đặt, khởi tạo biến môi trường từ `.env.example`, chạy DB migration và khởi động server).
  4. `## Verification & Testing` (Lệnh chạy test cơ bản và healthcheck để xác nhận môi trường local hoạt động đúng).
  5. `## Project Links / Documentation Map` (Liên kết trực tiếp tới `AGENTS.md`, `ARCHITECTURE.md`, `docs/adr/`, `docs/runbooks/` và môi trường Staging/Production).
* **Các mục tuỳ chọn:**
  * `## Deployment Overview` (nếu quy trình CI/CD đặc thù).
  * `## Troubleshooting / Common Gotchas` (các lỗi cài đặt thường gặp trên macOS/Linux).

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài:** **80–150 dòng Markdown** (tương đương 400–800 từ).
* **Mức chi tiết:** Chỉ giữ lại lệnh thực thi và đường dẫn; mọi giải thích dài dòng về thiết kế phải tách sang `ARCHITECTURE.md` hoặc `docs/`.

### 5. Anti-pattern
* **Biến README thành Wiki toàn tập (Encyclopedia README):** Nhồi nhét toàn bộ tài liệu API, lịch sử kiến trúc và quy ước code vào một file khiến không ai bảo trì và nhanh chóng lỗi thời (Prana et al., `https://arxiv.org/abs/1811.06959`, 2019).
* **Hướng dẫn cài đặt "ngầm định" (Implicit Setup Steps):** Ghi *"Cài đặt dependencies và chạy server"* nhưng thiếu phiên bản Node/Python cụ thể hoặc quên bước tạo `.env`, dẫn đến lỗi ngay lần chạy đầu tiên (`https://www.makeareadme.com/`, 2024).
* **Lạm dụng Badges và HTML trang trí:** Tốn công bảo trì và làm bẩn lịch sử diff của PR đối với repo nội bộ `(suy luận)`.

### 6. Khác biệt khi có AI agent
* **Tách bạch đối tượng đọc:** Trong kỷ nguyên AI agent, `README.md` ưu tiên phục vụ **con người (Human Onboarding)**, còn quy tắc vận hành chi tiết cho máy nằm ở `AGENTS.md` (`https://agents.md/`, 2025).
* **Tự động kiểm chứng (Executable README):** Agent có thể được giao nhiệm vụ đọc `README.md` và chạy thử các lệnh trong mục `## Quickstart` trên môi trường sạch (container) để phát hiện tài liệu bị lệch (documentation drift) so với `package.json` / `Makefile` `(suy luận)`.

---

## D2. File hướng dẫn cho AI agent (`AGENTS.md` / `CLAUDE.md` / rules)

### 1. Các ứng viên
* **AGENTS.md (`agentsmd/agents.md` – Agentic AI Foundation / Linux Foundation):**
  * **Nguồn:** Chuẩn mở khởi xướng bởi OpenAI, Google, Cursor, Factory và được chuyển giao cho Agentic AI Foundation (AAIF) thuộc Linux Foundation quản trị (`https://agents.md/`, `https://github.com/agentsmd/agents.md`, và `https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation`, 2025).
  * **Mức độ phổ biến:** Đã được hơn 60.000+ dự án mã nguồn mở áp dụng và được hỗ trợ nguyên bản bởi hầu hết các công cụ AI coding lớn: OpenAI Codex, GitHub Copilot, Cursor, Windsurf, Aider, Zed, Google Jules/Gemini (`https://agents.md/`, 2025–2026).
  * **Ưu điểm:** Trung lập nhà cung cấp (vendor-neutral), viết một lần dùng cho mọi agent trong team; hỗ trợ phân cấp theo thư mục con (nested `AGENTS.md` cho monorepo).
  * **Nhược điểm:** Không chứa cú pháp metadata đặc thù riêng của từng IDE (như glob auto-attach của Cursor hay `@import` riêng của một số bản CLI).
* **CLAUDE.md (Anthropic Claude Code Memory):**
  * **Nguồn:** Anthropic, `https://docs.anthropic.com/en/docs/claude-code/memory` và `https://code.claude.com/docs/en/best-practices` (2025–2026).
  * **Mức độ phổ biến:** Chuẩn mặc định cho mọi kỹ sư sử dụng hệ sinh thái Claude Code (CLI và IDE extensions).
  * **Ưu điểm:** Hỗ trợ cơ chế nạp phân tầng (`CLAUDE.md` ở root, thư mục con, và `CLAUDE.local.md` cho cá nhân), hỗ trợ cú pháp `@path/to/file` để nhúng tài liệu liên quan theo ngữ cảnh (`https://docs.anthropic.com/en/docs/claude-code/memory`, 2025).
  * **Nhược điểm:** Tên file gắn chặt với thương hiệu Anthropic; nếu team có người dùng Cursor, Copilot hoặc Codex thì phải cấu hình đọc chéo hoặc symlink.
* **GitHub Copilot Instructions (`.github/copilot-instructions.md` & `.github/instructions/*.instructions.md`):**
  * **Nguồn:** GitHub Docs, `https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot` (2024–2026).
  * **Mức độ phổ biến:** Phổ biến trong các doanh nghiệp chuẩn hóa trên hệ sinh thái GitHub Copilot Workspace, PR Review Agent và VS Code.
  * **Ưu điểm:** Hỗ trợ YAML frontmatter `applyTo: "**/*.ts"` để chỉ nạp quy tắc khi agent chạm vào đúng loại file, giúp tiết kiệm context window.
  * **Nhược điểm:** Bị khóa vào hệ sinh thái GitHub/VS Code ( dù từ cuối 2025 Copilot cũng đã hỗ trợ đọc `AGENTS.md`).
* **Cursor Project Rules (`.cursor/rules/*.mdc`):**
  * **Nguồn:** Cursor Documentation, `https://docs.cursor.com/context/rules` (2025–2026).
  * **Mức độ phổ biến:** Rất phổ biến với các team dùng Cursor IDE (thay thế cho file `.cursorrules` cũ đã bị deprecated).
  * **Ưu điểm:** Cho phép cấu hình 4 chế độ kích hoạt (Always, Auto Attached theo glob, Agent Requested theo mô tả, Manual).
  * **Nhược điểm:** Định dạng `.mdc` đặc thù của Cursor, gây phân mảnh nếu trong team 3–10 người có thành viên dùng công cụ khác `(suy luận)`.

### 2. Chọn
* **Template nền khuyến nghị:** **`AGENTS.md` đặt tại thư mục gốc làm nguồn chân lý duy nhất (Single Source of Truth)**, kết hợp tạo file `CLAUDE.md` gồm 1 dòng `@AGENTS.md` (hoặc symlink `ln -s AGENTS.md CLAUDE.md`) để tương thích tuyệt đối với Claude Code và mọi agent khác (`https://agents.md/`, 2025; `https://docs.anthropic.com/en/docs/claude-code/memory`, 2025).
* **Lý do:** Team 3–10 người thường sử dụng đa dạng công cụ (người dùng Claude Code, người dùng Cursor/Copilot, cộng với CI review agent). Duy trì nhiều bộ rule riêng lẻ sẽ dẫn đến bất đồng bộ. Chuẩn `AGENTS.md` của Linux Foundation giải quyết triệt để bài toán tính khả chuyển (portability).

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc (5 mục):**
  1. `## Commands (Build, Test, Lint, Typecheck)` (Câu lệnh chính xác kèm cờ chạy từng file đơn lẻ, ví dụ `pnpm vitest run <path>` để agent tự kiểm tra nhanh mà không chạy lại toàn bộ suite).
  2. `## Architecture & Directory Map` (Mô tả ngắn gọn 5–10 thư mục quan trọng nhất và luồng phụ thuộc chính, kèm con trỏ tới `ARCHITECTURE.md`).
  3. `## Code Style & Non-Obvious Conventions` (Chỉ ghi những quy ước mà linter không bắt được hoặc agent dễ làm sai do dữ liệu huấn luyện cũ, ví dụ: *"Dùng Zod v4 syntax, không dùng default export"*).
  4. `## Verification & Workflow Rules` (Quy trình bắt buộc trước khi kết thúc task: phải chạy typecheck + test liên quan, không tự ý sửa migration đã merge).
  5. `## Hard Boundaries / Do Not Touch` (Danh sách thư mục sinh tự động `src/generated/`, cấu hình bảo mật, hoặc lệnh bị cấm thực thi).
* **Các mục tuỳ chọn:**
  * `## Context Routing (Progressive Disclosure)` (Danh sách liên kết tới `docs/api-guidelines.md`, `docs/testing.md` kèm hướng dẫn *"Chỉ đọc file X khi sửa module Y"*).
  * Nested `AGENTS.md` trong từng gói của monorepo (`apps/web/AGENTS.md`, `apps/api/AGENTS.md`).

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài:** **60–150 dòng Markdown** (tối đa tuyệt đối không quá 200 dòng).
* **Mức chi tiết:** Áp dụng **"Mistake Test"** của Anthropic (`https://code.claude.com/docs/en/best-practices`, 2025): với mỗi dòng trong `AGENTS.md`, tự hỏi *"Nếu xóa dòng này, AI agent có mắc lỗi lặp đi lặp lại không?"* Nếu không, hãy xóa dòng đó.

### 5. Anti-pattern
* **Nhồi nhét hoặc dùng LLM tự sinh file `AGENTS.md` dài dòng (Context Bloat):** Nghiên cứu thực nghiệm của ETH Zurich & LogicStar AI (*"Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"*, `https://arxiv.org/abs/2602.11988`, tháng 2/2026) chứng minh rằng các file `AGENTS.md` do LLM tự sinh hoặc mô tả tổng quan dư thừa làm **giảm 0.5%–3% tỷ lệ giải quyết đúng tác vụ** trên SWE-bench/AGENTbench và làm **tăng 20%–23% chi phí token suy luận** do agent bị phân tán sự chú ý và chạy quá nhiều lệnh thăm dò không cần thiết.
* **Lặp lại quy tắc của Linter/Formatter:** Viết hàng chục dòng quy định thụt lề 2 dấu cách hay dấu chấm phẩy trong `AGENTS.md` thay vì để Prettier/Biome/Ruff xử lý tự động qua pre-commit hook (`https://code.claude.com/docs/en/best-practices`, 2025).
* **Sao chép nguyên văn tài liệu API hoặc Schema vào `AGENTS.md`:** Làm tràn context window ở mọi phiên làm việc thay vì dùng kỹ thuật tiết lộ tăng dần (Progressive Disclosure) qua đường dẫn file (`https://agents.md/`, 2025).

### 6. Khác biệt khi có AI agent
* **Đây là tài liệu sinh ra dành riêng cho Agent:** Khác với tài liệu cho người cần văn phong dẫn dắt, `AGENTS.md` cần viết dưới dạng mệnh lệnh khẳng định, cấu trúc danh sách phẳng (bullet points) và ưu tiên câu lệnh CLI xác định (deterministic commands).
* **Cập nhật theo vòng lặp phản hồi lỗi (Error-Driven Evolution):** Mỗi khi kỹ sư trong team thấy AI agent làm sai một quy ước trong PR, thay vì chỉ sửa code, kỹ sư bổ sung đúng 1 dòng quy tắc phòng ngừa vào `AGENTS.md` qua chính PR đó `(suy luận)`.

---

## D3. Tài liệu kiến trúc tổng quan (`ARCHITECTURE.md`)

### 1. Các ứng viên
* **Matklad's `ARCHITECTURE.md` (Alex Kladov / `rust-analyzer` style):**
  * **Nguồn:** Alex Kladov (`matklad`), bài viết kinh điển *"ARCHITECTURE.md"* tại `https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html` (2021) và kho tổng hợp `https://github.com/matklad/awesome-architecture.md` (2021–2025).
  * **Mức độ phổ biến:** Trở thành chuẩn thực tế (de facto standard) cho các dự án mã nguồn mở và hệ thống quy mô vừa (10k–200k LOC) như `rust-analyzer`, `esbuild`, `caddy`, `ruff`.
  * **Ưu điểm:** Chi phí bảo trì cực thấp; tập trung vào **bản đồ mã nguồn (Code Map)** và **các bất biến kiến trúc (Architectural Invariants)** ít thay đổi theo thời gian; nằm gọn trong 1 file Markdown duy nhất ở thư mục gốc.
  * **Nhược điểm:** Ít biểu đồ chuẩn hóa cho các bên liên quan phi kỹ thuật (non-technical stakeholders).
* **Mô hình C4 (C4 Model – Simon Brown) kết hợp Mermaid.js:**
  * **Nguồn:** Simon Brown, `https://c4model.com/` (2018–2025) và hỗ trợ C4/Flowchart trong Mermaid (`https://mermaid.js.org/syntax/c4.html`, 2023–2025).
  * **Mức độ phổ biến:** Phương pháp trực quan hóa kiến trúc phổ biến nhất ngành phần mềm hiện nay, được ThoughtWorks Technology Radar khuyến nghị và tích hợp sẵn trình render trên GitHub/GitLab Markdown.
  * **Ưu điểm:** Phân cấp rõ ràng 4 tầng trừu tượng (Level 1: System Context, Level 2: Container, Level 3: Component, Level 4: Code); với team nhỏ chỉ cần vẽ Level 1 và Level 2 bằng Mermaid ngay trong Markdown.
  * **Nhược điểm:** Nếu vẽ xuống tới Level 3 và Level 4 sẽ ngay lập tức bị lỗi thời sau vài PR đổi tên class/module (`https://c4model.com/`, 2024).
* **arc42 (`arc42.org`):**
  * **Nguồn:** Dr. Gernot Starke & Dr. Peter Hruschka, `https://arc42.org/` và `https://github.com/arc42/arc42-template` (2012–2025).
  * **Mức độ phổ biến:** Chuẩn vàng trong khối doanh nghiệp châu Âu và các hệ thống lớn cần kiểm toán kiến trúc chặt chẽ.
  * **Ưu điểm:** Toàn diện, gồm 12 mục cố định bao phủ từ mục tiêu chất lượng, ràng buộc, ngữ cảnh, khối xây dựng, kịch bản runtime đến rủi ro kỹ thuật.
  * **Nhược điểm:** Quá nặng nề cho team 3–10 người; việc duy trì đủ 12 mục thường dẫn đến tình trạng bỏ hoang tài liệu sau giai đoạn khởi tạo dự án `(suy luận)`.

### 2. Chọn
* **Template nền khuyến nghị:** **Matklad's `ARCHITECTURE.md`** làm khung văn bản, nhúng thêm **2 sơ đồ Mermaid theo tư duy C4 (Level 1 System Context + Level 2 Container)** và phần **Cross-cutting Concepts** rút gọn từ arc42.
* **Lý do:** Giải quyết đúng nỗi đau lớn nhất của cả kỹ sư mới lẫn AI coding agent: *"Thành phần X nằm ở đâu trong codebase, luồng dữ liệu đi như thế nào, và ranh giới nào không được phép vi phạm?"* mà không tốn quá 1–2 giờ cập nhật mỗi quý (`https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html`, 2021).

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc (5 mục):**
  1. `## Bird's-Eye View (System Context)` (1 đoạn văn + 1 sơ đồ Mermaid mô tả hệ thống làm gì, giao tiếp với người dùng và hệ thống bên ngoài nào).
  2. `## Containers & Deployment Topology` (Sơ đồ Mermaid C4 Level 2: Web app, API server, Worker, Database, Cache, Queue).
  3. `## Code Map (High-Level Directory & Module Guide)` (Liên kết tên thư mục/package với khái niệm kiến trúc; chỉ rõ điểm vào `entry points` của ứng dụng).
  4. `## Core Data Flow / Critical Runtime Scenarios` (Mô tả đường đi của 1–2 luồng nghiệp vụ quan trọng nhất từ lúc nhận request đến khi lưu DB/phát sự kiện).
  5. `## Architectural Invariants & Boundaries` (Các quy tắc bất biến, bao gồm cả những điều cố tình **không** làm, ví dụ: *"Module `domain/` tuyệt đối không được import từ `infrastructure/` hay `http/`"*).
* **Các mục tuỳ chọn:**
  * `## Cross-Cutting Concerns` (Cách xử lý AuthN/AuthZ, Logging/Tracing, Error Handling, Multi-tenancy trên toàn hệ thống — mượn từ mục 8 của `https://arc42.org/`, 2024).

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài:** **150–300 dòng Markdown** (khoảng 1.000–1.800 từ, đọc hết trong 5–10 phút).
* **Mức chi tiết:** Tuyệt đối **không dùng đường dẫn liên kết tới từng dòng code hay tên hàm nhỏ** dễ thay đổi; chỉ dừng ở cấp độ thư mục, package, hoặc interface/trait cốt lõi (`https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html`, 2021).

### 5. Anti-pattern
* **Vẽ sơ đồ bằng công cụ đóng (PNG/Draw.io/Lucidchart xuất ảnh tĩnh):** Không thể xem diff trong PR, không ai sửa được khi thiếu file gốc, và AI agent không thể cập nhật bằng văn bản (`https://c4model.com/`, 2024).
* **Tài liệu hóa xuống tận cấp độ Class/Method (C4 Level 4):** Tự động hóa bằng IDE/LSP hoặc đọc code trực tiếp luôn chính xác hơn tài liệu viết tay ở cấp độ này (`https://c4model.com/`, 2024).
* **Viết những điều hiển nhiên từ cấu trúc framework:** Giải thích lại cách hoạt động của Next.js hay Spring Boot thay vì giải thích kiến trúc nghiệp vụ đặc thù của dự án `(suy luận)`.

### 6. Khác biệt khi có AI agent
* **Bản đồ định hướng giảm thiểu chi phí tìm kiếm của Agent:** Khi có `ARCHITECTURE.md` chuẩn Matklad (được trỏ tới từ `AGENTS.md`), AI agent nắm bắt ngay cấu trúc module và bất biến kiến trúc mà không cần gọi hàng chục lệnh `grep`/`find` mù quáng trên toàn repo `(suy luận)`.
* **Biểu đồ dạng văn bản (Mermaid-as-Code):** Nhờ viết sơ đồ bằng khối lệnh ```` ```mermaid ````, AI agent vừa có thể **đọc hiểu** luồng kiến trúc từ mã nguồn Mermaid, vừa có thể **tự động cập nhật sơ đồ** trong cùng PR khi thêm một service hoặc queue mới `(suy luận)`.

---

## D4. ADR — Architecture Decision Record (`docs/adr/`)

### 1. Các ứng viên
* **Michael Nygard's ADR Template:**
  * **Nguồn:** Michael Nygard, bài viết *"Documenting Architecture Decisions"* trên Cognitect Blog (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`, 2011) và kho tổng hợp `https://github.com/joelparkerhenderson/architecture-decision-record` (2016–2026).
  * **Mức độ phổ biến:** Kho `joelparkerhenderson/architecture-decision-record` đạt hơn 17.000+ GitHub stars (2026); được ThoughtWorks Technology Radar xếp vào nhóm *Adopt* từ năm 2016 và được GitHub, AWS, Microsoft, Google Cloud khuyến nghị chính thức.
  * **Ưu điểm:** Cực kỳ tối giản (chỉ gồm 5 mục: Title, Status, Context, Decision, Consequences), dễ viết trong 15 phút.
  * **Nhược điểm:** Bản gốc của Nygard không có mục liệt kê tường minh **các phương án thay thế đã cân nhắc (Considered Options)**, khiến người đọc sau này không biết tại sao phương án B hoặc C lại bị loại bỏ (`https://adr.github.io/madr/`, 2024).
* **MADR — Markdown Architectural Decision Records (`adr/madr`):**
  * **Nguồn:** Oliver Kopp, Olaf Zimmermann et al., `https://adr.github.io/madr/` và `https://github.com/adr/madr` (2017–2025, phiên bản MADR 3.0 / 4.0).
  * **Mức độ phổ biến:** Hơn 2.800+ GitHub stars trên repo chính thức (`https://github.com/adr/madr`, 2026), được tích hợp làm template mặc định trong nhiều công cụ CLI quản lý ADR (`log4brains`, `adr-tools`) và tài liệu kiến trúc của Eclipse Foundation.
  * **Ưu điểm:** Bổ sung mục **Considered Options** và **Pros and Cons of the Options** rất rõ ràng; cung cấp sẵn cả bản đầy đủ (`template.md`) và bản rút gọn (`bare-minimal`).
  * **Nhược điểm:** Bản đầy đủ của MADR có khá nhiều metadata frontmatter và các mục phụ (Decision Drivers, Confirmation, More Information) hơi rườm rà nếu áp dụng máy móc cho quyết định nhỏ.
* **Y-Statements (Olaf Zimmermann / Uwe Zdun):**
  * **Nguồn:** Olaf Zimmermann, *IEEE Software* / Medium (`https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html`, 2015–2020) và `https://github.com/joelparkerhenderson/architecture-decision-record` (2025).
  * **Mức độ phổ biến:** Được sử dụng phổ biến như bản tóm tắt siêu ngắn gọn (1 câu gồm 6 mệnh đề: *In the context of... facing... we decided for... and neglected... to achieve... accepting...*).
  * **Ưu điểm:** Cực nhanh, ép người viết đi thẳng vào sự đánh đổi (trade-off).
  * **Nhược điểm:** Quá ngắn để lưu trữ các chi tiết kỹ thuật, benchmark hoặc ràng buộc phức tạp khi cần tra cứu sâu sau 1–2 năm `(suy luận)`.

### 2. Chọn
* **Template nền khuyến nghị:** **MADR Bare-Minimal (MADR rút gọn)** — thực chất là khung Nygard (Context, Decision, Consequences) cộng thêm mục **Considered Options** của MADR, và dùng 1 câu **Y-Statement** ở đầu mục Decision (`https://adr.github.io/madr/`, 2024).
* **Lý do:** Giúp team 3–10 người ghi lại không chỉ *"chúng ta đã chọn gì"* mà quan trọng hơn là *"tại sao chúng ta từ chối các phương án khác và chấp nhận đánh đổi gì"*, trong khi vẫn giữ thời gian viết mỗi ADR dưới 20–30 phút `(suy luận)`.

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc (5 mục, lưu tại `docs/adr/NNNN-slug-title.md`):**
  1. `# NNNN. <Tiêu đề quyết định ngắn gọn>` + **Metadata dòng đầu** (`Status`: Proposed | Accepted | Superseded by ADR-XXXX; `Date`: YYYY-MM-DD).
  2. `## Context and Problem Statement` (Bối cảnh kỹ thuật/nghiệp vụ, các giới hạn thực tế đang đối mặt).
  3. `## Considered Options` (Danh sách ít nhất 2–3 phương án đã đưa lên bàn cân, kèm ưu/nhược điểm ngắn gọn của từng phương án).
  4. `## Decision Outcome` (Phương án được chọn và lý do cốt lõi — khuyến khích mở đầu bằng 1 câu theo cấu trúc Y-statement).
  5. `## Consequences` (Hệ quả tích cực, hệ quả tiêu cực/nợ kỹ thuật phải chấp nhận, và các file/module bị ảnh hưởng).
* **Các mục tuỳ chọn:**
  * `## Confirmation / Compliance` (Cách kiểm tra xem quyết định này có được tuân thủ trong code hay không, ví dụ: thông qua bài test kiến trúc hoặc quy tắc trong `AGENTS.md`).
  * `## Links` (Liên kết tới PR, RFC hoặc ADR bị thay thế).

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài:** **40–100 dòng Markdown** (300–600 từ, gọn trong 1–2 trang màn hình).
* **Mức chi tiết:** Mỗi ADR chỉ giải quyết **đúng 1 quyết định kiến trúc có tính chất quan trọng** (Architecturally Significant Decision — ví dụ: chọn thư viện ORM, đổi cơ chế xác thực, tách worker queue).

### 5. Anti-pattern
* **Sửa đè lịch sử các ADR cũ đã thi hành (Mutating Historical ADRs):** Thay vì tạo ADR mới (`0012-switch-to-valkey.md`) và cập nhật trạng thái ADR cũ thành `Superseded by ADR-0012`, nhiều team lại xóa hoặc sửa nội dung ADR cũ làm mất dấu vết lịch sử (`https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions`, 2011).
* **Viết ADR cho những chuyện vụn vặt (Trivial Decisions):** Viết ADR chỉ để đổi tên biến hay chọn thư viện tiện ích nhỏ khiến team mệt mỏi (ADR fatigue).
* **Biến ADR thành tài liệu biện minh sau khi đã code xong xuôi (Rubber-stamp ADR):** Mục `Considered Options` chỉ liệt kê các phương án bù nhìn (strawman options) để hợp thức hóa lựa chọn cá nhân `(suy luận)`.

### 6. Khác biệt khi có AI agent
* **Bảo vệ "Hàng rào Chesterton" (Chesterton's Fence) trước AI Agent:** AI agent thường có xu hướng đề xuất "tối ưu hóa" hoặc "refactor" những đoạn code trông có vẻ vòng vo về lại cách làm tiêu chuẩn trên internet. Khi có `docs/adr/`, agent có thể tra cứu lý do lịch sử (ví dụ: *"Tại sao dùng polling thay vì WebSockets ở module X?"*) để không phá vỡ các quyết định đánh đổi có chủ đích của team `(suy luận)`.
* **Agent hỗ trợ nháp ADR từ cuộc thảo luận:** Kỹ sư có thể yêu cầu agent tổng hợp luồng thảo luận trên PR/Slack hoặc kết quả benchmark thử nghiệm thành bản nháp `docs/adr/NNNN-*.md` theo đúng chuẩn MADR để con người review `(suy luận)`.

---

## D5. API contract & quy ước API (OpenAPI, style guide, …)

### 1. Các ứng viên
* **OpenAPI Specification v3.1 (`OAI/OpenAPI-Specification`):**
  * **Nguồn:** OpenAPI Initiative (Linux Foundation), `https://spec.openapis.org/oas/v3.1.0` và `https://github.com/OAI/OpenAPI-Specification` (2021–2026).
  * **Mức độ phổ biến:** Hơn 29.000+ GitHub stars (`https://github.com/OAI/OpenAPI-Specification`, 2026); chuẩn công nghiệp tuyệt đối cho REST/HTTP APIs trên toàn cầu, tương thích 100% với JSON Schema draft 2020-12 kể từ bản 3.1.
  * **Ưu điểm:** Máy đọc được (machine-readable), cho phép sinh tự động SDK client, kiểu dữ liệu TypeScript (`openapi-typescript`), mock server và tài liệu tương tác (Scalar, Swagger UI, Redoc).
  * **Nhược điểm:** File YAML/JSON kích thước lớn rất khó viết tay từ đầu nếu không có công cụ hỗ trợ hoặc sinh từ code-first schema (như Zod/FastAPI/Pydantic).
* **Zalando RESTful API and Event Guidelines:**
  * **Nguồn:** Zalando SE, `https://opensource.zalando.com/restful-api-guidelines/` và `https://github.com/zalando/restful-api-guidelines` (2016–2025).
  * **Mức độ phổ biến:** Hơn 3.600+ GitHub stars (`https://github.com/zalando/restful-api-guidelines`, 2026); là một trong những bộ quy ước API doanh nghiệp nổi tiếng nhất thế giới, có bộ ruleset kiểm tra tự động bằng công cụ Spectral (`https://github.com/stoplightio/spectral`, 2025).
  * **Ưu điểm:** Quy định cực kỳ rõ ràng theo cấp độ RFC 2119 (`MUST`, `SHOULD`, `MAY`) về cách đặt tên URI, phân trang, lọc, xử lý lỗi chuẩn RFC 9457 / RFC 7807 (`Problem Details for HTTP APIs`, `https://www.rfc-editor.org/rfc/rfc9457.html`, 2023), và idempotency.
  * **Nhược điểm:** Bộ quy tắc gốc rất đồ sộ (hơn 200 trang/quy tắc), quá sức nếu bắt team 3–10 người đọc hết mà không chắt lọc.
* **Google API Improvement Proposals (`google.aip.dev`) / Protocol Buffers (gRPC):**
  * **Nguồn:** Google, `https://google.aip.dev/` (2019–2026).
  * **Mức độ phổ biến:** Chuẩn thiết kế API hướng tài nguyên (Resource-Oriented Design) hàng đầu thế giới, đặc biệt phổ biến cho các hệ thống dùng gRPC/Protobuf hoặc REST quy mô lớn.
  * **Ưu điểm:** Rất chặt chẽ về các phương thức chuẩn (List, Get, Create, Update, Delete), xử lý tác vụ chạy nền (Long-running operations - AIP-151) và phân trang bằng cursor/page token (AIP-158).
  * **Nhược điểm:** Nhiều khái niệm đặc thù của hệ sinh thái Google Cloud/Protobuf không hoàn toàn tự nhiên với các team web/SaaS nhỏ dùng JSON/REST thuần túy `(suy luận)`.
* **AsyncAPI Specification (`asyncapi/spec`):**
  * **Nguồn:** AsyncAPI Initiative (Linux Foundation), `https://www.asyncapi.com/` và `https://github.com/asyncapi/spec` (2017–2026).
  * **Mức độ phổ biến:** Hơn 3.900+ GitHub stars, chuẩn hàng đầu cho kiến trúc hướng sự kiện (Kafka, RabbitMQ, WebSockets).
  * **Ưu điểm:** Chuẩn hóa cấu trúc message payload và channel tương tự OpenAPI.
  * **Nhược điểm:** Chỉ cần thiết khi hệ thống có nhiều luồng sự kiện bất đồng bộ phức tạp.

### 2. Chọn
* **Template nền khuyến nghị:**
  1. **Contract định dạng máy đọc:** **OpenAPI 3.1 (`openapi.yaml`)** (hoặc `.proto` nếu dùng gRPC; `asyncapi.yaml` nếu có message broker) được kiểm tra tự động hoặc trích xuất từ schema code (Zod/TypeBox/Pydantic) trong CI (`https://spec.openapis.org/oas/v3.1.0`, 2021).
  2. **Tài liệu quy ước (`docs/api-guidelines.md`):** Chắt lọc **1 trang tóm tắt dựa trên Zalando RESTful API Guidelines** (kết hợp chuẩn lỗi **RFC 9457 Problem Details**) và thực thi tự động qua linter `.spectral.yaml` (`https://opensource.zalando.com/restful-api-guidelines/`, 2025).
* **Lý do:** Team nhỏ không có thời gian duy trì tài liệu API viết tay bằng bảng Markdown (vì chắc chắn sẽ lệch với code sau vài tuần). Kết hợp `openapi.yaml` (hợp đồng máy đọc) + `docs/api-guidelines.md` (1 trang quy ước thiết kế) mang lại độ chính xác 100% và tự động hóa việc sinh client code `(suy luận)`.

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc trong `docs/api-guidelines.md` (6 mục, đi kèm `openapi.yaml`):**
  1. `## URL Structure & Naming Conventions` (Danh từ số nhiều `/v1/orders`, kebab-case cho path, camelCase hoặc snake_case thống nhất cho JSON fields).
  2. `## Standard HTTP Methods & Status Codes` (Quy định rõ mã trả về chuẩn: `200`, `201`, `204`, `400`, `401`, `403`, `404`, `409`, `422`, `429`, `500`).
  3. `## Standard Error Format (RFC 9457 Problem Details)` (Cấu trúc JSON lỗi thống nhất gồm `type`, `title`, `status`, `detail`, `instance`, và mảng `errors` cho lỗi validation).
  4. `## Pagination, Filtering & Sorting` (Quy ước chuẩn một kiểu phân trang duy nhất, ưu tiên Cursor-based pagination với `cursor` & `limit`).
  5. `## Idempotency & Concurrency` (Sử dụng header `Idempotency-Key` cho các request `POST`/`PATCH` nhạy cảm như thanh toán, tạo đơn).
  6. `## Versioning & Breaking Changes Policy` (Thế nào là breaking change và quy tắc không phá vỡ tương thích ngược).
* **Các mục tuỳ chọn:**
  * `## Webhook & Event Payload Conventions` (Chuẩn CloudEvents hoặc AsyncAPI cho các sự kiện bắn ra ngoài).
  * `## Rate Limiting Headers` (`RateLimit-Limit`, `RateLimit-Remaining`, `Retry-After`).

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài:** File quy ước `docs/api-guidelines.md` chỉ nên dài **100–180 dòng Markdown** (600–1.000 từ); còn file `openapi.yaml` có độ dài tỉ lệ thuận với số lượng endpoint và được quản lý/sinh tự động.

### 5. Anti-pattern
* **Viết tài liệu danh sách API endpoint thủ công bằng bảng Markdown hoặc Wiki/Postman rời rạc ngoài repo:** Đây là nguyên nhân số một gây lệch hợp đồng (contract drift) giữa Backend và Frontend (`https://opensource.zalando.com/restful-api-guidelines/`, 2025).
* **Mỗi endpoint tự sáng tạo một kiểu gói dữ liệu trả về (Envelope) và format lỗi khác nhau:** Ví dụ chỗ trả về `{ error: "msg" }`, chỗ trả về `{ message: "msg", code: 123 }` khiến cả client developer lẫn AI agent không thể viết trình xử lý lỗi chung (`https://www.rfc-editor.org/rfc/rfc9457.html`, 2023).

### 6. Khác biệt khi có AI agent
* **Contract-First giúp hai AI Agent (Backend & Frontend) làm việc song song:** Khi file `openapi.yaml` được chốt và duyệt qua PR trước, team có thể giao một AI agent viết Backend implementation và một AI agent khác viết Frontend UI cùng lúc mà không sợ lệch kiểu dữ liệu `(suy luận)`.
* **Tránh nạp toàn bộ `openapi.yaml` khổng lồ vào context mặc định:** Với dự án có hàng trăm endpoint, file `openapi.yaml` có thể dài hàng chục nghìn dòng. Thay vào đó, giữ `docs/api-guidelines.md` thật gọn để agent đọc khi thiết kế endpoint mới, và dùng công cụ tạo kiểu tĩnh (như `openapi-typescript`) để agent kiểm tra hợp đồng thông qua trình biên dịch (`tsc`) `(suy luận)`.

---

## D6. Spec / Design Doc / RFC cho một feature (`docs/specs/`)

### 1. Các ứng viên
* **Google Design Doc Template (Malte Ubl / Industrial Empathy):**
  * **Nguồn:** Malte Ubl (cựu Principal Engineer tại Google), bài viết *"Design Docs at Google"* tại `https://www.industrialempathy.com/posts/design-docs-at-google/` (2020).
  * **Mức độ phổ biến:** Một trong những tài liệu tham chiếu về văn hóa thiết kế phần mềm có sức ảnh hưởng lớn nhất ngành công nghệ; được hàng nghìn công ty khởi nghiệp và tập đoàn áp dụng làm mẫu chuẩn.
  * **Ưu điểm:** Nhấn mạnh tính phi hình thức (informality), tập trung vào **Goals & Non-Goals**, đánh đổi thiết kế (Trade-offs), và độ dài linh hoạt theo quy mô tính năng.
  * **Nhược điểm:** Ban đầu được thiết kế cho Google Docs (tối ưu cho comment theo luồng của con người), chưa có phần tách danh sách tác vụ (Task Breakdown) hay tiêu chí kiểm thử thực thi cho AI coding agent.
* **GitHub Spec Kit (`github/spec-kit` – Spec-Driven Development / SDD):**
  * **Nguồn:** GitHub, `https://github.com/github/spec-kit` và bài công bố trên GitHub Blog *"Spec-driven development with AI: Get started with a new open source toolkit"* (`https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/`, 2025; phân tích đánh giá bởi ThoughtWorks / Martin Fowler tại `https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html`, 2025).
  * **Mức độ phổ biến:** Bùng nổ mạnh mẽ trong giai đoạn 2025–2026 với hơn 70.000–120.000+ GitHub stars (`https://github.com/github/spec-kit`, 2026), cùng xu hướng Spec-Driven Development trên các công cụ như AWS Kiro và Tessl.
  * **Ưu điểm:** Thiết kế chuyên biệt cho quy trình làm việc cùng AI agent theo chuỗi `Specify -> Plan -> Tasks -> Implement`; ép buộc làm rõ các điểm mơ hồ (`[NEEDS CLARIFICATION]`) và định nghĩa tiêu chí nghiệm thu trước khi viết code.
  * **Nhược điểm:** Theo đánh giá thực nghiệm trên trang Martin Fowler (`https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html`, 2025), quy trình đầy đủ của Spec Kit sinh ra quá nhiều file Markdown trung gian (`spec.md`, `plan.md`, `tasks.md`, `research.md`, `data-model.md`), dễ gây nặng nề (BDUF - Big Design Up Front) cho các tính năng vừa và nhỏ của team 3–10 người.
* **Rust RFCs (`rust-lang/rfcs`) & Kubernetes KEPs (`kubernetes/enhancements`):**
  * **Nguồn:** Rust Project (`https://github.com/rust-lang/rfcs/blob/master/0000-template.md`, 2014–2025) và Kubernetes SIG Architecture (`https://github.com/kubernetes/enhancements/blob/master/keps/sig-architecture/0000-kep-process/README.md`, 2018–2025).
  * **Mức độ phổ biến:** Chuẩn mẫu mực cho phát triển phần mềm phân tán qua Pull Request (docs-as-code RFC).
  * **Ưu điểm:** Cấu trúc chặt chẽ (Summary, Motivation, Guide-level explanation, Reference-level explanation, Drawbacks, Rationale and alternatives, Unresolved questions); KEP đặc biệt mạnh về tiêu chí sẵn sàng vận hành (Production Readiness Review).
  * **Nhược điểm:** Quá nặng về thủ tục đồng thuận cộng đồng (governance) đối với một nhóm sản phẩm chỉ có 3–10 kỹ sư `(suy luận)`.

### 2. Chọn
* **Template nền khuyến nghị:** **1-File Feature Spec lai ghép giữa Google Design Doc và Spec-Driven Development (SDD)** — gộp chung **Intent/Design (theo Google Design Doc)** và **Acceptance Criteria + Implementation Plan (theo SDD)** vào **một file duy nhất** `docs/specs/YYYY-MM-DD-feature-name.md` cho mỗi tính năng lớn.
* **Lý do:** Tránh được sự cồng kềnh sinh ra 4–5 file cho mỗi tính năng của `spec-kit` nguyên bản (`https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html`, 2025), nhưng vẫn cung cấp đủ hợp đồng kỹ thuật chặt chẽ để AI coding agent thực thi từng pha (phase) mà không bị "vibe coding" chệch hướng (`https://www.industrialempathy.com/posts/design-docs-at-google/`, 2020).

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc (6 mục):**
  1. `## 1. Context & Problem Statement` (Tại sao phải làm tính năng này ngay bây giờ? Giá trị người dùng/hệ thống là gì?).
  2. `## 2. Goals & Non-Goals` (Phạm vi làm và **những thứ cố tình không làm** trong đợt này để chặn scope creep).
  3. `## 3. Proposed Technical Design` (Thay đổi về Data Model/DB Schema, API endpoints/contracts, luồng xử lý chính và các file/module dự kiến sửa đổi).
  4. `## 4. Edge Cases, Security & Failure Modes` (Xử lý lỗi, race conditions, giới hạn quyền truy cập, chiến lược rollback/feature flag).
  5. `## 5. Verification & Acceptance Criteria` (Các kịch bản kiểm thử xác định dạng Given/When/Then hoặc danh sách test cases bắt buộc phải pass).
  6. `## 6. Phased Implementation Plan (Task Checklist)` (Chia nhỏ thành 2–5 bước tuần tự `- [ ] Phase 1: ...`, mỗi bước đủ nhỏ để AI agent thực hiện và kiểm chứng trong 1 PR/commit).
* **Các mục tuỳ chọn:**
  * `## Alternatives Considered` (Nếu quyết định thiết kế mang tính lâu dài, hoặc tách phần này thành 1 file ADR riêng trong `docs/adr/`).
  * `## Observability & Rollout Plan` (Metrics cần theo dõi, kịch bản миграция dữ liệu không downtime).

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài:** **100–250 dòng Markdown** (800–1.500 từ, tương đương 1–3 trang của Google Design Doc loại "Mini Design Doc" theo `https://www.industrialempathy.com/posts/design-docs-at-google/`, 2020).
* **Mức chi tiết:** Chỉ viết Spec cho các tính năng tốn **từ 2 ngày công trở lên** hoặc chạm vào nhiều module/DB schema. Các bugfix hoặc tính năng nhỏ dưới 1 ngày chỉ cần mô tả trực tiếp trong Issue/PR `(suy luận)`.

### 5. Anti-pattern
* **"Vibe Coding" tính năng lớn không qua Spec:** Giao một câu prompt ngắn gọn cho AI agent tự thiết kế cả DB schema, API lẫn UI, dẫn đến kiến trúc chắp vá và tốn thời gian đập đi xây lại nhiều hơn thời gian viết spec (`https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/`, 2025).
* **Nhầm lẫn Spec tính năng (tài liệu theo thời điểm - Point-in-time artifact) với Tài liệu kiến trúc sống (Living documentation):** Cố gắng cập nhật lại toàn bộ các file Spec cũ đã hoàn thành từ năm ngoái mỗi khi code thay đổi. Khi tính năng đã merge xong, Spec đóng vai trò lưu trữ lịch sử (chuyển trạng thái thành `Implemented`), còn các bất biến lâu dài phải được rút trích sang `ARCHITECTURE.md` hoặc `docs/adr/` (`https://www.industrialempathy.com/posts/design-docs-at-google/`, 2020).

### 6. Khác biệt khi có AI agent
* **Spec trở thành "Mã nguồn thực thi cấp cao" (Executable Prompt Artifact):** Trước đây Design Doc chỉ để kỹ sư đọc rồi tự gõ code; nay kỹ sư có thể dùng AI agent để **phỏng vấn ngược (Grill/Clarify)** tìm lỗ hổng trong bản nháp Spec, sau đó duyệt Spec qua PR và ra lệnh cho agent: *"Thực thi Phase 1 trong `docs/specs/2026-10-payment-webhook.md` và chạy bộ test tương ứng"* (`https://github.com/github/spec-kit`, 2025).
* **Tập trung vào `Non-Goals` và `Edge Cases`:** AI agent rất giỏi sinh code cho luồng thuận (happy path) nhưng hay tự ý thêm tính năng thừa (over-engineering) hoặc bỏ sót race condition. Mục `Non-Goals` và `Failure Modes` trong Spec giúp khóa chặt phạm vi sinh code của agent `(suy luận)`.

---

## D7. Test strategy + Definition of Done (`docs/testing-and-dod.md`)

### 1. Các ứng viên
* **Google Test Sizes Taxonomy (*Software Engineering at Google*):**
  * **Nguồn:** Titus Winters, Tom Manshreck, Hyrum Wright (Eds.), *Software Engineering at Google*, Chương 11 (Testing Overview) (`https://abseil.io/resources/swe-book/html/ch11.html`, O'Reilly, 2020).
  * **Mức độ phổ biến:** Chuẩn tham chiếu hàng đầu của ngành công nghệ về phân loại kiểm thử tự động trong CI/CD hiện đại.
  * **Ưu điểm:** Thay vì tranh cãi ngữ nghĩa mơ hồ giữa "Unit test" và "Integration test", Google phân loại dựa trên **giới hạn tài nguyên thực thi xác định (Deterministic Resource Constraints)**: **Small** (1 process, không I/O mạng/disk, chạy dưới vài mili-giây), **Medium** (1 máy local/container, cho phép localhost DB/loopback), và **Large** (nhiều máy/môi trường đầy đủ).
  * **Nhược điểm:** Cần kết hợp thêm hướng dẫn về độ phủ hành vi nghiệp vụ cho các ứng dụng web/UI.
* **Testing Trophy (Kent C. Dodds) & Practical Test Pyramid (Martin Fowler / Ham Vocke):**
  * **Nguồn:** Kent C. Dodds (`https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications`, 2018) và Martin Fowler / Ham Vocke (`https://martinfowler.com/articles/practical-test-pyramid.html`, 2018).
  * **Mức độ phổ biến:** Hai mô hình tư duy kiểm thử phổ biến nhất trong phát triển ứng dụng Web/Cloud hiện đại.
  * **Ưu điểm:** Testing Trophy đặt nền móng bằng **Static Analysis (Typecheck + Linter)** ở đáy, ưu tiên **Integration Tests** (kiểm thử tích hợp ở cấp độ module/API/component) vì mang lại ROI cao nhất, và giữ E2E tests ở mức tối thiểu cho các luồng sống còn.
  * **Nhược điểm:** Không phải là một template tài liệu hoàn chỉnh mà là mô hình phân bổ tỷ trọng test.
* **Scrum Guide Definition of Done (DoD) + GitLab Testing Standards:**
  * **Nguồn:** Ken Schwaber & Jeff Sutherland, *The 2020 Scrum Guide* (`https://scrumguides.org/scrum-guide.html`, 2020) và GitLab Engineering Handbook (`https://handbook.gitlab.com/handbook/engineering/testing/`, 2024–2025).
  * **Mức độ phổ biến:** Chuẩn quản trị chất lượng phổ biến nhất trong các đội ngũ Agile/DevOps toàn cầu.
  * **Ưu điểm:** Biến chính sách chất lượng trừu tượng thành **danh sách kiểm tra nhị phân (Pass/Fail checklist)** áp dụng cho mọi PR và tính năng trước khi đóng.
  * **Nhược điểm:** Nếu tách rời Test Strategy và Definition of Done thành 2 tài liệu dài dòng riêng biệt, team nhỏ sẽ không đọc cả hai `(suy luận)`.

### 2. Chọn
* **Template nền khuyến nghị:** Gộp chung thành **1 tài liệu ngắn gọn `docs/testing-and-dod.md`**, kết hợp **Testing Trophy + Google Test Sizes (Small/Medium/Large)** cho phần Chiến lược kiểm thử và **Scrum/GitLab Checklist** cho phần Definition of Done.
* **Lý do:** Team 3–10 người không có bộ phận QA thủ công độc lập quy mô lớn; chất lượng phụ thuộc trực tiếp vào pipeline tự động và chuẩn nghiệm thu của kỹ sư + AI agent trên từng PR `(suy luận)`.

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc (5 mục):**
  1. `## 1. Test Tiers & Resource Rules` (Định nghĩa rõ 4 tầng: **Static** [Typecheck/Lint], **Small/Unit** [Pure logic, không DB/network, <100ms], **Medium/Integration** [API/Service với Testcontainers hoặc DB thật ở local], **Large/E2E** [Chỉ dành cho 3–5 luồng Critical User Journeys như Login, Checkout]).
  2. `## 2. Mocking & Test Data Policy` (Quy tắc vàng: **Ưu tiên dùng DB thật trong container/in-memory và fake/stub ở ranh giới hệ thống bên thứ ba**; cấm mock nội bộ các class/function của chính mình gây ra bài test giòn/vô nghĩa — theo *SWE at Google*, `https://abseil.io/resources/swe-book/html/ch13.html`, 2020).
  3. `## 3. Flaky Test & Coverage Policy` (Không chạy đua theo con số % coverage giả tạo; bắt buộc 100% nhánh logic cho module thanh toán/bảo mật; test bị flaky trong CI phải được sửa hoặc quarantine trong vòng 24h).
  4. `## 4. Definition of Done (PR & Feature Checklist)` (Điều kiện bắt buộc để một tính năng được coi là Hoàn thành: Code pass CI + Test mới cho hành vi mới + Không giảm hiệu năng/bảo mật + Cập nhật docs/schema + Đã kiểm chứng trên môi trường Preview/Staging).
  5. `## 5. How to Run Tests Locally` (Các câu lệnh thực thi nhanh từng tầng test, đồng bộ với `AGENTS.md`).
* **Các mục tuỳ chọn:**
  * `## Performance / Load Testing Baseline` (Ngưỡng p95/p99 latency cho các API quan trọng).

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài:** **80–140 dòng Markdown** (500–800 từ).

### 5. Anti-pattern
* **Áp đặt chỉ tiêu phần trăm Code Coverage cứng nhắc (vd. bắt buộc >90% line coverage cho mọi file):** Theo Martin Fowler (*TestCoverage*, `https://martinfowler.com/bliki/TestCoverage.html`, 2012) và *SWE at Google* (2020), điều này thúc đẩy việc viết các bài test vô hồn (assertion-free tests hoặc test chỉ kiểm tra lệnh mock trả về đúng giá trị đã mock).
* **"Cây kem ốc quế" (Ice-Cream Cone Anti-pattern):** Ít unit/integration test nhưng lại có hàng trăm bài E2E UI test chạy mất 45 phút và liên tục đỏ vì lỗi mạng/timeout (`https://martinfowler.com/articles/practical-test-pyramid.html`, 2018).

### 6. Khác biệt khi có AI agent
* **Chống lại bệnh "Tự viết Mock để Test xanh" của AI Agent:** AI coding agent khi được yêu cầu *"viết test và đảm bảo test pass"* rất hay chọn đường tắt là dùng `vi.mock()` / `jest.mock()` để mock toàn bộ hàm xử lý bên dưới hoặc thậm chí sửa luôn assertion/production code cho khớp với kết quả sai `(suy luận)`. Tài liệu `docs/testing-and-dod.md` (được tham chiếu từ `AGENTS.md`) phải **cấm rõ hành vi mock nội bộ (internal module mocking)** và bắt buộc kiểm thử dựa trên hành vi đầu vào/đầu ra thực tế (Behavioral/Integration testing).
* **Tự động hóa DoD:** Hầu hết các mục trong Definition of Done cần được chuyển hóa thành CI checks để agent có thể tự chạy lệnh kiểm chứng trước khi mở PR `(suy luận)`.

---

## D8. Pull Request Template (`.github/pull_request_template.md`)

### 1. Các ứng viên
* **Google Engineering Practices — Writing Good CL Descriptions:**
  * **Nguồn:** Google Engineering Practices Documentation, `https://google.github.io/eng-practices/review/developer/cl-descriptions.html` (2019–2025).
  * **Mức độ phổ biến:** Bộ quy chuẩn code review có ảnh hưởng sâu rộng nhất trong ngành phần mềm.
  * **Ưu điểm:** Tập trung vào 2 câu hỏi cốt lõi: **What** (dòng đầu tiên viết ở thể mệnh lệnh + tóm tắt thay đổi) và **Why** (bối cảnh, vấn đề gốc rễ, tại sao chọn hướng giải quyết này mà không phải hướng khác).
  * **Nhược điểm:** Không cung cấp sẵn cú pháp Markdown checklist của GitHub.
* **GitHub Standard Pull Request Template:**
  * **Nguồn:** GitHub Docs, `https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository` (2020–2026).
  * **Mức độ phổ biến:** Cơ chế tích hợp nguyên bản trên hàng triệu repository GitHub/GitLab.
  * **Ưu điểm:** Tự động nạp nội dung file `.github/pull_request_template.md` vào khung soạn thảo mỗi khi tạo PR mới.
  * **Nhược điểm:** Nhiều mẫu cộng đồng chia sẻ trên mạng quá dài dòng (15–20 ô checkbox như *"Tôi đã tự review code"*, *"Code của tôi theo đúng style guide"*), biến thành thủ tục hành chính vô nghĩa.
* **Angular / Conventional Commits PR Guidelines:**
  * **Nguồn:** Conventional Commits (`https://www.conventionalcommits.org/en/v1.0.0/`, 2019–2025) và Angular Contributing Guide (`https://github.com/angular/angular/blob/main/contributing-docs/commit-message-guidelines.md`, 2025).
  * **Mức độ phổ biến:** Chuẩn công nghiệp để kết hợp PR title (khi dùng Squash and Merge) với việc sinh `CHANGELOG.md` và nâng phiên bản Semantic Versioning tự động.
  * **Ưu điểm:** Chuẩn hóa tiêu đề PR (`feat(scope): ...`, `fix(scope): ...`, `refactor!: ...`), giúp lịch sử `git log` cực kỳ sạch sẽ.
  * **Nhược điểm:** Chỉ giải quyết phần tiêu đề/cấu trúc commit, cần ghép với khung nội dung của Google CL description.

### 2. Chọn
* **Template nền khuyến nghị:** Kết hợp **Google CL Description (`What` & `Why`)** + **GitHub PR Template siêu gọn** + tiêu đề theo **Conventional Commits** tại `.github/pull_request_template.md`.
* **Lý do:** Với team 3–10 người review code hàng ngày (thường dùng chế độ *Squash and Merge* trên GitHub), nội dung PR chính là thông điệp commit vĩnh viễn trong lịch sử Git (`git blame`). Template phải ngắn để không gây lười biếng nhưng buộc người mở PR (hoặc AI agent) phải giải thích **Tại sao (Why)** và **Cách kiểm chứng (How to Verify)** (`https://google.github.io/eng-practices/review/developer/cl-descriptions.html`, 2025).

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc (4 mục):**
  1. `## Context & Why` (Giải thích bài toán cần giải quyết, nguyên nhân gốc rễ nếu là bug, và liên kết tới Issue/Spec `Closes #123`).
  2. `## Summary of Changes` (Gạch đầu dòng ngắn gọn những thay đổi chính về mặt kiến trúc/logic và các đánh đổi đáng chú ý cho reviewer).
  3. `## How Has This Been Tested / Verified?` (Bằng chứng kiểm thử: câu lệnh test đã chạy, kịch bản đã test tay trên local/preview, hoặc ảnh chụp/video nếu sửa UI).
  4. `## Rollout & Risk Notes` (Có DB migration không? Có biến môi trường `.env` mới không? Có thay đổi phá vỡ tương thích ngược hay cần bật feature flag không?).
* **Các mục tuỳ chọn (nên đặt trong HTML comment `<!-- ... -->` để ẩn đi nếu không dùng):**
  * `## AI Assistance Disclosure / Review Focus` (Ghi chú phần nào do AI agent sinh tự động và chỉ điểm cho human reviewer những file/dòng logic phức tạp cần soi kỹ nhất) `(suy luận)`.

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài file template:** **20–35 dòng Markdown** (bao gồm cả hướng dẫn ẩn trong thẻ `<!-- comment -->`).
* **Độ dài nội dung PR khi điền:** 100–300 từ (đọc lướt trong 30–60 giây).

### 5. Anti-pattern
* **Hội chứng "Tick-box Zombie" (Danh sách 15 ô checkbox thủ tục):** Khi PR template có một dãy dài `- [ ] Tôi đã chạy linter`, `- [ ] Tôi đã viết code sạch`, lập trình viên (và cả AI agent) sẽ đánh dấu `[x]` toàn bộ theo phản xạ tự động mà không thực sự làm, hoặc gõ `N/A` vào mọi ô (`https://google.github.io/eng-practices/review/developer/cl-descriptions.html`, 2025). Những gì kiểm tra được bằng máy (lint, build, test) phải chặn ở CI, không hỏi bằng checkbox trong PR `(suy luận)`.
* **Mô tả PR chỉ lặp lại `git diff` (What without Why):** Viết *"Sửa hàm `calculateTax` ở file `tax.ts`"* mà không giải thích tại sao công thức thuế cũ lại sai (`https://google.github.io/eng-practices/review/developer/cl-descriptions.html`, 2025).

### 6. Khác biệt khi có AI agent
* **Chống lại "Sương mù Văn xuôi AI" (AI-Generated PR Prose Slop):** Khi AI agent tự mở PR, nếu không bị giới hạn bởi template, nó thường liệt kê dài dòng từng file đã sửa (vốn dĩ hiển thị rõ trong tab *Files changed* của GitHub) bằng văn phong hoa mỹ nhưng lại giấu nhẹm các giả định rủi ro (assumptions/shortcuts) mà nó đã tự quyết định `(suy luận)`.
* **Bắt buộc mục "Reviewer Attention / Assumptions":** Khi có AI agent cùng làm việc, PR template nên hướng dẫn agent liệt kê rõ: (1) Các giả định (assumptions) mà agent đã tự đưa ra khi code, và (2) Top 1–3 điểm rủi ro nhất cần kỹ sư con người kiểm tra kỹ `(suy luận)`.

---

## D9. Runbook + Postmortem (`docs/ops/`)

### 1. Các ứng viên
* **Google SRE Postmortem Culture & Template:**
  * **Nguồn:** Betsy Beyer et al., *Site Reliability Engineering: How Google Runs Production Systems*, Chương 15 (Postmortem Culture: Learning from Failure) và Phụ lục D (`https://sre.google/sre-book/postmortem-culture/`, `https://sre.google/sre-book/example-postmortem/`, O'Reilly / Google, 2016–2025).
  * **Mức độ phổ biến:** Chuẩn vàng toàn cầu về văn hóa phân tích sự cố không đổ lỗi (**Blameless Postmortem**).
  * **Ưu điểm:** Cấu trúc rõ ràng (Summary, Impact, Root Causes, Trigger, Resolution, Detection, Action Items, Lessons Learned: What went well / What went wrong / Where we got lucky); đặt trọng tâm vào việc sửa lỗi hệ thống thay vì phạt cá nhân.
  * **Nhược điểm:** Bản mẫu gốc của Google có một số trường dữ liệu phù hợp với quy mô hạ tầng khổng lồ hơn là nhóm 3–10 người.
* **PagerDuty Incident Response & Postmortem Documentation (`PagerDuty/incident-response-docs`):**
  * **Nguồn:** PagerDuty, `https://response.pagerduty.com/` và `https://github.com/PagerDuty/incident-response-docs` (2017–2025).
  * **Mức độ phổ biến:** Hơn 3.200+ GitHub stars (`https://github.com/PagerDuty/incident-response-docs`, 2026), được hàng nghìn đội ngũ DevOps/On-call sử dụng làm khung phản ứng sự cố thực chiến.
  * **Ưu điểm:** Rất thực tế, kết hợp chặt chẽ giữa hướng dẫn xử lý khi đang cháy (Runbook/Incident Response) và quy trình mổ xẻ sau sự cố (Postmortem).
  * **Nhược điểm:** Phần phân vai Incident Commander / Scribe / Communications Liaison phức tạp đối với team chỉ có 3–5 người (nơi 1–2 kỹ sư thường kiêm nhiệm tất cả).
* **SkeltonThatcher Run Book Template (Dialogue Sheet) & AWS Well-Architected Runbooks:**
  * **Nguồn:** Matthew Skelton (đồng tác giả *Team Topologies*) & Nick Thatcher (`https://github.com/SkeltonThatcher/run-book-template`, 2015–2024) và AWS Well-Architected Operational Excellence Pillar (`https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/Substantiate-operations-with-runbooks-and-playbooks.html`, 2024).
  * **Mức độ phổ biến:** Kho `SkeltonThatcher/run-book-template` đạt hơn 1.400+ GitHub stars, là tài liệu tham chiếu chuẩn về vận hành hệ thống trong cộng đồng DevOps.
  * **Ưu điểm:** AWS phân biệt rõ **Playbook** (cách điều tra một triệu chứng chưa rõ nguyên nhân) và **Runbook** (các bước lệnh chuẩn hóa để thực hiện một thao tác vận hành hoặc khôi phục cụ thể).
  * **Nhược điểm:** Bản gốc của SkeltonThatcher bao phủ toàn bộ hồ sơ hệ thống (tài nguyên mạng, backup, SLA), dễ bị trùng lặp với `ARCHITECTURE.md` nếu không gọt bớt.
* **Etsy Debriefing Facilitation Guide:**
  * **Nguồn:** John Allspaw, Morgaineeth et al. (Etsy), `https://extfiles.etsy.com/DebriefingFacilitationGuide.pdf` (2016).
  * **Mức độ phổ biến:** Tài liệu nền tảng khai sinh phong trào Blameless Postmortem và tâm lý học an toàn trong vận hành phần mềm.
  * **Ưu điểm:** Cung cấp bộ câu hỏi đào sâu nhận thức luận (tại sao tại thời điểm sự cố, hành động đó lại có vẻ hợp lý với người trực?).
  * **Nhược điểm:** Thiên về kỹ năng điều phối cuộc họp hơn là template văn bản lưu trong Git.

### 2. Chọn
* **Template nền khuyến nghị:**
  1. **Runbook (`docs/ops/runbooks/<ten-tac-vu>.md`):** Áp dụng mẫu **Actionable Runbook của AWS/PagerDuty** (ngắn gọn, tập trung vào Triệu chứng -> Kiểm tra -> Lệnh xử lý -> Rollback).
  2. **Postmortem (`docs/ops/postmortems/YYYY-MM-DD-slug.md`):** Áp dụng mẫu **Google SRE Blameless Postmortem rút gọn**, kết hợp phương pháp truy tìm nguyên nhân hệ thống của **Etsy** (`https://sre.google/sre-book/example-postmortem/`, 2016).
* **Lý do:** Lúc 2 giờ sáng khi hệ thống sập, kỹ sư trực on-call của team 3–10 người chỉ cần các câu lệnh copy-paste chạy được ngay và an toàn (Runbook). Sau khi dập lửa xong, một file Postmortem 1 trang được review qua PR giúp cả nhóm (và AI agent) biến sự cố thành bài test/cảnh báo tự động để lỗi đó không bao giờ lặp lại `(suy luận)`.

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc cho Runbook (`docs/ops/runbooks/` — 4 mục):**
  1. `## Trigger / Alert & Impact` (Cảnh báo nào kích hoạt runbook này? Mức độ ảnh hưởng tới người dùng là gì?).
  2. `## Triage & Diagnostics` (Các câu lệnh CLI, câu truy vấn log/metrics hoặc link dashboard cụ thể để xác nhận nguyên nhân).
  3. `## Mitigation / Resolution Steps` (Các bước thực thi tuần tự kèm câu lệnh chính xác và kết quả mong đợi sau mỗi lệnh).
  4. `## Rollback & Escalation` (Nếu bước 3 thất bại hoặc làm tình hình tệ hơn thì chạy lệnh gì để hoàn tác? Liên hệ ai tiếp theo?).
* **Các mục bắt buộc cho Postmortem (`docs/ops/postmortems/` — 5 mục):**
  1. `## Incident Summary & Impact` (Thời gian bắt đầu/kết thúc theo UTC, thời gian gián đoạn dịch vụ, số lượng người dùng/request bị ảnh hưởng).
  2. `## Timeline (UTC)` (Dòng thời gian ngắn gọn: Lúc phát hiện -> Lúc chẩn đoán -> Lúc khắc phục tạm thời -> Lúc phục hồi hoàn toàn).
  3. `## Root Cause & Contributing Factors` (Giải thích kỹ thuật không đổ lỗi cá nhân: lỗi tiềm ẩn nào kết hợp với tác nhân kích hoạt nào đã gây ra sự cố, và tại sao hệ thống phòng vệ/test hiện tại lại để lọt?).
  4. `## Lessons Learned` (3 gạch đầu dòng chuẩn Google SRE: *What went well*, *What went wrong*, *Where we got lucky*).
  5. `## Action Items (Prevent / Detect / Mitigate)` (Danh sách việc cần làm có gắn người phụ trách, hạn chót và link Issue/PR cụ thể — ví dụ: thêm integration test, chỉnh ngưỡng alert).
* **Các mục tuỳ chọn:**
  * `## Customer Communication Log` (Bản tin trạng thái đã gửi cho khách hàng).

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài:** Runbook: **30–70 dòng Markdown** (mỗi runbook chỉ giải quyết 1 kịch bản cụ thể như *Database Connection Pool Exhausted*, *Rotate API Keys*, *Rollback Production*). Postmortem: **60–120 dòng Markdown** (chỉ bắt buộc viết cho sự cố mức độ nghiêm trọng SEV-1/SEV-2 gây gián đoạn người dùng thật).

### 5. Anti-pattern
* **Đổ lỗi cho "Lỗi con người" (Human Error as Root Cause):** Kết luận nguyên nhân gốc rễ là *"Kỹ sư A chạy nhầm lệnh"* và giải pháp là *"Nhắc nhở anh em cẩn thận hơn"*. Theo Google SRE (`https://sre.google/sre-book/postmortem-culture/`, 2016) và Etsy (`https://extfiles.etsy.com/DebriefingFacilitationGuide.pdf`, 2016), lỗi con người chỉ là triệu chứng của việc thiếu công cụ bảo vệ (guardrails) trong hệ thống.
* **Postmortem "Bỏ ngăn kéo" (Write-only Postmortems):** Viết báo cáo rất hay nhưng mục `Action Items` không gắn với ticket cụ thể hoặc không bao giờ được ưu tiên làm trong Sprint kế tiếp (`https://sre.google/sre-book/postmortem-culture/`, 2016).
* **Runbook văn xuôi mơ hồ:** Viết *"Hãy kiểm tra xem hàng đợi Kafka có bị nghẽn không"* mà không ghi rõ câu lệnh CLI hay đường dẫn dashboard để kiểm tra `(suy luận)`.

### 6. Khác biệt khi có AI agent
* **AI Agent đóng vai trò Trợ lý Điều tra Sự cố (AI SRE / Triage Assistant):** Khi lưu Runbook và lịch sử Postmortem ngay trong repo (`docs/ops/`), lúc xảy ra sự cố, kỹ sư có thể cho AI agent đọc `docs/ops/runbooks/` và `docs/ops/postmortems/` kết hợp với MCP đọc log/metrics để chẩn đoán nhanh xem sự cố hiện tại có giống với ca nào trong quá khứ không `(suy luận)`.
* **Biến Postmortem thành Quy tắc Phòng vệ cho Agent:** Một bước bắt buộc mới trong mục `Action Items` của Postmortem thời đại AI là: *"Cập nhật bài học hoặc ràng buộc mới vào `AGENTS.md` / `ARCHITECTURE.md` / bộ test tự động"* để ngăn AI coding agent tái tạo lại mẫu lỗi tương tự trong tương lai `(suy luận)`.

---

## D10. Chính sách bảo mật + sử dụng AI agent (`SECURITY.md` & Quy tắc AI)

### 1. Các ứng viên
* **GitHub Standard `SECURITY.md` + RFC 9116 (`security.txt`):**
  * **Nguồn:** GitHub Docs (`https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository`, 2020–2026) và IETF RFC 9116 — *A File Format to Aid in Security Vulnerability Disclosure* (`https://www.rfc-editor.org/rfc/rfc9116.html`, 2022).
  * **Mức độ phổ biến:** Chuẩn bắt buộc trong bảng điểm bảo mật OpenSSF Scorecard (`https://securityscorecards.dev/`, 2025) và tab *Security* của mọi repository trên GitHub.
  * **Ưu điểm:** Ngắn gọn, hiển thị tự động khi người dùng định báo lỗi bảo mật trên GitHub, chuẩn hóa kênh liên lạc riêng tư.
  * **Nhược điểm:** Bản gốc chỉ tập trung vào việc tiếp nhận báo cáo lỗ hổng từ bên ngoài (Vulnerability Disclosure), chưa bao gồm các quy tắc bảo mật nội bộ cho đội ngũ kỹ sư và AI coding agent.
* **OWASP Top 10 for Agentic Applications (2026) & OWASP Top 10 for LLM Applications (2025):**
  * **Nguồn:** OWASP GenAI Security Project, `https://genai.owasp.org/` và bản phát hành *OWASP Top 10 for Agentic Applications* (`https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/`, cuối 2025–2026).
  * **Mức độ phổ biến:** Khung tham chiếu bảo mật AI và Agentic AI uy tín nhất toàn cầu hiện nay.
  * **Ưu điểm:** Định danh chính xác 10 rủi ro đặc thù khi dùng AI agent (ASI01: Agent Goal Hijack / Prompt Injection qua dữ liệu ngoài; ASI02: Tool Misuse; ASI03: Identity & Privilege Abuse; ASI04: Agentic Supply Chain / MCP vulnerabilities; ASI05: Unexpected Code Execution; ASI06: Memory/Context Poisoning; ASI09: Human-Agent Trust Exploitation).
  * **Nhược điểm:** Là khung phân tích rủi ro tổng thể, cần được chuyển hóa thành các quy tắc ngắn gọn cấp độ repository.
* **Linux Foundation Generative AI Policy & OpenSSF AI Code Guidelines:**
  * **Nguồn:** Linux Foundation (`https://www.linuxfoundation.org/legal/generative-ai`, 2023–2025) và OpenSSF Best Practices Working Group — *Security-Focused Guide for AI Code Assistant Instructions* (`https://best.openssf.org/`, 2024–2025).
  * **Mức độ phổ biến:** Chuẩn pháp lý và trách nhiệm giải trình (accountability) được áp dụng trên hàng trăm dự án hạ tầng trọng yếu (Linux Kernel, CNCF, AAIF).
  * **Ưu điểm:** Khẳng định nguyên tắc cốt lõi: **AI agent không có tư cách pháp nhân để ký Developer Certificate of Origin (DCO) hay chịu trách nhiệm khi đẩy code lỗi; con người đứng tên mở/duyệt PR chịu trách nhiệm 100%** (`https://www.linuxfoundation.org/legal/generative-ai`, 2024).

### 2. Chọn
* **Template nền khuyến nghị:** Duy trì **1 file `SECURITY.md` tại thư mục gốc** tích hợp 3 phần gọn nhẹ: (1) **Vulnerability Disclosure** (theo chuẩn GitHub/RFC 9116), (2) **Engineering Security Baseline** (quản lý secrets, dependencies), và (3) **AI Agent Usage & Security Policy** (chắt lọc từ OWASP Agentic Top 10 và Linux Foundation AI Policy).
* **Lý do:** Với team 3–10 người, tách riêng `SECURITY.md` và `AI_POLICY.md` là không cần thiết. Gộp chung vào `SECURITY.md` (và trích xuất các lệnh cấm thực thi sang mục `Hard Boundaries` của `AGENTS.md`) giúp quản lý tập trung mọi rủi ro bảo mật của cả người lẫn máy `(suy luận)`.

### 3. Các mục bắt buộc và mục tuỳ chọn
* **Các mục bắt buộc trong `SECURITY.md` (5 mục):**
  1. `## 1. Reporting a Vulnerability` (Kênh báo cáo lỗ hổng bảo mật riêng tư, email liên hệ, SLA phản hồi dự kiến).
  2. `## 2. Secrets & Data Handling Rules` (Cấm tuyệt đối việc commit API keys, `.env`, dữ liệu PII/production dump vào Git hoặc dán vào cửa sổ chat của AI/LLM chưa được cấp phép).
  3. `## 3. AI Agent Permission & Tool Guardrails (OWASP Agentic Baseline)` (Quy định nguyên tắc đặc quyền tối thiểu [Least Privilege]: AI agent chỉ được chạy trên môi trường sandbox/local/staging; cấm cấp quyền ghi DB production hoặc AWS/GCP admin credentials cho agent; chỉ sử dụng các MCP server đã được team phê duyệt trong repo để tránh rủi ro chuỗi cung ứng ASI04).
  4. `## 4. Human-in-the-Loop & Code Review Accountability` (Quy tắc trách nhiệm giải trình theo Linux Foundation: Mọi dòng code do AI agent sinh ra phải có ít nhất 1 kỹ sư con người hiểu rõ, chịu trách nhiệm đứng tên và được review độc lập trước khi merge vào `main`; cấm merge PR mà người mở không giải thích được logic bên trong).
  5. `## 5. Dependency & Slopsquatting Protection` (Bắt buộc kiểm tra sự tồn tại thực tế, giấy phép bản quyền và độ uy tín của mọi thư viện mới trước khi cài đặt — phòng chống việc AI ảo giác tên gói phần mềm dẫn đến tấn công *slopsquatting* / *package hallucination*).
* **Các mục tuỳ chọn:**
  * `## Supported Versions` (Nếu dự án là thư viện hoặc phần mềm phát hành nhiều phiên bản).
  * File `/.well-known/security.txt` theo chuẩn RFC 9116 cho ứng dụng web public.

### 4. Độ dài / mức chi tiết hợp lý
* **Độ dài:** **70–120 dòng Markdown** (400–700 từ).

### 5. Anti-pattern
* **Chính sách AI dạng văn bản pháp lý dài 10 trang trên Notion/Confluence:** Không một kỹ sư nào mở ra đọc khi đang code, và AI agent trong repo cũng không hề biết đến sự tồn tại của nó `(suy luận)`.
* **Tin tưởng mù quáng vào kết quả của AI Agent (Human-Agent Trust Exploitation – OWASP ASI09):** Duyệt các PR lớn hàng nghìn dòng do AI agent sinh ra chỉ vì thấy bài test xanh và mô tả PR viết mượt mà (`https://genai.owasp.org/`, 2026).
* **Cho phép AI Agent tự ý cài đặt package mới hoặc kết nối MCP server bên thứ ba không kiểm duyệt:** Mở cửa cho tấn công chuỗi cung ứng và đánh cắp biến môi trường local qua prompt injection gián tiếp (Indirect Prompt Injection – OWASP ASI01 & ASI04, `https://genai.owasp.org/`, 2026).

### 6. Khác biệt khi có AI agent
* **Thực thi chính sách bằng Cấu hình Máy (Policy-as-Code) song hành với Văn bản:** Một chính sách viết trong `SECURITY.md` chỉ dành cho con người nếu không được ánh xạ sang cấu hình kỹ thuật (như danh sách `deny` commands/paths trong `.claude/settings.json`, Cursor rules, hoặc mục `## Hard Boundaries` trong `AGENTS.md`). Team cần đồng bộ các lệnh cấm trong `SECURITY.md` trực tiếp vào cấu hình quyền của AI agent `(suy luận)`.

---

## D11. Tài liệu nào team nhỏ THƯỜNG THIẾU mà nên có? Loại nào trong D1–D10 KHÔNG đáng làm riêng?

### 1. Hai loại tài liệu team 3–10 người THƯỜNG THIẾU nhưng mang lại giá trị cực cao (Nên bổ sung)

#### A. Từ điển Thuật ngữ Nghiệp vụ — Domain Glossary / Ubiquitous Language (`docs/glossary.md` hoặc gộp vào `ARCHITECTURE.md`)
* **Cơ sở & Nguồn:** Khái niệm **Ubiquitous Language (Ngôn ngữ Chung)** của Eric Evans trong *Domain-Driven Design: Tackling Complexity in the Heart of Software* (Addison-Wesley, 2003; tóm tắt bởi Martin Fowler tại `https://martinfowler.com/bliki/UbiquitousLanguage.html`, 2006).
* **Tại sao team nhỏ thường thiếu nhưng lại cấp thiết khi có AI agent:**
  * Trong các nhóm 3–10 người, kiến thức nghiệp vụ thường truyền miệng. Kết quả là cùng một thực thể khách hàng nhưng trong DB gọi là `account`, ở Backend gọi là `organization`, ở Frontend gọi là `workspace`, còn trong tài liệu sản phẩm gọi là `tenant`.
  * Khi có AI coding agent, sự thiếu nhất quán về từ vựng này là thảm họa: mỗi lần agent viết một tính năng mới, nó lại đoán mò hoặc đẻ thêm một thuật ngữ đồng nghĩa mới làm ô nhiễm mô hình miền (domain model) `(suy luận)`.
* **Cách làm tối thiểu:** Một bảng ngắn **30–60 dòng** (đặt trong `ARCHITECTURE.md` hoặc `docs/glossary.md`) định nghĩa chính xác 10–25 thuật ngữ cốt lõi của sản phẩm, tên thực thể tương ứng trong code, và **các từ đồng nghĩa bị cấm dùng (Deprecated/Forbidden Synonyms)**.

#### B. Nhật ký Thay đổi & Hướng dẫn Nâng cấp — Changelog (`CHANGELOG.md`)
* **Cơ sở & Nguồn:** Chuẩn **Keep a Changelog v1.1.0** của Olivier Lacan (`https://keepachangelog.com/en/1.1.0/`, 2023) kết hợp với công cụ tự động hóa như Release Please (`https://github.com/googleapis/release-please`, 2025) hoặc Changesets (`https://github.com/changesets/changesets`, 2025).
* **Tại sao nên có:** Giúp cả team, bộ phận vận hành/khách hàng và chính AI agent biết ngay những thay đổi lớn (`Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`), đặc biệt là các thay đổi cấu hình `.env` hoặc DB migration giữa các bản phát hành mà không phải đọc ngược hàng trăm dòng `git log`.

### 2. Loại tài liệu nào trong D1–D10 KHÔNG đáng làm thành file/quy trình nặng nề riêng biệt cho team 3–10 người?

Với quy mô 3–10 kỹ sư, mục tiêu tối thượng là **tránh "Thuế Bảo trì Tài liệu" (Documentation Maintenance Tax)**. Có **3 hạng mục trong D1–D10 không nên làm theo kiểu truyền thống tách rời** mà phải cắt bỏ hoặc gộp lại `(suy luận)`:

1. **KHÔNG viết tài liệu API thủ công bằng Markdown (trong D5):**
   * Tuyệt đối không duy trì các trang Markdown liệt kê từng endpoint, request/response body bằng tay. Hãy để code (Zod/TypeBox/Pydantic/FastAPI/NestJS) tự sinh ra `openapi.yaml`, và chỉ duy trì đúng 1 trang ngắn `docs/api-guidelines.md` (100–150 dòng) cho các quy ước thiết kế chung.
2. **KHÔNG viết tài liệu Test Strategy dài hàng chục trang kiểu IEEE 829 hay arc42 đầy đủ 12 mục (trong D3 & D7):**
   * Các bản mẫu Test Strategy doanh nghiệp truyền thống (gồm phân tích rủi ro vĩ mô, ma trận phân quyền QA, lịch trình kiểm thử) hoàn toàn vô dụng với team 3–10 người làm CI/CD liên tục. Hãy gộp gọn phần phân tầng test (Small/Medium/Large + không mock nội bộ) và Definition of Done vào đúng 1 trang `docs/testing-and-dod.md` (~100 dòng). Tương tự, bỏ qua arc42 12 mục để dùng `ARCHITECTURE.md` 1 file của Matklad.
3. **KHÔNG tách rời `SECURITY.md` và `AI_USAGE_POLICY.md`, cũng KHÔNG viết Spec (D6) cho mọi task nhỏ:**
   * Gộp chính sách AI trực tiếp vào `SECURITY.md` (về mặt trách nhiệm/bảo mật) và `AGENTS.md` (về mặt ranh giới kỹ thuật).
   * Với **D6 (Feature Spec)**, không bắt buộc viết spec cho các task/bugfix nhỏ dưới 1–2 ngày công. Hơn nữa, một khi tính năng lớn đã triển khai xong, coi file Spec trong `docs/specs/` là **hồ sơ lịch sử tĩnh (immutable point-in-time record)** — không tốn công cập nhật lại Spec cũ khi yêu cầu thay đổi sau này, mà cập nhật vào `ARCHITECTURE.md` hoặc tạo `ADR` mới.

---

## Top 10 kết luận

1. **Cấu trúc tối giản 8 file/thư mục cốt lõi:** Một team 3–10 người chỉ cần duy trì bộ khung: `README.md`, `AGENTS.md` (kèm symlink `CLAUDE.md`), `ARCHITECTURE.md`, `SECURITY.md`, `.github/pull_request_template.md`, `docs/testing-and-dod.md`, và 3 thư mục lưu trữ theo sự kiện (`docs/adr/`, `docs/specs/`, `docs/ops/`).
2. **`AGENTS.md` là chuẩn mở trung tâm nhưng phải cực kỳ tinh gọn (<150 dòng):** Nghiên cứu thực nghiệm năm 2026 (`https://arxiv.org/abs/2602.11988`) chứng minh file hướng dẫn AI dài dòng hoặc do LLM tự sinh làm giảm tỷ lệ hoàn thành task và tăng hơn 20% chi phí token; chỉ nên ghi các câu lệnh thực thi và những quy ước đặc thù theo nguyên tắc *"Mistake Test"*.
3. **Tách biệt rõ "Tài liệu sống" (Living Docs) và "Hồ sơ theo thời điểm" (Point-in-time Artifacts):** `README.md`, `AGENTS.md`, `ARCHITECTURE.md`, `docs/api-guidelines.md` phải được cập nhật liên tục; ngược lại, `ADR`, `Feature Spec`, và `Postmortem` là các bản ghi lịch sử gắn với thời điểm ra quyết định — không sửa đè mà chỉ tạo bản mới thay thế.
4. **Kiến trúc tổng quan theo phong cách Matklad + Mermaid C4:** Đặt 1 file `ARCHITECTURE.md` duy nhất ở gốc dự án tập trung vào **Code Map (bản đồ thư mục)**, **2 sơ đồ Mermaid C4 (Context & Container)** và **Architectural Invariants (các quy tắc bất biến)** để cả người và AI agent định vị codebase tức thì (`https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html`, 2021).
5. **Ghi nhận quyết định bằng MADR rút gọn để bảo vệ "Hàng rào Chesterton":** Lưu `docs/adr/NNNN-*.md` có mục `Considered Options` giúp ngăn chặn AI coding agent vô tình "refactor" hoặc xóa bỏ các giải pháp đánh đổi có chủ đích của team (`https://adr.github.io/madr/`, 2024).
6. **Hợp đồng API phải do máy đọc và tự động kiểm tra:** Dùng `openapi.yaml` (OpenAPI 3.1) làm nguồn chân lý cho dữ liệu endpoint và 1 trang `docs/api-guidelines.md` (dựa trên Zalando Guidelines + RFC 9457 Problem Details) để chuẩn hóa cách đặt tên, phân trang và trả lỗi.
7. **Spec-Driven Development (SDD) thực dụng trong 1 file duy nhất cho tính năng lớn:** Tránh tạo 4–5 file rườm rà cho một tính năng (`https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html`, 2025); hãy dùng 1 file `docs/specs/YYYY-MM-DD-slug.md` gộp chung *Goals/Non-Goals*, *Technical Design*, *Acceptance Criteria* và *Phased Tasks* cho các tính năng từ 2 ngày công trở lên.
8. **Chiến lược kiểm thử khóa chặt hành vi gian lận của AI Agent:** Kết hợp Google Test Sizes (Small/Medium/Large) và Testing Trophy, trong đó quy định rõ việc **cấm mock nội bộ (internal module mocking)** để ngăn AI agent viết các bài test giả tạo chỉ nhằm vượt qua CI (`https://abseil.io/resources/swe-book/html/ch11.html`, 2020).
9. **PR Template ưu tiên giải thích "Why" và chỉ điểm rủi ro của AI:** Loại bỏ các danh sách checkbox hình thức; dùng cấu trúc Google CL Description để buộc người mở PR và AI agent giải thích bối cảnh, các giả định đã tự đưa ra và những vùng code nhạy cảm cần con người soi kỹ (`https://google.github.io/eng-practices/review/developer/cl-descriptions.html`, 2025).
10. **Mọi sự cố vận hành và rủi ro bảo mật phải khép kín thành quy tắc cho Agent:** Từ Blameless Postmortem (Google SRE) đến chính sách bảo mật (OWASP Agentic Top 10, Linux Foundation DCO), mọi bài học rút ra đều phải được chuyển hóa thành test tự động, linter rule, hoặc ranh giới cấm trong `AGENTS.md`.

---

## Bảng chọn cuối

| Loại | Template nền chọn | 3–6 mục bắt buộc | Độ dài |
| :--- | :--- | :--- | :--- |
| **D1. README dự án (`README.md`)** | **Make a README** + cấu trúc cốt lõi **Standard Readme** (3 trụ cột *What – Why – How* của Prana et al., 2019) | 1. Tên & Mô tả dự án (What/Why)<br>2. Tech Stack & Prerequisites<br>3. Quickstart / Local Setup<br>4. Verification & Testing<br>5. Documentation Map (Links) | 80–150 dòng (400–800 từ) |
| **D2. Hướng dẫn AI Agent (`AGENTS.md` + `CLAUDE.md`)** | **AGENTS.md** (Linux Foundation AAIF) làm gốc + `CLAUDE.md` nhúng `@AGENTS.md` theo **Anthropic Best Practices** | 1. Commands (Build/Test/Lint từng file)<br>2. Architecture & Directory Map<br>3. Non-Obvious Code Conventions<br>4. Verification & Workflow Rules<br>5. Hard Boundaries / Do Not Touch | 60–150 dòng (tối đa <200 dòng) |
| **D3. Kiến trúc tổng quan (`ARCHITECTURE.md`)** | **Matklad's `ARCHITECTURE.md`** + **Mermaid C4 (Level 1 & 2)** + **arc42** Cross-cutting concepts rút gọn | 1. Bird's-Eye View (System Context)<br>2. Containers & Topology (Mermaid)<br>3. Code Map (Directory & Entry points)<br>4. Core Data Flow / Runtime Scenarios<br>5. Architectural Invariants & Boundaries | 150–300 dòng (1.000–1.800 từ) |
| **D4. Quyết định kiến trúc (`docs/adr/NNNN-*.md`)** | **MADR Bare-Minimal** (Nygard + Considered Options) mở đầu Decision bằng **Y-Statement** | 1. Title + Metadata (Status, Date)<br>2. Context & Problem Statement<br>3. Considered Options (Pros/Cons)<br>4. Decision Outcome (Y-statement)<br>5. Consequences | 40–100 dòng / ADR (300–600 từ) |
| **D5. API Contract & Quy ước (`openapi.yaml` + `docs/api-guidelines.md`)** | **OpenAPI 3.1** (sinh/kiểm từ code) + 1 trang tóm tắt **Zalando RESTful Guidelines** & **RFC 9457** | 1. URL & Naming Conventions<br>2. HTTP Methods & Status Codes<br>3. Error Format (RFC 9457)<br>4. Pagination, Filtering & Sorting<br>5. Idempotency & Versioning Policy | Guidelines: 100–180 dòng; OpenAPI: tự động theo code |
| **D6. Spec / Design Doc cho Feature (`docs/specs/`)** | Lai ghép **Google Design Doc** (Malte Ubl) + **Spec-Driven Development (SDD)** trong 1 file duy nhất | 1. Context & Problem Statement<br>2. Goals & Non-Goals<br>3. Proposed Technical Design<br>4. Edge Cases, Security & Failure Modes<br>5. Acceptance Criteria & Test Cases<br>6. Phased Implementation Plan (Checklist) | 100–250 dòng / spec (chỉ làm cho feature ≥ 2 ngày) |
| **D7. Test Strategy + DoD (`docs/testing-and-dod.md`)** | **Google Test Sizes** (Small/Medium/Large) + **Testing Trophy** (Kent C. Dodds) + **Scrum/GitLab DoD** | 1. Test Tiers & Resource Rules<br>2. Mocking Policy (No internal mocks)<br>3. Flaky Test & Coverage Policy<br>4. Definition of Done Checklist<br>5. Local Test Execution Commands | 80–140 dòng (500–800 từ) |
| **D8. Pull Request Template (`.github/pull_request_template.md`)** | **Google Eng-Practices CL Description** + **GitHub PR Template** + **Conventional Commits** title | 1. Context & Why (kèm Issue link)<br>2. Summary of Changes & Trade-offs<br>3. How Has This Been Verified?<br>4. Rollout, Migration & Risk Notes | Template: 20–35 dòng; Nội dung điền: 100–300 từ |
| **D9. Runbook + Postmortem (`docs/ops/`)** | **AWS/PagerDuty Actionable Runbook** + **Google SRE Blameless Postmortem** (kết hợp tư duy **Etsy**) | *Runbook:* 1. Trigger/Impact, 2. Diagnostics, 3. Mitigation Steps, 4. Rollback.<br>*Postmortem:* 1. Summary, 2. Timeline (UTC), 3. Root Cause, 4. Lessons Learned, 5. Action Items. | Runbook: 30–70 dòng;<br>Postmortem: 60–120 dòng |
| **D10. Bảo mật + Chính sách AI (`SECURITY.md`)** | **GitHub `SECURITY.md`** (RFC 9116) + **OWASP Top 10 for Agentic Applications (2026)** + **Linux Foundation AI Policy** | 1. Reporting a Vulnerability<br>2. Secrets & Data Handling Rules<br>3. AI Agent Permission Guardrails<br>4. Human Review & Accountability (DCO)<br>5. Dependency & Slopsquatting Check | 70–120 dòng (400–700 từ) |
| **D11. Bổ sung khuyến nghị (`docs/glossary.md` & `CHANGELOG.md`)** | **DDD Ubiquitous Language Glossary** (Eric Evans / Martin Fowler) + **Keep a Changelog v1.1.0** | *Glossary:* 1. Core Domain Terms, 2. Code Entity Mapping, 3. Forbidden Synonyms.<br>*Changelog:* Unreleased / Versioned (`Added`, `Changed`, `Fixed`, `Security`). | Glossary: 30–60 dòng;<br>Changelog: tự động qua PR |

---

## Điều chưa chắc

1. **Sự hội tụ của các định dạng Rule phân mảnh theo đường dẫn (Path-scoped Agent Rules):** Mặc dù `AGENTS.md` ở thư mục gốc và thư mục con đã trở thành chuẩn mở thuộc Linux Foundation (`https://agents.md/`, 2025), cơ chế gắn rule theo glob pattern (như `.cursor/rules/*.mdc` dùng `globs` hay `.github/instructions/*.instructions.md` dùng `applyTo`) vẫn chưa được chuẩn hóa thống nhất giữa các nhà cung cấp tính đến tháng 10/2026. Team dùng hỗn hợp nhiều IDE vẫn phải ưu tiên đặt nested `AGENTS.md` theo thư mục thay vì phụ thuộc sâu vào glob frontmatter của riêng một hãng.
2. **Ngưỡng điểm gãy của Spec-Driven Development (SDD) theo tốc độ cải tiến của Frontier Models:** Các bộ công cụ SDD như GitHub `spec-kit` hay AWS Kiro sinh ra nhiều tạo phẩm Markdown trung gian đang bị một bộ phận kỹ sư đánh giá là tạo ra ma sát không cần thiết cho các tác vụ nhỏ (`https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html`, 2025). Chưa có nghiên cứu định lượng quy mô lớn nào xác định chính xác ngưỡng độ phức tạp (tính theo LOC hoặc số file bị chạm) mà tại đó việc viết một file Spec đầy đủ tiết kiệm tổng thời gian hơn so với chế độ lập kế hoạch tương tác trực tiếp trong phiên (in-session plan mode) của agent.
3. **Độ trôi của tài liệu (Documentation Drift) khi AI Agent tự sửa code hàng loạt:** Khi tốc độ thay đổi code tăng gấp 3–5 lần nhờ AI agent, ngay cả các tài liệu gọn nhẹ như `ARCHITECTURE.md` cũng có nguy cơ lệch khỏi thực tế nhanh hơn trước nếu team không thiết lập cơ chế kiểm tra tự động trong CI (ví dụ: script kiểm tra các đường dẫn thư mục được nhắc tới trong `AGENTS.md` và `ARCHITECTURE.md` có còn tồn tại thật trong repo hay không).

---

## Nguồn

1. **Prana, G. A. A., Treude, C., Thung, F., Atapattu, T., & Lo, D. (2019).** *Categorizing the Content of GitHub README Files*. Empirical Software Engineering (Springer) / arXiv preprint. URL: `https://arxiv.org/abs/1811.06959` (2018/2019).
2. **Guo, D. (2024).** *Make a README*. URL: `https://www.makeareadme.com/` và `https://github.com/dguo/makeareadme` (2018–2024).
3. **Littauer, R. (2026).** *Standard Readme Specification*. URL: `https://github.com/RichardLitt/standard-readme` (2016–2026).
4. **Drew, O. (2026).** *Best-README-Template*. URL: `https://github.com/othneildrew/Best-README-Template` (2019–2026).
5. **GitHub Docs (2024).** *About READMEs*. URL: `https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes` (2024).
6. **Agentic AI Foundation / OpenAI et al. (2025–2026).** *AGENTS.md — A simple, open format for guiding coding agents*. URL: `https://agents.md/` và `https://github.com/agentsmd/agents.md` (2025–2026).
7. **Linux Foundation (2025).** *Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF)*. URL: `https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation` (2025).
8. **Anthropic (2025–2026).** *Claude Code Documentation: Manage Claude's memory (`CLAUDE.md`) & Best Practices*. URL: `https://docs.anthropic.com/en/docs/claude-code/memory` và `https://code.claude.com/docs/en/best-practices` (2025–2026).
9. **GitHub Docs (2025–2026).** *Adding repository custom instructions for GitHub Copilot*. URL: `https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot` (2025–2026).
10. **Cursor Documentation (2025–2026).** *Rules for AI (`.cursor/rules`)*. URL: `https://docs.cursor.com/context/rules` (2025–2026).
11. **ETH Zurich & LogicStar AI (2026).** *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?*. arXiv:2602.11988. URL: `https://arxiv.org/abs/2602.11988` (2026).
12. **Kladov, A. / matklad (2021).** *ARCHITECTURE.md*. URL: `https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html` và `https://github.com/matklad/awesome-architecture.md` (2021–2025).
13. **Brown, S. (2024–2025).** *The C4 model for visualising software architecture*. URL: `https://c4model.com/` (2018–2025).
14. **Mermaid.js (2025).** *C4 Diagram Syntax in Mermaid*. URL: `https://mermaid.js.org/syntax/c4.html` (2023–2025).
15. **Starke, G., & Hruschka, P. (2025).** *arc42 — Template for documentation of software and system architecture*. URL: `https://arc42.org/` và `https://github.com/arc42/arc42-template` (2012–2025).
16. **Nygard, M. (2011).** *Documenting Architecture Decisions*. Cognitect Blog. URL: `https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions` (2011).
17. **Henderson, J. P. (2026).** *Architecture Decision Record (ADR) GitHub Repository*. URL: `https://github.com/joelparkerhenderson/architecture-decision-record` (2016–2026).
18. **Kopp, O., Zimmermann, O., et al. (2025–2026).** *Markdown Architectural Decision Records (MADR)*. URL: `https://adr.github.io/madr/` và `https://github.com/adr/madr` (2017–2026).
19. **Zimmermann, O. (2020).** *Architectural Decision Making and Y-Statements*. URL: `https://ozimmer.ch/practices/2020/04/27/ArchitectureDecisionMaking.html` (2020).
20. **OpenAPI Initiative (2021–2026).** *OpenAPI Specification v3.1.0*. URL: `https://spec.openapis.org/oas/v3.1.0` và `https://github.com/OAI/OpenAPI-Specification` (2021–2026).
21. **Zalando SE (2025–2026).** *Zalando RESTful API and Event Guidelines*. URL: `https://opensource.zalando.com/restful-api-guidelines/` và `https://github.com/zalando/restful-api-guidelines` (2016–2026).
22. **Nottingham, M., Wilde, E., & Dalal, S. (2023).** *RFC 9457: Problem Details for HTTP APIs* (Obsoletes RFC 7807). IETF. URL: `https://www.rfc-editor.org/rfc/rfc9457.html` (2023).
23. **Google (2025–2026).** *Google API Improvement Proposals (AIP)*. URL: `https://google.aip.dev/` (2019–2026).
24. **AsyncAPI Initiative (2025–2026).** *AsyncAPI Specification*. URL: `https://www.asyncapi.com/` và `https://github.com/asyncapi/spec` (2017–2026).
25. **Stoplight (2025).** *Spectral — JSON/YAML OpenAPI Linter*. URL: `https://github.com/stoplightio/spectral` (2019–2025).
26. **Ubl, M. (2020).** *Design Docs at Google*. Industrial Empathy. URL: `https://www.industrialempathy.com/posts/design-docs-at-google/` (2020).
27. **GitHub (2025–2026).** *Spec Kit — Spec-Driven Development Toolkit*. URL: `https://github.com/github/spec-kit` và `https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/` (2025–2026).
28. **Böckeler, B. / MartinFowler.com (2025).** *Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl*. URL: `https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html` (2025).
29. **Rust Project (2025).** *Rust RFC 0000-template.md*. URL: `https://github.com/rust-lang/rfcs/blob/master/0000-template.md` (2014–2025).
30. **Kubernetes SIG Architecture (2025).** *Kubernetes Enhancement Proposal (KEP) Process*. URL: `https://github.com/kubernetes/enhancements/blob/master/keps/sig-architecture/0000-kep-process/README.md` (2018–2025).
31. **Winters, T., Manshreck, T., & Wright, H. (2020).** *Software Engineering at Google: Lessons Learned from Programming Over Time* (Chapters 11–14: Testing). O'Reilly Media / Abseil. URL: `https://abseil.io/resources/swe-book/html/ch11.html` và `https://abseil.io/resources/swe-book/html/ch13.html` (2020).
32. **Dodds, K. C. (2018).** *The Testing Trophy and Testing Classifications*. URL: `https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications` (2018).
33. **Vocke, H. / MartinFowler.com (2018).** *The Practical Test Pyramid*. URL: `https://martinfowler.com/articles/practical-test-pyramid.html` (2018).
34. **Fowler, M. (2012).** *TestCoverage*. URL: `https://martinfowler.com/bliki/TestCoverage.html` (2012).
35. **Schwaber, K., & Sutherland, J. (2020).** *The 2020 Scrum Guide*. URL: `https://scrumguides.org/scrum-guide.html` (2020).
36. **GitLab (2025).** *GitLab Engineering Handbook — Testing Standards*. URL: `https://handbook.gitlab.com/handbook/engineering/testing/` (2025).
37. **Google (2025).** *Google Engineering Practices Documentation — Writing good CL descriptions*. URL: `https://google.github.io/eng-practices/review/developer/cl-descriptions.html` (2019–2025).
38. **GitHub Docs (2025).** *Creating a pull request template for your repository*. URL: `https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository` (2025).
39. **Conventional Commits (2025).** *Conventional Commits v1.0.0*. URL: `https://www.conventionalcommits.org/en/v1.0.0/` (2019–2025).
40. **Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (2016).** *Site Reliability Engineering: How Google Runs Production Systems* (Chapter 15: Postmortem Culture & Appendix D: Example Postmortem). Google / O'Reilly. URL: `https://sre.google/sre-book/postmortem-culture/` và `https://sre.google/sre-book/example-postmortem/` (2016).
41. **PagerDuty (2025–2026).** *PagerDuty Incident Response Documentation*. URL: `https://response.pagerduty.com/` và `https://github.com/PagerDuty/incident-response-docs` (2017–2026).
42. **Skelton, M., & Thatcher, N. (2024).** *Run Book Template (Dialogue Sheet)*. URL: `https://github.com/SkeltonThatcher/run-book-template` (2015–2024).
43. **AWS (2024).** *AWS Well-Architected Framework — Operational Excellence Pillar: Runbooks and Playbooks*. URL: `https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/Substantiate-operations-with-runbooks-and-playbooks.html` (2024).
44. **Allspaw, J., et al. / Etsy (2016).** *Etsy Debriefing Facilitation Guide for Blameless Postmortems*. URL: `https://extfiles.etsy.com/DebriefingFacilitationGuide.pdf` (2016).
45. **GitHub Docs (2025).** *Adding a security policy to your repository (`SECURITY.md`)*. URL: `https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository` (2025).
46. **Foudil, E., & Shafranovich, Y. (2022).** *RFC 9116: A File Format to Aid in Security Vulnerability Disclosure (`security.txt`)*. IETF. URL: `https://www.rfc-editor.org/rfc/rfc9116.html` (2022).
47. **OWASP GenAI Security Project (2025–2026).** *OWASP Top 10 for Agentic Applications & LLM Applications*. URL: `https://genai.owasp.org/` và `https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/` (2025–2026).
48. **Linux Foundation (2024–2025).** *Generative AI Policy and Developer Certificate of Origin (DCO) Guidance*. URL: `https://www.linuxfoundation.org/legal/generative-ai` (2024–2025).
49. **Fowler, M., & Evans, E. (2006).** *Ubiquitous Language (Domain-Driven Design)*. URL: `https://martinfowler.com/bliki/UbiquitousLanguage.html` (2006).
50. **Lacan, O. (2023).** *Keep a Changelog v1.1.0*. URL: `https://keepachangelog.com/en/1.1.0/` (2023).

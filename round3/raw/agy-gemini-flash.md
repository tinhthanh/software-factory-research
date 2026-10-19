## D1. README dự án

### 1. Các ứng viên
*   **Ứng viên A: Standard Readme**
    *   *Nguồn:* Dự án mã nguồn mở do Richard Littauer khởi xướng (2016) tại [github.com/RichardLitt/standard-readme](https://github.com/RichardLitt/standard-readme).
    *   *Mức độ phổ biến/adoption:* Hơn 3.500 stars trên GitHub (2024). Được cộng đồng IPFS, các gói thư viện JavaScript và nhiều tổ chức mã nguồn mở chấp nhận rộng rãi; có cả CLI generator (`generator-standard-readme`) và bộ linter tự động kiểm tra định dạng.
    *   *Ưu điểm:* Cấu trúc đồng nhất, tính module cao, có quy chuẩn đánh badge và phân mục chuẩn chỉ (Table of Contents, Install, Usage, API, Contributing, License).
    *   *Nhược điểm:* Quá nặng về mặt thủ tục đối với các ứng dụng nội bộ (internal services/apps); mục API tích hợp sẵn trong README dễ gây phình to (bloat), vi phạm tính tinh gọn.
*   **Ứng viên B: Make a README**
    *   *Nguồn:* Hướng dẫn cộng đồng và template do Danny Guo khởi xướng (2017) tại [makeareadme.com](https://www.makeareadme.com) và [github.com/ddnexus/make-a-readme](https://github.com/ddnexus/make-a-readme).
    *   *Mức độ phổ biến/adoption:* Hơn 3.000 stars trên GitHub (2024). Là tài liệu hướng dẫn mặc định được trích dẫn trong rất nhiều khóa đào tạo kỹ sư phần mềm và các hackathon toàn cầu.
    *   *Ưu điểm:* Dễ tiếp cận, tập trung vào người đọc (giải thích dự án làm gì, tại sao hữu ích, cách bắt đầu), ngôn từ tự nhiên, không gò bó khuôn mẫu.
    *   *Nhược điểm:* Thiếu cơ chế kiểm soát cấu trúc chặt chẽ cho môi trường doanh nghiệp; không quy định rõ vị trí của các thông tin quan trọng như biến môi trường (`.env`), kiểm thử hoặc kiến trúc thư mục.
*   **Ứng viên C: GitHub Recommended Minimal README**
    *   *Nguồn:* Tài liệu chính thức từ GitHub Docs (2016–2024) tại [docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes).
    *   *Mức độ phổ biến/adoption:* Tiêu chuẩn mặc định hiển thị trên hàng chục triệu kho lưu trữ mã nguồn của GitHub.
    *   *Ưu điểm:* Cực kỳ tinh gọn, thiết lập trong 2 phút, hiển thị trực quan ngay trang chủ repo.
    *   *Nhược điểm:* Quá sơ sài nếu áp dụng cho một codebase sản phẩm thực tế; thiếu hướng dẫn cụ thể về quy trình phát triển cục bộ và xác thực môi trường.

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:** **Pragmatic Developer README** (Template tinh gọn kết hợp giữa triết lý thực dụng của *Make a README* và các trường thực thi kỹ thuật của *Standard Readme*).
*   **Lý do cho team 3–10 người:**
    *   Mục tiêu sống còn của team nhỏ là **Onboarding tốc độ cao** (dưới 15 phút từ lúc `git clone` đến lúc chạy được ứng dụng và vượt qua bộ test cục bộ).
    *   Tránh lãng phí thời gian tạo các mục hành chính rườm rà như Table of Contents hay Maintainers list dài dòng khi toàn đội ngồi cùng phòng hoặc cùng một kênh Slack/Discord `(suy luận)`.
    *   Tập trung 100% vào việc khởi tạo môi trường, kết nối cơ sở dữ liệu giả lập, và các lệnh chạy hàng ngày.

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc:**
    1.  `Project Title & TL;DR`: Tên sản phẩm + 1 câu mô tả chính xác hệ thống giải quyết vấn đề gì, cho đối tượng nào.
    2.  `Prerequisites`: Phiên bản Node/Go/Python/Docker cụ thể bắt buộc phải cài.
    3.  `Quickstart (Local Setup)`: Tối đa 4–5 dòng lệnh chạy được ngay (Clone -> Copy `.env.example` -> Cài package -> Seed database -> Khởi động dev server).
    4.  `Environment Variables`: Bảng giải thích các biến môi trường quan trọng nhất (hoặc dẫn chiếu trực tiếp đến file `.env.example`).
    5.  `Verification & Testing`: Lệnh chính xác để chạy unit/integration test cục bộ nhằm xác nhận môi trường đã sẵn sàng hoạt động.
    6.  `Key Architecture / Directory Map`: Cây thư mục 10–15 dòng giải thích logic mã nguồn nằm ở đâu.
*   **Các mục tuỳ chọn:**
    *   `Badges`: Trạng thái CI/CD build, test coverage.
    *   `Deployment Summary`: Hướng dẫn hoặc link trỏ sang runbook triển khai production.
    *   `Contributing / Links`: Trỏ tới `AGENTS.md`, `ARCHITECTURE.md`, `SECURITY.md`.

### 4. Độ dài / mức chi tiết hợp lý
*   **Độ dài:** 1–2 trang màn hình (khoảng 40–80 dòng Markdown, tương đương 300–600 từ).
*   **Chi tiết:** Không nhồi nhét tài liệu API hay lịch sử phiên bản vào README. Mọi dòng lệnh phải là bản copy-paste chạy được ngay.

### 5. Anti-pattern (điều nên tránh)
*   **Mega-README (Wall of Text):** Nhồi toàn bộ tài liệu API, hướng dẫn cài đặt Kubernetes, sơ đồ database và changelog vào một file README duy nhất. Hiện tượng này dẫn đến "Bit rot" (tài liệu bị ôi thiu), khi code thay đổi nhưng không ai cập nhật nổi một file dài 2.000 dòng.
*   **Lệnh giả định (Assumed environment):** Ghi chung chung *"Cài đặt các gói phụ thuộc và chạy cơ sở dữ liệu"* mà không cung cấp lệnh cụ thể hoặc file `docker-compose.yml`, khiến lập trình viên mới mất hàng giờ sửa lỗi môi trường.

### 6. Khác biệt khi có AI agent
*   **Cách agent đọc/viết:** AI coding agent (như Cursor, Aider, Claude Code) luôn đọc `README.md` đầu tiên khi tiếp nhận codebase để hiểu ngữ cảnh tổng quát và cách chạy dự án.
*   **Điều cần đổi:**
    *   Các lệnh trong mục Quickstart và Testing phải tuyệt đối chính xác về mặt cú pháp; không sử dụng các placeholder mơ hồ kiểu `<thay_bang_secret_cua_ban>` trong lệnh khởi động cơ bản `(suy luận)`.
    *   README cần có chỉ dẫn rõ ràng trỏ tới file quy ước của agent (như `AGENTS.md`) và lệnh kiểm thử đơn lẻ (single-test command) để agent có thể chạy vòng lặp sửa lỗi tự động (feedback loop).

---

## D2. File hướng dẫn cho AI agent (AGENTS.md / CLAUDE.md / rules)

### 1. Các ứng viên
*   **Ứng viên A: AGENTS.md**
    *   *Nguồn:* Chuẩn mở độc lập nền tảng được cộng đồng và các công cụ phát triển phần mềm AI thúc đẩy (2024–2025) tại [agents.md](https://agents.md).
    *   *Mức độ phổ biến/adoption:* Đang nhanh chóng trở thành tiêu chuẩn de facto trung lập (tool-agnostic) được hỗ trợ bởi nhiều công cụ như OpenAI Codex, Aider, Zed, Cursor, Amp và Bodegaone. Hỗ trợ cấu trúc phân cấp kế thừa từ root repo đến từng thư mục con (`subfolder/AGENTS.md`).
    *   *Ưu điểm:* Không bị khóa chặt vào một nhà cung cấp (vendor-agnostic); định dạng Markdown thuần khiết, nhẹ, dễ đọc; cho phép chia sẻ quy ước chung cho toàn bộ kỹ sư dù họ dùng các AI client khác nhau.
    *   *Nhược điểm:* Chưa có schema xác thực tự động chính thức; một số IDE đời cũ vẫn cần file cấu hình riêng biệt.
*   **Ứng viên B: CLAUDE.md**
    *   *Nguồn:* Tài liệu chính thức của Anthropic dành cho công cụ Claude Code CLI (2024–2025) tại [docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code).
    *   *Mức độ phổ biến/adoption:* Tiêu chuẩn bắt buộc cho người dùng hệ sinh thái Anthropic Claude Code. Được cộng đồng kỹ sư dùng Claude Code đánh giá rất cao nhờ khả năng tự động tải vào bộ nhớ ngữ cảnh ban đầu (system prompt memory).
    *   *Ưu điểm:* Tối ưu hóa sâu cho vòng lặp kiểm tra lệnh shell, build và test của Claude Code; cấu trúc phân tầng rõ ràng (User level, Project level, Directory level).
    *   *Nhược điểm:* Mang tính chất độc quyền cho công cụ của Anthropic; công cụ khác không tự động nhận diện nếu không cấu hình thêm.
*   **Ứng viên C: Cursor Rules (`.cursor/rules/*.mdc` / legacy `.cursorrules`)**
    *   *Nguồn:* Tài liệu chính thức của Cursor IDE (Anysphere, 2024–2025) tại [docs.cursor.com/context/rules-for-ai](https://docs.cursor.com/context/rules-for-ai).
    *   *Mức độ phổ biến/adoption:* Phổ biến bậc nhất hiện nay trong giới kỹ sư sử dụng Cursor. Đã chuyển dịch từ một file đơn lẻ `.cursorrules` sang thư mục `.cursor/rules/` chứa các file định dạng `.mdc`.
    *   *Ưu điểm:* Rất mạnh nhờ metadata frontmatter (`globs`, `alwaysApply`, `description`). Cho phép kích hoạt quy tắc theo ngữ cảnh (chỉ load khi sửa file khớp với glob pattern như `*.tsx` hoặc khi agent nhận diện cần thiết), giúp tiết kiệm token tối đa.
    *   *Nhược điểm:* Định dạng `.mdc` có cú pháp riêng, khó tái sử dụng trực tiếp cho các agent chạy qua terminal (như Claude Code hay Aider) nếu không có script chuyển đổi.
*   **Ứng viên D: GitHub Copilot Instructions (`.github/copilot-instructions.md`)**
    *   *Nguồn:* Tài liệu chính thức của GitHub Copilot (Microsoft/GitHub, 2024) tại [docs.github.com](https://docs.github.com).
    *   *Mức độ phổ biến/adoption:* Tích hợp tự nhiên trong hệ sinh thái GitHub Copilot Chat và Workspace Agent.
    *   *Ưu điểm:* Nằm sẵn trong thư mục `.github/`, tương thích tự nhiên với repository hosting.
    *   *Nhược điểm:* Tính năng còn đơn giản, thiếu khả năng phân vùng ngữ cảnh linh hoạt theo glob pattern như Cursor.

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:** **AGENTS.md tại thư mục gốc làm Single Source of Truth (SSOT)**, kết hợp tạo symlink (hoặc script đồng bộ tự động) sang `CLAUDE.md` và `.cursor/rules/main.mdc` nếu trong team có sự phân hóa công cụ.
*   **Lý do cho team 3–10 người:**
    *   Trong một team nhỏ, mỗi kỹ sư có thể có sở thích công cụ khác nhau (người dùng Cursor, người dùng Claude Code trên iTerm2, người dùng Copilot trong VS Code). Việc duy trì 3–4 file quy tắc riêng lẻ sẽ dẫn đến tình trạng "lệch quy chuẩn" (configuration drift) `(suy luận)`.
    *   `AGENTS.md` theo chuẩn mở của [agents.md](https://agents.md) đóng vai trò như một bản "README dành riêng cho máy", dễ quản lý và review qua Pull Request y hệt như code.

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc:**
    1.  `Project Tech Stack & Runtime Constraints`: Ngôn ngữ, framework, phiên bản runtime (vd: Node 22 LTS, strict TypeScript, Python 3.12).
    2.  `Build, Lint & Test Commands`: Các lệnh CLI chính xác dạng 1 dòng (lệnh chạy linter, lệnh chạy toàn bộ test, lệnh chạy một test đơn lẻ).
    3.  `Code Style & Hard Architectural Rules`: 3–5 quy tắc không thể thương lượng (vd: "Luôn dùng Zod validate dữ liệu đầu vào", "Không dùng type `any`", "Dùng Tailwind CSS thay vì inline style").
    4.  `Boundaries & Safety ("Never Do")`: Các hành động bị cấm tuyệt đối (vd: "Không sửa file trong `dist/` hoặc `generated/`", "Không tự ý thêm thư viện ngoài khi chưa có xác nhận", "Không commit secret").
*   **Các mục tuỳ chọn:**
    *   `File Routing & Architecture Map`: Quy định tạo file mới ở đâu (vd: API route đặt tại `src/app/api/`).
    *   `Preferred Patterns / Error Handling`: Mẫu trả về lỗi chuẩn, cách xử lý bất đồng bộ.
    *   `Git & PR Etiquette for Agent`: Quy tắc viết commit message chuẩn Conventional Commits.

### 4. Độ dài / mức chi tiết hợp lý
*   **Độ dài:** 80–200 dòng (khoảng 500–1.200 từ, tương đương 800–1.800 tokens).
*   **Nguyên tắc:** Ngắn gọn, súc tích, mang tính mệnh lệnh. Không đưa vào các giải thích dài dòng mang tính triết lý.

### 5. Anti-pattern (điều nên tránh)
*   **Instruction Bloat (Nhồi nhét kiến thức phổ thông):** Dạy lại LLM những điều nó đã biết quá rõ (như giải thích nguyên lý SOLID là gì, cú pháp vòng lặp `for` trong Python ra sao). Việc này làm lãng phí dung lượng context window và làm giảm sự chú ý của mô hình vào các quy tắc dự án đặc thù.
*   **Quy tắc mâu thuẫn hoặc lỗi thời (Stale Rules):** Ghi trong rule là "Cấm dùng Axios, bắt buộc dùng fetch" nhưng trong codebase lại có hàng trăm file dùng Axios. Khi đó, AI agent sẽ rơi vào trạng thái bối rối (hallucination hoặc từ chối thực hiện).

### 6. Khác biệt khi có AI agent
*   Đây là tài liệu được sinh ra **dành riêng cho AI agent đọc**, con người chỉ đóng vai trò viết, giám sát và duy trì.
*   Mọi chỉ dẫn phải chuyển từ dạng mô tả thụ động sang **mệnh lệnh hành động (imperative verbs)**.
*   Phải cung cấp lệnh tự kiểm tra (Verification loop): Hướng dẫn agent cách tự chạy linter và test sau khi viết code xong để nó tự sửa lỗi trước khi bàn giao lại cho lập trình viên.

---

## D3. Tài liệu kiến trúc tổng quan (arc42, C4, …)

### 1. Các ứng viên
*   **Ứng viên A: arc42**
    *   *Nguồn:* Sáng lập bởi Dr. Peter Hruschka và Dr. Gernot Starke (2005–2024) tại [arc42.org](https://arc42.org) và [github.com/arc42/arc42-template](https://github.com/arc42/arc42-template).
    *   *Mức độ phổ biến/adoption:* Tiêu chuẩn vàng của Hiệp hội Kiến trúc Phần mềm Quốc tế (iSAQB). Được áp dụng rộng rãi tại các tập đoàn lớn, cơ quan chính phủ và các hệ thống ngân hàng/bảo hiểm tại châu Âu.
    *   *Ưu điểm:* Cực kỳ toàn diện, gồm đúng 12 phần bao quát mọi góc nhìn kiến trúc (từ mục tiêu kinh doanh, bối cảnh, khối xây dựng, runtime, deployment cho đến thuộc tính chất lượng và rủi ro).
    *   *Nhược điểm:* Quá cồng kềnh cho team 3–10 người. Việc duy trì 12 phần đòi hỏi nỗ lực lớn, dễ dẫn đến tình trạng tài liệu hóa hình thức và lỗi thời chỉ sau vài tuần phát triển nhanh `(suy luận)`.
*   **Ứng viên B: C4 Model**
    *   *Nguồn:* Khởi xướng bởi Simon Brown (2018) tại [c4model.com](https://c4model.com).
    *   *Mức độ phổ biến/adoption:* Được hàng chục nghìn đội ngũ kỹ thuật trên toàn cầu sử dụng. Trở thành chuẩn mực mô hình hóa trực quan trong phong trào Agile và Docs-as-Code; tích hợp sâu với Structurizr, PlantUML, Mermaid.
    *   *Ưu điểm:* Cung cấp tư duy phân tầng trực quan giống như bản đồ địa lý Google Maps (Context -> Container -> Component -> Code). Giúp mọi đối tượng (từ kinh doanh đến kỹ sư) đều hiểu được hệ thống ở tầng trừu tượng phù hợp.
    *   *Nhược điểm:* Bản thân C4 chỉ là mô hình vẽ sơ đồ (diagramming framework), không cung cấp sẵn cấu trúc văn bản để ghi chép các quyết định kỹ thuật sâu, chiến lược dữ liệu hay các yêu cầu phi chức năng.
*   **Ứng viên C: Pragmatic Markdown Architecture Doc (Architecture Hoisting / ADR-Centric)**
    *   *Nguồn:* Thúc đẩy bởi Martin Fowler và ThoughtWorks Technology Radar (2015–2024) tại [martinfowler.com](https://martinfowler.com).
    *   *Mức độ phổ biến/adoption:* Rất phổ biến trong các startup công nghệ và các dự án mã nguồn mở hiện đại (vd: tài liệu `ARCHITECTURE.md` của các dự án lớn trên GitHub).
    *   *Ưu điểm:* Tinh gọn, đặt ngay trong repo (`docs/ARCHITECTURE.md`), sử dụng sơ đồ Mermaid dạng text, review qua Git PR, sống đồng hành cùng mã nguồn.
    *   *Nhược điểm:* Có thể thiếu tính cấu trúc chặt chẽ nếu đội ngũ kỹ thuật thiếu kỷ luật tự giác.

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:** **Pragmatic Architecture Doc (kết hợp C4 Level 1 & Level 2 vẽ bằng Mermaid + Tech Stack Matrix + Tham chiếu ADR)**.
*   **Lý do cho team 3–10 người:**
    *   Team nhỏ không có vai trò Kiến trúc sư chuyên trách (Dedicated Enterprise Architect). Bản thân các kỹ sư phải kiêm nhiệm, nên tài liệu phải ngắn gọn, dễ sửa qua PR.
    *   Việc sử dụng sơ đồ C4 (Context & Container) vẽ bằng mã nguồn Mermaid cho phép GitHub/GitLab render trực tiếp trên web mà không cần lưu file ảnh nhị phân (PNG/JPEG) không diff được `(suy luận)`.

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc:**
    1.  `System Context (C4 Level 1)`: Sơ đồ Mermaid mô tả hệ thống ở trung tâm, người dùng (actors) xung quanh và các hệ thống bên thứ ba tích hợp (Stripe, SendGrid, OAuth, v.v.).
    2.  `Container Architecture (C4 Level 2)`: Sơ đồ mô tả các khối chạy độc lập (Frontend SPA, Backend API Gateway, Worker Service, PostgreSQL, Redis) và các giao thức giao tiếp (HTTPS, gRPC, WebSocket).
    3.  `Core Technology Stack & Rationale`: Bảng tổng hợp công nghệ chính kèm 1 câu lý do lựa chọn.
    4.  `Data Flow & Critical Paths`: Mô tả luồng dữ liệu của 2–3 nghiệp vụ sống còn nhất (vd: luồng Đăng ký & Xác thực, luồng Thanh toán & Xử lý đơn hàng).
    5.  `Cross-cutting Concerns`: Quy ước nền tảng về Bảo mật (AuthN/AuthZ), Nhật ký (Logging/Tracing) và Xử lý lỗi tập trung.
*   **Các mục tuỳ chọn:**
    *   `Component View (C4 Level 3)`: Chỉ vẽ cho container nào có độ phức tạp thuật toán đặc biệt cao.
    *   `Infrastructure & Deployment View`: Sơ đồ ánh xạ lên cloud (AWS ECS/EKS, Vercel, Supabase).
    *   `Ubiquitous Language / Glossary`: Bảng từ điển thuật ngữ nghiệp vụ cốt lõi.

### 4. Độ dài / mức chi tiết hợp lý
*   **Độ dài:** 3–6 trang Markdown (khoảng 1.000–2.000 từ) kèm 2–3 biểu đồ Mermaid.
*   **Nguyên tắc:** Cập nhật tài liệu này chỉ khi có sự thay đổi về ranh giới dịch vụ, cơ sở dữ liệu mới hoặc đổi khung công nghệ. Không mô tả chi tiết từng class hay function.

### 5. Anti-pattern (điều nên tránh)
*   **C4 Level 4 (Code Level) Diagramming:** Cố gắng vẽ sơ đồ chi tiết class/function bằng tay. Simon Brown (tác giả C4) khuyến cáo rõ ràng: Level 4 là không cần thiết vì mã nguồn thay đổi hàng ngày, việc vẽ tay sẽ làm tài liệu sai lệch ngay lập tức; hãy để IDE tự sinh nếu cần [c4model.com](https://c4model.com).
*   **Biểu đồ nhị phân (Binary Images):** Xuất sơ đồ ra file PNG/Visio rồi commit vào git. Khi cần sửa, người sau không có file gốc hoặc phần mềm chuyên dụng, dẫn đến sơ đồ bị bỏ rơi vĩnh viễn.

### 6. Khác biệt khi có AI agent
*   **Cách agent đọc/viết:** AI agent không thể "nhìn" và suy luận ngữ cảnh sâu từ ảnh PNG một cách đáng tin cậy trong context code, nhưng chúng đọc và sinh mã **Mermaid/PlantUML** cực kỳ xuất sắc.
*   **Điều cần đổi:** Cung cấp sơ đồ C4 dạng Mermaid giúp AI agent hiểu rõ ranh giới kiến trúc (architectural boundaries). Nhờ đó, agent sẽ không sinh mã vi phạm kiến trúc (vd: không tự ý import database driver trực tiếp vào React component, không gọi xuyên tầng service mà không qua interface) `(suy luận)`.

---

## D4. ADR — Architecture Decision Record (Nygard, MADR, Y-statement, …)

### 1. Các ứng viên
*   **Ứng viên A: Michael Nygard Template**
    *   *Nguồn:* Đề xuất bởi Michael Nygard (2011) trong bài viết kinh điển *"Documenting Architecture Decisions"* trên blog Cognitect tại [cognitect.com/blog/2011/11/15/documenting-architecture-decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
    *   *Mức độ phổ biến/adoption:* Là mẫu ADR đầu tiên và phổ biến nhất trên thế giới. Được tích hợp trong công cụ CLI huyền thoại `adr-tools` và áp dụng tại hàng nghìn tổ chức.
    *   *Ưu điểm:* Cấu trúc tối giản gồm 5 phần: Title, Status, Context, Decision, Consequences. Rất ít ma sát khi viết, lập trình viên có thể soạn thảo xong trong 10 phút.
    *   *Nhược điểm:* Thiếu mục so sánh các phương án đã bị từ chối (Alternatives Considered) và động lực thúc đẩy (Decision Drivers), dễ dẫn đến việc ghi chép mang tính thiên kiến một chiều.
*   **Ứng viên B: MADR (Markdown Architectural Decision Records)**
    *   *Nguồn:* Dự án chuẩn mở do Oliver Kopp, Olaf Zimmermann và cộng sự phát triển (2017–2024) tại [adr.github.io/madr](https://adr.github.io/madr/).
    *   *Mức độ phổ biến/adoption:* Chuẩn ADR hiện đại được hỗ trợ mạnh mẽ nhất hiện nay trên GitHub. Hỗ trợ template chính thức từ phiên bản 2.x đến 3.x, có công cụ linter và VS Code extension.
    *   *Ưu điểm:* Thiết kế tối ưu cho Markdown trong Git; cấu trúc chặt chẽ gồm Decision Drivers, Considered Options (kèm bảng phân tích Pros/Cons cho từng phương án), Chosen Option, và Consequences.
    *   *Nhược điểm:* Bản đầy đủ có thể hơi dài đối với các quyết định kỹ thuật nhỏ.
*   **Ứng viên C: Y-Statement**
    *   *Nguồn:* Đề xuất bởi Olaf Zimmermann (2012, 2017) tại [ozimmer.ch](https://ozimmer.ch).
    *   *Mức độ phổ biến/adoption:* Được giảng dạy rộng rãi trong giới nghiên cứu kiến trúc phần mềm và hội thảo IEEE/ACM; thường được dùng làm câu tóm tắt mở đầu cho các tài liệu ADR lớn hơn.
    *   *Ưu điểm:* Cô đọng toàn bộ quyết định kiến trúc phức tạp vào đúng **1 câu duy nhất** theo mẫu: *"Trong ngữ cảnh [X], đối mặt với [Y], chúng tôi quyết định chọn [Z] (và từ bỏ [W]) để đạt được [Q], chấp nhận [C]"*.
    *   *Nhược điểm:* Quá ngắn để diễn giải chi tiết kỹ thuật, đoạn mã minh họa hoặc các bước kiểm chứng thực tế.

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:** **MADR phiên bản tinh gọn (MADR v3.0.0 Minimal/Standard)**.
*   **Lý do cho team 3–10 người:**
    *   Điểm giá trị nhất của một tài liệu quyết định kiến trúc không phải là ghi lại những gì mình làm, mà là ghi lại **những gì mình đã quyết định KHÔNG LÀM và TẠI SAO**.
    *   Mục "Considered Options" với phân tích ưu/nhược điểm trong MADR giúp loại bỏ triệt để các cuộc tranh cãi lặp đi lặp lại khi có thành viên mới gia nhập đội ngũ.
    *   Định dạng Markdown chuẩn hóa với metadata rõ ràng giúp lưu trữ tự nhiên trong thư mục `docs/adr/`.

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc:**
    1.  `Title`: Định dạng số thứ tự + tên quyết định (vd: `0004-use-postgres-for-event-storage.md`).
    2.  `Status`: Proposed / Accepted / Deprecated / Superseded by [ADR-XXXX].
    3.  `Context and Problem Statement`: Bối cảnh kỹ thuật và bài toán cần giải quyết (2–4 câu).
    4.  `Decision Drivers`: 3–4 tiêu chí cốt lõi định hình quyết định (vd: tốc độ ra mắt, chi phí hạ tầng, yêu cầu ACID).
    5.  `Considered Options`: Liệt kê ít nhất 2 phương án (kèm tóm tắt ưu/nhược điểm chính của từng phương án).
    6.  `Decision Outcome`: Lựa chọn cuối cùng và lý do vượt trội so với các phương án còn lại.
    7.  `Consequences`: Cả hệ quả tích cực (lợi ích đạt được) lẫn hệ quả tiêu cực/rủi ro kỹ thuật phải chấp nhận đánh đổi (trade-offs).
*   **Các mục tuỳ chọn:**
    *   `Confirmation / Validation Path`: Cách thức kiểm chứng quyết định trong tương lai (vd: benchmark, test tải).
    *   `Pros and Cons of the Options`: Bảng chấm điểm chi tiết nếu là quyết định phức tạp.

### 4. Độ dài / mức chi tiết hợp lý
*   **Độ dài:** 1–2 trang Markdown (khoảng 300–600 từ cho mỗi bản ADR).
*   **Thời gian viết & review:** Không quá 30–45 phút để soạn thảo; review bất đồng bộ qua PR cùng lúc với code triển khai.

### 5. Anti-pattern (điều nên tránh)
*   **Sửa đổi nội dung ADR đã "Accepted" thay vì "Supersede":** ADR là bản ghi nhật ký bất biến theo dòng thời gian (immutable append-only log). Khi một quyết định cũ không còn phù hợp, tuyệt đối không sửa đè lên file cũ mà phải tạo một ADR mới đánh dấu trạng thái "Supersedes ADR-0002" [cognitect.com](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions).
*   **Lạm phát ADR cho các quyết định vi mô:** Viết ADR cho việc đặt tên biến, chọn thư viện format ngày tháng, hay cấu trúc file CSS. Chỉ viết ADR cho những quyết định mang tính "đắt giá, khó đảo ngược" (one-way door decisions).

### 6. Khác biệt khi có AI agent
*   **Soạn thảo bản nháp (Drafting):** AI agent là công cụ xuất sắc để draft ADR. Kỹ sư chỉ cần cung cấp bài toán và các ràng buộc, agent có thể tra cứu thông tin, liệt kê 3 phương án khả thi kèm bảng ưu/nhược điểm theo đúng chuẩn MADR trong 60 giây `(suy luận)`.
*   **Agent đọc hiểu ràng buộc:** Khi tiếp nhận task lập trình, AI agent có thể quét toàn bộ thư mục `docs/adr/` để nắm rõ các quyết định đã chốt của dự án (vd: "Dự án đã chốt dùng Kysely thay vì Prisma theo ADR-0003"). Điều này ngăn chặn việc agent tự ý cài đặt các thư viện lạ đi ngược lại định hướng của đội ngũ.

---

## D5. API contract & quy ước API (OpenAPI, style guide …)

### 1. Các ứng viên
*   **Ứng viên A: OpenAPI Specification (OAS 3.0 / 3.1)**
    *   *Nguồn:* Quản lý bởi OpenAPI Initiative trực thuộc Linux Foundation (2021) tại [spec.openapis.org/oas/latest.html](https://spec.openapis.org/oas/latest.html).
    *   *Mức độ phổ biến/adoption:* Tiêu chuẩn công nghiệp toàn cầu tuyệt đối cho giao diện lập trình ứng dụng RESTful. Hỗ trợ hệ sinh thái công cụ khổng lồ: Swagger UI, Redoc, Prism mock server, Orval, OpenAPI Generator.
    *   *Ưu điểm:* Định dạng máy đọc được (JSON/YAML), trung lập với mọi ngôn ngữ lập trình, cho phép tự động hóa hoàn toàn từ sinh mã client SDK, kiểm thử tự động, đến tài liệu hóa tương tác.
    *   *Nhược điểm:* Việc viết và duy trì file YAML thủ công bằng tay rất tốn công sức và dễ mắc lỗi cú pháp nếu không có công cụ hỗ trợ.
*   **Ứng viên B: Google Cloud API Design Guide / AIPs**
    *   *Nguồn:* Tài liệu chuẩn thiết kế API của Google (2017–2024) tại [cloud.google.com/apis/design](https://cloud.google.com/apis/design) và cộng đồng mã nguồn mở [aip.dev](https://aip.dev).
    *   *Mức độ phổ biến/adoption:* Được coi là "kinh thánh" về thiết kế API định hướng tài nguyên (Resource-oriented design) cho cả hệ thống REST lẫn gRPC.
    *   *Ưu điểm:* Chuẩn mực hóa cực kỳ sâu sắc về quy ước đặt tên URL (danh từ số nhiều, phân cấp), các phương thức chuẩn (`Get`, `List`, `Create`, `Update`, `Delete`), cơ chế phân trang cursor (`page_size`, `page_token`), và mô hình xử lý lỗi.
    *   *Nhược điểm:* Rất đồ sộ, nhiều quy định chỉ phù hợp cho quy mô siêu lớn của Google; cần chắt lọc tinh gọn khi đưa vào team nhỏ.
*   **Ứng viên C: Spectral Automated Linter Ruleset**
    *   *Nguồn:* Dự án mã nguồn mở của Stoplight (2019–2024) tại [github.com/stoplightio/spectral](https://github.com/stoplightio/spectral).
    *   *Mức độ phổ biến/adoption:* Thư viện linter JSON/YAML tiêu chuẩn phổ biến nhất thế giới để kiểm tra tự động các file OpenAPI trong pipeline CI/CD.
    *   *Ưu điểm:* Biến các quy tắc trên giấy thành **code thực thi tự động** (`.spectral.yaml`). Nếu kỹ sư hoặc AI viết API sai quy ước đặt tên hoặc thiếu mô tả lỗi, CI sẽ báo đỏ ngay lập tức trên PR.
    *   *Nhược điểm:* Đòi hỏi đội ngũ phải cấu hình bộ ruleset ban đầu.

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:** **OpenAPI 3.1 Spec (Code-first hoặc Design-first tinh gọn) + Quy ước thiết kế rút gọn từ Google AIP + Kiểm tra tự động bằng Spectral (`.spectral.yaml`)**.
*   **Lý do cho team 3–10 người:**
    *   Team nhỏ không có thời gian họp review từng tên trường API trên PR. Cách tiếp cận tốt nhất là ban hành một quy ước ngắn gọn và dùng Spectral để CI tự động kiểm tra `(suy luận)`.
    *   OpenAPI 3.1 tương thích hoàn toàn 100% với JSON Schema (2020-12), giúp tái sử dụng hoàn hảo các schema xác thực dữ liệu (như Zod hoặc Pydantic).

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc:**
    1.  `Resource Naming & URI Conventions`: Danh từ số nhiều, chữ thường, nối dấu gạch ngang (`kebab-case`) cho endpoint (vd: `/v1/user-profiles/{profile_id}`).
    2.  `Field Casing Convention`: Thống nhất duy nhất một chuẩn cho payload dữ liệu (khuyến nghị `camelCase` cho JavaScript/TypeScript stack hoặc `snake_case` cho Python/Go; tuyệt đối không trộn lẫn).
    3.  `Standard HTTP Methods & Status Codes`: Sử dụng nghiêm ngặt: `GET` (200), `POST` (201), `PUT/PATCH` (200), `DELETE` (204), và các mã lỗi `400, 401, 403, 404, 409, 422, 500`.
    4.  `Unified Error Response Envelope`: Khung trả lời lỗi thống nhất toàn hệ thống (dựa theo chuẩn [RFC 7807 Problem Details](https://datatracker.ietf.org/doc/html/rfc7807) hoặc chuẩn Google Error: `{ error: { code, message, details: [] } }`).
    5.  `Pagination & Filtering Standards`: Quy định tham số phân trang chuẩn cho các endpoint dạng danh sách (vd: `page_size` và `page_token` hoặc `limit` và `offset`).
    6.  `Authentication Scheme`: Định dạng truyền Bearer JWT qua header `Authorization`.
*   **Các mục tuỳ chọn:**
    *   `Idempotency Key`: Header `Idempotency-Key` cho các giao dịch thanh toán quan trọng.
    *   `Rate Limiting Headers`: Chuẩn header `X-RateLimit-*`.
    *   `API Versioning Strategy`: Quy ước phiên bản trên đường dẫn URL (URI path: `/v1/`) hay qua header.

### 4. Độ dài / mức chi tiết hợp lý
*   **Tài liệu văn bản (Style Guide):** Tối đa 2–3 trang Markdown (khoảng 600–1.000 từ) tóm tắt các quy tắc cốt lõi.
*   **File cấu hình tự động:** Một file `.spectral.yaml` khoảng 40–80 dòng chạy trực tiếp trong GitHub Actions.

### 5. Anti-pattern (điều nên tránh)
*   **HTTP 200 Tunneling:** Trả về mã trạng thái HTTP 200 OK cho mọi request, nhưng bên trong body lại chứa `{ "success": false, "error": "User not found" }`. Điều này phá vỡ hoàn toàn khả năng giám sát tự động của các hạ tầng mạng (API Gateway, Cloudflare, Datadog) [cloud.google.com/apis/design/errors](https://cloud.google.com/apis/design/errors).
*   **Format rác không nhất quán:** Endpoint A trả về lỗi dạng chuỗi `{ "error": "failed" }`, endpoint B trả về đối tượng `{ "message": "failed", "code": 12 }`, endpoint C trả về mảng chuỗi `["failed"]`.

### 6. Khác biệt khi có AI agent
*   **Hợp đồng dữ liệu hoàn hảo cho Agent:** OpenAPI spec là định dạng tốt nhất để AI coding agent hiểu và tích hợp hệ thống. Từ file spec, AI agent có thể sinh toàn bộ code client-side, mock data, unit test và integration test với độ chính xác tuyệt đối mà không cần hỏi lại lập trình viên `(suy luận)`.
*   **Đồng bộ hóa 2 chiều:** Khi backend thay đổi API contract qua PR, AI agent có thể tự động đọc bản diff của OpenAPI spec và tạo một PR phụ để cập nhật toàn bộ frontend code tương ứng.

---

## D6. Spec / design doc / RFC cho một feature (Google design doc, RFC/KEP, …)

### 1. Các ứng viên
*   **Ứng viên A: Google Design Doc Template**
    *   *Nguồn:* Đúc kết từ thực tiễn kỹ thuật tại Google, được cựu Giám đốc Kỹ thuật Malte Ubl chia sẻ (2020) tại [industrialempathy.com/posts/design-docs-at-google](https://www.industrialempathy.com/posts/design-docs-at-google/).
    *   *Mức độ phổ biến/adoption:* Chuẩn mực kinh điển được sao chép và áp dụng tại hầu hết các công ty công nghệ tại Thung lũng Silicon (Meta, Uber, Airbnb, Vercel).
    *   *Ưu điểm:* Cực kỳ hiệu quả trong việc thúc đẩy tư duy phản biện. Cấu trúc tập trung mạnh mẽ vào: Context, Goals & Non-Goals, Proposed Solution, Alternatives Considered, và Cross-cutting concerns (Security, Observability, Cost).
    *   *Nhược điểm:* Có thể trở nên quá nặng nề nếu áp dụng nguyên bản cho các tính năng nhỏ chỉ mất 1–2 ngày lập trình.
*   **Ứng viên B: Rust RFC Template**
    *   *Nguồn:* Quy trình phát triển mã nguồn mở chính thức của ngôn ngữ lập trình Rust (2014–2024) tại [github.com/rust-lang/rfcs/blob/master/0000-template.md](https://github.com/rust-lang/rfcs/blob/master/0000-template.md).
    *   *Mức độ phổ biến/adoption:* Tiêu chuẩn vàng trong thế giới mã nguồn mở cho các thay đổi lớn về ngôn ngữ, compiler và core tooling.
    *   *Ưu điểm:* Phân tách rất xuất sắc giữa góc nhìn người dùng (`Guide-level explanation`) và chi tiết kỹ thuật triển khai nội bộ (`Reference-level explanation`), kèm mục `Drawbacks` và `Unresolved questions`.
    *   *Nhược điểm:* Khá hàn lâm và dài, thích hợp cho việc phát triển framework hoặc nền tảng hơn là các tính năng nghiệp vụ của ứng dụng web/mobile.
*   **Ứng viên C: ThoughtWorks Lightweight RFC / One-Pager**
    *   *Nguồn:* Thực hành Agile từ ThoughtWorks và Martin Fowler (2015–2024).
    *   *Mức độ phổ biến/adoption:* Phổ biến trong các đội ngũ khởi nghiệp phát triển sản phẩm theo chu kỳ ngắn.
    *   *Ưu điểm:* Đúng 1 trang A4: Problem, Proposed Solution, Open Questions. Ra quyết định cực nhanh.
    *   *Nhược điểm:* Dễ bỏ sót các khía cạnh an ninh, khả năng mở rộng hoặc kế hoạch rollback khi gặp sự cố sản xuất.

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:** **Pragmatic Google Design Doc (Mini-Design Doc / RFC)**.
*   **Lý do cho team 3–10 người:**
    *   Mục **Non-Goals** (Những gì KHÔNG LÀM) trong mẫu của Google là công cụ hữu hiệu nhất để bảo vệ một team nhỏ khỏi hội chứng phình phạm vi (scope creep) `(suy luận)`.
    *   Mục **Alternatives Considered** (Các giải pháp thay thế) buộc người viết phải suy nghĩ thấu đáo ít nhất 2 phương án trước khi gõ những dòng code đầu tiên.
    *   Tài liệu được lưu trực tiếp dưới dạng `docs/rfc/YYYY-MM-feature-name.md` và review bất đồng bộ qua Git PR trong vòng 24–48 giờ.

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc:**
    1.  `Context & Problem Statement`: Tại sao tính năng này cần thiết? Giải quyết nỗi đau gì của người dùng hoặc hệ thống?
    2.  `Goals & Explicit Non-Goals`:
        *   *Goals:* 2–3 mục tiêu định lượng đo lường được.
        *   *Non-Goals:* Danh sách rõ ràng những gì đội ngũ quyết định **chưa làm** trong đợt triển khai này.
    3.  `Proposed Technical Architecture`: Thiết kế kỹ thuật chi tiết (sơ đồ luồng, thay đổi database schema, danh sách API endpoint mới, logic xử lý chính).
    4.  `Alternatives Considered`: Ít nhất 1 giải pháp thay thế đã được cân nhắc và lý do bị loại bỏ.
    5.  `Rollout, Migration & Rollback Strategy`: Triển khai qua feature flag thế nào? Migration dữ liệu ra sao? Khi hệ thống lỗi thì rollback bằng cách nào mà không mất dữ liệu?
*   **Các mục tuỳ chọn:**
    *   `Security, Privacy & Compliance`: Đánh giá rủi ro lộ dữ liệu người dùng (PII).
    *   `Observability & Metrics`: Các chỉ số cảnh báo (alert metrics) và dashboard cần tạo.
    *   `Open Questions`: Những câu hỏi kỹ thuật còn bỏ ngỏ cần thảo luận thêm.

### 4. Độ dài / mức chi tiết hợp lý
*   **Độ dài:** 2–4 trang Markdown (khoảng 800–1.500 từ).
*   **Quy tắc:** Viết trong nửa ngày, thảo luận và phê duyệt qua PR trong 24 giờ. Nếu một tính năng chỉ mất dưới 2 ngày công để lập trình, chỉ cần viết một bản tóm tắt ngắn (1–2 đoạn) ngay trong GitHub Issue chứ không cần tạo file design doc riêng lẻ.

### 5. Anti-pattern (điều nên tránh)
*   **Bỏ qua mục Non-Goals:** Dẫn đến việc các bên liên quan liên tục đưa thêm yêu cầu mới vào giữa chừng, biến một task 3 ngày thành một dự án kéo dài 1 tháng không thể phát hành.
*   **Write-Only Design Doc:** Viết tài liệu rất hoành tráng để xin phê duyệt, nhưng trong quá trình lập trình thực tế lại thay đổi cấu trúc hoàn toàn mà không cập nhật lại bản doc, biến tài liệu thành đồ bỏ phế [industrialempathy.com](https://www.industrialempathy.com/posts/design-docs-at-google/).

### 6. Khác biệt khi có AI agent
*   **AI làm trợ lý phác thảo:** Kỹ sư viết bài toán nghiệp vụ thô và các ràng buộc, sau đó ra lệnh cho AI agent phác thảo khung design doc với đầy đủ database schema và API signature để kỹ sư rà soát và chỉnh sửa `(suy luận)`.
*   **Bản đặc tả định hướng cho AI code:** Một bản design doc hoàn chỉnh chính là tài liệu ngữ cảnh chất lượng cao nhất (High-context prompt) để nạp cho AI agent. Agent có thể bám sát từng mục trong design doc để sinh mã nguồn, tránh hiện tượng agent tự sáng tác các giải pháp kiến trúc kỳ dị.

---

## D7. Test strategy + Definition of Done (DoD)

### 1. Các ứng viên
*   **Ứng viên A: Practical Test Pyramid Framework**
    *   *Nguồn:* Phát triển từ mô hình gốc của Mike Cohn (2009) và được Ham Vocke & Martin Fowler chuẩn hóa (2018) tại [martinfowler.com/articles/practical-test-pyramid.html](https://martinfowler.com/articles/practical-test-pyramid.html).
    *   *Mức độ phổ biến/adoption:* Mô hình chiến lược kiểm thử tự động kinh điển nhất trong ngành kỹ nghệ phần mềm hiện đại.
    *   *Ưu điểm:* Phân bổ rõ ràng tỷ trọng và chi phí của các tầng kiểm thử: Chân tháp rộng là Unit Tests (chạy nhanh, rẻ, cô lập), thân tháp là Integration Tests (kiểm tra tích hợp DB/API), đỉnh tháp là End-to-End (E2E) UI Tests (rất ít, chỉ kiểm tra luồng trọng yếu).
    *   *Nhược điểm:* Tập trung vào mặt kỹ thuật tự động hóa, chưa bao quát được quy trình nghiệm thu và định nghĩa hoàn thành công việc ở cấp độ sprint.
*   **Ứng viên B: Scrum Guide Definition of Done (DoD)**
    *   *Nguồn:* Định nghĩa chính thức trong Scrum Guide bởi Ken Schwaber và Jeff Sutherland (2020) tại [scrumguides.org/scrum-guide.html](https://scrumguides.org/scrum-guide.html).
    *   *Mức độ phổ biến/adoption:* Tiêu chuẩn quản trị dự án Agile/Scrum phổ biến nhất trên toàn thế giới.
    *   *Ưu điểm:* Tính cam kết cao; DoD là cam kết bắt buộc cho mỗi Increment (phần tăng trưởng sản phẩm). Đảm bảo tính minh bạch và chất lượng đồng đều trước khi bàn giao.
    *   *Nhược điểm:* Định nghĩa mang tính nguyên lý trừu tượng, không đưa ra các tiêu chí kỹ thuật cụ thể cho từng loại dự án phần mềm.
*   **Ứng viên C: Agile Testing Quadrants**
    *   *Nguồn:* Đề xuất bởi Brian Marick (2003) và phát triển bởi Lisa Crispin & Janet Gregory trong sách *Agile Testing* (2009).
    *   *Mức độ phổ biến/adoption:* Được cộng đồng chuyên gia QA/QC toàn cầu áp dụng trong các hệ thống lớn.
    *   *Ưu điểm:* Phân chia 4 góc phần tư toàn diện: Q1 (Unit/Component - hướng công nghệ), Q2 (Functional - hướng nghiệp vụ), Q3 (Exploratory - đánh giá trải nghiệm), Q4 (Performance/Security - phi chức năng).
    *   *Nhược điểm:* Quá phức tạp và mang nặng tính lý thuyết cho một đội ngũ chỉ có 3–10 kỹ sư hoạt động không có đội ngũ QA chuyên trách riêng biệt.

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:** **Mô hình kết hợp: Chiến lược kiểm thử theo Practical Test Pyramid + Bộ tiêu chí Definition of Done (DoD) thực thi tự động qua CI checklist**.
*   **Lý do cho team 3–10 người:**
    *   Team nhỏ không có nhân sự QA thủ công chuyên trách. Bộ kiểm thử tự động là tấm lưới an toàn duy nhất để đội ngũ tự tin triển khai code lên production liên tục `(suy luận)`.
    *   Tỷ lệ vàng tối ưu cho team nhỏ: **70% Unit Tests** (kiểm tra logic nghiệp vụ thuần túy), **25% Integration Tests** (kiểm tra truy vấn database thật qua Testcontainers và API contracts), **5% E2E Smoke Tests** (kiểm tra 1–2 luồng người dùng sống còn bằng Playwright).
    *   DoD được tích hợp thẳng vào Pull Request Template dưới dạng các checkbox bắt buộc phải tích và vượt qua kiểm tra tự động của CI.

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc:**
    1.  `Testing Layers & Boundaries`: Quy định rõ cái gì test ở đâu (Logic tính toán -> Unit Test; Query DB / External API -> Integration Test; Giao diện phức tạp -> E2E Test).
    2.  `Meaningful Coverage Target`: Thiết lập ngưỡng kiểm thử thực chất (vd: tối thiểu 80% coverage cho thư mục `domain/` và `services/`, không ép coverage cho các file config hoặc migration).
    3.  `The Executable Definition of Done (DoD) Checklist`:
        *   Code biên dịch không có lỗi và không có warning từ compiler/linter.
        *   Tất cả Unit và Integration tests đều pass trên môi trường CI cục bộ.
        *   Các chức năng mới hoặc sửa lỗi bắt buộc phải có test đi kèm (không merge code không có test).
        *   Kiểm tra bảo mật tự động vượt qua (dependency vulnerability audit không có lỗi High/Critical).
        *   Tài liệu liên quan được cập nhật (README, API Spec hoặc ADR nếu có thay đổi kiến trúc).
*   **Các mục tuỳ chọn:**
    *   `Performance Benchmark`: Kiểm tra thời gian phản hồi không vượt quá ngưỡng cho phép (SLA).
    *   `Feature Flag Verification`: Xác nhận cờ tính năng đã được cấu hình trên môi trường Staging.

### 4. Độ dài / mức chi tiết hợp lý
*   **Độ dài:** 1–2 trang Markdown (`docs/TESTING_STRATEGY.md`), khoảng 400–800 từ, kèm checklist ngắn tích hợp trong PR template.

### 5. Anti-pattern (điều nên tránh)
*   **The Ice Cream Cone (Cây kem ốc quế ngược):** Không viết Unit test, viết rất ít Integration test, nhưng xây dựng một bộ kiểm thử đồ sộ toàn E2E UI tests bằng Cypress/Selenium. Kết quả: Bộ test chạy mất 45 phút, liên tục bị lỗi chập chờn (flaky tests), CI bị nghẽn và kỹ sư bắt đầu bỏ qua kết quả kiểm thử [martinfowler.com](https://martinfowler.com/articles/practical-test-pyramid.html).
*   **Vanity 100% Coverage Metric:** Ép buộc chỉ số 100% test coverage một cách mù quáng. Kỹ sư sẽ đối phó bằng cách viết các bài test vô nghĩa (test các hàm getter/setter, mock toàn bộ logic bên trong để chạy qua dòng lệnh mà không assert giá trị thực tế).

### 6. Khác biệt khi có AI agent
*   **Hiện tượng Test Ảo của AI:** AI agent có tốc độ sinh Unit test cực nhanh nhưng có xu hướng lạm dụng mock (mock toàn bộ hệ thống bên ngoài lẫn bên trong) khiến test luôn xanh dù code chạy thực tế bị lỗi `(suy luận)`.
*   **Quy tắc bắt buộc cho AI:**
    *   Phải hướng dẫn AI agent trong `AGENTS.md`: "Khi viết test, ưu tiên viết test kiểm tra các trường hợp biên (edge cases), dữ liệu rỗng (null/undefined), lỗi mạng và dữ liệu độc hại thay vì chỉ test happy path".
    *   Yêu cầu AI agent tự chạy bộ test sau khi viết code xong để đạt được trạng thái DoD trước khi tạo PR.

---

## D8. Pull request template

### 1. Các ứng viên
*   **Ứng viên A: GitHub Default Community PR Template**
    *   *Nguồn:* Tài liệu chuẩn của GitHub Docs (2016–2024) tại [docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository).
    *   *Mức độ phổ biến/adoption:* Biểu mẫu mặc định đặt tại `.github/pull_request_template.md`, được hàng triệu dự án trên GitHub sử dụng.
    *   *Ưu điểm:* Cấu trúc quen thuộc với mọi lập trình viên: Description, Issue link, How has this been tested, Checklist.
    *   *Nhược điểm:* Thường quá chung chung; nếu không tinh chỉnh, lập trình viên sẽ có thói quen xóa trắng template khi tạo PR.
*   **Ứng viên B: Conventional PRs Template**
    *   *Nguồn:* Dựa trên quy chuẩn Conventional Commits (2018–2024) tại [conventionalcommits.org](https://www.conventionalcommits.org).
    *   *Mức độ phổ biến/adoption:* Được cộng đồng mã nguồn mở hiện đại và các dự án áp dụng Semantic Release (tự động đánh version và xuất changelog) sử dụng rất rộng rãi.
    *   *Ưu điểm:* Tiêu đề và nội dung phân loại rõ ràng theo tiền tố ngữ nghĩa (`feat:`, `fix:`, `refactor:`, `chore:`, `perf:`), giúp reviewer hiểu ngay phạm vi ảnh hưởng chỉ qua tiêu đề PR.
    *   *Nhược điểm:* Cần một thời gian ngắn để các thành viên mới làm quen với chuẩn đặt tên.
*   **Ứng viên C: ThoughtWorks High-Context PR Template**
    *   *Nguồn:* Chia sẻ từ các chuyên gia tư vấn kỹ thuật của ThoughtWorks (2018–2024).
    *   *Mức độ phổ biến/adoption:* Phổ biến trong các tổ chức coi trọng thực hành Pair Programming và Code Review sâu.
    *   *Ưu điểm:* Tập trung giải thích sâu về "Tại sao thay đổi này tồn tại" (Why), "Các rủi ro tiềm ẩn" và cung cấp "Hướng dẫn reviewer cách tiếp cận bản diff hiệu quả nhất".
    *   *Nhược điểm:* Đòi hỏi người tạo PR mất nhiều thời gian biên soạn, dễ gây ức chế cho các PR nhỏ (dưới 20 dòng code).

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:** **Conventional PR Template kết hợp DoD Checklist tinh giản**.
*   **Lý do cho team 3–10 người:**
    *   Team nhỏ cần tốc độ review nhanh. Việc chuẩn hóa tiêu đề theo Conventional Commits giúp người review phân loại ngay độ ưu tiên `(suy luận)`.
    *   Một checklist ngắn dưới 5 mục đóng vai trò như chốt chặn an toàn cuối cùng buộc người tạo PR (dù là người hay AI) phải tự kiểm điểm lại trước khi bấm nút yêu cầu đồng nghiệp review.

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc:**
    1.  `PR Title Format`: Hướng dẫn đặt tiêu đề chuẩn `type(scope): short description` kèm link issue (vd: `fix(auth): handle expired refresh tokens (#142)`).
    2.  `Summary of Changes`: 2–3 gạch đầu dòng tóm tắt bản chất thay đổi (không liệt kê lại danh sách file đã sửa).
    3.  `Why`: Một câu giải thích bối cảnh và lý do tại sao chọn cách giải quyết này.
    4.  `How to Test / Verification Steps`: Các bước cụ thể để reviewer có thể tái hiện và kiểm tra tính đúng đắn của code.
    5.  `Pre-Merge Quality Checklist`:
        *   [ ] Đã chạy linter và unit test nội bộ (tất cả đều pass).
        *   [ ] Không commit các file thừa, console log hoặc secrets (`.env`).
        *   [ ] Đã bổ sung test case cho logic mới/sửa đổi.
*   **Các mục tuỳ chọn:**
    *   `Screenshots / Demo GIFs`: Bắt buộc nếu có thay đổi giao diện người dùng (UI/UX).
    *   `Breaking Changes & Migration Note`: Cảnh báo đỏ nếu thay đổi làm hỏng tương thích ngược của database hoặc API.
    *   `AI-Assisted Flag`: Checkbox xác nhận `[x] PR này có sự hỗ trợ của AI Agent (Model: ...)`.

### 4. Độ dài / mức chi tiết hợp lý
*   **File template:** 20–35 dòng Markdown (khoảng 150–250 từ).
*   **Nội dung điền thực tế trên PR:** Nửa trang màn hình (khoảng 100–300 từ). Quy tắc: Không làm mất quá 3–5 phút của người tạo PR.

### 5. Anti-pattern (điều nên tránh)
*   **Checklist mỏi mệt (Checklist Fatigue):** Đưa ra một danh sách 15–20 mục kiểm tra thủ tục hành chính. Hậu quả thực tế là lập trình viên sẽ nhắm mắt tích chọn tất cả các ô kiểm mà không đọc một chữ nào.
*   **PR khổng lồ không bối cảnh (Ghost PR):** Một PR sửa 1.500 dòng code trên 40 files nhưng phần mô tả để trống hoặc chỉ ghi vỏn vẹn "update code". Reviewer phải tự mò mẫm bản diff để suy đoán ý đồ của tác giả.

### 6. Khác biệt khi có AI agent
*   **AI tự động điền PR Template:** AI agent (như GitHub Copilot Workspace, Claude Code, Cursor) có khả năng đọc toàn bộ `git diff`, đối chiếu với commit log và tự động điền toàn bộ PR template với độ chính xác và mạch lạc vượt trội so với con người `(suy luận)`.
*   **Gắn cờ minh bạch và nâng cao cảnh giác:** PR template cần có mục khai báo việc sử dụng AI. Khi reviewer thấy PR do AI tạo, họ sẽ tập trung rà soát sâu vào các lỗ hổng bảo mật tiềm ẩn, các dependency lạ (hallucinated packages) và logic nghiệp vụ ngầm thay vì chỉ săm soi phong cách code (code style).

---

## D9. Runbook + postmortem (Google SRE, PagerDuty, …)

### 1. Các ứng viên
*   **Ứng viên A: Google SRE Runbook & Postmortem Framework**
    *   *Nguồn:* Sách *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy - Google/O'Reilly, 2016) tại [sre.google/sre-book/postmortem-culture](https://sre.google/sre-book/postmortem-culture/) và [sre.google/sre-book/example-postmortem](https://sre.google/sre-book/example-postmortem/).
    *   *Mức độ phổ biến/adoption:* Tiêu chuẩn vàng tuyệt đối của ngành công nghiệp điện toán đám mây về văn hóa vận hành tin cậy và báo cáo sự cố không quy trách nhiệm (Blameless Postmortem).
    *   *Ưu điểm:* Xây dựng văn hóa tâm lý an toàn (Psychological Safety) đỉnh cao; phân định rạch ròi giữa "Ngòi nổ kích hoạt" (Trigger) và "Nguyên nhân gốc rễ hệ thống" (Root Cause); Action Items có người chịu trách nhiệm và bug tracking cụ thể.
    *   *Nhược điểm:* Quy trình đầy đủ của Google rất sâu và đòi hỏi nhiều dữ liệu giám sát chi tiết, có thể gây quá tải cho một đội ngũ vận hành nhỏ.
*   **Ứng viên B: PagerDuty Incident Response & Postmortem Documentation**
    *   *Nguồn:* Tài liệu quy trình xử lý sự cố mở của PagerDuty (2017–2024) tại [response.pagerduty.com](https://response.pagerduty.com).
    *   *Mức độ phổ biến/adoption:* Được hàng nghìn công ty SaaS vừa và nhỏ áp dụng làm quy trình chuẩn trực chiến (on-call).
    *   *Ưu điểm:* Cực kỳ thực chiến. Thiết kế mẫu tài liệu nhằm mục đích **giảm tải nhận thức cho kỹ sư lúc 3 giờ sáng**; quy định rõ ràng về khung thời gian hoàn thành postmortem (trong vòng 5 ngày làm việc để tránh hiện tượng "khảo cổ học sự cố").
    *   *Nhược điểm:* Phần phân vai trực chiến (Incident Commander, Scribe) hơi cồng kềnh đối với team dưới 5 người.
*   **Ứng viên C: GitLab Public Runbooks Structure**
    *   *Nguồn:* Hệ thống tài liệu vận hành công khai của GitLab (2018–2024) tại [gitlab.com/gitlab-com/runbooks](https://gitlab.com/gitlab-com/runbooks) và [runbooks.gitlab.com](https://runbooks.gitlab.com).
    *   *Mức độ phổ biến/adoption:* Điển hình xuất sắc nhất thế giới về thực hành Docs-as-Code cho việc vận hành hạ tầng.
    *   *Ưu điểm:* Toàn bộ runbook được lưu dưới dạng file Markdown trong repo git, liên kết trực tiếp với Prometheus/Grafana alerts; hướng dẫn xử lý bao gồm các lệnh CLI cụ thể mà kỹ sư trực chiến có thể copy chạy ngay trong terminal.
    *   *Nhược điểm:* Cần kỷ luật rất cao để cập nhật lệnh khi hạ tầng thay đổi.

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:**
    *   **Runbook:** **GitLab Markdown Service Runbook** đặt trực tiếp tại `docs/runbooks/{service-name}.md`.
    *   **Postmortem:** **Google SRE Blameless Postmortem rút gọn** đặt tại `docs/postmortems/YYYY-MM-DD-incident-title.md`.
*   **Lý do cho team 3–10 người:**
    *   Khi sự cố xảy ra lúc nửa đêm, kỹ sư không có thời gian đọc các tài liệu lý thuyết dài dòng. Một runbook chuẩn kiểu GitLab với các dòng lệnh copy-paste được liên kết từ link cảnh báo alert là cứu cánh duy nhất `(suy luận)`.
    *   Văn hóa "Không quy trách nhiệm" (Blameless) của Google giúp team nhỏ dám nhìn thẳng vào sự thật, không giấu lỗi và tập trung vá lỗ hổng quy trình/hệ thống thay vì chỉ trích cá nhân.

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc đối với RUNBOOK:**
    1.  `Service Overview & Dashboard Links`: Dịch vụ làm gì, link trực tiếp tới Grafana dashboard và log stream trên CloudWatch/Datadog.
    2.  `Common Alerts & Step-by-Step Playbooks`: Bảng ánh xạ: Tên Alert -> Ý nghĩa triệu chứng -> Lệnh CLI chẩn đoán -> Lệnh khắc phục khẩn cấp (vd: lệnh restart pod, lệnh scale up database connection pool).
    3.  `Rollback Procedure`: Quy trình 3 bước đảo ngược bản deploy lỗi về phiên bản ổn định trước đó.
    4.  `Escalation Contacts`: Danh sách số điện thoại/handle liên hệ khẩn cấp nếu không thể tự xử lý trong 15 phút.
*   **Các mục bắt buộc đối với POSTMORTEM:**
    1.  `Incident Summary & Impact`: Tóm tắt sự cố trong 2 câu + Các chỉ số thiệt hại định lượng (Thời gian gián đoạn - Downtime, Số lượng người dùng bị ảnh hưởng, Doanh thu thất thoát nếu có).
    2.  `Timeline (UTC / Local)`: Dòng thời gian chi tiết từng phút (Thời điểm phát sinh lỗi -> Thời điểm alert kích hoạt -> Thời điểm kỹ sư vào việc -> Thời điểm khắc phục xong).
    3.  `Root Cause vs. Trigger`: Phân biệt rõ ngòi nổ (vd: do một request có payload đặc biệt) và nguyên nhân gốc rễ (hệ thống thiếu timeout và connection pool bị cạn kiệt).
    4.  `Where We Got Lucky vs. Where We Failed`: Điều gì đã diễn ra tốt (hệ thống backup hoạt động tốt) và điều gì còn kém (cảnh báo bị trễ 20 phút).
    5.  `Corrective Action Items`: Bảng các đầu việc phòng ngừa (bắt buộc: có mô tả cụ thể, có người chịu trách nhiệm chính, và có link issue ticket trên sprint backlog).
*   **Các mục tuỳ chọn:**
    *   `Supporting Graphs / Log Snippets`: Ảnh chụp đồ thị metric tại thời điểm sập hệ thống.

### 4. Độ dài / mức chi tiết hợp lý
*   **Runbook:** 1–2 trang Markdown cho mỗi microservice/hợp phần (khoảng 300–600 từ, tập trung vào code block và URL).
*   **Postmortem:** 2–3 trang Markdown (khoảng 600–1.200 từ) cho các sự cố nghiêm trọng (SEV-1/SEV-2). Hoàn thành trong vòng 3–5 ngày sau khi sự cố được khắc phục.

### 5. Anti-pattern (điều nên tránh)
*   **Postmortem quy trách nhiệm cá nhân (The Blame Game):** Ghi trong báo cáo: *"Nguyên nhân do lập trình viên Nam sơ suất gõ nhầm lệnh drop database"*. Cách tiếp cận này khiến nhân viên sợ hãi, giấu giếm sai sót và tìm cách đổ lỗi; trong khi nguyên nhân gốc rễ thực sự là tại sao hệ thống lại cho phép một lập trình viên có quyền chạy lệnh nguy hiểm trên production mà không có cơ chế xác thực kép [sre.google/sre-book/postmortem-culture](https://sre.google/sre-book/postmortem-culture/).
*   **Runbook dạng tiểu thuyết:** Viết runbook bằng các đoạn văn dài miêu tả nguyên lý hoạt động thay vì các bước thao tác cụ thể. Lúc hệ thống gặp sự cố, không ai có khả năng đọc hiểu lý thuyết.

### 6. Khác biệt khi có AI agent
*   **Agent tổng hợp Timeline Postmortem:** Việc lập timeline trong postmortem thường mất nhiều thời gian nhất. AI agent có thể quét toàn bộ log chat trên kênh cứu sự cố (Slack/Discord), commit log của git và alert history của hệ thống giám sát để tự động phác thảo một timeline chính xác đến từng giây `(suy luận)`.
*   **Agent thực thi Runbook tự động (AI SRE Assistant):** Runbook viết bằng Markdown chuẩn chỉ là đầu vào hoàn hảo để AI on-call agent có thể hỗ trợ kỹ sư trực chiến: Agent đọc runbook, tự chạy các lệnh kiểm tra chẩn đoán an toàn (read-only diagnostics) và báo cáo tóm tắt tình hình cho kỹ sư quyết định xử lý.

---

## D10. Chính sách bảo mật + sử dụng AI agent (SECURITY.md, AI usage policy …)

### 1. Các ứng viên
*   **Ứng viên A: GitHub Standard SECURITY.md + OpenSSF Best Practices**
    *   *Nguồn:* Chuẩn mực của GitHub Docs (2019–2024) tại [docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository) và Open Source Security Foundation (OpenSSF) tại [openssf.org](https://openssf.org).
    *   *Mức độ phổ biến/adoption:* Tiêu chuẩn bảo mật kho lưu trữ phổ biến nhất toàn cầu. Được tích hợp trong công cụ quét OpenSSF Scorecard để đánh giá mức độ tin cậy của mã nguồn mở.
    *   *Ưu điểm:* Cung cấp quy trình báo cáo lỗ hổng có trách nhiệm (Responsible Vulnerability Disclosure); hỗ trợ kích hoạt tính năng báo cáo bảo mật riêng tư (GitHub Private Vulnerability Reporting).
    *   *Nhược điểm:* Thuần túy là chính sách bảo mật truyền thống cho dự án, hoàn toàn chưa có quy định về việc sử dụng AI coding agent.
*   **Ứng viên B: Linux Foundation Generative AI Policy**
    *   *Nguồn:* Chính sách chính thức của The Linux Foundation (2023–2024) tại [linuxfoundation.org/legal/generative-ai-policy](https://www.linuxfoundation.org/legal/generative-ai-policy).
    *   *Mức độ phổ biến/adoption:* Chuẩn mực pháp lý hàng đầu cho các dự án mã nguồn mở toàn cầu về việc đóng góp code do AI sinh ra.
    *   *Ưu điểm:* Quy định cực kỳ chặt chẽ về sở hữu trí tuệ (IP), bản quyền mã nguồn của các công cụ AI, và trách nhiệm pháp lý của người đóng góp khi sử dụng AI.
    *   *Nhược điểm:* Viết dưới góc nhìn pháp chế doanh nghiệp (legal language), khá khô khan và thiếu hướng dẫn thao tác an toàn kỹ thuật hàng ngày cho kỹ sư.
*   **Ứng viên C: OWASP Top 10 for LLM Applications & AI Governance Guidelines**
    *   *Nguồn:* Dự án cộng đồng của OWASP Foundation (2023–2025) tại [owasp.org/www-project-top-10-for-large-language-model-applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/).
    *   *Mức độ phổ biến/adoption:* Tiêu chuẩn an ninh ứng dụng hàng đầu thế giới về các rủi ro bảo mật liên quan đến Mô hình Ngôn ngữ Lớn (Prompt Injection, Rò rỉ dữ liệu nhạy cảm, Package Hallucination).
    *   *Ưu điểm:* Cung cấp các góc nhìn kỹ thuật sâu sắc về những hiểm họa an ninh mới xuất hiện khi đưa AI vào quy trình phát triển phần mềm.
    *   *Nhược điểm:* Khối lượng kiến thức lớn, cần được cô đọng thành các quy tắc vận hành thực tế cho team nhỏ.

### 2. Chọn template nền khuyến nghị
*   **Lựa chọn:** **Bộ đôi tài liệu thực dụng: `SECURITY.md` (chuẩn GitHub/OpenSSF) kết hợp `AI_USAGE_POLICY.md` (tổng hợp tinh gọn từ OWASP LLM và Linux Foundation)**.
*   **Lý do cho team 3–10 người:**
    *   `SECURITY.md` đặt ở root hoặc `.github/` là chuẩn mực tự động giúp các công cụ quét bảo mật nhận diện kênh liên hệ khẩn cấp.
    *   Một team nhỏ đang ứng dụng AI agent bắt buộc phải có một chính sách sử dụng AI minh bạch nhằm ngăn chặn rủi ro rò rỉ dữ liệu khách hàng (PII) và rủi ro bản quyền mã nguồn `(suy luận)`.

### 3. Các mục bắt buộc và tuỳ chọn
*   **Các mục bắt buộc đối với SECURITY.md:**
    1.  `Supported Versions`: Bảng các phiên bản phần mềm đang được duy trì và nhận bản vá bảo mật.
    2.  `Reporting a Vulnerability`: Kênh liên hệ an toàn, bí mật (Email chuyên dụng hoặc kích hoạt GitHub Private Vulnerability Reporting; nghiêm cấm mở public issue để báo lỗi bảo mật).
    3.  `Response & Resolution SLA`: Cam kết thời gian phản hồi (vd: xác nhận trong vòng 48 giờ, cung cấp bản vá trong vòng 7–14 ngày tùy độ nghiêm trọng).
*   **Các mục bắt buộc đối với AI_USAGE_POLICY.md:**
    4.  `Data Privacy & Sensitive Code Boundaries`:
        *   Nghiêm cấm tuyệt đối việc đưa API keys, mật khẩu, database credentials hoặc thông tin nhận dạng cá nhân của khách hàng (PII) vào prompt của bất kỳ công cụ AI nào.
        *   Chỉ được phép sử dụng các công cụ AI có cam kết bảo vệ dữ liệu doanh nghiệp (Enterprise Tier không dùng dữ liệu người dùng để huấn luyện mô hình).
    5.  `The Human Accountability Principle (Con người chịu trách nhiệm cuối cùng)`: Mọi dòng code do AI sinh ra phải được kỹ sư con người review, hiểu rõ và chịu trách nhiệm 100% về chất lượng cũng như lỗi bảo mật phát sinh; không chấp nhận lý do "do AI viết".
    6.  `Prohibited Autonomous Actions`:
        *   Cấm AI agent tự động merge code vào nhánh `main`/`production` mà không có con người phê duyệt (Human-in-the-loop).
        *   Cấm AI tự ý bổ sung các thư viện bên thứ ba mà chưa qua bước kiểm tra an toàn (chống rủi ro Dependency Confusion / Package Hallucination).
*   **Các mục tuỳ chọn:**
    *   `List of Pre-approved AI Tools`: Danh sách các công cụ được phê duyệt chính thức (vd: GitHub Copilot Enterprise, Cursor, Claude Code).
    *   `Copyright & Licensing Notice`: Hướng dẫn kiểm tra giấy phép mã nguồn mở (Apache 2.0, MIT) đối với các đoạn code AI sinh ra.

### 4. Độ dài / mức chi tiết hợp lý
*   **`SECURITY.md`:** 1 trang màn hình (khoảng 200–400 từ).
*   **`AI_USAGE_POLICY.md`:** 1–2 trang Markdown (khoảng 400–800 từ). Ngắn gọn, thực tế, mọi kỹ sư đều có thể đọc và nắm bắt trong 10 phút.

### 5. Anti-pattern (điều nên tránh)
*   **Báo lỗi bảo mật công khai (Public Bug Reporting):** Yêu cầu người dùng báo lỗi bảo mật bằng cách mở một GitHub Issue công khai. Điều này tạo điều kiện cho tin tặc khai thác lỗ hổng ngay trước khi đội ngũ kịp tung ra bản vá [github.com](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository).
*   **Thả nổi hoàn toàn (Unrestricted Vibe Coding):** Lập trình viên để AI tự do cài đặt các gói phụ thuộc không tồn tại hoặc các gói độc hại giả mạo (Typosquatting / Package Hallucination) rồi đẩy thẳng lên production mà không qua bất kỳ khâu kiểm duyệt nào.
*   **Cấm đoán cực đoan (Luddite Policy):** Ban hành chính sách cấm 100% AI. Hậu quả là kỹ sư vẫn sẽ lén lút sử dụng trên máy cá nhân và copy-paste code vào các tài khoản AI miễn phí không an toàn, làm tăng nguy cơ rò rỉ dữ liệu doanh nghiệp gấp nhiều lần `(suy luận)`.

### 6. Khác biệt khi có AI agent
*   **Nạp chính sách vào System Prompt:** Chính sách sử dụng AI không chỉ để trên giấy cho người đọc, mà các ràng buộc bảo mật (vd: "Không đọc file `.env`", "Không commit secret") bắt buộc phải được tóm tắt và đưa trực tiếp vào file `AGENTS.md` để agent tự tuân thủ ngay trong quá trình hoạt động `(suy luận)`.
*   **AI làm chốt chặn bảo mật:** Tận dụng chính các agent chuyên trách bảo mật để thực hiện Static Application Security Testing (SAST), quét lỗ hổng phụ thuộc và kiểm tra rà soát toàn bộ code do AI khác sinh ra trước khi tạo Pull Request.

---

## D11. (Tuỳ chọn) Đánh giá mở rộng: Tài liệu thường thiếu vs. Tài liệu không đáng làm

### 1. Hai loại tài liệu team nhỏ THƯỜNG THIẾU mà NÊN CÓ
1.  **Tài liệu Khởi tạo Môi trường Cục bộ & Đóng góp (`DEVELOPMENT.md` hoặc `CONTRIBUTING.md` kèm `.env.example` chuẩn chỉ):**
    *   *Thực trạng:* Các team 3–10 người thường mắc bẫy "ngồi cạnh nhau chỉ miệng". Kỹ sư cũ cài cắm môi trường qua nhiều tháng nên không nhớ hết các phụ thuộc ẩn, dẫn đến việc tuyển một kỹ sư mới mất 3–5 ngày chỉ để khởi động được ứng dụng trên máy cục bộ.
    *   *Tại sao cần thiết trong kỷ nguyên AI:* AI coding agent không thể "hỏi miệng" đồng nghiệp. Nếu codebase không có một file hướng dẫn khởi tạo môi trường rõ ràng, không có file `.env.example` đầy đủ các biến mẫu và một lệnh duy nhất để chạy toàn bộ stack cục bộ (như Docker Compose), AI agent sẽ hoàn toàn tê liệt trong việc chạy thử và tự sửa lỗi `(suy luận)`.
2.  **Từ điển Thuật ngữ Nghiệp vụ & Bản đồ Thực thể Dữ liệu (`GLOSSARY.md` hoặc `DOMAIN_MODEL.md`):**
    *   *Thực trạng:* Mỗi thành viên trong team hiểu một từ nghiệp vụ theo một nghĩa khác nhau (vd: "Customer" khác "User" thế nào, "Order" chuyển sang trạng thái "Completed" khi nào).
    *   *Tại sao cần thiết trong kỷ nguyên AI:* AI agent rất giỏi viết cú pháp nhưng hoàn toàn mù tịt về ngữ cảnh kinh doanh ngầm của công ty. Khi thiếu một tài liệu định nghĩa ngôn ngữ chung (Ubiquitous Language theo Domain-Driven Design), AI agent sẽ tự suy diễn, tự đặt tên biến và thiết kế các bảng cơ sở dữ liệu xung đột hoàn toàn với logic thực tế của sản phẩm `(suy luận)`.

### 2. Hai loại tài liệu trong D1–D10 KHÔNG ĐÁNG LÀM (hoặc nên tinh giản cực độ)
1.  **arc42 bản đầy đủ 12 chương (trong D3 - Kiến trúc tổng quan):**
    *   *Lý do không đáng làm:* Việc ngồi viết đủ 12 chương của arc42 là một gánh nặng hành chính khổng lồ đối với team 3–10 người. Trong giai đoạn phát triển nhanh, kiến trúc hệ thống thay đổi liên tục. Một tài liệu 12 chương sẽ bị lỗi thời chỉ sau 1 tháng, trở thành "tài liệu chết" gây lãng phí hàng trăm giờ công vô ích.
    *   *Giải pháp thay thế:* Chỉ duy trì duy nhất một file `docs/ARCHITECTURE.md` dài 2–3 trang với 2 biểu đồ C4 vẽ bằng Mermaid và bảng công nghệ cốt lõi.
2.  **Tài liệu Chiến lược Kiểm thử (Testing Strategy) độc lập dài hàng chục trang (trong D7):**
    *   *Lý do không đáng làm:* Không ai trong một team nhỏ mở một file Word/Confluence 30 trang về "Quy trình đảm bảo chất lượng" ra đọc trước khi viết code. Những tài liệu này chỉ mang tính chất đối phó kiểm toán.
    *   *Giải pháp thay thế:* Biến toàn bộ chiến lược kiểm thử thành **code thực thi tự động** trong cấu hình CI (ngưỡng coverage bắt buộc, linter rules) và tích hợp Definition of Done thành một checklist 5 dòng ngay trong Pull Request Template.

---

## Top 10 kết luận

1.  **Tất cả tài liệu phải sống trong repo (Docs-as-Code):** Mọi tài liệu kỹ thuật bắt buộc phải định dạng Markdown, nằm chung kho mã nguồn và được cập nhật, phê duyệt đồng thời qua Pull Request.
2.  **`AGENTS.md` là trung tâm chỉ huy duy nhất cho AI:** Thay vì phân mảnh cấu hình cho từng IDE, hãy dùng `AGENTS.md` tại thư mục gốc làm nguồn chân lý duy nhất và đồng bộ sang các công cụ khác.
3.  **Tối ưu hóa tài liệu cho AI đọc đồng nghĩa với tối ưu cho con người:** Các câu lệnh chính xác, cấu trúc logic rõ ràng và ranh giới hệ thống minh bạch giúp cả AI lẫn kỹ sư mới onboarding nhanh chóng.
4.  **Bỏ qua sơ đồ mã nguồn C4 Level 4:** Tuyệt đối không vẽ sơ đồ chi tiết class/function bằng tay; chỉ duy trì sơ đồ C4 Level 1 (Context) và Level 2 (Container) bằng mã nguồn text Mermaid.
5.  **Ghi chép những gì KHÔNG LÀM quan trọng hơn những gì ĐÃ LÀM:** Giá trị lớn nhất của ADR và Design Doc nằm ở các mục *Non-Goals* và *Considered Alternatives* nhằm chấm dứt các cuộc tranh cãi lặp lại.
6.  **Quy ước API phải được kiểm tra tự động bằng máy:** Đừng lãng phí thời gian review thủ công cú pháp API trên PR; hãy dùng linter tự động như Spectral để CI bắt lỗi vi phạm quy chuẩn thiết kế.
7.  **Chuyển dịch toàn bộ Definition of Done vào Pull Request Template:** Đưa tiêu chuẩn bàn giao thành một checklist dưới 5 mục bắt buộc phải tích chọn và pass CI trước khi merge.
8.  **Tuân thủ nghiêm ngặt văn hóa Postmortem không quy trách nhiệm (Blameless):** Lỗi của con người chỉ là triệu chứng của một hệ thống thiếu an toàn; tập trung cải tiến cơ chế tự động thay vì chỉ trích cá nhân.
9.  **Con người chịu trách nhiệm 100% cho mã nguồn của AI:** Chính sách AI phải quy định rõ nguyên tắc trách nhiệm giải trình của lập trình viên và cấm tuyệt đối AI tự ý merge code vào production.
10. **Thà có một tài liệu 1 trang được cập nhật liên tục còn hơn một tài liệu 50 trang bị bỏ hoang:** Đối với team 3–10 người, tính tinh gọn và tính cập nhật là tiêu chuẩn đạo đức số một của tài liệu kỹ thuật.

---

## Bảng chọn cuối

| Loại tài liệu | Template nền chọn | 3–6 mục bắt buộc | Độ dài hợp lý |
| :--- | :--- | :--- | :--- |
| **D1. README dự án** | Pragmatic Developer README (Make a README + Standard Readme) | 1. TL;DR & Purpose<br>2. Prerequisites<br>3. Quickstart (Local Commands)<br>4. Env Variables<br>5. Verification & Testing | 1–2 trang màn hình<br>(300–600 từ) |
| **D2. Hướng dẫn AI Agent** | AGENTS.md (Open Standard) | 1. Tech Stack & Runtime<br>2. Build/Lint/Test Commands<br>3. Code Style & Rules<br>4. Boundaries ("Never Do") | 80–200 dòng<br>(500–1.200 từ) |
| **D3. Kiến trúc tổng quan** | Pragmatic Markdown Doc (C4 Level 1 & 2 via Mermaid) | 1. System Context (C4 L1)<br>2. Container View (C4 L2)<br>3. Tech Stack Matrix<br>4. Critical Data Flows<br>5. Cross-cutting Concerns | 3–6 trang<br>(1.000–2.000 từ) |
| **D4. ADR** | MADR v3.0.0 (Minimal/Standard) | 1. Title & Status<br>2. Context & Problem<br>3. Decision Drivers<br>4. Considered Options (Pros/Cons)<br>5. Decision Outcome<br>6. Consequences | 1–2 trang/bản<br>(300–600 từ) |
| **D5. API Contract & Quy ước** | OpenAPI 3.1 + Google AIP + Spectral Linter | 1. Resource Naming (kebab-case)<br>2. Field Casing<br>3. HTTP Verbs & Status Codes<br>4. Error Envelope (RFC 7807)<br>5. Pagination Standards | 2–3 trang quy ước<br>+ File `.spectral.yaml` |
| **D6. Spec / Design Doc / RFC** | Pragmatic Google Design Doc (Mini-Design Doc) | 1. Context & Problem<br>2. Goals & Non-Goals<br>3. Proposed Architecture<br>4. Alternatives Considered<br>5. Rollout & Rollback Plan | 2–4 trang<br>(800–1.500 từ) |
| **D7. Test Strategy + DoD** | Practical Test Pyramid + Executable CI DoD Checklist | 1. Test Layers (Unit/Integration/E2E)<br>2. Meaningful Coverage Target<br>3. Automated DoD Checklist (Compile, Tests, Linter, Security) | 1–2 trang<br>(400–800 từ) |
| **D8. Pull Request Template** | Conventional PRs + Lean Quality Checklist | 1. Title (Conventional format)<br>2. Summary of Changes<br>3. Why / Context<br>4. Verification Steps<br>5. Pre-Merge Checklist | 20–35 dòng template<br>(100–300 từ khi điền) |
| **D9. Runbook & Postmortem** | GitLab Runbook + Google SRE Blameless Postmortem | **Runbook:** 1. Dashboards, 2. Common Alerts & CLI Commands, 3. Rollback Steps<br>**Postmortem:** 1. Impact, 2. Timeline, 3. Root Cause vs Trigger, 4. Action Items | **Runbook:** 1–2 trang<br>**Postmortem:** 2–3 trang |
| **D10. Bảo mật & Chính sách AI** | GitHub SECURITY.md + AI_USAGE_POLICY.md (OWASP/Linux Foundation) | 1. Vulnerability Reporting & SLA<br>2. Supported Versions<br>3. Data Privacy Boundaries<br>4. Human Accountability<br>5. Prohibited Autonomous Actions | **SECURITY:** 1 trang<br>**AI POLICY:** 1–2 trang |
| **D11. Tài liệu bổ trợ (Thiếu)** | Local Dev Quickstart (`DEVELOPMENT.md`) & Domain Glossary | 1. Local Stack Architecture<br>2. Seed Data Instructions<br>3. Ubiquitous Language Glossary<br>4. Entity Relationships | 2–3 trang<br>(600–1.200 từ) |

---

## Điều chưa chắc

1.  **Mức độ ổn định lâu dài của chuẩn `AGENTS.md`:** Dù `AGENTS.md` đang nhận được sự ủng hộ rộng rãi từ cộng đồng mã nguồn mở và nhiều công cụ (Aider, Zed, Cursor, Codex), cuộc chiến định dạng cấu hình AI giữa các "ông lớn" công nghệ (như Microsoft với Copilot, Anthropic với Claude Code, Anysphere với Cursor) vẫn đang tiếp diễn và có thể dẫn đến các chuẩn phân mảnh mới trong tương lai.
2.  **Khả năng tự động hóa 100% việc thực thi Runbook của AI Agent:** Mặc dù AI agent có thể đọc và hiểu rất tốt các lệnh trong Runbook dạng Markdown, mức độ tin cậy để cấp quyền cho AI agent tự động chạy các lệnh khắc phục sự cố nghiêm trọng (remediation commands) trên hạ tầng production mà không cần sự phê duyệt của con người (Human-in-the-loop) hiện nay vẫn tiềm ẩn rủi ro rất cao về an toàn vận hành `(suy luận)`.
3.  **Công cụ tự động hóa kiểm tra tính nhất quán giữa Code và Architecture:** Mặc dù việc dùng Spectral để kiểm tra OpenAPI hay linter kiểm tra cú pháp mã nguồn đã rất hoàn thiện, các công cụ tự động để phát hiện sự sai lệch giữa biểu đồ kiến trúc C4/Mermaid và cấu trúc thư mục code thực tế vẫn còn ở giai đoạn sơ khai và chủ yếu dựa vào việc rà soát thủ công của con người qua PR.

---

## Nguồn

*   **D1 (README):**
    *   Richard Littauer. (2016). *Standard Readme Specification*. [https://github.com/RichardLitt/standard-readme](https://github.com/RichardLitt/standard-readme)
    *   Danny Guo. (2017). *Make a README*. [https://www.makeareadme.com](https://www.makeareadme.com)
    *   GitHub. (2016–2024). *About READMEs - GitHub Docs*. [https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
*   **D2 (AI Agent Instructions):**
    *   Agents.md Community. (2024–2025). *AGENTS.md: A README for AI Agents*. [https://agents.md](https://agents.md)
    *   Anthropic. (2024–2025). *Claude Code Documentation & Memory Management*. [https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)
    *   Cursor / Anysphere. (2024–2025). *Rules for AI - Cursor Docs*. [https://docs.cursor.com/context/rules-for-ai](https://docs.cursor.com/context/rules-for-ai)
*   **D3 (Architecture Documentation):**
    *   Dr. Peter Hruschka, Dr. Gernot Starke. (2005–2024). *arc42: Template for documentation of software and system architecture*. [https://arc42.org](https://arc42.org) & [https://github.com/arc42/arc42-template](https://github.com/arc42/arc42-template)
    *   Simon Brown. (2018). *The C4 model for visualising software architecture*. [https://c4model.com](https://c4model.com)
    *   Martin Fowler. (2015–2024). *Software Architecture Guide*. [https://martinfowler.com/architecture/](https://martinfowler.com/architecture/)
*   **D4 (Architecture Decision Records):**
    *   Michael Nygard. (2011). *Documenting Architecture Decisions*. Cognitect Blog. [https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
    *   Oliver Kopp, Olaf Zimmermann, et al. (2017–2024). *Markdown Architectural Decision Records (MADR)*. [https://adr.github.io/madr/](https://adr.github.io/madr/)
    *   Olaf Zimmermann. (2012, 2017). *Architectural Decisions in Practice & The Y-statement*. [https://ozimmer.ch](https://ozimmer.ch)
*   **D5 (API Contract & Guidelines):**
    *   OpenAPI Initiative. (2021). *OpenAPI Specification 3.1.0*. [https://spec.openapis.org/oas/v3.1.0](https://spec.openapis.org/oas/v3.1.0)
    *   Google. (2017–2024). *Google Cloud API Design Guide & AIPs*. [https://cloud.google.com/apis/design](https://cloud.google.com/apis/design) & [https://aip.dev](https://aip.dev)
    *   Stoplight. (2019–2024). *Spectral: A flexible JSON/YAML linter for OpenAPI*. [https://github.com/stoplightio/spectral](https://github.com/stoplightio/spectral)
    *   IETF. (2016). *RFC 7807: Problem Details for HTTP APIs*. [https://datatracker.ietf.org/doc/html/rfc7807](https://datatracker.ietf.org/doc/html/rfc7807)
*   **D6 (Design Docs & RFC):**
    *   Malte Ubl. (2020). *Design Docs at Google*. Industrial Empathy. [https://www.industrialempathy.com/posts/design-docs-at-google/](https://www.industrialempathy.com/posts/design-docs-at-google/)
    *   Rust Language. (2014–2024). *Rust RFC Template (0000-template.md)*. [https://github.com/rust-lang/rfcs](https://github.com/rust-lang/rfcs)
    *   Kubernetes SIG Architecture. (2018–2024). *Kubernetes Enhancement Proposals (KEPs)*. [https://github.com/kubernetes/enhancements](https://github.com/kubernetes/enhancements)
*   **D7 (Test Strategy & DoD):**
    *   Ham Vocke, Martin Fowler. (2018). *The Practical Test Pyramid*. [https://martinfowler.com/articles/practical-test-pyramid.html](https://martinfowler.com/articles/practical-test-pyramid.html)
    *   Ken Schwaber, Jeff Sutherland. (2020). *The 2020 Scrum Guide (Definition of Done)*. [https://scrumguides.org/scrum-guide.html](https://scrumguides.org/scrum-guide.html)
    *   Lisa Crispin, Janet Gregory. (2009). *Agile Testing: A Practical Guide for Testers and Agile Teams* (Agile Testing Quadrants). Addison-Wesley.
*   **D8 (Pull Request Template):**
    *   GitHub. (2016–2024). *Creating a pull request template for your repository*. [https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
    *   Conventional Commits Community. (2018–2024). *Conventional Commits Specification 1.0.0*. [https://www.conventionalcommits.org](https://www.conventionalcommits.org)
*   **D9 (Runbook & Postmortem):**
    *   Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy. (2016). *Site Reliability Engineering: How Google Runs Production Systems (Chapters 15 & 17)*. O'Reilly Media / Google. [https://sre.google/sre-book/postmortem-culture/](https://sre.google/sre-book/postmortem-culture/) & [https://sre.google/sre-book/example-postmortem/](https://sre.google/sre-book/example-postmortem/)
    *   PagerDuty. (2017–2024). *PagerDuty Incident Response Documentation & Postmortem Template*. [https://response.pagerduty.com/](https://response.pagerduty.com/)
    *   GitLab. (2018–2024). *GitLab Operations Runbooks Repository*. [https://gitlab.com/gitlab-com/runbooks](https://gitlab.com/gitlab-com/runbooks)
*   **D10 (Security & AI Policy):**
    *   GitHub. (2019–2024). *Adding a security policy to your repository (SECURITY.md)*. [https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)
    *   OpenSSF. (2020–2024). *Open Source Security Foundation Best Practices & Scorecard*. [https://openssf.org](https://openssf.org)
    *   The Linux Foundation. (2023–2024). *Generative AI Policy*. [https://www.linuxfoundation.org/legal/generative-ai-policy](https://www.linuxfoundation.org/legal/generative-ai-policy)
    *   OWASP Foundation. (2023–2025). *OWASP Top 10 for Large Language Model Applications*. [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

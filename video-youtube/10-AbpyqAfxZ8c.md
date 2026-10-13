# I Built an Agentic Software Factory with Codex and Claude Code
- Kênh: Owain Lewis
- URL: https://www.youtube.com/watch?v=AbpyqAfxZ8c
- Thời lượng: Khoảng 20:48 (ước lượng từ timestamp cuối [20:48])

## Tóm tắt (5-8 câu)
Video chia sẻ phương pháp xây dựng một "AI Software Factory" (nhà máy phần mềm điều khiển bởi AI agent) nhằm tự động hóa quy trình phát triển từ khâu tiếp nhận yêu cầu đến tạo Pull Request (PR). Tác giả nhấn mạnh kỹ thuật phần mềm cốt lõi nằm ở tư duy thiết kế hệ thống (systems thinking), trong đó AI agent chỉ phát huy tối đa hiệu quả khi được đặt vào các workflow tuần tự, rõ ràng thay vì chỉ prompt tương tác ngẫu nhiên. Để hiện thực hóa mô hình này, tác giả giới thiệu dự án mã nguồn mở "Factory" viết bằng Rust, hoạt động như một daemon liên tục theo dõi hàng đợi GitHub Issues và điều phối các tác vụ. Quy trình gồm hai giai đoạn chính: agent tự động phân tích và hoàn thiện đặc tả kỹ thuật cho ticket sơ sài (triage/spec), sau đó agent triển khai viết mã nguồn, chạy kiểm thử và review trong môi trường cô lập. Hệ thống đảm bảo an toàn bằng Git worktrees hoặc Docker sandboxes, đồng thời tối ưu hóa chi phí token nhờ cơ chế polling mang tính tất định (deterministic). Ngoài ra, các tác vụ lập lịch định kỳ (scheduled jobs) như tự động tìm kiếm lỗi (bug finder) được tích hợp để chủ động nâng cao chất lượng mã nguồn. Tác giả kết luận mô hình này tương tự như sự ra đời của CI/CD trước đây, giúp nâng cao mặt bằng chất lượng phần mềm và giải phóng lập trình viên khỏi các công việc tẻ nhạt, cơ học.

## Định nghĩa 'software factory' theo tác giả
- **Bản chất mở rộng của quy trình sẵn có**: Software factory thực chất là sự mở rộng của quy trình phát triển phần mềm chuẩn mà các kỹ sư vẫn đang thực hiện hàng ngày (từ các công ty như Google, Netflix, Amazon đến lập trình viên độc lập), bằng cách áp dụng AI agent vào từng khâu cụ thể trong quy trình thay vì can thiệp thủ công [00:46 - 01:06, 03:00 - 03:05].
- **Chuyển hóa khép kín từ ý định thành mã nguồn**: Hệ thống hóa toàn bộ chu kỳ: nhận ý định (intent từ khách hàng, PM, dev) -> đưa vào backlog -> tinh chỉnh và thiết kế -> phân rã tác vụ -> viết code, kiểm thử, code review -> mở PR -> merge và deploy [01:07 - 02:05, 08:04 - 08:18].
- **Tương đồng với CI/CD**: Tác giả xem CI/CD là một phép so sánh trực quan; nếu CI/CD tự động hóa việc đưa mã nguồn an toàn vào production mà không cần deploy thủ công, thì software factory tự động hóa chu trình tạo và kiểm thử mã nguồn từ ticket ban đầu [02:14 - 02:40, 19:56 - 20:34].
- **Cốt lõi nằm ở Workflow, không phải model**: Software factory không phụ thuộc vào việc dùng Claude Code, Codex hay mô hình nào khác vì năng lực các agent hiện nay tương đương nhau; yếu tố cốt lõi mang lại sự ổn định và nhất quán là định nghĩa quy trình từng bước (workflow definition) để agent thực thi [05:00 - 05:06, 07:11 - 07:16].

## Kiến trúc & quy trình (các bước/pipeline, có timestamp)
Hệ thống vận hành theo một vòng lặp pipeline tự động thông qua công cụ Factory daemon giám sát GitHub [08:21 - 08:29, 08:54 - 09:00]:

1. **Tiếp nhận & Tinh chỉnh tác vụ (Triage / Spec Pipeline)**:
   - [03:07 - 03:30] Tiếp nhận ticket thô ("badly defined ticket") thiếu mô tả và tiêu chí chấp nhận (acceptance criteria).
   - [09:45 - 09:55] Người dùng hoặc hệ thống gắn nhãn kích hoạt (ví dụ: `factory: ready-for-spec`).
   - [10:05 - 10:20] Daemon Factory phát hiện nhãn, tạo một Git worktree mới và ủy quyền tác vụ cho agent (như Codex).
   - [10:32 - 10:55, 11:39 - 12:00] Agent chạy workflow triage: quét codebase, tái hiện lỗi, hoàn thiện ticket theo khuôn mẫu chuẩn (mục tiêu, ngữ cảnh, tiêu chí nghiệm thu) để sẵn sàng triển khai.
2. **Triển khai mã nguồn (Implementation Pipeline)**:
   - [12:28 - 12:35] Con người xác nhận ticket đạt yêu cầu và gắn nhãn (ví dụ: `factory: ready-to-implement`).
   - [10:59 - 11:27, 12:46 - 12:55] Daemon phát hiện nhãn, kích hoạt agent triển khai. Agent dùng GitHub CLI kéo issue về, tạo nhánh/worktree cô lập và bắt đầu viết mã.
   - [05:08 - 05:27, 18:21 - 18:42] Agent chạy độc lập từ 20 đến 35 phút (thậm chí 1 tiếng cho task lớn) qua các bước: lập kế hoạch thay đổi -> viết code -> chạy unit/integration tests -> chạy browser testing (nếu là UI) -> chạy sub-agent code review -> commit theo chuẩn Conventional Commits -> chờ kiểm tra CI và tự sửa lỗi nếu có.
3. **Mở Pull Request & Bàn giao**:
   - [04:09 - 04:14, 06:17 - 06:20, 07:20 - 07:28] Agent tạo Pull Request trên GitHub, đính kèm kết quả review (ví dụ Codex duyệt "thumbs up") và bàn giao lại cho kỹ sư người thật xem xét lần cuối trước khi squash merge.
4. **Tác vụ lập lịch định kỳ (Scheduled Workflows)**:
   - [16:41 - 17:10] Cấu hình các công việc chạy tự động theo lịch (hoặc trigger thủ công) qua file `config.toml`, được quản lý phiên bản (version controlled).
   - [17:33 - 18:00] Ví dụ workflow `bug finder`: định kỳ tạo Git worktree, rà soát toàn bộ codebase tìm lỗi tiềm ẩn, sau đó tự tạo issue chi tiết hoặc tự mở PR sửa lỗi.

## Vai trò agent & con người
- **Vai trò của AI Agent**:
  - Đóng vai trò là "công nhân" (workers) xử lý các tác vụ thực thi cơ học, tẻ nhạt mà lập trình viên không thích làm (vá lỗi nhỏ, nâng cấp bảo mật, sửa tài liệu) [19:42 - 19:52].
  - Tự động triage, điều tra lỗi trong mã nguồn và điền đầy đủ thông số kỹ thuật cho ticket [11:45 - 12:00].
  - Thực thi độc lập các chuỗi công việc dài (20 - 60 phút): tự viết code, tự kiểm thử, tự review chéo (sub-agent review) và tự phản hồi sửa lỗi theo CI [05:20 - 05:27, 15:31 - 15:37, 18:34 - 18:42].
- **Vai trò của Con người (Kỹ sư / Tech Lead)**:
  - Giữ vai trò tư duy hệ thống và thiết kế hệ thống (systems thinking & systems design) [00:20 - 00:24, 06:26 - 06:31].
  - Tập trung vào khâu lập kế hoạch (planning), kiến trúc cấp cao và viết đặc tả ban đầu [06:26 - 06:31].
  - Điều phối dòng chảy công việc (coordination) thông qua nhãn hoặc bảng task, xác định việc nào nên giao cho agent và việc nào cần con người tương tác trực tiếp [12:52 - 12:56, 15:07 - 15:24].
  - Giữ tư duy phản biện (critical thinking) và đóng vai trò người gác cổng (gatekeeper): xem xét kỹ lưỡng PR, phán đoán kỹ thuật và ra quyết định merge cuối cùng [06:17 - 06:20, 19:30 - 19:37].

## Công cụ / stack được nêu
- **Nền tảng & Công cụ tự phát triển**:
  - `Factory`: Ứng dụng daemon mã nguồn mở được tác giả viết bằng ngôn ngữ **Rust** [07:51 - 07:56], quản lý vòng lặp và kích hoạt agent.
  - `Neo`: Coding agent riêng do tác giả tự xây dựng [05:32 - 05:36].
  - Định nghĩa Workflow / Skills: `task to PR` [04:40], `plan` [06:35], `bug finder` [16:46].
  - Cấu hình hệ thống: `config.toml` dùng để quản lý phiên bản cho các workflow và lịch trình tự động [16:53 - 17:08].
- **AI Models & Nền tảng Agent**:
  - **Codex** (OpenAI) [07:08, 07:24, 10:16]
  - **Claude Code** (Anthropic) [07:07]
  - **Pi** [07:08]
  - Claude routines, Codex automations [16:58 - 17:01]
- **Hệ sinh thái Quản lý & CI/CD**:
  - **GitHub**: GitHub Issues (quản lý backlog/tác vụ), GitHub Labels (cơ chế kích hoạt trigger), GitHub CLI (`gh`) [11:11], GitHub Actions [15:48 - 15:57].
- **Môi trường & Cơ chế cách ly (Isolation)**:
  - **Git worktrees**: Tạo thư mục làm việc phân nhánh cách ly nhanh cho từng agent chạy trên máy cục bộ hoặc server [05:08, 09:05 - 09:12, 13:41 - 13:43].
  - **Docker sandboxes / Docker containers**: Cơ chế sandbox cách ly an toàn khi chạy trên máy ảo (VM) / production [09:19 - 09:20, 13:51 - 13:55].
  - **Virtual Machines (VM) / Cloud**: Môi trường chạy nền 24/7 để agent xử lý công việc độc lập mà lập trình viên không cần giữ máy [08:33 - 08:36, 15:51 - 15:55].
  - **Browser testing**: Công cụ tự động chạy kiểm thử trình duyệt cho giao diện web [06:03 - 06:05].

## Kiểm chứng chất lượng (test, review, gate)
- **Local & Automated Testing**: Agent phải tự chạy toàn bộ test suite cục bộ sau khi sửa code [01:43 - 01:45, 06:00].
- **Browser Testing**: Kiểm thử giao diện tự động trên trình duyệt đối với các thay đổi liên quan đến frontend/UI [06:03 - 06:05].
- **Sub-agent Code Review & CI Loop**: Sử dụng sub-agent để rà soát mã nguồn độc lập; đẩy commit theo chuẩn Conventional Commit, chờ phản hồi từ hạ tầng CI và tự động lặp lại quy trình để sửa đổi nếu phát hiện lỗi [05:20 - 05:26, 06:05 - 06:17, 18:34 - 18:42].
- **Cổng kiểm soát chuyển trạng thái (State Transition Gates)**:
  - Cổng 1 (Spec Gate): Chỉ khi ticket thô được agent triage đầy đủ ngữ cảnh và tiêu chí nghiệm thu, con người mới phê duyệt qua nhãn `ready-to-implement` [12:30 - 12:35].
  - Cổng 2 (Cấm tự merge): Trong prompt triển khai quy định nghiêm ngặt: "Do not merge or auto merge" [11:09 - 11:10].
- **Human-in-the-loop Final Gate**: Kỹ sư con người là chốt chặn cuối cùng kiểm tra toàn bộ diff trên PR và thực hiện thao tác merge thủ công [06:17 - 06:20, 07:26 - 07:28, 15:37 - 15:40].

## Rủi ro / hạn chế / lời khuyên tác giả nêu
- **Vấn đề chi phí & Tiêu hao Token**:
  - *Rủi ro*: Chạy tự động hóa liên tục có thể gây lãng phí token ngân sách lớn [14:08 - 14:13].
  - *Lời khuyên*: Thiết kế hệ thống theo hướng tất định (deterministic). Quá trình daemon quét GitHub tìm việc dùng code thuần túy, không dùng AI; chỉ khi có ticket đúng nhãn mới gọi model, giúp hệ thống tiết kiệm token tối đa dù chạy 24/7 [14:30 - 15:02].
- **Giới hạn trí tuệ của AI ("AI isn't smart enough")**:
  - *Rủi ro*: AI chưa đủ thông minh để xử lý mọi loại tác vụ phức tạp; giao phó hoàn toàn có thể dẫn đến sai lệch nghiêm trọng [15:01 - 15:07].
  - *Lời khuyên*: Không áp dụng pipeline này cho 100% công việc; lập trình viên cần chủ động tham gia ("in the loop"), chọn phương thức tương tác lặp (interactive) cho việc khó, và chỉ bàn giao cho factory các việc cơ học, rõ ràng [15:07 - 15:25, 19:38 - 19:52].
- **Rủi ro an toàn môi trường thực thi**:
  - *Rủi ro*: Agent thực thi lệnh shell có thể phá hỏng hoặc làm mất dữ liệu hệ thống [13:17 - 13:23].
  - *Lời khuyên*: Bắt buộc phải áp dụng giải pháp cách ly: dùng Git worktrees khi chạy local, và dùng Docker sandboxes/containers khi chạy trên VM/production [13:24 - 13:56].
- **Nguy cơ lạm dụng văn hóa (Cultural abuse)**:
  - *Rủi ro*: Nhóm kỹ sư có thể ỷ lại, lạm dụng đẩy mọi thứ vào pipeline và đánh mất tư duy phản biện [19:20 - 19:30].
  - *Lời khuyên*: Xây dựng văn hóa đội ngũ tôn trọng chất lượng, luôn duy trì tư duy kỹ thuật (engineering thinking) và năng lực phán đoán của con người ở mọi bước [19:23 - 19:38].
- **Giai đoạn phát triển của công cụ**: Dự án `Factory` viết bằng Rust hiện còn rất sơ khai (early stage), chưa thích hợp để áp dụng đại trà ngay lập tức [15:41 - 15:45]; tác giả khuyên người xem nên học hỏi nguyên lý hoặc tự triển khai mô hình tương tự thông qua GitHub Actions [15:45 - 15:57].

## Trích dẫn nguyên văn (5 câu, giữ tiếng gốc, kèm [mm:ss] đúng như transcript)
1. [00:46] "So, the first question is what is a software factory? And it's basically just an extension of everything we've already been doing as developers."
2. [05:33] "We're just giving the agent a task. We're defining the workflow or the steps the agent needs to run through, and then we're just letting it run."
3. [07:12] "Ultimately, the workflow is what matters. All of the agents are equally capable at this point."
4. [14:30] "But the way Factory is designed is to be largely deterministic. So, when we're polling GitHub looking for work to do, we're not wasting any tokens."
5. [19:34] "You still need human judgment. You still need engineering thinking at every single step of the process."

## Đánh giá: điểm hữu ích cho team 3-10 kỹ sư (1-5) + lý do; nội dung là demo/quảng cáo hay thực chiến?
- **Điểm hữu ích**: **4/5**
  - **Lý do**:
    - *Rất phù hợp bài toán nguồn lực team nhỏ*: Đội ngũ 3-10 kỹ sư thường xuyên quá tải bởi các công việc bảo trì nhỏ (triage phản hồi của khách hàng, sửa bug vụn, bảo mật, viết ticket). Mô hình tự động hóa ticket-to-spec và ticket-to-PR giúp giải phóng đáng kể thời gian kỹ sư để họ tập trung vào kiến trúc lõi.
    - *Tiết kiệm chi phí & An toàn*: Kiến trúc kết hợp polling tất định (deterministic polling) và cách ly bằng Git worktrees/Docker giúp team nhỏ kiểm soát chi phí token chặt chẽ và không sợ hỏng môi trường phát triển chính.
    - *(suy luận) Trừ 1 điểm*: Dự án Rust `Factory` còn ở giai đoạn rất sơ khai, chưa phải giải pháp "plug-and-play" hoàn chỉnh; việc thiết lập hạ tầng sandbox (Docker sandboxes) và quản lý agent chạy nền 30-60 phút vẫn đòi hỏi team phải có kỹ sư am hiểu về DevOps/Infra để vận hành ổn định.
- **Tính chất nội dung: Thực chiến hay Demo/Quảng cáo?**
  - **Mang tính Thực chiến & Hướng dẫn kiến trúc (Practical Architectural Guide)**.
  - Video không nhằm mục đích bán phần mềm hay quảng cáo thương mại. Tác giả chia sẻ công khai mã nguồn mở, đi sâu vào các bài toán kỹ thuật thực tế (cách ly bằng worktrees/sandboxes, phân tầng triage và implement, kiểm thử CI/CD khép kín, scheduled bug finder). Đồng thời, tác giả rất thẳng thắn chỉ ra các nhược điểm thực tế: chi phí token, hạn chế trí tuệ của AI, tính chưa hoàn thiện của Docker sandbox, và cảnh báo về văn hóa lạm dụng tự động hóa trong nhóm kỹ sư.

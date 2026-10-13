# Every Claude Code Skill I Use to Drive My Entire Development Process
- **Kênh:** Cole Medin
- **URL:** https://www.youtube.com/watch?v=MbiMwgbGdxw
- **Thời lượng ước tính:** ~23:05 (dựa trên timestamp cuối `[23:02]`)

## Tóm tắt (5-8 câu)
Tác giả Cole Medin chia sẻ rằng anh không còn tự viết bất kỳ dòng mã nào trong hơn một năm qua và đã xây dựng một quy trình phát triển hoàn chỉnh dựa hoàn toàn vào các trợ lý AI thông qua hệ thống kỹ năng (skills) tái sử dụng. Quy trình này được tinh gọn thành hai vòng lặp cốt lõi gồm Outer Loop (hoạch định cấp cao để tạo PRD, tài liệu kiến trúc kỹ thuật và phân rã epic) cùng Inner Loop (thực thi từng ticket thông qua priming, planning, implementation và validation). Trọng tâm mang tính đột phá của hệ thống là chiến lược "Validation-First" (Test-Driven Development dành cho agent), trong đó chiến lược kiểm thử toàn diện và tiêu chí hoàn thành được định nghĩa chi tiết trước khi sinh code. Nhờ có khung kiểm thử sẵn sàng, agent có thể tự vận hành test, tự phát hiện lỗi và lặp lại việc sửa code mà không phụ thuộc vào sự can thiệp liên tục của con người hay tạo ra "AI slop". Để khắc phục hiện tượng suy giảm nhận thức do quá tải ngữ cảnh ("context rot" / "dumb zone") của LLM, tác giả tách biệt nghiêm ngặt các giai đoạn lập kế hoạch và viết code vào các phiên hội thoại độc lập. Toàn bộ các skill được đóng gói tối giản dưới dạng plugin cắm-rút (plug-and-play), dễ dàng tích hợp vào Claude Code hoặc các công cụ như Cursor, Pi và Copilot mà không ép buộc người dùng phải thay đổi toàn bộ quy trình sẵn có.

## Định nghĩa 'software factory' theo tác giả
Trong toàn bộ transcript, tác giả Cole Medin **không sử dụng trực tiếp cụm từ "software factory"**. Tuy nhiên, mô hình tương đương được tác giả định nghĩa và vận hành chính là một **"vòng đời phát triển phần mềm bằng AI hoàn chỉnh" (full AI software development life cycle / AI coding workflow)** [00:13, 00:49, 00:94], hoạt động như một dây chuyền sản xuất phần mềm:
- **(suy luận)** Đây là một cỗ máy sản xuất phần mềm tự động hóa theo mô-đun, nơi con người đóng vai trò là "quản lý sản phẩm" và "người kiểm soát chất lượng ở đầu ra", chỉ định nghĩa mục tiêu ("cái gì & tại sao" - what & why) cùng tiêu chí nghiệm thu/kiểm thử ("exit criteria" / "validation strategy").
- **(suy luận)** Toàn bộ công đoạn gia công kỹ thuật ("như thế nào" - how, phân rã công việc, nạp ngữ cảnh mã nguồn, viết mã, chạy thử và sửa lỗi) được chuyển giao hoàn toàn cho các tác nhân AI thực hiện tự động thông qua các khuôn mẫu (templates) và kỹ năng (skills) được chuẩn hóa.

## Kiến trúc & quy trình (các bước/pipeline, có timestamp)
Quy trình phát triển phần mềm gồm 2 vòng lặp chính:

### 1. Outer Loop (Vòng lặp hoạch định cấp cao - chạy 1 lần mỗi Epic/Tính năng lớn) [05:29 - 12:16]
- **Tạo PRD (`plan-create-prd`)** [06:23 - 08:07, 09:46 - 10:06]:
  - Tiếp nhận ý tưởng sản phẩm ở mức tổng quan từ người dùng.
  - Agent phỏng vấn người dùng bằng hàng loạt câu hỏi để làm rõ bài toán, đối tượng người dùng mục tiêu và giả thuyết cần chứng minh; xuất ra tài liệu PRD theo template chuẩn (chỉ tập trung vào "what" và "why", không bàn cách viết code).
- **Thiết kế kiến trúc / Spec (`spec skill`)** [10:06 - 10:49]:
  - Chạy trong **phiên hội thoại tách biệt** với bước PRD để tránh lẫn lộn ngữ cảnh.
  - Agent phỏng vấn người dùng dựa trên template kiến trúc để định hình giải pháp kỹ thuật, cấu trúc triển khai ("how").
- **Phân rã Epic (`piv-slice-epic`)** [10:50 - 12:16]:
  - Nhận đầu vào là PRD và tài liệu Spec/Architecture (dưới dạng file Markdown cục bộ hoặc liên kết Confluence qua MCP server).
  - Phân tích phụ thuộc kỹ thuật, xác định các hạng mục có thể thực hiện song song, chia epic thành các ticket/issue nhỏ gọn, độc lập (dưới dạng file Markdown, Jira tickets hoặc GitHub issues).

### 2. Inner Loop (Vòng lặp thực thi - lặp lại cho từng Ticket) [12:16 - 21:21]
- **Nạp ngữ cảnh codebase (`prime-codebase`)** [12:52 - 13:43]:
  - Khám phá và nạp ngữ cảnh mã nguồn liên quan đến ticket cụ thể trước khi lập kế hoạch, giải quyết tình trạng thiếu thông tin của model khi bắt đầu phiên làm việc.
- **Lập kế hoạch chi tiết (`piv-plan-implementation`)** [13:44 - 19:12]:
  - Chạy trong **cùng phiên hội thoại** với bước `prime-codebase`.
  - Agent tiếp tục phỏng vấn người dùng để tránh đưa ra các giả định sai lầm.
  - Đọc tài liệu, xác định các file cần sửa/tạo mới, lập kế hoạch chi tiết từng tác vụ và xây dựng **chiến lược kiểm thử toàn diện (Validation Strategy / Validation-First)** gồm: unit test, integration test, edge cases, lệnh linter, type-check, và kịch bản test bằng browser automation.
- **Hiện thực hóa mã nguồn (`piv-implement`)** [19:12 - 20:13]:
  - Bắt buộc chạy trong **một phiên hội thoại hoàn toàn mới** để tránh "context rot".
  - Đầu vào duy nhất là đường dẫn tuyệt đối đến file plan vừa tạo.
  - Agent đọc kế hoạch, sinh code và tự động kích hoạt các bước kiểm thử theo kế hoạch để lặp lại việc sửa lỗi.
- **Xác thực, đánh giá & mở PR (`validate & review`)** [20:14 - 21:21]:
  - Quá trình kiểm thử tự động diễn ra lồng ghép trong bước implement (hoặc chạy skill validate riêng).
  - Con người tự thực hiện code review và manual validation (sử dụng thêm các review skills hỗ trợ).
  - Đóng ticket bằng cách mở Pull Request (PR) trên GitHub, kiểm tra lần cuối, merge vào nhánh chính và chuyển sang ticket tiếp theo.

## Vai trò agent & con người
- **Vai trò của con người:**
  - **Định hướng chiến lược (Product Owner / PM):** Cung cấp ý tưởng ban đầu, trả lời các câu hỏi phỏng vấn của agent để làm rõ yêu cầu, phạm vi và giải pháp kỹ thuật [07:43, 11:15, 14:24].
  - **Thiết lập tiêu chuẩn hoàn thành (Guardrails & Exit Criteria):** Định nghĩa kết quả mong đợi và kiểm duyệt chiến lược kiểm thử trong file plan [17:36, 18:18].
  - **Cổng kiểm duyệt chất lượng cuối (Review Gatekeeper):** Thực hiện kiểm thử thủ công bổ sung, trực tiếp review mã nguồn trên Pull Request trước khi merge [20:30 - 21:12].
  - **Chỉ đạo tùy biến:** Yêu cầu agent sửa đổi các file kỹ năng (`skill.md`) bằng ngôn ngữ tự nhiên thay vì tự tay sửa mã [22:18].
  - **Không viết code thủ công:** Hoàn toàn không tự gõ code trong suốt quá trình phát triển [00:00].
- **Vai trò của Agent:**
  - **Người phỏng vấn / Trích xuất yêu cầu:** Đặt câu hỏi có cấu trúc để khai thác toàn diện thông tin từ người dùng [07:44, 14:22].
  - **Kiến trúc sư & Quản lý phụ thuộc:** Phác thảo spec kỹ thuật, chia nhỏ khối lượng công việc và lập bản đồ phụ thuộc giữa các ticket [10:10, 11:11].
  - **Kỹ sư khảo sát ngữ cảnh:** Quét và phân tích cấu trúc codebase phù hợp với mục tiêu của ticket [12:19, 13:17].
  - **Lập trình viên tự hành (Autonomous Developer):** Viết code, tự chạy test suite, linter, type-checker và browser automation [16:25, 20:06].
  - **Tự phát hiện và sửa lỗi (Self-healing & Iteration):** Dựa vào kết quả kiểm thử để tự sửa sai lặp đi lặp lại trước khi bàn giao cho con người [17:08, 18:38].

## Công cụ / stack được nêu
- **AI Coding Assistants:** Claude Code (công cụ chính của tác giả, có hệ thống marketplace plugins) [03:12, 05:16]; Cursor, Pi, GitHub Copilot (các agent tương thích khác) [00:30, 04:33].
- **Bộ kỹ năng & Khung làm việc (Skills & Frameworks):**
  - Cole's AI skills (bao gồm: `plan-create-prd`, `spec skill`, `piv-slice-epic`, `prime-codebase`, `piv-plan-implementation`, `piv-implement`, các skill review/validate) [03:59, 07:22, 11:25, 13:05, 19:53, 20:47].
  - GitHub Spec Kit, Gastown (nhắc tới như các framework agentic cồng kềnh, thiếu linh hoạt để đối chiếu) [01:30, 01:46].
- **Công cụ kiểm thử & tự động hóa:** Unit test, Integration test, Linters, Type checkers [16:25]; Agent browser / Browser automation tools [16:35].
- **Hệ thống quản lý mã nguồn, tác vụ & tài liệu:** GitHub (quản lý repository, Issues, Pull Requests) [12:44, 20:53]; Confluence (lưu trữ PRD/Spec, truy xuất qua MCP server) [11:46, 12:04]; Jira (quản lý ticket) [11:47, 12:45]; VS Code [20:01].
- **Nền tảng hạ tầng giọng nói AI (Nhà tài trợ video):** Agora (SDK, hạ tầng mạng thời gian thực, hỗ trợ các mô hình tương thích OpenAI) [08:08 - 09:44].

## Kiểm chứng chất lượng (test, review, gate)
- **Chiến lược "Validation-First" (TDD cho AI Agent)** [16:03 - 17:23]: Toàn bộ kế hoạch kiểm thử phải được chốt trước khi viết bất kỳ dòng mã nào. Kế hoạch này là một hợp đồng ràng buộc bao gồm unit test, integration test, kiểm tra edge case, linter, type-check và kịch bản giả lập hành vi người dùng qua browser automation.
- **Vòng lặp tự kiểm thử và sửa lỗi khép kín (Self-Correction Loop)** [17:08 - 17:23, 18:38]: Agent không trả lại kết quả viết code ở lượt đầu tiên (first pass). Nó sử dụng bộ kiểm thử làm giá đỡ (harness) để tự chạy, tự bắt lỗi và tự điều chỉnh code liên tục cho đến khi vượt qua toàn bộ tiêu chí nghiệm thu ("let the model cook").
- **Cổng phân tách phiên làm việc (Context Gate chống Context Rot)** [19:20 - 19:50]: Ngăn chặn việc mô hình bị quá tải thông tin bằng cách đóng phiên planning dài dòng và khởi tạo phiên hội thoại mới tinh cho bước implement, chỉ nạp đúng duy nhất file plan làm chỉ dẫn.
- **Cổng phê duyệt con người (Human Gate & Code Review)** [20:26 - 21:12]: Tác giả nhấn mạnh không bao giờ coi output của AI là hoàn hảo 100%. Con người bắt buộc phải tự rà soát code, kiểm thử thủ công và thực hiện quy trình review chính thống trên GitHub Pull Request trước khi merge vào codebase chính.

## Rủi ro / hạn chế / lời khuyên tác giả nêu
- **Rủi ro LLM đưa ra các giả định sai lầm tai hại:** LLM có xu hướng tự tin đưa ra những giả định rất tệ ("LLMs will confidently make terrible assumptions" [14:36]). Lời khuyên: Phải bắt buộc agent trải qua bước phỏng vấn ngược người dùng và nghiên cứu kỹ codebase trước khi lập plan.
- **Rủi ro suy thoái ngữ cảnh ("Context rot" / "Dumb zone"):** Khi ngữ cảnh hội thoại quá dài, mô hình LLM sẽ rơi vào trạng thái quá tải thông tin và xử lý kém đi rõ rệt [19:36 - 19:42]. Lời khuyên: Phải tách rời các khâu PRD, Spec và Implement vào các phiên hội thoại riêng biệt.
- **Hạn chế của các framework nguyên khối (Gastown, GitHub Spec Kit):** Các framework này bắt buộc người dùng phải tuân thủ 100% quy trình định sẵn của họ, khó áp dụng vào các dự án sẵn có [01:30 - 01:59]. Lời khuyên: Nên dùng các skill tối giản, độc lập và cắm-rút (plug-and-play) để dễ dàng tích hợp vào quy trình hiện tại.
- **Nguy cơ sinh mã rác ("AI slop") khi thiếu kiểm thử:** Nếu để agent code tự do mà không có khung kiểm thử trước, kết quả trả về thường kém chất lượng [17:17]. Lời khuyên: Xác định rõ điểm kết thúc (the end / exit criteria / validation), để model tự tìm phương thức thực hiện (the means) thay vì can thiệp vi mô [18:18 - 18:28].
- **Lời khuyên về tùy biến:** Đừng bao giờ tự tay gõ lại hoặc chỉnh sửa thủ công các file kỹ năng (`skill.md`); hãy mô tả yêu cầu bằng ngôn ngữ tự nhiên để chính agent thực hiện sửa đổi [22:18].

## Trích dẫn nguyên văn (5 câu, giữ tiếng gốc, kèm [mm:ss] đúng như transcript)
1. `[00:00]` "I haven't written a single line of code myself in over a year now"
2. `[14:36]` "Because LLMs will confidently make terrible assumptions."
3. `[16:49]` "So I call it Test Driven Development, but for agents."
4. `[18:02]` "He said you want to describe the task, you want to describe the guardrails and the exit criteria, including the validation, and then just let the model cook and come back in a little bit."
5. `[19:36]` "We want to avoid context rot because large language models have a dumb zone where they get overwhelmed with information, just like people do."

## Đánh giá: điểm hữu ích cho team 3-10 kỹ sư (1-5) + lý do; nội dung là demo/quảng cáo hay thực chiến?
- **Điểm hữu ích cho team 3-10 kỹ sư:** **4.5 / 5**
  - **Lý do:**
    - **Tính linh hoạt và khả năng cắm rút:** Khác với các framework cồng kềnh ép buộc thay đổi toàn bộ SDLC, bộ skill này cho phép team nhỏ tích hợp từng phần (như khâu tạo PRD hoặc khâu lập plan kiểm thử) vào quy trình hiện tại mà không gây xáo trộn.
    - **Giải quyết bài toán kiểm soát chất lượng:** Khái niệm "Validation-First" (ép agent viết test plan, chạy test và tự fix trước khi submit) giúp giải quyết triệt để vấn đề "AI slop" và lỗi ngầm khi nhiều kỹ sư cùng sử dụng AI sinh code.
    - **Tương thích với các công cụ cộng tác nhóm:** Quy trình hỗ trợ liên kết với Confluence qua MCP, phân bổ task thành Jira/GitHub issues và kết thúc bằng Pull Request chuẩn mực, rất phù hợp cho team 3-10 người cần kiểm soát qua code review.
    - **Điểm trừ nhỏ:** Chưa đạt 5/5 vì video không demo trực tiếp việc chạy code và sửa lỗi thực tế trong terminal từ đầu đến cuối mà chỉ giải thích luồng; đồng thời phương pháp này đòi hỏi codebase của team phải có sẵn nền tảng kiểm thử (test suite, linter, CI) đủ tốt thì agent mới có thể tự xác thực hiệu quả.
- **Bản chất nội dung (Demo / Quảng cáo / Thực chiến):**
  - **Mang tính Thực chiến cao (Battle-tested methodology):** Đây là kinh nghiệm đúc kết từ hơn nửa năm làm việc thực tế của một cựu kỹ sư không còn tự gõ code. Các vấn đề cốt lõi được nêu (như `context rot`, `dumb zone`, sự nguy hiểm của các giả định sai từ LLM, cơ chế phân tách conversation) đều là những bài toán thực chiến mà bất kỳ ai ứng dụng AI coding sâu đều gặp phải.
  - Video có chứa 1 phân đoạn quảng cáo tài trợ từ `[08:08]` đến `[09:44]` cho nền tảng Agora, nhưng phần còn lại hoàn toàn tập trung vào việc chia sẻ kiến trúc quy trình, triết lý TDD cho agent và hướng dẫn sử dụng bộ plugin nguồn mở phục vụ công việc lập trình thực tế.

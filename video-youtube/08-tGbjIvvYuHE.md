# How to Build a Software Factory for AI Coding Agents
- **Kênh:** Boundary and HumanLayer (Podcast *AI that works*, người dẫn: Dex – HumanLayer và Vibh – Boundary ML)
- **URL:** https://www.youtube.com/watch?v=tGbjIvvYuHE
- **Thời lượng:** ~70 phút 44 giây (ước từ timestamp cuối [70:44])

---

## Tóm tắt (5-8 câu)
1. Video là buổi đối thoại chuyên sâu giữa Dex (CEO HumanLayer) và Vibh (Đồng sáng lập Boundary ML) về các mẫu thiết kế kiến trúc "nhà máy phần mềm" (software factory) nhằm đưa AI coding agent vào quy trình kỹ thuật thực tế thay vì chỉ dừng ở các bản demo.
2. Hai tác giả mổ xẻ sự đánh đổi giữa hai thái cực tự xây dựng toàn bộ in-house (Build) và mua giải pháp trọn gói từ nhà cung cấp cloud (Buy), từ đó nhấn mạnh tầm quan trọng của tính module hóa (composition) cho phép kỹ sư tự do tích hợp các khối hệ thống mở.
3. Cấu trúc một software factory doanh nghiệp được chia tách thành 4 tầng rõ rệt: Hạ tầng tính toán (Compute), Môi trường phát triển (Dev Environment), Bộ khung agent (Inner/Outer Harness) và Mặt phẳng điều phối (Control Plane / Orchestration).
4. Boundary minh họa ca thực chiến "Agent Tries BAML" (ATB) vận hành trên cụm máy MacBook in-house: tiếp nhận phản hồi lỗi từ người dùng, coi phản hồi là không đáng tin cậy để tự sinh kịch bản tái hiện (repro), phân loại độ khó, chạy vòng lặp sửa lỗi tự động cùng bot review và tự điều phối merge queue.
5. Về phía phát triển tính năng, Dex chia sẻ quy trình xây dựng mockup PRD, để các model tranh luận và viết mã thâu đêm tạo ra các bản PR thô ("slop PR"), rồi dùng chính agent để cắt nhỏ thành các PR gọn nhẹ 1.000 – 3.000 dòng giúp con người dễ dàng review và kiểm soát kiến trúc.
6. Kết luận then chốt của buổi chia sẻ là loại bỏ ảo tưởng xây dựng hệ thống tự động hóa 100%, thay vào đó tập trung vào mục tiêu tự động hóa khoảng 95%, duy trì con người làm "người chăn dắt" (shepherd) và chốt chặn phê duyệt cuối cùng (gatekeeper) trước khi đưa mã vào nhánh chính.

---

## Định nghĩa 'software factory' theo tác giả
Theo Dex và Vibh [00:00 - 00:04, 22:10 - 22:35, 60:44 - 60:52]:
- **Khái niệm cốt lõi:** Bắt đầu từ quy trình phát triển phần mềm truyền thống nơi kỹ sư con người trực tiếp xây dựng ("human builds the thing"), sau đó hoán đổi mắt xích này bằng hệ thống các AI agent tự động xây dựng ("agent builds the thing"), tự động chạy kiểm thử và nhận phản hồi khép kín ("agent test the thing and getting feedback").
- **Bản chất hệ thống:** Software factory không đơn thuần là một công cụ sinh mã dòng lệnh riêng lẻ, mà là một hệ thống dây chuyền tích hợp gồm các khối giao diện mở (building blocks) kết nối từ khâu tiếp nhận yêu cầu/báo lỗi, tạo môi trường thực thi cô lập, gọi agent xử lý vòng lặp sửa lỗi, chạy CI/CD và liên tục cải tiến chính sản phẩm (tương tự như cách Boundary xây dựng *Agent Tries BAML* để tự động nâng cấp ngôn ngữ lập trình BAML).
- **Tính lắp ghép (Compositionality):** Tác giả định nghĩa đây là một cấu trúc phân tầng nơi kỹ sư có thể tùy biến linh hoạt việc "Build" (tự quản lý compute, sandbox, dev environment) hoặc "Buy" (mua harness hoặc orchestration plane) tùy theo nhu cầu bảo mật và tính phức tạp của hệ thống nội bộ [56:55 - 57:22].

---

## Kiến trúc & quy trình (các bước/pipeline, có timestamp)

### 1. 4 Tầng kiến trúc của Software Factory [28:40 - 29:45, 33:50 - 41:15]
- **Tầng 1: Hạ tầng tính toán (Compute / Sandbox Isolation) [22:48 - 24:00, 32:57 - 33:35]:**
  - Cung cấp môi trường thực thi an toàn, cô lập cho agent.
  - *Lựa chọn in-house:* Boundary dùng trực tiếp cụm MacBook và Mac mini đặt tại văn phòng vì máy có sẵn cấu hình, không tốn thời gian boot máy và chi phí rẻ.
  - *Lựa chọn Cloud / Vendor:* Sử dụng EC2, cụm Kubernetes tự quản trị, hoặc mua sandbox từ Daytona, E2B (ETP), Freestyle.
  - *Mô hình Pet vs Cattle [42:27 - 45:30]:* Môi trường MacBook hiện tại của Boundary mang tính chất "Pet" (cấu hình sẵn cố định), trong khi hướng đi dài hạn cho dev environment là "Cattle" (tạo máy ảo/container theo nhu cầu và xóa bỏ khi xong).
- **Tầng 2: Môi trường phát triển (Dev Environment) [34:06 - 36:20, 41:30 - 42:18]:**
  - Chứa runtime ngôn ngữ cụ thể (ví dụ Rust toolchain phiên bản chuẩn), bộ giả lập web preview và cơ chế cấp phát danh tính (identity provisioning, quyền truy cập API keys, quyền truy cập mạng nội bộ).
  - Đóng vai trò cầu nối giúp agent truy cập được các dịch vụ nội bộ (shared dev cloud gồm hàng chục microservices) mà không cần phải tải toàn bộ mã nguồn về sandbox.
- **Tầng 3: Bộ khung agent (Harness: Inner vs Outer Harness) [24:40 - 25:35, 36:23 - 37:25, 52:45 - 54:05]:**
  - *Inner Harness:* Công cụ agent cốt lõi thực thi câu lệnh trực tiếp (Claude Code CLI, Codex CLI, Pi, OpenCode, Devin).
  - *Outer Harness:* Vòng lặp tùy biến bọc bên ngoài do team tự phát triển (`while loop` kiểm tra điều kiện hoàn thành, cơ chế nén ngữ cảnh - context compaction, cơ chế tiêm skills, định dạng bộ nhớ).
- **Tầng 4: Mặt phẳng điều phối (Control Plane / Orchestration) [28:40 - 29:36, 40:00 - 41:07, 61:05 - 63:10]:**
  - Bộ não quản lý toàn bộ hệ thống: tiếp nhận webhook từ Linear, Slack, GitHub; điều phối hàng đợi tác vụ; lưu trữ vết thực thi (session traces); quản lý hạn mức chi phí (spend/budget) và tích hợp tri thức đội ngũ (*compounding engineering*).

---

### 2. Hai Pipeline quy trình cụ thể

#### A. Pipeline sửa lỗi & cải tiến tự động (Agent Tries BAML - Boundary) [16:08 - 21:08, 25:00 - 26:23]
1. **Tiếp nhận phản hồi (Feedback Reported) [16:16]:** Nhận báo lỗi từ người dùng hoặc agent khác. Áp dụng nguyên tắc "Zero Trust" (mọi phản hồi thô từ bên ngoài đều không đáng tin cậy).
2. **Kiểm tra phiên bản mới nhất [16:29]:** Xác định nhanh xem lỗi đã được vá trên bản release mới nhất chưa; nếu rồi thì phản hồi ngay cho user.
3. **Lọc trùng lặp (Deduplication) [16:35]:** Agent đối chiếu xem lỗi đã tồn tại kịch bản tái hiện chưa.
4. **Tạo kịch bản tái hiện chuẩn (Create Repro) [17:05]:** Đốt token nội bộ để agent tự viết mã repro cô lập. Nếu không thể tự tạo repro, hệ thống chuyển giao (escalate) sang kỹ sư con người [18:28].
5. **Phân loại độ khó (Classify Issue Difficulty) [19:35]:** Agent phân loại lỗi theo số dòng code dự kiến (dưới 60 dòng là lỗi nhỏ, trên 500 dòng là lỗi lớn/phức tạp).
6. **Lập kế hoạch hoặc Viết mã sửa lỗi [19:08]:** Nếu là lỗi phức tạp, agent lập Plan và ping người phụ trách ("shepherd") qua Slack để duyệt; nếu là lỗi nhỏ, agent tự động code bản vá.
7. **Vòng lặp kiểm thử CodeRabbit (`while loop`) [25:00]:** Agent đẩy PR lên và nhận phản hồi từ bot CodeRabbit; tự động sửa lặp lại tối đa 3 lần cho đến khi bot phê duyệt.
8. **Con người duyệt & Hàng đợi merge thông minh (Agentic Merge Queue) [25:42]:** Kỹ sư con người bấm nút chấp thuận; sau đó agent tự động quản lý nhánh, liên tục rebase/merge từ nhánh `main`, xử lý xung đột phát sinh cho đến khi toàn bộ CI/CD pass và merge thành công.

#### B. Pipeline phát triển tính năng lớn (Dex - HumanLayer) [11:08 - 15:32]
1. **Khởi tạo Spec/PRD & HTML Mockup [11:13 - 12:00]:** Con người tương tác qua lại với model để chốt định hướng giao diện và luồng nghiệp vụ.
2. **Chạy lặp thâu đêm (Overnight Model Auto Looping) [12:00 - 12:19]:** Xếp hàng loạt khoảng 15 prompts (giao việc cho Claude Code / Codex CLI cày đêm, cho các model tự đánh giá chéo và nén ngữ cảnh) tạo ra bản PR thử nghiệm khổng lồ ("slop PR").
3. **Thẩm định & Thiết kế lại kiến trúc [12:19 - 12:25, 14:08 - 14:25]:** Con người kiểm tra sản phẩm buổi sáng, quyết định kiến trúc chuẩn và yêu cầu AI tái cấu trúc từ đầu dựa trên bản mẫu.
4. **Chia tách PR thành các phần nhỏ (Digestible PRs) [12:26 - 12:40, 14:35 - 14:40]:** Yêu cầu model chia nhỏ khối mã nguồn khổng lồ (~20.000 dòng) thành chuỗi các PR độc lập từ 1.000 đến 3.000 dòng để kỹ sư trong team có thể review cẩn thận từng phần.

---

## Vai trò agent & con người

| Vai trò | Phân công nhiệm vụ cụ thể theo tác giả |
| :--- | :--- |
| **AI Agent** | - Thực thi các vòng lặp cày mã thâu đêm (overnight coding loops), tự phản biện mã nguồn.<br>- Tự sinh kịch bản tái hiện lỗi (repro) độc lập từ mô tả người dùng.<br>- Phân loại độ khó tác vụ và lọc trùng lặp lỗi.<br>- Tự sửa lỗi theo nhận xét của bot review tĩnh (CodeRabbit) trong vòng lặp kín.<br>- Vận hành hàng đợi merge (Agentic Merge Queue): tự động rebase từ `main`, giải quyết xung đột mã và theo dõi CI/CD.<br>- Hỗ trợ bóc tách các khối mã lớn thành từng pull request nhỏ. |
| **Con người** | - Thiết lập định hướng sản phẩm, yêu cầu nghiệp vụ và tương tác tạo bản thiết kế ban đầu.<br>- Đóng vai trò "Shepherd" (người chăn dắt/giám sát): can thiệp khi agent không thể tái hiện lỗi, khi tác vụ bị phân loại quá phức tạp hoặc khi vòng lặp tự sửa lỗi thất bại quá 3 lần.<br>- Định hình và kiểm soát kiến trúc hệ thống (từ chối mã nếu kiến trúc sai lệch).<br>- Giữ vai trò chốt chặn cuối cùng (Gatekeeper): bắt buộc con người phải nhấn nút phê duyệt merge (không cho phép hệ thống tự merge hoàn toàn).<br>- Xử lý các ca lỗi phụ thuộc vào nguồn dữ liệu hoặc dịch vụ bên ngoài. |

---

## Công cụ / stack được nêu
- **Mô hình AI:** OpenAI Codex (o3/Codex CLI/Terra/Soul - bí danh dùng trong buổi nói chuyện), Anthropic Claude (Opus, Sonnet/Fable).
- **Harnesses / CLI:** Claude Code (chạy chế độ headless xuất file log `JSONL`), Codex CLI, Pi, OpenCode, Devin, Cognition Outposts/Workers, Factory, Amp, OpenInspect.
- **Hạ tầng tính toán (Compute / Sandbox):** Cụm máy phần cứng in-house MacBook / Mac mini, AWS EC2, XC.dev, Daytona, E2B (ETP), cụm Kubernetes, Freestyle.
- **Nền tảng điều phối & Ngôn ngữ:** HumanLayer (multiplayer coding agent workspace), Boundary ML / BAML (ngôn ngữ lập trình chuyên biệt cho agent), Web server cục bộ (REST API) kết hợp Cloud Dispatcher.
- **Giao thức kết nối (Protocols / Interfaces):** Model Context Protocol (MCP), Agent Client Protocol (ACP), AGUI, REST API, CLI streaming JSONL.
- **Công cụ kiểm thử, Review & CI/CD:** CodeRabbit (PR review bot), GitHub Actions, GitHub Merge Queue, Git Subtrees (Ralph loop của Mike Hostetler).
- **Kênh tiếp nhận sự kiện (Integrations):** Webhooks từ Slack, Linear, GitHub.

---

## Kiểm chứng chất lượng (test, review, gate)
- **Cơ chế "Zero Trust" với dữ liệu bên ngoài [16:21, 31:09]:** Hệ thống không bao giờ thực thi trực tiếp mã lỗi do người dùng báo cáo; bắt buộc phải chạy prompt nội bộ để sinh ra kịch bản tái hiện (repro) đáng tin cậy trên môi trường chuẩn trước khi ghi nhận thành issue.
- **Đánh giá định lượng (Evals & Benchmarks) [19:50 - 20:40, 30:33 - 30:52]:** Xây dựng bộ kiểm thử dựa trên kho dữ liệu lỗi trong quá khứ; đo lường tỷ lệ tái hiện thành công (repro rate) và tỷ lệ vượt qua kiểm thử (pass rate) trên từng PR của chính pipeline tự động (ví dụ: đo tỷ lệ chính xác của PR deduplication).
- **Hồi quy liên tục (Regression Test Suite) [17:21 - 17:30]:** Mọi PR mới đều kích hoạt kiểm tra lại toàn bộ danh sách các issue trong quá khứ để đảm bảo không bị tái phát lỗi (chỉ tốn chi phí CPU rẻ).
- **Cổng kiểm duyệt tự động (Bot Review Gate) [25:00 - 25:40]:** Tích hợp bot CodeRabbit vào một vòng lặp `while loop` với giới hạn tối đa 3 lần lặp; agent phải tự sửa đến khi CodeRabbit chấp thuận thì mới thông báo cho kỹ sư con người.
- **Cổng phê duyệt của con người (Human Gate) [25:23 - 25:27]:** Quy tắc bất di bất dịch: con người bắt buộc phải trực tiếp kiểm tra và ấn nút merge, hệ thống không được tự ý đưa code vào production mà không có sự đồng ý của kỹ sư.
- **Tiêu chuẩn PR vừa tầm tiếp thu (Digestible PR Bar) [13:56 - 14:10]:** Nghiêm cấm đưa các PR khổng lồ 20.000 dòng ra review vì con người sẽ giảm chuẩn chất lượng ("lower the bar of quality"); bắt buộc phải chia nhỏ thành các PR 1.000 – 3.000 dòng có kèm migration rõ ràng.

---

## Rủi ro / hạn chế / lời khuyên tác giả nêu
- **Cạm bẫy tự động hóa 100% (The 100% automation folly) [32:30]:** Tác giả khẳng định việc cố gắng tự động hóa toàn bộ quy trình là sai lầm; mục tiêu khả thi và hiệu quả hơn nhiều là đạt 95% tự động hóa, 5% còn lại dành cho con người can thiệp xử lý ngoại lệ.
- **Rủi ro phụ thuộc hạ tầng đám mây của bên thứ ba [35:14 - 36:20]:** Khi đưa mã vào sandbox của vendor bên ngoài, việc cấu hình toolchain phức tạp hoặc "chọc lỗ" (poke holes) xuyên qua tường lửa để truy cập 50+ dịch vụ nội bộ sẽ gây ra ma sát rất lớn; chưa kể các lỗi tiềm ẩn do kernel Linux giả lập không hỗ trợ một số system calls.
- **Quá tải nhận thức do PR rác [13:56, 18:56]:** Agent viết code cực nhanh dẫn đến bùng nổ số lượng PR nhỏ hoặc PR quá lớn gây tắc nghẽn khâu review của kỹ sư; giải pháp là phải hạ thấp thời gian can thiệp của con người xuống mức tối thiểu bằng các bộ lọc tự động.
- **Thiếu chuẩn giao tiếp chung cho Harness [52:45 - 53:32]:** Hiện tại các giao thức như ACP hay AGUI đều thiếu hỗ trợ hooks vòng đời; mỗi harness (Claude Code, Codex, Pi) lại có cơ chế plugin và UI hoàn toàn khác nhau.
- **Cảnh báo về cấu trúc kho mã (Monorepo vs Multi-repo) [45:51 - 49:40]:** Đa kho lưu trữ (multi-repo) là trở ngại lớn cho agent. Lời khuyên:
  - Nên dùng monorepo hoặc tạo thư mục điều phối (coordination repo/folder) chứa cấu hình hướng dẫn agent tra cứu giữa các repo.
  - Tuyệt đối tránh xa Git Submodules vì cơ chế ghim commit cố định sẽ gây lỗi nghiêm trọng; nếu cần liên kết giữa các repo, hãy ưu tiên dùng Git Subtrees.
- **Nguyên tắc "Composition over Inheritance" trong mua sắm giải pháp [56:55 - 57:22]:** Tránh tư duy cực đoan "mua tất cả hoặc tự xây tất cả"; kỹ sư nên chọn các giải pháp có giao diện mở để tự quản lý môi trường dev/compute nội bộ, trong khi có thể mua ngoài lớp điều phối hoặc hoán đổi harness khi có model tốt hơn.

---

## Trích dẫn nguyên văn (5 câu, giữ tiếng gốc, kèm [mm:ss] đúng như transcript)

1. **[25:31]** `"Yeah. Like basically do not notify a human until code rabbit is happy."`
2. **[32:30]** `"I think the folly that a lot of people make is they try and make a system that is fully automatic. That is much harder than getting a system that's 95% automatic."`
3. **[36:04]** `"one of my thesis is like you are going to want to own this uh unless you're building like tiny little toy nex.js JS apps and you're like, you know, in the like majority like in distribution set of stuff, you're going to start to hit friction unless you can own this in a really clean way."`
4. **[48:50]** `"What I would the other thing I would recommend is please don't use subm modules."`
5. **[57:15]** `"The real answer is like you should have as an engineer choice and the ability to like work in open systems and plug these things together."`

---

## Đánh giá: điểm hữu ích cho team 3-10 kỹ sư (1-5) + lý do; nội dung là demo/quảng cáo hay thực chiến?

### Điểm hữu ích cho team 3-10 kỹ sư: **4.5 / 5**
- **Lý do đánh giá cao:**
  - *Tính khả thi và tiết kiệm chi phí:* Mô hình tận dụng máy tính Mac có sẵn trong văn phòng kết hợp với headless CLI qua REST API đơn giản là giải pháp cực kỳ thực tế cho team nhỏ, không đòi hỏi ngân sách khổng lồ cho hạ tầng cloud hay các nền tảng enterprise phức tạp.
  - *Khung tư duy phân tầng mạch lạc:* Giúp nhóm nhỏ tránh việc "phát minh lại bánh xe", phân định rõ phần nào nên tự xây dựng (môi trường dev, kịch bản test repro) và phần nào nên tận dụng (harness từ Claude Code / Codex, bot review CodeRabbit).
  - *Giải quyết trực diện nút thắt review:* Chiến lược chia nhỏ PR (1.000 – 3.000 dòng), vòng lặp bot review gác cổng và hàng đợi merge tự động giải tỏa gánh nặng tâm lý lớn nhất của các team nhỏ khi ứng dụng AI (nguy cơ kỹ sư bị ngập trong PR rác).
  - *(suy luận) Lý do trừ 0.5 điểm:* Một số nội dung ở cuối video (tính năng mở rộng phần mềm động trong thời gian thực - extendable code) vẫn còn dang dở ở mức ý tưởng thử nghiệm; ngoài ra giải pháp xử lý multi-repo đòi hỏi team phải tự cấu hình kịch bản điều phối chứ chưa có công cụ dựng sẵn.

### Tính chất nội dung: **Thực chiến (Battle-tested / Production-ready)**
- **Minh chứng rõ ràng từ nội dung trao đổi:**
  - Hai tác giả nói chuyện từ vị trí người trực tiếp vận hành hệ thống hàng ngày tại startup của họ (Boundary và HumanLayer), công khai chia sẻ cả những số liệu chưa đạt kỳ vọng (ví dụ: độ chính xác của agent lọc trùng lặp ban đầu còn thấp [20:34], buổi demo tính năng live code bị lỗi biên dịch do thay đổi API của BAML [67:23]).
  - Nội dung đi sâu vào các bài toán kỹ thuật gai góc ở cấp độ hệ thống mà các video quảng cáo thường né tránh: giới hạn system calls của kernel giả lập, xung đột cấu hình mạng khi chọc lỗ truy cập microservices nội bộ, độ trễ CI/CD, cơ chế retry khi bot review không duyệt.
  - Cả hai diễn giả đều giữ quan điểm khách quan về "Build vs Buy": Dex thừa nhận sản phẩm HumanLayer của mình chưa có API bề mặt đủ rộng để Vibh tích hợp [62:08 - 62:17], đồng thời khen ngợi các giải pháp đối thủ như cơ chế Outpost của Devin/Cognition [56:13 - 56:30]. Không có dấu hiệu bán hàng một chiều hay dàn dựng kịch bản hào nhoáng.

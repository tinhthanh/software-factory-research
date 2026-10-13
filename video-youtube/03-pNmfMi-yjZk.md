# Build an agentic software factory: deep dive
- Kênh: Steve (Builder.io)
- URL: https://www.youtube.com/watch?v=pNmfMi-yjZk
- Thời lượng: Khoảng 17 phút 35 giây (ước tính từ timestamp cuối [17:34])

## Tóm tắt (5-8 câu)
1. Video phân tích chi tiết mô hình "software factory" – hệ thống phần mềm tự hoàn thiện liên tục thông qua các vòng lặp agentic tự động xử lý telemetry và phản hồi người dùng.
2. Tác giả xây dựng và mã nguồn mở bộ kỹ năng (skills) chạy theo lịch định kỳ trên Codex hoặc Claude Code để tự động chuyển hóa các lỗi có thể tái lập thành các pull request (PR).
3. Quy trình vận hành cốt lõi đi theo một pipeline khép kín gồm: thu thập lỗi (collect), mở PR, theo dõi và giải quyết phản hồi PR (babysit), rà soát phê duyệt (review) và triển khai (ship), với yêu cầu bắt buộc là kiểm chứng (verification) ở từng bước.
4. Để khắc phục hiện tượng agent bỏ dở tác vụ hoặc sửa đi sửa lại một lỗi không dứt, hệ thống bổ sung agent giám sát (watchdog) và quy trình hồi cứu tuần (look back) sử dụng các mô hình AI lớn hơn nhằm tìm ra giải pháp mang tính hệ thống.
5. Về mặt hạ tầng, tác giả khẳng định hệ thống cần chạy trên máy Mac cục bộ (sử dụng một laptop phụ hoạt động 24/7) thay vì cloud để tận dụng đầy đủ biến môi trường, tài khoản đăng nhập thực tế và tránh làm nghẽn máy làm việc chính.
6. Để giảm thiểu rủi ro hỏng hóc cho người dùng cuối, tác giả phân tách môi trường: cập nhật liên tục các PR vào môi trường beta cho nội bộ dùng, còn môi trường production chỉ phát hành 1 lần mỗi ngày để dễ dàng rollback khi phát sinh sự cố.
7. Tác giả định vị vai trò của kỹ sư phần mềm sẽ chuyển dịch từ viết code chi tiết sang kỹ sư hệ thống (systems engineer), đồng thời khuyên người xem nên bắt đầu từng bước nhỏ từ chạy thủ công và dry-run trước khi tự động hóa toàn diện.

## Định nghĩa 'software factory' theo tác giả
- **Bản chất**: Là "phần mềm tự cải thiện" (*literally software that self-improves*) [00:03]. Khi hệ thống thu thập phản hồi và telemetry, phần mềm sẽ tự động trở nên tốt hơn mà không cần con người phải can thiệp thủ công vào từng dòng code.
- **Cách thức vận hành**: Tự động hóa việc phân loại bug và cải tiến thông qua các vòng lặp agentic (*agentic loops*), biến đầu vào là lỗi thành đầu ra là phần mềm chất lượng tốt hơn, trong đó con người đóng vai trò thiết lập các điểm chạm kiểm soát (*human touchpoints*) để bảo vệ và tiếp quản khi cần [00:10].
- **Sự thay đổi tư duy kỹ thuật**: Biến kỹ sư thành "kỹ sư hệ thống" (*systems engineer*) hoặc như một "nhà khoa học quan sát một sinh vật sinh học" (*scientist of a biological organism*) – tập trung vào việc thiết kế, đo lường, tối ưu hóa và đánh giá cỗ máy tạo ra phần mềm thay vì tự tay viết code vụn vặt [02:00, 12:20, 13:08].

## Kiến trúc & quy trình (các bước/pipeline, có timestamp)
1. **Thu thập nguồn đầu vào (Input Sources) [00:22, 02:10]**:
   - Dữ liệu lỗi & telemetry: Lỗi từ Sentry, error logs, chỉ số uptime, độ trễ phản hồi P90.
   - Phản hồi từ con người: Phản hồi trong ứng dụng (*in-app feedback*), kênh Slack, phỏng vấn khách hàng, GitHub issues và pull requests.
2. **Thu thập & Đánh giá chính sách (Factory Collect & Policy) [02:35, 05:46]**:
   - Skill `factory collect` chạy ngầm theo lịch định kỳ (vài giờ một lần) trên Codex/Claude Code, cấu hình qua file YAML và natural language prompts.
   - Nếu issue thiếu thông tin: Skill có thể tự động phản hồi yêu cầu người dùng làm rõ (như xin URL, mốc thời gian xảy ra) và kiểm tra lại sau [05:46 - 06:14].
   - Đánh giá theo chính sách (*fixed policy*): Chỉ những lỗi rõ ràng và "có thể kiểm chứng được" (*verifiably fixable*) mới được giao cho agent.
   - Nếu không thỏa mãn chính sách: Chuyển toàn bộ sang hàng đợi gom nhóm cho con người xử lý (*human inputs/batching*) [04:14].
3. **Thực thi & Tái lập - Kiểm chứng (Execution & Verification) [01:17, 03:20, 03:54]**:
   - Khi chính sách cho phép, Codex tự động mở một nhánh/cây thư mục cô lập (*isolated work tree*).
   - Agent bắt buộc phải tái lập được lỗi (chạy browser end-to-end, chụp màn hình screenshotting), tiến hành sửa lỗi, kiểm chứng rằng bản sửa đã hết lỗi trước khi tạo hoặc cập nhật PR. Cấm tuyệt đối việc agent đoán mò rồi đẩy PR [04:04].
4. **Theo dõi và xử lý PR (Factory Babysit PR) [04:23 - 05:03]**:
   - Skill `factory babysit pr` giám sát PR vừa mở.
   - Agent bắt buộc phải kiểm tra và giải quyết từng phản hồi từ review bot hoặc lỗi CI: nếu đúng lỗi thì sửa tiếp và phản hồi lại; nếu không đồng ý thì trả lời giải thích lý do không sửa.
5. **Rà soát & Phê duyệt (Review PRs & Approval Policy) [05:03 - 05:33]**:
   - Một agent/skill rà soát PR độc lập chạy vài giờ một lần để đảm bảo CI đã pass, hết xung đột merge và các comment đã được xử lý.
   - Áp dụng Approval Policy (cấu hình YAML + prompt): nếu thay đổi an toàn (có unit test tốt, sửa CSS đơn giản) thì cho phép tự động merge và deploy; nếu tiềm ẩn rủi ro thì gán nhãn chờ con người duyệt (*human review*).
6. **Vòng lặp Giám sát & Tối ưu hóa hệ thống (Supervision & Lookback)**:
   - **Factory Watchdog [08:33, 09:37]**: Chạy khoảng 4 lần/ngày (hoặc gắn link giám sát một thread cụ thể). Nhiệm vụ là đôn đốc các PR/task bị dừng giữa chừng mà không hoàn tất, đồng thời dùng một model độc lập để kiểm chứng chéo và hướng dẫn agent worker.
   - **Factory Look Back [10:33 - 11:52]**: Chạy định kỳ hàng tuần. Dùng mô hình lớn (Opus, Soul, Fable) quét dữ liệu 30 ngày để tìm các mẫu lỗi lặp đi lặp lại (*recurring patterns*) hoặc các vùng code dễ vỡ (*brittle areas*) mà agent tưởng đã sửa nhưng thực chất vẫn phát sinh, từ đó phân tích meta-analysis và đưa ra giải pháp toàn diện.
7. **Phân tách môi trường triển khai (Beta -> Production) [14:00 - 14:27]**:
   - PR tự động merge liên tục vào nhánh `main` và deploy lên môi trường **Beta**. Người dùng nội bộ Builder.io dùng môi trường này để phát hiện lỗi sớm.
   - Môi trường **Production** chỉ được cut release deploy 1 lần/ngày để giữ sự ổn định cao và dễ rollback nếu có lỗi lọt lưới.

## Vai trò agent & con người
- **Vai trò của Agent**:
  - Tự động quét và gom lỗi từ nhiều nguồn theo lịch trình.
  - Tự tái lập lỗi trên môi trường thực tế (trình duyệt), viết mã sửa lỗi trong git worktree cô lập.
  - Tự mở PR, tự theo dõi phản hồi CI/bot review ("babysit PR") và phản hồi comment.
  - Đóng vai trò giám sát viên (Watchdog) để đôn đốc agent khác hoặc kiểm tra chéo.
  - Tiến hành phân tích meta-analysis đa chiều dài hạn (Lookback) qua logs, telemetry và feedback để tìm lỗi gốc rễ.
- **Vai trò của Con người**:
  - Đóng vai trò "Kỹ sư hệ thống": thiết kế quy trình, viết file YAML, tinh chỉnh system prompts, đánh giá tỷ lệ hiệu quả của toàn bộ nhà máy.
  - Đóng vai trò chốt chặn an toàn (*guard/touchpoint*): nhận các issue không rõ ràng hoặc các PR có độ rủi ro cao vượt ngoài phạm vi tự merge.
  - Hỗ trợ giải quyết các rào cản vật lý/xác thực: nhập mã OTP, xác thực passkey, cung cấp khóa bí mật khi agent bị kẹt (thông qua cảnh báo Telegram) [07:10].
  - Dành thời gian giải quyết các bài toán kiến trúc lớn, tính năng phức tạp thay vì bị chôn vùi vào việc sửa lỗi vụn vặt hàng ngày [12:40 - 13:08].

## Công cụ / stack được nêu
- **Công cụ điều phối & Môi trường Agent**:
  - Codex (ưu tiên sử dụng nhờ khả năng quản lý worktree/remote tasks trực quan qua icon quả cầu xanh).
  - Claude Code (hỗ trợ điều khiển qua tính năng SSH).
  - Kho mã nguồn mở Skills repo và công cụ dòng lệnh cài đặt (Installer CLI) của tác giả.
- **Các mô hình AI (LLMs)**:
  - Luna (chạy trên Codex ở max settings: chi phí siêu rẻ, tốc độ cao, dùng làm worker chính xử lý khối lượng lớn PR).
  - Claude Opus 5.5, Soul, Fable (các mô hình lớn, đắt tiền hơn, dùng cho Watchdog và phân tích sâu Lookback).
  - Sonnet (được nhắc đến khi phối hợp với skill Efficient Frontier để tạo sub-agent tiết kiệm chi phí).
- **Hạ tầng & Thiết bị**:
  - Máy tính riêng biệt (một chiếc laptop Mac thứ hai hoặc Mac mini chuyên dụng chạy 24/7, cấu hình nhiều RAM).
  - Telegram (kênh thông báo đẩy khi agent bị kẹt cần con người đăng nhập OTP/passkey).
  - Git worktrees / Monorepo.
- **Nền tảng giám sát, CI/CD & Ứng dụng**:
  - Sentry (báo cáo lỗi runtime, source maps), hệ thống đo lường Uptime & P90 latency.
  - GitHub (Issues, PRs, Review bots, CI).
  - Vercel (nền tảng triển khai ứng dụng web).
  - Agent Native Framework / agentnative.com (framework và bộ ứng dụng mã nguồn mở của tác giả: công cụ thiết kế giống Figma, slide giống Google Slides, Loom clone, Calendar, Mail...).

## Kiểm chứng chất lượng (test, review, gate)
- **Tái lập lỗi là điều kiện bắt buộc (*Reproduction Gate*)**: Agent không được đoán mò; phải chạy trình duyệt end-to-end, chụp ảnh màn hình để chứng minh lỗi tồn tại và chứng minh bản sửa đã giải quyết được lỗi trước khi được phép mở PR [04:04].
- **Cơ chế Babysit PR bắt buộc**: Mọi PR phải vượt qua toàn bộ bài kiểm tra CI. Agent phải phản hồi hoặc xử lý từng comment của bot/người trước khi chuyển sang bước tiếp theo [04:48].
- **Cổng phê duyệt phân tầng (*Approval Policy Gate*)**: Phân loại mức độ rủi ro dựa trên cấu hình và prompt. Các thay đổi an toàn (CSS, có unit test rõ ràng) được tự merge; các thay đổi quan trọng/phức tạp bắt buộc phải có con người review [05:13].
- **Kiểm thử E2E nặng và Agent testing trên Beta**: Chạy các bộ test E2E toàn diện và thả agent vào test tự do trên môi trường Beta để bắt lỗi hiệu năng và luồng người dùng (không chạy trên CI của PR vì quá lâu và tốn kém) [14:40 - 14:55].
- **Cổng phát hành Production 1 lần/ngày**: Tách biệt Beta (đồng bộ main liên tục) và Production (deploy 1 lần/ngày). Chu kỳ này giúp hạn chế việc xả liên tục hàng tá PR của agent vào production, đồng thời giúp việc rollback trở nên đơn giản nếu phát sinh lỗi rò rỉ [14:13 - 14:26].

## Rủi ro / hạn chế / lời khuyên tác giả nêu
- **Rủi ro & Hạn chế**:
  - *Môi trường Cloud không đáp ứng được*: Khó tái lập chính xác môi trường thực tế (thiếu phiên cookie trình duyệt, file môi trường, passkey, OTP, native Mac apps) [06:33 - 06:54].
  - *Agent bỏ quên tác vụ giữa chừng*: Khi mở quá nhiều worktree, agent Luna đôi lúc quên hoặc dừng lại không thực hiện tiếp các bước sau của quy trình [09:54].
  - *Bẫy lỗi lặp lại (*Recurring patterns / Brittle areas*)**: Agent tưởng đã sửa xong nhưng thực tế người dùng vẫn báo lỗi tiếp, hoặc sửa chỗ này làm gãy chỗ khác [10:25].
  - *Tốn tài nguyên phần cứng & chi phí token*: Chạy browser test tự động song song ngốn rất nhiều RAM/CPU; nếu dùng mô hình lớn không kiểm soát sẽ gây bùng nổ chi phí [03:51, 07:37, 15:48].
- **Lời khuyên của tác giả**:
  - *Bắt đầu từ quy mô nhỏ (*Start small - Step zero*)**: Bắt đầu bằng việc chạy lệnh thủ công (dry run) với `/factory collect` trên máy cá nhân, chỉnh sửa file YAML cho vừa ý trước khi lên lịch tự động hoàn toàn [14:28, 14:56 - 15:35].
  - *Chất lượng đầu vào quyết định hiệu quả*: Dành thời gian xây dựng hệ thống telemetry tốt, kênh feedback rõ ràng, cấu hình source maps chuẩn xác để agent lần ra đúng dòng code gốc [14:52 - 14:60].
  - *Sử dụng Monorepo*: Giúp factory kiểm soát toàn bộ dự án trong một codebase tập trung, tránh phân mảnh [14:49].
  - *Dùng phần cứng riêng biệt*: Cần một máy Mac riêng (Macbook hoặc Mac mini nhiều RAM) chạy 24/7 để gánh các tác vụ nặng, tránh làm chậm máy làm việc của lập trình viên [07:01, 15:46].
  - *Kết hợp mô hình hợp lý*: Dùng mô hình rẻ và nhanh (như Luna max settings) cho các tác vụ hàng ngày để tối ưu chi phí, chỉ điều động mô hình lớn (Opus/Fable) cho các tác vụ giám sát sâu [08:08, 08:33, 10:52].

## Trích dẫn nguyên văn (5 câu, giữ tiếng gốc, kèm [mm:ss] đúng như transcript)
1. `[00:03]` "Literally software that self-improves. That as you collect feedback and telemetry, the software gets better automatically."
2. `[04:09]` "We need to know it's reproduced, it's fixed before we get any autonomous factory PR."
3. `[06:30]` "And my definitive answer right now is it's got to run on a laptop. Because to actually verify things, it needs my actual environment."
4. `[12:20]` "Now, at the end of the day, I spend most of my time feeling like a scientist of a biological organism, always inspecting, microscoping, and assessing if the factory's working as efficiently and as effectively as it possibly can."
5. `[14:28]` "And lastly, I would start small. You don't have to start with all these things."

## Đánh giá: điểm hữu ích cho team 3-10 kỹ sư (1-5) + lý do; nội dung là demo/quảng cáo hay thực chiến?
- **Điểm hữu ích**: **4/5**
  - **Lý do**:
    - *Rất giá trị cho đội ngũ nhỏ*: Với team 3-10 người, nguồn lực kỹ thuật thường bị phân mảnh vì phải vừa phát triển tính năng mới vừa trực sửa các lỗi vặt (UI glitch, CSS, lỗi build/deploy, bug nhỏ). Quy trình này giúp tự động hóa khâu triage và sửa các bug dễ tái lập.
    - *Cách tiếp cận thực tế, có thể áp dụng dần*: Lời khuyên bắt đầu từ chạy thủ công, dry-run, cấu hình prompt qua YAML, phân tách Beta - Production và nhấn mạnh kiểm chứng (verification) giúp các team nhỏ tránh được cái bẫy tạo ra mã rác.
    - *Rào cản khiến chưa đạt 5/5*: Để hệ thống hoạt động hiệu quả, dự án đòi hỏi phải có nền tảng telemetry (Sentry, logs) và bộ test E2E tương đối tốt từ trước (nếu codebase chưa có test, agent rất khó tự verify) (suy luận). Ngoài ra, giải pháp sử dụng một laptop Mac phụ cắm sạc 24/7 và gửi tin nhắn Telegram khi cần OTP/passkey mang tính giải pháp tình thế cá nhân, chưa phải là kiến trúc chuẩn hóa cấp doanh nghiệp cho cả nhóm dùng chung (suy luận).
- **Tính chất nội dung: Mang tính thực chiến cao (Field-tested / Practical)**
  - Mặc dù tác giả có lồng ghép giới thiệu các dự án nguồn mở của mình (Agent Native Framework, skills repo), nội dung video hoàn toàn không phải là một bài demo được dàn dựng màu hồng.
  - Video tập trung giải quyết những bài toán hóc búa rất thực tế mà các demo thông thường hay né tránh: cách xử lý khi agent bị kẹt/quên việc (Watchdog), hiện tượng sửa lỗi tái diễn nhiều lần (Lookback meta-analysis), bài toán chi phí token khi chạy quy mô lớn (dùng model rẻ cho worker, model đắt cho giám sát), giới hạn của hạ tầng cloud đối với việc xác thực/passkey, và vấn đề quá tải CPU/RAM khi chạy nhiều browser test song song.

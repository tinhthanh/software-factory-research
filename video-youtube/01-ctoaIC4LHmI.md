# Build Your Own AI Software Factory with Claude Code
- **Kênh:** ZazenCodes
- **URL:** https://www.youtube.com/watch?v=ctoaIC4LHmI
- **Thời lượng:** Khoảng 27:47 (ước lượng từ timestamp cuối `[27:47]`)

---

## Tóm tắt (5-8 câu)
1. Video hướng dẫn quy trình tự xây dựng một "xưởng phần mềm AI" (AI software factory) vận hành trực tiếp bên trong một dự án mã nguồn thực tế bằng Claude Code.
2. Quy trình cốt lõi hoạt động theo một vòng lặp tác tử (agentic loop) khép kín: tiếp nhận tính năng, viết đặc tả kỹ thuật (Spec Writer), lập trình tính năng (Builder), thẩm định độc lập qua nhiều góc độ (Security, UX, UI, Code Review), và phê duyệt sáp nhập mã nguồn (Approver).
3. Hệ thống sử dụng kết hợp giữa mô hình Claude Opus 5.5 và Sonnet 5.5, trong đó Opus được ưu tiên đảm nhận vai trò bộ điều phối (orchestrator) và kiểm duyệt cấp cao để đảm bảo độ chính xác chi tiết.
4. Trạng thái vận hành và siêu dữ liệu (metadata) của các tác vụ được lưu trữ hoàn toàn dưới dạng tệp Markdown cục bộ và hiển thị trực quan thông qua một web dashboard chuyên dụng.
5. Tác giả giải quyết bài toán chạy song song nhiều tính năng trong backlog cùng lúc bằng cách tích hợp công cụ Git worktrees trên các phiên tmux độc lập.
6. Hệ thống thiết lập cơ chế giám sát con người (human-in-the-loop), tự động leo thang (escalate) chuyển sang bước người duyệt khi chạm đến các khu vực nhạy cảm như phân quyền, thanh toán, hoặc cơ chế xóa cache.
7. Mặc dù thừa nhận chi phí token tăng cao khi chạy nhiều sub-agent trao đổi ngữ cảnh, tác giả khẳng định giải pháp tự thiết kế này mang lại năng suất thực chất và khả năng kiểm soát cao hơn so với việc phụ thuộc vào các framework phức tạp bên ngoài.

---

## Định nghĩa 'software factory' theo tác giả
- **Nguồn gốc lịch sử:** Tác giả trích dẫn khái niệm do Bob Beamer tại General Electric (GE) mô tả lần đầu vào năm 1968: một môi trường lập trình do máy tính kiểm soát (computer-controlled programming environment), chứa các công cụ phát triển tiêu chuẩn hóa cùng với thông tin lịch sử phục vụ cho việc quản lý và đo lường.
- **Tiến trình phát triển:**
  - Thập niên 1960–1970: Xuất hiện sớm tại Nhật Bản, châu Âu và Mỹ.
  - Thập niên 2000: Hướng tới việc tái sử dụng các mẫu thiết kế (patterns), mô hình (models) và bộ khung (frameworks).
  - Thập niên 2010–2020: Định hình bởi các đường ống CI/CD chuẩn mực và GitHub Actions.
- **Trong kỷ nguyên AI (Agentic Factory):** Tác giả định nghĩa điểm mới mẻ cốt lõi nằm ở *"sự tự động hóa các công việc nhận thức tương đối phi cấu trúc (unstructured cognitive work) giữa các giai đoạn mang tính tất định (deterministic stages), bao gồm cả việc tự viết toàn bộ mã nguồn"*.
- **Về bản chất thực hành:** Đây là một hệ thống tác tử có tính tái sử dụng cao, nơi một nhóm AI agent tự động nhận yêu cầu tính năng, tự triển khai trên nhánh riêng, tự phản biện/thẩm định qua nhiều vòng, và chỉ đưa vào codebase chính sau khi qua các chốt kiểm duyệt nghiêm ngặt.

---

## Kiến trúc & quy trình (các bước/pipeline, có timestamp)
Kiến trúc vận hành dựa trên cơ chế vòng lặp nhiều tầng (Agentic Loop) kết hợp Git branch/worktree:

1. **Tiếp nhận yêu cầu (Input & Trigger) `[01:14 - 01:23]`, `[09:55 - 10:17]`:**
   - Người dùng kích hoạt lệnh điều phối `factory <mô tả tính năng>` hoặc `factory next` (lấy việc từ `backlog.md`).
   - Kiểm tra tiền điều kiện (Precondition): Thư mục làm việc Git bắt buộc phải sạch (`clean working tree`) `[10:41 - 10:44]`.
2. **Viết đặc tả kỹ thuật (Spec Writer Agent) `[01:25 - 01:27]`, `[11:10 - 11:24]`:**
   - Sub-agent (sử dụng Claude Opus) tiếp nhận yêu cầu, phân tích codebase và xuất ra tệp đặc tả kỹ thuật Markdown (`spec file`) ghi rõ tiêu chí nghiệm thu.
3. **Xây dựng mã nguồn (Builder Agent) `[01:27 - 01:34]`, `[11:26 - 12:16]`:**
   - Builder Agent nhận tệp spec, checkout nhánh làm việc riêng của factory (hoặc thư mục Git worktree riêng), thực hiện chỉnh sửa code thực tế, tạo các commit tương ứng và xuất tệp nghiệm thu build.
4. **Hội đồng thẩm định đa chiều (Review Sub-agents) `[01:34 - 01:46]`, `[12:20 - 12:40]`:**
   - Mã nguồn được đồng thời chuyển tới 4 sub-agent chuyên biệt chạy độc lập:
     - *Security Review Agent:* Rà soát lỗ hổng bảo mật.
     - *UX Review Agent:* Đánh giá trải nghiệm người dùng.
     - *UI Design Review Agent:* Đánh giá giao diện.
     - *Code Review Agent:* Rà soát chất lượng và quy chuẩn mã nguồn.
5. **Vòng lặp sửa đổi (Rework Loop) `[01:47 - 01:52]`, `[07:22 - 07:36]`:**
   - Nếu bất kỳ vòng review nào không đạt, phản hồi lỗi được nạp ngược lại cho Builder Agent để sửa đổi. Hệ thống thiết lập ngưỡng chặn tối đa 2 vòng (`max two rounds`) để tránh kẹt lặp vô hạn.
6. **Thẩm định sáp nhập & Leo thang (Approver Agent) `[01:53 - 02:04]`, `[12:48 - 13:05]`:**
   - Approver Agent (chạy Opus) phân tích toàn bộ kết quả review và thay đổi mã. Nếu đáp ứng đầy đủ điều kiện an toàn, agent có thể tự động merge. Nếu chạm phải logic nhạy cảm (billing, quyền khóa học, cache rendering), agent sẽ đánh dấu `escalate` và chuyển tác vụ sang trạng thái `Needs human`.
7. **Phê duyệt của con người & Hợp nhất (Human Approval & Merge) `[13:26 - 14:17]`:**
   - Con người kiểm tra thông tin trên dashboard, chạy lệnh `factory approve <id>` trong session Claude Code để thực thi merge vào nhánh chính.
8. **Mở rộng chạy song song (Parallel execution via Git Worktrees) `[16:16 - 19:35]`:**
   - Để nhiều agent/session tmux xử lý nhiều tính năng đồng thời trong `backlog.md` mà không xung đột working directory, pipeline tích hợp thêm cơ chế phân lập bằng Git worktrees.
9. **Mở rộng tương lai (Future pipeline vision) `[24:05 - 25:48]`:**
   - Đưa GitHub Issues hoặc Slack làm nguồn tiếp nhận tự động (Intake triggers).
   - Kết nối nền tảng giám sát lỗi như Sentry để tự động đưa bối cảnh lỗi từ production vào factory xử lý.
   - Giám sát hạ tầng (CPU/RAM) sau triển khai (Post-deployment) và tự động hoàn tác (rollback) nếu tính năng mới gây suy thoái hệ thống.

---

## Vai trò agent & con người
- **Orchestrator Agent (Claude Code):** Giữ vai trò nhạc trưởng điều phối toàn bộ vòng đời công việc, phân phối tác vụ và quản lý vòng đời sub-agents qua skill `factory`. Tác giả khuyến nghị nên sử dụng mô hình mạnh nhất (Opus 5.5, high effort) cho vị trí này.
- **Spec Writer Agent:** Tác tử chuyên trách chuyển dịch ngôn ngữ tự nhiên từ backlog/yêu cầu thành tài liệu đặc tả kỹ thuật chi tiết (.md).
- **Builder Agent:** Tác tử thực thi kỹ thuật, trực tiếp đọc spec, viết mã, sửa đổi file và tạo commit trên nhánh Git cô lập.
- **Reviewer Agents (UI, UX, Security, Code Review):** Các tác tử độc lập đóng vai trò kiểm soát chất lượng chuyên môn sâu trước khi mã nguồn được phép đưa vào nhánh chính.
- **Approver Agent:** Tác tử thẩm phán cấp cao, chịu trách nhiệm ra quyết định có hợp nhất tự động hay bắt buộc chuyển giao cho con người.
- **Con người (Human-in-the-loop):**
  - Đóng vai trò khởi tạo đề bài và cung cấp ngữ cảnh ban đầu.
  - Thiết lập ranh giới an toàn (guardrails), quyền hạn bypass và danh mục các trường hợp bắt buộc phải leo thang phê duyệt.
  - Đóng vai trò chốt chặn cuối cùng (Human gate): đánh giá lý do leo thang trên dashboard và kích hoạt phê duyệt sáp nhập (`factory approve`).

---

## Công cụ / stack được nêu
- **Công cụ điều phối & Agent:** Claude Code (CLI từ Anthropic), Claude Skills (định dạng kỹ năng cho agent), Claude Sub-agents.
- **Mô hình AI:** Claude Opus 5.5, Claude Sonnet 5.5 (thiết lập mức nỗ lực `high effort` hoặc `low effort`).
- **Quản lý phiên bản & Mã nguồn:** Git, Git worktrees (phân lập môi trường chạy song song), LazyGit (giao diện TUI quản lý Git), Vim (xem và chỉnh sửa file).
- **Lưu trữ trạng thái & Dữ liệu:** Markdown files (đặt trong thư mục `factory/`, bao gồm `backlog.md`, tệp spec, build log, review feedback).
- **Công cụ dòng lệnh & Đa nhiệm:** tmux (quản lý nhiều phiên làm việc song song của agent).
- **Giao diện quan sát (Observability):** Custom Web Dashboard hiển thị các cột trạng thái tiến trình (Spec, Builder, Review, Needs human, Done).
- **Hệ thống liên kết / Đề xuất tích hợp:** GitHub (GitHub Issues, PRs, GitHub Actions), Slack, Sentry (nền tảng giám sát ứng dụng).

---

## Kiểm chứng chất lượng (test, review, gate)
- **Cổng tiền điều kiện Git (Clean Working Tree Gate):** Bắt buộc nhánh làm việc và nhánh main phải hoàn toàn sạch trước khi bắt đầu tạo job và trước khi thực hiện merge `[10:41]`, `[22:12]`.
- **Cổng đặc tả kỹ thuật (Spec-first Gate):** Không cho phép agent lập trình tự do khi chưa hoàn tất tài liệu spec với đầy đủ acceptance criteria rõ ràng.
- **Hội đồng phản biện 4 chiều độc lập (Multi-angle Review Gate):** Tách bạch hoàn toàn giữa agent viết mã và 4 agent thẩm định (Bảo mật, Code quality, UI, UX) nhằm loại bỏ sự tự thiên vị của mô hình.
- **Cơ chế giới hạn số vòng lặp (Rework Threshold):** Khống chế tối đa 2 vòng sửa đổi để ngăn ngừa hiện tượng lặp vô tận gây tốn chi phí và treo hệ thống.
- **Cổng phân loại rủi ro & Leo thang (Escalation Gate):** Quy tắc cứng bắt buộc Approver chuyển giao cho con người khi chạm vào các vùng rủi ro cao:
  - Các module tài chính/thanh toán (billing) `[07:41]`.
  - Cơ chế phân quyền/truy cập khóa học (course access) `[07:44]`.
  - Thao tác nặng ảnh hưởng hệ thống (hủy cache hiển thị trang blog - cache invalidation) `[21:43]`.
  - Xung đột trạng thái cục bộ (như tệp backlog chưa commit trên main) `[22:24]`.
- **Giao diện minh bạch (Observability):** Dashboard hiển thị chi tiết nguyên nhân escalate và chi tiết từng vòng review giúp con người thẩm định nhanh chóng trước khi gõ lệnh duyệt.

---

## Rủi ro / hạn chế / lời khuyên tác giả nêu
- **Rủi ro chi phí Token (Cost / Token consumption):** Việc chia nhỏ quy trình thành nhiều sub-agent yêu cầu liên tục truyền tải ngữ cảnh (context passing) qua lại, đẩy chi phí token tăng cao đáng kể `[26:36 - 26:50]`.
- **Rào chắn quá khắt khe (Overly cautious guardrails):** Agent có xu hướng cảnh giác quá mức, dễ tìm ra các lý do kỹ thuật để đẩy việc về trạng thái `Needs human` (ví dụ: e ngại việc làm mới cache blog), làm giảm bớt tính tự động `[21:26 - 21:34]`.
- **Nhiễu loạn hệ thống tệp Git (Repository clutter):** Việc sinh ra quá nhiều tệp Markdown theo dõi metadata trong thư mục dự án có thể làm hỏng tính năng tìm kiếm mờ (fuzzy searching); tác giả khuyên nên đưa vào `.gitignore` và dùng tiến trình riêng để sao lưu lên cloud storage nếu cần `[15:18 - 15:58]`.
- **Xung đột trạng thái Git khi chạy song song:** Chạy song song không thể vận hành ổn định nếu thiếu Git worktrees; ngoài ra, việc chỉnh sửa đồng thời các file dùng chung như `backlog.md` dễ gây tắc nghẽn lệnh merge `[22:12 - 22:35]`.
- **Phụ thuộc vào năng lực mô hình điều phối:** Sử dụng mô hình yếu làm orchestrator dễ gây lỗi quy trình; vị trí điều phối bắt buộc phải dùng mô hình mạnh nhất (như Opus) `[19:05 - 19:15]`, `[22:39 - 22:45]`.
- **Lời khuyên thực chiến của tác giả:**
  - *Tự xây dựng (Build your own):* Không nên mù quáng theo đuổi các framework phức tạp, các skill "thổi phồng" (hyped) hàng triệu tính năng được gắn sao nhiều trên GitHub. Hãy tự viết các prompt, skill và sub-agents đơn giản để làm chủ và kiểm soát 100% quy trình của mình `[19:43 - 20:26]`.
  - Phải tích hợp Git worktrees ngay từ đầu nếu có ý định xử lý đa nhiệm `[16:20 - 16:40]`.

---

## Trích dẫn nguyên văn (5 câu, giữ tiếng gốc, kèm [mm:ss] đúng như transcript)
1. `[01:06]` *"It's a simple agentic software factory where a team of agents take a feature and pull that into the main codebase by the end of our factory."*
2. `[03:06]` *"What's new is the automation of relatively unstructured cognitive work between the deterministic stages including of course writing the entire code it you know itself."*
3. `[05:43]` *"That's the power of a software factory and this is why everybody's so excited about these things right now and we could imagine in the future we want you know we can bring in data sources from the outside world and we can also have other things like we can have stuff that triggers this instead of a feature."*
4. `[19:43]` *"Also, we just built this ourselves. Like this is your own thing. You you just built it. You can change it. You can do whatever you want. You're not relying on like some dude's um you know factory skill that is all hyped and you found it and it does like a million things."*
5. `[26:41]` *"Anytime we're using sub agents, that's could incur extra costs because the agent has to pass contacts back and forth."*

---

## Đánh giá: điểm hữu ích cho team 3-10 kỹ sư (1-5) + lý do; nội dung là demo/quảng cáo hay thực chiến?

- **Điểm hữu ích cho team 3-10 kỹ sư:** **3.5 / 5**
  - **Lý do cộng điểm:**
    - *Kiến trúc tinh gọn, dễ tiếp cận:* Không đòi hỏi dựng hạ tầng máy chủ agent phức tạp; tận dụng ngay Claude Code CLI, Markdown và Git worktrees có sẵn trong môi trường của lập trình viên.
    - *Mô hình phân rã vai trò rất giá trị cho team nhỏ:* Việc thiết lập các sub-agent chuyên rà soát Security, UX/UI và Code Review giúp bù đắp sự thiếu hụt nhân sự chuyên trách mà các team 3–10 người thường gặp phải.
    - *Tư duy Human-in-the-loop thiết thực:* Cơ chế kiểm tra clean git tree và chặn tự động merge khi đụng chạm logic thanh toán hay cache là kinh nghiệm bảo vệ an toàn mã nguồn thực tế, tránh rủi ro AI phá hỏng nhánh production.
  - **Lý do trừ điểm (suy luận):**
    - *Thiếu kiểm thử tất định (Deterministic Testing):* Toàn bộ quy trình trong video dựa vào mô hình LLM để đánh giá (LLM-as-a-judge), hoàn toàn thiếu vắng bước kích hoạt các bộ kiểm thử tự động của dự án (Unit Test, Integration Test, Linter, CI pipeline) trước khi phê duyệt.
    - *Gánh nặng chi phí token:* Với quy trình chạy 4–5 sub-agent cho mỗi tính năng, nếu cả team 3–10 kỹ sư cùng vận hành liên tục trên API thương mại, chi phí sẽ tăng rất nhanh (tác giả demo dựa trên gói thuê bao cá nhân, không tính theo API token).
    - *Khó khăn trong chia sẻ trạng thái nhóm:* Cơ chế lưu metadata bằng file Markdown cục bộ (bị `.gitignore`) phù hợp cho cá nhân làm việc độc lập hơn là chia sẻ trạng thái đồng bộ giữa nhiều kỹ sư trong cùng một nhóm.

- **Nội dung là demo/quảng cáo hay thực chiến?**
  - **Kết luận:** Nội dung là sự **kết hợp giữa Video tài trợ (Sponsorship Demo) và Bằng chứng thực nghiệm thực tế (Proof-of-Concept / Thực chiến cấp cơ sở)**.
  - **Yếu tố tài trợ / Demo:** Video được Anthropic tài trợ chính thức (`Thank you to Anthropic for sponsoring today's video`), sử dụng gói tài khoản cá nhân của tác giả để tránh tính phí token API, đồng thời nhiều lần lồng ghép kêu gọi tham gia cộng đồng trả phí cá nhân. Các tính năng demo có độ phức tạp thấp (bỏ paywall bài viết, thêm nút copy code, tạo trang 404).
  - **Yếu tố thực chiến:** Không sử dụng mã nguồn giả lập hay kịch bản dàn dựng hoàn hảo, tác giả triển khai trực tiếp trên website cá nhân đang chạy production. Khi gặp các sự cố thực tế (nhánh Git không sạch, xung đột tệp `backlog.md`, agent từ chối merge do sợ hỏng cache), tác giả trực tiếp phân tích lỗi, tinh chỉnh guardrails và tích hợp thêm Git worktrees để gỡ rối. Đây là một bản thiết kế mẫu (blueprint) có giá trị thực hành cao, cung cấp phương pháp luận thực tế cho các nhóm kỹ sư muốn tự thiết kế luồng tự động hóa bằng AI mà không bị phụ thuộc vào các framework bên ngoài.

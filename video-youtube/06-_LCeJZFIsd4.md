# Building a Software Factory that actually works (Full Course)
- **Kênh:** Greg Isenberg (khách mời: Ross Mike / Mickey Schmollis)
- **URL:** https://www.youtube.com/watch?v=_LCeJZFIsd4
- **Thời lượng:** ~31 phút 28 giây (ước tính từ timestamp cuối [31:28])

---

## Tóm tắt (5-8 câu)
1. Video là cuộc trao đổi giữa Greg Isenberg và khách mời Ross Mike (Mickey) nhằm làm rõ khái niệm đang thịnh hành "software factory" (nhà máy phần mềm) và hướng dẫn cách thiết lập thực tế.
2. Tác giả khẳng định software factory không phải là một sản phẩm thương mại hay nền tảng đóng gói sẵn, mà là quy trình chuẩn hóa các kỹ năng (skills), luồng công việc (workflows) và kiến thức chuyên môn thông qua các tệp markdown đơn giản.
3. Dây chuyền phát triển gồm 4 bước chính có tính lặp: Isolate (cô lập nhánh bằng Git worktree), Build (xây dựng mã theo kiến trúc Service Layer), Prove (chứng minh kết quả bằng video/ảnh chụp hoặc số liệu), và Ship (đánh giá tự động qua code review agent).
4. Thiết kế này giải quyết triệt để rủi ro phổ biến khi dùng AI coding: 95% trường hợp agent tự ý xóa nhầm hoặc ghi đè mã nguồn của nhau khi làm việc đa nhiệm.
5. Quy trình thiết lập một vòng lặp tự sửa lỗi (feedback loop), buộc agent tự sửa code và kiểm thử lại cho tới khi đạt điểm tối đa (5/5) từ công cụ đánh giá độc lập trước khi gửi tới con người.
6. Vai trò của con người được chuyển dịch từ việc viết và soi từng dòng code sang vai trò quản đốc ("agent manager"), chỉ duyệt nhanh qua các bằng chứng trực quan trực quan kiểu "story" và nhấn merge.
7. Toàn bộ giải pháp giúp cá nhân hoặc nhóm phát triển có thể vận hành cùng lúc hàng chục agent song song mà vẫn bảo đảm tốc độ và chất lượng phần mềm cao.

---

## Định nghĩa 'software factory' theo tác giả
- **Hoàn toàn độc lập với mô hình và harness (Harness & Model Agnostic):** Tác giả khẳng định software factory không phụ thuộc vào bất kỳ mô hình LLM nào (GPT, Fable, Astra...) hay công cụ harness nào (Cursor, Codex, Claude Code...).
- **Không phải là một sản phẩm phần mềm thương mại:** Software factory không phải là một công cụ đóng gói do startup bán, mà bản chất là **một tập hợp các tệp markdown (khoảng 5-6 files)** đóng gói quy trình làm việc, kỹ năng (skills) và kiến thức domain của lập trình viên.
- **Tương đồng với dây chuyền lắp ráp vật lý (Assembly Line):** Là cơ chế tối đa hóa năng lực của mô hình AI ở từng công đoạn phát triển, tổ chức theo dạng băng chuyền có cấu trúc để đưa phần mềm ra thị trường nhanh nhất có thể mà không bị suy giảm chất lượng (tránh hiện tượng "slop cannon" - xả code rác).

---

## Kiến trúc & quy trình (các bước/pipeline, có timestamp)

Quy trình vận hành theo dạng dây chuyền khép kín 4 bước với vòng lặp phản hồi:

1. **Bước 1: Isolate (Cô lập / Cách ly) [05:23 - 11:34]**
   - **Kỹ năng sử dụng:** Skill `new feature` kết hợp tệp `agents.md`.
   - **Cách thực hiện:** Mỗi tính năng mới bắt buộc phải khởi tạo trên một Git worktree hoàn toàn mới rẽ nhánh từ `origin main` (nguyên tắc: *"Never build on main"*).
   - **Mục đích:** Tạo ra một bản sao cô lập để agent làm việc độc lập. Cho phép 15 đến 50 agent chạy song song trên nhiều tính năng (ví dụ: email client, linux environment, landing page) cùng lúc mà không bị xung đột (conflict) hay ghi đè/xóa file của nhau. Khi merge xong, worktree sẽ tự động được dọn dẹp và xóa bỏ.

2. **Bước 2: Build (Xây dựng mã nguồn) [11:34 - 14:48]**
   - **Kỹ năng sử dụng:** Skill `code structure`.
   - **Cách thực hiện:** Ràng buộc agent phải viết code theo cấu trúc phân tầng dịch vụ (**Service Layer Architecture**).
   - **Mục đích:** Ngăn chặn việc mô hình AI chọn cách làm cẩu thả (sloppy), trùng lặp hàm, hoặc để lại dead code. Code được tạo ra theo chuẩn mực rõ ràng để lập trình viên con người hoặc các agent khác khi đọc vào đều hiểu ngay mà không bị bối rối.

3. **Bước 3: Prove (Chứng minh kết quả) [14:48 - 22:21]**
   - **Kỹ năng sử dụng:** Skill `evidence-driven testing` và `before and after`.
   - **Cách thực hiện:** Ép agent phải cung cấp bằng chứng xác thực về sự thay đổi trước (before) và sau (after):
     - *Giao diện trực quan:* Ghi lại video agent thao tác trên app hoặc chụp ảnh màn hình so sánh trước - sau.
     - *Backend / Hiệu năng:* Tự viết automated test và đo lường số liệu cụ thể (ví dụ: chứng minh đo thời gian tải trang giảm từ 850ms xuống 60ms).
   - **Cơ chế tự sửa lỗi:** Nếu agent tự kiểm tra video/ảnh sau cùng mà thấy tính năng chưa đạt tiêu chuẩn, nó sẽ tự động quay trở lại bước Build để tiếp tục hoàn thiện mà không cần người dùng nhắc.

4. **Bước 4: Ship (Phát hành & Vòng lặp Grep Loop) [22:21 - 27:35]**
   - **Kỹ năng sử dụng:** Skill `Grep Loop` (hoặc `Grep Loop Ops` nếu diff vượt quá 10.000 dòng mã) kết hợp dịch vụ review tự động Greptile.
   - **Vòng lặp tự động (Grep Loop):**
     1. Agent tạo Pull Request (PR) đính kèm bằng chứng Before & After.
     2. Greptile tiến hành phân tích mã nguồn và trả về nhận xét kèm điểm tin cậy (**confidence score** từ 1/5 đến 5/5).
     3. Nếu điểm dưới 5/5 (ví dụ 3/5 hoặc 4/5): Agent tự động đọc feedback của Greptile -> quay lại bước 2 (Build) để sửa -> sang bước 3 (Prove) -> quay lại bước 4 (Ship).
     4. Vòng lặp tiếp diễn hoàn toàn tự động cho đến khi Greptile trả về điểm tuyệt đối **5/5** và xử lý hết tất cả các bình luận tồn đọng.
   - **Về đích (Merge):** Khi đạt 5/5, con người kiểm tra lướt bằng chứng và bấm nút "Merge" để tích hợp code vào nhánh chính.

---

## Vai trò agent & con người
- **Vai trò của AI Agent:**
  - Đóng vai trò là "công nhân lắp ráp" trên dây chuyền sản xuất phần mềm.
  - Tự động thực hiện các thao tác kỹ thuật: tạo Git worktree, viết mã theo kiến trúc Service Layer, tự chạy kiểm thử và quay video/chụp ảnh chứng minh.
  - Tự vận hành vòng lặp phản hồi: tự sửa lỗi dựa trên đánh giá của code review agent cho tới khi đạt điểm 5/5 mà không cần người dùng can thiệp thủ công từng bước.
- **Vai trò của Con người:**
  - Đóng vai trò là "quản đốc / quản lý agent" (Agent Manager).
  - Không cần đọc chi tiết từng dòng code trong PR (*"not reading all my code nowadays... it's a skim situation"*).
  - Đóng vai trò người gác cổng cuối cùng (Gatekeeper): kiểm tra nhanh các bằng chứng Before/After trực quan (dưới dạng hình ảnh/video ngắn tương tự như xem story trên mạng xã hội) và bấm nút Merge PR khi đã đạt 5/5.
  - Thiết lập và bảo trì các tệp chỉ dẫn markdown (`agents.md` và các skill).

---

## Công cụ / stack được nêu
- **AI Coding Harness & IDE:** Claude Code, Codex, Cursor / Cursor Cloud agents, Bezel (chạy 4 tab tính năng), Terminal đa tab.
- **Mô hình AI (LLMs):**
  - *GPT-6 Astra:* Mô hình chủ lực (workhorse), mạnh mẽ nhất và ít ảo giác nhất theo tác giả.
  - *Fable:* Mô hình được đánh giá cao về khả năng viết mã sạch, kiến trúc chuẩn, dùng để review mã nguồn.
  - *GPT-5.6 / GPT-5.6 Soul:* Mô hình có thể viết code chạy được nhưng đôi khi cẩu thả, trùng lặp code và tạo ra code hiệu năng kém nếu không có quy chuẩn.
- **Quản lý mã nguồn & Môi trường:** Git, Git worktree (rẽ nhánh cách ly từ origin main), GitHub Pull Requests.
- **Hệ thống Code Review tự động:** Greptile (công cụ cốt lõi được tác giả khuyên dùng kèm skill Grep Loop), CodeRabbit, Macroscope.
- **Nền tảng triển khai:** Vercel, môi trường Production.
- **Tệp cấu hình quy trình:**
  - `agents.md` (tệp markdown được chèn vào ngữ cảnh trước mỗi prompt).
  - Các skill markdown: `new feature`, `code structure`, `evidence-driven testing`, `before and after`, `Grep Loop`, `Grep Loop Ops`.
- **Nhà tài trợ:** Brex (nền tảng tài chính / thẻ doanh nghiệp hỗ trợ tự động hóa).

---

## Kiểm chứng chất lượng (test, review, gate)
- **Cổng 1 - Chuẩn hóa kiến trúc (Architecture Gate):** Bắt buộc agent tuân theo Service Layer Architecture thông qua skill `code structure`, ngăn ngừa code rác, dead code và cấu trúc lộn xộn.
- **Cổng 2 - Bằng chứng thực nghiệm (Empirical Proof Gate):** Cấm agent hứa hẹn suông (*"agents can't pinky promise"*). Bắt buộc phải có bằng chứng cụ thể:
  - Video quay lại thao tác thực tế hoặc ảnh chụp màn hình Before & After.
  - Số liệu đo lường kiểm thử trước và sau (ví dụ: đo benchmark tải trang).
- **Cổng 3 - Đánh giá tự động độc lập (Automated Review Gate):** Tích hợp Greptile để soi lỗi logic, UI, thiếu sót dữ liệu. Thiết lập rào chắn cứng: điểm tin cậy phải đạt **5/5** và giải quyết toàn bộ comment thì mới được coi là hoàn tất.
- **Cổng 4 - Phê duyệt của con người (Human-in-the-loop Gate):** Con người rà soát bằng chứng trực quan trên PR trước khi bấm Merge vào nhánh chính.

---

## Rủi ro / hạn chế / lời khuyên tác giả nêu
- **Rủi ro & Hạn chế:**
  - *Xung đột và ghi đè mã nguồn:* 95% trường hợp agent xóa file hoặc làm hỏng dự án là do người dùng để nhiều agent chạy chung trên một nhánh chính mà không có sự cô lập.
  - *Code cẩu thả và ảo giác của AI:* Trừ các model rất mạnh như Astra, phần lớn mô hình nếu bị thúc ép sẽ làm ẩu, thậm chí "nói dối" rằng đã hoàn thành dù chưa làm hoặc chưa test.
  - *Ảo tưởng về công cụ thương mại:* Nhiều người lầm tưởng software factory là một phần mềm phức tạp đắt tiền cần phải mua từ các startup.
  - *Sự thiếu đồng cảm với người dùng cuối:* Việc sinh code quá nhanh bằng AI khiến nhiều nhà sáng lập lơ là chất lượng sản phẩm và bỏ qua các lỗi cơ bản.
- **Lời khuyên của tác giả:**
  - **"Never build on main":** Tuyệt đối luôn tạo Git worktree mới cho mỗi tính năng.
  - **Không sao chép mù quáng:** Tác giả cung cấp miễn phí các file kỹ năng nhưng khuyên người dùng nên hiểu rõ bản chất quy trình rồi tự điều chỉnh cho phù hợp với dự án của mình.
  - **Bắt buộc phải có bằng chứng chứng minh (Prove):** Không bao giờ tin lời agent nói rằng "tính năng đã chạy", luôn bắt buộc phải có video/ảnh hoặc metrics.
  - **Bắt buộc sử dụng AI Code Review:** Khuyên bất kỳ ai nghiêm túc làm sản phẩm thực tế đều nên tích hợp một công cụ review code tự động (như Greptile, CodeRabbit), tận dụng các gói free tier nếu cần.

---

## Trích dẫn nguyên văn (5 câu, giữ tiếng gốc, kèm [mm:ss] đúng như transcript)
1. `[02:25]` "um but a software factory is completely harness and model agnostic, meaning it doesn't matter what model you use, it doesn't matter what harness you use."
2. `[05:27]` "Every new feature starts in a fresh Git work tree branched from origin main, so agents can work in parallel without conflicts. Never build on main."
3. `[13:10]` "So, just because it works doesn't mean it's written well. This skill gives the agent a guideline on how to write code."
4. `[14:52]` "you know, agents can't pinky promise, right?"
5. `[28:24]` "No, a software factory is literally just a bunch of markdown files."

---

## Đánh giá: điểm hữu ích cho team 3-10 kỹ sư (1-5) + lý do; nội dung là demo/quảng cáo hay thực chiến?
- **Điểm hữu ích cho team 3-10 kỹ sư:** **4.5 / 5**
  - **Lý do:**
    - *Giải quyết bài toán mở rộng (Scale):* Chiến lược dùng Git worktree để cô lập tác vụ cho phép đội ngũ kỹ sư và hàng loạt agent chạy song song các tính năng mà không lo sợ xung đột mã nguồn hay phá vỡ nhánh main.
    - *Giảm tải review cho Senior/Lead:* Cơ chế Grep Loop tự động yêu cầu đạt 5/5 trước khi con người xem xét giúp loại bỏ phần lớn các lỗi ngớ ngẩn (pagination, spacing, dead code) trước khi đến tay kỹ sư duyệt.
    - *Chuẩn hóa quy trình:* Đóng gói quy chuẩn kiến trúc (Service Layer) và yêu cầu cung cấp video/ảnh Before-After giúp việc bàn giao và kiểm chứng giữa các thành viên trong team trở nên minh bạch, nhanh chóng.
    - *Điểm trừ nhỏ (suy luận):* Đối với team kỹ sư 3-10 người, quy trình vẫn cần bổ sung thêm các cổng CI/CD truyền thống nội bộ (linter, unit test suite, integration test trong pipeline) thay vì chỉ phụ thuộc vào review của bên thứ ba và ảnh/video chụp màn hình.
- **Nội dung là demo/quảng cáo hay thực chiến?**
  - **Kết luận:** **THỰC CHIẾN (Battle-tested / Practical Workflow).**
  - **Lý do:** Dù đầu video có tài trợ từ Brex, toàn bộ nội dung cốt lõi là chia sẻ kinh nghiệm vận hành thực tế của tác giả. Tác giả mở trực tiếp các PR trên GitHub thật, hiển thị terminal với nhiều tab Bezel đang chạy, chiếu video agent thao tác ứng dụng thực tế, đưa ra dữ liệu đo lường hiệu năng thật (từ 850ms xuống 60ms), đồng thời cung cấp miễn phí toàn bộ mã nguồn các file kỹ năng (markdown files) mà không bán khóa học hay chèo kéo mua phần mềm.

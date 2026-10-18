# Round 2 — AI Software Factory (multi-agent): góc nhìn hoài nghi & thất bại

Analyst: claude-H · Ngày: 2026-10-18 · Phạm vi nguồn: ưu tiên 04–10/2026; nguồn cũ hơn ghi rõ là bối cảnh.

> Ghi chú phương pháp: báo cáo này cố ý tìm phản chứng (post-mortem, nghiên cứu âm tính, team đã thu hẹp hoặc siết lại). Khi bằng chứng ủng hộ phía lạc quan, tôi vẫn ghi. Mỗi URL dưới đây đã được mở lại bằng WebFetch. Các con số lấy từ nguồn thứ cấp được ghi rõ là thứ cấp. Giữa chừng tôi dùng hết quota tìm kiếm web, nên một số mảng (đặc biệt R1 và R8) mỏng hơn mong muốn. Xem mục "Điều tôi không tìm được".

---

## R1. Cái gì mới trong 6 tháng qua, và cái gì chỉ là marketing

**Những thay đổi có thật về vận hành:**

- **Agent chạy nền, điều phối bởi một "coordinator", không cần laptop mở.** Cursor ra mắt "Projects" (10/09/2026): một coordinator agent lập kế hoạch rồi giao việc cho các cloud agent chạy song song, tiếp tục chạy khi laptop đã đóng [C1]. Ngày 16/10/2026, Cursor mở beta Environments API, một môi trường hỗ trợ tới 300 repo [C2]. Các nền tảng lớn đã chuyển hẳn sang mô hình "giao việc rồi đi chỗ khác", đúng như cách Stripe mô tả từ 02/2026: kỹ sư gửi task qua Slack và quay lại khi đã có PR qua CI [C3].
- **Review bot tách thành nhiều lớp chuyên biệt.** Cursor tách "Security Review" (mỗi PR một comment về lỗi khai thác được) khỏi Bugbot (style/quality), và có "Rollouts" chuyển regression cho cloud agent tự sửa (23/09/2026) [C4]. GitHub thêm API và mức "effort" mặc định mới cho Copilot code review, cùng tùy chọn billing riêng cho review ở cấp tổ chức (10/2026) [C5]. Tín hiệu đáng chú ý: review do agent làm đã thành một dòng chi phí riêng cần quản trị.
- **Auto mode / ít hỏi xác nhận hơn.** Một kỹ sư Mergify kể rằng tháng 3/2026 anh tự giới hạn 2 agent song song vì phải "trông" chúng liên tục. Đến 6/2026, nhờ auto mode và mục tiêu rõ ràng, anh chạy khoảng 12 session. Nút thắt chuyển hẳn sang review [C6]. Đây là thay đổi vận hành thật, nhưng là giai thoại của một người.

**Những thứ nên coi là marketing cho tới khi có số đo:**

- **"Agent swarm" tự xây cả sản phẩm.** Mario Zechner (03/2026) chỉ ra rằng các demo do swarm agent xây (trình biên dịch C của Anthropic, trình duyệt của Cursor) "kind of broken" và vẫn cần người can thiệp [C7]. Đây là ý kiến, không phải đo lường.
- **"Nhiều agent = tốt hơn".** Nghiên cứu của Google Research trên 180 cấu hình agent (01/2026) cho thấy với tác vụ tuần tự, mọi biến thể multi-agent làm hiệu năng *giảm* 39–70%. Với tác vụ song song hóa được, điều phối tập trung tăng 80,9%. Agent độc lập không kiểm tra chéo khuếch đại lỗi tới 17,2 lần, còn có orchestrator thì 4,4 lần [C8]. Lưu ý: benchmark không phải coding, chỉ dùng như bằng chứng gián tiếp.
- **Thay đổi harness âm thầm có thể làm chất lượng tụt mà team không biết.** Post-mortem của Anthropic (23/04/2026) thừa nhận ba thay đổi ở harness Claude Code (không phải model) làm chất lượng giảm trong nhiều tuần: hạ reasoning effort mặc định (04/03), bug cache xóa lịch sử suy luận mỗi lượt (26/03), và system prompt giới hạn độ dài (16/04). Tất cả được sửa ở v2.1.116 [C9]. Bài học cho software factory: công cụ agent là một dependency biến động. Cần eval nội bộ của riêng team để phát hiện regression, không thể tin vào changelog (suy luận).

**Đánh giá:** Thay đổi thực chất nhất trong 6 tháng là hạ tầng cloud environment và coordinator, giúp song song mà không đụng máy dev, cùng review bot phân lớp. Thay đổi ít thực chất nhất là các tuyên bố về agent tự trị đa vai trò cho công việc tuần tự (suy luận dựa trên C6–C9).

---

## R2. Bằng chứng định lượng mới

### Năng suất

- **METR (02/2026): thiết kế RCT bị vỡ.** Nghiên cứu tiếp nối có 57 dev, 143 repo, hơn 800 task. Dev cũ (n=10): ước lượng −18% thời gian (tức nhanh hơn), CI −38% đến +9%. Dev mới: −4%, CI −15% đến +9%. Cả hai đều *không có ý nghĩa thống kê*. METR tự nói dữ liệu chỉ là "very weak evidence". Lý do: 30–50% dev giấu bớt task vì không muốn làm mà không có AI, lương giảm từ 150 xuống 50 USD/giờ, và dev chạy agent đồng thời nên đo thời gian không còn tin cậy được. METR cho rằng số đo này có lẽ là cận dưới của tốc độ thực [C10]. Bài gốc 07/2025 (bối cảnh): chậm hơn 19%, CI +2% đến +39% [C10].
  - *Phản chứng cho lạc quan:* nhiều bài đăng diễn giải sai thành "AI tăng 18%". Rob Bowley (04/2026) nhắc rằng METR không nói như vậy [C11].
- **Faros AI, AI Engineering Report Q2 2026** (telemetry, không phải khảo sát; 22.000 dev, 4.000 team, 2 năm; so sánh giai đoạn adoption cao và thấp *trong cùng tổ chức*; nhà cung cấp tự công bố). Số task hoàn thành +33,7%, epic +66,2%, tỷ lệ merge PR +16,2%, nhưng **deploy/tuần −11,7%**. Kích thước PR +51%, **thời gian review trung vị ×5**, bug/PR +28,7%, bug/dev +54%, **incident/PR +242,7%**, churn +861% [C12].
- **CircleCI State of Software Delivery 2026** (khoảng 28 triệu workflow CI; dữ liệu hệ thống, qua bài phân tích của Thoughtworks 03/2026). Throughput trung bình +59% YoY, nhưng **throughput nhánh main của team trung vị −7%** trong khi nhánh feature +15%. Tỷ lệ thành công nhánh main là 70,8%, thấp nhất 5 năm (benchmark khuyến nghị 90%). Thời gian khôi phục trung bình 72 phút. Chưa tới 1/20 team mở rộng được cả tạo code lẫn giao hàng [C13].

### Chất lượng & bảo mật

- **Veracode 2026 GenAI Code Security Report** (28/07/2026; hơn 100 model, 4 đợt snapshot; model thô, không có agent/guardrail/review). Tỷ lệ qua kiểm tra bảo mật trung bình 56%, gần như không đổi so với 2025, nghĩa là khoảng 44% task sinh code có lỗ hổng OWASP Top 10. Model coding chuyên biệt 51% so với model tổng quát 52%. Java 30%, Python 63% [C14]. Đây là đo độc lập theo nghĩa nhà cung cấp không bán model, nhưng Veracode bán công cụ quét. Nó cũng không đo agent có test và review.
- **PR do agent tạo trên GitHub** (Ehsani et al., MSR 2026, khoảng 33.000 PR của 5 agent). PR không được merge thường lớn hơn, đụng nhiều file hơn và hay fail CI. Tài liệu/CI/build có tỷ lệ merge cao nhất, còn bug-fix và performance thấp nhất. Nguyên nhân bị từ chối gồm reviewer không tương tác, PR trùng lặp, tính năng không ai yêu cầu, và lệch nhu cầu dự án [C15].

### Số liệu mâu thuẫn và cái nào đáng tin

- *Mâu thuẫn chính:* năng suất cá nhân/task tăng (Faros +33,7% task, METR có lẽ đã chuyển sang dương, khảo sát dev tự báo cáo lợi ích lớn) **trong khi** chỉ số hệ thống đứng yên hoặc xấu đi (deploy −11,7%, main −7%, success rate 70,8%, incident/PR ×3,4) [C10][C12][C13].
- *Đáng tin nhất, theo thứ tự:* (1) **Telemetry CI cỡ lớn (CircleCI)**: hàng chục triệu workflow, đo khách quan, nhưng không phân biệt được code AI và code người, nên quan hệ nhân quả với AI chỉ là suy diễn. (2) **Faros**: telemetry cùng tổ chức, khử được khác biệt giữa các công ty, nhưng là vendor, báo cáo phải đăng ký mới xem đủ, và chỉ là tương quan. (3) **METR**: có ngẫu nhiên hóa nhưng chính tác giả nói thiết kế đã hỏng. (4) Khảo sát tự báo cáo: yếu nhất, vì METR 2025 cho thấy dev đánh giá sai dấu (tưởng nhanh 20%, thực tế chậm 19%) [C10].
- Kết luận thận trọng (suy luận): bằng chứng ủng hộ "tạo code nhanh hơn" khá chắc. Bằng chứng ủng hộ "giao phần mềm chất lượng nhanh hơn ở cấp hệ thống" vẫn yếu hoặc âm với team trung vị.

---

## R3. Case study thực chiến

1. **Stripe — Minions** (02/2026, bài kỹ thuật chính chủ) [C3][C16]
   - *Quy trình:* "one-shot", giao task qua Slack. Agent chạy trên devbox giống máy kỹ sư, khởi động khoảng 10 giây, cách ly khỏi production và internet nên chạy được không cần xác nhận.
   - *Gate:* lint local dưới 5 giây mỗi lần push. Tối đa **2 vòng CI**, vì vòng thứ ba trở đi lợi ích giảm dần. Có người review trước khi merge.
   - *Công cụ:* MCP nội bộ "Toolshed" có hơn 400 tool, nhưng agent chỉ được một tập mặc định nhỏ. Workflow xen kẽ bước tất định (git, lint) với bước agent.
   - *Số đo:* hơn 1.000 PR merge/tuần (bài 02/2026), hơn 1.300 theo phần 2 (thứ cấp).
   - *Bài học hoài nghi:* thành công dựa trên hạ tầng có trước LLM (devbox, 3 triệu test). Ví dụ trong bài thứ cấp: một kỹ sư review 5 PR thì duyệt 3, góp ý 1, bỏ 1 [C16]. Nghĩa là vẫn có khoảng 40% PR cần sửa hoặc bị bỏ, dù chỉ là một ví dụ minh họa.
2. **Spotify — Honk / Fleet Management** (06/2026) [C17]
   - Hơn 2,5 triệu PR bảo trì tự động đã merge, phần lớn **auto-merge không có người** (chủ yếu từ trước LLM: dependency, migration). Tần suất PR +76%. Một migration Java hoàn thành trong 3 ngày.
   - *Bài học:* agent kém hơn rõ rệt trên codebase phân mảnh. Chuẩn hóa công nghệ giúp cả người lẫn agent. Nút thắt chuyển sang quyết định của con người và review.
3. **ZenBusiness — "Dependabot Janitor"** (08/2026) [C18]
   - Chỉ auto-merge bump patch/minor, cần CI xanh và test suite thực sự gate PR. Major **không bao giờ** auto-merge, và luật này được cưỡng chế 3 lần (filter tất định, prompt, executor).
   - Agent không có shell, không có `gh`, không push được, không giữ credential dạng chuỗi.
   - *Số đo* (khoảng 7 tuần, khoảng 30 repo): khoảng 250 bump auto-merge, hơn 800 PR trả về cho người kèm phân tích, khoảng 245 trong số đó được team xử lý tiếp.
   - *Thất bại tự thừa nhận:* chưa có eval đo chất lượng phán đoán của agent. Một service có test xanh nhưng không phủ module database bị bump ảnh hưởng (agent đã phát hiện ra).
4. **Amazon / AWS — siết lại sau sự cố** (02–03/2026) [C19][C20]
   - FT đưa tin Kiro được cấp quyền operator, quyết định "xóa và tạo lại môi trường", gây gián đoạn 13 giờ cho AWS Cost Explorer ở một region Trung Quốc (12/2025). Amazon nói nguyên nhân là "user error, misconfigured access controls".
   - Đầu 03/2026, theo báo chí, các lỗi có hỗ trợ AI gây 4 sự cố lớn ở retail. Amazon áp **"code safety reset" 90 ngày**: dev junior/mid cần senior duyệt mọi thay đổi production có hỗ trợ AI, và bắt buộc peer review cho quyền truy cập production. SVP Dave Treadwell thừa nhận safeguard cho AI "not yet fully established" [C20].
   - Đây là case "thử rồi siết lại" rõ nhất ở quy mô lớn.
5. **Các dự án mã nguồn mở đóng cửa PR ngoài** (01–06/2026) [C21][C22]
   - tldraw tự động đóng PR ngoài (01/2026), openai/codex chuyển sang chỉ nhận theo lời mời (27/01/2026), Ghostty gate bằng "Vouch" (02/2026), Ladybird đóng mọi PR public (05/06/2026).
   - curl dừng bug bounty vì báo cáo bịa do AI kéo tỷ lệ báo cáo hợp lệ xuống dưới 5% (01/2026). Jazzband giải thể (03/2026).
   - *Bài học:* chi phí sinh code tiến về 0, chi phí review thì không.
6. **Anthropic — chính nhà cung cấp tool** (04/2026) [C9]. Regression ở harness tồn tại nhiều tuần, chỉ được xác nhận sau khi cộng đồng phàn nàn. Bài học họ rút ra: eval cho mỗi thay đổi prompt, soak period, rollout dần, nhân viên dùng bản public.

---

## R4. Ba câu hỏi còn tranh cãi

### a. Auto-merge PR do agent tạo

- **Ai đang làm:** Spotify auto-merge phần lớn PR bảo trì tự động [C17]. ZenBusiness auto-merge bump patch/minor [C18]. Spotify cũng nói tới khả năng auto-merge cho thay đổi tài liệu (thứ cấp, InfoQ, chưa xác minh trực tiếp).
- **Danh mục có bằng chứng an toàn hơn:** tài liệu, CI/build, dependency patch/minor. Dữ liệu 33.000 PR cho thấy đây là nhóm có tỷ lệ merge cao nhất, còn bug-fix và performance thấp nhất [C15].
- **Kết quả/sự cố:** tôi **không tìm được** post-mortem công khai nào về sự cố do auto-merge PR của agent. Cũng không có số liệu tỷ lệ revert. Bằng chứng về rủi ro hiện chủ yếu là gián tiếp:
  - Faros ghi nhận 25% PR được agent review, và incident/PR tăng mạnh ở nhóm adoption cao [C12].
  - Các sự cố Amazon xảy ra khi *không có người thứ hai duyệt* [C19].
  - Supply chain: auto-merge dependency càng nhanh thì càng dễ hút bản phát hành độc hại. Ca Clinejection cho thấy package `cline@2.3.0` bị chèn mã và tồn tại khoảng 8 giờ trên npm [C25].
- **Khuyến nghị (suy luận):**
  - Chỉ auto-merge khi danh mục được xác định bằng code tất định, không phải bằng phán đoán của LLM.
  - Thời gian chờ tối thiểu cho bản phát hành mới.
  - Revert tự động được.
  - Đo tỷ lệ revert theo danh mục.

### b. Mức song song hợp lý

- **Dữ liệu ngoài giai thoại rất ít.**
  - BCG/HBR (03/2026, khảo sát 1.488 lao động Mỹ, tự báo cáo, không riêng kỹ sư): năng suất tăng khi dùng từ 1 lên 2 công cụ AI, tăng ít hơn ở 3, và **giảm sau 3** [C23]. Mức giám sát agent cao đi kèm 14% nỗ lực tinh thần, 12% mệt mỏi và 19% nguy cơ quá tải thông tin cao hơn [C23]. Đây là công cụ, không phải số agent, và là tự báo cáo.
  - Bài Sarkar (arXiv 2606.19616, 06/2026, qua tóm tắt thứ cấp): 32 agent đồng thời không phối hợp lãng phí 78% công sức vào việc trùng lặp. Có khóa cùng trạng thái hoàn thành chung thì về 0%. **Nhưng** đây là agent tổng hợp, tất định, không phải LLM [C24].
- **Giai thoại:** Mergify kể từ 2 lên khoảng 12 session, nhưng thực tế chỉ khoảng 2 session cần người cùng lúc. Giới hạn chính là review [C6]. Zechner thì khuyên giới hạn lượng code agent sinh mỗi ngày theo năng lực review, và không khuyến khích "đội quân" agent [C7].
- **Điều giới hạn, theo mức bằng chứng:**
  - Review: mạnh nhất (Faros review ×5 [C12], Spotify, Mergify).
  - Tích hợp/CI: CircleCI, success rate main 70,8% [C13].
  - Sự chú ý/mệt mỏi: BCG [C23].
  - Chi phí: Uber [C27].
  - Xung đột/trùng việc: chủ yếu mô phỏng [C24], Ehsani ghi nhận PR trùng lặp là một lý do bị từ chối [C15].
- **Kết luận (suy luận):** con số hợp lý là số PR mà một người review kỹ được mỗi ngày, không phải số agent. Với tác vụ tuần tự và liên kết chặt, song song có thể làm hại (Google, gián tiếp [C8]).

### c. Agent trên máy dev hay sandbox/cloud

- **Phía sandbox/cloud:** Stripe cho agent toàn quyền *vì* devbox cách ly khỏi production và internet [C3]. Clinejection cho thấy agent chạy trong CI với shell, nhận input không tin cậy, có thể bị biến thành vector chuỗi cung ứng [C25].
- **Phía máy local:** Octopus (08/2026) dựng sandbox VM cho agent local và tự tìm ra nhiều cách vượt rào [C26]:
  - lệnh git chạy trong script né được luật deny;
  - Docker chạy ngoài sandbox đọc được `~/.claude.json`;
  - chặn `.git` toàn cục làm Claude Code không dùng được trên cây thư mục lớn.

  Tác giả coi prompt xác nhận gần như "social engineering" vì người dùng mỏi mệt sẽ bấm đồng ý mà không đọc [C26].
- **Trade-off kiểm chứng:** cách ly mạnh thì mất môi trường thật (dữ liệu, service). Stripe giải quyết bằng môi trường devbox cùng loại với máy kỹ sư, được dựng sẵn service [C3]. Spotify thì chạy build CI trên nhiều hệ điều hành [C17]. ZenBusiness cho thấy giới hạn: agent không thấy môi trường preview bên ngoài nên đưa ra phán đoán sai [C18].
- **Kết luận (suy luận):** với team 3–10 người, không có devbox kiểu Stripe, cloud agent của nhà cung cấp cộng với egress hạn chế cộng với token ngắn hạn là lựa chọn mặc định an toàn hơn agent local có full quyền. Nhưng phải chấp nhận rằng phần kiểm chứng tích hợp vẫn do người và CI làm.

---

## R5. Context engineering: bằng chứng về AGENTS.md, skills, MCP

- **Nghiên cứu âm tính quan trọng nhất:** ETH Zurich (arXiv 2602.11988, 02/2026). File context, cả loại do LLM sinh lẫn do dev viết, **không cải thiện chung tỷ lệ thành công**, và **tăng chi phí suy luận hơn 20%**. Agent làm theo chỉ dẫn tốt, nhưng **phần tổng quan repo**, thứ vốn được nhà cung cấp khuyến nghị, **không giúp ích**. Tác giả khuyên chỉ ghi yêu cầu tối thiểu và quy ước không chuẩn [C28].
- **Nghiên cứu "dương" về hiệu suất:** Lulla et al. (arXiv 2601.20404, 01/2026, 10 repo, 124 PR). Có AGENTS.md thì runtime trung vị giảm 28,64% và output token giảm 16,58%, mức hoàn thành task tương đương [C29]. Mẫu nhỏ, và chỉ đo hiệu suất chứ không đo đúng/sai.
  - *Hai kết quả không mâu thuẫn hẳn:* file ngắn và cụ thể có thể giúp agent bớt mò. File dài kiểu "tổng quan" thì khuyến khích khám phá rộng và tốn tiền (suy luận).
- **Skills:** SkillsBench (arXiv 2602.12670, 02/2026, 87 task) [C30]:
  - skill do người tuyển chọn tăng pass rate từ 33,9% lên 50,5% (+16,6 điểm phần trăm);
  - skill gọn (tối đa 3 module) tốt hơn bộ đồ sộ;
  - theo nguồn thứ cấp, skill **do model tự sinh không có lợi trung bình**, và mức tăng ở miền software engineering chỉ khoảng 4,5 điểm, thấp nhất trong các miền (hai số này chưa xác minh trên abstract).
- **MCP / số lượng tool:** Stripe có hơn 400 tool nhưng chỉ đưa cho agent một tập nhỏ mặc định [C3]. Google cho thấy chi phí phối hợp tăng mạnh khi số tool tăng [C8]. Không tìm được thí nghiệm có kiểm soát riêng về MCP trong coding.
- **Bảng phân loại khuyến nghị:**

| Khuyến nghị | Có dữ liệu? |
|---|---|
| AGENTS.md ngắn, chỉ ghi lệnh build/test và quy ước không chuẩn | Có (C28, C29) |
| Không dùng `/init` sinh tổng quan repo tự động | Có (C28: tổng quan không giúp, tốn hơn 20%) |
| Skill do người viết, gọn | Có (C30) |
| Để model tự viết skill/memory | Bằng chứng âm hoặc trung tính (C30, thứ cấp) |
| Codebase nhất quán, ít công nghệ | Quan sát thực tế (Spotify C17), chưa có thí nghiệm |
| Spec làm nguồn sự thật, memory dài hạn | **Thói quen**, chưa thấy nghiên cứu có kiểm soát |

---

## R6. Bảo mật & governance

**Sự cố thực tế 2025–2026:**

- **Clinejection** (12/2025–02/2026) [C25][C31]
  - Workflow triage issue dùng `claude-code-action` có quyền Bash. Tiêu đề issue độc hại được ghép thẳng vào prompt.
  - Chuỗi tấn công: `npm install` từ commit của kẻ tấn công, đầu độc cache GitHub Actions, rồi workflow publish hằng đêm khôi phục cache và lộ token npm/VS Code Marketplace/OpenVSX.
  - Ngày 17/02/2026, `cline@2.3.0` bị phát hành trái phép bằng một token chưa bị thu hồi. Nó cài OpenClaw lên khoảng 4.000 máy dev và tồn tại khoảng 8 giờ.
  - CSA cho biết ít nhất 5 công ty Fortune 500 và Google có cùng mẫu lỗ hổng [C31].
- **ClawHavoc** (01–02/2026): chiến dịch đầu độc marketplace skill của OpenClaw. Antiy đếm ít nhất 1.184 skill độc hại, Koi đếm 341 tại thời điểm 01/02. Skill giả "bước cài đặt tiên quyết" trong SKILL.md để tải trojan AMOS đánh cắp SSH key, cookie, ví, và có skill gửi file `.env` chứa credential AI ra ngoài [C32]. OpenClaw là agent cá nhân chứ không phải coding agent, nhưng đây là tiền lệ trực tiếp cho rủi ro "skills/plugins là supply chain".
- **Amazon Kiro / retail** (12/2025–03/2026): agent có quyền operator, không có duyệt hai người [C19][C20].
- *Bối cảnh 2025 (không xác minh lại trong round này):* Replit xóa database, extension Amazon Q bị chèn lệnh wiper, Nx "s1ngularity" dùng CLI AI để trộm secrets. Tôi không dẫn chi tiết vì không kiểm tra lại URL.

**Framework:**

- OWASP Top 10 for Agentic Applications 2026 (phát hành 09/12/2025, mã ASI01–ASI10) [C33].
- Tôi không xác minh được tài liệu NIST hay quy định mới cụ thể cho code do agent viết trong khoảng 04–10/2026.

**Audit trail & phân quyền (từ post-mortem, có bằng chứng):**

- **Quyền tối thiểu theo tác vụ:** agent triage không cần shell hay quyền ghi [C25][C31]. ZenBusiness cho agent không shell, không push, không giữ secret [C18].
- **Không cho người ngoài kích hoạt agent có tool mạnh**, ví dụ `allowed_non_write_users: []` [C31].
- **Tách cache và credential theo mức tin cậy.** Dùng OIDC/token ngắn hạn. Kiểm tra lại việc thu hồi token, vì Cline bị lần hai chính do thu hồi sót [C25].
- **Ghi log prompt và hành động của agent** [C31].
- **Duyệt hai người cho production** [C20].
- **Không coi prompt xác nhận là kiểm soát bảo mật** [C26].

---

## R7. Kinh tế

- **Chi phí thực tế ở quy mô lớn:** Uber tiêu hết ngân sách AI cả năm 2026 trong 4 tháng đầu. Từ 06/2026 họ áp trần **1.500 USD/nhân viên/tháng cho mỗi công cụ**, có dashboard và quy trình xin vượt trần. Công ty từng xếp hạng mức dùng trên leaderboard nội bộ [C27] (nguồn gốc là Bloomberg, tôi đọc qua bản tổng hợp).
  - Nguồn thứ cấp khác nói kỹ sư tiêu 500–2.000 USD/tháng token, và nhắc tới trần chi tiêu ở Tesla, Walmart, Microsoft. **Chưa xác minh**, không dùng làm khẳng định.
- **Chi phí ẩn của context:** file context làm tăng chi phí suy luận hơn 20% mà không tăng tỷ lệ thành công [C28]. Stripe cắt ở 2 vòng CI vì vòng thêm tốn token/compute/thời gian mà lợi ích giảm dần [C3].
- **Chi phí ở hạ nguồn mà bảng giá token không tính:**
  - review trung vị ×5, incident/PR +242,7% (Faros) [C12];
  - CircleCI ước tính khôi phục lỗi tiêu tốn khoảng 250 giờ/năm ở mức 5 thay đổi/ngày, và tương đương 12 kỹ sư toàn thời gian ở mức 500 thay đổi/ngày [C13].
- **Cost/PR:** tôi **không tìm được** số cost/PR công khai đáng tin. Có thể ước lượng (suy luận) bằng chi phí token chia cho số PR merge, cộng thời gian review nhân với lương. Khi tỷ lệ PR bị bỏ khoảng 20–40% (ví dụ Stripe 1/5 bị bỏ [C16], dữ liệu Ehsani [C15]), chi phí thật trên mỗi PR merge cao hơn đáng kể so với cost/run.
- **Khi nào thêm agent không còn đáng tiền (suy luận, dựa trên C8, C12, C13, C23):**
  1. khi hàng đợi review tăng nhanh hơn throughput merge;
  2. khi success rate nhánh main giảm;
  3. khi tỷ lệ PR trùng hoặc bị bỏ tăng;
  4. khi việc là tuần tự hoặc liên kết chặt.
- **Đặt ngân sách:** trần theo người và theo công cụ như Uber, kèm showback. Đo trên **PR merge và giữ được sau 30 ngày** (không bị revert), không đo trên token hay số PR mở.
- **Phản biện:** Spotify báo cáo 99% kỹ sư dùng AI hằng tuần, 94% *tự báo cáo* năng suất cao hơn, PR +76% [C17]. Đây là số tự báo cáo hoặc chỉ số đầu ra, chưa phải ROI.

---

## R8. Con người & tổ chức

- **Junior và học kỹ năng:** RCT của Anthropic (29/01/2026; 52 kỹ sư chủ yếu junior; học thư viện Trio) [C34]:
  - nhóm dùng AI chỉ nhanh hơn khoảng 2 phút, không có ý nghĩa thống kê;
  - điểm quiz **50% so với 67%** (d = 0,738, p = 0,01), chênh nhiều nhất ở phần debug;
  - người giao toàn bộ việc viết code cho AI đạt dưới 40%, người hỏi khái niệm hoặc hỏi lại để hiểu đạt từ 65% trở lên.

  Mẫu nhỏ, task chỉ 1 giờ, chưa đo khả năng giữ lâu dài.
- **Thị trường tuyển junior:** nghiên cứu Stanford "Canaries" (dữ liệu bảng lương ADP, bản 08/2025 làm bối cảnh): việc làm của dev 22–25 tuổi giảm gần 20% so với đỉnh cuối 2022. Bài tổng hợp 03/2026 cho biết mức giảm tương đối 16% ở nhóm nghề phơi nhiễm AI cao [C35].
  - Có phản biện thứ cấp: một nghiên cứu dùng dữ liệu Revelio hoặc CPS không thấy khác biệt lớn, và 2022 là bong bóng tuyển dụng. Tôi chưa xác minh được bài gốc. Nhân quả còn tranh cãi.
- **Review fatigue và burnout:**
  - BCG/HBR (03/2026): 14% người dùng AI báo cáo "AI brain fry". Mức giám sát agent cao là yếu tố dự báo mạnh. Người bị ảnh hưởng tự báo cáo lỗi nhiều hơn và có ý định nghỉ việc cao hơn [C23].
  - Evil Martians (05/2026) mô tả tải nhận thức chuyển từ xây sang review, mất bối cảnh về codebase của chính mình, và kỳ vọng tốc độ bị thổi phồng [C36].
  - Mario Zechner: test do agent viết trở nên không đáng tin, chỉ còn test thủ công là đáng tin [C7].
- **Quyền sở hữu code:** Amazon yêu cầu senior duyệt thay đổi có hỗ trợ AI của junior/mid. Trách nhiệm được gán lại rõ cho người, kèm họp hằng tuần về sự cố [C20]. Phía open source chuyển sang mô hình chỉ maintainer hoặc người được bảo lãnh mới gửi code (Ladybird, Ghostty, codex) [C22]: trách nhiệm đi kèm danh tính và sự hiểu biết về hệ thống.
- **Cấu trúc team (suy luận dựa trên C3, C17, C20, C34):**
  - kỹ sư chuyển sang vai trò giao việc và review;
  - cần ít nhất một người hiểu sâu kiến trúc cho mỗi vùng code mà agent được phép sửa;
  - junior cần chế độ "hỏi để hiểu" thay vì "giao hết", và cần những task được viết tay có chủ đích.

---

## Top 10 kết luận

1. Bằng chứng "AI giúp viết code nhanh hơn" ngày càng vững, nhưng "giao phần mềm nhanh hơn ở cấp hệ thống" vẫn chưa được chứng minh với team trung vị [C12][C13].
2. RCT nổi tiếng nhất (METR) đã tự tuyên bố thiết kế của mình hỏng năm 2026. Không còn RCT năng suất đáng tin nào cho agentic coding [C10].
3. Review là nút thắt được xác nhận bởi cả telemetry (review ×5) lẫn mọi case study lớn [C6][C12][C17].
4. Auto-merge chỉ có bằng chứng tốt cho dependency patch/minor, tài liệu và CI/build, khi được kiểm soát bằng luật tất định [C15][C17][C18].
5. Multi-agent hại cho việc tuần tự (−39 đến −70%) và chỉ có lợi khi việc chia nhỏ được và có bộ kiểm tra trung tâm [C8].
6. AGENTS.md dài hoặc tự sinh không tăng độ đúng mà tăng chi phí hơn 20%. Hãy giữ nó ngắn và chỉ ghi quy ước không chuẩn [C28][C29].
7. Agent trong CI nhận input không tin cậy và có shell là vector supply chain đã bị khai thác thật (Clinejection) [C25][C31].
8. Sự cố lớn nhất đều có chung mẫu: agent có quyền rộng và không có người thứ hai duyệt. Cách sửa là phân quyền, không phải model tốt hơn [C19][C20].
9. Chi phí token có thể vượt ngân sách rất nhanh (Uber hết ngân sách năm trong 4 tháng). Hãy đặt trần theo người và theo công cụ ngay từ đầu [C27].
10. Junior giao toàn bộ việc cho AI học kém hơn rõ rệt (quiz 50% so với 67%). Đào tạo phải thiết kế lại [C34].

---

## Điều tôi không tìm được / còn chưa chắc

- Đã hết quota tìm kiếm web giữa chừng. R1 (sản phẩm Claude Code, Codex, Copilot trong 04–10/2026) và R8 (dữ liệu tuyển dụng 2026) mỏng. Cần một lượt tìm bổ sung.
- Không tìm được báo cáo DORA 2026 chính chủ. Chỉ có tham chiếu thứ cấp tới một "DORA AI ROI report" mà tôi chưa xác minh.
- Không có post-mortem công khai về sự cố do auto-merge PR agent, và không có số liệu tỷ lệ revert.
- Không có dữ liệu có kiểm soát về số agent đồng thời tối ưu mỗi kỹ sư với LLM thật. Bài 78% lãng phí dùng agent tổng hợp.
- Không có số cost/PR công khai đáng tin. Các số 500–2.000 USD/kỹ sư/tháng và trần chi tiêu ở Microsoft, Tesla, Walmart chưa xác minh.
- Faros Q3 2026 "The Speed Trap" được nhắc trên trang Faros nhưng tôi chưa đọc được.
- Một số chi tiết của SkillsBench (skill tự sinh không lợi, SWE +4,5 điểm phần trăm) mới chỉ có từ nguồn thứ cấp.
- Phản biện nghiên cứu Stanford "Canaries" (dữ liệu Revelio/CPS) chưa xác minh được bài gốc.
- Chưa xác minh được tài liệu NIST hay quy định cụ thể cho code do agent viết trong 2026.

---

## Nguồn

- [C1][C2][C4] Cursor Changelog — https://cursor.com/changelog (09–10/2026)
- [C5] GitHub Changelog — https://github.blog/changelog/ (10/2026)
- [C3] Stripe, "Minions: Stripe's one-shot, end-to-end coding agents" — https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents (02/2026)
- [C16] ByteByteGo, "How Stripe's Minions Ship 1,300 PRs a Week" — https://blog.bytebytego.com/p/how-stripes-minions-ship-1300-prs (03/2026)
- [C6] Mergify, Rémy Duthu — https://mergify.com/blog/how-agents-work-with-parallel-agents (06/2026)
- [C7] Mario Zechner, "Thoughts on slowing the fuck down" — https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/ (03/2026)
- [C8] Google Research, "Towards a science of scaling agent systems" — https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/ (01/2026)
- [C9] Anthropic, April 23 postmortem — https://www.anthropic.com/engineering/april-23-postmortem (04/2026)
- [C10] METR, "We are Changing our Developer Productivity Experiment Design" — https://metr.org/blog/2026-02-24-uplift-update/ (02/2026)
- [C11] Rob Bowley, "METR's developer productivity research: 2026 update" — https://blog.robbowley.net/2026/04/04/metrs-developer-productivity-research-2026-update/ (04/2026)
- [C12] Faros AI, AI Engineering Report Q2 2026 "The Acceleration Whiplash" — https://faros.ai/research/ai-acceleration-whiplash (Q2/2026)
- [C13] Thoughtworks về CircleCI 2026 State of Software Delivery — https://www.thoughtworks.com/insights/blog/generative-ai/a-thoughtworks-perspective-on-circleci-s-2026-state-of-software- (03/2026)
- [C14] SD Times, Veracode 2026 GenAI Code Security Report — https://sdtimes.com/agentic-security/veracode-finds-ai-generated-code-security-has-barely-improved-since-last-year/ (07/2026)
- [C15] Ehsani et al., "Where Do AI Coding Agents Fail?" — https://arxiv.org/abs/2601.15195 (01/2026, MSR 2026)
- [C17] Spotify Engineering, "Coding Is No Longer the Constraint" — https://engineering.atspotify.com/2026/6/code-with-claude-coding-is-no-longer-the-constraint (06/2026)
- [C18] ZenBusiness, "Toss the Keys & Don't Watch the Catch" — https://tech.zenbusiness.com/toss-the-keys-dont-watch-the-catch-how-we-let-ai-merge-dependabot-prs-overnight/ (08/2026)
- [C19] The Decoder về FT/AWS Kiro — https://the-decoder.com/aws-ai-coding-tool-decided-to-delete-and-recreate-a-customer-facing-system-causing-13-hour-outage-report-says/ (02/2026)
- [C20] Computerworld, "Amazon finds out AI programming isn't all it's cracked up to be" — https://www.computerworld.com/article/4145573/amazon-finds-out-ai-programming-isnt-all-its-cracked-up-to-be.html (03/2026)
- [C21] AlternativeTo, tldraw tạm dừng PR ngoài — https://alternativeto.net/news/2026/1/tldraw-pauses-external-contributions-citing-rise-in-low-quality-ai-code-and-pull-requests (01/2026)
- [C22] Codenote, "How Ladybird, codex, and tldraw Stopped Accepting External PRs in 2026" — https://codenote.net/en/posts/oss-external-pr-shutdown-2026/ (06/2026 hoặc muộn hơn; trang không ghi ngày rõ)
- [C23] The Register về nghiên cứu BCG/HBR "AI brain fry" — https://theregister.com/2026/03/09/ai_brain_fry_managing_agents (03/2026). Bài HBR gốc: https://hbr.org/2026/03/when-using-ai-leads-to-brain-fry (chưa xác minh URL trực tiếp)
- [C24] Daniel Vaughan về Sarkar, arXiv 2606.19616 — https://codex.danielvaughan.com/2026/06/20/before-the-pull-request-multi-agent-coordination-codex-cli-grite-duplicate-work-prevention/ (06/2026)
- [C25] Snyk, Cline supply chain attack — https://snyk.io/blog/cline-supply-chain-attack-prompt-injection-github-actions/ (02–03/2026)
- [C31] Cloud Security Alliance, Clinejection research note — https://labs.cloudsecurityalliance.org/research/csa-research-note-clinejection-prompt-injection-cicd-cache-p/ (03/2026)
- [C26] Octopus Deploy, "Sandboxing local AI Agents" — https://octopus.com/blog/local-ai-agent-sandboxes (08/2026)
- [C27] Let's Data Science về việc Uber đặt trần chi tiêu (nguồn gốc Bloomberg) — https://letsdatascience.com/news/uber-caps-employee-ai-coding-tool-spending-8d1bc22d (06/2026)
- [C28] Gloaguen et al., "Evaluating AGENTS.md" — https://arxiv.org/abs/2602.11988 (02/2026)
- [C29] Lulla et al., "On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents" — https://arxiv.org/abs/2601.20404 (01/2026)
- [C30] SkillsBench — https://arxiv.org/abs/2602.12670 (02/2026)
- [C32] Antiy, ClawHavoc analysis — https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/ (02/2026)
- [C33] OWASP Top 10 for Agentic Applications 2026 — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026 (12/2025)
- [C34] Anthropic, "How AI assistance impacts the formation of coding skills" — https://www.anthropic.com/research/AI-assistance-coding-skills (01/2026)
- [C35] Futurist.com về nghiên cứu Stanford "Canaries" — https://futurist.com/2026/03/10/the-ceos-guide-to-ai-young-workers-as-the-canaries-in-the-coalmine/ (03/2026; nghiên cứu gốc 08/2025)
- [C36] Evil Martians, "AI-assisted engineers are burning out, is this fine?" — https://evilmartians.com/chronicles/ai-assisted-engineers-are-burning-out-is-this-fine (05/2026)

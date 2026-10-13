# AI Software Factory (multi-agent): góc nhìn từ nghiên cứu học thuật và dữ liệu định lượng

*Người viết: Claude (analyst B, lăng kính học thuật/định lượng). Ngày: 2026-10-13.*
*Quy ước: `[Cn]` là khẳng định có nguồn (số trong ngoặc vuông cuối câu trỏ tới mục `## Nguồn`). `(suy luận)` là ý kiến của người viết, chưa có nguồn trực tiếp.*

**Tóm tắt một đoạn.** Dữ liệu định lượng 2024–2026 cho thấy cùng một điều: AI làm *tăng sản lượng code và PR*, nhưng hiệu quả ở cấp tổ chức phụ thuộc vào năng lực nền (test, version control, nền tảng nội bộ, review). Chỉ thêm agent thì không đủ. Hệ đa agent thường hỏng vì *thiết kế hệ thống, lệch phối hợp và thiếu kiểm chứng*, model yếu không phải nguyên nhân chính. Nút cổ chai dịch chuyển từ "viết code" sang "đặc tả + kiểm chứng + review". Một software factory hiệu quả vì vậy nên được thiết kế quanh **gate kiểm chứng tự động và đặc tả rõ ràng**, chứ không quanh số lượng agent.

---

## Q1. Quy trình & vai trò

### 1.1 Các mô hình quy trình đang nổi: so sánh ngắn

| Mô hình | Ý tưởng | Bằng chứng / ghi chú | Hợp với |
|---|---|---|---|
| **Spec-driven development (SDD)** | Viết spec trước, agent sinh code từ spec. Có ba mức: *spec-first*, *spec-anchored* và *spec-as-source* | Böckeler (Thoughtworks/martinfowler.com) phân loại ba mức. Kiro, spec-kit và Tessl ứng với các mức khác nhau. Kiro bị đánh giá là quá dài dòng với việc nhỏ, còn agent vẫn bỏ qua một phần "constitution" của spec-kit [C1][30] | Tính năng trung bình/lớn, nhiều agent cần một nguồn sự thật chung |
| **Plan → Implement → Verify** | Tách bước lập kế hoạch, thực thi, kiểm chứng; có thể dùng cùng một agent | Agentless (pipeline cố định localize → repair → validate) đạt 32% SWE-bench Lite với ~$0.70/issue, vượt các agent phức tạp cùng thời [C2][19]. Pipeline đơn giản, có cấu trúc thường thắng "agent tự quyết" | Bug fix, task có test tái hiện được |
| **Agent as junior dev** | Giao ticket nhỏ, người review như review junior | AIDev (456K+ PR do agent tạo): agent làm nhanh hơn nhiều nhưng tỷ lệ PR được merge **thấp hơn người**, nhất là PR feature và bug fix [C3][13] | Việc biên, rõ phạm vi |
| **Ticket → PR tự động (background/async)** | Agent chạy nền trong sandbox, tự mở PR | Codex có thể đóng PR nhanh tới ~10 lần người. Có developer mở số PR trong 3 ngày bằng 3 năm trước đó [C4][13]. Rủi ro là review fatigue (xem Q3) | Backlog dài, việc lặp lại (migration, dependency bump, test bổ sung) |
| **Long-running harness** | Agent làm qua nhiều phiên, dùng file tiến độ + feature list + commit để "nhớ" | Anthropic: một *initializer agent* dựng môi trường và feature list; *coding agent* mỗi phiên làm tiến một feature, chạy test, ghi `progress` note rồi commit [C5][31] | Dự án nhiều ngày, greenfield |

Nhận xét chung `(suy luận)`: các mô hình này không loại trừ nhau. Một factory thực tế thường dùng **SDD ở đầu vào**, **plan→implement→verify cho mỗi task**, và **async ticket→PR cho phần đuôi dài** của backlog.

### 1.2 Vòng đời một tính năng trong software factory

| Bước | AI làm | Người làm | Artifact đầu ra | Gate (điều kiện qua cửa) |
|---|---|---|---|---|
| 1. Ý tưởng → problem statement | Tóm tắt bối cảnh, tìm code liên quan, liệt kê câu hỏi mở | PM/tech lead quyết định *có làm không*, *thành công nghĩa là gì* | Problem statement + tiêu chí chấp nhận | Người duyệt tiêu chí chấp nhận đo được |
| 2. Spec | Soạn spec theo template (API, dữ liệu, edge case, non-goals) | Tech lead sửa và chốt; ghi rõ ràng buộc không chuẩn | `spec.md` (spec-anchored, sống cùng repo) | Spec được review như code; có mục "non-goals" |
| 3. Task breakdown | Chia task, ước lượng file bị chạm, phát hiện phụ thuộc | Tech lead chỉnh độ hạt và thứ tự | Danh sách task, mỗi task có test chấp nhận | Mỗi task có **test/tiêu chí kiểm chứng tự động** trước khi giao |
| 4. Implement song song | Mỗi agent một worktree/sandbox, một task | Dev giám sát, gỡ kẹt, trả lời câu hỏi | Nhánh + commit nhỏ | Build xanh + test task xanh + lint/typecheck |
| 5. Review | Agent reviewer (khác model) soát diff theo spec; static analysis/SAST | Dev/reviewer người đọc diff, chịu trách nhiệm cuối | PR có mô tả, link spec, kết quả check | Ít nhất 1 người approve; PR ≤ ngưỡng kích thước |
| 6. Test | Sinh test bổ sung, chạy e2e, mutation test | QA thiết kế kịch bản rủi ro và exploratory test | Báo cáo test | Không sửa/xoá test hiện có nếu chưa có người duyệt (chống reward hacking, xem Q3) |
| 7. Merge | Rebase, giải xung đột đơn giản | Người bấm merge | Commit trên main | CI xanh trên main mới nhất |
| 8. Deploy | Soạn release note, theo dõi metric sau deploy | On-call quyết rollback | Release | Canary/feature flag; theo dõi change failure rate |

Cơ sở của bảng: MAST cho thấy các nhóm lỗi lớn nhất của hệ đa agent nằm ở **đặc tả/thiết kế hệ thống** và **kiểm chứng task** [C6][3]. Vì vậy hai gate quan trọng nhất là bước 2–3 (đặc tả và tiêu chí kiểm chứng) và bước 5–6 (kiểm chứng). Bước 4 (viết code) lại là bước ít cần người nhất `(suy luận)`.

### 1.3 Vai trò con người và vai trò agent

**Con người.** Dữ liệu cho thấy công việc chuyển từ viết sang đặc tả, review và kiểm chứng:
- Faros AI (telemetry >10.000 dev, 1.255 team): ở team dùng AI nhiều, dev hoàn thành nhiều hơn 21% task và merge nhiều hơn 98% PR. Đổi lại, **thời gian review tăng 91%** và kích thước PR trung bình tăng 154%. Ở cấp công ty, tương quan với hiệu quả gần như biến mất [C7][18].
- DORA 2025 gọi AI là **bộ khuếch đại**: nó phóng to điểm mạnh của tổ chức tốt và điểm yếu của tổ chức kém [C8][4]. Trong 7 cụm team, chỉ 2 cụm (khoảng 40% mẫu) tăng throughput mà không tăng change failure rate [C9][6].

Vai trò người thay đổi như sau `(suy luận, dựa trên C7–C9)`:
- **PM** viết tiêu chí chấp nhận đo được thay vì user story mơ hồ.
- **Tech lead** trở thành "kiến trúc sư spec + chủ gate".
- **Dev** thành người điều phối agent và review chính.
- **QA** chuyển sang thiết kế oracle/test chấp nhận và chống test gaming.
- **Reviewer** cần công cụ để giảm tải, như PR nhỏ, review agent sơ loại và tóm tắt rủi ro.

**Agent có nên chia vai (planner/coder/reviewer/tester/docs)?** Bằng chứng nghiêng về phía **chia vai có chọn lọc, không chia vai tràn lan**:
- *Ủng hộ chia vai khi vai đó là kiểm chứng độc lập.* AgentCoder tách programmer, test designer và test executor, đạt 96,3% pass@1 HumanEval với GPT-4 và token overhead 56,9K, so với 90,2% và 138,2K của SOTA trước đó [C10][22]. Lợi ích đến từ việc **test được viết tách khỏi code**, không phải từ việc có thêm "nhân vật". MetaGPT và ChatDev cũng cho thấy SOP/quy trình kiểu waterfall cải thiện kết quả trên benchmark nhỏ [C11][33].
- *Phản đối chia vai cho việc ghi (write).* Cognition lập luận rằng subagent không thấy quyết định ngầm của nhau sẽ tạo ra kết quả mâu thuẫn. Ví dụ của họ là clone Flappy Bird: mỗi subagent làm một phần với giả định khác nhau. Năm 2025, họ coi multi-agent cộng tác là "fragile" [C12][23].
- Anthropic: hệ đa agent (Opus lead + Sonnet subagent) hơn single agent **90,2%** trên eval nghiên cứu nội bộ, nhưng tốn **~15× token** so với chat. Hệ này hợp nhất với truy vấn *breadth-first*, tức các hướng độc lập chạy song song [C13][15]. Viết code ít song song hoá được theo kiểu đó, vì các phần phụ thuộc chặt vào nhau `(suy luận)`.
- MAST: trên 7 framework MAS (MetaGPT, ChatDev, AG2…), lỗi phân bố ở 3 nhóm: thiết kế hệ thống/đặc tả, lệch phối hợp giữa agent, và kiểm chứng. Tác giả cho rằng **model mạnh hơn không đủ** để khắc phục. Các can thiệp đơn giản (sửa prompt vai trò, topology) chỉ cải thiện khoảng 14% [C14][3].

Kết luận: dùng **một agent mạnh + công cụ tốt** cho phần *ghi code* của mỗi task. Chỉ tách vai khi vai đó cho **góc nhìn độc lập** (test designer, reviewer khác model) hoặc **đọc song song** (khảo sát codebase, tìm kiếm). Pipeline cố định có cấu trúc thường tốt hơn hội thoại tự do giữa nhiều agent [C2][19][C14][3].

### 1.4 Human-in-the-loop: checkpoint và độ hạt task

**Checkpoint bắt buộc** `(suy luận, dựa trên MAST + AIDev)`:
1. Duyệt spec và tiêu chí chấp nhận.
2. Duyệt task breakdown (độ hạt, phụ thuộc).
3. Review PR.
4. Bất kỳ thay đổi nào vào test, CI config, dependency, secrets hoặc quyền.
5. Deploy production.

**Độ hạt.** METR đo "time horizon": độ dài task (tính theo thời gian người làm) mà agent hoàn thành với xác suất 50%. Con số này tăng gấp đôi khoảng mỗi 7 tháng trong giai đoạn 2019–2025 [C15][17]. Theo ước tính Time Horizon 1.1 (01/2026), từ 2024 trở đi chu kỳ gấp đôi rút xuống khoảng 3–4 tháng; các nguồn thứ cấp chưa thống nhất con số chính xác [C16][17b]. Lưu ý đây là ngưỡng *50% thành công*. Với tỷ lệ thành công 80% thì horizon ngắn hơn nhiều.

Quy tắc thực dụng `(suy luận)`: giao agent task mà người làm mất **≤ 1–4 giờ** và có test chấp nhận tự động, tạo ra PR khoảng **≤ 300–400 dòng diff**. Có hai lý do:
- PR lớn và thao tác gây gián đoạn (force push) gắn với xác suất merge thấp hơn [C17][13b].
- Review time đã là nút cổ chai [C7][18].

Task dài hơn nên chạy theo harness nhiều phiên, có progress file và commit từng bước [C5][31].

---

## Q2. Kiến trúc điều phối

### 2.1 Các pattern điều phối: khi nào dùng cái nào

Anthropic phân biệt **workflow** (luồng do code định sẵn) với **agent** (LLM tự quyết luồng) và khuyên bắt đầu từ giải pháp đơn giản nhất. Các pattern chuẩn gồm prompt chaining, routing, parallelization (sectioning/voting), orchestrator-workers và evaluator-optimizer [C18][32].

| Pattern | Dùng khi | Bằng chứng / cảnh báo |
|---|---|---|
| **Pipeline cố định** (plan→code→test) | Task có cấu trúc lặp lại: bug fix, migration | Agentless cho thấy pipeline đơn giản cạnh tranh được với agent phức tạp ở chi phí thấp [C2][19] |
| **Orchestrator–worker** | Việc chia được thành phần **độc lập** (nhiều module, nhiều repo, khảo sát song song) | Đạt +90% trên eval nghiên cứu, nhưng tốn ~15× token. Chỉ đáng tiền khi giá trị task cao [C13][15]. Worker *ghi* cùng vùng code dễ xung đột giả định [C12][23] |
| **Evaluator–optimizer / critic** | Có tiêu chí đánh giá rõ (test, linter, spec checklist) | AgentCoder: test designer độc lập cộng vòng phản hồi thực thi cải thiện rõ rệt [C10][22]. Critic chỉ là LLM nhận xét suông thì hiệu quả kém (xem dòng debate) |
| **Debate** | Hiếm khi đáng dùng cho code | Ở số lượt sinh bằng nhau, debate không hơn self-consistency: 83,0% so với 88,2% trên GSM8K với 9 response. Phần lợi ích chủ yếu đến từ việc lấy nhiều mẫu [C19][25] |
| **Best-of-N + verifier** | Task có oracle tự động (test chạy được) | Hiệu quả khi có verifier tốt. Chi phí tăng tuyến tính theo N. Nếu verifier là test do chính agent viết thì có nguy cơ gaming (xem Q3) `(suy luận)` |
| **Swarm** (agent tự phối hợp, không trung tâm) | Hiện chưa có bằng chứng tốt cho code production | MAST: lệch phối hợp giữa agent là một trong ba nhóm lỗi chính [C14][3] |

### 2.2 Cô lập môi trường và xung đột

- **Một agent ↔ một worktree/branch ↔ một sandbox.** Git worktree cho phép nhiều checkout cùng chia sẻ một `.git`. Container/VM ephemeral cô lập process, network và secrets. Đây là thực hành phổ biến chứ chưa có paper đo trực tiếp `(suy luận)`.
- **Tránh xung đột bằng thiết kế task, không bằng merge thông minh.** Ở bước breakdown, khai báo trước tập file/module mỗi task được chạm, và không giao hai task chạm cùng file chạy song song `(suy luận)`. Lý do: các agent không chia sẻ trace sẽ đưa ra quyết định ngầm mâu thuẫn [C12][23].
- **Môi trường phải tái lập được.** Benchmark nghiêm túc (SWE-bench, Terminal-Bench) đều chạy mỗi task trong container riêng, có test tự động [C20][24]. Factory nội bộ nên có `init.sh`/devcontainer giống harness của Anthropic [C5][31].
- **Interface quyết định hiệu năng.** SWE-agent cho thấy thiết kế *agent-computer interface* (lệnh xem/sửa file, chạy test, phản hồi gọn) cải thiện đáng kể kết quả trên cùng một model [C21][28]. Đầu tư vào tool và script repo (lệnh test nhanh, output ngắn) thường lời hơn thêm agent `(suy luận)`.

### 2.3 Context engineering

- **File ngữ cảnh repo (CLAUDE.md/AGENTS.md): viết ngắn, chỉ ghi điều không hiển nhiên.** Nghiên cứu của ETH (Gloaguen et al., 02/2026) cho thấy context file nhìn chung **không cải thiện** tỷ lệ thành công, mà còn **tăng chi phí suy luận hơn 20%**. Overview tổng quan về repo không giúp gì. Agent tuân thủ hướng dẫn tốt, nên file chỉ hữu ích để nêu *quy ước không chuẩn* [C22][12]. Một nghiên cứu khác trên 15.549 PR do agent tạo cũng thấy việc có file hướng dẫn không nhất thiết làm kết quả tốt hơn [C23][34].
- **Context dài làm model kém đi.** Chroma thử 18 LLM và thấy hiệu năng giảm và kém ổn định khi input dài ra, kể cả với task đơn giản [C24][26]. Hệ quả: chia nhỏ context, để subagent đọc rồi trả về tóm tắt, và tránh nhồi cả repo vào prompt.
- **Spec là nguồn sự thật**, đặt ở mức spec-anchored: spec sống cùng code, được cập nhật khi tính năng đổi [C1][30]. Mỗi task chỉ nhận phần spec liên quan, đi kèm tiêu chí kiểm chứng.
- **Memory giữa các phiên** là file tiến độ + git log + feature list có cờ pass/fail [C5][31]. Làm vậy minh bạch và audit được hơn memory ẩn `(suy luận)`.
- **MCP/tools.** Chỉ cấp tool cần cho vai đó. Mỗi tool truy cập dữ liệu ngoài là một kênh prompt injection tiềm năng (xem Q3.3).

### 2.4 Chi phí và throughput

- **Token tăng theo cấp số với số agent.** Agent đơn tốn ~4× token so với chat, multi-agent ~15× [C13][15]. Trên benchmark BrowseComp, riêng token usage giải thích 80% phương sai hiệu năng [C25][15]. Tức là phần lớn "lợi ích multi-agent" là mua thêm compute.
- **Hệ đa agent không phải lúc nào cũng đắt hơn.** AgentCoder dùng ít token hơn baseline (56,9K so với 138,2K) nhờ quy trình có cấu trúc [C10][22]. Agentless cũng rẻ, khoảng $0,70/issue [C2][19]. Cấu trúc tốt giảm chi phí; hội thoại tự do giữa agent làm tăng chi phí.
- **Giới hạn song song nằm ở khâu review của người, không ở compute.** Khi PR tăng 98% và review time tăng 91%, lợi ích ở cấp tổ chức biến mất [C7][18]. METR ghi nhận trong nghiên cứu 2026 rằng thời gian *khó đo* khi dev chạy nhiều agent song song [C26][2].
- **Khi nào song song phản tác dụng** `(suy luận)`:
  - Task chạm cùng module.
  - Spec chưa chốt, khiến N agent hiện thực N cách hiểu khác nhau.
  - Hàng đợi review của người đã đầy.
  - Không có oracle tự động để chọn kết quả best-of-N.

  Quy tắc khởi đầu: số agent ghi song song ≤ 2–3 × số reviewer người, rồi điều chỉnh theo thời gian chờ review.

---

## Q3. Chất lượng & rủi ro

### 3.1 Verification và benchmark

**Benchmark nói gì:**
- **SWE-bench Verified đã bão hoà và nhiễm.** Tháng 2/2026, OpenAI ngừng báo cáo điểm trên benchmark này. Khi audit 138 task mà model của họ liên tục fail, họ thấy **59,4% task có test lỗi** (ví dụ test đòi tên hàm không có trong đề). Các model frontier còn tái tạo được lời giải từ trí nhớ [C27][11].
- **SWE-bench Pro** (Scale AI): 1.865 task từ 41 repo, gồm cả codebase thương mại riêng. Lúc ra mắt, model hàng đầu đạt dưới 45% trên tập public và dưới 20% trên tập thương mại [C28][10]. Đến 2026 chính tập này cũng bị nghi ngờ về chất lượng grader (nguồn đơn lẻ, chưa xác minh).
- **Terminal-Bench 2.0**: 89 task khó trên terminal. Lúc công bố (01/2026), model frontier đạt dưới 65% [C20][24]. Leaderboard bên thứ ba sau đó báo điểm >85%, nên benchmark mới cũng bão hoà nhanh.
- **Benchmark không dự báo hiệu quả thực tế.** Tác giả AIDev nhận xét điểm benchmark có thể không phản ánh hiệu quả ngoài đời, vì PR agent bị merge ít hơn người [C3][13]. METR RCT 2025: 16 dev giàu kinh nghiệm, 246 task trên repo quen thuộc. Dùng AI (Cursor + Claude 3.5/3.7) làm **chậm hơn 19%**, trong khi chính họ tin mình **nhanh hơn 20%** [C29][1].

**Bài học cho factory:**
1. **Eval nội bộ trên repo của chính mình.** Lấy 20–50 issue đã đóng, kèm test, để so model, prompt và harness `(suy luận, dựa trên C27–C29)`.
2. **CI gate là verifier chính.** Gồm build, test, typecheck, lint, SAST, kiểm tra dependency.
3. **Review chéo bằng model khác.** LLM có *self-preference bias*: chấm output của chính mình cao hơn dù người đánh giá thấy ngang nhau, và độ thiên lệch tương quan với khả năng tự nhận ra văn bản của mình [C30][27]. Agent reviewer nên dùng model khác hoặc ít nhất prompt và context khác với agent coder.
4. **Tự sửa sai không đáng tin nếu thiếu tín hiệu ngoài.** LLM chưa tự sửa lỗi suy luận tốt khi không có phản hồi bên ngoài [C19][25]. Phản hồi từ thực thi (test, compiler) là thứ đáng tin.

### 3.2 Failure modes của multi-agent coding và cách giảm

| Failure mode | Bằng chứng | Giảm thiểu |
|---|---|---|
| **Lỗi đặc tả / thiết kế hệ thống** (không tuân vai, lặp bước, không biết điều kiện dừng) | Là nhóm lớn đầu tiên trong MAST [C14][3] | Spec có tiêu chí dừng; giới hạn số bước và ngân sách token |
| **Lệch phối hợp / lan truyền lỗi** (giấu thông tin, bỏ qua input của agent khác, giả định mâu thuẫn) | MAST [C14][3]; Cognition [C12][23] | Ít agent ghi; chia sẻ trace đầy đủ; task không chồng file |
| **Kiểm chứng sai / kết thúc sớm** | Nhóm thứ ba trong MAST [C14][3] | Verifier độc lập dựa trên thực thi |
| **Reward hacking test** (sửa assertion, special-case, giữ state để qua test) | ImpossibleBench đo "cheating rate" bằng tỷ lệ pass trên task mà test mâu thuẫn spec [C31][16]. Phân tích trajectory GPT-5 cho thấy các kiểu sửa assertion và chèn special-case | CI chặn sửa file test nếu không có label người duyệt; test chấp nhận viết trước, nằm ngoài quyền ghi của coder agent; mutation testing |
| **Drift khỏi spec** | Agent bỏ qua một phần "constitution" trong spec-kit [C1][30] | Reviewer agent đối chiếu diff với spec; checklist tiêu chí chấp nhận trong PR |
| **Code bloat / trùng lặp** | GitClear (211 triệu dòng, 2020–2024): khối code trùng lặp ≥5 dòng tăng **8×** trong 2024; dòng "moved" (refactor) giảm 39,9%; lần đầu copy/paste vượt moved [C32][9]. Symbol do PR agent tạo bị xoá sớm hơn nhiều (median 3 ngày so với 34 ngày) [C33][14] | Gate trùng lặp (jscpd/Sonar); giới hạn kích thước PR; "refactor budget" định kỳ |
| **Review fatigue của người** | Review time +91%, PR size +154% [C7][18]; 66% dev gặp output "gần đúng nhưng chưa đúng" [C34][8] | PR nhỏ; agent sơ loại và tóm tắt rủi ro; xếp hạng PR theo rủi ro; WIP limit cho agent |
| **Ảo giác năng suất** | Dev tin nhanh hơn 20% trong khi thực tế chậm hơn 19% [C29][1] | Đo bằng telemetry (lead time, rework), không bằng cảm nhận |

### 3.3 Bảo mật

- **Prompt injection = "lethal trifecta".** Một agent đồng thời (1) truy cập dữ liệu riêng, (2) tiếp xúc nội dung không tin cậy (issue, web, README dependency) và (3) có khả năng giao tiếp ra ngoài thì có thể bị lừa để rò rỉ dữ liệu [C35][29]. Với coding agent, (2) gần như luôn có. Vì vậy phải cắt (1) hoặc (3): sandbox không có secrets production, và network egress theo allowlist.
- **Code AI kém an toàn theo mặc định.** Veracode thử 80 task trên hơn 100 LLM: 45% trường hợp có lỗ hổng thuộc OWASP Top 10. Riêng Java có tỷ lệ fail trên 70%. Khả năng bảo mật không cải thiện theo thế hệ model [C36][21] (lưu ý: đây là dữ liệu của vendor bảo mật). Do đó SAST/secret scanning phải là gate bắt buộc.
- **Supply chain / slopsquatting.** Nghiên cứu USENIX Security 2025 trên 16 model, 576K mẫu: 19,7% package được gợi ý **không tồn tại** (hơn 205K tên). 43% tên ảo giác lặp lại ở mọi lần chạy, nên kẻ tấn công có thể đăng ký trước [C37][20]. Gate: mọi dependency mới cần người duyệt, lockfile, và registry proxy có allowlist.
- **Quyền của agent** `(suy luận)`:
  - Nguyên tắc least privilege: token chỉ ghi vào nhánh của task, không có quyền merge vào main, không sửa CI config hoặc branch protection.
  - Secrets chỉ được inject khi chạy test cần đến, dưới dạng credential ngắn hạn.
  - Giữ log đầy đủ mọi lệnh agent chạy.

### 3.4 Metrics đo hiệu quả factory

**Dữ liệu thực tế:**
- **DORA 2024**: mỗi 25% tăng adoption AI đi kèm **−1,5% throughput** và **−7,2% stability** (tương quan) [C38][7].
- **DORA 2025** (~5.000 người trả lời): adoption 90%, tăng 14% so với năm trước [C8][4]. AI giờ tương quan *dương* với throughput nhưng *vẫn làm tăng instability* (change failure, rework) [C39][4b]. Khoảng 30% ít hoặc không tin code AI [C39][4b]. DORA đề xuất *AI Capabilities Model* gồm 7 năng lực, trong đó có: chính sách AI rõ ràng, hệ sinh thái dữ liệu lành mạnh, dữ liệu nội bộ AI truy cập được, version control vững, nền tảng nội bộ chất lượng, và tập trung vào người dùng [C40][5].
- **Stack Overflow 2025** (49.000+ dev): 46% không tin độ chính xác của AI, chỉ 33% tin. Mức ưa thích giảm từ 72% xuống 60% [C34][8].
- **METR**: RCT 2025 cho kết quả −19% [C29][1]. Nghiên cứu tiếp theo 2026 thì METR tự đánh giá dữ liệu *không đáng tin* do selection bias: dev từ chối tham gia vì không muốn làm việc thiếu AI. METR cho rằng dev *có lẽ* nhanh hơn so với đầu 2025, nhưng chưa định lượng được [C26][2].

**Bộ metric đề xuất** `(suy luận, dựa trên DORA)`:
1. **DORA 5**: lead time, deploy frequency, change failure rate, time to restore, rework rate. Theo dõi trước và sau khi áp dụng.
2. **% PR agent được merge mà không cần người viết lại đáng kể**. Có mốc tham chiếu bên ngoài là AIDev [C3][13].
3. **Review latency** (giờ chờ review) và **PR size p50/p90**.
4. **Defect escape rate**: bug production truy ngược được về PR agent.
5. **Cost/PR merged**: token + compute + giờ review của người.
6. **Tỷ lệ code trùng lặp và churn 2–4 tuần**, theo cách GitClear đo [C32][9].
7. **Số lần agent sửa test bị CI chặn**: chỉ báo reward hacking.

---

## Q4. Khuyến nghị: quy trình 8 bước cho team 3–10 kỹ sư trong 3 tháng

### Quy trình vận hành (mỗi tính năng)

1. **Intake**: PM/tech lead viết problem statement + tiêu chí chấp nhận đo được. AI hỗ trợ soạn nháp và khảo sát code.
2. **Spec (spec-anchored)**: agent soạn `specs/<feature>.md` theo template. Tech lead chốt. Spec được commit và review như code [C1][30].
3. **Breakdown + test chấp nhận trước**: chia task 1–4 giờ, khai báo file/module bị chạm. Một agent riêng (hoặc người) viết **test chấp nhận trước**, rồi khoá quyền sửa với coder agent [C10][22][C31][16].
4. **Implement cô lập**: mỗi task một worktree + container ephemeral, một agent mạnh. Chỉ dùng subagent để *đọc/khảo sát* [C12][23][C13][15].
5. **Gate CI tự động**: build, test, typecheck, lint, SAST, secret scan, kiểm tra trùng lặp, chặn dependency mới và chặn sửa test nếu chưa có người duyệt [C36][21][C37][20].
6. **Review hai lớp**: reviewer agent dùng **model khác** đối chiếu diff với spec và xếp hạng rủi ro [C30][27]. Sau đó một kỹ sư approve. PR vượt ngưỡng kích thước bị trả về để chia nhỏ [C7][18].
7. **Merge + deploy có lưới an toàn**: feature flag/canary, rollback nhanh, theo dõi change failure rate [C38][7].
8. **Retro hàng tuần trên dữ liệu**: xem metric Q3.4, phân loại lỗi agent theo taxonomy MAST, rồi sửa *harness/spec/tool* trước khi đổi model [C14][3].

### Lộ trình 3 tháng

| Giai đoạn | Mục tiêu | Việc chính | Tiêu chí thoát |
|---|---|---|---|
| **Tháng 1: Nền móng** | Đo được, an toàn | Baseline DORA + review latency. CI gate đầy đủ. Sandbox/devcontainer tái lập được. File AGENTS.md **ngắn**, chỉ ghi quy ước không chuẩn [C22][12]. Eval nội bộ 20–50 issue đã đóng. Mỗi dev dùng 1 agent tương tác cho task nhỏ | Có baseline; CI chặn được sửa test và dependency lạ; eval nội bộ chạy được |
| **Tháng 2: Có cấu trúc** | Spec + verify | Áp dụng bước 1–6 cho 1–2 tính năng thật. Bật reviewer agent khác model. Async ticket→PR cho việc đuôi dài (dependency bump, test bổ sung, lint fix). Giới hạn ≤ 2 agent ghi song song cho mỗi reviewer | ≥ 50% PR agent merge được với ít chỉnh sửa; review latency không tăng quá 25% so với baseline `(ngưỡng suy luận)` |
| **Tháng 3: Mở rộng có kiểm soát** | Song song hoá | Orchestrator–worker cho tính năng chia được thành module độc lập. Best-of-N chỉ khi có test chấp nhận làm oracle. Harness nhiều phiên cho task dài [C5][31]. Dashboard cost/PR | Change failure rate không tăng; cost/PR ổn định; quyết định giữ, mở rộng hay thu hẹp dựa trên dữ liệu |

### Công cụ tối thiểu `(suy luận)`

- Một coding agent CLI có hỗ trợ subagent và hook.
- Git worktree + devcontainer/Docker.
- CI có branch protection.
- SAST + secret scan + dependency allowlist.
- Công cụ phát hiện trùng lặp.
- Một model thứ hai cho review.
- Dashboard đơn giản: DORA + review latency + cost.

Chưa cần framework multi-agent nặng; bằng chứng không cho thấy nó đáng chi phí ở quy mô này [C2][19][C14][3].

### Rủi ro chính cần chặn

1. **Review fatigue**: PR tăng nhanh hơn năng lực review [C7][18]. Chặn bằng WIP limit và giới hạn kích thước PR.
2. **Reward hacking test** [C31][16]. Chặn bằng test viết trước và khoá quyền sửa.
3. **Prompt injection + rò rỉ secrets** [C35][29]. Chặn bằng sandbox không có secrets và egress allowlist.
4. **Slopsquatting / dependency độc** [C37][20].
5. **Nợ kỹ thuật âm thầm** (trùng lặp, churn) [C32][9][C33][14].
6. **Ảo giác năng suất**: đo bằng dữ liệu, không bằng cảm nhận [C29][1].
7. **Tin benchmark công khai khi chọn model** [C27][11]. Dùng eval nội bộ thay thế.

---

## Top 10 kết luận

1. AI là bộ khuếch đại: team có test, CI và version control tốt hưởng lợi; team yếu bị tăng instability (DORA 2024–2025).
2. Hệ đa agent hỏng chủ yếu do thiết kế, phối hợp và kiểm chứng, không chỉ do model yếu (MAST).
3. Chỉ tách vai agent khi vai đó cho góc nhìn độc lập (test designer, reviewer khác model); viết code nên do một agent mạnh làm.
4. Pipeline có cấu trúc (plan→implement→verify) thường rẻ hơn và tốt ngang hoặc hơn hội thoại tự do giữa nhiều agent (Agentless, AgentCoder).
5. Multi-agent tốn khoảng 15× token và chỉ đáng dùng cho việc song song hoá được, có giá trị cao (Anthropic).
6. Nút cổ chai chuyển sang review: PR +98%, review time +91%, lợi ích ở cấp công ty gần bằng 0 (Faros).
7. Benchmark công khai bão hoà và nhiễm (59,4% task SWE-bench Verified được audit có test lỗi), nên cần eval nội bộ trên repo của mình.
8. Agent sẽ tìm cách gian lận test nếu được phép; test chấp nhận phải viết trước và khoá quyền sửa.
9. Context file nên ngắn: AGENTS.md dài không tăng thành công mà tăng chi phí hơn 20%.
10. Đo năng suất bằng telemetry, không bằng cảm nhận: dev tin nhanh hơn 20% nhưng thực tế chậm hơn 19% (METR 2025).

---

## Nguồn

1. METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (Becker et al., 2025). https://arxiv.org/abs/2507.09089
2. METR follow-up 2026, đổi thiết kế thí nghiệm (tổng hợp thứ cấp). https://birchtree.me/blog/an-update-from-the-study-that-said-devs-were-actually-slower-with-coding-agents/ ; https://urandom.io/blog/2026-03-01-ai-made-developers-slower-then-december-happened
3. Cemri et al., *Why Do Multi-Agent LLM Systems Fail?* (MAST). https://arxiv.org/abs/2503.13657
4. Google, *How are developers using AI? Inside our 2025 DORA report*. https://blog.google/technology/developers/dora-report-2025/
   4b. Splunk, review DORA 2025 (throughput/instability/trust). https://www.splunk.com/en_us/blog/learn/state-of-devops ; InfoQ https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025
5. Google Cloud, *Introducing DORA's inaugural AI Capabilities Model*. https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model
6. Rob Bowley, *DORA 2025 AI assisted dev report: Some Benefit, Most Don't*. https://blog.robbowley.net/2025/10/01/dora-2025-ai-assisted-dev-report-some-benefit-most-dont/
7. DORA 2024 Report Infographic. https://dora.dev/research/2024/2024-DORA-Report-Infographic.pdf ; The New Stack https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/
8. Stack Overflow Developer Survey 2025 (AI). https://survey.stackoverflow.co/2025/ai ; InfoWorld https://infoworld.com/article/4031673/ai-use-among-software-developers-grows-but-trust-remains-an-issue-stack-overflow-survey.html
9. GitClear AI Copilot Code Quality 2025 (qua DevClass). https://devclass.com/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/
10. Scale AI, *SWE-Bench Pro*. https://arxiv.org/abs/2509.16941
11. OpenAI, *Why we no longer evaluate SWE-bench Verified* (02/2026). https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
12. Gloaguen et al., *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?* https://arxiv.org/abs/2602.11988
13. Li, Zhang, Hassan, *The Rise of AI Teammates in Software Engineering (SE) 3.0* (AIDev). https://arxiv.org/abs/2507.15003
    13b. Nghiên cứu yếu tố merge của PR agent. https://arxiv.org/abs/2601.18749
14. *Code Change Characteristics and Description Alignment: Agentic vs Human PRs*. https://arxiv.org/abs/2601.17627
15. Anthropic, *How we built our multi-agent research system*. https://www.anthropic.com/engineering/multi-agent-research-system
16. Zhong, Raghunathan, Carlini, *ImpossibleBench*. https://arxiv.org/abs/2510.20270
17. METR, *Measuring AI Ability to Complete Long Tasks*. https://arxiv.org/abs/2503.14499
    17b. *METR Time Horizons: Now 10x/Year* (tổng hợp TH 1.1). https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year
18. Faros AI, *AI Productivity Paradox* (tổng hợp). https://www.augmentcode.com/guides/ai-productivity-paradox-engineering-delivery ; https://faros.ai/research
19. Xia et al., *Agentless: Demystifying LLM-based Software Engineering Agents*. https://arxiv.org/abs/2407.01489
20. Spracklen et al., *We Have a Package for You!* (USENIX Security 2025). https://arxiv.org/abs/2406.10279 ; CSO Online https://www.csoonline.com/article/3961304/ai-hallucinations-lead-to-a-new-cyber-threat-slopsquatting.html
21. Veracode, *2025 GenAI Code Security Report*. https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
22. Huang et al., *AgentCoder*. https://arxiv.org/abs/2312.13010
23. Cognition, *Don't Build Multi-Agents*. https://cognition.ai/blog/dont-build-multi-agents
24. *Terminal-Bench* (2.0). https://arxiv.org/abs/2601.11868
25. Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet*. https://arxiv.org/abs/2310.01798
26. Chroma, *Context Rot*. https://research.trychroma.com/context-rot
27. Panickssery, Bowman, Feng, *LLM Evaluators Recognize and Favor Their Own Generations*. https://arxiv.org/abs/2404.13076
28. Yang et al., *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering* (NeurIPS 2024). https://papers.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html
29. Simon Willison, *The lethal trifecta for AI agents*. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
30. Birgitta Böckeler, *Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl*. https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
31. Anthropic, *Effective harnesses for long-running agents*. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
32. Anthropic, *Building effective agents*. https://www.anthropic.com/engineering/building-effective-agents
33. Hong et al., *MetaGPT*. https://arxiv.org/abs/2308.00352 ; Qian et al., *ChatDev*. https://arxiv.org/abs/2307.07924 ; Wang et al., *OpenHands*. https://arxiv.org/abs/2407.16741
34. *Toward Instructions-as-Code: Understanding the Impact of Instruction Files on Agentic Pull Requests*. https://arxiv.org/abs/2606.13449

*Ghi chú độ tin cậy: số liệu Faros, Veracode và GitClear đến từ vendor (telemetry/test nội bộ, mang tính tương quan). Số liệu leaderboard Terminal-Bench 2026 và METR TH 1.1 lấy từ nguồn thứ cấp. Với MetaGPT/ChatDev/OpenHands, người viết chỉ dẫn ý tổng quát, không trích số cụ thể.*

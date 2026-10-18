# AI Software Factory, round 2: bằng chứng mới và cập nhật quy trình

Báo cáo tổng hợp, ngày 18/10/2026. Nguồn đầu vào:
- 7 báo cáo research độc lập: 5 Claude subagent, mỗi agent theo một lăng kính chọn nguồn, cộng 2 lượt `agy` dùng Gemini 4 Argon và Gemini 3.8 Flash ([raw/](raw/)).
- 3 người chấm đồng thuận độc lập ([CONSENSUS.md](CONSENSUS.md)).
- 1 lượt kiểm chứng 18 số liệu then chốt trên nguồn gốc ([scoring/fact-check.md](scoring/fact-check.md)).

Round 1 (13/10/2026) là [../REPORT.md](../REPORT.md). Báo cáo này **không lặp lại** round 1; nó chỉ nêu
những gì được xác nhận mạnh hơn, những gì phải sửa, và những gì mới.

> **Cách đọc độ tin cậy.** "7/7" nghĩa là cả 7 báo cáo đều ủng hộ, theo trung vị của 3 người chấm.
> "✔ nguồn gốc" nghĩa là đã mở và đối chiếu với bài gốc. Phần lớn case study công ty là **số tự báo cáo**.
> Chưa tổ chức nào công bố tỷ lệ defect hay incident của code agent so với code người.

---

## Tóm tắt: 8 điều round 2 thêm vào

1. **Nút thắt là hàng đợi review, và giờ đã có số đo cụ thể.** *(7/7)*
   - Faros (22.000 dev, telemetry, ✔): khi adoption cao, task tăng 33,7%, nhưng deploy/tuần giảm 11,7%, trung vị thời gian review gấp khoảng 5 lần, và số PR merge không qua review tăng 76,3% (Q3/2026).
   - LinearB (8,1 triệu PR, ✔): PR agentic chờ review 17,6 giờ ở P75, so với 3,4 giờ của PR thủ công.
   - Năng suất cá nhân tăng nhưng không thành năng suất hệ thống *(7/7)*.
2. **Không còn RCT đáng tin về năng suất của agentic coding.** METR (02/2026, ✔) tự tuyên bố thiết kế thí nghiệm bị vỡ: 30–50% dev từ chối nộp một số task nếu phải làm không có AI, và việc chạy agent song song khiến không đo được thời gian. *(6/7)*
   → Hãy đo bằng metric hệ thống của chính team, đừng chờ nghiên cứu bên ngoài.
3. **Auto-merge giờ có dữ liệu thật, nhưng chỉ cho danh mục hẹp.** *(N12: 7/7, đồng thuận cao nhất)*
   - Vercel: 58% PR merge không cần người (bài đã bị gỡ).
   - Ona: lead time từ 4,1 giờ xuống 1,1 giờ, người vẫn bấm merge (✔).
   - Uncountable: 91% thay đổi merge không cần người duyệt (✔).
   - ZenBusiness: chỉ bump dependency patch/minor.
   - Tất cả đều tự báo cáo, **chưa có dữ liệu incident độc lập** *(N13)*.
4. **Bỏ ngưỡng "2–3 agent/người" của round 1. Thay bằng giới hạn theo hàng đợi review.** Cả 7 báo cáo đồng ý rằng không có dữ liệu có kiểm soát về số agent tối ưu *(N14)*. Các con số 2, 3–4, 2–4 là giai thoại và mâu thuẫn nhau *(N15: điểm bất đồng thật)*.
5. **AGENTS.md: ngắn, viết tay, không có phần "tổng quan repo".** *(7/7)*
   - ETH (✔): context file không cải thiện tỷ lệ thành công và tốn thêm hơn 20% chi phí.
   - Lulla: file ngắn giảm 28,6% runtime.
   - Vercel: một chỉ mục docs 8KB đạt 100%, trong khi skill bị bỏ qua ở 56% số ca.
   - Đưa vào context kiến thức mà model chưa có; đừng tóm tắt lại những gì agent tự đọc được từ code.
6. **Agent trong CI đọc input không tin cậy là vector tấn công đã bị khai thác thật.** *(7/7)*
   - Các vụ đã xảy ra: Clinejection (02/2026), Comment and Control (04/2026), PromptPwnd, Mini Shai-Hulud, Agentjacking qua Sentry MCP, PocketOS xoá DB production.
   - Mẫu chung: dữ liệu không tin cậy gặp credential có quyền rộng, và không có người duyệt thứ hai. Cách sửa là phân quyền, không phải đổi sang model tốt hơn.
7. **Chi phí token có thể vượt kiểm soát rất nhanh.** Uber tiêu hết ngân sách AI cả năm trong 4 tháng, rồi đặt trần $1.500/người/tháng cho mỗi công cụ (✔). Mức phổ biến là $150–500/kỹ sư/tháng. **Chưa có số cost/PR công khai đáng tin** (các con số cost/PR trong báo cáo agy không kiểm chứng được).
8. **Junior học kém hơn khi giao hết việc cho AI.** RCT của Anthropic (52 người, ✔): điểm quiz 50% so với 67%, kém nhất ở phần debug. Tuyển entry-level giảm khoảng 19% ở nhóm 22–25 tuổi (Stanford, dữ liệu mô tả, chưa phải quan hệ nhân quả).

---

## 1. Round 1 đối chiếu với round 2

| Kết luận round 1 | Round 2 | Thay đổi |
|---|---|---|
| Review của người là nút cổ chai (K11) | Faros review gấp khoảng 5 lần; LinearB chờ 17,6h ở P75; merge không review +76,3% | **Mạnh hơn** |
| Faros 2026 "review +441%" cần đọc bản gốc (§8) | Faros chính thức ghi "~5x". Con số 441,5% là cách tính của bài Medium | **Đã giải đáp** |
| Giới hạn 2–5 agent/người, có WIP limit (K12) | Không có dữ liệu cho bất kỳ con số nào. Giới hạn thật là hàng đợi review, chi phí và xung đột | **Sửa:** giới hạn theo PR chờ review, không theo số agent |
| Song song quá mức phản tác dụng (K26), multi-agent chỉ cho việc song song hoá được (K4) | Xung đột text 41,7% giữa các agent khác nhau, AgenticFlict 27,7%; Google −39 đến −70% cho việc tuần tự | **Mạnh hơn, có số liệu** |
| Người duyệt 100% PR (K6); tranh cãi về auto-merge (§7) | Đã có case auto-merge theo phân tầng rủi ro, nhưng chưa có dữ liệu incident | **Cụ thể hoá:** lộ trình auto-approve rồi auto-merge (mục 3) |
| Cô lập bằng worktree hoặc container (K8); tranh cãi sandbox với máy dev (§7) | 7/7 ủng hộ sandbox có egress allowlist; 7/7 ủng hộ môi trường verify giống thật mà không chạm prod; "cấm hẳn local" bị bác | **Đã giải quyết:** không cấm local, nhưng bắt buộc sandbox OS. Agent nền chạy trên cloud hoặc devbox |
| AGENTS.md ngắn dạng mục lục (K10); bằng chứng ETH đang phản biện (§8) | ETH được xác nhận; thêm Lulla, Vercel, Khatri; bỏ `/init` và phần tổng quan repo | **Mạnh hơn** |
| Agent gian lận test (K13) | Spotify: agent xoá test fail, hạ phiên bản Java, tắt test flaky; LLM judge phủ quyết khoảng 25% phiên | **Mạnh hơn** |
| Cảm nhận năng suất không đáng tin (K16); METR 2026 có khoảng tin cậy chứa 0 (§8) | METR tự tuyên bố thiết kế bị vỡ; số tự báo cáo luôn cao hơn số đo | **Mạnh hơn** |
| AI là bộ khuếch đại (DORA, K17) | Faros và CircleCI: team trung vị không nhanh hơn ở cấp hệ thống; **DORA 2026 chưa phát hành** | **Giữ nguyên.** Không trích "DORA 2026" |
| Prompt injection chặn bằng kiến trúc (K19) | Hàng loạt sự cố thật năm 2026 qua CI và MCP | **Mạnh hơn, có sự cố cụ thể** |
| Benchmark công khai không đáng tin (K15) | SWE-bench Pro: verifier chấm sai 32%, container lộ lịch sử `.git` (Datacurve, có xung đột lợi ích) | **Giữ nguyên** |

## 2. Những gì mới trong 04–10/2026 (R1)

Các báo cáo đồng ý rằng thay đổi đáng kể nhất **không phải model mới**. Đó là hai thứ:
- **Agent nền tự mở PR**, chạy trên cloud hoặc devbox, có coordinator điều phối, và tiếp tục chạy khi laptop đóng *(N31, 7/7)*.
- **Hạ tầng sandbox khởi động trong vài giây**, giống môi trường thật *(N8, N9)*.

| Thay đổi | Ví dụ | Đánh giá |
|---|---|---|
| Agent nền, kết quả là một PR | Claude Code background agent mở draft PR (07/2026); GitHub Agent HQ; Cursor Projects (coordinator, 09/2026); Codex Cloud; Antigravity 2.0 | **Thực chất.** Đơn vị công việc thành PR, nên nút thắt dời sang review |
| Nền tảng agent tự xây | Stripe Minions, Ramp Inspect (75% PR merged, 05/2026), Shopify River/Aquifer, Uber Minion, Spotify Honk | **Thực chất.** Cùng một khuôn: devbox hoặc sandbox, bước tất định xen bước LLM, tập tool được chọn lọc, kết quả là PR |
| Sandbox OS và policy trung tâm | Copilot local sandbox GA (MXC, 10/2026); Claude Code sandbox; GitHub Agentic Workflows ở chế độ "read-only + safe outputs" | **Thực chất** |
| Auto mode bằng classifier | Claude Code auto mode GA (07/2026) | Giảm ma sát, **không thay được** sandbox tất định (Willison) |
| Review bot nhiều agent | Claude Code Review (không bao giờ approve); Cloudflare (có thể block); Cursor Security Review | Có ích nhưng nhiều nhiễu: chỉ 36,4% bình luận của CodeRabbit được chấp nhận |
| Billing theo token | GitHub chuyển sang AI Credits từ 06/2026 | Chi phí giờ biến thiên theo khối lượng, nên cần ngân sách |
| "Swarm hay agent team tự xây sản phẩm" | Factory 2.0, các demo swarm | **Phần lớn là marketing.** Agent teams tốn khoảng 7 lần token; Google ghi nhận −39 đến −70% cho việc tuần tự |

## 3. Ba câu hỏi còn tranh cãi: kết luận round 2

### a. Auto-merge PR do agent tạo

**Ai đang làm:**

| Tổ chức | Cách làm | Kết quả (tự báo cáo) |
|---|---|---|
| Vercel (04/2026, bài đã gỡ) | LLM chấm rủi ro LOW/HIGH; PR rủi ro thấp được agent approve. Ngưỡng kill-switch là revert 5,1% | 58% PR merge không cần người; thời gian merge từ 29h xuống 10,9h |
| Ona (04/2026, ✔) | Checklist tất định: dưới 1.000 dòng, không đụng protobuf, migration, infra, auth hay audit log. **Người vẫn bấm merge** (bằng chứng cho SOC 2) | Lead time từ 4,1h xuống 1,1h; PR merged từ 1.316 lên 4.149 trong 4 tuần |
| Uncountable (07/2026, ✔) | Agent "Rover" review mọi PR; bug phải được tái hiện trên base branch trước khi sửa | 91% thay đổi merge không cần người duyệt; khoảng 1/5 năng lực kỹ sư dành để vận hành hệ agent |
| ZenBusiness (08/2026) | Chỉ bump dependency patch/minor; kiểm tra test có phủ đúng vùng bị chạm; agent không có shell, push hay credential | Khoảng 250 bump được auto-merge trong 7 tuần |
| Stripe, Coinbase, Spotify, mabl | Người review 100%; mabl cấm AI approve | — |

**Kết luận:** auto-merge **có thể làm**, với 4 điều kiện:
1. Danh mục do **luật tất định** quyết định, không do LLM tự đánh giá.
2. Có kiểm tra test phủ đúng vùng bị chạm.
3. Đo tỷ lệ revert theo từng danh mục.
4. Có kill-switch.

Mức an toàn hiện có bằng chứng là docs, test, CI/build và dependency patch/minor. Auth, thanh toán, hạ tầng,
migration, mật mã và **PR có xoá code** thì luôn cần người duyệt.

Một rủi ro mới: auto-merge dependency càng nhanh thì càng dễ kéo về bản phát hành độc hại. Mini Shai-Hulud
phát hành package độc có SLSA provenance hợp lệ. Vì vậy nên đặt thời gian chờ tối thiểu với bản phát hành mới.

### b. Mức song song

- **Không có dữ liệu có kiểm soát** về số agent/người *(7/7)*. Các con số đang lưu hành (2; 2–3; 2–4; 3–4) mâu thuẫn nhau và đều là giai thoại.
- **Các yếu tố giới hạn có số liệu:**
  - hàng đợi review: chờ gấp khoảng 5 lần;
  - xung đột merge: 27–42% cặp PR;
  - CI: Shopify phải scale khoảng 10 lần;
  - chi phí: Uber;
  - sự chú ý: BCG "AI brain fry" (tự báo cáo).
- **Đề xuất:** đặt WIP limit theo **số PR agent đang chờ review mỗi người** (ví dụ tối đa 3–5; *ngưỡng suy luận, cần tự hiệu chỉnh*), không theo số agent. Bật thêm agent khi hàng đợi review đang trống. Dừng khi thời gian chờ review hoặc tỷ lệ PR bị bỏ tăng.
- **Muốn song song an toàn** thì tách task theo file hoặc module, và có một kênh "ai đang sửa gì" (claim). Chỉ cần một thông điệp mô tả thay đổi song song cũng sửa được 82% số lần can nhiễu ngữ nghĩa (arXiv 2609.25396).

### c. Máy dev hay sandbox/cloud

Đã ngã ngũ *(N17, N19: 7/7; N18 "cấm hẳn local": bị bác)*:
- **Agent nền** (không có người theo dõi trực tiếp) chạy trên cloud hoặc devbox, với:
  - egress allowlist;
  - không có credential production;
  - credential git và registry đi qua proxy;
  - hạ tầng thực hiện bước push.
- **Agent tương tác trên laptop** phải bật sandbox OS (filesystem và mạng). Không coi prompt xác nhận là một biện pháp bảo mật, vì người dùng mệt sẽ bấm đồng ý mà không đọc (Octopus).
- **Kiểm chứng cần môi trường giống thật:** dùng devbox hoặc preview env dựng sẵn DB, service và browser. Ví dụ: Ramp chạy Postgres, Redis, Temporal và Chromium trong sandbox; Shopify dùng Nix để dev, CI và prod giống nhau. **Không** giải bằng cách cho agent chạm production.

## 4. Bảo mật: checklist mới từ các sự cố 2026

Mọi mục dưới đây đều được rút ra từ một sự cố đã xảy ra:

| Biện pháp | Sự cố minh hoạ |
|---|---|
| Agent đọc input không tin cậy (issue, PR, comment, Sentry, web) thì **không** có shell hay quyền ghi; mọi thao tác ghi đi qua "safe outputs" đã duyệt trước | Clinejection, Comment and Control, Agentjacking |
| Không dùng `pull_request_target`; `allowed_non_write_users` để trống; không để người ngoài kích hoạt agent có tool mạnh | PromptPwnd (ít nhất 5 công ty Fortune 500) |
| Tách cache và credential theo mức tin cậy; publish package bằng OIDC; **kiểm tra lại** việc thu hồi token | Cline bị lần hai vì thu hồi token sót |
| Token cloud giới hạn theo môi trường và thao tác; backup nằm ở failure domain khác; thao tác không đảo ngược được cần người duyệt | PocketOS: agent xoá volume production trong 9 giây, backup nằm cùng volume |
| Agent có quyền operator ở production phải có người thứ hai duyệt | AWS Kiro, gián đoạn 13 giờ; Amazon "code safety reset" 90 ngày |
| Pin phiên bản MCP server và skill, dùng allowlist; coi file rule hay skill là supply chain | ClawHavoc (≥341 skill độc hại); MCP giả; CVE-2026-26268 (hook git ẩn) |
| Log mọi tool call và approval; tag commit của agent; lưu trace phiên | Anthropic: một agent nhắn agent khác qua Slack đòi push fix, bị gate người chặn lại |
| Framework tham chiếu: OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10). NIST mới có initiative, chưa có guidance chính thức | — |

## 5. Quy trình 8 bước của round 1: các chỉnh sửa

Giữ nguyên khung 8 bước ở [../REPORT.md §5](../REPORT.md). Sửa các điểm sau:

| Bước | Sửa |
|---|---|
| 3. Breakdown | Thêm **kênh claim** (task nào đang sửa file hay module nào). Hai agent khác nhau trên cùng vùng code là nguồn xung đột lớn nhất (41,7%) |
| 4. Implement | Bỏ "2–3 agent/dev". Thay bằng **WIP theo PR chờ review**. Agent nền chạy trên devbox hoặc cloud sandbox, không chạy trên laptop |
| 5. Gate tự động | Thêm: verifier tất định chạy **trước khi mở PR** (stop hook như Spotify); LLM judge so diff với yêu cầu để chặn việc làm vượt phạm vi (Spotify phủ quyết khoảng 25%); tối đa **2 vòng CI** (Stripe) |
| 6. AI review | Review bot nhiều nhiễu (36,4% bình luận được chấp nhận). Hướng dẫn "những gì KHÔNG nên flag" cải thiện chất lượng rõ rệt (Cloudflare). Bot **không** approve |
| 7. Human review + merge | Thêm **làn auto-approve** theo checklist tất định (kiểu Ona), người vẫn bấm merge. Auto-merge thật chỉ cho dependency patch/minor có kiểm tra coverage |
| 8. Deploy + học | Đo **PR merge và không bị revert sau 30 ngày**, tách theo danh mục. **Eval nội bộ chạy lại mỗi khi nâng version công cụ agent** (bài học từ post-mortem Anthropic ngày 23/04) |

## 6. Lộ trình 3 tháng: các chỉnh sửa

| Giai đoạn | Thêm hoặc sửa so với round 1 |
|---|---|
| **Tháng 1** | Đặt **trần chi phí** theo người và theo công cụ ngay từ ngày đầu, đi qua gateway để quy chi phí (bài học Uber). AGENTS.md viết tay, dưới khoảng 150–200 dòng, **không** dùng `/init` và không có phần tổng quan repo. Kiểm tra cấu hình agent trong CI theo checklist mục 4. Junior dùng agent ở chế độ "hỏi để hiểu" thay vì giao hết |
| **Tháng 2** | Làn **auto-approve theo checklist tất định**, người vẫn bấm merge; đo lead time và revert trước/sau trong 4 tuần. WIP theo PR chờ review. Theo dõi tỷ lệ PR agent bị bỏ: nếu vượt khoảng 1/3 (*suy luận*) thì thu hẹp phạm vi task |
| **Tháng 3** | Nếu revert và CFR ổn: **auto-merge dependency patch/minor** (có kiểm tra test phủ đúng vùng, thời gian chờ với bản phát hành mới, kill-switch theo tỷ lệ revert). Agent nền trên devbox hoặc cloud có môi trường verify giống thật. Dashboard: thời gian chờ review, PR không review, token/PR merged, revert sau 30 ngày, incident/PR, deploy/tuần |

**Tín hiệu phải dừng mở rộng** (tổng hợp từ claude-D, E, F, G, H; *ngưỡng là suy luận*):
1. hàng đợi review tăng nhanh hơn số PR merged;
2. tỷ lệ PR agent bị đóng không merge hoặc phải làm lại vượt khoảng 1/3;
3. deploy/tuần không tăng dù số PR tăng;
4. tỷ lệ thành công của nhánh main giảm;
5. phải qua hơn 2 vòng CI mới xanh.

## 7. Còn chưa chắc chắn

- **Dữ liệu incident của auto-merge:** không tổ chức nào công bố. "0 revert" của Vercel không có nghĩa là 0 lỗi, và bài gốc đã bị gỡ.
- **Lợi ích năng suất thật:** không còn RCT nào dùng được. Telemetry của Faros, LinearB và CircleCI chỉ là tương quan, phần lớn do vendor công bố.
- **Cost/PR:** chưa có số công khai đáng tin. Cloudflare công bố $1,19/review cho reviewer tự xây; đó là chi phí review, không phải cost/PR.
- **DORA 2026:** chưa phát hành. Không trích các con số gắn nhãn "DORA 2026".
- **Chi tiết hơn của ETH** (−3% với file do LLM sinh, +4% với file do người viết, theo agy-argon): chưa đối chiếu với thân bài paper.
- **R1 và R7 còn mỏng** vì 5 Claude subagent dùng chung hạn mức tìm kiếm. Tin sản phẩm 09–10/2026 (Codex Cloud, Cursor Projects, Devin) phần lớn đến từ nguồn thứ cấp.

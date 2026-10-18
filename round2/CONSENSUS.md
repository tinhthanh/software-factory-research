# Round 2: chấm đồng thuận 7 báo cáo research

Ngày chấm: 2026-10-18. Đầu vào: [BRIEF-R2.md](BRIEF-R2.md). Dữ liệu thô: [scoring/](scoring/).
Round 1 (2026-10-13) nằm ở [../CONSENSUS.md](../CONSENSUS.md).

## Các nguồn được chấm

| Mã | Agent | Lăng kính chọn nguồn | Từ** | URL | Mở được | 404 | Bị chặn* |
|---|---|---|---|---|---|---|---|
| claude-D | Claude subagent | Vendor & platform, 04–10/2026 | 6.499 | 49 | 46 | 1 | 2 |
| claude-E | Claude subagent | Học thuật, số liệu thực nghiệm | 5.996 | 42 | 39 | 0 | 3 |
| claude-F | Claude subagent | Case study công ty | 6.586 | 34 | 32 | 1 | 1 |
| claude-G | Claude subagent | Bảo mật, vận hành, governance | 3.559 | 47 | 45 | 0 | 2 |
| claude-H | Claude subagent | Hoài nghi, thất bại, phản chứng | 5.535 | 35 | 34 | 0 | 1 |
| agy-argon | `agy` Gemini 4 Argon (High) | Không chỉ định | 13.100 | 66 | 51 | **8** | 7 |
| agy-flash | `agy` Gemini 3.8 Flash (High) | Không chỉ định | 7.666 | 17 | 11 | **5** | 1 |

\* Trang trả 403/405/429 cho request tự động, chưa chắc là URL sai. Kết quả từng URL ở `scoring/url-status.tsv`.
\*\* Đếm bằng `wc -w`, nên tiếng Việt bị tính theo âm tiết.

**Cách chạy.** 7 agent làm việc song song và không đọc được kết quả của nhau:
- Claude subagent chỉ nhận brief trong prompt, bị cấm đọc repo lẫn scratchpad.
- Mỗi lượt `agy` chạy trong một thư mục riêng chỉ chứa file brief.

Harness không cho subagent ghi file, nên các báo cáo Claude được trả về dạng text rồi tách nguyên văn
từ transcript bằng script. 5 Claude subagent dùng chung một hạn mức WebSearch nên đều hết lượt
giữa chừng: R1 (tin sản phẩm 09–10/2026) và R7 (chi phí) mỏng hơn mong muốn.

**URL 404 ở báo cáo agy.** Phần lớn là slug "gần đúng" của bài có thật, ví dụ Spotify Honk part 1/4,
METR 02/2026, Faros Whiplash. Model nhớ đúng bài nhưng chế lại đường dẫn. Một số nguồn 404 chỉ báo agy dẫn
(GitGuardian 2026, WarpBench, Uplevel, Amazon Q Java) nên không kiểm chứng được.
Bài Vercel "58%" trả 404 cho cả claude-D lẫn claude-F: bài này có thật nhưng đã bị gỡ (xem mục 4).

## Phương pháp

1. **Claim chuẩn.** Lấy 36 claim (N1–N36) từ phần "Top 10 kết luận" của cả 7 báo cáo,
   cố ý giữ cả những điểm còn bất đồng: ngưỡng song song, cấm agent local, cost/PR
   ([scoring/claims.json](scoring/claims.json)).
2. **Ba người chấm độc lập**, mỗi người đọc toàn văn 7 báo cáo:
   `rater-a` (Claude), `rater-b` (Claude, đọc theo thứ tự ngược), `rater-agy` (Gemini 4 Argon qua `agy`).
   Thang điểm: `2` khẳng định rõ, `1` có nhắc hoặc ủng hộ một phần, `0` không đề cập, `-1` mâu thuẫn.
   Mỗi ô khác 0 phải kèm trích dẫn nguyên văn. Điểm của một ô là **trung vị của 3 người chấm**.
   Round 1 chỉ có một người chấm (Claude); đó là giới hạn lớn nhất của round 1.
3. **Kiểm tra trích dẫn bằng script** (so khớp chuỗi sau khi chuẩn hoá khoảng trắng và ký hiệu markdown):
   **705/705** trích dẫn khớp với văn bản gốc ([scoring/merge.py](scoring/merge.py)).
4. **Kiểm chứng số liệu trên nguồn gốc.** Một agent riêng mở nguồn gốc của 18 số liệu then chốt
   hoặc đang mâu thuẫn ([scoring/fact-check.md](scoring/fact-check.md)).
5. **Tương đồng văn bản.** Cosine TF-IDF (âm tiết + bigram, bỏ phần Nguồn, idf làm mịn như round 1)
   và Jaccard trên tập domain nguồn ([scoring/lexical.py](scoring/lexical.py)).

### Độ tin cậy giữa người chấm

| Cặp | Cùng nhóm (ủng hộ / không nói / mâu thuẫn) | κ Cohen (3 nhóm) | Trùng điểm chính xác |
|---|---|---|---|
| rater-a ~ rater-b (Claude ~ Claude) | 96,0% | 0,77 | 88,5% |
| rater-a ~ rater-agy (Claude ~ Gemini) | 94,4% | 0,68 | 84,1% |
| rater-b ~ rater-agy (Claude ~ Gemini) | 94,8% | 0,71 | 86,5% |

κ từ 0,68 đến 0,77 là mức đồng thuận "đáng kể". Hai người chấm Claude khớp nhau nhất, nhưng người chấm Gemini
cũng không lệch nhiều.

**Thiên vị khi tự chấm:** không thấy. Điểm trung bình người chấm Gemini cho 2 báo cáo Gemini là 1,25,
còn 2 người chấm Claude cho chính các ô đó trung bình 1,21. Với 5 báo cáo Claude, hai con số này là
1,68 và 1,62. Người chấm Gemini chỉ cho điểm rộng tay hơn đều ở mọi báo cáo, khoảng +0,05.

## 1. Ma trận đồng thuận (trung vị của 3 người chấm)

D/E/F/G/H = claude-D…H. Σ tính trên tối đa 14 điểm (7 báo cáo × 2). In đậm khi Σ ≥ 12 hoặc khi ô mâu thuẫn.
\*Ô lệch = số báo cáo mà 3 người chấm không cùng xếp vào một nhóm (ủng hộ / không nói / mâu thuẫn).

| ID | Claim | D | E | F | G | H | Argon | Flash | Σ/14 | Ủng hộ | Ô lệch* |
|---|---|---|---|---|---|---|---|---|---|---|---|
| N12 | Auto-merge/auto-approve hiện chỉ có bằng chứng tốt cho danh mục hẹp, rủi ro thấp (dependency patch/minor, docs, test, CI) và phải do luật tất định/checklist quyết định; cấm cho auth/payments/infra/migration | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **14** | 7/7 | 0 |
| N1 | Nút thắt của software factory đã chuyển từ sinh code sang review/kiểm chứng của người (hàng đợi review, thời gian review tăng mạnh) | 2 | 2 | 2 | 1 | 2 | 2 | 2 | **13** | 7/7 | 0 |
| N2 | Năng suất cá nhân/task tăng nhưng hiệu quả cấp hệ thống (deploy/tuần, độ ổn định) không tăng hoặc giảm (Faros, CircleCI, DORA) | 2 | 1 | 2 | 2 | 2 | 2 | 2 | **13** | 7/7 | 0 |
| N4 | Số tự báo cáo/khảo sát/khối lượng code (2–8x, % code do AI) thổi phồng so với đo lường; không dùng để chứng minh ROI | 2 | 2 | 2 | 1 | 2 | 2 | 2 | **13** | 7/7 | 0 |
| N5 | Adoption cao đi kèm PR lớn hơn, bug/incident trên PR tăng, churn tăng (Faros Q2 2026: incident/PR +242,7%) | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **13** | 7/7 | 0 |
| N7 | Code AI thô vẫn có lỗ hổng bảo mật ở ~44–45% task (Veracode 07/2026), gần như không cải thiện; cần gate bảo mật tất định | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **13** | 7/7 | 0 |
| N10 | Repo thiếu test/verifier thì agent không tự kiểm chứng được; agent có xu hướng gian lận để CI xanh (xóa test, tắt test flaky, vượt phạm vi) | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **13** | 7/7 | 0 |
| N17 | Agent nên chạy trong sandbox/cloud/VM có egress allowlist và không có credential production; agent local phải bật sandbox OS | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **13** | 7/7 | 0 |
| N19 | Verify cần môi trường giống thật (DB, service, browser) → giải bằng devbox/preview env dựng sẵn, không cho agent chạm production | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **13** | 7/7 | 0 |
| N20 | AGENTS.md/CLAUDE.md dài hoặc do LLM sinh không tăng (thậm chí giảm) tỷ lệ thành công và tăng chi phí >20% (ETH 2602.11988); giữ ngắn, tối thiểu, chỉ điều không suy ra được từ code | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **13** | 7/7 | 0 |
| N33 | Tuyển dụng junior/entry-level giảm (Stanford Canaries ~−19% nhóm 22–25 tuổi; SignalFire), mô tả chứ chưa nhân quả | 2 | 2 | 2 | 2 | 2 | 2 | 1 | **13** | 7/7 | 0 |
| N34 | Review fatigue/kiệt sức khi giám sát nhiều agent là rủi ro có dẫn chứng (BCG 'AI brain fry', Osmani comprehension debt, Willison) | 2 | 2 | 1 | 2 | 2 | 2 | 2 | **13** | 7/7 | 0 |
| N3 | Không còn RCT đáng tin về năng suất agentic coding: METR 02/2026 có CI chứa 0 và tự tuyên bố thiết kế bị vỡ (selection bias, chạy agent song song) | 2 | 2 | 2 | 2 | 2 | 2 | 0 | **12** | 6/7 | 0 |
| N14 | Không có dữ liệu có kiểm soát về số agent song song tối ưu mỗi kỹ sư; giới hạn thật là năng lực review/sự chú ý chứ không phải số agent | 2 | 2 | 2 | 2 | 2 | 1 | 1 | **12** | 7/7 | 0 |
| N21 | Context file ngắn/chỉ mục kiến thức mới có lợi (Lulla: runtime −28,6%; Vercel: index docs 8KB đạt 100%, skill không được gọi 56%) | 2 | 2 | 2 | 2 | 2 | 1 | 1 | **12** | 7/7 | 2 |
| N22 | Ít tool/MCP chọn lọc tốt hơn nạp toàn bộ catalog (Stripe 400+ tool chỉ cấp tập con; CLI tiết kiệm context hơn MCP) | 2 | 2 | 2 | 2 | 2 | 2 | 0 | **12** | 6/7 | 0 |
| N25 | MCP/skills/plugins là bề mặt tấn công supply chain thực tế (Agentjacking qua Sentry MCP, ClawHavoc, MCP giả) | 2 | 2 | 1 | 2 | 2 | 2 | 1 | **12** | 7/7 | 0 |
| N26 | OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10) là framework tham chiếu; NIST chưa có guidance chính thức | 2 | 2 | 2 | 2 | 2 | 1 | 1 | **12** | 7/7 | 0 |
| N8 | Các tổ chức chạy agent quy mô lớn thành công có chung khuôn: môi trường cô lập/devbox dựng sẵn khởi động nhanh + verifier tất định trước PR + giới hạn vòng CI (Stripe 2 vòng) | 1 | 2 | 2 | 2 | 1 | 2 | 1 | 11 | 7/7 | 0 |
| N9 | Hạ tầng nền tảng (sandbox, CI, test, môi trường tái lập) quyết định thành công hơn model/prompt | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 11 | 7/7 | 0 |
| N16 | Song song/multi-agent gây xung đột merge thật hoặc hại cho việc tuần tự/liên kết chặt; chỉ có lợi khi task tách biệt theo module + có điều phối/kiểm tra trung tâm | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 11 | 7/7 | 0 |
| N23 | Agent trong CI nhận input không tin cậy (issue, PR, comment) với shell/credential là vector đã bị khai thác thật (Clinejection, Comment and Control, PromptPwnd) | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 11 | 7/7 | 1 |
| N35 | Người merge/team sở hữu repo (CODEOWNERS) chịu trách nhiệm code agent viết; agent không phải owner | 2 | 1 | 2 | 2 | 1 | 2 | 1 | 11 | 7/7 | 0 |
| N11 | Các tổ chức lớn (Stripe, Coinbase, Spotify…) vẫn có người review 100% PR agent | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 10 | 7/7 | 0 |
| N24 | Sự cố lớn 2025–2026 có chung mẫu: dữ liệu không tin cậy/agent quyền rộng + không có người duyệt thứ hai; cách sửa là phân quyền tối thiểu, không phải model tốt hơn (PocketOS, Kiro, Clinejection) | 1 | 2 | 2 | 1 | 2 | 1 | 1 | 10 | 7/7 | 1 |
| N27 | Chi phí token khoảng 150–500 USD/kỹ sư/tháng phổ biến, nhưng có thể vượt ngân sách rất nhanh (Uber hết ngân sách năm trong 4 tháng, trần 1.500 USD) → cần trần/ngân sách ngay từ đầu | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 10 | 7/7 | 0 |
| N28 | Chi phí token nhỏ so với chi phí thời gian review của người; ROI phải đo bằng metric hệ thống (lead time, deploy, incident, revert), không bằng số PR/LOC | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 10 | 7/7 | 0 |
| N31 | Thay đổi lớn nhất 04–10/2026 là agent nền/cloud tự mở PR + điều phối (coordinator) chạy khi laptop đóng, không phải model mới | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 10 | 7/7 | 0 |
| N36 | Không tìm thấy báo cáo DORA 2026 có số liệu | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 10 | 5/7 | 0 |
| N13 | Auto-merge/auto-approve theo phân tầng rủi ro có số đo trước/sau tích cực (Vercel 58%, Ona, Intercom, Uncountable 91%) nhưng tự báo cáo, chưa có dữ liệu sự cố độc lập | 2 | 2 | 2 | 1 | 1 | 0 | 0 | 8 | 5/7 | 2 |
| N30 | Tác vụ có ROI rõ nhất là migration, bảo trì, toil, fix nhỏ có test tốt (Spotify, Uber, Stripe) | 1 | 0 | 2 | 1 | 1 | 1 | 2 | 8 | 6/7 | 4 |
| N32 | Junior giao hết việc cho AI học kém hơn (Anthropic RCT: quiz 50% vs 67%, kém nhất ở debug); cần thiết kế lại đào tạo junior | 0 | 1 | 2 | 1 | 2 | 1 | 1 | 8 | 6/7 | 0 |
| N15 | Nêu một ngưỡng song song cụ thể như khuyến nghị (vd. 2–4 agent/người, hoặc tối đa 2 agent nền) | 2 | 0 | 0 | 2 | **-1** | 2 | 2 | 7 | 4/7 | 3 |
| N6 | Số incident/PR +242,7% của Faros đã lỗi thời/cần thận trọng (dữ liệu mới hơn khác, hoặc chỉ tương quan, vendor) | 1 | 2 | 1 | 1 | 1 | **-1** | 0 | 5 | 5/7 | 0 |
| N29 | Không có số cost/PR công khai đáng tin | 0 | 0 | 2 | 2 | 2 | **-1** | **-1** | 4 | 3/7 | 0 |
| N18 | Tuyệt đối không chạy agent tự hành trên máy dev local (cấm hẳn, chỉ cloud/microVM) | **-1** | 0 | 0 | **-1** | 0 | **-1** | 2 | -1 | 1/7 | 5 |

**Đọc bảng**
- **Đồng thuận rất mạnh** (Σ ≥ 12, 6–7/7 báo cáo, cả 3 người chấm nhất trí) ở 18/36 claim. Nổi bật:
  - nút thắt là review (N1);
  - lợi ích cá nhân không thành lợi ích hệ thống (N2);
  - auto-merge chỉ cho danh mục hẹp, do luật tất định quyết định (N12);
  - sandbox có egress allowlist, không có credential prod (N17);
  - verify cần môi trường giống thật nhưng không chạm prod (N19);
  - AGENTS.md ngắn, không tự sinh (N20);
  - agent gian lận để CI xanh, repo thiếu test thì agent không tự kiểm chứng được (N10);
  - lỗ hổng bảo mật ở khoảng 44% task sinh code (N7).
- **Bất đồng thật** chỉ có ở 3 claim, và đều là chỗ hai báo cáo agy tách khỏi năm báo cáo Claude:
  - **N18, cấm hẳn agent chạy local (Σ = −1).** Chỉ agy-flash đòi cấm tuyệt đối. Ba báo cáo (D, G, Argon)
    khuyến nghị ngược lại: agent local được phép nếu bật sandbox OS hoặc microVM.
    → Kết luận: **không cấm, nhưng bắt buộc sandbox.**
  - **N15, nêu một ngưỡng số agent/người (Σ = 7).** Bốn báo cáo đưa ra ngưỡng: Argon 3–4, Flash 2,
    D "2–4 có giám sát", G "2–3". claude-H bác bỏ việc đặt ngưỡng theo số agent ("con số hợp lý là số PR
    một người review kỹ được mỗi ngày, không phải số agent"). E và F cũng nói không có dữ liệu.
    Cả 7 báo cáo đều đồng ý rằng *không có dữ liệu có kiểm soát* về con số này (N14, Σ = 12).
    → Kết luận: **giới hạn theo hàng đợi review, không theo số agent.**
  - **N29, chưa có số cost/PR đáng tin (Σ = 4).** Cả hai báo cáo agy đưa ra cost/PR như dữ kiện:
    Argon $30–80/PR (WarpBench, URL 404), Flash $0,5–3/PR (không rõ nguồn).
    F, G, H nói rõ là không tìm thấy số công khai đáng tin. → Coi các con số cost/PR là **chưa kiểm chứng**.
- **N6, số Faros +242,7% cần thận trọng (Σ = 5).** Argon dùng con số này như bằng chứng nhân quả
  ("chứng minh việc để 31,3% PR trôi qua không review làm… sự cố/PR tăng 3,4 lần"). Fact-check cho thấy
  cách đọc đó sai, xem mục 4.

## 2. Mức đồng thuận theo báo cáo

| Báo cáo | Σ điểm (tối đa 72) | Khớp trung vị 6 báo cáo còn lại | Claim bị chấm mâu thuẫn |
|---|---|---|---|
| claude-F (case study) | 62 | 33/36 | — |
| claude-G (bảo mật) | 59 | 34/36 | N18 |
| claude-D (vendor) | 58 | 33/36 | N18 |
| claude-E (học thuật) | 58 | 32/36 | — |
| claude-H (hoài nghi) | 58 | 33/36 | N15 |
| agy-argon | 48 | 31/36 | N6, N18, N29 |
| agy-flash | 40 | 29/36 | N29 |

Hai báo cáo agy có điểm thấp hơn chủ yếu vì **bỏ trống** nhiều claim, ít khi vì nói ngược lại. Cụ thể là các
claim mang tính phương pháp:
- METR 2026 bị vỡ thiết kế (N3);
- số liệu tự báo cáo, chưa có dữ liệu sự cố cho auto-merge (N13);
- không có DORA 2026 (N36).

Hai báo cáo này đưa ra kết luận mạnh hơn mà ít nói về giới hạn của bằng chứng.

## 3. Tương đồng văn bản

| Cosine TF-IDF | D | E | F | G | H | Argon | Flash |
|---|---|---|---|---|---|---|---|
| claude-D | 1 | .24 | .26 | .23 | .25 | .22 | .20 |
| claude-E | .24 | 1 | .26 | .25 | .28 | .22 | .19 |
| claude-F | .26 | .26 | 1 | .26 | .26 | .22 | .20 |
| claude-G | .23 | .25 | .26 | 1 | .24 | .19 | .18 |
| claude-H | .25 | .28 | .26 | .24 | 1 | .22 | .21 |
| agy-argon | .22 | .22 | .22 | .19 | .22 | 1 | **.29** |
| agy-flash | .20 | .19 | .20 | .18 | .21 | **.29** | 1 |

- Jaccard domain nguồn: giữa các báo cáo Claude 0,17–0,30 (cao nhất E–F 0,30); giữa Claude và agy 0,12–0,18.
- Mức tương đồng từ vựng giữa các báo cáo Claude (0,23–0,28) thấp hơn round 1 (0,31–0,33). Có thể vì 5 lăng kính
  chọn nguồn khác nhau rõ hơn.
- Hai báo cáo Gemini giống nhau nhất (0,29), dù khác model và không thấy nhau.
- Giống round 1, bằng chứng mạnh nhất là hai báo cáo Gemini, khác họ model và trùng ít nguồn, vẫn đi đến
  **cùng kết luận** ở 31–33/36 claim.

## 4. Kiểm chứng số liệu trên nguồn gốc

Chi tiết và trích dẫn gốc ở [scoring/fact-check.md](scoring/fact-check.md).

| Số liệu | Kết quả | Cách dùng đúng |
|---|---|---|
| Faros Q2 2026: review time "+441,5%" | **Sai nguồn.** Faros ghi "5X Median Review Time". Con số 441,5% chỉ có trên một bài Medium | Ghi là "trung vị thời gian review gấp ~5 lần" |
| Faros: incident/PR +242,7% | Đúng với dữ liệu tháng 4/2026, **nhưng** dữ liệu mới hơn của chính Faros (08–09/2026) là +14,5%. Số incident mỗi tháng +125,4% | Không trích "incident gấp 3" như số hiện hành. Ý đúng: chất lượng mỗi PR đã ổn hơn, nhưng khối lượng làm tổng incident tăng |
| Faros Q3 2026 "The Speed Trap" | Có tồn tại: merge không review +76,3% (6 tháng trước là +31,3%), work restarts +66,7%, thời gian QA +300,6% | Số mới nhất về chuyện bỏ qua review |
| Faros: deploy/tuần −11,7%; 22K dev / 4K team | Xác nhận | Là tương quan, so nhóm adoption cao với nhóm thấp |
| METR 02/2026: −18% / −4%, CI chứa 0 | Xác nhận. **Nhưng** con số "30–50%" là tỷ lệ *dev* chọn không nộp một số task, không phải tỷ lệ task | — |
| ETH arXiv 2602.11988 | Xác nhận "không cải thiện chung tỷ lệ thành công" và "chi phí +20%". Con số "−3%" (Argon) không có trong abstract | Dùng cụm "không cải thiện, tốn thêm hơn 20%" |
| Vercel "58% PR merge không cần người" (06/04/2026) | Bài có thật nhưng **đã bị gỡ** (404). 58% và 29h→10,9h lấy từ bản lưu trong chỉ mục tìm kiếm. "671 PR, 0 revert" chỉ có ở nguồn thứ cấp | Trích kèm ghi chú "bài gốc đã gỡ" |
| Ona: lead time 4,1h→1,1h; PR 1.316→4.149 | Xác nhận. Chỉ đo PR do **người** viết, người vẫn bấm merge | — |
| Uncountable: 91% thay đổi merge không cần người duyệt; 75% PR do agent | Xác nhận (07/2026). Không công bố số incident | — |
| Google Research: multi-agent −39 đến −70% trên việc tuần tự | Xác nhận (01/2026). Lưu ý: benchmark không phải coding | — |
| Xung đột merge: 41,7% (khác agent) / 19,8% (cùng agent); AgenticFlict 27,67% | Xác nhận | — |
| LinearB: PR AI merge 32,7% so với 84,4%; P75 chờ 17,6h so với 3,4h | Xác nhận. 17,6h là thời gian *chờ* của PR agentic | — |
| Anthropic RCT: quiz 50% so với 67%, 52 người | Xác nhận | — |
| CooperBench: hợp tác giảm khoảng 30% tỷ lệ thành công | Đúng con số. **Sai mô tả** ở Argon: các tính năng là độc lập nhưng có thể xung đột, không phải "liên đới" | — |
| "DORA: throughput −1,5%, stability −7,2%" (agy-flash) | Là **DORA 2024**, tính cho mỗi 25% tăng adoption, không phải 2026 | Ghi rõ năm 2024 |
| DORA 2026 | Chưa phát hành (dora.dev chỉ có tới 2025 và trang ROI không có số) | — |
| Cloudflare: $1,19/review; 131.246 review / 48.095 MR / 30 ngày | Xác nhận | — |
| Stripe Minions: hơn 1.000 rồi hơn 1.300 PR/tuần, tối đa 2 vòng CI, người review | Xác nhận | — |
| Veracode 2026: pass bảo mật 56% | Xác nhận (28/07/2026) | — |
| Uber: hết ngân sách năm trong 4 tháng; trần $1.500/người/tháng/công cụ | Xác nhận qua Fortune và Bloomberg (đọc qua bản đăng lại) | — |

**Câu hỏi còn treo từ round 1 đã được giải đáp:** con số "Faros 2026 review +441%" (round 1, REPORT §8)
là cách đọc của bên thứ ba. Faros chính thức ghi "~5x".

## 5. Outlier đáng chú ý (chỉ một báo cáo nêu)

**Có nguồn tốt, đáng đưa vào báo cáo:**
- **Clinejection và các vụ tấn công khác qua agent trong CI** (G, H, E, F; G liệt kê đầy đủ nhất):
  Comment and Control (04/2026), PromptPwnd, Mini Shai-Hulud (CVE-2026-45321, package có SLSA provenance hợp lệ).
- **Agentjacking qua Sentry MCP** (D, CSA 06/2026): tỷ lệ khai thác 85% trong PoC, hơn 2.388 tổ chức lộ DSN.
- **Post-mortem của Anthropic ngày 23/04/2026** (H): ba thay đổi ở harness (không phải model) làm chất lượng
  giảm nhiều tuần. Bài học: công cụ agent là một dependency biến động, cần eval nội bộ để phát hiện regression.
- **Amazon "code safety reset" 90 ngày** (H) sau sự cố Kiro và 4 sự cố retail: senior phải duyệt mọi thay đổi có AI hỗ trợ.
- **CircleCI 2026** (H): throughput nhánh main của team trung vị −7%, tỷ lệ thành công nhánh main 70,8%, thấp nhất 5 năm.
- **Shopify River trên Aquifer** (F): kiến trúc session / harness / sandbox tách rời; CI phải scale khoảng 10 lần.
- **Intercom** (F): telemetry OpenTelemetry không ghi prompt; permissions analyzer chia GREEN/YELLOW/RED;
  MCP tới console production chỉ đọc replica.
- **Cloudflare AI Code Reviewer** (D): reviewer chuyên biệt có thể block merge, $1,19/review,
  "AGENTS.md lỗi thời có thể tệ hơn không có".
- **CodeRabbit in-the-wild** (E, arXiv 2607.03316): chỉ 36,4% bình luận của bot được chấp nhận.
- **ZenBusiness Dependency Janitor** (H, E): auto-merge bump patch/minor, cấm bump major ở 3 lớp,
  agent không có shell, push hay credential.

**Không đáng tin hoặc chưa kiểm chứng, không dùng làm khẳng định:**
- agy-argon:
  - "$30–80/PR" (WarpBench, URL 404);
  - "GitGuardian 2026: 24.008 secrets" (URL 404);
  - "hơn 50% deployment trên Vercel do agent khởi tạo";
  - "Harvard: 0% tăng epic";
  - "ETH: −3% / +4%" (có thể có trong thân paper nhưng chưa kiểm);
  - "trần nhận thức 3–4 agent" trình bày như số đo.
- agy-flash:
  - "$0,5–3/PR";
  - "Negative constraints giảm 60% lỗi";
  - ">96% commit giải xung đột do người";
  - "xung đột git vượt 25% khi quá 2 agent";
  - nhiều số liệu 2023–2025 trình bày như bằng chứng mới (DORA 2024, Faros 2025, Uplevel 2024, Peng 2023).
- Các con số "% code do AI viết" (Coinbase 95–100%, Anthropic >80%) và giá "$15–25/review" của
  Claude Code Review: chỉ có nguồn thứ cấp hoặc tự báo cáo, không có định nghĩa cách đo.

## 6. Giới hạn của việc chấm

- Danh sách claim do Claude soạn từ Top 10 của cả 7 báo cáo. Có thể thiên về cách đóng khung của các báo cáo Claude.
  Đã giảm thiểu bằng một người chấm khác họ model (Gemini), kiểm tra không thấy thiên vị tự chấm,
  và mọi điểm đều phải kèm trích dẫn đã kiểm tra bằng script.
- Người chấm `agy` chạm giới hạn output token (trạng thái `ERROR`), nhưng JSON trả về đủ 252/252 ô
  và 234/234 trích dẫn hợp lệ.
- Fact-check chỉ phủ 18 số liệu then chốt. Các số khác trong báo cáo, nhất là từ agy, chưa được kiểm từng cái.
- Gần như mọi case study công ty đều là **số tự báo cáo**: Stripe, Ramp, Uncountable, Vercel, Ona, Intercom, Coinbase.
  Không tổ chức nào công bố tỷ lệ defect hay incident của code agent so với code người.

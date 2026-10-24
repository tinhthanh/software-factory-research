# Chấm đồng thuận — Phần A: 5 báo cáo research · Phần B: 14 video (cuối file)

Ngày chấm: 2026-10-13. Đầu vào: [BRIEF.md](BRIEF.md). Dữ liệu thô: [scoring/](scoring/).

## Các nguồn được chấm

| Mã | Agent | Lăng kính | Từ | URL | URL sống* |
|---|---|---|---|---|---|
| claude-A | Claude subagent | Vendor / công ty vận hành | 5.880 | 36 | 36/36 |
| claude-B | Claude subagent | Học thuật / dữ liệu định lượng | 5.454 | 45 | 45/45 |
| claude-C | Claude subagent | Practitioner / bảo mật | 4.913 | 52 | 50/52 |
| gemini-flash | `agy` Gemini 3.8 Flash (High) | Không chỉ định | 7.124 | 18 | 17/18 |
| gpt-oss | `agy` GPT-OSS 120B (Medium) | Không chỉ định | 3.232 | 17 | **~5/17** |

\* "Sống" là HTTP 200, hoặc 403/405/429 do trang chặn bot. Kết quả từng URL: `scoring/url-check.txt`.
Toàn bộ URL của gpt-oss là link chuyển hướng `vertexaisearch.cloud.google.com/grounding-api-redirect/...`:
10 link trả 404, và có nhiều link gần trùng nhau, chỉ khác vài ký tự (model chép sai token).
Vì vậy nguồn của gpt-oss **không kiểm chứng được**. Báo cáo gpt-oss đã bị xoá khi dọn thư mục; chỉ còn điểm số trong `scoring/consensus.json`.

> Gemini 3.1 Pro (theo kế hoạch ban đầu) không còn trong danh sách model của `agy`,
> nên được thay bằng GPT-OSS 120B để giữ một họ model khác.

## Phương pháp

1. **Claim chuẩn**: tổng hợp 26 khẳng định (K1–K26) từ phần "Top 10 kết luận" của cả 5 báo cáo
   ([scoring/claims.json](scoring/claims.json)).
2. **Ma trận claim × báo cáo**: một subagent đọc toàn văn từng báo cáo rồi cho điểm mỗi claim:
   `2` = khẳng định rõ, `1` = có nhắc / ngầm định, `0` = không đề cập, `-1` = mâu thuẫn.
   Mỗi ô có trích dẫn nguyên văn làm bằng chứng ([scoring/consensus.json](scoring/consensus.json)).
3. **Tương đồng văn bản**: cosine TF-IDF (unigram + bigram âm tiết, đã bỏ phần Nguồn),
   cùng chỉ số Jaccard trên tập domain nguồn ([scoring/lexical.json](scoring/lexical.json)).
4. **Outlier**: những khẳng định chỉ có ở một báo cáo, kèm đánh giá độ tin cậy (40 mục).

## 1. Ma trận đồng thuận

| ID | Claim | A | B | C | Gem | GPT | Σ/10 |
|---|---|---|---|---|---|---|---|
| K6 | Checkpoint người: duyệt spec/plan trước code + duyệt PR trước merge | 2 | 2 | 2 | 2 | 2 | **10** |
| K8 | Cô lập worktree / container là bắt buộc khi song song | 2 | 2 | 2 | 2 | 2 | **10** |
| K13 | Agent gian lận test → test viết trước, khoá quyền sửa, bảo vệ bằng CI | 2 | 2 | 2 | 2 | 2 | **10** |
| K14 | Review chéo bằng model khác / reviewer độc lập | 2 | 2 | 2 | 2 | 2 | **10** |
| K26 | Song song quá mức phản tác dụng | 2 | 2 | 2 | 2 | 2 | **10** |
| K7 | Task nhỏ, tự đủ, có pass/fail, vừa một PR nhỏ | 2 | 2 | 2 | 2 | 1 | 9 |
| K11 | Review của người là nút cổ chai mới | 2 | 2 | 2 | 2 | 1 | 9 |
| K12 | Giới hạn 2–5 agent song song mỗi người / WIP limit | 2 | 2 | 2 | 2 | 1 | 9 |
| K15 | Benchmark công khai bão hoà/nhiễm → cần eval nội bộ | 2 | 2 | 2 | 2 | 1 | 9 |
| K18 | Đo bằng DORA + telemetry, không bằng LOC/số PR | 2 | 2 | 2 | 2 | 1 | 9 |
| K24 | Áp dụng theo giai đoạn 3 tháng, bắt đầu từ task rủi ro thấp | 2 | 2 | 2 | 2 | 1 | 9 |
| K1 | Spec-driven có giá trị cho feature vừa-lớn, quá nặng cho task nhỏ | 2 | 2 | 2 | 1 | 1 | 8 |
| K4 | Multi-agent cho việc song song hoá được; tốn ~15× token | 2 | 2 | 2 | 1 | 1 | 8 |
| K5 | Harness kiểm chứng quyết định chất lượng hơn số agent | 2 | 2 | 2 | 1 | 1 | 8 |
| K17 | AI là bộ khuếch đại (DORA) | 2 | 2 | 2 | 2 | 0 | 8 |
| K19 | Prompt injection chặn bằng kiến trúc (lethal trifecta / Rule of Two) | 2 | 2 | 2 | 1 | 1 | 8 |
| K22 | Code AI tăng trùng lặp/churn | 2 | 2 | 2 | 1 | 1 | 8 |
| K2 | Pipeline có cấu trúc tốt hơn hội thoại tự do giữa nhiều agent | 1 | 2 | 1 | 2 | 1 | 7 |
| K3 | Mặc định 1 agent mạnh viết code; chỉ tách vai để kiểm chứng độc lập | 2 | 2 | 2 | 2 | **-1** | 7 |
| K9 | Chia task song song theo ranh giới file/module, chốt interface trước | 2 | 2 | 1 | 2 | 0 | 7 |
| K10 | AGENTS.md ngắn dạng mục lục; luật bắt buộc → hook/CI | 2 | 2 | 2 | 1 | 0 | 7 |
| K16 | Cảm nhận năng suất của dev không đáng tin (METR) | 2 | 2 | 2 | 1 | 0 | 7 |
| K20 | Supply chain: package ảo giác / slopsquatting | 1 | 2 | 1 | 2 | 1 | 7 |
| K25 | Context engineering là yếu tố then chốt | 1 | 1 | 1 | 2 | 1 | 6 |
| K21 | Multi-agent hỏng chủ yếu do thiết kế/phối hợp (MAST) | 1 | 2 | 1 | 1 | 0 | 5 |
| K23 | Orchestrator-worker + best-of-N là pattern tốt nhất | **-1** | **-1** | **-1** | **-1** | 2 | **-2** |

**Đọc bảng**: 22/26 claim được cả 5 báo cáo ủng hộ ở mức ≥1, hoặc 4/5 báo cáo ủng hộ và báo cáo còn lại
không đề cập. Chỉ có **một điểm bất đồng thật** là K23 (và K3, mặt kia của cùng vấn đề).
gpt-oss cho rằng chia vai kiểu swarm/orchestrator là tốt nhất. Bốn báo cáo còn lại đều khuyến nghị
một agent mạnh viết code, chỉ thêm agent cho review, research hoặc việc thật sự độc lập.

**K25** cần đọc kỹ. Gemini nói AGENTS.md + MCP "quyết định 80% độ chính xác", nhưng con số này
không có nguồn. claude-B dẫn nghiên cứu ETH ([arXiv 2602.11988](https://arxiv.org/abs/2602.11988)):
file context dài **không** tăng tỷ lệ thành công mà còn tăng chi phí hơn 20%.
→ Kết luận an toàn: context file cần có nhưng phải **ngắn**.

## 2. Mức đồng thuận theo báo cáo

| Báo cáo | Σ điểm (max 52) | Khớp với trung vị 4 báo cáo còn lại | Tỉ lệ khớp cặp với mỗi báo cáo khác |
|---|---|---|---|
| claude-B | 48 | 26/26 | 1.00 / 1.00 / 1.00 / 0.73 (với gpt-oss) |
| claude-A | 45 | 26/26 | 1.00 với A/B/C/Gem, 0.73 với gpt-oss |
| claude-C | 44 | 26/26 | như trên |
| gemini-flash | 41 | 26/26 | như trên |
| gpt-oss | 25 | **19/26** | 0.73 với cả 4 |

(Tỉ lệ khớp cặp = tỉ lệ claim mà hai báo cáo cùng rơi vào một nhóm: ủng hộ / không nói / mâu thuẫn.)

## 3. Tương đồng văn bản (TF-IDF cosine)

|  | Gem | GPT | A | B | C |
|---|---|---|---|---|---|
| gemini-flash | 1 | .236 | .243 | .243 | .231 |
| gpt-oss | .236 | 1 | .207 | .216 | .216 |
| claude-A | .243 | .207 | 1 | **.329** | **.315** |
| claude-B | .243 | .216 | **.329** | 1 | **.312** |
| claude-C | .231 | .216 | **.315** | **.312** | 1 |

Jaccard domain nguồn: A–B 0,25, B–C 0,20, A–C 0,14, Gemini–Claude 0,08–0,14, gpt-oss–mọi báo cáo **0**.

**Diễn giải**: tương đồng từ vựng giữa ba báo cáo Claude (~0,31–0,33) cao hơn giữa Claude và agy
(~0,21–0,24). Điều này có thể do cùng họ model và cùng một số nguồn gốc, nên **không** phải bằng
chứng độc lập. Bằng chứng mạnh hơn là Gemini Flash, khác model, khác nguồn và có tương đồng từ vựng
thấp, vẫn đi đến **cùng kết luận** ở 26/26 claim.

## 4. Outlier đáng chú ý (chỉ một báo cáo nêu)

**Có nguồn tốt, đáng đưa vào báo cáo:**
- Stripe Minions: hơn 1.000 PR merge mỗi tuần, 100% có người review, tối đa 2 vòng CI (claude-C,
  [stripe.dev](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)).
- Slopsquatting: 19,7% package được gợi ý không tồn tại, 43% tên lặp lại ở mọi lần chạy (claude-B,
  [arXiv 2406.10279](https://arxiv.org/abs/2406.10279), USENIX Security 2025).
- Tấn công s1ngularity (Nx, 08/2025): script postinstall gọi agent CLI với `--yolo` để lục secrets (claude-C,
  [Wiz](https://wiz.io/blog/s1ngularity-supply-chain-attack)).
- METR 02/2026 (57 dev, hơn 800 task): khoảng tin cậy chứa 0, tức chưa chứng minh được tăng tốc
  (claude-A, [metr.org](https://metr.org/blog/2026-02-24-uplift-update/)).
- Meta "Agents Rule of Two" (claude-C), một khung bổ sung cho lethal trifecta.
- Anthropic C compiler: 16 agent, khoảng 20.000 USD, khoảng 100K dòng Rust (claude-A), một case study về chi phí.

**Không đáng tin, loại bỏ:**
- gpt-oss: "swarm chính xác hơn 12–18%", "cross-model review +12%", "DORA khuyến cáo task 200–500 LOC
  và 4–6 worker", "cost/PR ~$0,12", bảng metric "CFR 15%→4%". Không có nguồn truy được,
  và mâu thuẫn với DORA 2024/2025.
- gemini-flash: "context quyết định 80% độ chính xác", "kỹ sư dành 70% thời gian đọc spec (DORA)",
  "token inflation 20–50×". Các con số này không có trong nguồn được dẫn.
- Faros 2026 "thời gian review +441%" (claude-A): cần đọc bản gốc, vì số này lệch xa mức +91% của Faros 2025.

## 5. Giới hạn của việc chấm

- Danh sách claim và người chấm đều là Claude, nên có thể thiên về cách đóng khung của báo cáo Claude.
  Để giảm thiểu: claim được lấy từ Top 10 của **cả 5** báo cáo, mỗi điểm phải kèm trích dẫn nguyên văn,
  và tôi đã đối chiếu riêng bằng tương đồng từ vựng.
- Hai lần chạy `agy` chỉ mất khoảng 150 giây và 1 turn mỗi lần, nên mức nghiên cứu nông hơn hẳn
  3 subagent Claude (khoảng 40–46 tool call mỗi agent).
- Một số số liệu vendor (Devin merge rate, Coinbase "95% AI-assisted", OpenAI harness) là số tự báo cáo
  hoặc lấy từ nguồn thứ cấp.

---

# Phần B — Đồng thuận giữa 14 video YouTube và research

Ngày chấm: 2026-10-13. Video và bản phân tích nằm ở [video-youtube/](video-youtube/).
Dữ liệu chấm: [scoring/video-consensus-a.json](scoring/video-consensus-a.json) (v01–v06),
[video-consensus-b.json](scoring/video-consensus-b.json) (v07–v12), [video-consensus-c.json](scoring/video-consensus-c.json) (v13),
[video-consensus-d.json](scoring/video-consensus-d.json) (v14, chấm ngày 2026-10-23),
[video-agy-scores.json](scoring/video-agy-scores.json), [video-merged.json](scoring/video-merged.json), [video-claims.json](scoring/video-claims.json).
Script tạo bảng: `scoring/merge_video.py` → `scoring/render_partB.py`.

## Phương pháp

- **Người chấm chính**: 4 Claude subagent (v01–06, v07–12, v13, v14). Điểm 2 hoặc -1 chỉ được cho khi có câu trích
  **nguyên văn trong transcript** kèm [mm:ss]. Script đã so khớp lại toàn bộ trích dẫn.
- **Người chấm thứ hai**: `agy` (Gemini 3.8 Flash) chấm độc lập cả 14 video, chỉ cho điểm, không kèm trích dẫn.
- **Độ khớp giữa hai người chấm**: trùng điểm tuyệt đối 62%, trùng nhóm (ủng hộ / không nói / mâu thuẫn) 70%,
  **Cohen's κ = 0.44** (mức vừa), sai lệch trung bình (MAE) 0.41.
  agy chấm **dễ hơn rõ rệt**. Ví dụ, agy cho K21 (MAST) được 12/14 video ủng hộ, dù không video nào nhắc tới MAST.
  → **Điểm của Claude (có bằng chứng) là số chính**; điểm agy chỉ dùng để kiểm tra độ nhạy.
- **Độ mạnh bằng chứng của video** (1–5): v03 Builder.io, v04 Factory, v08 HumanLayer và v14 theSeniorDev đạt 3 (thực chiến hoặc talk
  production, số liệu tự báo cáo). v01, v05, v06, v07, v10, v11, v12, v13 đạt 2 (tutorial hoặc dự án cá nhân).
  v02 và v09 đạt 1 (demo, tin sản phẩm). **Không video nào có số liệu đo có phương pháp.**
- **Nguồn transcript**: v01–v12 dùng phụ đề YouTube (tải bằng `youtube-transcript-api`). Riêng v13 được Gemini 3.1 Pro
  trong AI Studio chép từ video, vì YouTube chặn IP khi tải phụ đề. Nên trích dẫn của v13 được đối chiếu với
  bản chép của một model, không phải phụ đề gốc.

## 1. Claim K1–K26: research so với video

Ký hiệu cột video, theo thứ tự v01 → v14: ● = 2 (khẳng định rõ), ◐ = 1 (nhắc một phần), · = 0 (không nói), ✗ = -1 (mâu thuẫn).

| ID | Claim (rút gọn) | Research (≥1/5) | v01…v14 (Claude) | Video ≥1 | agy ≥1 | Nhận xét |
|---|---|---|---|---|---|---|
| K5 | Harness kiểm chứng quyết định chất lượng | 5/5 | `◐·●●◐●◐◐◐◐●●●●` | **13/14** | 13 | **Đồng thuận mạnh nhất** |
| K2 | Pipeline có cấu trúc > hội thoại tự do | 5/5 | `◐·◐◐◐●◐◐·●●◐●◐` | **12/14** | 13 | Đồng thuận |
| K6 | Checkpoint người: plan + PR | 5/5 | `◐◐◐·◐◐◐●◐●·◐●◐` | **12/14** | 14 | Đồng thuận (nhưng xem V2) |
| K3 | 1 agent mạnh viết code, tách vai để kiểm chứng | 4/5 | `◐·◐◐◐◐··◐◐◐●◐◐` | **11/14** | 12 | Đồng thuận, phần lớn ở mức ◐ |
| K25 | Context engineering then chốt | 5/5 | `·●◐●·◐·◐·◐◐●●●` | **10/14** | 14 | Đồng thuận; v13: phiên mới để tránh "context rot" |
| K14 | Review chéo / reviewer độc lập | 5/5 | `◐·●◐◐●·◐·◐◐●·●` | **10/14** | 12 | Đồng thuận |
| K8 | Cô lập worktree / sandbox | 5/5 | `●·◐◐·●·◐·●◐●·◐` | 9/14 | 9 | Đồng thuận (nhưng xem V19) |
| K7 | Task nhỏ, có pass/fail | 5/5 | `··●◐◐··◐·●·◐●◐` | 8/14 | 12 | Trung bình |
| K21 | Lỗi multi-agent do thiết kế/phối hợp | 4/5 | `◐·◐◐·◐··●··◐·◐` | 7/14 | 13 | Trung bình |
| K1 | Spec-first cho feature vừa-lớn | 5/5 | `◐··◐···●·◐·●◐·` | 6/14 | 7 | Trung bình |
| K4 | Multi-agent tốn token, chỉ cho việc song song hoá được | 5/5 | `◐·◐◐····●··●·◐` | 6/14 | 10 | v12: "~7× token" |
| K11 | Review của người là nút cổ chai | 5/5 | `◐·◐·●◐·●·····◐` | 6/14 | 10 | Trung bình |
| K22 | Code AI tăng trùng lặp/bloat | 5/5 | `··◐●·●·····◐·●` | 5/14 | 10 | Yếu |
| K18 | Đo bằng DORA/telemetry | 5/5 | `··◐···◐◐··◐··◐` | 5/14 | 8 | Yếu; video đo *lần chạy* (V5), không đo DORA |
| K23 | Orchestrator + best-of-N là tốt nhất | 1/5 | `◐··◐··◐·◐··◐··` | 5/14 | 1 | Video **cởi mở với orchestrator hơn** research, nhưng v04 nói worker tuần tự, không swarm |
| K26 | Song song quá mức phản tác dụng | 5/5 | `◐·◐··✗·◐◐··●··` | 5/14 | 11 | **v06 mâu thuẫn** |
| K24 | Áp dụng theo giai đoạn | 5/5 | `··●······◐·◐·◐` | 4/14 | 12 | Yếu |
| K19 | Prompt injection, chặn bằng kiến trúc | 5/5 | `·◐····◐◐···◐··` | 4/14 | 10 | **Video gần như bỏ qua** |
| K13 | Reward hacking → khoá test | 5/5 | `···●·◐·······◐` | 3/14 | 8 | **Video gần như bỏ qua** (chỉ v04) |
| K10 | AGENTS.md ngắn, luật → hook | 4/5 | `·····◐·····◐·◐` | 3/14 | 6 | Yếu |
| K17 | AI là bộ khuếch đại (DORA) | 4/5 | `···●·········◐` | 2/14 | 10 | Chỉ v04 ("power law") |
| K9 | Chia task theo ranh giới file | 4/5 | `···········◐◐·` | 2/14 | 9 | Video gần như không bàn |
| K15 | Benchmark công khai không đáng tin | 5/5 | `·······◐··◐···` | 2/14 | 3 | Video không bàn |
| K12 | WIP limit 2–5 agent/người | 5/5 | `·····✗◐··✗·◐··` | 2/14 | 9 | **Bất đồng: v06, v10 mâu thuẫn** |
| K20 | Slopsquatting / supply chain | 5/5 | `···········◐··` | 1/14 | 1 | **Video bỏ qua** |
| K16 | Cảm nhận năng suất không đáng tin | 4/5 | `··············` | 0/14 | 2 | **Video bỏ qua** |

**Đọc bảng:**
- **Video xác nhận phần "cách làm"** của research: harness kiểm chứng (K5), pipeline có cấu trúc (K2),
  checkpoint người (K6), một agent viết code (K3), reviewer độc lập (K14), context (K25), worktree (K8).
- **Video im lặng về phần "rủi ro và đo lường"**: reward hacking (K13), supply chain (K20), prompt injection (K19),
  ảo tưởng năng suất (K16), benchmark (K15), DORA (K17, K18). Đây là **điểm mù của nội dung YouTube**.
  Research có nguồn tốt ở các mục này, nên giữ nguyên khuyến nghị của research.
- **Bất đồng thật**: K12/K26. v06 khoe chạy song song 15 feature "không xung đột", v10 nói "10, 20 tickets at a time".
  Research (Faros, DORA) cho thấy làm vậy sẽ dồn tắc ở khâu review. Cả hai video đều là trình diễn
  một người làm, không có số đo, nên **giữ khuyến nghị WIP limit**.

## 2. Claim mới chỉ có trong video (V1–V22)

| ID | Claim | Video | n | Đánh giá |
|---|---|---|---|---|
| V3 | Model routing theo pha/chi phí: model mạnh cho plan/orchestrate/review, model rẻ cho scan/worker; chọn model rẻ nhất vượt ngưỡng độ khó | v01 v03 v04 v07 v08 v11 v12 v14 | **8** | Thực hành phổ biến; v04 tự báo cáo tiết kiệm ~25% |
| V1 | Code tất định điều phối pipeline (polling, gate, CI, retry, rollout); agent chỉ làm bước cần phán đoán — 'agent proposes, code disposes' | v02 v05 v07 v08 v10 v11 | **6** | Đồng thuận cao giữa practitioner; khớp ý "harness" của research |
| V4 | Khép vòng với production: telemetry/Sentry/feedback/incident tự thành ticket; job định kỳ (bug finder, health check, watchdog việc bỏ dở, lookback hàng tuần) | v03 v04 v05 v07 v10 v14 | **6** | Thực chiến, định tính |
| V7 | Kiểm chứng tốn kém (~40% một mission) và phải end-to-end thật: browser/computer-use, PR kèm bằng chứng before/after, repro suite làm regression | v03 v04 v06 v08 v13 v14 | **6** | v04 có số (tự báo cáo); v13: kiểm chứng viết trước |
| V2 | Phân loại rủi ro thay đổi để định tuyến: low-risk được auto-merge/agent tự sửa, high-risk (DB, infra, khó) bắt buộc người duyệt plan/PR | v01 v03 v05 v08 v14 | **5** | **Căng với K6** (research: người duyệt mọi PR) |
| V11 | Vệ sinh context: nạp tool dần (progressive disclosure, ~50% token), không đẩy output test pass vào context, compact thủ công, MCP ổn định → skill/script | v04 v11 v12 v13 | 4 | Bổ sung cho K10/K25 |
| V5 | Đo từng lần chạy (token, thời gian, kết quả) để agent/người tối ưu prompt-harness-model (self-improving, A/B) | v01 v07 v11 | 3 | Demo |
| V6 | Vòng bot-review có giới hạn lặp: agent phải xử lý mọi comment/CI fail, chỉ báo người khi bot reviewer đạt ngưỡng | v03 v06 v08 | 3 | Thực chiến (Boundary: max 3 vòng) |
| V9 | Factory cho việc cơ học/nền/chạy lâu (20–60 phút); việc thiết kế, lặp nhanh, việc khó vẫn làm tương tác với agent local | v07 v10 v11 | 3 | Ý kiến, khớp K7/K24 |
| V12 | Worker chạy tuần tự với context sạch; song song chỉ ở sub-agent nhỏ trong một bước; xác suất thành công giảm theo 0.95^n khi thêm agent | v04 v12 v13 | 3 | Củng cố K3/K26 |
| V13 | Tự sở hữu tầng dev environment (môi trường dạng 'cattle'), tách control plane / data plane; dùng monorepo hoặc mô phỏng monorepo, tránh submodule | v07 v08 v14 | 3 | Ý kiến kiến trúc |
| V20 | Tự xây factory đơn giản từ skill/markdown, chọn lọc từng phần, harness/model-agnostic — thay vì framework/sản phẩm áp toàn bộ SDLC (Spec Kit, Gastown...) | v01 v06 v13 | 3 | Ý kiến; khớp khuyến nghị "chưa cần framework nặng" của research |
| V8 | Nhắm ~95% tự động, không 100%: luôn có đường thoát lên người khi vượt số vòng lặp hoặc không tạo được repro | v08 v14 | 2 | Ý kiến của người vận hành production |
| V10 | Factory dùng chung cho cả team (cùng prompt/harness/model) như CI/CD, thay vì mỗi dev tự cấu hình | v07 v10 | 2 | Ý kiến |
| V14 | Lỗi lặp lại ≥2 lần → thêm rule ngay; bộ nhớ lessons.md tích luỹ bài học sự cố | v02 v12 | 2 | Khớp bước "retro" của research |
| V15 | Bàn giao giữa các pha bằng JSON có schema, được validate | v11 v13 | 2 | Demo |
| V21 | Agent phải phỏng vấn/hỏi lại người trước khi viết PRD/spec/plan hoặc nhận việc, để loại giả định ngầm | v03 v13 | 2 | Ý kiến; khớp bước Brief của research (agent phỏng vấn) |
| V16 | Tách beta (auto-fix, đồng bộ main) và production (cắt deploy 1 lần/ngày) để giới hạn blast radius | v03 | 1 | Thực chiến |
| V17 | Prototype lớn ('slop PR') làm spec sống, rồi cho model chia lại thành chuỗi PR nhỏ dễ review | v08 | 1 | Thực chiến |
| V18 | Kiểm soát chi phí multi-agent: ước tính trước khi chạy, pause/resume khi hết quota | v09 | 1 | Phản ánh người dùng |
| V19 | Factory chạy trên máy/môi trường thật của dev vì kiểm chứng cần env, keys, session thật (đối lập với sandbox cô lập) | v03 | 1 | **Căng với K8/K19** (sandbox) |
| V22 | Tách PRD (what/why) và spec (how) thành hai phiên riêng; mọi artifact theo template cố định; người review plan tập trung vào chiến lược kiểm chứng (exit criteria) | v13 | 1 | Ý kiến (tutorial) |
| V23 | Ưu tiên e2e test chạy trên môi trường thật theo feature hơn unit test/TDD do agent tự viết; TDD với agent bị coi là phí token khi code thay đổi nhanh | v14 | 1 | **Căng với K13** (research: test viết trước, khoá lại); v14 vẫn tin E2E |
| V24 | Khi agent làm sai thì sửa factory (gate, context, kiến trúc) chứ không vá từng component; postmortem sự cố để tìm thay đổi kiến trúc, nghĩ theo hệ quả bậc 2–3 | v14 | 1 | Khớp bước retro/postmortem của research |
| V25 | Thiết kế codebase thân thiện với agent (modular, ranh giới rõ để giới hạn lỗi) kèm một lớp quy tắc/bất biến tĩnh (formal verification) mà agent không thể phá | v14 | 1 | Khớp mục "bất biến" trong template kiến trúc; formal verification còn sớm |
| V26 | Cấp cho agent dữ liệu giống production đã ẩn danh (mock production data, giữ hình dạng/độ dài dữ liệu thật) để tái hiện bug chính xác | v14 | 1 | Khớp nguyên tắc không dùng dữ liệu production thật |

## 3. Kết luận chấm gộp

1. **Không có mâu thuẫn ở cốt lõi.** 7 claim (K2, K3, K5, K6, K8, K14, K25) được cả research (≥4/5)
   lẫn đa số video (≥8/14) ủng hộ. Đây là phần đáng tin nhất của quy trình. K5 (harness kiểm chứng) được 13/14 video nhắc; video duy nhất không nhắc là v02 (agent SRE, không bàn quy trình code).
2. **Video bổ sung tầng "vận hành factory"** mà research còn mỏng: code tất định điều phối (V1),
   model routing (V3), khép vòng production (V4), định tuyến theo rủi ro (V2), kiểm chứng E2E (V7).
3. **Ba điểm căng cần quyết định khi áp dụng:**
   - **Auto-merge low-risk (V2) hay người duyệt 100% (K6)?** Đề xuất: tháng 1–2 duyệt 100% như Stripe.
     Chỉ bật auto-merge cho một danh mục rất hẹp (docs, dependency patch, test bổ sung) **sau khi**
     có baseline CFR và eval nội bộ.
   - **Song song lớn (v06, v10) hay WIP limit (K12)?** Giữ WIP limit vì video không có số đo.
   - **Chạy trên máy dev (V19) hay sandbox (K8/K19)?** Dùng sandbox có env tái lập được.
     Nếu bắt buộc chạy trên máy thật thì không cho agent đủ cả 3 yếu tố của lethal trifecta.
4. **Người chấm Gemini dễ dãi.** Với κ = 0.44 và lệch điểm có hệ thống, **không nên dùng agy làm người chấm duy nhất**.
   Nên dùng agy để tóm tắt (trích dẫn chính xác 65/65), còn khâu chấm cần người chấm bắt buộc kèm bằng chứng.

import json
m=json.load(open('scoring/video-merged.json')); V=m['videos']; c=m['claude']; g=m['agy']; ir=m['interrater']
rs=json.load(open('scoring/consensus.json'))['scores']
short={"K1":"Spec-first cho feature vừa-lớn","K2":"Pipeline có cấu trúc > hội thoại tự do","K3":"1 agent mạnh viết code, tách vai để kiểm chứng","K4":"Multi-agent tốn token, chỉ cho việc song song hoá được","K5":"Harness kiểm chứng quyết định chất lượng","K6":"Checkpoint người: plan + PR","K7":"Task nhỏ, có pass/fail","K8":"Cô lập worktree / sandbox","K9":"Chia task theo ranh giới file","K10":"AGENTS.md ngắn, luật → hook","K11":"Review của người là nút cổ chai","K12":"WIP limit 2–5 agent/người","K13":"Reward hacking → khoá test","K14":"Review chéo / reviewer độc lập","K15":"Benchmark công khai không đáng tin","K16":"Cảm nhận năng suất không đáng tin","K17":"AI là bộ khuếch đại (DORA)","K18":"Đo bằng DORA/telemetry","K19":"Prompt injection, chặn bằng kiến trúc","K20":"Slopsquatting / supply chain","K21":"Lỗi multi-agent do thiết kế/phối hợp","K22":"Code AI tăng trùng lặp/bloat","K23":"Orchestrator + best-of-N là tốt nhất","K24":"Áp dụng theo giai đoạn","K25":"Context engineering then chốt","K26":"Song song quá mức phản tác dụng"}
note={"K5":"**Đồng thuận mạnh nhất**","K2":"Đồng thuận","K6":"Đồng thuận (nhưng xem V2)","K3":"Đồng thuận, phần lớn ở mức ◐","K14":"Đồng thuận","K25":"Đồng thuận; v13: phiên mới để tránh \"context rot\"","K8":"Đồng thuận (nhưng xem V19)","K7":"Trung bình","K21":"Trung bình","K1":"Trung bình","K4":"v12: \"~7× token\"","K11":"Trung bình","K26":"**v06 mâu thuẫn**","K22":"Yếu","K18":"Yếu; video đo *lần chạy* (V5), không đo DORA","K19":"**Video gần như bỏ qua**","K24":"Yếu","K12":"**Bất đồng: v06, v10 mâu thuẫn**","K13":"**Video gần như bỏ qua** (chỉ v04)","K10":"Yếu","K15":"Video không bàn","K23":"Video **cởi mở với orchestrator hơn** research, nhưng v04 nói worker tuần tự, không swarm","K9":"Video gần như không bàn","K17":"Chỉ v04 (\"power law\")","K20":"**Video bỏ qua**","K16":"**Video bỏ qua**"}
G={2:'●',1:'◐',0:'·',-1:'✗'}; n=len(V)
rows=[]
for k in c:
    s=[c[k][v] for v in V]; sup=sum(x>=1 for x in s); w=sum(x for x in s)
    rows.append((sup,w,k,s))
rows.sort(key=lambda r:(-r[0],-r[1]))
out=[]
out.append(f"""# Phần B — Đồng thuận giữa {n} video YouTube và research

Ngày chấm: 2026-10-13. Video và bản phân tích nằm ở [video-youtube/](video-youtube/).
Dữ liệu chấm: [scoring/video-consensus-a.json](scoring/video-consensus-a.json) (v01–v06),
[video-consensus-b.json](scoring/video-consensus-b.json) (v07–v12), [video-consensus-c.json](scoring/video-consensus-c.json) (v13),
[video-agy-scores.json](scoring/video-agy-scores.json), [video-merged.json](scoring/video-merged.json), [video-claims.json](scoring/video-claims.json).
Script tạo bảng: `scoring/merge_video.py` → `scoring/render_partB.py`.

## Phương pháp

- **Người chấm chính**: 3 Claude subagent (v01–06, v07–12, v13). Điểm 2 hoặc -1 chỉ được cho khi có câu trích
  **nguyên văn trong transcript** kèm [mm:ss]. Script đã so khớp lại toàn bộ trích dẫn.
- **Người chấm thứ hai**: `agy` (Gemini 3.8 Flash) chấm độc lập cả {n} video, chỉ cho điểm, không kèm trích dẫn.
- **Độ khớp giữa hai người chấm**: trùng điểm tuyệt đối {ir['exact']:.0%}, trùng nhóm (ủng hộ / không nói / mâu thuẫn) {ir['bucket']:.0%},
  **Cohen's κ = {ir['kappa']:.2f}** (mức vừa), sai lệch trung bình (MAE) {ir['mae']:.2f}.
  agy chấm **dễ hơn rõ rệt**. Ví dụ, agy cho K21 (MAST) được 12/{n} video ủng hộ, dù không video nào nhắc tới MAST.
  → **Điểm của Claude (có bằng chứng) là số chính**; điểm agy chỉ dùng để kiểm tra độ nhạy.
- **Độ mạnh bằng chứng của video** (1–5): v03 Builder.io, v04 Factory và v08 HumanLayer đạt 3 (thực chiến hoặc talk
  production, số liệu tự báo cáo). v01, v05, v06, v07, v10, v11, v12, v13 đạt 2 (tutorial hoặc dự án cá nhân).
  v02 và v09 đạt 1 (demo, tin sản phẩm). **Không video nào có số liệu đo có phương pháp.**
- **Nguồn transcript**: v01–v12 dùng phụ đề YouTube (tải bằng `youtube-transcript-api`). Riêng v13 được Gemini 3.1 Pro
  trong AI Studio chép từ video, vì YouTube chặn IP khi tải phụ đề. Nên trích dẫn của v13 được đối chiếu với
  bản chép của một model, không phải phụ đề gốc.

## 1. Claim K1–K26: research so với video

Ký hiệu cột video, theo thứ tự v01 → v{n:02d}: ● = 2 (khẳng định rõ), ◐ = 1 (nhắc một phần), · = 0 (không nói), ✗ = -1 (mâu thuẫn).

| ID | Claim (rút gọn) | Research (≥1/5) | v01…v{n:02d} (Claude) | Video ≥1 | agy ≥1 | Nhận xét |
|---|---|---|---|---|---|---|""")
for sup,w,k,s in rows:
    r=sum(1 for x in rs[k].values() if x['score']>=1)
    ag=sum(1 for v in V if g[k][v]>=1)
    vs=f"**{sup}/{n}**" if sup>=10 else f"{sup}/{n}"
    out.append(f"| {k} | {short[k]} | {r}/5 | `{''.join(G[x] for x in s)}` | {vs} | {ag} | {note[k]} |")
out.append(f"""
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
|---|---|---|---|---|""")
vc=json.load(open('scoring/video-claims.json'))
ev={"V1":"Đồng thuận cao giữa practitioner; khớp ý \"harness\" của research","V2":"**Căng với K6** (research: người duyệt mọi PR)","V3":"Thực hành phổ biến; v04 tự báo cáo tiết kiệm ~25%","V4":"Thực chiến, định tính","V5":"Demo","V6":"Thực chiến (Boundary: max 3 vòng)","V7":"v04 có số (tự báo cáo); v13: kiểm chứng viết trước","V8":"Ý kiến của người vận hành production","V9":"Ý kiến, khớp K7/K24","V10":"Ý kiến","V11":"Bổ sung cho K10/K25","V12":"Củng cố K3/K26","V13":"Ý kiến kiến trúc","V14":"Khớp bước \"retro\" của research","V15":"Demo","V16":"Thực chiến","V17":"Thực chiến","V18":"Phản ánh người dùng","V19":"**Căng với K8/K19** (sandbox)","V20":"Ý kiến; khớp khuyến nghị \"chưa cần framework nặng\" của research","V21":"Ý kiến; khớp bước Brief của research (agent phỏng vấn)","V22":"Ý kiến (tutorial)"}
for x in sorted(vc,key=lambda x:-len(x['videos'])):
    k=len(x['videos']); out.append(f"| {x['id']} | {x['claim']} | {' '.join(x['videos'])} | {'**'+str(k)+'**' if k>=5 else k} | {ev[x['id']]} |")
out.append(f"""
## 3. Kết luận chấm gộp

1. **Không có mâu thuẫn ở cốt lõi.** 7 claim (K2, K3, K5, K6, K8, K14, K25) được cả research (≥4/5)
   lẫn đa số video (≥8/{n}) ủng hộ. Đây là phần đáng tin nhất của quy trình. K5 (harness kiểm chứng) được 12/{n} video nhắc; video duy nhất không nhắc là v02 (agent SRE, không bàn quy trình code).
2. **Video bổ sung tầng "vận hành factory"** mà research còn mỏng: code tất định điều phối (V1),
   model routing (V3), khép vòng production (V4), định tuyến theo rủi ro (V2), kiểm chứng E2E (V7).
3. **Ba điểm căng cần quyết định khi áp dụng:**
   - **Auto-merge low-risk (V2) hay người duyệt 100% (K6)?** Đề xuất: tháng 1–2 duyệt 100% như Stripe.
     Chỉ bật auto-merge cho một danh mục rất hẹp (docs, dependency patch, test bổ sung) **sau khi**
     có baseline CFR và eval nội bộ.
   - **Song song lớn (v06, v10) hay WIP limit (K12)?** Giữ WIP limit vì video không có số đo.
   - **Chạy trên máy dev (V19) hay sandbox (K8/K19)?** Dùng sandbox có env tái lập được.
     Nếu bắt buộc chạy trên máy thật thì không cho agent đủ cả 3 yếu tố của lethal trifecta.
4. **Người chấm Gemini dễ dãi.** Với κ = {ir['kappa']:.2f} và lệch điểm có hệ thống, **không nên dùng agy làm người chấm duy nhất**.
   Nên dùng agy để tóm tắt (trích dẫn chính xác 65/65), còn khâu chấm cần người chấm bắt buộc kèm bằng chứng.
""")
doc=open('CONSENSUS.md').read()
i=doc.index('# Phần B')
open('CONSENSUS.md','w').write(doc[:i]+'\n'.join(out))
print('ok')

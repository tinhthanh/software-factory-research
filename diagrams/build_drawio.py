"""Sinh software-factory.drawio (4 trang) từ kết quả research. Chạy: python3 build_drawio.py"""
from xml.sax.saxutils import escape
import os

# màu theo vai trò
HUMAN = "fillColor=#fff2cc;strokeColor=#d6b656;"
AI = "fillColor=#dae8fc;strokeColor=#6c8ebf;"
CODE = "fillColor=#d5e8d4;strokeColor=#82b366;"
GATE = "fillColor=#ffe6cc;strokeColor=#d79b00;"
RISK = "fillColor=#f8cecc;strokeColor=#b85450;"
NOTE = "fillColor=#f5f5f5;strokeColor=#999999;fontColor=#333333;"
PURPLE = "fillColor=#e1d5e7;strokeColor=#9673a6;"
BOX = "rounded=1;whiteSpace=wrap;html=1;arcSize=8;fontSize=12;spacing=6;"
TEXT = "text;html=1;whiteSpace=wrap;align=left;verticalAlign=top;fontSize=12;"
EDGE = "edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;fontSize=11;endArrow=block;endFill=1;strokeWidth=1.5;"


class Page:
    def __init__(self, name, w=1800, h=1100):
        self.name, self.w, self.h, self.cells, self.n = name, w, h, [], 0

    def _id(self):
        self.n += 1
        return f"c{self.n}"

    def box(self, label, x, y, w, h, style=BOX + AI, parent="1"):
        i = self._id()
        self.cells.append(f'<mxCell id="{i}" value="{escape(label, {chr(34): "&quot;"})}" style="{style}" vertex="1" parent="{parent}"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        return i

    def text(self, label, x, y, w, h, extra=""):
        return self.box(label, x, y, w, h, TEXT + extra)

    def edge(self, s, t, label="", style="", pts=None):
        i = self._id()
        geo = '<mxGeometry relative="1" as="geometry">'
        if pts:
            geo += '<Array as="points">' + "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts) + "</Array>"
        geo += "</mxGeometry>"
        self.cells.append(f'<mxCell id="{i}" value="{escape(label, {chr(34): "&quot;"})}" style="{EDGE}{style}" edge="1" parent="1" source="{s}" target="{t}">{geo}</mxCell>')
        return i

    def xml(self, idx):
        body = "".join(self.cells)
        return (f'<diagram id="p{idx}" name="{escape(self.name)}"><mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" '
                f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{self.w}" pageHeight="{self.h}" math="0" shadow="0">'
                f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>{body}</root></mxGraphModel></diagram>')


def title(p, t, sub):
    p.text(f"<b style='font-size:22px'>{t}</b><br><span style='color:#666'>{sub}</span>", 40, 15, 1500, 60)


# ---------------------------------------------------------------- Trang 1: quy trình 8 bước
def page_process():
    p = Page("1. Quy trình 8 bước", 2000, 900)
    title(p, "Vòng đời một feature trong AI Software Factory (8 bước, 2 gate người)",
          "Đồng thuận: research R 5/5 · video V 11/13 (checkpoint người), V 12/13 (harness kiểm chứng). Mũi tên đứt = vòng lặp sửa lỗi.")
    lanes = [("👤 Con người<br>(PM · Tech lead · Reviewer)", HUMAN, 90),
             ("🤖 AI agent<br>(coder · reviewer · test designer)", AI, 300),
             ("⚙️ Code tất định / CI<br>(script · hook · pipeline)", CODE, 510)]
    for lbl, col, y in lanes:
        p.box(f"<b>{lbl}</b>", 30, y, 150, 200, "rounded=0;whiteSpace=wrap;html=1;fontSize=12;" + col)
        p.box("", 180, y, 1790, 200, "rounded=0;whiteSpace=wrap;html=1;fillColor=none;dashed=1;strokeColor=#bbbbbb;")
    X = lambda i: 200 + i * 220  # cột bước i (0..7)
    W, H = 190, 110

    b1 = p.box("<b>1. Brief</b><br>mục tiêu + acceptance criteria đo được", X(0), 135, W, H, BOX + HUMAN)
    b1a = p.box("Agent <b>phỏng vấn</b> người, khảo sát code<br><i style='font-size:10px'>(loại giả định ngầm — v13)</i>", X(0), 345, W, H, BOX + AI)
    b2 = p.box("<b>2. Plan / Spec</b><br>plan.md (task nhỏ) hoặc specs/*.md (feature lớn), đọc code read-only", X(1), 345, W, H, BOX + AI)
    g1 = p.box("<b>Gate 1</b><br>TL duyệt plan<br><span style='font-size:10px'>trọng tâm: chiến lược kiểm chứng</span>", X(1) - 5, 115, W + 10, 150, "rhombus;whiteSpace=wrap;html=1;fontSize=11;" + GATE)
    b3 = p.box("<b>3. Breakdown</b><br>task ≤ 1 PR (~30' review), không chồng file<br>+ <b>test chấp nhận viết trước</b>", X(2), 345, W, H, BOX + AI)
    b3c = p.box("<b>Khoá test</b><br>hook/CI chặn sửa test, CI config, lockfile", X(2), 555, W, H, BOX + CODE)
    b4 = p.box("<b>4. Implement</b><br>1 agent · 1 worktree · 1 sandbox<br>plan → code → test + bằng chứng", X(3), 345, W, H, BOX + AI)
    n4 = p.box("WIP: 2–3 agent / dev<br>(tăng khi review theo kịp)", X(3), 140, W, 70, BOX + NOTE)
    b5 = p.box("<b>5. Gate tự động</b><br>lint · type · test · SAST · secret scan · trùng lặp · chặn dependency mới", X(4), 555, W, H, BOX + CODE)
    b6 = p.box("<b>6. AI review</b><br>context sạch, <b>model khác</b>, đối chiếu spec, gắn nhãn rủi ro, before/after", X(5), 345, W, H, BOX + AI)
    g2 = p.box("<b>Gate 2</b><br>Người review + approve<br><span style='font-size:10px'>không phải người giao task</span>", X(6) - 5, 115, W + 10, 150, "rhombus;whiteSpace=wrap;html=1;fontSize=11;" + GATE)
    b8 = p.box("<b>8. Deploy</b><br>feature flag / canary<br>(rollout bằng code)", X(7), 555, W, H, BOX + CODE)
    b8a = p.box("Theo dõi metric/log khi rollout<br>Sentry / incident → <b>ticket mới</b>", X(7), 345, W, H, BOX + AI)
    b8h = p.box("<b>Retro tuần</b><br>lỗi lặp ≥2 lần → rule AGENTS.md / hook / eval case", X(7), 135, W, H, BOX + HUMAN)

    dashed = "dashed=1;strokeColor=#b85450;fontColor=#b85450;"
    p.edge(b1, b1a, "")
    p.edge(b1a, b2, "")
    p.edge(b2, g1, "")
    p.edge(g1, b3, "duyệt", pts=[(X(2) + W / 2, 190)])
    p.edge(g1, b2, "sửa plan", dashed, pts=[(X(1) + W + 15, 190), (X(1) + W + 15, 400)])
    p.edge(b3, b3c, "")
    p.edge(b3, b4, "")
    p.edge(b4, b5, "", pts=[(X(3) + W / 2, 610)])
    p.edge(b5, b4, "fail (≤2–3 vòng)", dashed, pts=[(X(4) + W / 2, 470), (X(3) + W, 470)])
    p.edge(b5, b6, "pass", pts=[(X(5) + W / 2, 610)])
    p.edge(b6, b4, "comment → sửa (vòng có giới hạn)", dashed, pts=[(X(5) + W / 2, 320), (X(3) + W / 2, 320)])
    p.edge(b6, g2, "bot hài lòng", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;", pts=[(X(6) - 25, 400), (X(6) - 25, 190)])
    p.edge(g2, b8, "merge", pts=[(X(6) + W / 2, 610)])
    p.edge(b8, b8a, "")
    p.edge(b8a, b8h, "")
    p.edge(b8a, b1, "ticket mới (khép vòng production)", "dashed=1;strokeColor=#6c8ebf;fontColor=#6c8ebf;",
           pts=[(X(7) + W + 20, 400), (X(7) + W + 20, 75), (X(0) + W / 2, 75)])
    p.text("<b>Chú thích</b><br>🟨 người · 🟦 agent · 🟩 code tất định/CI · 🔶 gate người<br>"
           "Bug nhỏ: bỏ spec đầy đủ, chỉ cần plan ngắn. Low-risk auto-merge chỉ thử từ tháng 3 (xem trang 4).",
           200, 740, 900, 70)
    return p


# ---------------------------------------------------------------- Trang 2: kiến trúc
def page_arch():
    p = Page("2. Kiến trúc factory", 1800, 1100)
    title(p, "Kiến trúc: code tất định điều phối, agent chỉ làm phần cần phán đoán",
          "\"Agent proposes, code disposes\" — V1 (6/13 video). Cô lập worktree/sandbox — R 5/5 · V 8/13. Model routing — V3 (7/13).")
    # nguồn việc
    p.box("<b>Nguồn việc</b>", 40, 100, 220, 40, BOX + NOTE)
    src = [p.box(t, 40, 150 + i * 75, 220, 60, BOX + HUMAN) for i, t in enumerate([
        "Issue tracker<br>(nhãn agent-ok / risk)", "Spec / plan đã duyệt", "Job định kỳ: bug finder, watchdog, lookback", "Sentry · incident · feedback"])]
    # control plane
    p.box("", 320, 100, 520, 470, "rounded=1;whiteSpace=wrap;html=1;arcSize=3;dashed=1;fillColor=#f3faf1;strokeColor=#82b366;")
    p.text("<b>CONTROL PLANE — code tất định</b> (không tốn token)", 335, 108, 480, 25)
    q = p.box("<b>Hàng đợi task</b><br>trạng thái = label / file", 345, 145, 220, 70, BOX + CODE)
    cls = p.box("<b>Phân loại</b><br>độ khó + rủi ro (DB/infra/auth = cao)", 595, 145, 220, 70, BOX + CODE)
    router = p.box("<b>Model router</b><br>plan/review: model mạnh<br>scan/worker: model rẻ", 345, 255, 220, 80, BOX + CODE)
    disp = p.box("<b>Dispatcher</b><br>WIP limit · ngân sách token · retry", 595, 255, 220, 80, BOX + CODE)
    tele = p.box("<b>Telemetry</b><br>log mọi lần chạy: token · thời gian · pass rate · cost/PR · DORA", 345, 365, 220, 80, BOX + CODE)
    gates = p.box("<b>Gates + CI</b><br>lint · type · test · SAST · secret · khoá test · branch protection · max vòng lặp", 595, 365, 220, 90, BOX + CODE)
    rel = p.box("<b>Rollout</b><br>flag / canary / rollback", 345, 475, 220, 70, BOX + CODE)
    # data plane
    p.box("", 900, 100, 560, 470, "rounded=1;whiteSpace=wrap;html=1;arcSize=3;dashed=1;fillColor=#f2f6fc;strokeColor=#6c8ebf;")
    p.text("<b>DATA PLANE — agent trong sandbox</b>", 915, 108, 480, 25)
    ws = []
    for i in range(3):
        y = 145 + i * 105
        p.box("", 920, y, 320, 90, "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#6c8ebf;dashed=1;")
        p.text(f"<span style='font-size:10px'>sandbox {i+1} · worktree + container · egress allowlist</span>", 925, y + 2, 310, 20)
        ws.append(p.box(f"<b>Coder agent</b> (task {i+1})<br>plan → code → test", 935, y + 30, 290, 50, BOX + AI))
    tst = p.box("<b>Test designer</b><br>viết test chấp nhận trước; coder không sửa được", 1270, 145, 175, 90, BOX + PURPLE)
    rev = p.box("<b>Reviewer agent</b><br>model khác hãng<br>context sạch<br>đối chiếu spec<br>gắn nhãn rủi ro", 1270, 255, 175, 125, BOX + PURPLE)
    p.box("<b>Không</b> chia vai PM/Architect/Dev kiểu bầy agent — 1 coder mạnh / task", 920, 480, 320, 50, BOX + RISK)
    # repo & human
    p.box("<b>Git repo = nguồn sự thật</b>: AGENTS.md ngắn (mục lục) · specs/ · tasks · eval nội bộ 20–50 case", 900, 620, 560, 60, BOX + NOTE)
    hum = p.box("<b>Con người</b><br>Gate 1: duyệt plan<br>Gate 2: review PR<br>Retro tuần", 1580, 252, 200, 130, BOX + HUMAN)
    prod = p.box("<b>Production</b>", 345, 620, 220, 60, BOX + RISK)
    # edges: nguồn → bus x=295 → hàng đợi
    for i, s_ in enumerate(src):
        p.edge(s_, q, "", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;", pts=[(295, 180 + i * 75), (295, 180)])
    p.edge(q, cls, "")
    p.edge(cls, disp, "")
    p.edge(router, disp, "")
    p.edge(disp, ws[1], "giao task", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;")
    p.edge(tst, ws[0], "khoá", "dashed=1;exitX=0;exitY=0.5;entryX=1;entryY=0.5;")
    p.edge(ws[2], gates, "PR (mỗi task)", "strokeColor=#82b366;exitX=0;exitY=0.5;entryX=1;entryY=0.5;")
    p.edge(gates, rev, "pass → PR", "strokeColor=#9673a6;exitX=0.5;exitY=1;entryX=0.5;entryY=1;", pts=[(705, 590), (1357, 590)])
    p.edge(rev, hum, "PR + bằng chứng", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;")
    p.edge(hum, rel, "approve → merge", "exitX=0.5;exitY=1;entryX=1;entryY=0.5;", pts=[(1680, 760), (590, 760), (590, 510)])
    p.edge(rel, prod, "")
    p.edge(prod, src[3], "lỗi → ticket", "dashed=1;exitX=0;exitY=0.5;entryX=0.5;entryY=1;", pts=[(150, 650)])
    p.text("<b>Ranh giới bảo mật</b> (R 5/5): không session nào có đủ <i>lethal trifecta</i> — dữ liệu riêng + input không tin cậy + kênh ra ngoài. "
           "Dependency mới phải có người duyệt (slopsquatting 19,7%). Không chạy --yolo ngoài sandbox.", 40, 790, 820, 70)
    p.text("<b>Chi phí</b>: multi-agent ~15× token → chỉ bật cho task chia được, có ngân sách theo team. "
           "Kiểm chứng tốn ~40% thời gian một mission (v04) — dồn ngân sách vào kiểm chứng, không vào số worker.", 900, 790, 820, 70)
    return p


# ---------------------------------------------------------------- Trang 3: lộ trình
def page_roadmap():
    p = Page("3. Lộ trình 3 tháng", 1800, 680)
    title(p, "Lộ trình 3 tháng cho team 3–10 kỹ sư", "Mỗi giai đoạn chỉ sang bước tiếp khi đạt tiêu chí thoát. Ngưỡng % là suy luận — hiệu chỉnh theo baseline của team.")
    cols = [
        ("Tháng 1 — Nền móng “agent-ready”", "Một agent làm tốt trên repo; đo được",
         ["AGENTS.md ngắn (lệnh build/test, quy ước, gotcha)", "devcontainer / init.sh tái lập được", "CI nhanh (&lt;10 phút) + check test integrity",
          "Sandbox + network allowlist", "Mỗi dev: 1 agent tương tác, plan→implement→verify", "<b>Baseline DORA + thời gian review</b>", "Eval nội bộ 20–50 case từ PR đã đóng"],
         "CI tin cậy · có baseline · CI chặn sửa test & dependency lạ", CODE),
        ("Tháng 2 — Có cấu trúc + async", "Spec, verify, việc vặt chạy nền",
         ["Chạy đủ 8 bước cho 1–2 feature thật", "Reviewer agent model khác trong CI", "Nhãn <i>agent-ok</i>: bug có repro, bump dependency, test, docs → background agent",
          "Policy kích thước PR", "WIP ≤ 2–3 agent ghi / dev", "Người duyệt <b>100%</b> PR"],
         "≥ ~50% PR agent merge với ít chỉnh sửa · review time tăng ≤ 25–30%", AI),
        ("Tháng 3 — Song song có kiểm soát", "Factory nhỏ, dùng chung cả team",
         ["Dây chuyền bằng code tất định (queue, gate, retry)", "Orchestrator–worker cho feature chia được module", "Model routing theo pha · best-of-N chỉ khi có oracle",
          "Ephemeral devbox không secrets prod", "Sentry/incident → ticket · telemetry · dashboard cost/PR", "Thử auto-merge <b>danh mục hẹp</b> nếu CFR ổn định"],
         "CFR không tăng · cost/PR trong ngân sách · 0 sự cố bảo mật · quyết định bằng dữ liệu", PURPLE),
    ]
    prev = None
    for i, (h, goal, items, exitc, col) in enumerate(cols):
        x = 40 + i * 580
        hd = p.box(f"<b style='font-size:15px'>{h}</b><br><i>{goal}</i>", x, 100, 520, 70, BOX + col)
        p.box("<div style='text-align:left'>" + "<br>".join("• " + t for t in items) + "</div>", x, 185, 520, 165, BOX + "fillColor=#ffffff;strokeColor=#999999;align=left;verticalAlign=top;fontSize=13;")
        ex = p.box(f"<b>Tiêu chí thoát</b><br>{exitc}", x, 365, 520, 70, BOX + GATE)
        if prev:
            p.edge(prev, hd, "đạt", pts=[(x - 30, 400), (x - 30, 135)])
        prev = ex
    p.box("<b>Rủi ro phải chặn từ ngày đầu</b><br>"
          "① Reward hacking test → test viết trước + khoá bằng CI &nbsp; ② Review fatigue → WIP limit, PR nhỏ, AI lọc trước &nbsp; "
          "③ Prompt injection / rò secrets → sandbox, tránh lethal trifecta &nbsp; ④ Slopsquatting → chặn dependency mới &nbsp; "
          "⑤ Nợ kỹ thuật → linter trùng lặp + dọn định kỳ &nbsp; ⑥ Ảo tưởng năng suất → quyết định theo telemetry",
          40, 465, 1680, 80, BOX + RISK)
    p.box("<b>Công cụ tối thiểu</b>: 1 coding agent CLI (hook, subagent, worktree) · 1 model khác hãng để review · 1 async agent gắn tracker · "
          "Git có branch protection + merge queue · SAST + secret scan + dependency allowlist · devcontainer/Docker · dashboard DORA/review/cost. "
          "<b>Chưa cần</b> framework multi-agent nặng.", 40, 565, 1680, 60, BOX + NOTE)
    return p


# ---------------------------------------------------------------- Trang 4: đồng thuận
def page_consensus():
    p = Page("4. Bản đồ đồng thuận", 1800, 1000)
    title(p, "Research (5 báo cáo) × Video (13 video): chỗ nào đồng thuận, chỗ nào chỉ một bên nói, chỗ nào căng",
          "R = số báo cáo research ủng hộ /5 · V = số video ủng hộ /13 (điểm có trích dẫn transcript). Người chấm phụ agy: κ = 0,43, chấm dễ hơn.")
    p.box("", 40, 110, 780, 560, "ellipse;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;opacity=45;")
    p.box("", 440, 110, 780, 560, "ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;opacity=45;")
    p.text("<b style='font-size:16px'>Chỉ research nói</b><br><span style='color:#b85450'>(điểm mù của video)</span><br><br>"
           "• Reward hacking → khoá test (R5 · V2)<br>• Slopsquatting / supply chain (R5 · V1)<br>• Prompt injection, lethal trifecta (R5 · V4◐)<br>"
           "• Ảo tưởng năng suất, METR −19% (R4 · V0)<br>• Benchmark công khai nhiễm (R5 · V2)<br>• AI khuếch đại team (DORA) (R4 · V1)<br>"
           "• Chia task theo ranh giới file (R4 · V2)<br>• WIP limit 2–5 agent/người (R5 · V2, ✗ v06 v10)",
           85, 230, 345, 330, "fontSize=13;")
    p.text("<b style='font-size:16px'>Lõi đồng thuận</b><br><br>"
           "• Harness kiểm chứng quyết định chất lượng <b>R5 · V12</b><br>• Pipeline có cấu trúc <b>R5 · V11</b><br>"
           "• Gate người: plan + PR <b>R5 · V11</b><br>• 1 agent mạnh viết code <b>R4 · V10</b><br>• Context engineering <b>R5 · V9</b><br>"
           "• Reviewer độc lập / model khác <b>R5 · V9</b><br>• Worktree / sandbox <b>R5 · V8</b>",
           465, 255, 340, 330, "fontSize=13;")
    p.text("<b style='font-size:16px'>Chỉ video nói</b><br><span style='color:#2d7600'>(tầng vận hành factory)</span><br><br>"
           "• Model routing theo pha (V3 · 7 video)<br>• Code tất định điều phối (V1 · 6)<br>• Khép vòng production → ticket (V4 · 5)<br>"
           "• Kiểm chứng E2E thật, ~40% (V7 · 5)<br>• Định tuyến theo rủi ro (V2 · 4)<br>• Vệ sinh context, nạp tool dần (V11 · 4)<br>"
           "• Bot-review có giới hạn vòng (V6 · 3)<br>• Tự xây skill nhỏ, không framework (V20 · 3)",
           840, 230, 350, 330, "fontSize=13;")
    p.text("<b style='font-size:15px;color:#6c8ebf'>RESEARCH · 5 báo cáo</b>", 150, 140, 250, 30)
    p.text("<b style='font-size:15px;color:#2d7600'>VIDEO · 13 practitioner</b>", 880, 140, 260, 30)
    p.box("<b style='font-size:15px'>3 điểm căng — team cần quyết</b>", 1360, 110, 400, 45, BOX + GATE)
    tens = [("Auto-merge PR rủi ro thấp?", "Research: người duyệt 100% (Stripe)<br>Video: 4/13 cho auto-merge",
             "→ Tháng 1–2 duyệt 100%; tháng 3 thử danh mục hẹp; DB/infra/auth luôn cần người"),
            ("Song song bao nhiêu?", "Research: 2–5 agent/người<br>Video: 15–20 task (v06, v10, không số đo)", "→ Giữ WIP limit"),
            ("Máy dev hay sandbox?", "Research: sandbox cô lập<br>Video v03: cần env thật trên laptop",
             "→ Env tái lập được; nếu chạy máy thật: cấm egress tự do, không secrets prod")]
    for i, (q, a, d) in enumerate(tens):
        p.box(f"<b>{q}</b><br><span style='font-size:11px'>{a}</span><br><b style='color:#2d7600'>{d}</b>", 1360, 170 + i * 160, 400, 145, BOX + "fillColor=#ffffff;strokeColor=#d79b00;")
    p.box("<b>Độ tin cậy nguồn</b> — Research: paper, DORA, METR, blog kỹ thuật (URL đã kiểm tra; gpt-oss bị loại vì 10/17 link 404). "
          "Video: 3 video đạt 3/5 (Builder.io, Factory, HumanLayer), còn lại tutorial/demo; <b>không video nào có số đo có phương pháp</b>. "
          "Khi hai bên khác nhau về rủi ro/số liệu → ưu tiên research; video có giá trị nhất ở pattern vận hành.",
          60, 700, 1700, 80, BOX + NOTE)
    return p


pages = [page_process(), page_arch(), page_roadmap(), page_consensus()]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "software-factory.drawio")
with open(out, "w", encoding="utf-8") as f:
    f.write('<mxfile host="build_drawio.py">' + "".join(pg.xml(i) for i, pg in enumerate(pages)) + "</mxfile>")
print(out)

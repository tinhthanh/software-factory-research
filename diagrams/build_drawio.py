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
          "Đồng thuận: research R 5/5 · video V 11/13 (checkpoint người), V 12/13 (harness kiểm chứng). Mũi tên đứt = vòng lặp sửa lỗi. "
          "<b style='color:#9673a6'>Cập nhật round 2 (18/10/2026)</b>: WIP theo hàng đợi review, verifier trước PR, làn auto-approve.")
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
    b3 = p.box("<b>3. Breakdown</b><br>task ≤ 1 PR (~30' review), không chồng file, <b>claim</b> file/module<br>+ <b>test chấp nhận viết trước</b>", X(2), 345, W, H, BOX + AI)
    b3c = p.box("<b>Khoá test</b><br>hook/CI chặn sửa test, CI config, lockfile", X(2), 555, W, H, BOX + CODE)
    b4 = p.box("<b>4. Implement</b><br>1 agent · 1 worktree · 1 sandbox<br>agent nền: devbox/cloud · local: sandbox OS<br>verifier chạy <b>trước khi mở PR</b>", X(3), 345, W, H, BOX + AI)
    n4 = p.box("WIP: ≤ 3–5 <b>PR agent chờ review</b> / người<br><span style='font-size:10px'>(R2: không giới hạn theo số agent)</span>", X(3), 140, W, 70, BOX + NOTE)
    b5 = p.box("<b>5. Gate tự động</b><br>lint · type · test · SAST · secret · chặn dependency mới · LLM judge chặn vượt phạm vi", X(4), 555, W, H, BOX + CODE)
    b6 = p.box("<b>6. AI review</b><br>context sạch, <b>model khác</b>, đối chiếu spec, gắn nhãn rủi ro · <b>không approve</b>", X(5), 345, W, H, BOX + AI)
    b7a = p.box("<b>Làn auto-approve</b><br>checklist tất định: &lt;1.000 dòng, không auth/infra/migration/xoá code → người chỉ bấm merge", X(6), 555, W, H, BOX + CODE)
    g2 = p.box("<b>Gate 2</b><br>Người review + approve<br><span style='font-size:10px'>không phải người giao task</span>", X(6) - 5, 115, W + 10, 150, "rhombus;whiteSpace=wrap;html=1;fontSize=11;" + GATE)
    b8 = p.box("<b>8. Deploy</b><br>feature flag / canary<br>(rollout bằng code)", X(7), 555, W, H, BOX + CODE)
    b8a = p.box("Theo dõi metric/log khi rollout<br>Sentry / incident → <b>ticket mới</b>", X(7), 345, W, H, BOX + AI)
    b8h = p.box("<b>Retro tuần</b><br>lỗi lặp ≥2 lần → rule / hook / eval case · eval lại khi nâng version agent", X(7), 135, W, H, BOX + HUMAN)

    dashed = "dashed=1;strokeColor=#b85450;fontColor=#b85450;"
    p.edge(b1, b1a, "")
    p.edge(b1a, b2, "")
    p.edge(b2, g1, "")
    p.edge(g1, b3, "duyệt", pts=[(X(2) + W / 2, 190)])
    p.edge(g1, b2, "sửa plan", dashed, pts=[(X(1) + W + 15, 190), (X(1) + W + 15, 400)])
    p.edge(b3, b3c, "")
    p.edge(b3, b4, "")
    p.edge(b4, b5, "", pts=[(X(3) + W / 2, 610)])
    p.edge(b5, b4, "fail (≤2 vòng CI)", dashed, pts=[(X(4) + W / 2, 470), (X(3) + W, 470)])
    p.edge(b5, b6, "pass", pts=[(X(5) + W / 2, 610)])
    p.edge(b6, b4, "comment → sửa (vòng có giới hạn)", dashed, pts=[(X(5) + W / 2, 320), (X(3) + W / 2, 320)])
    p.edge(b6, g2, "bot hài lòng", "exitX=1;exitY=0.5;entryX=0;entryY=0.5;", pts=[(X(6) - 25, 400), (X(6) - 25, 190)])
    p.edge(g2, b8, "merge", "entryX=0;entryY=0.2;", pts=[(X(6) + W / 2, 290), (X(7) - 15, 290), (X(7) - 15, 577)])
    p.edge(b6, b7a, "rủi ro thấp", "dashed=1;strokeColor=#82b366;fontColor=#2d7600;", pts=[(X(5) + W - 30, 520), (X(6) + W / 2, 520)])
    p.edge(b7a, b8, "", "exitX=1;exitY=0.75;entryX=0;entryY=0.75;")
    p.edge(b8, b8a, "")
    p.edge(b8a, b8h, "")
    p.edge(b8a, b1, "ticket mới (khép vòng production)", "dashed=1;strokeColor=#6c8ebf;fontColor=#6c8ebf;",
           pts=[(X(7) + W + 20, 400), (X(7) + W + 20, 75), (X(0) + W / 2, 75)])
    p.text("<b>Chú thích</b><br>🟨 người · 🟦 agent · 🟩 code tất định/CI · 🔶 gate người<br>"
           "Bug nhỏ: bỏ spec đầy đủ, chỉ cần plan ngắn. Làn auto-approve từ tháng 2 (người vẫn bấm merge); "
           "auto-merge thật chỉ cho dependency patch/minor từ tháng 3, có kill-switch theo tỷ lệ revert (xem trang 3, 5).",
           200, 740, 1100, 70)
    return p


# ---------------------------------------------------------------- Trang 2: kiến trúc
def page_arch():
    p = Page("2. Kiến trúc factory", 1800, 1100)
    title(p, "Kiến trúc: code tất định điều phối, agent chỉ làm phần cần phán đoán",
          "\"Agent proposes, code disposes\" — V1 (6/13 video). Cô lập worktree/sandbox — R 5/5 · V 8/13. Model routing — V3 (7/13). <b style='color:#9673a6'>R2</b>: devbox không credential prod, WIP theo review, trần chi phí.")
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
    disp = p.box("<b>Dispatcher</b><br>WIP theo hàng đợi review · trần chi phí / người / công cụ · ≤2 vòng CI", 595, 255, 220, 80, BOX + CODE)
    tele = p.box("<b>Telemetry</b><br>token/PR merged · chờ review · PR không review · revert 30 ngày · DORA", 345, 365, 220, 80, BOX + CODE)
    gates = p.box("<b>Gates + CI</b><br>lint · type · test · SAST · secret · khoá test · LLM judge phạm vi · branch protection", 595, 365, 220, 90, BOX + CODE)
    rel = p.box("<b>Rollout</b><br>flag / canary / rollback", 345, 475, 220, 70, BOX + CODE)
    # data plane
    p.box("", 900, 100, 560, 470, "rounded=1;whiteSpace=wrap;html=1;arcSize=3;dashed=1;fillColor=#f2f6fc;strokeColor=#6c8ebf;")
    p.text("<b>DATA PLANE — agent trong sandbox</b>", 915, 108, 480, 25)
    ws = []
    for i in range(3):
        y = 145 + i * 105
        p.box("", 920, y, 320, 90, "rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#6c8ebf;dashed=1;")
        p.text(f"<span style='font-size:10px'>devbox {i+1} · egress allowlist · không credential prod · push qua proxy</span>", 925, y + 2, 310, 20)
        ws.append(p.box(f"<b>Coder agent</b> (task {i+1})<br>plan → code → verifier → PR", 935, y + 30, 290, 50, BOX + AI))
    tst = p.box("<b>Test designer</b><br>viết test chấp nhận trước; coder không sửa được", 1270, 145, 175, 90, BOX + PURPLE)
    rev = p.box("<b>Reviewer agent</b><br>model khác hãng<br>context sạch<br>đối chiếu spec<br>gắn nhãn rủi ro", 1270, 255, 175, 125, BOX + PURPLE)
    p.box("<b>Không</b> chia vai PM/Architect/Dev kiểu bầy agent — 1 coder mạnh / task", 920, 480, 320, 50, BOX + RISK)
    # repo & human
    p.box("<b>Git repo = nguồn sự thật</b>: AGENTS.md viết tay, ngắn (không /init, không tổng quan repo) · specs/ · tasks · eval nội bộ 20–50 case", 900, 620, 560, 60, BOX + NOTE)
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
           "Dependency mới phải có người duyệt (slopsquatting 19,7%). Không chạy --yolo ngoài sandbox.<br>"
           "<b>R2</b>: agent đọc input không tin cậy (issue/PR/Sentry) → không shell, ghi qua safe outputs; không pull_request_target; "
           "publish bằng OIDC; pin MCP/skill (Clinejection, Agentjacking, PocketOS).", 40, 790, 820, 110)
    p.text("<b>Chi phí</b>: multi-agent ~15× token (agent teams ~7×) → chỉ bật cho task chia được. "
           "Kiểm chứng tốn ~40% thời gian một mission (v04) — dồn ngân sách vào kiểm chứng, không vào số worker.<br>"
           "<b>R2</b>: Uber tiêu hết ngân sách AI năm trong 4 tháng → trần $/người/công cụ từ ngày đầu, đo token/PR merged.", 900, 790, 820, 110)
    return p


# ---------------------------------------------------------------- Trang 3: lộ trình
def page_roadmap():
    p = Page("3. Lộ trình 3 tháng", 1800, 800)
    title(p, "Lộ trình 3 tháng cho team 3–10 kỹ sư (cập nhật round 2)",
          "Mỗi giai đoạn chỉ sang bước tiếp khi đạt tiêu chí thoát. Ngưỡng % là suy luận — hiệu chỉnh theo baseline của team. "
          "<b style='color:#9673a6'>R2</b> = thêm/sửa ở round 2.")
    R2 = "<b style='color:#9673a6'>R2</b> "
    cols = [
        ("Tháng 1 — Nền móng “agent-ready”", "Một agent làm tốt trên repo; đo được",
         [R2 + "AGENTS.md viết tay ≤ ~150–200 dòng, không /init, không tổng quan repo", "devcontainer / init.sh tái lập được", "CI nhanh (&lt;10 phút) + check test integrity",
          "Sandbox OS + network allowlist", R2 + "Agent trong CI: read-only + safe outputs, không pull_request_target", R2 + "<b>Trần chi phí / người / công cụ</b> qua gateway",
          "<b>Baseline DORA + thời gian review</b> · eval nội bộ 20–50 case", R2 + "Junior: chế độ “hỏi để hiểu”, không giao hết"],
         "CI tin cậy · có baseline · CI chặn sửa test & dependency lạ", CODE),
        ("Tháng 2 — Có cấu trúc + async", "Spec, verify, việc vặt chạy nền",
         ["Chạy đủ 8 bước cho 1–2 feature thật", "Reviewer agent model khác trong CI (không approve)", "Nhãn <i>agent-ok</i>: bug có repro, bump dependency, test, docs → background agent",
          "Policy kích thước PR", R2 + "WIP ≤ 3–5 <b>PR agent chờ review</b> / người (không đếm agent)",
          R2 + "<b>Làn auto-approve</b> theo checklist tất định, người vẫn bấm merge; đo lead time + revert trước/sau 4 tuần"],
         "≥ ~50% PR agent merge với ít chỉnh sửa · review time tăng ≤ 25–30% · " + R2 + "PR agent bị bỏ &lt; ~1/3", AI),
        ("Tháng 3 — Song song có kiểm soát", "Factory nhỏ, dùng chung cả team",
         ["Dây chuyền bằng code tất định (queue, gate, retry)", "Orchestrator–worker cho feature chia được module + kênh claim", "Model routing theo pha · best-of-N chỉ khi có oracle",
          R2 + "Agent nền trên devbox/cloud, env verify giống thật, không chạm prod",
          R2 + "Dashboard: chờ review · PR không review · token/PR merged · revert 30 ngày · deploy/tuần",
          R2 + "Auto-merge <b>dependency patch/minor</b>: coverage vùng chạm, chờ bản phát hành mới, kill-switch theo revert"],
         "CFR không tăng · chi phí trong trần · 0 sự cố bảo mật · quyết định bằng dữ liệu", PURPLE),
    ]
    prev = None
    for i, (h, goal, items, exitc, col) in enumerate(cols):
        x = 40 + i * 580
        hd = p.box(f"<b style='font-size:15px'>{h}</b><br><i>{goal}</i>", x, 100, 520, 70, BOX + col)
        p.box("<div style='text-align:left'>" + "<br>".join("• " + t for t in items) + "</div>", x, 185, 520, 230, BOX + "fillColor=#ffffff;strokeColor=#999999;align=left;verticalAlign=top;fontSize=13;")
        ex = p.box(f"<b>Tiêu chí thoát</b><br>{exitc}", x, 430, 520, 70, BOX + GATE)
        if prev:
            p.edge(prev, hd, "đạt", pts=[(x - 30, 465), (x - 30, 135)])
        prev = ex
    p.box("<b>Rủi ro phải chặn từ ngày đầu</b><br>"
          "① Reward hacking test → test viết trước + khoá bằng CI &nbsp; ② Review fatigue → WIP theo hàng đợi review, PR nhỏ, AI lọc trước &nbsp; "
          "③ Prompt injection / rò secrets → sandbox, tránh lethal trifecta &nbsp; ④ Slopsquatting → chặn dependency mới &nbsp; "
          "⑤ Nợ kỹ thuật → linter trùng lặp + dọn định kỳ &nbsp; ⑥ Ảo tưởng năng suất → quyết định theo telemetry &nbsp; "
          + R2 + "⑦ Agent CI + input không tin cậy → không shell, OIDC &nbsp; " + R2 + "⑧ Chi phí vượt trần (Uber) → trần theo người/công cụ",
          40, 530, 1680, 95, BOX + RISK)
    p.box("<b>Công cụ tối thiểu</b>: 1 coding agent CLI (hook, subagent, worktree, sandbox) · 1 model khác hãng để review · 1 async agent gắn tracker · "
          "Git có branch protection + merge queue · SAST + secret scan + dependency allowlist · devcontainer/Docker · " + R2 + "gateway quy chi phí · dashboard DORA/review/cost. "
          "<b>Chưa cần</b> framework multi-agent nặng.", 40, 645, 1680, 60, BOX + NOTE)
    p.text("<b>Tín hiệu dừng mở rộng</b> (R2): hàng đợi review tăng nhanh hơn PR merged · PR agent bị bỏ/làm lại &gt; ~1/3 · deploy/tuần không tăng dù PR tăng · "
           "tỷ lệ xanh nhánh main giảm · cần &gt; 2 vòng CI mới xanh.", 40, 720, 1680, 50)
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
             "→ Tháng 1–2 duyệt 100%; tháng 3 thử danh mục hẹp; DB/infra/auth luôn cần người",
             "R2 (7/7): auto-approve checklist tất định (Ona), auto-merge chỉ dep patch/minor; chưa có dữ liệu incident"),
            ("Song song bao nhiêu?", "Research: 2–5 agent/người<br>Video: 15–20 task (v06, v10, không số đo)", "→ Giữ WIP limit",
             "R2 (7/7): không có dữ liệu cho con số nào → WIP theo PR chờ review; xung đột 27–42% cặp PR"),
            ("Máy dev hay sandbox?", "Research: sandbox cô lập<br>Video v03: cần env thật trên laptop",
             "→ Env tái lập được; nếu chạy máy thật: cấm egress tự do, không secrets prod",
             "R2 (7/7): local OK nếu sandbox OS; agent nền trên devbox/cloud giống thật; “cấm hẳn local” bị bác")]
    for i, (q, a, d, r2) in enumerate(tens):
        p.box(f"<b>{q}</b><br><span style='font-size:11px'>{a}</span><br><b style='color:#2d7600'>{d}</b>"
              f"<br><span style='font-size:11px;color:#9673a6'><b>{r2}</b></span>", 1360, 170 + i * 165, 400, 155, BOX + "fillColor=#ffffff;strokeColor=#d79b00;")
    p.box("<b>Độ tin cậy nguồn</b> — Research: paper, DORA, METR, blog kỹ thuật (URL đã kiểm tra; gpt-oss bị loại vì 10/17 link 404). "
          "Video: 3 video đạt 3/5 (Builder.io, Factory, HumanLayer), còn lại tutorial/demo; <b>không video nào có số đo có phương pháp</b>. "
          "Khi hai bên khác nhau về rủi ro/số liệu → ưu tiên research; video có giá trị nhất ở pattern vận hành.",
          60, 700, 1700, 80, BOX + NOTE)
    return p


# ---------------------------------------------------------------- Trang 5: round 2
def page_round2():
    p = Page("5. Round 2 — đồng thuận & sửa đổi", 1800, 780)
    title(p, "Round 2 (18/10/2026): 7 báo cáo cô lập × 3 người chấm độc lập — cái gì vững, cái gì phải sửa",
          "5 Claude subagent (vendor · học thuật · case study · bảo mật · hoài nghi) + agy Gemini 4 Argon / 3.8 Flash. "
          "Điểm = trung vị 3 người chấm (2 Claude + 1 Gemini, κ = 0,68–0,77), 705/705 trích dẫn đã kiểm. Chi tiết: round2/CONSENSUS.md")
    strong = [("Nút thắt = hàng đợi review (Faros review ~5×, LinearB chờ 17,6h P75)", "7/7"),
              ("Lợi ích cá nhân ≠ lợi ích hệ thống (Faros deploy/tuần −11,7%)", "7/7"),
              ("Auto-merge chỉ danh mục hẹp, quyết bằng luật tất định", "7/7"),
              ("Sandbox egress allowlist, không credential prod", "7/7"),
              ("Verify cần env giống thật, không chạm prod", "7/7"),
              ("AGENTS.md ngắn, viết tay — dài/tự sinh tốn +20%, không tăng độ đúng", "7/7"),
              ("Agent gian lận để CI xanh; repo thiếu test → agent không tự kiểm được", "7/7"),
              ("~44% task sinh code có lỗ hổng (Veracode 2026)", "7/7"),
              ("Agent CI + input không tin cậy đã bị khai thác (Clinejection…)", "7/7"),
              ("Không còn RCT năng suất đáng tin (METR 02/2026 tự nhận vỡ thiết kế)", "6/7")]
    p.box("<b style='font-size:15px'>Đồng thuận rất mạnh</b> (18/36 claim, Σ ≥ 12/14)", 40, 100, 820, 40, BOX + CODE)
    p.box("<div style='text-align:left'>" + "<br>".join(f"• {t} &nbsp;<b>{s}</b>" for t, s in strong) + "</div>",
          40, 150, 820, 290, BOX + "fillColor=#ffffff;strokeColor=#82b366;align=left;verticalAlign=top;fontSize=13;")
    p.box("<b style='font-size:15px'>Bất đồng thật</b> (đều do 2 báo cáo agy)", 900, 100, 860, 40, BOX + GATE)
    dis = [("N18 · “Cấm hẳn agent local” (Σ −1)", "Chỉ Flash đòi cấm; D, G, Argon nói ngược lại", "→ Không cấm, bắt buộc sandbox OS"),
           ("N15 · Ngưỡng số agent/người (Σ 7)", "Argon 3–4 · Flash 2 · D 2–4 · G 2–3; H bác bỏ đặt ngưỡng; 7/7: không có dữ liệu", "→ WIP theo PR chờ review"),
           ("N29 · Đã có cost/PR đáng tin? (Σ 4)", "Argon $30–80 (URL 404) · Flash $0,5–3 (không nguồn); F, G, H: chưa có", "→ Coi mọi cost/PR là chưa kiểm chứng")]
    for i, (q, a, d) in enumerate(dis):
        p.box(f"<b>{q}</b><br><span style='font-size:11px'>{a}</span><br><b style='color:#2d7600'>{d}</b>",
              900, 150 + i * 102, 860, 92, BOX + "fillColor=#ffffff;strokeColor=#d79b00;")
    p.box("<b style='font-size:15px'>Fact-check trên nguồn gốc</b> (18 số liệu: 12 đúng · 5 sai một phần · 1 không kiểm được)", 40, 480, 1720, 40, BOX + RISK)
    fixes = ["Faros review “+441%” → <b>sai nguồn</b>; Faros ghi “5X median review time” (441,5% là bài Medium) — giải đáp câu hỏi treo của round 1",
             "Faros incident/PR +242,7% (04/2026) → <b>đã cũ</b>: dữ liệu 08–09/2026 chỉ +14,5%/PR nhưng incident/tháng +125,4%; Q3 “Speed Trap”: merge không review +76,3%",
             "METR “30–50%” là tỷ lệ <b>dev</b> giữ lại task, không phải tỷ lệ task · ETH: “không cải thiện, +20% chi phí” (−3% chưa thấy trong abstract)",
             "Vercel “58% PR merge không cần người” → bài <b>đã bị gỡ</b> (404); “671 PR, 0 revert” chỉ có nguồn thứ cấp",
             "“DORA −1,5% / −7,2%” là <b>DORA 2024</b> (mỗi 25% tăng adoption) · DORA 2026 <b>chưa phát hành</b> · CooperBench: tính năng độc lập, không “liên đới”"]
    p.box("<div style='text-align:left'>" + "<br>".join("• " + t for t in fixes) + "</div>",
          40, 530, 1720, 115, BOX + "fillColor=#ffffff;strokeColor=#b85450;align=left;verticalAlign=top;fontSize=13;")
    p.box("<b>Độ tin cậy nguồn R2</b>: Claude subagent 94–100% URL mở được; agy-argon 8/66 và agy-flash 5/17 URL 404 (slug “gần đúng”). "
          "Flash dùng nhiều số 2023–2025 như bằng chứng mới. Gần như mọi case study công ty (Stripe, Ramp, Uncountable, Vercel, Ona, Intercom) là <b>tự báo cáo</b>; "
          "chưa ai công bố defect/incident của code agent so với code người.", 40, 670, 1720, 80, BOX + NOTE)
    return p


pages = [page_process(), page_arch(), page_roadmap(), page_consensus(), page_round2()]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "software-factory.drawio")
with open(out, "w", encoding="utf-8") as f:
    f.write('<mxfile host="build_drawio.py">' + "".join(pg.xml(i) for i, pg in enumerate(pages)) + "</mxfile>")
print(out)

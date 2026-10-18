"""In bảng ma trận đồng thuận (Markdown) từ consensus.json."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(f'{D}/consensus.json'))
cols = ['claude-D-vendor', 'claude-E-academic', 'claude-F-casestudy', 'claude-G-security', 'claude-H-skeptic', 'agy-gemini-argon', 'agy-gemini-flash']
hdr = ['D', 'E', 'F', 'G', 'H', 'Argon', 'Flash']
fmt = lambda x: (f'**{int(x)}**' if x < 0 else str(int(x))) if x == int(x) else f'{x:.1f}'
print('| ID | Claim | ' + ' | '.join(hdr) + ' | Σ/14 | Ủng hộ | Ô lệch* |')
print('|' + '---|' * (len(hdr) + 5))
for cid, v in sorted(d['claims'].items(), key=lambda kv: (-kv[1]['sum'], int(kv[0][1:]))):
    s = v['sum']; s = f'**{int(s)}**' if s >= 12 else str(int(s))
    print(f'| {cid} | {v["claim"]} | ' + ' | '.join(fmt(v['cells'][c]['median']) for c in cols) + f' | {s} | {v["support"]}/7 | {len(v["disputed_cells"])} |')

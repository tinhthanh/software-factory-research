"""In bảng ma trận đồng thuận (Markdown) từ consensus.json."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(f'{D}/consensus.json'))
cols = ['claude-T1-handbooks', 'claude-T2-standards', 'claude-T3-ai-agent', 'claude-T4-smallteam', 'agy-gemini-argon', 'agy-gemini-flash']
hdr = ['T1', 'T2', 'T3', 'T4', 'Argon', 'Flash']
fmt = lambda x: (f'**{int(x)}**' if x < 0 else str(int(x))) if x == int(x) else f'{x:.1f}'
print('| ID | Claim | ' + ' | '.join(hdr) + ' | Σ/12 | Ủng hộ | Mức |')
print('|' + '---|' * (len(hdr) + 5))
for cid, v in d['claims'].items():
    s = v['sum']; tier = 'A' if v['sum'] >= 10 and v['contradict'] == 0 else ('B' if v['sum'] >= 7 else 'C')
    s = f'**{int(s)}**' if s >= 12 else str(int(s))
    print(f'| {cid} | {v["doc"]}: {v["claim"]} | ' + ' | '.join(fmt(v['cells'][c]['median']) for c in cols) + f' | {s} | {v["support"]}/6 | {tier} |')

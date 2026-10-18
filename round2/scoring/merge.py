"""Gộp điểm các rater-*.json: kiểm tra trích dẫn, đo đồng thuận giữa người chấm, lấy trung vị → consensus.json."""
import json, glob, os, re, statistics, itertools, collections
D = os.path.dirname(os.path.abspath(__file__))
claims = json.load(open(f'{D}/claims.json'))
reports = sorted(os.path.basename(p)[:-3] for p in glob.glob(f'{D}/../raw/*.md'))
norm = lambda s: re.sub(r'\s+', ' ', s.replace('*', '').replace('`', '')).strip().lower()
text = {r: norm(open(f'{D}/../raw/{r}.md').read()) for r in reports}
raters = {json.load(open(p))['rater']: json.load(open(p))['scores'] for p in sorted(glob.glob(f'{D}/rater-*.json'))}
qc = collections.Counter(); bad = []
for rn, sc in raters.items():
    for c in claims:
        for r in reports:
            s, q = sc[c['id']][r]
            if s != 0:
                ok = bool(q) and norm(q) in text[r]
                qc[(rn, ok)] += 1
                if not ok: bad.append((rn, c['id'], r, q[:80]))
cat = lambda s: 'S' if s > 0 else ('C' if s < 0 else 'N')   # support / contradict / none
def kappa(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = collections.Counter(a), collections.Counter(b)
    pe = sum(ca[k] * cb[k] for k in ca) / n / n
    return (po - pe) / (1 - pe) if pe < 1 else 1.0, po
names = list(raters)
vec = {rn: [raters[rn][c['id']][r][0] for c in claims for r in reports] for rn in names}
pair = {f'{a}~{b}': dict(zip(('kappa_3cat', 'agree_3cat'), kappa([cat(x) for x in vec[a]], [cat(x) for x in vec[b]])),
                         exact=sum(x == y for x, y in zip(vec[a], vec[b])) / len(vec[a]))
        for a, b in itertools.combinations(names, 2)}
cons = {}
for c in claims:
    row = {}
    for r in reports:
        ss = [raters[rn][c['id']][r][0] for rn in names]
        row[r] = {'median': statistics.median(ss), 'scores': dict(zip(names, ss)),
                  'quote': next((raters[rn][c['id']][r][1] for rn in names if raters[rn][c['id']][r][0] != 0), '')}
    tot = sum(v['median'] for v in row.values())
    cons[c['id']] = {'claim': c['claim'], 'sum': tot, 'support': sum(v['median'] > 0 for v in row.values()),
                     'contradict': sum(v['median'] < 0 for v in row.values()),
                     'disputed_cells': [r for r, v in row.items() if len({cat(x) for x in v['scores'].values()}) > 1], 'cells': row}
json.dump({'raters': names, 'pairwise': pair, 'quote_check': {f'{k[0]}:{"ok" if k[1] else "bad"}': v for k, v in qc.items()},
           'bad_quotes': bad, 'claims': cons}, open(f'{D}/consensus.json', 'w'), ensure_ascii=False, indent=1)
print('quotes', dict(qc)); [print('  BAD', b) for b in bad[:15]]
for k, v in pair.items(): print(k, {x: round(y, 3) for x, y in v.items()})
short = [r.split('-')[-1][:5] for r in reports]
print(f'{"id":4} {"Σ":>5} sup con  ' + ' '.join(f'{s:>5}' for s in short) + '  disputed')
for cid, v in sorted(cons.items(), key=lambda kv: -kv[1]['sum']):
    print(f'{cid:4} {v["sum"]:5.1f} {v["support"]:3} {v["contradict"]:3}  ' + ' '.join(f'{v["cells"][r]["median"]:5.1f}' for r in reports) + f'  {len(v["disputed_cells"])}')
# Thiên vị tự chấm: rater-agy (Gemini) chấm báo cáo agy (Gemini) so với trung bình 2 rater Claude trên cùng ô
if 'rater-agy' in raters:
    for grp in (['agy-gemini-argon', 'agy-gemini-flash'], [r for r in reports if r.startswith('claude')]):
        g = [raters['rater-agy'][c['id']][r][0] for c in claims for r in grp]
        cl = [statistics.mean(raters[n][c['id']][r][0] for n in names if n != 'rater-agy') for c in claims for r in grp]
        print('self-bias', 'agy-reports' if grp[0].startswith('agy') else 'claude-reports', 'agy-rater mean', round(statistics.mean(g), 3), 'claude-raters mean', round(statistics.mean(cl), 3))

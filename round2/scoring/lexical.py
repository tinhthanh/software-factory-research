"""TF-IDF cosine (idf làm mịn như sklearn: ln((1+N)/(1+df))+1) (unigram+bigram âm tiết, bỏ phần Nguồn) + Jaccard domain nguồn giữa các báo cáo round 2."""
import re, math, json, glob, os, collections, itertools
from urllib.parse import urlparse
R = sorted(glob.glob(os.path.join(os.path.dirname(__file__), '..', 'raw', '*.md')))
names = [os.path.basename(p)[:-3] for p in R]
docs, doms = [], []
for p in R:
    t = open(p).read()
    doms.append({urlparse(u).netloc.removeprefix('www.') for u in re.findall(r'https?://[^\s)>\]`"*]+', t)})
    body = re.split(r'\n## Nguồn', t)[0]
    body = re.sub(r'https?://\S+', ' ', body).lower()
    toks = re.findall(r'\w+', body)
    docs.append(collections.Counter(toks + [a + '_' + b for a, b in zip(toks, toks[1:])]))
df = collections.Counter(k for d in docs for k in d)
N = len(docs)
vec = [{k: (1 + math.log(v)) * (math.log((1 + N) / (1 + df[k])) + 1) for k, v in d.items()} for d in docs]
def cos(a, b):
    s = sum(a[k] * b.get(k, 0) for k in a)
    return s / math.sqrt(sum(x * x for x in a.values()) * sum(x * x for x in b.values()))
out = {'names': names, 'cosine': [[round(cos(a, b), 3) for b in vec] for a in vec],
       'jaccard_domains': [[round(len(a & b) / len(a | b), 2) if a | b else 0 for b in doms] for a in doms]}
json.dump(out, open(os.path.join(os.path.dirname(__file__), 'lexical.json'), 'w'), indent=1)
short = [n.split("-")[-1][:6] for n in names]
for key in ('cosine', 'jaccard_domains'):
    print(key); print('      ' + ' '.join(f'{s:>6}' for s in short))
    for s, row in zip(short, out[key]): print(f'{s:>6}' + ' '.join(f'{x:6.2f}' for x in row))

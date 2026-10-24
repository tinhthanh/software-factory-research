import json,collections
a=json.load(open('scoring/video-consensus-a.json'));b=json.load(open('scoring/video-consensus-b.json'));c3=json.load(open('scoring/video-consensus-c.json'));d4=json.load(open('scoring/video-consensus-d.json'))
g=json.load(open('scoring/video-agy-scores.json'))
cl={x['id']:x['claim'] for x in json.load(open('scoring/claims.json'))}
rs=json.load(open('scoring/consensus.json'))['scores']
V=[f'v{i:02d}' for i in range(1,15)]
meta={**a['video_meta'],**b['video_meta'],**c3['video_meta'],**d4['video_meta']}
C={k:{**a['scores'][k],**b['scores'][k],**c3['scores'][k],**d4['scores'][k]} for k in cl}
def sc(x): return x['score'] if isinstance(x,dict) else x
bk=lambda s: 1 if s>=1 else (-1 if s<0 else 0)
# inter-rater
pairs=[(sc(C[k][v]),g[k][v]) for k in cl for v in V]
exact=sum(x==y for x,y in pairs)/len(pairs); buck=sum(bk(x)==bk(y) for x,y in pairs)/len(pairs)
# cohen kappa on buckets
n=len(pairs); cats=[-1,0,1]; po=buck
pe=sum((sum(bk(x)==c for x,_ in pairs)/n)*(sum(bk(y)==c for _,y in pairs)/n) for c in cats)
kappa=(po-pe)/(1-pe)
mae=sum(abs(x-y) for x,y in pairs)/n
print(f"Claude vs agy: exact {exact:.2f}, bucket {buck:.2f}, kappa {kappa:.2f}, MAE {mae:.2f}, mean Claude {sum(x for x,_ in pairs)/n:.2f} mean agy {sum(y for _,y in pairs)/n:.2f}")
print('meta:',{v:(meta[v].get('kind'),meta[v].get('evidence_strength')) for v in V})
rows=[]
for k in cl:
    cs=[sc(C[k][v]) for v in V]; gs=[g[k][v] for v in V]
    sup=sum(s>=1 for s in cs); strong=sum(s==2 for s in cs); contra=[v for v,s in zip(V,cs) if s<0]
    w=sum(s*meta[v].get('evidence_strength',1) for v,s in zip(V,cs) if s>0)
    agy_sup=sum(s>=1 for s in gs)
    rsup=sum(1 for r in rs[k].values() if r['score']>=1)
    rows.append((k,cl[k],rsup,sup,strong,agy_sup,w,contra,cs))
    print(f"{k}|reports {rsup}/5|videos Claude ≥1:{sup}/{len(V)} (=2:{strong}) agy≥1:{agy_sup}/{len(V)}|weighted {w}|contra {contra}|{cs}")
json.dump({'videos':V,'meta':meta,'claude':{k:{v:sc(C[k][v]) for v in V} for k in cl},'agy':g,'interrater':{'exact':exact,'bucket':buck,'kappa':kappa,'mae':mae}},open('scoring/video-merged.json','w'),indent=1,ensure_ascii=False)

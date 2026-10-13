import re,glob,os,difflib,json,sys
root=sys.argv[1]; res={}
def norm(s): return re.sub(r'[^\w ]','',re.sub(r'\s+',' ',s.lower())).strip()
for md in sorted(glob.glob(root+'/[0-9][0-9]-*.md')):
    base=os.path.basename(md)[:-3]; vid=base[3:]
    tr=open(f'{root}/transcripts/{vid}.txt').read().splitlines()
    segs=[]
    for l in tr:
        m=re.match(r'\[(\d+):(\d+)\] (.*)',l)
        if m: segs.append((int(m[1])*60+int(m[2]),m[3]))
    text=open(md).read()
    sec=re.split(r'##\s*Trích dẫn[^\n]*\n',text)
    if len(sec)<2: res[base]={'quotes':0}; continue
    sec=re.split(r'\n## ',sec[1])[0]
    items=[]
    for line in sec.splitlines():
        ts=re.findall(r'\[(\d+):(\d+)(?::(\d+))?\]',line)
        q=re.findall(r'["“”]([^"“”]{15,})["“”]',line) or re.findall(r'\*([^*]{15,})\*',line)
        if not ts or not q: continue
        h=ts[0]; t=(int(h[0])*3600+int(h[1])*60+int(h[2])) if h[2] else int(h[0])*60+int(h[1])
        qn=norm(q[0])
        # best match over sliding windows of 6 segments
        best=(0,None)
        for i in range(len(segs)):
            w=norm(' '.join(s for _,s in segs[i:i+6]))
            r=difflib.SequenceMatcher(None,qn,w).find_longest_match(0,len(qn),0,len(w)).size/max(1,len(qn))
            if r>best[0]: best=(r,segs[i][0])
        items.append({'q':q[0][:70],'ts':t,'match':round(best[0],2),'found_at':best[1],'ts_off':None if best[1] is None else abs(best[1]-t)})
    res[base]=items
for k,v in res.items():
    if not v or isinstance(v,dict): print(k,'NO QUOTES PARSED'); continue
    ok=sum(1 for x in v if x['match']>=0.6); tsok=sum(1 for x in v if x['match']>=0.6 and x['ts_off']<=60)
    print(f"{k}: {len(v)} quotes, text-match≥0.6: {ok}, timestamp within 60s: {tsok}", [ (x['match'],x['ts_off']) for x in v])
json.dump(res,open(root+'/quote-check.json','w'),ensure_ascii=False,indent=1)

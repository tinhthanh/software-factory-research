import sys,warnings;warnings.filterwarnings('ignore')
from youtube_transcript_api import YouTubeTranscriptApi
out=sys.argv[1]; ids=sys.argv[2:]
api=YouTubeTranscriptApi()
for vid in ids:
    try:
        tl=api.list(vid); langs=[t.language_code for t in tl]
        pref=['en','en-US','vi']+langs
        t=api.fetch(vid,languages=pref)
        lines=[f"[{int(s.start//60):02d}:{int(s.start%60):02d}] {s.text}" for s in t]
        open(f"{out}/{vid}.txt","w").write("\n".join(lines))
        print(vid,"OK",t.language_code,len(lines),"segs", int(t[-1].start//60),"min")
    except Exception as e: print(vid,"FAIL",type(e).__name__,str(e)[:150].replace('\n',' '))

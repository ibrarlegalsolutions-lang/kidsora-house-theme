import json,sys
from faster_whisper import WhisperModel
m=WhisperModel("large-v3",device="cpu",compute_type="int8")
import numpy as np,subprocess
a=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",sys.argv[1],"-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout,np.int16).astype(np.float32)/32768
segs,info=m.transcribe(a,word_timestamps=True,vad_filter=False,language="ur",beam_size=5)
print(info.language, info.language_probability)
words=[]
for s in segs:
    print(f"[{s.start:6.2f}-{s.end:6.2f}] {s.text}")
    for w in s.words: words.append({"text":w.word.strip(),"start":round(w.start,3),"end":round(w.end,3),"p":round(w.probability,2)})
json.dump(words,open("transcript_lv3.json","w"),indent=0)

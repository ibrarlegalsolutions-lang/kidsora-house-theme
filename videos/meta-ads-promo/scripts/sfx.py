import numpy as np, wave
sr=48000; N=int(46*sr); out=np.zeros(N); rng=np.random.default_rng(3)
def add(x,t,g):
    i=int(t*sr); j=min(N,i+len(x)); out[i:j]+=x[:j-i]*g
def whoosh(d=0.5):
    n=rng.standard_normal(int(d*sr)); t=np.arange(len(n))/sr
    # moving one-pole lowpass sweep
    y=np.zeros_like(n); a=0
    for k in range(len(n)):
        fc=300+4000*np.sin(np.pi*t[k]/d)**2; c=np.exp(-2*np.pi*fc/sr); a=(1-c)*n[k]+c*a; y[k]=a
    return y*np.sin(np.pi*t/d)**1.5
def pop():
    t=np.arange(int(0.12*sr))/sr; f=900*np.exp(-t*18)+300
    return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-t*35)
def ding():
    t=np.arange(int(0.9*sr))/sr
    return sum(a*np.sin(2*np.pi*f*t) for f,a in ((1318,1),(1976,.5),(2637,.25)))*np.exp(-t*5)
def impact():
    t=np.arange(int(0.6*sr))/sr; f=40+120*np.exp(-t*20)
    return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-t*6)+0.3*rng.standard_normal(len(t))*np.exp(-t*25)
add(whoosh(0.45),3.30,0.5)
for t in (4.75,8.3,12.6,14.95,17.12,18.7,20.35,27.6,33.85,36.95,42.4): add(pop(),t,0.35)
add(ding(),31.93,0.22)
add(impact(),39.35,0.55)
add(whoosh(0.6),40.2,0.45)
out/=max(1,np.abs(out).max()/0.9)
w=wave.open("sfx.wav","wb");w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes((out*32767).astype(np.int16).tobytes());w.close()

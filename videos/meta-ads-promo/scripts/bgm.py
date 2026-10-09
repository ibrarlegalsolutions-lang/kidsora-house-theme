import numpy as np, wave
sr=44100; bpm=100; beat=60/bpm; dur=46.5
N=int(sr*dur); L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(7)
def note(m): return 440*2**((m-69)/12)
def add(sig,t0,pan=0.0,g=1.0):
    i=int(t0*sr); j=min(N,i+len(sig)); s=sig[:j-i]*g
    L[i:j]+=s*np.sqrt(0.5*(1-pan)); R[i:j]+=s*np.sqrt(0.5*(1+pan))
def tone(f,d,harm=(1,.5,.25,.12),att=0.01,dec=None):
    t=np.arange(int(d*sr))/sr
    x=sum(a*np.sin(2*np.pi*f*k*t+rng.uniform(0,6)) for k,a in enumerate(harm,1))
    env=np.minimum(1,t/att)
    env*= np.exp(-t/dec) if dec else np.minimum(1,(d-t)/0.4).clip(0,1)
    return x*env
# I-V-vi-IV in C : C G Am F, each chord 2 bars (8 beats)
chords=[[48,55,60,64,67],[43,55,59,62,67],[45,57,60,64,69],[41,57,60,65,69]]
bar=4*beat; clen=2*bar
t=0.0;ci=0
while t<dur:
    ch=chords[ci%4]
    # pad
    for m in ch[1:]:
        for det in (-0.08,0.08):
            add(tone(note(m)*(1+det/100),clen+0.6,harm=(1,.35,.15,.05),att=0.8),t,pan=det*6,g=0.045)
    # sub bass
    add(tone(note(ch[0]-12+12),clen,harm=(1,.2),att=0.05),t,g=0.10)
    # arpeggio 8ths
    arp=[ch[2]+12,ch[3]+12,ch[4]+12,ch[3]+12]
    for k in range(16):
        tt=t+k*beat/2
        if tt>=dur: break
        add(tone(note(arp[k%4]),0.6,harm=(1,.3,.1),att=0.004,dec=0.18),tt,pan=0.35*np.sin(k),g=0.06)
    t+=clen;ci+=1
# drums: start after 3.5s (post-hook), lighter in body
def kick():
    tt=np.arange(int(0.35*sr))/sr; f=50+90*np.exp(-tt*30)
    return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-tt*9)
def hat():
    n=rng.standard_normal(int(0.06*sr)); n=np.diff(n,prepend=0); tt=np.arange(len(n))/sr
    return n*np.exp(-tt*70)
def clap():
    n=rng.standard_normal(int(0.2*sr)); tt=np.arange(len(n))/sr
    n=np.convolve(n,np.ones(6)/6,'same'); return n*np.exp(-tt*22)
b=0
while b*beat<dur:
    tt=b*beat
    if tt>=3.4:
        if b%2==0: add(kick(),tt,g=0.20)
        if b%4==2: add(clap(),tt,g=0.05)
        add(hat(),tt+beat/2,pan=0.3,g=0.05)
    b+=1
# riser into hook-cut at ~3.57 and into CTA at ~40.6
for t0 in (2.6,39.6):
    d=1.0; tt=np.arange(int(d*sr))/sr
    n=rng.standard_normal(len(tt)); n=np.convolve(n,np.ones(3)/3,'same')
    add(n*(tt/d)**2*0.08,t0)
# reverb
ir_t=np.arange(int(1.8*sr))/sr; ir=rng.standard_normal(len(ir_t))*np.exp(-ir_t*3.2); ir/=np.abs(ir).sum()/6
def fconv(x,h):
    n=len(x)+len(h); n2=1<<(n-1).bit_length()
    return np.fft.irfft(np.fft.rfft(x,n2)*np.fft.rfft(h,n2),n2)[:len(x)]
L=L+0.35*fconv(L,ir); R=R+0.35*fconv(R,np.roll(ir,37))
# master: fade in/out
tt=np.arange(N)/sr
env=np.minimum(1,tt/1.2)*np.clip((dur-tt)/2.5,0,1)
L*=env;R*=env
m=max(np.abs(L).max(),np.abs(R).max()); L=L/m*0.85; R=R/m*0.85
st=(np.stack([L,R],1)*32767).astype(np.int16)
w=wave.open("bgm.wav","wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(st.tobytes()); w.close()

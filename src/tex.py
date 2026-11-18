import struct,numpy as np,texture2ddecoder,etcpak
def mip_sizes(w,h,mips,bs):
    return [(max(1,w>>m),max(1,h>>m),max(1,((w>>m)+3)//4)*max(1,((h>>m)+3)//4)*bs) for m in range(mips)]
def split(t):
    sz,mips,one,fmt,w,h,ns=struct.unpack_from('<7I',t,0)
    assert fmt==2 and one==1 and sz==len(t)
    ms=mip_sizes(w,h,mips,8); tot=sum(x[2] for x in ms)
    head=t[:len(t)-tot]; data=t[len(t)-tot:]; out=[]; p=0
    for mw,mh,n in ms: out.append((mw,mh,data[p:p+n])); p+=n
    return head,out
def dec_bc1(blob,mw,mh):
    W=max(4,(mw+3)//4*4); H=max(4,(mh+3)//4*4)
    img=texture2ddecoder.decode_bc1(blob,W,H)
    a=np.frombuffer(img,np.uint8).reshape(H,W,4)[...,[2,1,0,3]]  # BGRA->RGBA
    return a.copy()
def enc_bc1(rgba):
    H,W,_=rgba.shape
    return etcpak.compress_bc1(np.ascontiguousarray(rgba).tobytes(),W,H)
def recolor(rgba):
    a=rgba.astype(np.float32)/255; r,g,b=a[...,0],a[...,1],a[...,2]
    mx=np.maximum(np.maximum(r,g),b); mn=np.minimum(np.minimum(r,g),b); v=mx
    s=np.where(mx>0,(mx-mn)/np.maximum(mx,1e-6),0); d=np.maximum(mx-mn,1e-6)
    hh=np.where(mx==r,((g-b)/d)%6,np.where(mx==g,(b-r)/d+2,(r-g)/d+4))*60
    hd=np.minimum(np.abs(hh),360-np.abs(hh))
    hd=np.where(hh>180, np.minimum(hd, np.maximum(0,300-hh)+0), hd)  # crimson/plum shadows (300..360) count as red
    w=np.clip((32-hd)/8,0,1)*np.clip((s-0.5)/0.12,0,1)*np.clip((0.5-g/np.maximum(r,1e-6))/0.1,0,1)
    # edge pass: softer reds (anti-aliased cape borders) next to the cape
    from scipy.ndimage import maximum_filter
    near=maximum_filter((w>0.5).astype(np.float32),size=7)
    soft=np.clip((32-hd)/8,0,1)*np.clip((s-0.2)/0.1,0,1)*np.clip((0.7-g/np.maximum(r,1e-6))/0.1,0,1)*(r>b)
    w=np.maximum(w,soft*near)
    P=np.stack([v*0.55,v*0.22,v*0.85],-1)
    out=a.copy(); out[...,:3]=a[...,:3]*(1-w[...,None])+P*w[...,None]
    return (np.clip(out,0,1)*255+0.5).astype(np.uint8), w
def build(t):
    head,mips=split(t); newdata=b''; stats=[]
    for mw,mh,blob in mips:
        img=dec_bc1(blob,mw,mh); new,w=recolor(img)
        H,W,_=img.shape; bw,bh=W//4,H//4
        enc=enc_bc1(new)
        changed=(w.reshape(bh,4,bw,4).max(axis=(1,3))>0.002)
        ob=bytearray(blob); n=0
        for by in range(bh):
            for bx in range(bw):
                if changed[by,bx]:
                    i=(by*bw+bx)*8; ob[i:i+8]=enc[i:i+8]; n+=1
        newdata+=bytes(ob); stats.append((mw,n,bw*bh))
    out=head+newdata; assert len(out)==len(t); return out,stats

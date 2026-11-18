M=2**64-1
def mix64(a,b,c):
    a=(a-b-c)&M; a^=(c>>43)
    b=(b-c-a)&M; b^=(a<<9)&M
    c=(c-a-b)&M; c^=(b>>8)
    a=(a-b-c)&M; a^=(c>>38)
    b=(b-c-a)&M; b^=(a<<23)&M
    c=(c-a-b)&M; c^=(b>>5)
    a=(a-b-c)&M; a^=(c>>35)
    b=(b-c-a)&M; b^=(a<<49)&M
    c=(c-a-b)&M; c^=(b>>11)
    a=(a-b-c)&M; a^=(c>>12)
    b=(b-c-a)&M; b^=(a<<18)&M
    c=(c-a-b)&M; c^=(b>>22)
    return a,b,c
def lookup8(k,level=0x123456789abcdeff):
    L=len(k); a=b=level; c=0x9e3779b97f4a7c13; i=0; n=L
    while n>=24:
        a=(a+int.from_bytes(k[i:i+8],'little'))&M; b=(b+int.from_bytes(k[i+8:i+16],'little'))&M; c=(c+int.from_bytes(k[i+16:i+24],'little'))&M
        a,b,c=mix64(a,b,c); i+=24; n-=24
    c=(c+L)&M; r=k[i:]
    for j in range(len(r)):
        if j<8: a=(a+(r[j]<<(8*j)))&M
        elif j<16: b=(b+(r[j]<<(8*(j-8))))&M
        else: c=(c+(r[j]<<(8*(j-16+1))))&M
    a,b,c=mix64(a,b,c); return c

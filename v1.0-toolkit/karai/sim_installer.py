# Mirrors KaraiMod.ps1 Set-Level exactly (table parse, Level-Of, rebuild-from-backup, patch walk, SHA checks)
import re,struct,hashlib,shutil,sys,os
PS='/home/claude/pkg/KaraiMod/KaraiMod.ps1'; HERE=os.path.dirname(PS)
s=open(PS).read()
files=[]
for m in re.finditer(r"Name='([^']*)';\s*Rel='([^']*)';\s*Backup='([^']*)';\s*Sha=@\(([^)]*)\);\s*Patch=@\(([^)]*)\)",s,re.S):
    files.append(dict(Name=m[1],Rel=m[2],Backup=m[3],Sha=re.findall(r"'([0-9A-F]{40})'",m[4]),Patch=re.findall(r"'([^']*)'",m[5])))
def sha(p):
    h=hashlib.sha1()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<24),b''): h.update(b)
    return h.hexdigest().upper()
def apply(target,pf,rev):
    with open(pf,'rb') as br, open(target,'r+b') as fs:
        assert br.read(4)==b'KPAT'
        old,new=struct.unpack('<QQ',br.read(16)); cnt,=struct.unpack('<I',br.read(4))
        for _ in range(cnt):
            off,ln=struct.unpack('<QI',br.read(12)); nw=br.read(ln); od=br.read(ln)
            fs.seek(off); fs.write(od if rev else nw)
        fs.truncate(old if rev else new)
def set_level(f,path,bak,target,log):
    cur=f['Sha'].index(sha(path)) if sha(path) in f['Sha'] else -1
    want=min(target,len(f['Sha'])-1)
    if cur<0:
        if os.path.exists(bak) and sha(bak)==f['Sha'][0]:
            log.append('unknown build -> rebuild from backup'); shutil.copyfile(bak,path); lvl=0
            while lvl<want:
                if f['Patch'][lvl]: apply(path,os.path.join(HERE,f['Patch'][lvl]),False)
                lvl+=1; assert sha(path)==f['Sha'][lvl],('check failed at',lvl)
        else: log.append('REFUSED unknown'); return False
    else:
        lvl=cur
        while lvl!=want:
            if lvl<want:
                if f['Patch'][lvl]: apply(path,os.path.join(HERE,f['Patch'][lvl]),False)
                lvl+=1
            else:
                lvl-=1
                if f['Patch'][lvl]: apply(path,os.path.join(HERE,f['Patch'][lvl]),True)
            assert sha(path)==f['Sha'][lvl],('check failed at',lvl)
    assert sha(path)==f['Sha'][want]; log.append('OK level %d %s'%(want,sha(path))); return True
if __name__=='__main__':
    for f in files: print(f['Name'],len(f['Sha']),len(f['Patch']),[p for p in f['Patch'] if p and not os.path.exists(os.path.join(HERE,p))])

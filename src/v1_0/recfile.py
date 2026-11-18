"""Readable source for additions to an encrypted CFF0 game-data record.

The mod never changes the original part of a record: it only appends new data, new pointers and new
symbols. A .rec file lists exactly what is appended (offsets are inside the decrypted data):

  record <key>                 pak entry key (hex)
  base <n>                     size of the original data; everything below is appended after it
  size <n>                     final data size
  ptch_pad <0|1>               whether the pointer table chunk is padded to 16 bytes
  sym <off> <type> <len> <name>  a new symbol (exported object): offset, type hash, chunk length
                               (name + zero padding, as stored), name
  ptr <slot> <target>          a new pointer: the 8-byte slot at <slot> points to offset <target>
  str <off> "<text>"           a C string (JSON-quoted)
  hex <off> <bytes>            raw bytes (numbers, flags); the comment shows them as u32 / f32
Bytes that are not listed are zero. Pointer slots stay zero in the data; the game fills them from the
pointer table when it loads the record.
"""
import os, sys, json, struct
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
from cff import dec, enc

class Rec:
    """Minimal CFF0 record reader/writer (same logic as v1.0-toolkit/tools/cffrec.py). Round-trips byte-exactly."""
    @staticmethod
    def _chunks(d):
        i = 0x40; out = []
        while i + 8 <= len(d):
            tag = d[i:i + 4]; n = struct.unpack_from('<I', d, i + 4)[0]
            if n < 8 or not tag.isalnum(): break
            out.append((tag, i, n)); i += n
        return out
    @classmethod
    def load(cls, raw):
        r = cls(); r.wrap = None; d = raw
        if d[:4] == b'RSC0': r.wrap = d[:32]; d = d[32:]
        r.hdr = bytearray(d[:0x40]); r.order = []; r.syms = []; r.extra = []
        for tag, i, n in cls._chunks(d):
            body = d[i + 8:i + n]; r.order.append(tag)
            if tag == b'DEF0': r.def0 = body
            elif tag == b'INST': r.keyidx = r.def0[1]; r.inst = bytearray(dec(body, r.keyidx))
            elif tag == b'PTCH':
                cnt = struct.unpack_from('<I', body, 0)[0]; r.ptch_hdr = body[4:8]
                r.ptrs = [struct.unpack_from('<II', body, 8 + k * 8) for k in range(cnt)]
                r.ptch_pad = len(body) - (8 + cnt * 8)
            elif tag == b'SYMB': r.syms.append(body)
            else: r.extra.append((tag, body))
        r.tail = d[sum(n for _, _, n in cls._chunks(d)) + 0x40:]
        return r
    def save(self):
        ch = lambda tag, body: tag + struct.pack('<I', len(body) + 8) + body
        pt = struct.pack('<I', len(self.ptrs)) + self.ptch_hdr + b''.join(struct.pack('<II', a, b) for a, b in self.ptrs)
        pt += b'\0' * ((-(len(pt) + 8)) % 16) if self.ptch_pad else b''
        out = b''
        for tag in self.order:
            if tag == b'DEF0': out += ch(tag, self.def0)
            elif tag == b'INST': out += ch(tag, enc(bytes(self.inst), self.keyidx))
            elif tag == b'PTCH': out += ch(tag, pt)
        for s in self.syms: out += ch(b'SYMB', s)
        for t, b in self.extra: out += ch(t, b)
        hdr = bytearray(self.hdr); struct.pack_into('<I', hdr, 4, 0x40 + len(out) + len(self.tail))
        body = bytes(hdr) + out + self.tail
        if self.wrap:
            w = bytearray(self.wrap); struct.pack_into('<II', w, 4, len(body), len(body)); return bytes(w) + body
        return body

def _sym_parse(s):
    off, th = struct.unpack_from('<II', s, 0); e = s.find(b'\0', 8); return off, th, s[8:e].decode('latin1')

def _sym_make(off, th, name, length):
    b = struct.pack('<II', off, th) + name.encode() + b'\0'
    assert length >= len(b)
    return b + b'\0' * (length - len(b))

def write_source(key, orig_raw, new_raw, path, title):
    ra, rb = Rec.load(orig_raw), Rec.load(new_raw)
    n = len(ra.inst); I = bytes(rb.inst)
    assert I[:n] == bytes(ra.inst), 'original part changed'
    assert rb.ptrs[:len(ra.ptrs)] == ra.ptrs and rb.syms[:len(ra.syms)] == ra.syms
    assert rb.order == ra.order + [b'SYMB'] * (len(rb.syms) - len(ra.syms))
    newp = rb.ptrs[len(ra.ptrs):]; P = dict(newp)
    L = ['; %s' % title, '; Generated from the released patch by gen_source.py; build.py rebuilds the record from',
         '; the original game record + this file and must reproduce the release byte for byte.', '',
         'record %016x' % key, 'base %d' % n, 'size %d' % len(I), 'ptch_pad %d' % (1 if rb.ptch_pad else 0), '']
    for s in rb.syms[len(ra.syms):]:
        off, th, nm = _sym_parse(s); L.append('sym %#x %#010x %d %s' % (off, th, len(s), nm))
    L.append('')
    strings = set()
    for slot, t in newp:
        if t >= n and I[t:t + 1] != b'\0':
            e = I.find(b'\0', t); s = I[t:e]
            if s and all(32 <= c < 127 for c in s): strings.add(t)
    symat = {_sym_parse(s)[0]: _sym_parse(s)[2] for s in rb.syms}
    o = n; covered = set()
    while o < len(I):
        if o in symat: L.append(''); L.append('; ---- %s' % symat[o])
        if o in strings:
            e = I.find(b'\0', o); L.append('str %#x %s' % (o, json.dumps(I[o:e].decode()))); o = e + 1; continue
        if o in P:
            t = P[o]; e = I.find(b'\0', t); ts = I[t:e] if t < len(I) else b''
            note = repr(ts.decode()) if ts and all(32 <= c < 127 for c in ts) else symat.get(t, '')
            L.append('ptr %#x %#x%s' % (o, t, ('    ; ' + note) if note else '')); o += 8; continue
        q = I[o:o + 8]
        if o % 8 or len(q) < 8:
            if I[o] != 0: L.append('hex %#x %s' % (o, I[o:o + 1].hex()))
            o += 1; continue
        if q != b'\0' * 8:
            u = struct.unpack('<2I', q); f = struct.unpack('<2f', q)
            ff = ', '.join('%g' % x for x in f if x == x and 1e-6 < abs(x) < 1e7)
            L.append('hex %#x %s    ; u32 %#x %#x%s' % (o, q.hex(), u[0], u[1], ('  f32 ' + ff) if ff else ''))
        o += 8
    # pointers that live inside the original part (none expected) or point to the original part are already listed;
    extra = [(s, t) for s, t in newp if s < n]
    for s, t in extra: L.append('ptr %#x %#x' % (s, t))
    open(path, 'w').write('\n'.join(L) + '\n')

def build(orig_raw, path):
    r = Rec.load(orig_raw); hdr = {}; syms = []; ptrs = []; writes = []
    for ln in open(path):
        line = ln.split(';', 1)[0].strip() if not ln.lstrip().startswith('str ') else ln.strip()
        if not line: continue
        k, rest = line.split(None, 1)
        if k in ('record', 'base', 'size', 'ptch_pad'): hdr[k] = rest
        elif k == 'sym':
            off, th, ln_, nm = rest.split(None, 3); syms.append(_sym_make(int(off, 16), int(th, 16), nm, int(ln_)))
        elif k == 'ptr':
            s, t = rest.split()[:2]; ptrs.append((int(s, 16), int(t, 16)))
        elif k == 'str':
            off, js = rest.split(None, 1); writes.append((int(off, 16), json.loads(js).encode() + b'\0'))
        elif k == 'hex':
            off, hx = rest.split()[:2]; writes.append((int(off, 16), bytes.fromhex(hx)))
        else: raise SystemExit('%s: unknown line %r' % (path, ln))
    base, size = int(hdr['base']), int(hdr['size'])
    assert len(r.inst) == base, 'this is not the original record (%d bytes, expected %d)' % (len(r.inst), base)
    I = bytearray(r.inst) + bytearray(size - base)
    for off, b in writes:
        assert off >= base, 'source writes into the original part at %#x' % off
        I[off:off + len(b)] = b
    r.inst = I; r.ptrs = r.ptrs + ptrs; r.syms = r.syms + syms
    r.order = r.order + [b'SYMB'] * len(syms); r.ptch_pad = int(hdr['ptch_pad'])
    return r.save()

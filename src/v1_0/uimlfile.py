"""Readable source for the select-screen layout change (UIML, default.pak2).

The layout is a tree of UI elements. The mod inserts elements (banners and portraits) and, in the Both build, changes a few attributes (the
portrait size). The .json source lists each edit in order: insert (parent path, position, full element)
or set_attrs (element path, new attribute list).
"""
import json, struct, difflib

def parse(d):
    assert d[:5] == b'UIML!' and d[9] == 1
    hdr_len = 11 + 4 * d[10]
    def el(o):
        t = d[o]; o += 1; nl = d[o]; nm = d[o + 1:o + 1 + nl].decode('latin1'); o += 1 + nl
        ac = d[o]; o += 1; at = []
        for _ in range(ac):
            i, l = d[o], d[o + 1]; at.append([i, d[o + 2:o + 2 + l].decode('latin1')]); o += 2 + l
        pc = d[o]; o += 1; props = []
        for _ in range(pc):
            i = d[o]; o += 1; e, o = el(o); props.append([i, e])
        nc = (d[o] << 8) | d[o + 1]; o += 2; kids = []
        for _ in range(nc):
            e, o = el(o); kids.append(e)
        return {'type': t, 'name': nm, 'attrs': at, 'props': props, 'kids': kids}, o
    root, end = el(hdr_len)
    assert end == len(d)
    return d[:hdr_len], root

def ser(e):
    b = bytearray([e['type'], len(e['name'].encode('latin1'))]) + e['name'].encode('latin1')
    b.append(len(e['attrs']))
    for i, v in e['attrs']:
        vb = v.encode('latin1'); b += bytes([i, len(vb)]) + vb
    b.append(len(e['props']))
    for i, p in e['props']: b.append(i); b += ser(p)
    b += struct.pack('>H', len(e['kids']))
    for k in e['kids']: b += ser(k)
    return bytes(b)

def _key(e):
    """identity of an element for matching: type, name and its id-like attributes (27 = element id, 14 = image)"""
    return (e['type'], e['name'], tuple(v for i, v in e['attrs'] if i in (27,)))

def diff_ops(a, b, path=()):
    """Element trees a -> b. Returns ops in apply order: ('attrs', path, new attrs) and ('insert', parent path, index, element).
    Paths are child indexes in the NEW tree; applying the ops in order rebuilds b from a."""
    assert a['type'] == b['type'] and a['name'] == b['name']
    for (i, p), (j, q) in zip(a['props'], b['props']): assert i == j and ser(p) == ser(q)
    assert len(a['props']) == len(b['props'])
    out = []
    if a['attrs'] != b['attrs']: out.append(('attrs', list(path), b['attrs']))
    ka = [ser(k) for k in a['kids']]; kb = [ser(k) for k in b['kids']]
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ka, kb, autojunk=False).get_opcodes():
        if tag == 'equal': continue
        if tag == 'delete': raise ValueError('element removed at %s' % (path,))
        if tag == 'insert':
            for j in range(j1, j2): out.append(('insert', list(path), j, b['kids'][j]))
            continue
        # replace: match by identity, recurse into matched pairs, insert the rest
        sa = [_key(x) for x in a['kids'][i1:i2]]; sb = [_key(x) for x in b['kids'][j1:j2]]
        for t2, x1, x2, y1, y2 in difflib.SequenceMatcher(None, sa, sb, autojunk=False).get_opcodes():
            if t2 == 'equal' or (t2 == 'replace' and x2 - x1 == y2 - y1):
                for x, y in zip(range(i1 + x1, i1 + x2), range(j1 + y1, j1 + y2)): out += diff_ops(a['kids'][x], b['kids'][y], path + (y,))
            elif t2 == 'insert':
                for y in range(j1 + y1, j1 + y2): out.append(('insert', list(path), y, b['kids'][y]))
            else: raise ValueError('not a pure insertion/edit at %s: %s' % (path, t2))
    return out

def write_source(orig_doc, new_doc, path, title):
    ha, ra = parse(orig_doc); hb, rb = parse(new_doc)
    assert ha == hb, 'header changed'
    ops = []
    for op in diff_ops(ra, rb):
        if op[0] == 'attrs': ops.append({'op': 'set_attrs', 'path': op[1], 'attrs': op[2]})
        else: ops.append({'op': 'insert', 'parent_path': op[1], 'index': op[2], 'element': op[3]})
    doc = {'comment': title + ' Generated from the released patch by gen_source.py; build.py applies these edits '
                      '(in order) to the original layout and must reproduce the release byte for byte. '
                      'Paths are child indexes from the root; attributes are [attribute id, text] pairs.',
           'ops': ops}
    open(path, 'w').write(json.dumps(doc, indent=1) + '\n')

def build(orig_doc, path):
    hdr, root = parse(orig_doc)
    for op in json.load(open(path))['ops']:             # in order; indexes already account for earlier inserts
        node = root
        for k in op.get('parent_path', op.get('path')): node = node['kids'][k]
        if op['op'] == 'insert': node['kids'].insert(op['index'], op['element'])
        else: node['attrs'] = op['attrs']
    return hdr + ser(root)

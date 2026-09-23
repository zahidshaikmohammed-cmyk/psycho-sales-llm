#!/usr/bin/env python3
"""Executable v2 canonical chapter validator."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path
from collections import Counter

SECTION_ORDER = ["Purpose", "Definition", "Core Understanding", "Relationship to This Chapter", "Boundaries", "Key Principles"]
GATE_NAMES = ["Ontology match", "Structural integrity", "Ownership", "Semantic depth", "Neighbor distinctions", "Scientific/evidence integrity", "Relationships", "Retrieval", "Anti-template", "Cross-chapter boundaries", "Final validation"]
TOPIC_RE = re.compile(r"^##\s+(?P<id>\d+\.\d+\.\d+)\s+(?P<name>.+?)\s*$", re.M)
SECTION_RE = re.compile(r"^##\s+(?P<n>\d+)\.\s+(?P<name>.+?)\s*$", re.M)
ARCH_CHAPTER_RE = re.compile(r"^#\s+CHAPTER\s+(?P<num>\d+\.\d+)\s+—\s+.+$", re.M)
ATTESTATION_HEADER = "## V2 Semantic Gate — Required for Canonical Seal"

def norm(s):
    return re.sub(r"\s+", " ", s.strip())

def architecture_names(text, chapter_num):
    matches = list(ARCH_CHAPTER_RE.finditer(text))
    target = None
    for i, m in enumerate(matches):
        if m.group('num') == chapter_num:
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            target = text[m.start():end]
            break
    if target is None:
        raise ValueError('Chapter ' + chapter_num + ' not found in architecture')
    names = []
    for line in target.splitlines():
        if re.match(r'^[-*]\s+', line):
            name = norm(re.sub(r'^[-*]\s+', '', line))
            if name and not name.startswith(('**', '`')):
                names.append(name)
    return names

def topic_blocks(text):
    matches = list(TOPIC_RE.finditer(text))
    return [(m.group('id'), norm(m.group('name')), text[m.end():(matches[i+1].start() if i+1 < len(matches) else len(text))]) for i,m in enumerate(matches)]

def sections(block):
    matches = list(SECTION_RE.finditer(block))
    return [(norm(m.group('name')), block[m.end():(matches[i+1].start() if i+1 < len(matches) else len(block))].strip()) for i,m in enumerate(matches)]

def check_attestation(text):
    errors=[]
    if ATTESTATION_HEADER not in text:
        return ['missing v2 semantic gate attestation']
    section=text.split(ATTESTATION_HEADER,1)[1]
    for gate in GATE_NAMES:
        m=re.search(r'^-\s+'+re.escape(gate)+r':\s+(PASS|FAIL)\s*$', section, re.M)
        if not m: errors.append('missing attestation gate: '+gate)
        elif m.group(1)!='PASS': errors.append('attestation gate is not PASS: '+gate)
    for label in ('P0','P1','P2','P3'):
        m=re.search(r'^-\s+'+label+r':\s+(\d+)\s*$', section, re.M)
        if not m: errors.append('missing attestation count: '+label)
        elif label in ('P0','P1') and m and int(m.group(1)) != 0: errors.append(label+' must be 0 for a seal')
    return errors

def validate(chapter_path, architecture_path, validation_path=None):
    chapter=chapter_path.read_text(encoding='utf-8')
    architecture=architecture_path.read_text(encoding='utf-8')
    errors=[]
    m=re.search(r'CHAPTER\s+(\d+\.\d+)', chapter[:1200])
    if not m: return ['cannot identify chapter number']
    num=m.group(1)
    expected=architecture_names(architecture,num)
    blocks=topic_blocks(chapter)
    ids=[x[0] for x in blocks]; names=[x[1] for x in blocks]
    if len(ids)!=len(set(ids)): errors.append('duplicate Topic IDs')
    if len(names)!=len(set(names)): errors.append('duplicate Topic names within chapter')
    if len(names)!=len(expected): errors.append('Topic count mismatch: chapter=%d architecture=%d' % (len(names),len(expected)))
    if names!=expected: errors.append('Topic names/order do not exactly match architecture')
    for tid,name,block in blocks:
        sec=sections(block); sn=[x[0] for x in sec]
        if sn!=SECTION_ORDER:
            errors.append('%s %s: six-section order mismatch' % (tid,name)); continue
        d=dict(sec)
        for s in SECTION_ORDER:
            if not d[s].strip(): errors.append('%s %s: empty %s' % (tid,name,s))
        if not re.search(r'^###\s+Owns\s*$', d['Boundaries'], re.M): errors.append('%s %s: missing Owns boundary' % (tid,name))
        if not re.search(r'^###\s+Defers\s*$', d['Boundaries'], re.M): errors.append('%s %s: missing Defers boundary' % (tid,name))
        core=d['Core Understanding']
        wc=len(re.findall(r'\b\w+[\w’\'-]*\b',core))
        if wc<45: errors.append('%s %s: Core Understanding below executable minimum (%d<45)' % (tid,name,wc))
        if re.search(r'\bTOPIC\b|For\s+\*\*TOPIC\*\*|This Topic belongs to Chapter|This chapter covers this Topic',block,re.I): errors.append('%s %s: template/generic signature' % (tid,name))
    core_sections=[dict(sections(b)).get('Core Understanding','').strip() for _,_,b in blocks]
    rel_sections=[dict(sections(b)).get('Relationship to This Chapter','').strip() for _,_,b in blocks]
    key_sections=[dict(sections(b)).get('Key Principles','').strip() for _,_,b in blocks]
    for label,vals in [('Core Understanding',core_sections),('Relationship to This Chapter',rel_sections),('Key Principles',key_sections)]:
        dup=[k for k,v in Counter(vals).items() if v and v>1]
        if dup: errors.append('repeated '+label+' blocks detected')
    if re.search(r'(?i)This Topic belongs to Chapter|This chapter covers this Topic',chapter): errors.append('generic chapter-membership language detected')
    if validation_path is None:
        errors.append('validation record path is required for v2 seal')
    else:
        errors.extend(check_attestation(Path(validation_path).read_text(encoding='utf-8')))
    return errors

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--chapter',required=True)
    p.add_argument('--architecture',required=True)
    p.add_argument('--validation',required=True)
    a=p.parse_args()
    try: errors=validate(Path(a.chapter),Path(a.architecture),Path(a.validation))
    except Exception as exc: errors=['validator exception: '+str(exc)]
    print('CANONICAL_V2_VALIDATION=PASS' if not errors else 'CANONICAL_V2_VALIDATION=FAIL')
    for e in errors: print('- '+e)
    return 0 if not errors else 1

if __name__=='__main__': sys.exit(main())
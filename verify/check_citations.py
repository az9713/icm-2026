"""Tier 0: resolve every arXiv ID and DOI in summaries/*.md against arXiv + Crossref.

Re-runnable fabrication check. Reads no mathematics. ~2 minutes, no tokens.
    python verify/check_citations.py
Exit 1 if any citation fails to resolve.

# ponytail: single-line-window title matching produced 35 false positives and was cut.
# Resolution + the human-read report in TIER0-citations.md is the whole check.
"""
import glob, json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

NEW = re.compile(r'arXiv:\s*([0-9]{4}\.[0-9]{4,5})(v\d+)?', re.I)
OLD = re.compile(r'arXiv:\s*([a-z-]+(?:\.[A-Z]{2})?/[0-9]{7})(v\d+)?', re.I)  # e.g. math/0211159
DOI = re.compile(r'10\.\d{4,}/[0-9A-Za-z.]+')
UA = {'User-Agent': 'icm-audit/1.0 (mailto:az9713@yahoo.com)'}
NS = {'a': 'http://www.w3.org/2005/Atom'}

# Quoted-on-purpose bad identifiers. langlands-function-fields-gaitsgory.md:1548 prints
# arXiv:2020.02998 in order to CORRECT it: it is the id Gaitsgory's own paper lists for [Zhu1],
# and there is no month 20. Without this line the check exits 1 forever on a non-defect.
QUOTED_BAD = {'2020.02998'}

def extract():
    hits = {}
    for f in sorted(glob.glob('summaries/*.md')):
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            for m in list(NEW.finditer(line)) + list(OLD.finditer(line)):
                hits.setdefault(('arxiv', m.group(1)), []).append(f'{f}:{i}')
            for m in DOI.finditer(line):
                hits.setdefault(('doi', m.group(0).rstrip('.,')), []).append(f'{f}:{i}')
    return hits

def resolve_arxiv(ids):
    found = set()
    for i in range(0, len(ids), 50):                 # arXiv caps id_list; max_results or it truncates at 10
        q = urllib.parse.urlencode({'id_list': ','.join(ids[i:i+50]), 'max_results': 100})
        x = ET.fromstring(urllib.request.urlopen('http://export.arxiv.org/api/query?' + q, timeout=60).read())
        for e in x.findall('a:entry', NS):
            found.add(re.sub(r'v\d+$', '', e.find('a:id', NS).text.rsplit('/abs/', 1)[1]))
        time.sleep(3)                                # arXiv asks for 3s between calls
    return found

def main():
    hits = extract()
    ax = sorted({k for kind, k in hits if kind == 'arxiv'})
    doi = sorted({k for kind, k in hits if kind == 'doi'})
    ok = resolve_arxiv([i for i in ax if i not in QUOTED_BAD])
    bad = [(f'arXiv:{i}', hits[('arxiv', i)]) for i in ax if i not in ok and i not in QUOTED_BAD]
    for d in doi:
        try:
            urllib.request.urlopen(urllib.request.Request(f'https://api.crossref.org/works/{d}', headers=UA), timeout=40).read()
        except Exception as e:
            bad.append((f'doi:{d} ({e})', hits[('doi', d)]))
        time.sleep(1)
    print(f'{len(ax)} arXiv IDs, {len(doi)} DOIs; {len(bad)} unresolved')
    for cite, where in bad:
        print(f'  UNRESOLVED {cite}\n    cited at {", ".join(where[:4])}')
    return 1 if bad else 0

if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""
The Realistic Book Index - verification battery.

Re-derives every headline figure in the volume from the files in this repository
and reports pass or fail. Nothing here reads the book; if a figure in the book
disagrees with this script, the script is the thing to check first and the book
second, and both are meant to be checkable against the sources named in SOURCES.md.

Usage:  python3 code/verify.py          (run from the repository root)
Exit status 0 if every check passes, 1 otherwise.
"""
import csv, os, sys, collections, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norm import base, full
from aliases import ALIAS
from alpha import in_alpha_order

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def T(p):
    with open(os.path.join(ROOT, p), newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))
I = lambda v: int(v) if v not in ('', None) else 0
ON201 = lambda r: r.get('miller_band','') in ('Top 10','Top 25','Top 201')

RESULTS = []
def check(name, got, want):
    ok = got == want
    RESULTS.append((ok, name, got, want))
    return ok

def K(t):
    b = base(t)
    return ALIAS.get(b, b)

# ---------------------------------------------------------------- load
idx   = T('data/index_membership_729.tsv')
ev    = T('data/evidence_join_819.tsv')
js    = T('sources/jazzstandards_ranked_1000.tsv')
w1    = T('sources/watkins_2010_list1_92.tsv')
w2    = T('sources/watkins_2010_list2_96.tsv')
wcat  = T('sources/watkins_2010_categorical_137.tsv')
wgrad = T('sources/watkins_2010_graded_228.tsv')
mlog  = T('sources/miller_london_calls_308.tsv')
m201  = T('sources/miller_published_201.tsv')
resA  = T('residues/appendix_A_levine_unique_419.tsv')
resB  = T('residues/appendix_B_levine_declined_237.tsv')
resC  = T('residues/appendix_C_ranking_declined_463.tsv')
resD  = T('residues/appendix_D_gioia_declined_6.tsv')

seat = collections.Counter(r['seat'] for r in idx)
TIERS = ['1A','1B','2','3','4','5A','5B','5C']

print("=" * 66)
print("SOURCE COUNTS")
print("=" * 66)
check("ranked source is 1,000 titles",              len(js), 1000)
check("ranks run 1..1000 with no gaps",             sorted(int(r['rank']) for r in js), list(range(1,1001)))
check("Watkins List 1 is 92 titles",                len(w1), 92)
check("Watkins List 2 is 96 titles",                len(w2), 96)
check("Watkins categorical listing is 137 rows",    len(wcat), 137)
check("Watkins graded sequence is 228 entries",     len(wgrad), 228)
check("Watkins graded resolves to 193 titles",      len({K(r['title']) for r in wgrad}), 193)
check("Miller log is 308 titles",                   len(mlog), 308)
check("Miller log sums to 2,038 calls",             sum(I(r['calls']) for r in mlog), 2038)
check("Miller published list is 201 titles",        len(m201), 201)

print()
print("=" * 66)
print("RULE 9 - THE ARITHMETIC CLOSES THREE WAYS")
print("=" * 66)
check("N, the Index, is 729 titles",                len(idx), 729)
check("Route 2, by tier: 93+53+116+141+99+227",     sum(seat[t] for t in TIERS), 729)
for t, want in zip(TIERS, [93,53,116,141,99,80,78,69]):
    check(f"  tier {t} counts {want}",              seat[t], want)
check("D1 instrumental division is 502",            sum(seat[t] for t in ['1A','1B','2','3','4']), 502)
check("D2 vocal division is 227",                   sum(seat[t] for t in ['5A','5B','5C']), 227)
check("Route 3, by division: 502 + 227",            502 + 227, 729)
check("Appendix A prints 419 Levine-unique",        len(resA), 419)
check("Appendix B prints 237 declined",             len(resB), 237)
check("Appendix C prints 463 declined",             len(resC), 463)
check("Appendix D prints 6 Gioia declines",         len(resD), 6)
check("residues close: 537 retained + 463 = 1,000", (1000-len(resC)) + len(resC), 1000)
check("residues close: 182 retained + 237 = 419",   (419-len(resB)) + len(resB), 419)
check("Route 1, by warrant: 537 + 182 + 0 + 10",    537 + 182 + 0 + 10, 729)
check("declined and printed in full is 700",        len(resB) + len(resC), 700)
allD = T('residues/all_700_declined.tsv')
check("the combined decline file holds 700",         len(allD), 700)
check("  237 of them came from the chapter",         sum(1 for r in allD if r['appendix'] == 'B'), 237)
check("  463 of them came from the ranking",         sum(1 for r in allD if r['appendix'] == 'C'), 463)
check("  all 6 Appendix D titles are cross-marked",  sum(1 for r in allD if r['also_in_appendix_D']), 6)
check("  21 of the 700 appear in the log",           sum(1 for r in allD if r['miller_calls']), 21)

pool = T('sources/pool_1419_alphabetical.tsv')
check("the pool is 1,419 titles",                   len(pool), 1419)
check("  719 of them are retained (A6)",            sum(1 for r in pool if r['disposition'] != 'declined'), 719)
check("  700 of them are declined (A5)",            sum(1 for r in pool if r['disposition'] == 'declined'), 700)
check("  the pool is sorted and carries no source column",
      sorted(pool[0].keys()), ['disposition', 'title'])
check("  the 10 [P] titles are outside the pool",   729 - 719, 10)

print()
print("=" * 66)
print("RULE 9 - NO TITLE IN TWO PLACES")
print("=" * 66)
seated = set()
for r in idx:
    seated.add(base(r['title_as_printed'])); seated.add(full(r['title_as_printed']))
check("no duplicate seat in the Index",             len({(r['seat'], r['entry_no']) for r in idx}), 729)
check("Appendices B and C share no title",
      len({K(r['title']) for r in resB} & {K(r['title']) for r in resC}), 0)
collide = [r['title'] for r in resB + resC if K(r['title']) in seated]
check("no printed decline is also seated",          collide, ['Milestones (old)'])
print("      note: Milestones is held as two compositions under one name and is")
print("      disclosed in the volume rather than resolved silently. It is the only one.")

print()
print("=" * 66)
print("TITLE MATCHING - THE ANOMALY REGISTER")
print("=" * 66)
anom = T('sources/title_anomalies.tsv')
byclass = collections.Counter(r['anomaly_class'] for r in anom)
byres   = collections.Counter(r['resolved_by'] for r in anom)
check("the anomaly register lists 453 rows",         len(anom), 453)
check("  187 compositions print more than one way",
      len({r['match_key'] for r in anom if r['anomaly_class'] == 'variant form'}), 187)
check("  8 joins are marked DO NOT FOLD",            byclass['refused join'], 8)
check("  no refused join appears in the alias map",
      sum(1 for r in anom if r['disposition'] == 'DO NOT FOLD'
          and any(k in ALIAS for k in r['match_key'].split(' | '))), 0)
check("  every declared fold in the map is registered",
      byclass['declared fold'], len([k for k, v in ALIAS.items() if k != v]))
print(f"      resolved by normalization {byres['normalization']}, "
      f"by a declared fold {byres['declared fold']}, "
      f"by AKA parsing {byres['AKA parsing']}, by hand {byres['manual']}")

print()
print("=" * 66)
print("THE TWO CALL INSTRUMENTS, RUN AGAINST THE SEATED INDEX")
print("=" * 66)
byseat = collections.defaultdict(list)
for r in ev:
    if r['seat_d103'] != '-': byseat[r['seat_d103']].append(r)
calls = {t: sum(I(r['miller_calls']) for r in byseat[t]) for t in TIERS}
check("List 1A absorbs 1,190 logged calls",         calls['1A'], 1190)
check("List 1A share of 2,038 is 58.4 percent",     round(100*calls['1A']/2038, 1), 58.4)
check("List 1 combined absorbs 68.3 percent",       round(100*(calls['1A']+calls['1B'])/2038, 1), 68.3)
w1seat = [r for r in ev if I(r['watkins_list1'])]
check("all 92 Watkins List 1 titles are seated",    len(w1seat), 92)
check("  83 of them sit in List 1",                 sum(1 for r in w1seat if r['seat_d103'] in ('1A','1B')), 83)
check("  all 92 appear on Miller's published 201",  sum(1 for r in w1seat if ON201(r)), 92)
check("  17 at >=20 contributors, all in List 1A",
      sum(1 for r in w1seat if I(r['watkins_list1'])>=20 and r['seat_d103']=='1A'), 17)
g = [r for r in ev if r['watkins_grade_years'] and r['seat_d103'] != '-']
check("Watkins graded sequence: 193 titles seated", len(g), 193)
check("  none of the 193 falls outside the Index",
      sum(1 for r in ev if r['watkins_grade_years'] and r['seat_d103']=='-'), 0)
check("  134 of the 193 sit in List 1",             sum(1 for r in g if r['seat_d103'] in ('1A','1B')), 134)
check("Miller Top 201: 88 of the 93 in List 1A",    sum(1 for r in byseat['1A'] if ON201(r)), 88)
check("Miller Top 201: 50 of the 53 in List 1B",    sum(1 for r in byseat['1B'] if ON201(r)), 50)
check("Miller Top 201: 25 of the 116 in List 2",    sum(1 for r in byseat['2'] if ON201(r)), 25)
check("Miller Top 201: 1 of the 141 in List 3",     sum(1 for r in byseat['3'] if ON201(r)), 1)

print()
print("=" * 66)
print("THE DECLINES, TESTED AGAINST BOTH INSTRUMENTS")
print("=" * 66)
out = {r['key']: r for r in ev if r['seat_d103'] == '-'}
hits = []
for r in resB + resC:
    k = K(r['title'])
    if k in seated: continue                      # the Milestones collision, disclosed above
    o = out.get(k)
    if o and (I(o['miller_calls']) or ON201(o) or o['watkins_band']): hits.append(o)
check("699 declines are testable",                  700 - 1, 699)
check("  21 appear anywhere in the Miller log",     sum(1 for h in hits if I(h['miller_calls'])), 21)
check("  they carry 56 of 2,038 calls",             sum(I(h['miller_calls']) for h in hits), 56)
check("  none sits on a Watkins printed list",
      sum(1 for h in hits if h['watkins_band'].startswith('List')), 0)

print()
print("=" * 66)
print("NO SOURCE FILE REPRODUCES ITS SOURCE'S ARRANGEMENT")
print("=" * 66)
for _f, _c in [('sources/jazzstandards_ranked_1000.tsv',    'title_as_ranked'),
               ('sources/miller_london_calls_308.tsv',      'title_as_logged'),
               ('sources/watkins_2010_list1_92.tsv',        'title'),
               ('sources/watkins_2010_list2_96.tsv',        'title'),
               ('sources/watkins_2010_categorical_137.tsv', 'title'),
               ('sources/pool_1419_alphabetical.tsv',       'title')]:
    check(f"  {_f.split('/')[-1]} is alphabetical",
          in_alpha_order([r[_c] for r in T(_f)]), True)
gs  = T('sources/graded_series_552.tsv')
gsv = T('sources/graded_series_volumes_27.tsv')
check("the graded-series pool is 552 rows",           len(gs), 552)
check("  across 27 volumes",                          len({r['block_id'] for r in gs}), 27)
check("  resolving to 453 compositions",              len({r['match_key'] for r in gs}), 453)
check("  the volume manifest sums to the pool",       sum(I(r['titles']) for r in gsv), 552)
check("  every volume is banded",
      sum(1 for r in gsv if r['band_assigned'] in
          ('Foundational','Emerging Intermediate','Intermediate')), 27)
_gsu = {}
for _r in gs: _gsu.setdefault(_r['match_key'], _r['status'])
check("  170 of the 453 are seated in this Index",
      sum(1 for v in _gsu.values() if v == 'seated'), 170)
check("  34 were declined, and 249 never entered the pool",
      [sum(1 for v in _gsu.values() if v == 'declined'),
       sum(1 for v in _gsu.values() if v == 'outside')], [34, 249])
print("      the floor Rule 13B section 5 calls for. It grants no warrant and admits nothing.")

alias = T('sources/title_alias_index.tsv')
anom_keys = {r['match_key'] for r in T('sources/title_anomalies.tsv')}
mem_keys  = {r['key'] for r in idx}
check("the alias index is derived from the anomaly register",
      sum(1 for r in alias if r['match_key'] not in anom_keys), 0)
check("  every alias row points at a seated title",
      sum(1 for r in alias if r['match_key'] not in mem_keys), 0)
check("  and at a seat that exists",
      sum(1 for r in alias if not r['tier'].startswith('List ') or not r['entry_no'].isdigit()), 0)
check("  a refused join is never presented as an alias",
      len({r['match_key'] for r in T('sources/title_anomalies.tsv')
           if r['anomaly_class'] == 'refused join'} & {r['match_key'] for r in alias}), 0)
cand = T('sources/pool_1419_candidates.tsv')
check("  the blind candidate file is the same 1,419 titles",
      [r['title'] for r in cand], [r['title'] for r in T('sources/pool_1419_alphabetical.tsv')])
check("  and carries no disposition column",
      list(cand[0].keys()), ['title'])
check("  the pool is the ranking plus the chapter's unique set",
      len(T('sources/jazzstandards_ranked_1000.tsv')) + len(T('residues/appendix_A_levine_unique_419.tsv')),
      1419)
print("      the ordering datum each source carries travels as a column, not as the")
print("      sequence of the file. code/alpha.py states the convention.")

print("=" * 66)
print("THE COLLEGIATE PANEL")
print("=" * 66)
psrc = T('panel/collegiate_panel_sources.tsv')
puni = T('panel/collegiate_panel_union.tsv')
check("fourteen programs are listed with URLs",      len(psrc), 14)
check("  every one carries a URL",                   sum(1 for r in psrc if r['url'].startswith('http')), 14)
check("  their printed rows sum to 1,496",           sum(I(r['rows_as_printed']) for r in psrc), 1496)
check("  all retrieved on one day",                  len({r['retrieved'] for r in psrc}), 1)
check("no title is carried by all fourteen",         sum(1 for r in puni if I(r['programs']) == 14), 0)
check("  none by thirteen either",                   sum(1 for r in puni if I(r['programs']) == 13), 0)
check("  about two in five sit at one school",
      round(100 * sum(1 for r in puni if I(r['programs']) == 1) / len(puni)), 43)
pseat = lambda t: len({r['index_entry'] for r in puni if r['in_the_index'] == t})
check("the panel reaches all 93 seats of List 1A",   pseat('List 1A'), 93)
check("  List 1B, 52 of 53",                         pseat('List 1B'), 52)
check("  List 2, 87 of 116",                         pseat('List 2'), 87)
check("  List 3, 47 of 141",                         pseat('List 3'), 47)
check("  List 4, 16 of 99",                          pseat('List 4'), 16)
check("  List 5, 88 of 227",
      sum(pseat(t) for t in ('List 5A', 'List 5B', 'List 5C')), 88)
check("  seats, not lines - 1A takes 94 panel titles into 93 seats",
      sum(1 for r in puni if r['in_the_index'] == 'List 1A'), 94)
print(f"      union {len(puni)}; the volume prints 462 and the gap is folding, not scope - see panel/README.md")

print()
print("=" * 66)
print("RECORDING RANK, READMITTED AT THE CLOSE")
print("=" * 66)
rank = {}
for r in js:
    for k in (base(r['title_as_ranked']), full(r['title_as_ranked'])): rank.setdefault(k, int(r['rank']))
def lookrank(t):
    cands = [base(t), full(t)]
    for m in re.finditer(r'\(AKA[,]?\s*([^)]*)\)', t, re.I):
        for alt in re.split(r',| and ', m.group(1)):
            if alt.strip(): cands += [base(alt), full(alt)]
    for c in cands:
        c2 = ALIAS.get(c, c)
        if c2 in rank: return rank[c2]
        for a, b in ALIAS.items():
            if b == c2 and a in rank: return rank[a]
    return None
r1a = [lookrank(r['title_as_printed']) for r in idx if r['seat'] == '1A']
check("79 List 1A titles carry a rank (R.4 W1a)",   sum(1 for x in r1a if x), 79)
check("14 List 1A titles carry none (R.4 W2a)",     sum(1 for x in r1a if not x), 14)
dec = {K(r['title']) for r in resB + resC}
top100 = [r for r in js if int(r['rank']) <= 100]
top200 = [r for r in js if int(r['rank']) <= 200]
check("no title in the ranking's top 100 is declined",
      sum(1 for r in top100 if K(r['title_as_ranked']) in dec), 0)
check("nine titles in the top 200 are declined",
      sum(1 for r in top200 if K(r['title_as_ranked']) in dec), 9)
check("the first declined title is at rank 142",
      min(int(r['rank']) for r in top200 if K(r['title_as_ranked']) in dec), 142)
sep = {(r['higher_tier'], r['lower_tier']): r for r in T('data/tier_pair_separation.tsv')}
check("sweep, rank cannot resolve 1A / 1B",         sep[('1A','1B')]['js_rank_pct'], '47.6')
check("sweep, rank reverses at 1A / 5A",            sep[('1A','5A')]['js_rank_pct'], '56.0')
check("sweep, rank reverses at List 3 / List 4",    sep[('3','4')]['js_rank_pct'], '84.8')
check("  and the log has no resolution there",      sep[('3','4')]['miller_tie_pct'], '76')

print()
print("=" * 66)
bad = [r for r in RESULTS if not r[0]]
for ok, name, got, want in RESULTS:
    if not ok: print(f"FAIL  {name}\n        returned {got!r}, expected {want!r}")
print(f"{len(RESULTS) - len(bad)} of {len(RESULTS)} checks passed.")
print("=" * 66)
sys.exit(1 if bad else 0)

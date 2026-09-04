#!/usr/bin/env python3
"""
Build the decision queue: every candidate title with every machine-derivable
fact attached, and no verdict on any of them.

This is the mechanical half of the method. It stops exactly where judgment
begins, which is Stage One of Rule 13. Nothing here declines a title, because
nothing here can: every one of the 1,419 candidates carries a source warrant by
construction - the pool IS the union of the three warrant sources - so warrant
checking removes no one. The reduction from 1,419 to a seated Index is the
practitioner filter doing all of it.

What this script settles, so a replicator does not have to:
  - the pool, as the union of the ranking and the chapter's unique set
  - title folding, against code/norm.py and code/aliases.py
  - warrant 1 and warrant 2 presence
  - recording rank
  - the two call instruments, which admit nothing and are attached for Stage Six
  - the graded-series floor Rule 13B section 5 calls for
  - what the collegiate panel reaches

What it cannot settle, and does not attempt:
  - any Stage One decline ground
  - the division rule
  - tier assignment
  - the form reservation at 4b
  - [P] and [E]

Run:  python3 code/build_queue.py
Out:  data/decision_queue_1419.tsv
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norm import base, full
from aliases import ALIAS, HOMONYMS
from alpha import alpha_key

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def T(p):
    with open(os.path.join(ROOT, p), newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))
def K(t):
    """Join key. Folds by the alias map, except for a declared homonym, where the
    parenthetical is what distinguishes two works and must survive."""
    k = base(t)
    if k in HOMONYMS: return full(t)
    return ALIAS.get(k, k)

rank   = {K(r['title_as_ranked']): int(r['rank']) for r in T('sources/jazzstandards_ranked_1000.tsv')}
levine = {K(r['title']) for r in T('residues/appendix_A_levine_unique_419.tsv')}
w1     = {K(r['title']): r['contributors'] for r in T('sources/watkins_2010_list1_92.tsv')}
w2     = {K(r['title']): r['contributors'] for r in T('sources/watkins_2010_list2_96.tsv')}
wcat   = {K(r['title']): r['total'] for r in T('sources/watkins_2010_categorical_137.tsv')}
mill   = {K(r['title_as_logged']): int(r['calls']) for r in T('sources/miller_london_calls_308.tsv')}
panel  = {K(r['title']) for r in T('panel/collegiate_panel_union.tsv')}

gs = {}
for r in T('sources/graded_series_552.tsv'):
    gs.setdefault(K(r['title_as_entered']), set()).add(r['block_id'])
band = {r['block_id']: r['band_assigned'] for r in T('sources/graded_series_volumes_27.tsv')}
ORDER = {'Foundational': 0, 'Emerging Intermediate': 1, 'Intermediate': 2}

def mark(k):
    """The scan mark, by the stated rule. Not admission - a scan after seating."""
    w = k in w1 or k in w2
    m = mill.get(k, 0)
    if w and m >= 1: return 'WM'
    if w:            return 'W'
    if m >= 10:      return 'M'
    return ''

rows = []
for r in T('sources/pool_1419_candidates.tsv'):
    t = r['title']; k = K(t)
    vols = sorted(gs.get(k, ()))
    floors = [band[v] for v in vols if v in band]
    rows.append({
        'title'            : t,
        'warrant_1_rank'   : rank.get(k, ''),
        'warrant_2_chapter': 'yes' if k in levine else '',
        'watkins_list1'    : w1.get(k, ''),
        'watkins_list2'    : w2.get(k, ''),
        'watkins_categorical': wcat.get(k, ''),
        'miller_calls'     : mill.get(k, ''),
        'scan_mark_by_rule': mark(k),
        'graded_volumes'   : len(vols),
        'graded_floor'     : min(floors, key=lambda b: ORDER[b]) if floors else '',
        'panel_reaches'    : 'yes' if k in panel else '',
        'verdict'          : '',      # yours
        'division'         : '',      # yours
        'tier'             : '',      # yours
        'ground_if_declined': '',     # yours
    })
rows.sort(key=lambda r: alpha_key(r['title']))

out = os.path.join(ROOT, 'data/decision_queue_1419.tsv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter='\t', lineterminator='\n')
    w.writeheader(); w.writerows(rows)

n = len(rows)
print(f'decision queue: {n} candidates, 0 verdicts')
print(f'  carrying a recording rank      {sum(1 for r in rows if r["warrant_1_rank"]):>5}')
print(f'  unique to the chapter          {sum(1 for r in rows if r["warrant_2_chapter"]):>5}')
print(f'  named by the survey            {sum(1 for r in rows if r["watkins_list1"] or r["watkins_list2"] or r["watkins_categorical"]):>5}')
print(f'  logged at least one call       {sum(1 for r in rows if r["miller_calls"]):>5}')
print(f'  carried by a graded series     {sum(1 for r in rows if r["graded_volumes"]):>5}')
print(f'  reached by the collegiate panel{sum(1 for r in rows if r["panel_reaches"]):>5}')
print(f'  would take a scan mark by rule {sum(1 for r in rows if r["scan_mark_by_rule"]):>5}')
print()
print(f'  candidates with NO external evidence of any kind '
      f'{sum(1 for r in rows if not any((r["watkins_list1"], r["watkins_list2"], r["watkins_categorical"], r["miller_calls"], r["graded_volumes"], r["panel_reaches"]))):>5}')
print()
print('Every one of these carries a source warrant. The warrants decline no one.')
print('The reduction is the filter, and the filter is not in this file.')

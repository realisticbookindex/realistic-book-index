#!/usr/bin/env python3
"""Verification battery for The Realistic Book Index, Draft 15.

    python3 code/verify.py

Every check recomputes a figure the volume prints from the files in this repository
and compares it with the printed value. The script prints one line per check and
exits 0 when every check passes, 1 otherwise. It reads nothing outside the repository
and needs only the Python standard library.
"""
import csv, collections, hashlib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from norm import match_key, alphakey  # noqa: E402
import panel  # noqa: E402

RESULTS = []


def check(name, got, want):
    ok = got == want
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else f"  got {got!r}, printed {want!r}"))


def read(rel):
    with open(os.path.join(ROOT, rel), newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


IDX = ["1A", "1B", "2", "3", "4", "5A", "5B", "5C"]
M = read("data/index_membership_729.tsv")
by_idx = collections.defaultdict(list)
for x in M:
    by_idx[x["index"]].append(x)

# ---------------------------------------------------------------- the Index (TABLE I.2, TABLE R.4)
check("N = 729 [A4]", len(M), 729)
check("tier sizes T1..T6 (93, 53, 116, 141, 99, 227)",
      [len(by_idx[i]) for i in ["1A", "1B", "2", "3", "4"]] + [len(by_idx["5A"]) + len(by_idx["5B"]) + len(by_idx["5C"])],
      [93, 53, 116, 141, 99, 227])
check("vocal bands T6a/T6b/T6c (80, 78, 69)", [len(by_idx[i]) for i in ["5A", "5B", "5C"]], [80, 78, 69])
check("D1 instrumental division = 502", sum(len(by_idx[i]) for i in ["1A", "1B", "2", "3", "4"]), 502)
w = collections.Counter(x["warrant"] for x in M)
check("Route 1: 536 [W1] + 183 [W2] + 0 [W3] + 10 [W4]",
      (w["1 ranking"], w["2 chapter"], w.get("3 guide", 0), w["4 filter"]), (536, 183, 0, 10))
check("A9 retained titles with no rank = 193", sum(1 for x in M if not x["rank"]), 193)
check("the [P] set is the warrant-4 set (TABLE IV.4)",
      sorted((x["index"], x["seat"]) for x in M if x["mark"] == "[P]"),
      sorted((x["index"], x["seat"]) for x in M if x["warrant"] == "4 filter"))
check("[P] by index: Index 2 two, Index 3 five, Index 4 three",
      dict(collections.Counter(x["index"] for x in M if x["mark"] == "[P]")), {"2": 2, "3": 5, "4": 3})
for i in IDX:
    seats = sorted(int(x["seat"]) for x in by_idx[i])
    check(f"Index {i}: seats run 1 to {len(seats)} without a gap", seats, list(range(1, len(seats) + 1)))
bad = []
for i in IDX:
    blocks = collections.defaultdict(list)
    for x in by_idx[i]:
        blocks[x["block"]].append(x)
    for b, v in blocks.items():
        v.sort(key=lambda x: int(x["seat"]))
        keys = [alphakey(x["title"]) for x in v]
        bad += [(i, b, v[k]["title"], v[k + 1]["title"]) for k in range(len(v) - 1) if keys[k] > keys[k + 1]]
check("every run and form block files by FM.1.f", bad, [])
blk = {i: [sum(1 for x in by_idx[i] if x["block"] == b) for b in ["main", "twelve-bar blues", "minor blues", "rhythm changes"]]
       for i in ["1A", "1B", "2", "3"]}
check("form blocks at § VI.5.f (1A 68/16/3/6, 1B 52/0/1/0, 2 91/16/2/7, 3 89/28/8/16)", blk,
      {"1A": [68, 16, 3, 6], "1B": [52, 0, 1, 0], "2": [91, 16, 2, 7], "3": [89, 28, 8, 16]})
check("italic counts M7..M10 (43, 38, 13, 0)",
      [sum(1 for x in by_idx[i] if x["italic"]) for i in ["1A", "1B", "2", "3"]], [43, 38, 13, 0])
check("boldface titles = 36", sum(1 for x in M if x["bold"]), 36)
check("italic only at Indexes 1 to 3, bold only at Index 5",
      (sorted({x["index"] for x in M if x["italic"]}), sorted({x["index"] for x in M if x["bold"]})),
      (["1A", "1B", "2"], ["5A", "5B", "5C"]))

# ---------------------------------------------------------------- bands (TABLE VI.3.b)
def untouched_ground(x):
    if x["rank"]:
        return "rank"
    if x["block"] != "main" and x["index"] in ("2", "3"):
        return "reservation"
    return "nothing"


table = {}
for i in IDX:
    b = collections.Counter(x["band"] for x in by_idx[i])
    u = collections.Counter(untouched_ground(x) for x in by_idx[i] if x["band"] == "Untouched")
    table[i] = [b["Reconciled"], b["Logged"], b["Distilled"], b["Sub-Floor"], u["rank"], u["reservation"], u["nothing"]]
PRINTED_VI3B = {"1A": [79, 7, 5, 2, 0, 0, 0], "1B": [36, 3, 14, 0, 0, 0, 0], "2": [14, 31, 10, 16, 29, 4, 12],
                "3": [0, 19, 1, 18, 12, 25, 66], "4": [5, 8, 2, 7, 73, 0, 4], "5A": [10, 23, 8, 1, 38, 0, 0],
                "5B": [1, 9, 3, 0, 65, 0, 0], "5C": [0, 11, 0, 0, 56, 0, 2]}
for i in IDX:
    check(f"TABLE VI.3.b row {i}", table[i], PRINTED_VI3B[i])
check("TABLE VI.3.b total row (145, 111, 43, 44, 273, 29, 84)",
      [sum(table[i][k] for i in IDX) for k in range(7)], [145, 111, 43, 44, 273, 29, 84])


def band_of(x):
    listed = bool(x["watkins_list1_count"] or x["watkins_list2_count"])
    calls = int(x["logged_calls"])
    if calls and listed:
        return "Reconciled"
    if calls:
        return "Logged"
    if listed:
        return "Distilled"
    if x["watkins_categorical"]:
        return "Sub-Floor"
    return "Untouched"


check("every band follows § VI.3.a from the evidence columns", [x["title"] for x in M if band_of(x) != x["band"]], [])
check("256 titles carry a logged call; 343 are reached",
      (sum(1 for x in M if int(x["logged_calls"])), sum(1 for x in M if x["band"] != "Untouched")), (256, 343))

# ---------------------------------------------------------------- phases (TABLE IV.5.c)
ph = collections.Counter(x["phase"] for x in M if x["phase"])
check("phases 67 + 58 + 49 = 174 [P4]", (ph["Foundational"], ph["Emerging Intermediate"], ph["Intermediate"]), (67, 58, 49))
check("panel sizes at § VI.4 (62, 19, 39, 16, 19, 11, 2, 6)",
      [sum(1 for x in by_idx[i] if x["phase"]) for i in IDX], [62, 19, 39, 16, 19, 11, 2, 6])

# ---------------------------------------------------------------- the two call instruments (§ II, App. K)
ml = read("sources/miller_london_calls_308.tsv")
check("the log carries 2,038 calls on 308 titles", (sum(int(r["calls"]) for r in ml), len(ml)), (2038, 308))
calls_1a = sum(int(x["logged_calls"]) for x in by_idx["1A"])
check("Index 1A carries 1,190 of 2,038 logged calls (58.4 percent)", (calls_1a, round(100 * calls_1a / 2038, 1)), (1190, 58.4))
w1 = read("sources/watkins_2010_list1_92.tsv")
check("Watkins's List 1 prints 92 titles", len(w1), 92)
on_list1 = [x for x in M if x["watkins_list1_count"]]
check("all 92 List 1 titles are seated, 83 of them in Index 1",
      (len(on_list1), sum(1 for x in on_list1 if x["index"] in ("1A", "1B"))), (92, 83))
check("List 1 contributor counts match the source file",
      sorted(int(x["watkins_list1_count"]) for x in on_list1), sorted(int(r["contributors"]) for r in w1))
check("Watkins's List 2 prints 96 titles", len(read("sources/watkins_2010_list2_96.tsv")), 96)

# ---------------------------------------------------------------- residues (TABLE IV.3, App. A to D, App. K.9)
A = read("residues/appendix_A_levine_unique_420.tsv")
B = read("residues/appendix_B_levine_declined_237.tsv")
C = read("residues/appendix_C_ranking_declined_464.tsv")
D = read("residues/appendix_D_gioia_declined_6.tsv")
check("App. A 420 [RA], App. B 237 [RB], App. C 464 [RC], App. D 6 [RD]", (len(A), len(B), len(C), len(D)), (420, 237, 464, 6))
check("App. A: 183 seated on the chapter and 237 declined at App. B",
      (sum(1 for r in A if r["seat"]), sum(1 for r in A if r["declined_at"] == "App. B")), (183, 237))
seated_w2 = sorted(f'{x["index"]} #{x["seat"]}' for x in M if x["warrant"] == "2 chapter")
check("App. A seats are exactly the warrant-2 seats", sorted(r["seat"] for r in A if r["seat"]), seated_w2)
check("App. B titles are the App. A titles marked declined",
      sorted(match_key(r["title_as_printed"]) for r in B), sorted(match_key(r["title_as_printed"]) for r in A if r["declined_at"]))
ranks_seated = sorted(int(x["rank"]) for x in M if x["rank"])
ranks_c = sorted(int(r["rank"]) for r in C)
check("536 seated ranks and 464 App. C ranks partition 1 to 1,000",
      sorted(ranks_seated + ranks_c), list(range(1, 1001)))
check("A5 declines = 237 + 464 = 701", len(B) + len(C), 701)
check("A1 pool = 536 + 464 + 420 = 1,420", len(ranks_seated) + len(C) + len(A), 1420)
check("App. A #353 is Sugar; App. C #345 is Sugar (That Sugar Baby O' Mine)",
      (A[352]["title_as_printed"], C[344]["title_as_printed"]), ("Sugar", "Sugar (That Sugar Baby O' Mine)"))
rk = read("sources/jazzstandards_ranked_1000.tsv")
check("the ranking file carries ranks 1 to 1,000", [int(r["rank"]) for r in rk], list(range(1, 1001)))
title_at = {int(r["rank"]): r["title_as_ranked"] for r in rk}
check("ranking #269 is Sugar (That Sugar Baby O' Mine), declined at App. C",
      (title_at[269], 269 in ranks_c), ("Sugar (That Sugar Baby O' Mine)", True))
check("no title in the ranking's top 100 is declined; nine in the top 200", (sum(1 for r in ranks_c if r <= 100), sum(1 for r in ranks_c if r <= 200)), (0, 9))

# ---------------------------------------------------------------- vocal bands (note under TABLE IV.6)
V = read("data/vocal_band_worksheet_227.tsv")
check("band worksheet has 227 rows", len(V), 227)
check("source counts: 83 triple, 108 double, 36 single",
      [sum(1 for r in V if r["source_count"] == s) for s in "321"], [83, 108, 36])


def median(v):
    v = sorted(v); n = len(v)
    return v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2


def quartile(v, p):
    v = sorted(v); h = (len(v) - 1) * p; lo = int(h); hi = min(lo + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (h - lo)


r3 = [int(r["rank"]) for r in V if r["source_count"] == "3" and r["rank"]]
r2 = [int(r["rank"]) for r in V if r["source_count"] == "2" and r["rank"]]
r1 = [int(r["rank"]) for r in V if r["source_count"] == "1" and r["rank"]]
check("median ranks 114 / 324 / 550.5 (83 / 107 / 34 ranked titles)",
      (median(r3), median(r2), median(r1), len(r3), len(r2), len(r1)), (114, 324, 550.5, 83, 107, 34))
check("interquartile ranges 73 to 180 and 229.5 to 458 (linear)",
      (quartile(r3, .25), quartile(r3, .75), quartile(r2, .25), quartile(r2, .75)), (73.0, 180.0, 229.5, 458.0))
dc = collections.Counter(r["delta"] for r in V)
check("42 screening drops, 1 rank drop (Lotus Blossom), 6 compiler seats",
      (dc["screening drop"], dc["rank drop"], dc["compiler seat above its source-count band"],
       [r["title"] for r in V if r["delta"] == "rank drop"]), (42, 1, 6, ["Lotus Blossom"]))
check("worksheet rows match the membership file",
      sorted((r["division"], r["seat"], match_key(r["title"])) for r in V),
      sorted((x["index"], x["seat"], match_key(x["title"])) for x in M if x["index"].startswith("5")))

# ---------------------------------------------------------------- style classification (§ VI.2.c, § VI.6.b)
S = read("data/style_classification.tsv")
basis = collections.Counter(r["basis"].split(";")[0] for r in S)
check("classified corpus 491 and 29 set-rule entries; pool 520", (basis["classified"], basis["set-rule entry"], len(S)), (491, 29, 520))
check("default pool by index at § VI.6.b (93, 53, 116, 141, 25, 48, 26, 18)",
      [sum(1 for r in S if r["index"] == i) for i in IDX], [93, 53, 116, 141, 25, 48, 26, 18])
reached45 = sorted((x["index"], x["seat"]) for x in M if x["index"] in ("4", "5A", "5B", "5C") and x["band"] != "Untouched")
check("classified titles of Indexes 4 and 5 are exactly the reached titles (88)",
      sorted((r["index"], r["seat"]) for r in S if r["index"] in ("4", "5A", "5B", "5C") and r["basis"].startswith("classified")), reached45)
fixed = sorted((x["index"], x["seat"]) for x in M if (x["index"] == "4" and x["mark"] == "[P]") or
               (x["index"].startswith("5") and x["bold"] and x["band"] == "Untouched"))
check("set-rule entries are the three [P] titles of Index 4 and the 26 boldface titles no instrument reaches",
      sorted((r["index"], r["seat"]) for r in S if r["basis"].startswith("set-rule")), fixed)
vv = collections.Counter((r["index"], r["idiom"]) for r in S if r["index"].startswith("5") and r["basis"].startswith("classified"))
check("vocal style values at Index 5A.1.e, 5B.1.e, 5C.1.e",
      (vv[("5A", "Straight-ahead")], vv[("5A", "Swing")], vv[("5A", "Latin jazz - Brazilian")],
       vv[("5B", "Straight-ahead")], vv[("5B", "Swing")], vv[("5B", "Latin jazz - Afro-Cuban")], vv[("5C", "Straight-ahead")]),
      (35, 6, 1, 11, 1, 1, 11))
check("twelve contested calls at § VI.5.e", len(read("data/style_contested_calls_12.tsv")), 12)

# ---------------------------------------------------------------- name table (FM.6)
NT = read("data/name_table.tsv")
seat_title = {f'{x["index"]} #{x["seat"]}': x["title"] for x in M}
check("every name-table seat resolves to the title it names",
      [r["name_as_it_also_circulates"] for r in NT if match_key(seat_title.get(r["seat"], "")) != match_key(r["seated_as"])], [])
fm6 = [r for r in NT if r["basis"] == "FM.6"]
check("FM.6: fifty-two names, forty-nine compositions", (len(fm6), len({r["seat"] for r in fm6})), (52, 49))

# ---------------------------------------------------------------- the panel (App. H, TABLE IV.8.b, App. L.3)
res = panel.main()
check("panel union under the six rules = 460", res["union"], 460)
check("no title on thirteen or fourteen lists; four on twelve",
      (sum(v for k, v in res["k"].items() if k >= 13), res["k"].get(12, 0)), (0, 4))
check("one program only: 179 (39 percent)", (res["one_program"], round(100 * res["one_program"] / res["union"])), (179, 39))
check("reach by tier at App. H (93, 52, 88, 47, 16, 92)",
      [res["reach"][t] for t in ["1A", "1B", "2", "3", "4", "5"]], [93, 52, 88, 47, 16, 92])
ps = read("panel/panel_sources_14.tsv")
check("fourteen program documents, retrieved 26 August 2026", (len(ps), {r["retrieved"] for r in ps}), (14, {"2026-08-26"}))
check("program title counts 313 down to 31",
      [int(r["titles_as_printed"]) for r in ps], [313, 260, 168, 127, 112, 100, 82, 51, 50, 46, 42, 40, 37, 31])

# ---------------------------------------------------------------- tier pairs (TABLE II.6, TABLE II.7)
TP = {(r["higher_tier"], r["lower_tier"]): r for r in read("data/tier_pair_separation.tsv")}
check("1A / 1B: ranking 47.6, log 22.9, survey 24.0",
      (TP[("1A", "1B")]["ranking_pct"], TP[("1A", "1B")]["log_pct"], TP[("1A", "1B")]["survey_pct"]), ("47.6", "22.9", "24.0"))
check("1A / 5A ranking 56.0; Index 2 / Index 3 ranking 24.6", (TP[("1A", "5A")]["ranking_pct"], TP[("2", "3")]["ranking_pct"]), ("56.0", "24.6"))

# ---------------------------------------------------------------- the call-instrument join (App. E)
# The checks above read the evidence file's own columns. These rebuild the join from
# sources/ back to the seated titles, which is what a replicator does and what the
# columns cannot be asked to confirm about themselves.
from aliases import SEATED, BY_SOURCE  # noqa: E402

FOLD = {match_key(v): match_key(s) for v, s in SEATED.items()}
for _r in read("data/name_table.tsv"):
    FOLD[match_key(_r["name_as_it_also_circulates"])] = match_key(_r["seated_as"])


def jkey(title, source=None):
    """match_key with the declared folds applied, source-scoped folds first."""
    k = match_key(title)
    for v, t in BY_SOURCE.get(source, {}).items():
        if match_key(v) == k:
            return match_key(t)
    return FOLD.get(k, k)


SEATED_KEYS = {jkey(x["title"]) for x in M}
check("the 729 seated titles carry 729 distinct join keys", len(SEATED_KEYS), 729)

for _name, _rel, _n in [
        ("List 1", "sources/watkins_2010_list1_92.tsv", 92),
        ("List 2", "sources/watkins_2010_list2_96.tsv", 96),
        ("graded sequence", "sources/watkins_2010_graded_228.tsv", 193)]:
    _k = {jkey(r["title_as_printed"]) for r in read(_rel)}
    check(f"Watkins's {_name}: {_n} distinct titles, every one joining to a seat",
          (len(_k), len(_k - SEATED_KEYS)), (_n, 0))

WCAT = {jkey(r["title_as_printed"]) for r in read("sources/watkins_2010_categorical_137.tsv")}
MILL = {jkey(r["title_as_logged"]) for r in read("sources/miller_london_calls_308.tsv")}
MILL |= {jkey(r["title_as_printed"]) for r in read("sources/miller_published_201.tsv")}
w_only, m_only, both = WCAT - SEATED_KEYS - MILL, MILL - SEATED_KEYS - WCAT, (WCAT & MILL) - SEATED_KEYS
check("App. E: 39 reach the survey alone, 46 the log alone, 6 both, 91 in all",
      (len(w_only), len(m_only), len(both), len((WCAT | MILL) - SEATED_KEYS)), (39, 46, 6, 91))
RB = {jkey(r["title_as_printed"]) for r in read("residues/appendix_B_levine_declined_237.tsv")}
RC0 = {jkey(r["title_as_printed"]) for r in read("residues/appendix_C_ranking_declined_464.tsv")}
_unseated = (WCAT | MILL) - SEATED_KEYS
check("App. E: 27 of the 91 print as declines, 64 never entered the pool",
      (len(_unseated & (RB | RC0)), len(_unseated - RB - RC0)), (27, 64))
_ml = read("sources/miller_london_calls_308.tsv")
check("the log: 2,038 calls on 308 titles; the 46 it reaches alone carry 148",
      (sum(int(r["calls"]) for r in _ml), len(_ml),
       sum(int(r["calls"]) for r in _ml if jkey(r["title_as_logged"]) in m_only)), (2038, 308, 148))

RESIDUE_KEYS = SEATED_KEYS | {jkey(r["title_as_printed"]) for rel in
                              ["residues/appendix_A_levine_unique_420.tsv",
                               "residues/appendix_B_levine_declined_237.tsv",
                               "residues/appendix_C_ranking_declined_464.tsv",
                               "residues/appendix_D_gioia_declined_6.tsv"] for r in read(rel)}
_NT = read("data/name_table.tsv")
check("every declared fold resolves to a seated or a printed-residue title",
      sorted(set(list(SEATED.values()) + [r["seated_as"] for r in _NT]
                 + [t for m in BY_SOURCE.values() for t in m.values()])
             - {v for v in list(SEATED.values()) + [r["seated_as"] for r in _NT]
                + [t for m in BY_SOURCE.values() for t in m.values()]
                if match_key(v) in RESIDUE_KEYS}), [])
check("no fold points at another fold's source, which would make the join order matter",
      sorted(v for v in list(SEATED.values()) + [r["seated_as"] for r in _NT]
             if match_key(v) in FOLD and FOLD[match_key(v)] != match_key(v)), [])
_SEATOF = {jkey(x["title"]): x["index"] + " #" + x["seat"] for x in M}
check("the name table's 133 seat addresses all agree with the roster",
      (len(_NT), sorted(r["name_as_it_also_circulates"] for r in _NT
                        if _SEATOF.get(jkey(r["seated_as"])) != r["seat"])), (133, []))

# The chapter and the guide are not in this repository (App. J Rule 13), so their presence
# columns cannot be rebuilt from a source file. They can be held against each other.
EJ = {r["title"]: r for r in read("data/evidence_join_729.tsv")}
check("the two data files agree on every seat", sorted(EJ) == sorted(x["title"] for x in M), True)
check("in_guide and guide_form agree on all 729 seats, at 258 present",
      (sorted(x["title"] for x in M if bool(x["in_guide"].strip()) != bool(EJ[x["title"]]["guide_form"].strip())),
       sum(1 for x in M if x["in_guide"].strip())), ([], 258))
check("in_chapter and chapter_form agree on all 729 seats, at 183 warrant 2 plus the overlap",
      sorted(x["title"] for x in M if bool(x["in_chapter"].strip()) != bool(EJ[x["title"]]["chapter_form"].strip())), [])

RANKED = {jkey(r["title_as_ranked"]) for r in read("sources/jazzstandards_ranked_1000.tsv")}
RC = {jkey(r["title_as_printed"]) for r in read("residues/appendix_C_ranking_declined_464.tsv")}
check("Rule 9, from the ranking file: 536 seated + 464 declined = 1,000, disjoint",
      (len(RANKED & SEATED_KEYS), len(RANKED & RC), len(RC & SEATED_KEYS), len(RANKED)),
      (536, 464, 0, 1000))

# ------------------------------------------------- the style file's ballad column (tool input)
# Not an apparatus figure. No count in the volume depends on it and no mark prints for it.
# It is declared here so it is recountable rather than only asserted, like the rest of the file.
SC = read("data/style_classification.tsv")
_SEATS = {(x["index"], x["seat"]) for x in M}
check("the style file's ballad column: 75 marks, all on seated rows, no other value",
      (len(SC),
       sum(1 for r in SC if r["ballad"] == "Y"),
       sorted({r["ballad"] for r in SC} - {"Y", ""}),
       sorted(r["title"] for r in SC if r["ballad"] == "Y" and (r["index"], r["seat"]) not in _SEATS)),
      (520, 75, [], []))

# --------------------------------------------- the set builder's Index 4 extension (tool input)
# Also not an apparatus figure. The volume's style page classifies 491 titles and stops; this
# file carries a reading of the 74 Index 4 seats it does not reach, for the set builder alone.
# It is kept out of style_classification.tsv so that VI.2.c's 491 and 520 stay true of that file.
EXT = read("data/setbuilder_extension.tsv")
_SC_SEATS = {(r["index"], r["seat"]) for r in SC}
check("the set-builder extension: 74 Index 4 seats, all seated, none already classified",
      (len(EXT),
       sorted({r["index"] for r in EXT}),
       sorted(r["title"] for r in EXT if (r["index"], r["seat"]) not in _SEATS),
       sorted(r["title"] for r in EXT if (r["index"], r["seat"]) in _SC_SEATS),
       sorted({r["ballad"] for r in EXT} - {"Y", ""})),
      (74, ["4"], [], [], []))
check("the extension and the style file together cover all 99 Index 4 seats",
      sorted([int(r["seat"]) for r in EXT] + [int(r["seat"]) for r in SC if r["index"] == "4"]),
      sorted(int(x["seat"]) for x in M if x["index"] == "4"))

# ------------------------------------------- the set builder's vocal-option file (tool input)
# The third reading that is not in the volume. Instrumental seats at Indexes 1 to 3 carrying a
# lyric a singer can front. All four instrumental indexes. No printed count uses it.
VO = read("data/vocal_option.tsv")
check("the vocal-option file: 44 rows across all four instrumental indexes, all seated, no duplicate seat",
      (len(VO),
       sorted({r["index"] for r in VO}),
       sorted(r["title"] for r in VO if (r["index"], r["seat"]) not in _SEATS),
       len(VO) - len({(r["index"], r["seat"]) for r in VO})),
      (44, ["1A", "1B", "2", "3"], [], 0))
check("its titles match the roster at those seats",
      sorted(r["title"] for r in VO
             if r["title"] != {(x["index"], x["seat"]): x["title"] for x in M}.get((r["index"], r["seat"]))),
      [])

# ---------------------------------------------------------------- the prompt (App. J Rule 13)
pp = os.path.join(ROOT, "prompts", "rule_13_screening_prompt.txt")
raw = open(pp, "rb").read()
sums = dict(line.split("  ")[::-1] for line in open(os.path.join(ROOT, "prompts", "SHA256SUMS")).read().splitlines() if line)
check("prompt SHA-256 matches SHA256SUMS", hashlib.sha256(raw).hexdigest(), sums.get("rule_13_screening_prompt.txt"))
check("prompt is plain ASCII, opens [BEGIN PROMPT], closes [/END PROMPT] and one newline",
      (all(b < 128 for b in raw), raw.startswith(b"[BEGIN PROMPT]"), raw.endswith(b"[/END PROMPT]\n")), (True, True, True))

print(f"\n{sum(RESULTS)} of {len(RESULTS)} checks pass")
sys.exit(0 if all(RESULTS) else 1)

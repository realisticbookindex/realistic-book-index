"""Rebuild the fourteen-program union and its k-counts from the pooled row file, and
count what the union reaches in each tier of the Index.

    python3 code/panel.py            # prints the summary
    python3 code/panel.py --write    # also writes panel/panel_union_k.tsv
"""
import csv, os, sys, collections, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from norm import match_key
from aliases import SEATED

# Folding rules (panel/FOLDING_RULES.md). Applied to the normalized column.
FOLD = {
    "misty i want to talk about you": "misty",               # rule 3: one option row, Misty only
    "in a mellotone": "in a mellow tone",                     # rule 4
    "autumn leaves em and gm": "autumn leaves",               # rule 1: performance keys
    "just friends f and g": "just friends",
    "on green dolphin street c and eb": "on green dolphin street",
    "round midnight monk changes": "round midnight",
    "samba de orfeo": "samba de orfeu",                        # rule 7: one-letter variants
    "the more i see you": "more i see you",
    "goodbye porkpie hat": "goodbye pork pie hat",
    "daydream": "day dream",
    "what a difference a day": "what a difference a day made",
    "unless its you a k a orbit": "unless its you",
}
NOT_TITLES = {"university jazz studies", "program", "bb rhythm changes"}   # page furniture; a form entry


def pooled_rows():
    with open(os.path.join(ROOT, "panel", "panel_rows_pooled.tsv"), newline="") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            yield r


def row_key(r):
    n = r["normalized"].strip()
    if r["institution"] == "Western Michigan" and r["title_as_printed"] == "Milestones (Old)":
        n = "milestones old"                                   # rule 5: the source row was normalized without its qualifier
    return match_key(FOLD.get(n, n))


def union():
    u = collections.defaultdict(set)
    forms = collections.defaultdict(set)
    for r in pooled_rows():
        if r["institution"] == "Marshall" and r["section"].startswith("entrance"):
            continue                                           # rule 8: Marshall pp. 17-18 only
        if r["normalized"] in NOT_TITLES:
            continue
        k = row_key(r)
        u[k].add(r["institution"])
        forms[k].add(r["title_as_printed"])
    return u, forms


def seated_lookup():
    seat = {}
    with open(os.path.join(ROOT, "data", "index_membership_729.tsv"), newline="") as f:
        for x in csv.DictReader(f, delimiter="\t"):
            seat.setdefault(match_key(x["title"]), (x["index"], int(x["seat"]), x["title"]))
    alias = {match_key(a): match_key(b) for a, b in SEATED.items()}
    def find(k):
        if k in alias and alias[k] in seat:
            return seat[alias[k]]
        return seat.get(k)
    return find


def tier_of(index):
    return "5" if index.startswith("5") else index


def main(write=False):
    u, forms = union()
    find = seated_lookup()
    kc = collections.Counter(len(v) for v in u.values())
    reach = collections.defaultdict(set)
    rows = []
    for k in sorted(u):
        hit = find(k)
        if hit:
            reach[tier_of(hit[0])].add((hit[0], hit[1]))
        rows.append((k, len(u[k]), "; ".join(sorted(u[k])), " | ".join(sorted(forms[k])),
                     "" if not hit else f"{hit[0]} #{hit[1]}", "" if not hit else hit[2]))
    out = {
        "union": len(u),
        "k": dict(sorted(kc.items(), reverse=True)),
        "one_program": kc[1],
        "at_twelve_or_more": sorted(k for k, v in u.items() if len(v) >= 12),
        "reach": {t: len(reach[t]) for t in ["1A", "1B", "2", "3", "4", "5"]},
    }
    if write:
        with open(os.path.join(ROOT, "panel", "panel_union_k.tsv"), "w", newline="") as f:
            w = csv.writer(f, delimiter="\t", lineterminator="\n")
            w.writerow(["match_key", "k_programs", "programs", "printed_forms", "seat", "seated_as"])
            w.writerows(rows)
    return out


if __name__ == "__main__":
    res = main(write="--write" in sys.argv)
    for k, v in res.items():
        print(f"{k}: {v}")

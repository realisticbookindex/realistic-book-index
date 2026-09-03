"""The alphabetical convention used by every source file in this repository.

Each source file here presents its rows alphabetically by title. Whatever ordering
datum the source itself carries - a recording rank, a call count, a contributor
count - travels as a column rather than as the sequence of the file.

The convention, in order of application:
  - case is folded, and a curly apostrophe is read as a straight one
  - a trailing article is rotated back ("Man I Love, The" reads as "The Man I Love")
  - a leading article is dropped, so "An Affair to Remember" files under Affair
  - a run of digits compares as a number, so 9:20 precedes 12th Street precedes 26-2
  - anything outside [a-z0-9 ] is deleted and interior spaces are kept, so
    A-Tisket files as "atisket" and lands between "At the Jazz Band Ball" and
    "Au Privave", and Senor Blues files as "seor blues" and lands between
    "Sentimental Journey" and "September in the Rain"
  - a parenthetical is retained, so "(Meet) The Flintstones" files under Meet

code/verify.py asserts that every source file is in this order. The convention
reproduces sources/pool_1419_alphabetical.tsv row for row, which is where it was
first set.
"""
import re

def alpha_key(t):
    s = t.replace('’', "'").replace('‘', "'").lower().strip()
    m = re.match(r"^(.*),\s*(the|a|an)$", s)
    if m: s = m.group(2) + ' ' + m.group(1)
    s = re.sub(r'^(the|a|an)\s+', '', s)
    s = s.replace('&', ' and ')
    out = []
    for p in re.split(r'(\d+)', s):
        if p.isdigit():
            out.append((0, int(p), ''))
        else:
            out.append((1, 0, re.sub(r' +', ' ', re.sub(r'[^a-z0-9 ]', '', p))))
    return tuple(out)

def in_alpha_order(titles):
    k = [alpha_key(t) for t in titles]
    return all(a <= b for a, b in zip(k, k[1:]))

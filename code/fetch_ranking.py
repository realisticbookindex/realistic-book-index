#!/usr/bin/env python3
"""
Rebuild sources/jazzstandards_ranked_1000.tsv from the published index pages.

The ranking is another party's compilation. This script documents exactly how the
copy in this repository was assembled so that a replicator can rebuild it from the
source rather than inherit it, and can date their own retrieval.

The ten pages are:
    https://www.jazzstandards.com/compositions/index.htm     ranks 1-100
    https://www.jazzstandards.com/compositions/index2.htm    ranks 101-200
    ...
    https://www.jazzstandards.com/compositions/index10.htm   ranks 901-1000

Fetch each, take the ranked title list in order, and write "rank<TAB>title".
Check your result with:  python3 code/verify.py
which asserts 1,000 rows and ranks 1..1000 with no gaps.

Observe the site's terms when taking them, and record your own access date.
The copy here was retrieved 2 September 2026.
"""
URLS = ["https://www.jazzstandards.com/compositions/index.htm"] + [
    f"https://www.jazzstandards.com/compositions/index{i}.htm" for i in range(2, 11)]

if __name__ == "__main__":
    print(__doc__)
    for i, u in enumerate(URLS):
        print(f"  ranks {i*100+1:>4}-{i*100+100:<4}  {u}")

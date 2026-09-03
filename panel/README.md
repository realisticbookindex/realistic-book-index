# The fourteen-program collegiate panel

Fourteen degree-granting jazz programs publish a list of tunes their students are required or
expected to know. They were retrieved on one day, **26 August 2026**, and pooled. The panel was
consulted after the Index closed. **It admitted no title, and warrant 4b is asserted for none.**

| file | what it is |
|---|---|
| `collegiate_panel_sources.tsv` | the fourteen programs: institution, document, URL, format, printed row and title counts, retrieval date, and any folding note that applies to that document |
| `collegiate_panel_union.tsv` | the pooled titles, one row each, with how many programs carry it, which tier and which numbered entry of the Index it lands on, which programs list it, and every printed form it appears under |

## What the panel shows

No title is required by all fourteen programs, or by thirteen. Three titles reach twelve, and that
is the ceiling. Roughly two in five appear at one school only. Agreement across programs is a set
intersection, so adding programs can only remove titles from the shared set and never add one; a
larger panel makes non-convergence more true rather than less.

Reach into the Index, counted in seats:

| tier | seats | reached |
|---|---|---|
| List 1A | 93 | 93 |
| List 1B | 53 | 52 |
| List 2 | 116 | 87 |
| List 3 | 141 | 47 |
| List 4 | 99 | 16 |
| List 5 | 227 | 88 |

Reach rises with panel size by construction, so the List 3 and List 4 figures are floors and not
estimates. List 1A is saturated by the eighth program; List 3 is still climbing at the fourteenth.

**Seats, not lines.** `index_entry` names the numbered entry a panel title lands on, and two panel
titles can land on one entry. List 1A takes **94** panel titles into **93** seats, because
*A Day In The Life Of A Fool* and *Black Orpheus* are both List 1A #31. Counting lines rather than
seats is what produced the printed figure of 132 into a tier of 93, and the column is here so that
the two counts cannot be confused again.

## The honest note on the union count

**The volume prints the union as 462. This file returns 486, and the difference has been narrowed
but not closed.**

The row scope reconciles exactly. The panel row file holds 1,533 rows; the folding rules count
Marshall at pp. 17-18 only, which is its 114 `listed` rows and excludes 37 audition-suggestion
rows. 1,533 minus 37 is **1,496**, which is the printed row total to the row.

What does not reconcile is the folding. This file applies the Index's own alias map, published at
`code/aliases.py`, and returns 486. Applying instead the six folding rules the volume declares for
the panel returns 490. Reaching 462 requires roughly twenty-four folds beyond the six that are
stated. **The rules table is incomplete rather than wrong**, and the missing folds are recoverable
from this file: sort by `printed_forms` and the candidates are the rows carrying more than one
form. The volume states the achievable band as 455 to 486; this file sits at the top of it.

Four statements survive every count in that band, and they are the only ones the volume rests on:
no title on all fourteen or thirteen, roughly two in five at one school, the reach ordering across
tiers, and warrant 4b asserted for no title.

## Reproducing this

The fourteen documents are at the URLs in `collegiate_panel_sources.tsv`. They are living pages
and PDFs; several will have changed since 26 August 2026. **Re-retrieve and re-date rather than
inheriting this snapshot.** A replication that pools its own fourteen and reaches the same shape
is worth more than one that reuses these rows.

List length is uncontrolled here: a 313-title program handbook and a 31-title audition sheet cast
equal votes. That is a limitation of the material rather than a choice, and it is stated so that a
replicator can correct for it if they wish.

`code/verify.py` tests the six panel figures above against this file.

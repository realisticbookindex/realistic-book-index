# The Realistic Book Index - replication data

Data and code sufficient to reproduce every figure in *The Realistic Book Index*, and to
run the same process against a different pool and reach a different answer.

The volume's argument is that a filtered repertoire list is only worth reading if its
rejections are printed and its arithmetic closes. This repository is that claim in
machine-readable form. **Every count in the book is re-derived here from the files in
`data/`, `sources/` and `residues/`, and the script reports pass or fail.**

```
python3 code/verify.py
```

61 checks. Exit status 0 if all pass.

---

## What the Index is

Three published sources form a candidate pool of **1,419** titles: a recording-frequency
ranking of 1,000, Mark Levine's repertoire chapter (964 titles, 419 of them absent from the
ranking), and Ted Gioia's critical survey (266, of which 265 resolve into the pool and none
enters on Gioia alone).

A declared practitioner filter reduces that pool to **729** retained titles in five lists and
two divisions, and declines **700**, every one of which is printed by name.

The total closes three ways, from columns not formed from each other:

```
by warrant     537 + 182 + 0 + 10                    = 729
by tier        93 + 53 + 116 + 141 + 99 + 227        = 729
by division    502 + 227                             = 729

residues       537 + 463 = 1,000        182 + 237 = 419
```

Two practitioner instruments were opened **after** the Index closed and admit nothing:
a 2010 survey of thirty-seven US educator-performers, and a log of 2,038 calls across 160
London sessions from 2019. Both are in `sources/`.

---

## Layout

```
data/         the Index and everything derived from it
sources/      the source lists as keyed for this project
residues/     the four printed residues - what the method rejected
panel/        the fourteen collegiate programs, their URLs, and the pooled titles
prompts/      the three prompts the method runs on, and the filter card you fill in
csv/          the same tables as .csv, for double-clicking
code/         normalization, the alias map, the sort convention, and the verification battery
SOURCES.md    where every source came from and how to get it yourself
```

**Three formats, same data.** The `.tsv` files are canonical and are what `verify.py` reads;
tab-separated because many of these titles contain commas. GitHub renders both `.tsv` and `.csv`
as sortable tables in the browser, so nothing needs downloading to be read. If you want the files
on your own machine, take the `csv/` copies, which open on a double-click anywhere, or the single
`RBI_replication_data.xlsx` workbook, which carries every table as a named sheet and needs no
delimiter or encoding decision from you.

### `data/`

| file | rows | what it is |
|---|---|---|
| `index_membership_729.tsv` | 729 | one row per seated title: tier, entry number, the scan mark as printed, the scan mark the stated rule returns, whether they agree, and the raw evidence columns |
| `evidence_join_819.tsv` | 819 | the Index joined to both call instruments, **plus every title either instrument names that the Index does not carry**. `seat_d103` is `-` for those |
| `tier_pair_separation.tsv` | 12 | for each pair of tiers, the share of title-against-title comparisons in which the lower tier comes out ahead, by each of three measures. Ties count as half, so 50 means the measure does not separate the two tiers |
| `priority_list1.tsv` … `priority_lists4_5.tsv` | 146 / 91 / 38 / 30 | the practice-order pages: which titles any external measure reaches, and in what order |

### `sources/`

**Every file here presents alphabetically by title.** The ordering datum a source carries - a
recording rank, a call count, a contributor count - travels as a column rather than as the
sequence of the file, so no file in this directory reproduces the arrangement of the compilation
it was keyed from. `code/alpha.py` states the convention, `code/verify.py` asserts it, and
`SOURCES.md` says what that does and does not settle. Sorting a file on its datum column puts
the source's order back, which is intended: the ranks are here because the volume's closing
finding cannot be checked without them.

### `sources/pool_1419_alphabetical.tsv`

**Two versions of the pool ship here, and which one you take matters.**
`sources/pool_1419_candidates.tsv` is the 1,419 titles and nothing else - no disposition column,
so it does not tell a screener what this edition decided. **That is the one to screen from.** The
file described next carries the answers and is for comparing afterward.

`sources/pool_1419_alphabetical.tsv` is the candidate pool: all 1,419 titles in one
alphabetical sequence with each title's disposition, retained to a list or declined. It is a
merge of three sources rather than a reproduction of any one of them, it carries no column
saying which source a title came from, and the arrangement is mechanical. It is the file a
replicator needs in order to run the screening step without first acquiring all three sources.
It closes independently: 719 retained and 700 declined, which is A6 and A5.

### `residues/`

The four appendices of rejected titles, which are the part of the method most worth
attacking and are therefore printed in full.

| file | rows |
|---|---|
| `appendix_A_levine_unique_419.tsv` | 419 Levine titles absent from the ranking, the set assessed |
| `appendix_B_levine_declined_237.tsv` | 237 of those declined |
| `appendix_C_ranking_declined_463.tsv` | 463 ranked titles declined |
| `appendix_D_gioia_declined_6.tsv` | 6 Gioia titles not retained |

`B + C = 700`, the declined total. Appendix D is a cross-reference: all six also appear in
Appendix C, so adding D again double-counts.

`residues/all_700_declined.tsv` is all of them in one alphabetical sequence, with which
appendix each came from, its rank where it has one, and whether either call instrument
reaches it. **464 of the 700 carry a recording rank, 21 appear in the London log, and 8 carry
any reference in the survey.** This is the file to search when you want to know why a
particular title is not in the Index.

### `prompts/`

**The data lets you check this edition. The prompts let you build your own.** Three, in the order
they run: the screening prompt that seats titles, the skill-path prompt that assigns practice
phases, and the listening prompt that returns recordings stage by stage. Plus
`filter_card_TEMPLATE.md`, which is the one part of the method a replicator has to write.

Start at `prompts/README.md`. It carries the running order, what to attach at each step, the four
printed defects reproduced rather than repaired, and the reason not to close your arithmetic to
this edition's 729.

### Three files handle title variance, and they are not interchangeable

Two lists of jazz standards disagree about punctuation, articles, alternate names and spelling
before they disagree about anything that matters. Three files here address that, each answering a
different question.

| file | question it answers | scope |
|---|---|---|
| `code/aliases.py` | *what does the code fold together?* | 27 folds, the operative map every join in this repository applies |
| `sources/title_anomalies.tsv` | *why did the join behave that way?* | 453 rows, 200 compositions - every hazard across every source, **including the ones that did not resolve** |
| `sources/title_alias_index.tsv` | *where does this name land?* | 124 rows, 84 compositions - name to seat, seated titles only |

**The register is the audit trail and the index is the finding aid.** The register carries what
the index cannot: 8 refused joins, which are pairs that look alike and are *not* the same
composition; 3 cases of one name over two works; 3 source defects; 4 extraction hazards. Putting
a refused join in an alias index would assert the opposite of what the register found. It also
covers the 44 rows that concern declined or source-only titles, which have no seat to point at.

`verify.py` asserts the index is derived from the register, that every row lands on a real seat,
and that no refused join appears in it.

### `code/build_queue.py` - the mechanical half, run in one command

```
python3 code/build_queue.py     ->  data/decision_queue_1419.tsv
```

**1,419 candidates, every machine-derivable fact attached, and no verdict on any of them.**
Recording rank, chapter presence, both call instruments, the graded-series floor, what the
collegiate panel reaches, and the scan mark the stated rule returns. Four columns are left empty
because they are not derivable: `verdict`, `division`, `tier`, `ground_if_declined`.

**This is where automation stops, and the reason is the volume's whole argument.** Every one of
the 1,419 carries a source warrant, because the pool *is* the union of the three warrant sources.
Warrant checking therefore declines no one. **The reduction from 1,419 to a seated Index is the
practitioner filter doing all of it**, and the filter is one player's observation of call
likelihood - the step Rule 5 says cannot be inherited.

What that buys a replicator is the whole clerical burden, gone. What it cannot buy is a single
decline.

**856 of the 1,419 carry no external evidence of any kind** - no survey mention, no logged call,
no graded series, no collegiate list. On those, the filter is not one signal among several. It is
the only one.

### The skill path, and how to rebuild it from scratch

Rule 13B assigns practice phases against a floor of graded pedagogical series. Two files carry
that floor, so a replicator can run the phase pass without owning seventeen books.

| file | rows | what it is |
|---|---|---|
| `sources/graded_series_volumes_27.tsv` | 27 | every volume: publisher, work, volume, title count, the band this edition assigned it, and its ISBN or catalogue number |
| `sources/graded_series_552.tsv` | 552 | every title in every one of those volumes, with the seat it lands on in this Index, or `declined`, or `outside` |

**453 distinct compositions.** 170 are seated here, 34 were declined and print at a residue, and
249 never entered the pool at all. That last figure is the one to read carefully: a graded series
teaches ensemble literature and educational originals alongside standards, and this Index counts
what gets called. **The two populations overlap on the standards and diverge everywhere else, and
the divergence is the measurement rather than a miss.**

Per-volume reach runs from 94 percent (Hal Leonard *Easy Jazz Play-Along* vol 2) to zero (Sher
*Latin Real Easy Book* Part 2). **A play-along teaches the repertoire; a school ensemble method
teaches the ensemble.** The two ends of that range are two different kinds of book.

**None of this grants a warrant.** TABLE V.2 in the volume says so and Rule 13B repeats it: these
sources inform the stratification and admit no title.

### `panel/`

Fourteen degree-granting jazz programs that publish a required or expected repertoire list,
retrieved on one day, 26 August 2026. The panel was consulted after the Index closed. **It
admitted no title.**

| file | rows |
|---|---|
| `collegiate_panel_sources.tsv` | the fourteen programs, with the document, its URL, format, printed row and title counts, and any folding note |
| `collegiate_panel_union.tsv` | 486 pooled titles, each with how many programs carry it, the numbered Index entry it lands on, which programs list it, and every printed form |

The fourteen URLs are live documents and several will have changed. **Re-retrieve and re-date
rather than inheriting this snapshot.**

`index_entry` names a seat, not a string. Two panel titles can land on one seat, which is how a
line count can exceed the size of the tier it is counting into. `panel/README.md` carries the
scope reconciliation, the reason this file returns 486 where the volume prints 462, and the four
statements that survive every count in that band.

---

## The join rules, which is where a replication will diverge first

Title matching is the whole problem. Two lists of jazz standards will disagree on
punctuation, articles, alternate titles and spelling before they disagree on anything that
matters. `code/norm.py` is the normalizer used throughout and `code/aliases.py` is the
complete fold list.

`norm.base()` strips bracketed marks and parentheticals, folds curly quotes, strips
diacritics, moves a trailing article to the front (`Theme, The` → `The Theme`), expands `&`,
`Mr.` and `St.`, drops a leading article, and reduces to lowercase alphanumerics.
`norm.full()` is the same but keeps what is inside the parentheses, so that
`Milestones (old)` and `Milestones (new)` stay distinct.

`sources/title_anomalies.tsv` is the register of everything that can go wrong here, in one
machine-readable file. 453 rows, six classes, and a `resolved_by` column saying whether your
normalizer already handles a case or whether you have to hard-code it.

| class | rows | what it is |
|---|---|---|
| `variant form` | 409 | **187 compositions are printed more than one way across the sources.** Each printed form gets a row against the key it folds to |
| `declared fold` | 26 | the alias map, as data |
| `refused join` | 8 | pairs close enough that a fuzzy matcher takes them, and must not |
| `extraction hazard` | 4 | long AKA parentheticals that wrap across printed columns and truncate silently |
| `one name, two works` | 3 | *Milestones*, and the unresolved *The Theme* |
| `source defect` | 3 | counts a published source prints below its own stated floor |

Of the 409 variant forms, **380 resolve by normalization alone and 28 do not.** Those 28 are the
ones that will silently cost you titles: *Black Orpheus* against *Manha De Carnaval*, *Wee* against
*Allen's Alley*, *Chega De Saudade* against *No More Blues*, *Unit 7* against *Unit Seven*, *Take 5*
against *Take Five*, *In A Mellow Tone* against *In a Mellotone*, *Georgia* against *Georgia on My
Mind*. Sort the file by `resolved_by` and the hard cases come to the top.

**Twenty-five folds cannot be derived and are declared** in `aliases.py` - among them
`Black Orpheus` → `Manha De Carnaval`, `Wee` → `Allen's Alley`, `No Blues` → `Pfrancing`,
`Chega de Saudade` → `No More Blues`, and `My Secret Love` → `Secret Love`. A replicator who
does not apply these will not reproduce the counts, and the difference is not small.

**One join must be refused:** Miller's `I Love You` is not the log's `P.S. I Love You`, and a
fuzzy matcher will take it.

**One collision is disclosed rather than resolved:** this Index holds the 1947 bebop line and
the 1958 modal composition as two titles both named *Milestones*. Watkins prints his entry as
*Milestones (new)*, so one instrument makes the same distinction and the other does not. The
verification script reports this as the single case where a printed decline shares a key with
a seated title.

---

## Reproducing the headline figures

Each of these is a check in `code/verify.py` and can be recomputed by hand from the files.

| figure | where it comes from |
|---|---|
| List 1A is 12.8% of the Index and absorbs **58.4%** of 2,038 logged calls | `evidence_join_819.tsv`, sum `miller_calls` by `seat_d103` |
| **All 92** titles on Watkins's first list are seated; 83 in List 1 | `watkins_2010_list1_92.tsv` joined to the membership file |
| **All 92** also appear on Miller's published Top 201 - nine years, two countries, no citation between them | `watkins_2010_list1_92.tsv` and `miller_published_201.tsv` |
| Watkins's four-year sequence carries 193 distinct titles; **every one is in the Index** | `watkins_2010_graded_228.tsv` |
| Of 699 testable declines, **21** appear in the log carrying **56 of 2,038** calls, and **none** sits on a Watkins printed list | residues joined to the log |
| **No title in the ranking's top 100 is declined**; nine in the top 200 are, the first at rank 142 | `jazzstandards_ranked_1000.tsv` and the residues |
| Recording rank cannot resolve the 1A / 1B line (**47.6%**) and reverses at the vocal division (**56.0%**) | `tier_pair_separation.tsv` |

---

## Running the process yourself

The point of publishing this is not that you should agree with the result. It is that the
method can be re-run.

1. Build your own pool from `SOURCES.md`. Substitutions are permitted and should be declared.
2. Write your own practitioner filter: the settings, scenes, period and instrument your
   call-likelihood judgments are drawn from. This step is unverifiable by construction, in
   this volume and in yours. Declaring it does not make it verifiable; it makes it legible.
3. Screen the pool. Print your residue in full.
4. Close your arithmetic by at least two independent routes. **Do not close to 729.** A run
   that lands on this edition's total has adopted this edition's declarations in place of its
   own, which makes it a weaker run and not a confirmation.
5. Run the two call instruments against your result afterward. They admit nothing. What they
   report is agreement or divergence, and divergence is the more interesting result.

---

## What this repository does not contain

Levine's chapter 21 and Gioia's survey are books. Their title lists are not reproduced here.
`residues/appendix_A_levine_unique_419.tsv` carries the 419 Levine titles absent from the
ranking, because that set is this project's own derivation and is printed in the volume, but
the full 964 is not here and has to be taken from the book. `SOURCES.md` gives the ISBN, the
page range and the extraction method.

The fourteen collegiate documents are not here either, though their pooled titles are, at
`panel/`. They were retrieved on one day in 2026 from live web pages and PDFs, and a replication
should re-retrieve and re-date rather than inherit a snapshot.

**The graded pedagogical series are treated the other way, and the difference is deliberate.**
Their contents are published in full at `sources/graded_series_552.tsv`, because a print edition
with an ISBN does not change between retrievals: a replicator can buy any of the 27 volumes and
check the transcription line by line, which is what `sources/graded_series_volumes_27.tsv` exists
to make possible. A collegiate program's web page offers no such fixed thing to check against.
**Snapshot a living document and you have a claim about one day; transcribe a fixed edition and
you have a claim anyone can audit.**

Appendix G, the contrafact corpus, is the volume's own apparatus rather than a source and is not
published here. Stage 4 of the listening prompt is unavailable without it, and that prompt is
written to say so rather than to guess.

---

## License

Three different things live here and they are licensed three different ways, because only two
of them are this project's to license.

| | license |
|---|---|
| the code in `code/` | MIT - see `LICENSE` |
| the data this project produced: `data/`, `residues/`, `csv/`, the workbook, the pool and the anomaly register | CC BY 4.0 - see `LICENSE-DATA` |
| the transcribed source lists in `sources/` | not licensed here; attributed in `SOURCES.md`, take them from the source |

Attribution is the only condition on the data. Use it, change it, publish a different answer
from it - that is what it is for. Say where it came from.

## Attribution

The ranking, the survey and the call log are other people's work and are cited in full at
`SOURCES.md`. The keyings in `sources/` are transcriptions made for this project; where a
count in one of them differs from the published source, **the published source governs** and
the difference should be reported. Two known instances are documented in `SOURCES.md`.

Everything in `data/`, `residues/` and `code/` is the work of this project.

Corrections that reach the author before a later edition will be recorded with attribution to
whoever found them.

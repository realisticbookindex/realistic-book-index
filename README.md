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
csv/          the same tables as .csv, for double-clicking
code/         normalization, the alias map, and the verification battery
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

### `sources/pool_1419_alphabetical.tsv`

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


---

## Attribution

The ranking, the survey and the call log are other people's work and are cited in full at
`SOURCES.md`. The keyings in `sources/` are transcriptions made for this project; where a
count in one of them differs from the published source, **the published source governs** and
the difference should be reported. Two known instances are documented in `SOURCES.md`.

Everything in `data/`, `residues/` and `code/` is the work of this project.

Corrections that reach the author before a later edition will be recorded with attribution to
whoever found them.

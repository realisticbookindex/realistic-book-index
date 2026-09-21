# The Realistic Book Index - replication materials, Draft 15

This repository holds the files *The Realistic Book Index* (Draft 15) sends a reader to, and a script that recomputes the volume's figures from them. The volume's claim is that a filtered repertoire index is worth reading only if its rejections are printed and its arithmetic closes. The files here let a reader test that claim without the author, and run the same procedure against a different filter.

```
python3 code/verify.py
```

The script runs 94 checks, prints one line for each, and exits 0 when all pass. It needs Python 3 and nothing else. Twelve of the checks rebuild a join rather than read a column: App. E is reconstructed from `sources/` back to the seated titles, Rule 9's ranking closure is recomputed from the ranking file and App. C, and the two data files are held against each other. A column cannot confirm itself, and those twelve are what a replicator's own run does.

**Two things to do first, if this is your first time.** On macOS, typing `python3` opens a dialog offering to install the developer tools; accept it, wait, and try again. On Windows, install Python from python.org and tick "Add python.exe to PATH" on the first screen. Nothing else is needed - no libraries, no accounts, no setup.

---

## Before you extract anything from the printed volume

Read `EXTRACTION.md` first. It is short, and it is the record of ten ways a machine reported
a defect in this volume that was not there. Three of them bite in the first ten minutes and
two of those bite silently.

**Every numbered entry carries a zero-width space between the marker and the title.** There
are 4,209 of them. `^\d+\.\s+(.*)$` does not match. `^\d+\.\s*(.*)$` matches and
captures U+200B into the title, which then joins to nothing while looking correct in a
terminal. Strip U+200B, U+00A0 and U+2011 before matching anything.

**The index pages set two and three columns, and a band's list runs on from one column into
the next.** Ordering lines by vertical position interleaves them and destroys both the
roster order and the band attribution. Cluster on the left edge, order the clusters left to
right, and expect a list to continue across a cluster boundary.

**Prove the extraction before trusting a finding from it.** The eight alphabetical runs hold
93, 53, 116, 141, 99, 80, 78 and 69 titles. An extraction that does not return those six
figures is not ready to be read for defects.

Two further rules decide most of the rest. The `.docx` character stream is authoritative for
what the text says; the render is authoritative for every generated number and for anything
positional - a line break, a heading, a column. Neither is authoritative for whether two
words have a space between them, which only the glyph geometry settles.

---

## The figures the checks recompute

Three published sources form the pool: a recording-frequency ranking of 1,000 titles, Mark Levine's repertoire chapter (964 titles, 420 of them absent from the ranking), and Ted Gioia's *The Jazz Standards* (266 titles, 264 of which resolve into the pool). The pool is 1,420 titles. A declared practitioner filter retains 729 and declines 701, and every decline is printed by name.

```
by warrant    536 [W1] + 183 [W2] + 0 [W3] + 10 [W4]    = 729
by tier       93 + 53 + 116 + 141 + 99 + 227            = 729
by division   502 [D1] + 227 [T6]                        = 729   (a regrouping of the tiers)

residues      536 + 464 = 1,000        183 + 237 = 420        declines 237 + 464 = 701
```

The first two lines are independent routes. The third sums the tiers into divisions and is printed as a regrouping, not as a third route.

Two call instruments were opened after the Index closed and admit nothing: Mark Watkins's 2010 survey of thirty-seven educator-performers, and David Miller's log of 2,038 calls at London sessions from 2019. A fourteen-program collegiate panel was consulted the same way.

---

## Three things the volume does not carry

`data/style_classification.tsv` holds a `ballad` column, marking 75 of the 520 rows. It is
the only column in this repository with no locus in the volume, and it is here on purpose
rather than by omission.

The volume declines to make tempo claims. A leader sets every tempo on the night and a
vocalist moves every key, so no mark prints for a ballad, no count depends on one, and
nothing in Appendix J asks a replicator to name any. The column exists because a tool built
on this data wanted the distinction and would otherwise have carried it privately, which
would have made it unassailable. It is a reading of which titles are habitually counted off
slow. It is not documentary, it is not derived from either book, and a replication that
ignores it loses nothing.

It is checked like the rest of the file - 75 marks, every one on a seated row, no third
value - so that a reader who disagrees with it can see exactly what it claims before
disagreeing.

`data/setbuilder_extension.tsv` is the second. The volume's style page classifies 491
titles and stops there, which leaves 74 of Index 4's 99 seats with no idiom, feel, form or
origin. Those fields are what a set builder scores a joint on, so without them those 74
titles cannot be ordered against anything.

The file carries a reading of exactly those 74 and nothing else. It is deliberately a
separate file: `style_classification.tsv` stays at 520 rows, so the 491 and the 520 the
volume prints at § VI.2.c and § VI.6.b remain true of the file they describe. Every row
states its own basis - `set-builder reading; not classified in the volume` - so no row of
the author's classification and no row of this one can be mistaken for the other.

`data/vocal_option.tsv` is the third. Index 1 to 3 seats are instrumental titles, and the
volume's italic marks the ones holding a current independent life as vocal repertoire. A
wider set carries a lyric that a singer can front at a session without holding that life -
*Afro Blue*, *Work Song*, *Night in Tunisia*, *Well You Needn't*. The volume does not mark
them, because italic turns on a stricter test and the counts printed at Indexes 1A, 1B and
2 turn on that test. The file records them for the set builder. A title is
entered only where known recordings carry the vocal, so a lyric that exists without a
standard vocal version is left out. All four instrumental indexes are read - 16, 10, 12 and 6
rows. A title is entered only where a named recording carries the vocal. Two checks hold it:
forty-four rows across those indexes, every one on a seated instrumental with no duplicate
seat, and every title matching the roster at its seat.

The rule applied throughout the Index 4 file: **provenance is who wrote the tune; idiom is
the tradition the tune is called in.** That is the rule the volume's own 25 classified Index 4 rows
follow, where Star Dust sits in the Armstrong and Waller group and reads Straight-ahead.
Two checks hold the file: 74 rows, all at Index 4, all on seated seats, none already
classified; and the two files together covering all 99 Index 4 seats exactly once.

## Layout, and the volume pointer each file answers

| file | rows | what it is | the volume's pointer |
|---|---|---|---|
| `data/index_membership_729.tsv` | 729 | one row per seat: index, seat, title as printed, form block, warrant, rank, chapter and guide presence, marks, band, logged calls, Watkins counts, phase, style group | App. J Rule 7: "the membership file at the repository governs" |
| `data/evidence_join_729.tsv` | 729 | the source forms each seat was matched on, Watkins's categorical split and graded years, Miller's Top 201 | § II, § VI.3 |
| `data/vocal_band_worksheet_227.tsv` | 227 | source count per vocal title, the rank drop, the forty-two screening drops, the six compiler seats | the note under TABLE IV.6: "the band file at the repository" |
| `data/style_classification.tsv` | 520 | provenance, idiom, rhythmic frame, form block and harmonic terrain for the 491 classified titles and the 29 set-rule entries, and a ballad column the volume does not carry | § VI, opening; § VI.2.c; the ballad column, none |
| `data/setbuilder_extension.tsv` | 74 | the same fields for the 74 Index 4 seats the style page does not classify, read by the compiler for the set builder alone | none |
| `data/vocal_option.tsv` | 44 | instrumental seats at Indexes 1A, 1B, 2 and 3 carrying a lyric a singer can front, with the lyricist and the named recordings that carry it | none |
| `data/style_contested_calls_12.tsv` | 12 | the idiom calls a second reader could file differently, with the argument for moving each | § VI.5.e |
| `data/name_table.tsv` | 133 | FM.6's fifty-two names, the case and punctuation variants, and the nine chapter folds | FM.6; App. J Rule 6d |
| `data/tier_pair_separation.tsv` | 12 | for each tier pair, the share of title-against-title comparisons the lower tier wins on the ranking, the log and the survey | TABLE II.6, TABLE II.7 |
| `residues/appendix_A_levine_unique_420.tsv` | 420 | Levine's titles absent from the ranking, with the seat of the 183 retained | App. A |
| `residues/appendix_B_levine_declined_237.tsv` | 237 | the chapter's declines | App. B |
| `residues/appendix_C_ranking_declined_464.tsv` | 464 | the ranking's declines, with rank | App. C |
| `residues/appendix_D_gioia_declined_6.tsv` | 6 | Gioia titles not retained (a cross-reference: all six also sit in App. C) | App. D |
| `sources/jazzstandards_ranked_1000.tsv` | 1,000 | the ranking, in rank order | App. J Rule 13 note |
| `sources/jazzstandards_ranked_1000_alphabetized.tsv` | 1,000 | the same list filed by FM.1.f, which is the form J.13.b supplies to a model | J.13.b |
| `sources/watkins_2010_*.tsv` | 92 / 96 / 137 / 228 | List 1, List 2, the categorical listing with its survey split, the four-year graded sequence | § II.1, App. M.1 |
| `sources/miller_*.tsv` | 308 / 201 | the call log as title and count, and the published Top 201 | § II.1, App. M.1 |
| `panel/panel_sources_14.tsv` | 14 | institution, document, address, format, rows and titles as printed, retrieval date | TABLE IV.8.b, App. H, App. L.8 |
| `panel/panel_rows_pooled.tsv` | 1,533 | every row of the fourteen documents as printed, with its normalized form | App. H: "the pooled row file" |
| `panel/panel_union_k.tsv` | 460 | the union under the folding rules, with the number of programs (k) and the seat each title reaches | App. H: "the k-counts" |
| `panel/FOLDING_RULES.md` | | the six folding rules and the reading decisions applied with them | App. H: "the folding rules" |
| `prompts/rule_13_screening_prompt.txt` | | the J.13 screening prompt, byte for byte as printed | App. J Rule 13 note |
| `prompts/SHA256SUMS` | | its checksum | App. J Rule 13 note |
| `code/norm.py`, `code/aliases.py` | | title identity, and every join normalization cannot make | App. L.8: "the data files and the verification script" |
| `code/panel.py` | | rebuilds the union, the k-counts and the reach table from the pooled rows | App. H |
| `code/verify.py` | | the battery | App. L.8 |

---

## Title identity, which is where a replication diverges first

`norm.identity()` removes performance keys and AKA parentheticals, strips diacritics, folds curly quotes and `&`, lower-cases, and keeps letters and digits. It keeps leading articles, because the volume files a title under its article. `norm.match_key()` removes a leading article for joining one source's spelling to another's, and nothing else. `norm.alphakey()` is the FM.1.f filing key.

Every other join is declared in `code/aliases.py`. Three kinds are worth knowing before a first run:

- **Folds normalization cannot derive.** *Black Orpheus* and *A Day in the Life of a Fool* are *Manha De Carnaval*; *Chega de Saudade* is *No More Blues*; *Budo* is *Hallucinations*; Miller's *My Secret Love* is *Secret Love*. The nine chapter folds used for the vocal band worksheet are listed there too, seven mechanical and two judgments (*In My Solitude*, *I've Grown Accustomed To Your Face*).
- **Forms a source prints that `match_key` cannot reach.** A leading parenthetical is the case it misses most often: Miller's log prints *Weaver Of Dreams* for App. B's *(You're A) Weaver Of Dreams*, Watkins's categorical listing prints *Flintstones, The* for *(Meet) The Flintstones* and *Jodie Grind, The* for *The Jody Grind*, the ranking prints *Until I Met You (Corner Pocket)*, and Miller's 201 prints *Well You Needen't*. Sources are cited as printed (Index 3.1.d), so the fold is declared rather than the row corrected.
- **Folds a replicator working from the books will need.** The chapter drops subtitles the ranking prints, so *Green Dolphin Street*, *Liza*, *Shaw*, *Who Cares?* and twenty-one others need a declared fold before the chapter joins to the ranking. Without them the chapter's unique count comes back 444 rather than the 420 at App. A. The chapter also carries one title twice, under *Amor Em Paz* and *Once I Loved*, so its 964 entries are 963 titles. Watkins's *No Blues (Pfrancing)* is the same case on this repository's own side.
- **Joins that are refused.** Miller's *I Love You* is not *P.S. I Love You*. *Prancing* is not *Pfrancing*. The ranking's *Sugar (That Sugar Baby O' Mine)* is not the Turrentine *Sugar* seated at Index 2 #70. Levine's *Lonely Woman (Silver)* is not Gioia's Coleman composition. *The Theme* is not *52nd Street Theme*.
- **One fold that is valid for a single source.** `aliases.BY_SOURCE` holds it. Levine's chapter carries Silver's *Lonely Woman*; Gioia and Watkins carry Coleman's, which TABLE R.4 puts outside the pool. A join that applies its folds without regard to which file it is reading will merge the two.
- **One column that can go stale, and the check that stops it.** `data/name_table.tsv` carries a `seat` for each folded name, which is a convenience and a hazard: a seat number is the roster's to state, and a second copy of it drifts the moment a title moves. An earlier packet for this project carried the same column and 45 of its 124 rows went stale while every one of its mappings stayed correct. The mapping is durable; the address is not. `verify.py` now asserts that all 133 addresses agree with the roster, that no fold points at another fold's source, and that every fold target is a title the volume seats or prints in a residue.
- **One collision, disclosed.** The Index seats the 1958 modal *Milestones* at Index 1A #33; the 1947 line is a separate composition, declined at App. B. Instruments that print one *Milestones* are not used to merge them.

---

## The screening prompt

App. J Rule 13 prints the J.13 prompt and states that it is mirrored here byte for byte, with the SHA-256 of the file. To confirm that the prompt in hand is the printed one:

```
cd prompts && sha256sum -c SHA256SUMS      # Linux
cd prompts && shasum -a 256 -c SHA256SUMS  # macOS
```

Either prints `rule_13_screening_prompt.txt: OK`. macOS ships `shasum` and not `sha256sum`, so the first command answers "command not found" there; it is the same check under a different name.

The file is plain ASCII and ends in one newline. `.gitattributes` turns off line-ending conversion, so a clone on any platform checks the file out byte for byte; a copy saved through an editor or a browser can change its line endings and fail the check. Where this file and the printed page differ, the printed page governs, and the difference is a defect to be filed here (App. L.8). A model given the prompt is given the files J.13.b lists and a completed filter card at J.13.c, and nothing else.

---

## Two different asks, and what each costs

**Checking this edition** takes about twenty minutes and costs nothing. Clone the repository, run the script above, run the checksum, and read `EXTRACTION.md` before pulling anything out of the printed volume. Everything needed is in this repository. No part of it requires agreeing with a single seating decision.

**Producing a comparable run** is a term's work. It needs two books this repository cannot carry, a filter only you can declare, and a screen across 1,420 titles - fifty-seven batches at the twenty-five J.13.e sets. The volume is explicit that your total will not be 729 and should not be.

**On the filter, which is where most people stop.** Rule 5 asks what you have observed being called, where, over what period, on what instrument, in what capacity. A short and narrow answer is a legitimate answer. Two years of student ensembles in one town, declared as exactly that, is a filter; it is a *different* filter from this edition's, which is the entire point. App. L says so in terms: a divergence between two declared filters "is a better object than this book." What is not legitimate is an undeclared filter, or one borrowed from here. The filter card at J.13.c has a line for known biases and a line for what the filter does not reach, and filling both honestly is what makes a thin filter usable rather than disqualifying.

---

## Running the procedure yourself

1. Build a pool from the sources at `SOURCES.md`. Substitutions are permitted and are declared.
2. Complete the filter card at J.13.c: settings, scene, period, instrument and vantage, known biases, and what the filter does not reach. This is the step no one can inherit.
3. Screen in batches, record a ground for every decline, and print the residue.
4. Close the arithmetic by at least two independent routes against your own total. **Do not close to 729.** App. J states that a run landing on this edition's total has adopted this edition's declarations in place of its own.
5. If you open the call instruments, open them after seating. They admit nothing; what they report is agreement or divergence.

---

## What is not here, and why

- **Levine's chapter and Gioia's list.** They are books. The chapter's 420 titles absent from the ranking are printed at App. A and are here, because that set is this project's derivation; the full 964 and Gioia's 266 have to be taken from the books cited at `SOURCES.md`.
- **The fourteen program documents.** Their addresses and retrieval dates are here, with every row as printed. A replication should retrieve and date the documents again rather than inherit a snapshot.
- **Model transcripts.** No count in the volume originates with a model (App. J Rule 2), and none is published as evidence here.

---

## Release, citation and corrections

This release is tagged `v15.0.1` and archived on Zenodo, which mints a version DOI for it. The tag and the DOI fill the two placeholders in the App. J Rule 13 note; cite the version DOI (see `CITATION.cff`). A correction to a count, a locator or a file is filed here as an issue and receives a dated, attributed record (App. L.8). An exception to a seat or to the filter is not a correction; App. L.3 states what one has to carry.

The ranking, the survey, the log and the program documents are other people's work and are cited in full at `SOURCES.md`. The keyings under `sources/` and `panel/` are transcriptions made for this project; where a keying differs from its published source, the published source governs. Everything under `data/`, `residues/` and `code/` is this project's own work.

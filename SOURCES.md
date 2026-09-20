# Sources

Where every keyed file in this repository came from, how it was taken, and what a replicator has to acquire independently. Editions are given exactly. The full citations are App. M.1 of the volume; where this file and App. M.1 differ, App. M.1 governs.

---

## The three sources that form the pool

### 1. The recording-frequency ranking

> JazzStandards.com: The Premier Site for the Study of Jazz Standards. Anonymous. https://www.jazzstandards.com/. Ranked list of 1,000 compositions at https://www.jazzstandards.com/compositions/index.htm. Accessed August 15, 2026 (App. M.1).

**Here:** `sources/jazzstandards_ranked_1000.tsv` (ranks 1 to 1,000, no gaps) and `sources/jazzstandards_ranked_1000_alphabetized.tsv` (the same titles filed by FM.1.f, with rank). The keying was taken from the ten paginated index pages, `index.htm` and `index2.htm` through `index10.htm`, on 2 September 2026.

**Method, as the site states it:** compositions are ranked by the number of different jazz artists, from a frame of about 700 whose principal body of work is jazz, holding a currently available CD containing the composition. Several recordings by one artist do not raise a rank, and out-of-print media are excluded. Rank 1 corresponds to more than 100 artists, rank 750 to at least 10, rank 1,000 to 6.

**Identity note:** the ranking's #269 is *Sugar (That Sugar Baby O' Mine)*, the 1927 song. It is declined at App. C #345. The *Sugar* seated at Index 2 #70 is Stanley Turrentine's composition and enters on Levine's chapter.

### 2. The pedagogical repertoire source

> Levine, Mark. *The Jazz Theory Book*. Petaluma, CA: Sher Music Co., 1995. ISBN 978-1-883217-04-4. Chapter 21, "The Repertoire," pp. 419-460.

**Not here.** Print only. The volume counts 964 entries on those pages (App. M.1 records Levine's own statement of 965 and the one composition entered under two names). **Derived and here:** `residues/appendix_A_levine_unique_420.tsv`, the 420 entries absent from the ranking, with the seat of the 183 retained; `residues/appendix_B_levine_declined_237.tsv`.

### 3. The critical guide

> Gioia, Ted. *The Jazz Standards: A Guide to the Repertoire*. 2nd ed. New York: Oxford University Press, 2021. ISBN 978-0-19-008717-3.

**Not here.** The volume counts 266 compositions by hand from the second edition. 264 resolve into the pool; Birdland (reserved for a companion index) and Ornette Coleman's *Lonely Woman* do not. No title enters on the guide alone, because every title that resolves is already ranked or in the chapter (TABLE IV.1.b). The first edition (2012; ISBN 978-0-19-993739-4) is not interchangeable. **Derived and here:** `residues/appendix_D_gioia_declined_6.tsv`.

---

## The two call instruments - opened after the Index closed, admitting nothing

### 4. The practitioner survey

> Watkins, Mark. "Repertoire." In *Fundamentals of Jazz Improvisation: What Everybody Thinks You Already Know*. Rexburg, ID: Brigham Young University-Idaho, 2010. https://content.byui.edu/file/be14498b-aa3f-4b2a-b9e6-4fb3fdbd1d12/1/07%20Repertoire.pdf

A free PDF: thirty-seven educator-performers asked for the tunes most called at gigs and jam sessions in their area. Levine is one of the thirty-seven, so this instrument and the chapter are not fully independent; the log is.

| file | what it is | where in the PDF |
|---|---|---|
| `sources/watkins_2010_list1_92.tsv` | 92 titles named by ten or more contributors, with counts | p. 4 |
| `sources/watkins_2010_list2_96.tsv` | 96 titles named by five or more, with counts | p. 4 |
| `sources/watkins_2010_categorical_137.tsv` | the categorical listing entries that print a survey / additional-sources split | pp. 8-10 |
| `sources/watkins_2010_graded_228.tsv` | the four-year graded sequence, 228 entries | p. 7 |

**Two source defects, keyed as printed.** In List 2, *Take 5* reads `03` and *Four in One* reads `01`, below the list's own floor of five. **One scope note.** The band rule at § VI.3.a reads the List 1 count only. The survey column of `data/tier_pair_separation.tsv` reads the count on whichever list prints a title, which is the reading that returns the survey figures TABLE II.7 prints.

### 5. The call log

> Miller, David. "The Top 25 Jazz Standards." Standard Repertoire. Updated October 2021. https://standardrepertoire.com/pages/the-top-25-jazz-standards.html. Accessed August 29, 2026.
> Miller, David. "About This Site." Standard Repertoire. https://standardrepertoire.com/pages/about-this-site.html.
> Data: https://github.com/davidmiller/repertoire/blob/master/content/data/514.calls.csv

| file | what it is |
|---|---|
| `sources/miller_london_calls_308.tsv` | the log as title and call count; 308 titles, 2,038 calls |
| `sources/miller_published_201.tsv` | the keeper's published Top 201, a selection and not an observation |

The keeper states that he adjusted his published lists where rehearsals with his own bands had inflated some titles. A single count is evidence that a title was played, not a measure of how widely it is called. The folds needed to join his spellings are in `code/aliases.py`, and one join is refused: his *I Love You* is not *P.S. I Love You*.

---

## The collegiate panel - consulted after the Index closed, admitting nothing

`panel/panel_sources_14.tsv` gives each program's document, address, format, rows and titles as printed, and the retrieval date (26 August 2026). `panel/panel_rows_pooled.tsv` carries every row as printed, with the normalized form used to pool it. The documents themselves are not redistributed; a replication should retrieve and date them again. The folding rules are at `panel/FOLDING_RULES.md`, and `code/panel.py` applies them.

---

## What a replicator needs

- To rebuild the pool: sources 1, 2 and 3. Two of the three are books.
- To rebuild the corroboration: sources 4 and 5, both free and online, and the panel documents at their addresses.
- To rebuild the filter: nothing from here. It is the replicator's own, declared on the card at J.13.c.

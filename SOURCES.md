# Sources

Where every file in `sources/` came from, how it was extracted, and what a replicator has to
acquire independently. Editions matter and are given exactly.

---

## The three warrant sources - the pool

### 1. Recording-frequency ranking

> JazzStandards.com: The Premier Site for the Study of Jazz Standards. Anonymous.
> `https://www.jazzstandards.com/`. Ranked list of 1,000 compositions consulted at
> `https://www.jazzstandards.com/compositions/index.htm`.

**In this repository:** `sources/jazzstandards_ranked_1000.tsv`, ranks 1-1000, no gaps.
**Acquired:** the ten paginated index pages, `index.htm` and `index2.htm` through
`index10.htm`, fetched 2 September 2026. `code/fetch_ranking.py` documents the procedure.
**Method, as the site states it:** titles ranked by the number of different jazz artists,
drawn from a frame of roughly 700 whose principal body of work is jazz, holding a currently
available CD containing the composition. Multiple recordings by one artist do not raise a
rank. Sales carry no weight. Out-of-print media are excluded by design. Rank 1 corresponds to
more than 100 distinct artists, rank 750 to at least 10, rank 1,000 to 6.
**Note:** the site names no editor, author or publishing entity and is cited as anonymous on
that basis. Its copyright line differs between pages - the home and overview pages read
2005-2022, the compositions index used here reads 2005-2020.

### 2. Pedagogical repertoire source

> Levine, Mark. *The Jazz Theory Book*. Petaluma, CA: Sher Music Co., 1995.
> ISBN 978-1-883217-04-4. Chapter 21, "The Repertoire," pp. 419-460.

**Not in this repository.** Print only; no machine-readable edition exists. 964 titles,
hand-transcribed for this project directly from those pages. The first attempt came to 950
and was corrected after one alphabetical run was found to have been skipped on a single page.
No published count exists to check it against, which is why the page range is given so that
anyone may make their own.
**Derived and included:** `residues/appendix_A_levine_unique_419.tsv`, the 419 titles absent
from the ranking, which is this project's own deduplication and is printed in the volume.

### 3. Critical and historical survey

> Gioia, Ted. *The Jazz Standards: A Guide to the Repertoire*. 2nd ed. New York:
> Oxford University Press, 2021. ISBN 978-0-19-008717-3.

**Not in this repository.** 266 compositions treated; the contents list is the extract.
265 resolve into the pool and none enters on Gioia alone. The one title outside both other
pools is *Birdland*, reserved.
**The first edition is not interchangeable:** New York: Oxford University Press, 2012,
ISBN 978-0-19-993739-4, treats 250. The second adds fifteen selections.
**Derived and included:** `residues/appendix_D_gioia_declined_6.tsv`.

---

## The two call instruments - consulted after the Index closed, admitting nothing

### 4. A 2010 practitioner survey

> Watkins, Mark. "Repertoire." In *Fundamentals of Jazz Improvisation: What Everybody Thinks
> You Already Know*. Rexburg, ID: Brigham Young University-Idaho, 2010. 12 pp.
> `https://content.byui.edu/file/be14498b-aa3f-4b2a-b9e6-4fb3fdbd1d12/1/07%20Repertoire.pdf`

Free PDF, publicly available. A published practitioner survey, not a peer-reviewed article.
Thirty-seven jazz educator-performers were asked for the tunes most called at gigs and jam
sessions in their area. 611 distinct titles; 263 named once; 87 named twice.

**In this repository, four separate instruments from that one document:**

| file | what it is | where in the PDF |
|---|---|---|
| `watkins_2010_list1_92.tsv` | 92 titles named by ten or more contributors, with counts | p. 4 |
| `watkins_2010_list2_96.tsv` | 96 titles named by five or more | p. 4 |
| `watkins_2010_categorical_137.tsv` | the categorical listing with the printed survey / additional-sources split | pp. 8-10 |
| `watkins_2010_graded_228.tsv` | the four-year curricular sequence, 228 entries, 193 distinct titles | p. 7 |

**Two source defects, not extraction artifacts.** In the List 2 table, *Take 5* reads `03` and
*Four in One* reads `01`, in a list whose stated floor is five. Both are keyed as printed.
Any threshold applied at five must therefore exclude them explicitly.

**One structural caution.** Watkins states at his p. 8 that the survey question under-reported
blues and rhythm-changes heads, and that he lowered his own threshold for those two columns of
the categorical listing to compensate. The categorical listing is therefore not comparable to
the two printed lists and should not be pooled with them.

**One dependency worth knowing.** Mark Levine is one of the thirty-seven contributors, so this
survey and warrant source 2 are not fully independent of each other. The call log is.

### 5. A London call log

> Miller, David. `https://standardrepertoire.com/pages/about-this-site.html`
> Data: `https://github.com/davidmiller/repertoire/blob/master/content/data/514.calls.csv`

Already machine-readable and publicly posted. 2,038 calls of 308 distinct titles across 160
sessions, beginning 22 June 2019. One observer, one city, one circuit.

| file | what it is |
|---|---|
| `miller_london_calls_308.tsv` | the log: title and call count. Sums to 2,038 |
| `miller_published_201.tsv` | his own published Top 201, which is a selection and not an observation |

**The filename is a misnomer:** nothing in the file equals 514.
**A scoping note the keeper supplies himself, and it governs every single count cited from
the log:** he states that he adjusted his published lists where rehearsals with his own bands
had raised otherwise uncommon tunes, and three titles this project cites are among those he
then left off. A single count is evidence that a title was played, not a measure of how widely
it is called.
**Four alias folds are needed** to join his lists to his log and to this Index, and one join
must be refused. All are in `code/aliases.py`.

---

## Not included, and why

**The fourteen collegiate program lists.** Retrieved on one day, 26 August 2026, from fourteen
degree-granting jazz programs publishing required or expected repertoire. A replication should
re-retrieve and re-date rather than inherit a snapshot. The union is sensitive to six folding
rules; without them a replicator lands anywhere between 455 and 470 titles.

**The pedagogical and play-along series** cited for the skill path. These informed
stratification and are not sources of survey warrant.

---

## What a replicator actually needs

To rebuild the pool: sources 1, 2 and 3. Two of the three are books.
To rebuild the corroboration: sources 4 and 5, both free and both online.
To rebuild the filter: nothing. It is yours, and it is the step that cannot be inherited.

# Folding rules for the fourteen-program panel

The fourteen documents disagree about what counts as a title. The union, the k-counts and the reach table at App. H depend on how rows are folded, so the rules are stated here and applied in `code/panel.py`. A replicator who applies them differently lands between 455 and 483 titles; applied as coded here they return 460.

## The six rules

1. **Performance keys are not part of a title.** Texas State prints keys inside the title cell: *Autumn Leaves (em and gm)* is *Autumn Leaves*; the same holds for *Just Friends (F and G)*, *On Green Dolphin Street (C and Eb)* and *'Round Midnight (Monk changes)*. Notes such as *(faster)*, *(A section only)* and *(Horace Silver)* are treated the same way.
2. **Utah's six model / contrafact lines are two titles each.** *How High the Moon / Ornithology*, *Indiana / Donna Lee*, *Ladybird / Half Nelson*, *Sweet Georgia Brown / Dig*, *In Walked Bud / Blue Skies*, *So What / Impressions*. The pooled row file already carries each pair as two rows.
3. **Oregon's *Misty / I Want to Talk About You* is one option row and counts as *Misty* only.**
4. ***In a Mellotone* and *In a Mellow Tone* are one title.**
5. ***Milestones* (1958) and *Milestones (Old)* are two compositions and are not folded.** California State University, Long Beach prints an unqualified *Milestones*, and it is not used to merge them. The pooled row for Western Michigan's *Milestones (Old)* was normalized without its qualifier; the script restores it.
6. ***A Day in the Life of a Fool*, *Black Orpheus* and *Manha de Carnaval* are one title.**

## Reading decisions applied with the rules

- **Five one-letter variants are folded:** *Samba de Orfeo* (Samba De Orfeu), *(The) More I See You*, *Goodbye Porkpie Hat* (Goodbye Pork Pie Hat), *Daydream* (Day Dream), *What A Difference A Day..* (What a Difference a Day Made).
- ***Prancing* and *Pfrancing* are not folded.**
- **Marshall is read at pp. 17-18 only.** The audition suggestions elsewhere in its handbook (the rows marked *entrance UG* and *entrance GR*) are excluded.
- **Rows that are not titles are excluded:** two page-furniture rows in the William Paterson document (*University Jazz Studies*, *Program*) and Iowa's form entry *Bb Rhythm Changes*.
- **Exemplar rows count.** Colorado Boulder's list is printed entirely as exemplars, and Iowa's exemplar rows are titles.

## What the rules return

| figure | value |
|---|---|
| union | 460 |
| titles on fourteen or thirteen lists | 0 |
| titles on twelve lists | 4 (All the Things You Are, Autumn Leaves, The Girl From Ipanema, Take the "A" Train) |
| titles on one list | 179 (39 percent) |
| reach, as distinct seats: Index 1A, 1B, 2, 3, 4, 5 | 93, 52, 88, 47, 16, 92 |

The reach figures count distinct seated titles the union reaches, not matching rows; several rows can resolve to one seat. They move only with title matching, and every join behind them is in `code/aliases.py`.

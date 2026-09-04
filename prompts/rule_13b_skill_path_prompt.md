# Rule 13B. The skill-path prompt

**This is the one that builds the Foundational / Emerging Intermediate / Intermediate bands.**
Transcribed from The Realistic Book Index, Draft 10.7, pp. 128-130.

**It runs second.** It admits nothing and declines nothing, so it cannot be used to build an
index. Run `rule_13_screening_prompt.md` first, seat the lists, then run this against what is
seated.

Compiler's note as printed: *Run this only after Lists 1-5 are seated. It does not admit or
decline. It does not change N.*

It now sits where it belongs. In Draft 10.3 it was preceded by the editorial line *"Paste this in
Appendix J after Rule 13, as a second executable prompt,"* which was an instruction to the
compiler sitting in the manuscript. That line is gone in 10.7 and the prompt is seated at
Appendix J behind Rule 13.

---

```
[BEGIN PROMPT]

1. Your role

You assign practice phases for educators. You do not admit titles to the Index. You do not remove
titles. You do not invent repertoire.

2. What I supply

The seated Lists 1-5. Sher Real Easy Books. Aebersold volumes 54 and 70. Any other graded series
I attach. TABLE V.2 is the series list in this edition.

3. What you may not do

Add a title that is not on Lists 1-5. Report it as an orphan if I ask you to place one. Do not
use recording rank to order a phase. Do not use Watkins, Miller, or a school list unless I attach
them and say so. Do not publish phase totals.

4. The phases

Foundational - high-circulation, playable early.

Emerging Intermediate - expanded harmony, rhythm, or style, still reachable.

Intermediate - what a working player is expected to carry.

At most one phase per title. Many seated titles get no phase.

5. How you grade

Floor: if the title is in Sher Real Easy or Aebersold 54 / 70, start there. Then use any other
attached graded series. Cite the edition. If no attached series carries the title, say so and
propose from harmonic and rhythmic demand only, marked unverified against pedagogy.

Time-grade, if I ask for a column:

  fnd - a competent section produces the feel without strain.
  emg - tempo or named feel is hard; a competent section still gets through it.
  int - not reliable without preparation or a stronger player.

Blank Feel = swing. Named feels are printed even when the time grade is fnd.

6. Grouping

Inside a phase, group by the list the title already sits on. Withdraw twelve-bar blues, minor
blues, and rhythm-changes titles from those groups and print them beneath, except List 4, which
keeps its period groups. Asterisk a modified form.

7. Output, one line

title | current list | proposed phase or none | floor edition or "none" | time-grade if asked |
feel if asked | one sentence

8. End of run

List orphans. List titles you could not floor against an attached series. No 66 / 58 / 50 / 174.
The compiler seats the phases. Sizes are TABLE IV.5.

[/END PROMPT]
```

---

## What to attach when you run this

| attach | from this repository |
|---|---|
| the seated Lists 1-5 | `data/index_membership_729.tsv` |
| **the graded-series floor section 5 calls for** | `sources/graded_series_552.tsv` |
| the volumes behind it, with editions | `sources/graded_series_volumes_27.tsv` |
| the practice-order pages, if you want the existing phase reading | `data/priority_list1.tsv` through `data/priority_lists4_5.tsv` |

**You do not need the seventeen books to run this.** Section 5 says *"if the title is in Sher Real
Easy or Aebersold 54 / 70, start there,"* and that floor is published here: 552 title lines across
27 volumes, 453 distinct compositions, each carrying the seat it lands on in this Index or the
note that it was declined or never entered the pool. `graded_series_volumes_27.tsv` gives the
volume, its title count, the band this edition assigned it, and its ISBN or catalogue number, so
a replicator can buy any volume they want to check rather than inherit the transcription.

**Substituting a different series is the better replication**, and section 5 is written for it -
*"Then use any other attached graded series. Cite the edition."* A replicator who grades against
their own shelf and lands on different phases has produced a finding. One who reuses this floor
has reproduced an arithmetic.

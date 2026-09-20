# The screening prompt, mirrored

`rule_13_screening_prompt.txt` is the J.13 prompt printed at App. J Rule 13 of *The Realistic Book Index*, Draft 15, from `[BEGIN PROMPT]` through `[/END PROMPT]`. It is plain ASCII and ends in one newline. The note above the printed prompt gives this file's SHA-256; `SHA256SUMS` carries the same value.

```
sha256sum -c SHA256SUMS
```

If the file and the printed page differ, the printed page governs, and the difference is a defect to be filed at this repository (App. L.8).

## What a run gives the model, and where each item is

After Publication in App. J states that the model is given the prompt as printed, the replicator's filter card at J.13.c, and the files J.13.b lists, and nothing else.

| J.13.b item | where it is |
|---|---|
| the ranked 1,000, already alphabetized | `sources/jazzstandards_ranked_1000_alphabetized.tsv` |
| Levine, chapter 21 | the book (see `SOURCES.md`); not redistributed |
| Gioia | the book (see `SOURCES.md`); not redistributed |
| the current seated indexes and declines, for a check rather than a first screen | a replicator's own; this edition's are `data/index_membership_729.tsv` and `residues/` |
| the Rule 5 declaration on the filter card | written by the replicator on the card at J.13.c |
| for Stage Five, the Levine-only residue | a replicator's own; this edition's are `residues/appendix_A_levine_unique_420.tsv` and `residues/appendix_B_levine_declined_237.tsv` |

Watkins, Miller and the panel enter only at Stage Six, and only when the operator attaches them and says the run is Rule 6d. This edition's copies are under `sources/` and `panel/`.

## The other printed prompt

Rule 13B, the skill-path prompt, prints in App. J after this one and is not mirrored here; no checksum is printed for it. A replicator uses the printed text.

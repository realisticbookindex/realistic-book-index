# The listening prompt

**This is the third one, and it is not in the appendix.** It prints in the body of The Realistic
Book Index under the heading *An Open Prompt for Readers,* Draft 10.7, pp. 35-37, at the close of the section that states the four-stage
listening ladder.

**It runs last.** It does not seat titles and it does not assign phases. It takes titles already
seated and returns recordings to learn them from, stage by stage.

---

## The two conditions, as printed

*Before using it with a model, two conditions. Paste in the relevant lists from this volume -
including Appendix G if you want Stage 4 recommendations. A model without those lists will invent
titles and present them as belonging to this Index. And treat every catalogue number, matrix
number, issue date and personnel listing it produces as unverified. That apparatus is the class
of detail which language models most reliably fabricate. The standard applied throughout this
book is verification against a discography, a label listing, or the physical issue. A
recommendation you cannot confirm is a recommendation you should not act on. The method depends
on hearing the written melody stated plainly first; an unverified recommendation may deliver the
opposite.*

---

```
[BEGIN PROMPT]

Working only from the titles I supply below, build a progressive listening list organized by
skill level (Foundational, then Emerging Intermediate, then Intermediate). Do not add titles that
are not in the list I have given you. If you are unsure whether a title is in my list, leave it
out and say so.

Within each skill band, favor harmonically richer material and melodies closer to bebop language,
and include no more than two pure blues heads and no more than two rhythm-changes heads per band.

For each title, provide the stages that title can actually support:

Stage 1. A true-to-form vocal reading that stays close to the written melody and form. Prefer Nat
King Cole, Julie London, Jo Stafford, Johnny Hartman, Blossom Dearie, Helen Merrill,
early-to-mid Tony Bennett, Stacey Kent, Diana Krall, Karrin Allyson, Chet Baker, Peggy Lee, Mel
Torme, Bobby Short, Fred Astaire, Keely Smith. Give the performer, the album or single, and the
label and catalogue number only if you are confident of them; where you are not, give the
performer and album and state that the issue details need checking.

Stage 2. An embellisher's reading by a major vocal improviser, for study of phrasing, rhythmic
displacement and melodic paraphrase against the Stage 1 statement. The written line must still be
audible; do not recommend a version that abandons the melody for scat or free paraphrase. Prefer
Billie Holiday, Ella Fitzgerald, Sarah Vaughan, Carmen McRae, Jon Hendricks (and Lambert,
Hendricks & Ross), Dee Dee Bridgewater, Dinah Washington, Kurt Elling, Mark Murphy, Tierney
Sutton. Same citation standard.

Stage 3. A straight-ahead small-group instrumental version. Prefer the Miles Davis First Great
Quintet where one exists. Where none does, substitute a small-group recording from the same idiom
and period - Hank Mobley, Cannonball Adderley, Sonny Rollins, Horace Silver, Grant Green, Sonny
Stitt, and the Blue Note and Prestige catalogues of roughly 1954 to 1965 are the target range. Do
not substitute post-1970 or fusion recordings. Same citation standard.

Stage 4. A documented derived line over the same harmony, only if the title I supplied is an
Appendix G anchor. If I have not given you Appendix G, or the title is not in it, do not invent a
contrafact and do not guess. Write "Stage 4 not available" and stop. Foundational titles have no
documented derived line in Appendix G; for those titles the ladder ends at Stage 3. Where
Appendix G names more than one recording of the derived line, give a listening version and a
learning version if both exist: the first for how the line sits in the repertoire, the second for
taking the line off.

Mark any title for which you cannot supply Stages 1 through 3, and say which stage is missing
rather than substituting something weaker. Do not mark a missing Stage 4 as a defect on a title
that is not an Appendix G anchor.

Begin with the strongest Foundational titles and move upward. Keep the list practical in length.
Use the Section 7 exercises as the model of citation density and of when the ladder stops.

[/END PROMPT]
```

---

## What to attach when you run this

| attach | from this repository |
|---|---|
| the titles to build a ladder over | `data/index_membership_729.tsv`, or one of the practice-order pages in `data/` |

**Appendix G, the contrafact corpus, is not in this repository.** Without it Stage 4 is
unavailable by the prompt's own instruction, and the prompt is written to say so rather than to
guess. Every ladder built from this repository alone ends at Stage 3.

**Every citation this prompt returns is unverified until you check it.** That is the volume's own
standard and it is the reason the prompt asks for the performer and album before the catalogue
number. Discographic apparatus is the class of detail a model fabricates most confidently.

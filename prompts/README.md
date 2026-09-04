# The three prompts

The rest of this repository is data and a verifier. It lets you check what this edition claims.
It does not let you build your own, because the instrument that builds one is a prompt and the
prompts print in the volume rather than in the data. They are here so that a replicator has the
method and not only the result.

**They run in order, and each one refuses to do the next one's work.**

| # | file | what it does | when |
|---|---|---|---|
| 1 | `rule_13_screening_prompt.md` | seats titles: retain or decline, division, tier, warrant, tags | first, and nothing else can run until the lists are seated |
| 2 | `rule_13b_skill_path_prompt.md` | assigns Foundational / Emerging Intermediate / Intermediate | after seating. Admits nothing, declines nothing, does not change N |
| 3 | `listening_ladder_prompt.md` | returns recordings for each title, by learning stage | last. Takes seated titles and gives you what to listen to |

Plus one form: **`filter_card_TEMPLATE.md`**, which is section 3 of the first prompt and is the
only part of the method you must write yourself.

Prompts 1 and 2 print at the replication instrument, Appendix J, Draft 10.7 pp. 119-130. Prompt 3
prints in the body at pp. 35-37 under the heading *An Open Prompt for Readers.*

## The run, end to end

Four passes. Each one refuses to do the next one's work, which is why they are separate.

**0. Write your filter card.** `filter_card_TEMPLATE.md`. This is the step that cannot be
inherited, and everything the instrument excludes at Lists 1, 2 and 3 rests on it. Paste it into
section 3 of the screening prompt.

**1. Screen the 1,419.** `rule_13_screening_prompt.md` + `sources/pool_1419_candidates.tsv`, in
batches of twenty-five. Out comes a retain-or-decline verdict, a division, a tier and a warrant
for every title. **The model proposes and the compiler seats** - that line is in the prompt and
it is not decoration. A run whose output is adopted unedited has not applied the method.

**2. Check against the instruments.** Same prompt, Stage Six, run only after the lists are
seated: attach `sources/watkins_2010_list1_92.tsv`, `watkins_2010_list2_96.tsv` and
`miller_london_calls_308.tsv` and say this is Rule 6d. It reports agree and diverge. **It admits
nothing and moves nothing.** Disagreeing with either instrument is not a defect in your run.

**3. Assign the phases.** `rule_13b_skill_path_prompt.md` against your seated lists, plus
`sources/graded_series_552.tsv` as the floor section 5 calls for. Out comes Foundational, Emerging
Intermediate and Intermediate. Admits nothing, declines nothing, does not change your total.

**4. Build the listening ladder.** `listening_ladder_prompt.md` against a phase. Out come
recordings by stage. Every citation it returns is unverified until you check it.

Then close your own arithmetic with `code/verify.py`, against your total rather than this one.

**Do not close to 729.** The volume is explicit: a later run does not reconcile to this edition's
figure and should not try. A run that lands on 729 has adopted this compiler's declarations
rather than made its own.

## You can run the whole thing from this repository

**The three sources are books, and you do not need them to run the screening.** The candidate
pool is published here, and the pool is what the instrument screens. The books are needed to
audit how the pool was built, not to build an index from it.

`sources/pool_1419_candidates.tsv` is the file to attach at step 3 above. It is the 1,419
candidate titles and nothing else - **no disposition column, so it does not tell you what this
edition did with any of them.** That is deliberate. The pool closes as 1,000 ranked plus 419
unique to the chapter, and both halves are here to check that against:
`sources/jazzstandards_ranked_1000.tsv` and `residues/appendix_A_levine_unique_419.tsv`.

`sources/pool_1419_alphabetical.tsv` is the same 1,419 **with** this edition's disposition on
every row. Use it to compare after your run, not to screen from. A screener who has read the
dispositions is anchored, and the agreement figure that comes out of such a run measures
consistency under anchoring rather than independent convergence. This project made that mistake
once, on 17 August 2026, and withdrew the figure.

Each warrant is checkable from what is here:

| warrant | what settles it | in this repository |
|---|---|---|
| 1. presence in the ranked 1,000 | the ranking | `sources/jazzstandards_ranked_1000.tsv`, complete |
| 2. presence in the chapter, net of the ranking | the 419 unique to it | `residues/appendix_A_levine_unique_419.tsv`, complete |
| 3. presence in the guide | the guide's title list | **not here, and it admits nothing.** Warrant 3 never admits alone and carried 0 net in this edition. The prompt says so at *What you may not assume* |
| 4. the practitioner filter | your own card | `filter_card_TEMPLATE.md`, which you write |

**Warrant 2 is complete for every title it can decide.** The chapter carries titles that also
rank, and those are not published here - but a title that ranks is already admitted on warrant 1,
so its warrant-2 status moves no seat. What warrant 2 decides on its own is the 419, and the 419
is here in full.

**The graded-series floor is here too.** Rule 13B section 5 grades against seventeen published
volumes. You do not need them: `sources/graded_series_552.tsv` carries all 552 title lines across
27 volumes, and `sources/graded_series_volumes_27.tsv` carries the volumes themselves with
editions, so any one of them can be bought and checked rather than taken on trust.

**One thing genuinely is missing.** Appendix G, the contrafact corpus, is the volume's own
apparatus rather than a source. Without it Stage 4 of the listening prompt is unavailable by that
prompt's own instruction, and every ladder built from this repository alone stops at Stage 3.

## Three defects, carried forward rather than repaired

These files transcribe the prompts as printed. Where the printed text has a defect it is
reproduced and listed here, on the same principle the volume applies to its own historical
screening prompt: a record of what was run is worth more than a tidied version of it. All three
are in prompt 1.

1. **Section 11 is used twice**, once for *Output, each title, one line* and once for *Where the
   criteria are silent or in conflict.* A model reading the prompt top to bottom meets the number
   twice and the second overwrites the first in any structured reading. Sections 4a and 4b also
   sit after section 5 rather than after section 4.

2. **Section 3 has dropped characters and a duplicated sentence.** The printed text reads *"Apply
   it as given. t governs exclusion at List 1. he declaration below is the only call-likelihood
   evidence you have. Apply it as given."* - two lost capitals, and the instruction given twice.
   **This is repaired in the transcription** because a replicator pastes section 3 verbatim and
   the sentence is unreadable as printed.

3. **Two output-format sections disagree.** Section 11 asks for six fields. Section 12 asks for
   eight, adding composer and the numbered decline ground. The eight-field version is the one that
   matches what the residues actually carry.

**A fourth item is repaired rather than carried.** The controlled-vocabulary pass left two broken
clauses in the printed prompt: *"no title list for the the guideis in the working set"* at Draft
10.7 p. 127, and a lower-case *source* opening three sentences. Both are find-and-replace
collisions rather than drafting, and both are corrected here.

## Rule 10 applies here too

Nothing a model returns is evidence until a hand pass derives it from the source. That holds for
a screening verdict, a phase assignment, and most sharply for a discographic citation: catalogue
numbers, matrix numbers, issue dates and personnel are the class of detail a model fabricates
most confidently. The listening prompt is written to ask for the performer and album first and
the catalogue number only where the model is sure, which is a mitigation and not a fix.

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

## Start here

1. Fill in `filter_card_TEMPLATE.md`. This is the step that cannot be inherited. Everything the
   instrument excludes at Lists 1, 2 and 3 rests on it.
2. Paste your card into section 3 of `rule_13_screening_prompt.md`.
3. Attach `sources/pool_1419_alphabetical.tsv` and run in batches of twenty-five.
4. Seat what the model proposes. **The model proposes and the compiler seats** - that line is in
   the prompt and it is not decoration. A run in which the model's output is adopted unedited has
   not applied the method.
5. Close your own arithmetic with `code/verify.py`, against your total rather than this one.

**Do not close to 729.** The volume is explicit: a later run does not reconcile to this edition's
figure and should not try. A run that lands on 729 has adopted this compiler's declarations.

## What is missing, and why

Three inputs the prompts call for are not in this repository and cannot be. Levine chapter 21 and
Gioia's *The Jazz Standards* are books. Appendix G, the contrafact corpus, is the volume's own
apparatus. Without Appendix G, Stage 4 of the listening prompt is unavailable by that prompt's
own instruction, and every ladder built from this repository alone stops at Stage 3.

What is here instead is each book's residue - what it produced after screening -
at `residues/appendix_A_levine_unique_419.tsv` and `residues/appendix_D_gioia_declined_6.tsv`.

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

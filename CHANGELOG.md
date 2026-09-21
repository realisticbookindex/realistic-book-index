# Changelog

## Unreleased

- `data/vocal_option.tsv` is added, 44 rows across Indexes 1A, 1B, 2 and 3: instrumental
  seats carrying a lyric a singer can front, for the set builder. A title is entered only
  where a named recording carries the vocal. It is not the italic mark, which
  turns on a stricter test, and no printed count uses it. Two checks hold it.
- `data/setbuilder_extension.tsv` is added, 74 rows: a reading of the Index 4 seats the
  volume's style page does not classify, for the set builder alone. It is a separate file
  so that `style_classification.tsv` stays at 520 rows and the 491 and 520 printed at
  § VI.2.c and § VI.6.b stay true of it. Every row states its own basis. Two checks hold
  it, taking `code/verify.py` to 94.
- `data/style_classification.tsv` gains a `ballad` column, 75 of 520 rows marked. It is a
  reading, not a documentary fact, it has no locus in the volume, and no printed count
  depends on it. It is published rather than held privately so that a reader can disagree
  with it. `code/verify.py` holds the column against the roster.
- Nothing in the instrument moves. The prompt, its checksum, the residues, the roster and
  every route to 729 are as v15.0.1 archived them.

## v15.0.1 - for Draft 15

The v15.0.0 release archived the Draft 10.3 files in error, before these materials were committed. v15.0.1 is the first release these notes describe and the first whose prompt mirror matches the checksum printed at App. J Rule 13.

This release replaces the files built for Draft 10.3. Every file is rebuilt against Draft 15 as the Draft 14 to Draft 15 checklist leaves it; none is carried forward unchanged.

### Figures
- *Sugar* at Index 2 #70 is Stanley Turrentine's composition, not the ranking's #269 *Sugar (That Sugar Baby O' Mine)*. The ranking carries 536 of the Index, the chapter 183; the chapter's titles absent from the ranking number 420; the ranking's declines number 464; the pool is 1,420 and the declines 701.
- Gioia's *Lonely Woman* (Ornette Coleman) is not Levine's *Lonely Woman (Silver)*. 264 Gioia titles resolve into the pool and 258 are retained.
- *Secret Love* and *Can't Help Lovin' Dat Man* each carry one logged call under the folds FM.6 declares, which moves both into the Logged band.
- The panel is rebuilt from the pooled rows under the six folding rules: union 460, four titles on twelve lists, 179 on one; reach 93, 52, 88, 47, 16, 92.

### Terms
- The eight divisions are indexes throughout, as FM.3 requires. Watkins's and Miller's rosters remain lists.
- Route 3 is reported as a regrouping of Route 2, not as a third independent route.

### Files
- Removed: the scan-mark columns, which described an apparatus Draft 15 no longer has; the priority-page files, which the volume now prints with each index; the markdown copies of the prompts.
- Added: `data/vocal_band_worksheet_227.tsv`, `data/style_classification.tsv`, `data/style_contested_calls_12.tsv`, `data/name_table.tsv`, `panel/panel_sources_14.tsv`, `panel/panel_rows_pooled.tsv`, `panel/panel_union_k.tsv`, `panel/FOLDING_RULES.md`, `prompts/rule_13_screening_prompt.txt` with `prompts/SHA256SUMS`, `code/panel.py`, and `.gitattributes`, which turns off line-ending conversion so the prompt file checks out byte for byte.
- `code/verify.py` runs 89 checks at this release and keeps the exit-status contract: 0 when every check passes. Twelve of them rebuild a join from `sources/` rather than read a pre-joined column, and three hold the declared folds and the name table against the roster.

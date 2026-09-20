# Changelog

## v15.0.1 - for Draft 15. v15.0.0 archived the Draft 10.3 files in error and v15.0.1 is the first release these notes describe.

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
- `code/verify.py` runs 89 checks and keeps the exit-status contract: 0 when every check passes. Twelve of them rebuild a join from `sources/` rather than read a pre-joined column, and three hold the declared folds and the name table against the roster.

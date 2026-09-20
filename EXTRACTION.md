# Reading this volume with a machine

**Status: draft, held for the final pass.** The catalogue is complete as to what was found.
The wording, the placement and the pointer from the README are not settled.

---

## What this is

A replicator runs a machine over a document. So does anyone auditing this one. Both will
produce findings that are not in the document but in the reader they used.

This file is the record of that happening during the preparation of Draft 15, kept in the
form App. I keeps its own: left as it happened rather than tidied afterward. App. I records
the errors that came from knowing or not knowing the music. These are the ones that came
from the file format, which is a separate class and a larger one. Every finding listed
below was reported as a defect in this volume and was not one.

The purpose is practical. A replicator who reads this will not spend a pass on any of them.
The sections are ordered by how soon each one bites. The first two bite in the first
minute, and both do it silently.

---

## The rule, in one line each

Four formats answer four different questions, and each is wrong about the others.

| the question | what answers it | what does not |
|---|---|---|
| What does the text say? | the `.docx` character stream | a PDF text extraction, which inserts and drops spaces |
| What number prints here? | the render | the `.docx` list definitions, whose `start` need not match |
| Where does a line break, what is a heading, what order do the columns run in? | the render's glyph coordinates | the paragraph elements in the XML, and the extractor's block order |
| Is there a space between these two words? | the glyph geometry | all of the above |

A claim made in the wrong format is not a weak finding. It is a finding about the
extractor.

---

## The catalogue

### 1. The list marker, and the character between it and the title

**What is there.** Every numbered entry in this volume carries a zero-width space, U+200B,
between the marker and the text. There are **4,209 of them in the printed render**. One
entry is four spans in three typefaces:

```
line text: '1.\u200b Shaw Nuff '
   span '1.'           font=CenturySchoolbook-Bold
   span '\u200b'       font=TimesNewRomanPS-BoldMT
   span ' '            font=CenturySchoolbook
   span 'Shaw Nuff '   font=CenturySchoolbook
```

**What it does to a first script.**

```
^\d+\.\s+(.*)$     ->  NO MATCH          the obvious pattern fails outright
^\d+\.\s*(.*)$     ->  '\u200b Shaw Nuff'   captures the invisible character into the title
^\d+\.[\s\u200b]*(.*)$  ->  'Shaw Nuff'       correct
```

The second is the dangerous one. It matches, it looks right when printed to a terminal, and
every title it produces then fails to join to anything. A replicator who sees a join rate
near zero should check this before checking anything else.

**The test.** Strip U+200B, U+00A0 and U+2011 before matching, and assert that the
character set of your extracted titles is what you expect:

```python
import collections
odd = collections.Counter(ch for t in titles for ch in t if ord(ch) > 126)
```

Ten non-breaking hyphens, U+2011, also print in this volume, inside titles such as *Hi-Fly*
and *Pent-Up House*. Title identity strips them, so they cost nothing once the join runs
through `norm.identity`, and they break a raw string comparison.

### 2. Columns, and the order a reader takes them in

**What is there.** The index pages set two and three columns, and a band's list runs on from
one column into the next. Page 27 of Draft 15-3 carries nine distinct left edges - 54, 63,
72, 81, 201, 234, 243, 260, 423 - because indents and column edges are mixed in the same
coordinate.

**What it does.** Sorting lines by vertical position, which is what a hand-rolled reader
does and what several tools do by default, interleaves the columns:

```
what the page shows                    what a sort by y returns
RHYTHM CHANGES                         RHYTHM CHANGES
Sub-Floor                              Untouched, reserved
1. Shaw Nuff                           9. Passion Dance
2. Salt Peanuts                        1. C.T.A.
3. Dexterity                           Sub-Floor
...                                    10. Spain
Untouched                              1. Shaw Nuff
1. Move                                11. The Moontrane
```

The roster order is destroyed and the band attribution goes with it. Every count taken from
that stream is wrong, and nothing about it looks wrong.

**The test.** Cluster on the left edge first, order the clusters left to right, then order
within a cluster by vertical position - and expect a list to continue across a cluster
boundary rather than to end at one. `NOT ORDERED *` on that page runs 1 through 8 in the
middle column and 9 through 12 in the right. Confirm the result by counting a roster you
can count by eye: the eight alphabetical runs should return 93, 53, 116, 141, 99, 80, 78
and 69.

### 3. Word spacing at a formatting boundary

**What the extractor does.** A PDF text extraction reconstructs spaces from glyph
positions. Where a run changes font, size or weight, it inserts a space that is not there
or drops one that is. The same document extracted twice, by two libraries, disagrees with
itself.

**What it produced here.** Eleven missing-space findings in one pass, every one at a
formatting boundary and none of them real. A twelfth, `every one carrying a rank.No two
share a rank`, read *with* a space in one extraction and had none in the render.

**The test.** Measure the gap between the two glyphs. In this volume a normal same-line
sentence break is about 6.6 points at 12 point body text. A real missing space measures
0.0. Anything between is the extractor.

```python
import pymupdf
chars = [c for blk in page.get_text("rawdict")["blocks"]
           for line in blk["lines"] for sp in line["spans"] for c in sp["chars"]]
gap = chars[i+1]["bbox"][0] - chars[i]["bbox"][2]     # same line only
```

Five real cases survive this test in Draft 15-3, at 0.0 points each. The eleven did not.

### 4. Generated list numbers

**What the extractor does.** This volume is authored in Google Docs. Docs keeps its own
list continuation state. On export it writes each list as a separate `abstractNum` whose
`start` does not always match what Docs renders, so Word and any XML reader see one number
and every reader of the document sees another.

**What it produced here.** § VI was reported as running 1, 2, 3, 3, 5, 6, with the
skill-path heading printing 3 where it should print 4. The XML says `start=3`. The page
prints 4. § VI was correct throughout.

**The test.** Read the number off a render. A claim about a printed number cannot be made
from `numbering.xml` at all.

### 5. A line break is not a paragraph break

**What the extractor does.** Nothing wrong. The reader does: it treats one paragraph as one
line, and a paragraph that wraps looks in the XML exactly like a paragraph that does not.

**What it produced here.** At Index 2.3 the block header and the band header sit in one
paragraph carrying two runs, `RHYTHM CHANGES ` and `Sub-Floor`. Reported as a merged
heading needing a split. The page prints them on two baselines, 20.7 points apart at the
same left edge, in the same two faces every other block and band pair uses, because the set
width of the whole string is marginally wider than the column. A reader sees two headers.
No edit was needed.

**What it cost.** Four further findings downstream. A parser segmenting on exact header
strings did not recognize the merged one, kept reading the preceding minor-blues band, and
reported four rhythm-changes titles as out of the priority order. With the block delimited
as the page delimits it, all 729 seats are in order at every position.

**The test.** Compare baseline `y` in the render. Two baselines is two lines, whatever the
XML says. And before reporting a structural finding about a heading, look at the heading.

### 6. Block and band segmentation

**What the extractor does.** A segmenter keyed on exact strings mis-attributes every entry
after a header it does not recognize, and the error propagates to the end of the section.

**What it produced here.** A first call-order pass reported 278 defects across 729 seats.
The second reported 8. The third reported 3. The correct figure was 0.

**The test.** The tell was available at the first pass and was missed. Indexes 4, 5A, 5B
and 5C came back perfectly clean while the others did not - and those four are the indexes
with no form blocks. A defect concentrated in exactly the structures the parser handles
specially is a parser finding. Segment on what the render shows as a heading, not on a
string table. The band headers themselves are not a fixed vocabulary: the three Untouched
grounds print under nine different strings in this edition, and `Sub-Floor` appears both
with a plain hyphen and with U+2011.

### 7. Column order inside a data file

**What it produced here.** Two titles reported as absent from Watkins's List 2. The join
had read the `contributors` column where `title_as_printed` was meant. Separately, an
alphabetized ranking file was read with its two columns reversed, producing a false alarm
about a swapped header.

**The test.** Print the header row and one data row before joining anything. It costs one
line and it has caught two of these.

### 8. Title identity

**What the extractor does.** Nothing. The failure is in the join, and it is the single
largest source of false findings in this material.

**What it produced here.** *(You're A) Weaver Of Dreams* reported as a data defect: the
name resolves through `norm.identity`, which the README documents. Six spellings in this
repository's own source files reported as divergences from App. E: leading parentheticals,
a dropped subtitle, a misspelling cited as its source prints it. Twenty-six spellings in
Levine's chapter that return 444 unique titles where App. A prints 420. Three in Gioia that
leave seated titles looking unwarranted.

**The test.** Join through `norm.match_key` with `aliases.SEATED` and the name table
applied, and treat every remaining miss as a fold candidate rather than a finding, until
the render says otherwise. One fold in this repository is valid for a single source and
wrong for the others; it is in `aliases.BY_SOURCE` and the reason is stated there.

The general point is stronger than the mechanism. A title is not a string. Two spellings of
one composition and one spelling of two compositions both occur in this material, and the
second is worse: Levine's chapter carries two different pieces called *Milestones* and an
automated pass merged them. App. I records that one.

### 9. Truncation against a wrap

**What it produced here.** Three entries in the index runs failed to join to the roster.
Two - `You and the Night` and `Upper Manhattan` at Index 2.3 - are titles typed across a
numbered paragraph and an unnumbered one. They print correctly, take one number each, and
are a join problem rather than a page problem. The third, `Bolivar Blu` at Index 3.2 entry
95, is a real truncation: the render prints it and then prints `96. Buzzy`, with nothing
continuing it.

**The test.** For every join miss, look at the next rendered line. If it continues the
title, the page is right. If it starts the next entry, the page is wrong.

### 10. A tool's figure against the document's figure

**What it produced here.** A priority-order parser reported 722 seats where the volume
prints 729, which was read as seven titles lost in an edit. Nothing was lost. That parser
counts only the entries it segments into bands and had returned 722 on every draft it had
ever been run against. The figure was never 729 and no one had checked.

**The test.** Compare a tool's output to the same tool's output on the previous draft, not
to a figure from the document. A number that differs from the page may mean the page is
wrong, or it may mean the tool has never agreed with the page. Establishing that baseline
takes one run and settles which.

---

## The order these checks belong in

1. **Clean the extraction and prove it.** Strip the invisible characters, resolve the
   columns, and count the eight alphabetical runs against 93, 53, 116, 141, 99, 80, 78, 69.
   Do not proceed on an extraction that does not return those.
2. **Diff the drafts**, if there is a previous one. Line-level, both directions. This
   establishes what actually changed and makes every later surprise attributable.
3. **Join the printed rosters to the data files**, title by title, with the declared folds
   applied. This is the check that finds truncations, and it found the only one here.
4. **Resolve the pointers**, then **evaluate the arithmetic**, every derivation against its
   own stated formula. Sixteen of eighteen derivations in TABLE R.4 closed; the two that did
   not traced to one cell.
5. **Read numbers off the render.** Never from the list definitions.
6. **Read layout off the render.** Baselines and left edges, not paragraphs.
7. **Measure spacing at the glyph level, or leave it alone.** In this volume the spacing
   class is closed for exactly this reason, and it was closed after two passes produced
   edits that were not needed.

---

## Why this is kept

App. I closes its own error list with a sentence that governs this one: "A method that
reports no errors reports only that it did not look."

The findings above were reported and withdrawn. Keeping them costs nothing and tells a
replicator which of their own findings to doubt first. A reader who wants to take exception
to this volume is better served by knowing where a machine will lie to them than by a
record in which no machine ever did.

Corrections to this file go where every other correction goes, at App. L.8.

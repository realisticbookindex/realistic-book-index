"""Title identity for The Realistic Book Index, Draft 15.

Two strings name the same title when identity() returns the same value.
match_key() is identity() with a leading article removed; it is used only to
join one source's spelling to another's, and every join that needs more than
match_key() is declared in aliases.py.
"""
import re
import unicodedata

# Performance keys and similar notes printed inside a title cell (folding rule 1).
KEY_PAREN = re.compile(
    r"\((?:[A-G][b#]?m?(?:\s+and\s+[A-G][b#]?m?)*|monk changes|faster|a section only|horace silver)\)",
    re.I)
AKA_PAREN = re.compile(r"\(\s*(?:aka|a\.k\.a\.|also known as)\b[^)]*\)", re.I)
TAGS = re.compile(r"\[(?:P|E|Q)\]")


def identity(title):
    t = TAGS.sub(" ", title)
    t = KEY_PAREN.sub(" ", t)
    t = AKA_PAREN.sub(" ", t)
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("&", " and ")
    t = t.lower()
    return re.sub(r"[^a-z0-9]+", "", t)


def match_key(title):
    t = title.strip()
    t = re.sub(r",\s*(the|a|an)\s*$", "", t, flags=re.I)
    t = re.sub(r"^\((the|a|an)\)\s*", "", t, flags=re.I)
    t = re.sub(r"^(the|a|an)\s+", "", t, flags=re.I)
    return identity(t)


def alphakey(title):
    """FM.1.f filing key: articles included, word by word, apostrophes and punctuation ignored."""
    t = unicodedata.normalize("NFKD", title)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("’", "'").replace("‘", "'").lower()
    t = re.sub(r"[-/]", " ", t)
    t = re.sub(r"[^a-z0-9 ]", "", t)
    return re.sub(r"\s+", " ", t).strip()

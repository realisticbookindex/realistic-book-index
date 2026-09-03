import re, unicodedata
def _core(s, keep_parens):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"')
    s=re.sub(r'\[[^\]]*\]','',s)
    if keep_parens:
        s=s.replace('(',' ').replace(')',' ')
        s=re.sub(r'\bAKA\b','',s,flags=re.I)
    else:
        s=re.sub(r'\([^)]*\)?','',s)          # closed or unclosed
    s=unicodedata.normalize('NFKD',s)
    s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.lower().strip()
    m=re.match(r"^(.*),\s*(the|a|an)$", s)
    if m: s=m.group(2)+' '+m.group(1)
    s=s.replace('&',' and ')
    s=re.sub(r"'",'',s)
    s=re.sub(r'^(the|a|an)\s+','',s)
    s=re.sub(r'\bmr\.?\b','mister',s)
    s=re.sub(r'\bst\.?\b','saint',s)
    return re.sub(r'[^a-z0-9]','',s)
def base(s): return _core(s, False)
def full(s): return _core(s, True)

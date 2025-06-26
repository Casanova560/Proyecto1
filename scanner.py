import re

TOKEN_PATTERNS = [
    ('ART',    r'\b(?:a|the)\b'),
    ('NOUN',   r'\b(?:cat|mat|rat)\b'),
    ('VERB',   r'\b(?:like|is|see|sees)\b'),
    ('ME',     r'\bme\b'),
    ('PERIOD', r'\.'),
    ('SKIP',   r'[ \t]+'),
    ('ERROR',  r'.'),
]

_pattern = re.compile(
    '|'.join(f'(?P<{name}>{pat})' for name, pat in TOKEN_PATTERNS),
    re.IGNORECASE
)

class ScanError(Exception):
    pass

def scan(line):
    tokens = []
    for m in _pattern.finditer(line):
        kind = m.lastgroup
        txt  = m.group().lower()
        if kind == 'SKIP':
            continue
        if kind == 'ERROR':
            raise ScanError(f"Carácter inesperado: '{txt}'")
        tokens.append((kind, txt))
    return tokens


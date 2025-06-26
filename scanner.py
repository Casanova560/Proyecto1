import re

TOKEN_PATTERNS = [
    ('ART', r'\b(?:the|a)\b'),
    ('N', r'\b(?:cat|dog|man|woman|telescope|park|boy|girl)\b'),
    ('V', r'\b(?:saw|liked|walked)\b'),
    ('PREP', r'\b(?:in|with|on)\b'),
    ('PERIOD', r'\.'),
    ('SKIP', r'[ \t]+'),
    ('ERROR', r'.'),
]

_master_pattern = re.compile(
    '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_PATTERNS),
    re.IGNORECASE
)

class ScanError(Exception):
    pass

def scan(text):
    tokens = []
    for m in _master_pattern.finditer(text):
        kind = m.lastgroup
        tok = m.group().lower()
        if kind == 'SKIP':
            continue
        if kind == 'ERROR':
            raise ScanError(f"Carácter inesperado: '{tok}'")
        tokens.append((kind, tok))
    return tokens

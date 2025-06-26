class ParseError(Exception):
    pass

def analyze(tokens):
    pos = 0

    def expect(ttype, val=None):
        nonlocal pos
        if pos < len(tokens) and tokens[pos][0] == ttype and (val is None or tokens[pos][1] == val):
            pos += 1
        else:
            found = tokens[pos] if pos < len(tokens) else 'EOF'
            exp = ttype + (f"('{val}')" if val else "")
            raise ParseError(f"Se esperaba {exp}, encontrado {found}")

    def subject():
        # <subject> ::= ε | a NOUN | the NOUN
        if pos < len(tokens) and tokens[pos][0] == 'ART':
            expect('ART')
            expect('NOUN')

    def verb():
        # <verb> ::= like | is | see | sees
        expect('VERB')

    def obj():
        # <object> ::= me | a NOUN | the NOUN
        if pos < len(tokens) and tokens[pos][0] == 'ME':
            expect('ME')
        else:
            expect('ART')
            expect('NOUN')

    # <sentence> ::= <subject> <verb> <object> PERIOD
    subject()
    verb()
    obj()
    expect('PERIOD')

    if pos != len(tokens):
        resto = tokens[pos:]
        raise ParseError(f"Tokens sobrantes: {resto}")

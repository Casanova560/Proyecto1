class ParseError(Exception):
    pass

def analyze(tokens):
    pos = 0

    def expect(ttype):
        nonlocal pos
        if pos < len(tokens) and tokens[pos][0] == ttype:
            pos += 1
        else:
            actual = tokens[pos] if pos < len(tokens) else 'EOF'
            raise ParseError(f"Se esperaba {ttype}, encontrado {actual}")

    def np():
        expect('ART')
        expect('N')

    def vp():
        expect('V')
        np()
        if pos < len(tokens) and tokens[pos][0] == 'PREP':
            expect('PREP')
            np()

    np()
    vp()
    expect('PERIOD')

    if pos != len(tokens):
        resto = tokens[pos:]
        raise ParseError(f"Tokens sobrantes: {resto}")
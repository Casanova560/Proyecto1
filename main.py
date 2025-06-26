import sys
from scanner import scan, ScanError
from syntax_analyzer import analyze, ParseError

def procesar(entrada, salida):
    resultados = []
    try:
        with open(entrada, encoding='utf-8') as f:
            lines = [l.strip() for l in f if l.strip()]
    except IOError as e:
        print(f"Error al leer '{entrada}': {e}")
        sys.exit(1)

    for i, line in enumerate(lines, 1):
        resultados.append(f"Oración {i}: «{line}»")
        # Léxico
        try:
            tokens = scan(line)
            resultados.append("  Léxico: OK")
        except ScanError as e:
            resultados.append(f"  Léxico: ERROR → {e}")
            resultados.append("")  # línea en blanco
            continue
        # Sintáctico
        try:
            analyze(tokens)
            resultados.append("  Sintáctico: OK")
        except ParseError as e:
            resultados.append(f"  Sintáctico: ERROR → {e}")
        resultados.append("")

    try:
        with open(salida, 'w', encoding='utf-8') as f:
            f.write("\n".join(resultados))
    except IOError as e:
        print(f"Error al escribir '{salida}': {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python main.py <archivo_entrada> <archivo_salida>")
        sys.exit(1)
    procesar(sys.argv[1], sys.argv[2])



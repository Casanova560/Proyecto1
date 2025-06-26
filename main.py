import sys
from scanner import scan, ScanError
from syntax_analyzer import analyze, ParseError

def procesar(archivo_entrada, archivo_salida):
    resultados = []
    try:
        with open(archivo_entrada, encoding='utf-8') as fin:
            lineas = [l.rstrip() for l in fin if l.strip()]
    except IOError as e:
        print(f"Error al leer '{archivo_entrada}': {e}")
        sys.exit(1)

    for i, linea in enumerate(lineas, 1):
        resultados.append(f"Oración {i}: «{linea}»")
        try:
            tokens = scan(linea)
            resultados.append("  Léxico: OK")
        except ScanError as e:
            resultados.append(f"  Léxico: ERROR → {e}")
            resultados.append("")
            continue

        try:
            analyze(tokens)
            resultados.append("  Sintáctico: OK")
        except ParseError as e:
            resultados.append(f"  Sintáctico: ERROR → {e}")
        resultados.append("")

    try:
        with open(archivo_salida, 'w', encoding='utf-8') as fout:
            fout.write("\n".join(resultados))
    except IOError as e:
        print(f"Error al escribir '{archivo_salida}': {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python main.py <archivo_entrada> <archivo_salida>")
        sys.exit(1)
    procesar(sys.argv[1], sys.argv[2])


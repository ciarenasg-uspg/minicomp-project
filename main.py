# main.py

from lexer.lexer import Lexer


def main():

    codigo = """
    entero x = 10;
    x = x + 5;
    """

    print("=" * 60)
    print("COMPILADOR - ENTREGA 1")
    print("=" * 60)

    print("\n[CODIGO FUENTE]")
    print(codigo)

    # -------------------------------------------------
    # FASE 1: ANALISIS LEXICO
    # -------------------------------------------------

    lexer = Lexer(codigo)
    tokens = lexer.analizar()
    print("[TOKENS]")

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()

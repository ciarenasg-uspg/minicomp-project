Entrega 1 — Lexer

Completar el Lexer proporcionado por el catedratico.

Implementar
PR_SI
PR_MIENTRAS
PR_IMPRIMIR
OP_REL
Tokens adicionales propuestos en la tarea anterior.

OP_REL debe reconocer:  ==  !=  <  >  <=  >=

Prueba: El Lexer debe procesar correctamente el siguiente código en main.py

codigo = """
entero x = 10;
entero limite = 20;

mientras (x <= limite) {
    si (x != 15) {
        imprimir x;
    }
    x = x + 2;
}
"""

Debe generar correctamente los tokens, incluyendo sus valores y números de línea.

Entrega

lexer.py
main.py

Esta entrega corresponde únicamente al análisis léxico.
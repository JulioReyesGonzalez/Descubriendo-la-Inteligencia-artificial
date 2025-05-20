"""
-------------------------------------------------------
🤏 BÚSQUEDA LOCAL CON MÍNIMOS CONFLICTOS (MIN-CONFLICTS)
-------------------------------------------------------

📌 ¿Qué es Min-Conflicts?
Es un algoritmo local para resolver CSPs que **ajusta las asignaciones actuales**
intentando reducir el número de conflictos en cada paso.

📌 ¿Cómo funciona?
1. Comienza con una asignación aleatoria.
2. Mientras haya conflictos:
   - Selecciona una variable conflictiva.
   - Asigna un valor que minimice los conflictos.

📌 Ventajas:
- Muy rápido en problemas grandes.
- Eficiente en CSPs densos o de estructura regular (como Sudoku o N-Reinas).

📌 Desventajas:
- No garantiza solución si el problema no tiene.
- Puede estancarse si se queda en un mínimo local.

📌 Ejemplo personalizado:
Resolver el clásico problema de las **8 reinas**, donde cada reina debe estar
en una fila diferente sin atacarse entre sí (columnas y diagonales).

-------------------------------------------------------
"""

import random

def conflictos(tablero, col, fila):
    conflictos = 0
    for c in range(len(tablero)):
        if c != col:
            f = tablero[c]
            if f == fila or abs(f - fila) == abs(c - col):
                conflictos += 1
    return conflictos

def min_conflicts(n=8, max_iter=1000):
    tablero = [random.randint(0, n - 1) for _ in range(n)]

    for _ in range(max_iter):
        conflictuadas = [c for c in range(n) if conflictos(tablero, c, tablero[c]) > 0]
        if not conflictuadas:
            return tablero  # Solución encontrada

        col = random.choice(conflictuadas)
        min_fila = min(range(n), key=lambda f: conflictos(tablero, col, f))
        tablero[col] = min_fila

    return None  # No se encontró solución en el tiempo dado

solucion = min_conflicts()
if solucion:
    print("Solución encontrada para 8 reinas:")
    for i in range(8):
        fila = ['Q' if solucion[j] == i else '.' for j in range(8)]
        print(' '.join(fila))
else:
    print("No se encontró solución.")

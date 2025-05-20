"""
-------------------------------------------------------
🔙 SATISFACCIÓN DE RESTRICCIONES - BÚSQUEDA DE VUELTA ATRÁS
-------------------------------------------------------

📌 ¿Qué es la búsqueda de vuelta atrás?
Es una técnica de exploración de espacios de solución que **prueba valores** 
y **retrocede (backtrack)** cuando una asignación no cumple las restricciones.

📌 Características:
- Es recursiva y sistemática.
- Explora todas las combinaciones posibles (si es necesario).
- Detiene la exploración al encontrar una solución válida (si se desea).

📌 Ejemplo personalizado:
Resolver un mini-Sudoku de 4x4 donde el objetivo es completar el tablero
respetando las reglas: los números del 1 al 4 no pueden repetirse por fila,
columna ni subcuadro 2x2.

-------------------------------------------------------
"""
def es_seguro(tablero, fila, col, num):
    for i in range(4):
        if tablero[fila][i] == num or tablero[i][col] == num:
            return False

    inicio_fila, inicio_col = 2 * (fila // 2), 2 * (col // 2)
    for i in range(inicio_fila, inicio_fila + 2):
        for j in range(inicio_col, inicio_col + 2):
            if tablero[i][j] == num:
                return False
    return True

def resolver_sudoku(tablero):
    for fila in range(4):
        for col in range(4):
            if tablero[fila][col] == 0:
                for num in range(1, 5):
                    if es_seguro(tablero, fila, col, num):
                        tablero[fila][col] = num
                        if resolver_sudoku(tablero):
                            return True
                        tablero[fila][col] = 0  # backtrack
                return False
    return True

# Mini-Sudoku 4x4 (0 = vacío)
sudoku = [
    [1, 0, 0, 4],
    [0, 0, 1, 0],
    [4, 0, 0, 2],
    [0, 1, 0, 0]
]

if resolver_sudoku(sudoku):
    print("Sudoku resuelto:")
    for fila in sudoku:
        print(fila)
else:
    print("No se encontró solución.")

"""
-------------------------------------------------------
🔁 SATISFACCIÓN DE RESTRICCIONES - PROPAGACIÓN DE RESTRICCIONES
-------------------------------------------------------

📌 ¿Qué es la propagación de restricciones?
Es una técnica que **reduce los dominios de las variables** propagando las
restricciones a lo largo del grafo de variables.

📌 ¿Cómo funciona?
- Cuando se asigna un valor a una variable, las restricciones se aplican
  a sus vecinos y se eliminan valores no válidos de sus dominios.
- Esto se propaga recursivamente hasta que no hay más cambios o se detecta inconsistencia.

📌 Beneficios:
- Reduce drásticamente el espacio de búsqueda.
- Puede detectar inconsistencias antes de explorar profundamente.

📌 Relación con otros algoritmos:
- Es una extensión de la comprobación hacia adelante.
- Se puede usar junto con backtracking o como preprocesamiento (AC-3, etc.).

📌 Ejemplo personalizado:
Se asignan horarios a profesores, asegurando que no se crucen clases
que comparten maestro o salón, propagando las restricciones.

-------------------------------------------------------
"""
from collections import deque

def ac3(variables, dominios, restricciones):
    cola = deque([(x, y) for x in variables for y in restricciones.get(x, [])])

    while cola:
        xi, xj = cola.popleft()
        if reducir(xi, xj, dominios):
            if not dominios[xi]:
                return False  # Inconsistencia encontrada
            for xk in restricciones[xi]:
                if xk != xj:
                    cola.append((xk, xi))
    return True

def reducir(xi, xj, dominios):
    eliminado = False
    for valor in dominios[xi][:]:
        if not any(valor != v for v in dominios[xj]):
            dominios[xi].remove(valor)
            eliminado = True
    return eliminado

# Variables y restricciones (horarios para 3 materias)
variables = ['Mate', 'Fisica', 'Quimica']
dominios = {
    'Mate': [1, 2, 3],
    'Fisica': [1, 2, 3],
    'Quimica': [1, 2, 3]
}
# Fisica y Quimica no pueden tener el mismo horario (comparten laboratorio)
# Mate y Fisica no pueden coincidir (mismo profesor)
restricciones = {
    'Mate': ['Fisica'],
    'Fisica': ['Mate', 'Quimica'],
    'Quimica': ['Fisica']
}

print("Dominios antes de AC-3:", dominios)
ac3(variables, dominios, restricciones)
print("Dominios después de AC-3:", dominios)


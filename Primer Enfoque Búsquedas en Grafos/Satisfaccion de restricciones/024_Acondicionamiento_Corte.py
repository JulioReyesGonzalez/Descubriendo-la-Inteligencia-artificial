"""
-------------------------------------------------------
✂️ SATISFACCIÓN DE RESTRICCIONES - ACONDICIONAMIENTO DEL CORTE
-------------------------------------------------------

📌 ¿Qué es el acondicionamiento del corte (cutset conditioning)?
Es una técnica avanzada para resolver CSPs complejos transformándolos en
problemas más simples. Elimina un pequeño conjunto de variables (cutset) y
resuelve el resto con un algoritmo eficiente (como backtracking o AC-3).

📌 ¿Cuándo se usa?
- En CSPs con muchos ciclos (no son árboles).
- Cuando se puede convertir en árbol eliminando pocas variables.

📌 ¿Cómo funciona?
1. Se identifica un **cutset** (conjunto de variables cuya remoción deja el grafo como árbol).
2. Se generan todas las posibles asignaciones del cutset.
3. Por cada asignación del cutset, se resuelve el CSP restante.

📌 Ejemplo personalizado:
Asignar colores a 5 regiones de un mapa. Eliminamos 1 región (cutset) y resolvemos
las otras como si el mapa fuera un árbol (más fácil de procesar).

-------------------------------------------------------
"""
import itertools

def es_valida(asignacion, restricciones):
    for var, vecinos in restricciones.items():
        for vecino in vecinos:
            if vecino in asignacion and asignacion.get(var) == asignacion[vecino]:
                return False
    return True

def backtracking_csp(variables, dominios, restricciones, asignacion={}):
    if len(asignacion) == len(variables):
        return asignacion

    var = [v for v in variables if v not in asignacion][0]
    for valor in dominios[var]:
        asignacion[var] = valor
        if es_valida(asignacion, restricciones):
            resultado = backtracking_csp(variables, dominios, restricciones, asignacion)
            if resultado:
                return resultado
        asignacion.pop(var)
    return None

def cutset_conditioning(variables, dominios, restricciones, cutset):
    restantes = [v for v in variables if v not in cutset]
    cutset_dominios = [dominios[v] for v in cutset]

    for combinacion in itertools.product(*cutset_dominios):
        asignacion_inicial = dict(zip(cutset, combinacion))
        if not es_valida(asignacion_inicial, restricciones):
            continue
        resultado = backtracking_csp(restantes, dominios, restricciones, asignacion_inicial.copy())
        if resultado:
            return resultado
    return None

# Variables y restricciones (mapa de 5 regiones)
variables = ['A', 'B', 'C', 'D', 'E']
dominios = {v: ['Rojo', 'Verde', 'Azul'] for v in variables}
restricciones = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C'],
    'E': ['C']
}

# 'C' es el cutset
solucion = cutset_conditioning(variables, dominios, restricciones, cutset=['C'])
print("Asignación con cutset conditioning:", solucion)


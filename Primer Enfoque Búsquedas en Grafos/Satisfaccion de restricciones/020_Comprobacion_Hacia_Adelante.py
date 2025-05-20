"""
-------------------------------------------------------
🔄 SATISFACCIÓN DE RESTRICCIONES - COMPROBACIÓN HACIA ADELANTE
-------------------------------------------------------

📌 ¿Qué es la comprobación hacia adelante?
Es una mejora del backtracking que, **cada vez que se asigna un valor**, elimina
los valores inválidos de los dominios de las variables no asignadas.

📌 Ventajas:
- Detecta fallos antes (early detection).
- Evita recorrer ramas del árbol que ya se sabe que fallarán.

📌 ¿Cómo funciona?
1. Al asignar un valor a una variable, se mira cómo afecta a las demás.
2. Si alguna variable se queda sin valores válidos, se hace backtrack.

📌 Ejemplo personalizado:
Colorear un mapa de regiones donde se eliminan los colores inválidos de los vecinos
en cuanto se asigna un color a una región.

-------------------------------------------------------
"""
def es_valido(valor, var, asignacion, restricciones):
    for vecino in restricciones.get(var, []):
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

def forward_checking(variables, dominios, restricciones, asignacion={}):
    if len(asignacion) == len(variables):
        return asignacion

    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        if es_valido(valor, var, asignacion, restricciones):
            asignacion[var] = valor
            nuevos_dominios = {v: list(dominios[v]) for v in dominios}
            consistent = True

            for vecino in restricciones.get(var, []):
                if vecino not in asignacion and valor in nuevos_dominios[vecino]:
                    nuevos_dominios[vecino].remove(valor)
                    if not nuevos_dominios[vecino]:
                        consistent = False
                        break

            if consistent:
                resultado = forward_checking(variables, nuevos_dominios, restricciones, asignacion)
                if resultado:
                    return resultado

            asignacion.pop(var)

    return None

# Variables y restricciones (mapa de 4 regiones)
variables = ['X', 'Y', 'Z', 'W']
dominios = {v: ['Rojo', 'Verde', 'Azul'] for v in variables}
restricciones = {
    'X': ['Y', 'Z'],
    'Y': ['X', 'Z'],
    'Z': ['X', 'Y', 'W'],
    'W': ['Z']
}

solucion = forward_checking(variables, dominios, restricciones)
print("Asignación con forward checking:", solucion)


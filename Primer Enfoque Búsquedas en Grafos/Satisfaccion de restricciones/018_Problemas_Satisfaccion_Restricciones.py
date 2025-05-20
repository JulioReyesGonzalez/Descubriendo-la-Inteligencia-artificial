"""
-------------------------------------------------------
🎯 SATISFACCIÓN DE RESTRICCIONES - INTRODUCCIÓN A CSP
-------------------------------------------------------

📌 ¿Qué es un CSP?
Un **Problema de Satisfacción de Restricciones** (CSP) busca asignar valores
a un conjunto de variables cumpliendo una serie de restricciones.

📌 Elementos clave:
- Variables: lo que hay que asignar (ej. colores, horarios, posiciones)
- Dominios: posibles valores para cada variable
- Restricciones: reglas que limitan las combinaciones válidas

📌 Aplicaciones:
- Coloreo de mapas
- Horarios de clases
- Sudoku y rompecabezas
- Configuración de sistemas

📌 Ejemplo personalizado:
Coloreado de un pequeño mapa con 4 regiones (A, B, C, D) usando
3 colores disponibles (Rojo, Verde, Azul) sin que dos regiones
vecinas compartan color.

-------------------------------------------------------
"""
def es_valida(asignacion, restricciones, var, valor):
    for vecino in restricciones.get(var, []):
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

def csp_coloreo(variables, dominios, restricciones, asignacion={}):
    if len(asignacion) == len(variables):
        return asignacion

    var = [v for v in variables if v not in asignacion][0]
    for valor in dominios[var]:
        if es_valida(asignacion, restricciones, var, valor):
            asignacion[var] = valor
            resultado = csp_coloreo(variables, dominios, restricciones, asignacion)
            if resultado:
                return resultado
            asignacion.pop(var)
    return None

# Variables: regiones del mapa
variables = ['A', 'B', 'C', 'D']
# Dominio de colores para cada región
dominios = {v: ['Rojo', 'Verde', 'Azul'] for v in variables}
# Restricciones (regiones vecinas no pueden tener el mismo color)
restricciones = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

solucion = csp_coloreo(variables, dominios, restricciones)
print("Colores asignados:", solucion)


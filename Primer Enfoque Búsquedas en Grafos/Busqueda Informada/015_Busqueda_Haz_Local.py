"""
-------------------------------------------------------
?? BÚSQUEDA INFORMADA - BÚSQUEDA DE HAZ LOCAL
-------------------------------------------------------

?? ¿Qué es la búsqueda de haz local?
Es una variante de la búsqueda local que **mantiene múltiples estados** (k candidatos)
en cada paso, en lugar de uno solo como en Hill Climbing.

?? ¿Cómo funciona?
- Se generan k estados iniciales aleatorios.
- En cada iteración, se generan los vecinos de todos ellos.
- Se seleccionan los k mejores y se repite.
- Puede converger hacia múltiples óptimos en paralelo.

?? Ventajas:
- Más robusta que Hill Climbing simple.
- Menos propensa a quedar atrapada en óptimos locales.

?? Desventajas:
- Si todos los caminos convergen al mismo punto, no mejora la diversidad.

?? Ejemplo personalizado:
Un sistema de logística busca la mejor ruta de entrega manteniendo 3 soluciones
paralelas y eligiendo siempre las rutas de menor costo en cada iteración.

-------------------------------------------------------
"""
import random

def costo_ruta(ruta, distancias):
    return sum(distancias.get((ruta[i], ruta[i+1]), 10) for i in range(len(ruta) - 1))

def vecinos(ruta):
    rutas = []
    for i in range(len(ruta)):
        for j in range(i + 1, len(ruta)):
            nueva = list(ruta)
            nueva[i], nueva[j] = nueva[j], nueva[i]
            rutas.append(nueva)
    return rutas

def haz_local(ciudades, distancias, haz=3, iteraciones=100):
    soluciones = [random.sample(ciudades, len(ciudades)) for _ in range(haz)]

    for _ in range(iteraciones):
        todos_vecinos = []
        for ruta in soluciones:
            todos_vecinos.extend(vecinos(ruta))
        soluciones = sorted(todos_vecinos, key=lambda r: costo_ruta(r, distancias))[:haz]

    mejor = min(soluciones, key=lambda r: costo_ruta(r, distancias))
    return mejor, costo_ruta(mejor, distancias)

# Ciudades ficticias y distancias simuladas
ciudades = ['C1', 'C2', 'C3', 'C4', 'C5']
distancias = {
    ('C1', 'C2'): 3, ('C2', 'C3'): 6, ('C3', 'C4'): 2,
    ('C4', 'C5'): 5, ('C5', 'C1'): 7, ('C1', 'C3'): 4,
    ('C2', 'C4'): 3, ('C3', 'C5'): 5, ('C4', 'C1'): 6, ('C5', 'C2'): 4
}

resultado, costo = haz_local(ciudades, distancias, haz=3)
print("Mejor ruta encontrada:", resultado)
print("Costo total:", costo)


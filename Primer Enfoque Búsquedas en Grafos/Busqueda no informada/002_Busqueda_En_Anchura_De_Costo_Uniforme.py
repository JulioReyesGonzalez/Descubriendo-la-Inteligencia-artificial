"""
-------------------------------------------------------
🔍 BÚSQUEDA NO INFORMADA - BÚSQUEDA EN ANCHURA DE COSTO UNIFORME (UCS)
-------------------------------------------------------

📌 ¿Qué es la búsqueda de costo uniforme?
Es una variación de la búsqueda en anchura (BFS), pero en lugar de expandir
los nodos por nivel (profundidad), expande por el **costo acumulado más bajo**.

Es ideal para encontrar el camino más barato en un grafo ponderado sin usar heurísticas.

📌 Diferencia con BFS:
- BFS asume que todos los costos son iguales (nivel por nivel).
- UCS se adapta a grafos con **costos reales** distintos entre los caminos.

📌 ¿Cómo funciona?
- Utiliza una **cola de prioridad** (ordenada por costo total acumulado).
- Siempre elige expandir el camino de menor costo actual.
- Es **óptimo** y **completo**, como A*, pero sin heurística.

📌 Ejemplo personalizado:
Supongamos que queremos entregar correspondencia en una red de barrios con calles
que tienen distintos costos de tiempo (en minutos).

-------------------------------------------------------
"""
import heapq

def costo_uniforme(grafo, inicio, objetivo):
    # Cola de prioridad: (costo acumulado, camino actual)
    frontera = [(0, [inicio])]
    visitados = set()

    while frontera:
        costo_actual, camino = heapq.heappop(frontera)
        nodo = camino[-1]

        if nodo == objetivo:
            return camino, costo_actual

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, costo in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                nuevo_costo = costo_actual + costo
                heapq.heappush(frontera, (nuevo_costo, nuevo_camino))

    return None, float('inf')  # No se encontró camino

# Ejemplo de grafo: barrios conectados con tiempos de entrega (en minutos)
grafo_barrios = {
    'Centro': [('Hospital', 10), ('Escuela', 5)],
    'Hospital': [('Parque', 3)],
    'Escuela': [('Biblioteca', 7)],
    'Parque': [('Oficina Postal', 4)],
    'Biblioteca': [('Oficina Postal', 2)],
    'Oficina Postal': []
}

camino, costo = costo_uniforme(grafo_barrios, 'Centro', 'Oficina Postal')
print("Camino más barato:", camino)
print("Costo total:", costo, "minutos")

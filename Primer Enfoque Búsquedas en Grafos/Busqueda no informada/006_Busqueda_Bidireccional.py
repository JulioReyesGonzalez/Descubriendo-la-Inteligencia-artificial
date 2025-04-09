"""
-------------------------------------------------------
🔃 BÚSQUEDA NO INFORMADA - BÚSQUEDA BIDIRECCIONAL
-------------------------------------------------------

📌 ¿Qué es la Búsqueda Bidireccional?
Es una técnica que realiza **dos búsquedas simultáneas**:
- Una desde el **nodo inicial**.
- Otra desde el **nodo objetivo**.

Cuando ambas búsquedas se encuentran, se puede reconstruir el camino completo.

📌 ¿Por qué es eficiente?
- Reduce drásticamente la cantidad de nodos explorados.
- Si la profundidad del objetivo es d, explora aproximadamente O(b^(d/2)) nodos,
  comparado con O(b^d) de una búsqueda unidireccional.

📌 Ventajas:
- Mucho más rápido en grafos grandes si se puede aplicar.
- Útil en navegación, redes, y juegos.

📌 Requisitos:
- Conocer el estado objetivo de antemano.
- El grafo debe ser reversible (puedes ir del objetivo al inicio).

📌 Ejemplo personalizado:
Una red de estaciones de metro. Queremos ir desde "Estación Norte" a "Estación Sur"
buscando desde ambos extremos simultáneamente.

-------------------------------------------------------
"""
from collections import deque

def bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]

    # Colas para ambas búsquedas
    cola_inicio = deque([[inicio]])
    cola_objetivo = deque([[objetivo]])

    # Visitados por cada dirección
    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}

    while cola_inicio and cola_objetivo:
        # Expandir desde el inicio
        camino_inicio = cola_inicio.popleft()
        nodo_inicio = camino_inicio[-1]

        for vecino in grafo.get(nodo_inicio, []):
            if vecino not in visitados_inicio:
                nuevo_camino = list(camino_inicio) + [vecino]
                visitados_inicio[vecino] = nuevo_camino
                cola_inicio.append(nuevo_camino)

                if vecino in visitados_objetivo:
                    return nuevo_camino[:-1] + visitados_objetivo[vecino][::-1]

        # Expandir desde el objetivo
        camino_obj = cola_objetivo.popleft()
        nodo_obj = camino_obj[-1]

        for vecino in grafo.get(nodo_obj, []):
            if vecino not in visitados_objetivo:
                nuevo_camino = list(camino_obj) + [vecino]
                visitados_objetivo[vecino] = nuevo_camino
                cola_objetivo.append(nuevo_camino)

                if vecino in visitados_inicio:
                    return visitados_inicio[vecino][:-1] + nuevo_camino[::-1]

    return None  # No se encontró conexión

# Grafo de red de metro (bidireccional)
red_metro = {
    'Estación Norte': ['Central A'],
    'Central A': ['Estación Norte', 'Intercambiador', 'Museo'],
    'Museo': ['Central A', 'Teatro'],
    'Teatro': ['Museo', 'Central B'],
    'Intercambiador': ['Central A', 'Central B'],
    'Central B': ['Intercambiador', 'Teatro', 'Estación Sur'],
    'Estación Sur': ['Central B']
}

ruta = bidireccional(red_metro, 'Estación Norte', 'Estación Sur')
print("Ruta encontrada (bidireccional):", ruta)



"""
-------------------------------------------------------
⚡ BÚSQUEDA INFORMADA - BÚSQUEDA VORAZ PRIMERO EL MEJOR
-------------------------------------------------------

📌 ¿Qué es la búsqueda voraz (Greedy Best-First Search)?
Es un algoritmo de búsqueda informada que **siempre elige el nodo con menor heurística h(n)**.
- Ignora el costo real desde el inicio (g(n)).
- Solo se guía por la estimación del nodo actual al objetivo (h(n)).

📌 Fórmula de selección: f(n) = h(n)

📌 Ventajas:
- Muy rápida si la heurística está bien diseñada.
- Consume menos memoria que A*.

📌 Desventajas:
- No es óptima.
- Puede quedar atrapada en caminos malos si la heurística es engañosa.

📌 Ejemplo personalizado:
Un dron de rescate busca la ruta más prometedora desde una base hacia una zona
de emergencia usando únicamente la distancia en línea recta como guía heurística.

-------------------------------------------------------
"""
import heapq

def heuristica(ciudad_actual, ciudad_destino, coordenadas):
    x1, y1 = coordenadas[ciudad_actual]
    x2, y2 = coordenadas[ciudad_destino]
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def busqueda_voraz(grafo, coordenadas, inicio, objetivo):
    frontera = []
    heapq.heappush(frontera, (heuristica(inicio, objetivo, coordenadas), [inicio]))
    visitados = set()

    while frontera:
        _, camino = heapq.heappop(frontera)
        nodo = camino[-1]

        if nodo == objetivo:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    prioridad = heuristica(vecino, objetivo, coordenadas)
                    heapq.heappush(frontera, (prioridad, nuevo_camino))
    return None

# Mapa ficticio para misión de rescate
mapa = {
    'Base': ['Puesto1', 'Puesto2'],
    'Puesto1': ['ÁreaA'],
    'Puesto2': ['ÁreaB'],
    'ÁreaA': ['ZonaX'],
    'ÁreaB': ['ZonaX'],
    'ZonaX': []
}

# Coordenadas ficticias
coords = {
    'Base': (0, 0),
    'Puesto1': (1, 2),
    'Puesto2': (2, 1),
    'ÁreaA': (3, 4),
    'ÁreaB': (4, 2),
    'ZonaX': (5, 5)
}

# Ejecutar búsqueda voraz
ruta = busqueda_voraz(mapa, coords, 'Base', 'ZonaX')
print("Ruta encontrada (voraz):", ruta)

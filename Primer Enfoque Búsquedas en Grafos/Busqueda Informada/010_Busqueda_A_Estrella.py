"""
-------------------------------------------------------
🧠 BÚSQUEDA INFORMADA - A* (A ESTRELLA)
-------------------------------------------------------

📌 ¿Qué es el algoritmo A*?
A* es uno de los algoritmos más importantes de búsqueda informada.
Usa tanto el costo real desde el inicio (g(n)) como una heurística (h(n)):

    f(n) = g(n) + h(n)

📌 Características:
- Es completo y óptimo (si la heurística es admisible).
- Muy usado en videojuegos, navegación, mapas, etc.

📌 Ejemplo personalizado:
Un vehículo autónomo busca la ruta más corta desde su ubicación
hasta una estación de carga usando un mapa de tráfico urbano.

-------------------------------------------------------
"""
import heapq

def heuristica(a, b, coordenadas):
    x1, y1 = coordenadas[a]
    x2, y2 = coordenadas[b]
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def a_estrella(grafo, coordenadas, inicio, objetivo):
    frontera = [(0 + heuristica(inicio, objetivo, coordenadas), 0, [inicio])]
    visitados = set()

    while frontera:
        f_actual, g_actual, camino = heapq.heappop(frontera)
        nodo = camino[-1]

        if nodo == objetivo:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, costo in grafo.get(nodo, []):
                nuevo_g = g_actual + costo
                nuevo_f = nuevo_g + heuristica(vecino, objetivo, coordenadas)
                nuevo_camino = list(camino) + [vecino]
                heapq.heappush(frontera, (nuevo_f, nuevo_g, nuevo_camino))

    return None

# Mapa urbano con costos de tráfico
mapa = {
    'Inicio': [('Avenida1', 2), ('Calle2', 5)],
    'Avenida1': [('Parque', 2)],
    'Calle2': [('Tienda', 2)],
    'Parque': [('EstacionCarga', 3)],
    'Tienda': [('EstacionCarga', 4)],
    'EstacionCarga': []
}

coordenadas = {
    'Inicio': (0, 0),
    'Avenida1': (1, 2),
    'Calle2': (2, 1),
    'Parque': (3, 3),
    'Tienda': (4, 1),
    'EstacionCarga': (5, 5)
}

ruta = a_estrella(mapa, coordenadas, 'Inicio', 'EstacionCarga')
print("Ruta A* encontrada:", ruta)


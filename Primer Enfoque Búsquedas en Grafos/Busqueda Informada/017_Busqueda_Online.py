"""
-------------------------------------------------------
🌍 BÚSQUEDA INFORMADA - BÚSQUEDA ONLINE
-------------------------------------------------------

📌 ¿Qué es la búsqueda online?
Es un tipo de búsqueda donde el agente **no conoce todo el entorno**
al inicio. Va descubriendo el grafo o mapa mientras se mueve.

📌 ¿Cuándo se usa?
- En entornos dinámicos o desconocidos.
- Cuando el mapa completo no está disponible de antemano.
- En navegación robótica, exploración de laberintos, IA en juegos, etc.

📌 Diferencia clave:
- La búsqueda tradicional (offline) planea antes de actuar.
- La búsqueda online **actúa mientras explora**.

📌 Ejemplo personalizado:
Un robot en un almacén debe encontrar la salida sin conocer el mapa completo.
Solo ve las celdas vecinas a su posición actual. Descubre el camino mientras se mueve.

-------------------------------------------------------
"""
def mover_robot(laberinto, inicio, objetivo):
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izq, der
    visitados = set()
    frontera = [(inicio, [inicio])]
    filas, cols = len(laberinto), len(laberinto[0])

    while frontera:
        (x, y), camino = frontera.pop(0)
        if (x, y) == objetivo:
            return camino

        visitados.add((x, y))

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < cols:
                if laberinto[nx][ny] != '#' and (nx, ny) not in visitados:
                    frontera.append(((nx, ny), camino + [(nx, ny)]))

    return None  # No se encontró camino

# Mapa del almacén
# S = inicio, G = objetivo, # = pared
laberinto = [
    ['S', '.', '.', '#', '.', '.'],
    ['#', '#', '.', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.'],
    ['#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', 'G']
]

# Coordenadas de inicio y objetivo
inicio = (0, 0)
objetivo = (4, 5)

camino = mover_robot(laberinto, inicio, objetivo)
print("Camino descubierto por el robot:", camino)


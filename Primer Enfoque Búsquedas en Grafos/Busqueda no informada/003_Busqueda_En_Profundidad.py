"""
-------------------------------------------------------
🌌 BÚSQUEDA NO INFORMADA - BÚSQUEDA EN PROFUNDIDAD (DFS)
-------------------------------------------------------

📌 ¿Qué es la Búsqueda en Profundidad?
DFS (Depth-First Search) es un algoritmo que explora un grafo o árbol adentrándose
en las ramas hasta el fondo antes de retroceder (backtracking).

📌 ¿Cómo funciona?
- Usa una pila (stack), o recursión implícita, para ir lo más profundo posible.
- Cuando no puede ir más allá, retrocede y sigue por otra rama.
- Muy útil para verificar si hay camino entre dos nodos, recorrer árboles, etc.

📌 Ventajas:
- Consume poca memoria comparado con BFS (solo necesita almacenar un camino a la vez).
- Puede ser más rápido si la solución está "profundamente escondida".

📌 Desventajas:
- No es óptimo: puede encontrar caminos más largos primero.
- Puede quedar atrapado en bucles si el grafo tiene ciclos y no se controlan.

📌 Ejemplo personalizado:
Supongamos que tenemos un castillo con habitaciones conectadas entre sí.
Queremos encontrar una ruta desde la Entrada hasta la Torre Oculta.

-------------------------------------------------------
"""
def dfs(grafo, inicio, objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = [inicio]

    if inicio == objetivo:
        return camino

    visitados.add(inicio)

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            resultado = dfs(grafo, vecino, objetivo, visitados, camino + [vecino])
            if resultado:
                return resultado

    return None  # No se encontró camino

# Grafo de un castillo con habitaciones conectadas
castillo = {
    'Entrada': ['Sala del Trono', 'Mazmorras'],
    'Sala del Trono': ['Biblioteca', 'Jardín Interior'],
    'Mazmorras': ['Almacén'],
    'Biblioteca': ['Torre Oculta'],
    'Jardín Interior': [],
    'Almacén': [],
    'Torre Oculta': []
}

ruta = dfs(castillo, 'Entrada', 'Torre Oculta')
print("Ruta hacia la Torre Oculta:", ruta)


"""
-------------------------------------------------------
🔁 BÚSQUEDA NO INFORMADA - BÚSQUEDA EN PROFUNDIDAD ITERATIVA (IDDFS)
-------------------------------------------------------

📌 ¿Qué es la Búsqueda en Profundidad Iterativa?
Combina lo mejor de la búsqueda en anchura (BFS) y la búsqueda en profundidad (DFS):
- Hace varias búsquedas en profundidad, pero con un límite de profundidad que va aumentando.

📌 ¿Cómo funciona?
- Ejecuta DFS con límite 0, luego 1, luego 2... hasta encontrar la solución.
- Cada vez explora un poco más profundo, pero reiniciando desde el nodo inicial.

📌 ¿Por qué usarlo?
- Usa menos memoria como DFS.
- Encuentra el camino más corto como BFS.
- Ideal cuando **no sabes cuán profundo está el objetivo**.

📌 Ejemplo personalizado:
Simulamos un sistema de túneles en una montaña. Un robot explorador debe encontrar
la salida más cercana sin saber qué tan profunda está.

-------------------------------------------------------
"""
def dfs_limitado(grafo, nodo_actual, objetivo, limite, camino=None):
    if camino is None:
        camino = [nodo_actual]

    if nodo_actual == objetivo:
        return camino

    if limite <= 0:
        return None

    for vecino in grafo.get(nodo_actual, []):
        if vecino not in camino:
            resultado = dfs_limitado(grafo, vecino, objetivo, limite - 1, camino + [vecino])
            if resultado:
                return resultado

    return None

def iddfs(grafo, inicio, objetivo, profundidad_max=10):
    for limite in range(profundidad_max + 1):
        resultado = dfs_limitado(grafo, inicio, objetivo, limite)
        if resultado:
            return resultado
    return None

# Grafo de túneles en una montaña
tuneles = {
    'Entrada': ['Zona A', 'Zona B'],
    'Zona A': ['Galería 1'],
    'Zona B': ['Galería 2'],
    'Galería 1': ['Pozo Abandonado'],
    'Galería 2': ['Sala de Cristales'],
    'Pozo Abandonado': ['Salida'],
    'Sala de Cristales': [],
    'Salida': []
}

camino = iddfs(tuneles, 'Entrada', 'Salida', profundidad_max=5)
print("Ruta encontrada (IDDFS):", camino)


"""
-------------------------------------------------------
🔍 BÚSQUEDA NO INFORMADA - BÚSQUEDA EN ANCHURA (BFS)
-------------------------------------------------------

📌 ¿Qué es la Búsqueda No Informada?
La búsqueda no informada se refiere a algoritmos que exploran el espacio de estados
sin conocimiento adicional sobre qué tan lejos o cerca están del objetivo.
No usan heurísticas, sólo siguen reglas generales de exploración.

📌 ¿Qué es la Búsqueda en Anchura (BFS)?
Es un algoritmo que explora un grafo por niveles, primero los vecinos del nodo inicial,
luego los vecinos de esos vecinos, y así sucesivamente. Garantiza encontrar la
solución más corta si todas las acciones tienen el mismo costo.

📌 Ventajas:
- Es completo: siempre encuentra una solución si existe.
- Es óptimo si los pasos tienen el mismo costo.
📌 Desventajas:
- Puede consumir mucha memoria.

📌 Ejemplo de grafo:
    'Casa'
     /  \
'Biblioteca' 'Parque'
     |         |
'Escuela'   'Museo'
                 |
              'Cafetería'

Para buscar el camino más corto desde 'Casa' hasta 'Cafetería'.

-------------------------------------------------------
"""

from collections import deque  # Importamos deque para usar una cola eficiente

def bfs(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para evitar visitar nodos repetidos
    cola = deque([[inicio]])  # Cola de caminos, iniciamos con el nodo inicial
    
    while cola:
        camino = cola.popleft()  # Tomamos el primer camino en la cola
        nodo = camino[-1]  # Último nodo del camino actual
        
        if nodo == objetivo:
            return camino  # Si encontramos el objetivo, retornamos el camino
        
        if nodo not in visitados:
            for vecino in grafo.get(nodo, []):  # Revisamos vecinos del nodo actual
                nuevo_camino = list(camino)  # Clonamos el camino actual
                nuevo_camino.append(vecino)  # Agregamos el vecino al nuevo camino
                cola.append(nuevo_camino)  # Encolamos el nuevo camino
            visitados.add(nodo)  # Marcamos el nodo como visitado

# Grafo representando lugares conectados de una ciudad ficticia
grafo_ciudad = {
    'Casa': ['Biblioteca', 'Parque'],
    'Biblioteca': ['Escuela'],
    'Parque': ['Museo'],
    'Escuela': [],
    'Museo': ['Cafetería'],
    'Cafetería': []
}

# Buscamos el camino desde 'Casa' hasta 'Cafetería'
print(bfs(grafo_ciudad, 'Casa', 'Cafetería'))  # Ejemplo: ['Casa', 'Parque', 'Museo', 'Cafetería']

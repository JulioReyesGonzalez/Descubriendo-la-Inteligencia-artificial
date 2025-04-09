"""
-------------------------------------------------------
🌐 INTRODUCCIÓN A LA BÚSQUEDA EN GRAFOS
-------------------------------------------------------

📌 ¿Qué es la Búsqueda en Grafos?
Es una técnica fundamental en Inteligencia Artificial para encontrar caminos
óptimos o válidos entre nodos (estados) en un grafo. Muy útil en:
- Planificación de rutas
- Juegos
- Resolución de problemas
- Agentes inteligentes

📌 ¿Qué es un Grafo?
Un grafo es una estructura de datos compuesta por:
- Nodos (o vértices)
- Aristas (o conexiones entre nodos)

Puede ser:
- **No dirigido**: las conexiones van en ambos sentidos.
- **Dirigido**: las conexiones tienen dirección (como una carretera de un solo sentido).
- **Ponderado**: las aristas tienen un costo o peso.

📌 Tipos de búsqueda sobre grafos:
- ❌ Sin heurística (no informada): BFS, DFS, UCS, etc.
- ✅ Con heurística (informada): A*, Greedy, etc.

📌 Ejemplo básico:
Modelaremos un mapa de un campus universitario donde los nodos son edificios
y las conexiones representan los caminos entre ellos.

-------------------------------------------------------
"""
from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    resultado = []

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            resultado.append(nodo)
            cola.extend(grafo.get(nodo, []))
    return resultado

# Grafo de un campus universitario
campus = {
    'Biblioteca': ['Cafetería', 'Laboratorio'],
    'Cafetería': ['Auditorio'],
    'Laboratorio': ['Aulas'],
    'Auditorio': ['Cancha'],
    'Aulas': ['Cancha'],
    'Cancha': []
}

print("Recorrido BFS del campus:", bfs(campus, 'Biblioteca'))


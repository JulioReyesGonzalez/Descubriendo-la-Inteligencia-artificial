"""
-------------------------------------------------------
⛓️ BÚSQUEDA NO INFORMADA - BÚSQUEDA EN PROFUNDIDAD LIMITADA (DLS)
-------------------------------------------------------

📌 ¿Qué es la Búsqueda en Profundidad Limitada?
Es una variante de la Búsqueda en Profundidad (DFS) que limita la profundidad
máxima que se puede explorar. Ayuda a evitar caer en ciclos o caminos infinitos.

📌 ¿Cuándo se usa?
- Cuando el espacio de búsqueda es muy profundo o infinito.
- Cuando no queremos que el algoritmo explore más allá de un cierto nivel.

📌 Parámetro clave:
- `límite`: indica la profundidad máxima permitida desde el nodo raíz.

📌 Ventajas:
- Menor riesgo de quedarse atrapado en ciclos que DFS.
- Puede ser base para iterativa profunda.

📌 Desventajas:
- Si el objetivo está más allá del límite, no se encontrará.
- Aún no es óptimo.

📌 Ejemplo personalizado:
Un robot explora habitaciones en un edificio de investigación,
pero solo puede avanzar hasta 3 habitaciones máximo por seguridad.

-------------------------------------------------------
"""

def dls(grafo, nodo_actual, objetivo, limite, camino=None):
    if camino is None:
        camino = [nodo_actual]

    if nodo_actual == objetivo:
        return camino

    if limite <= 0:
        return None  # Límite alcanzado

    for vecino in grafo.get(nodo_actual, []):
        if vecino not in camino:
            resultado = dls(grafo, vecino, objetivo, limite - 1, camino + [vecino])
            if resultado:
                return resultado

    return None  # No se encontró en este nivel

# Grafo de habitaciones en un laboratorio
laboratorio = {
    'Acceso Principal': ['Almacén de Equipos', 'Sala de Control'],
    'Almacén de Equipos': ['Pasillo B1'],
    'Sala de Control': ['Pasillo B2'],
    'Pasillo B1': ['Laboratorio Químico'],
    'Pasillo B2': ['Sala de Servidores'],
    'Laboratorio Químico': ['Reactor Central'],
    'Sala de Servidores': [],
    'Reactor Central': []
}

# Buscar desde Acceso Principal hasta Reactor Central con límite de profundidad 3
camino = dls(laboratorio, 'Acceso Principal', 'Reactor Central', limite=3)
print("Camino encontrado con límite 3:", camino)





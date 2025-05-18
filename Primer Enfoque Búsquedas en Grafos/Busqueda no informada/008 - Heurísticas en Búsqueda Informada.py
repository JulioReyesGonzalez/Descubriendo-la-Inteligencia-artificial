"""
-------------------------------------------------------
🎯 BÚSQUEDA INFORMADA - HEURÍSTICAS
-------------------------------------------------------

📌 ¿Qué es una heurística?
Una heurística es una función que estima cuán cerca está un estado del objetivo.
No garantiza ser exacta, pero **ayuda a guiar la búsqueda más inteligentemente**.

📌 ¿Por qué es importante?
- Permite tomar decisiones más rápidas y con menos exploración.
- Se usa en algoritmos como A*, Greedy, AO*, etc.

📌 Características deseables:
- Debe ser rápida de calcular.
- Debe ser "admisible" (nunca sobreestima el costo real).
- Si es consistente, aún mejor para A*.

📌 Ejemplo personalizado:
Un repartidor de paquetes en una ciudad quiere llegar a un destino.
La heurística será la distancia en línea recta (estimada) hasta el punto final.

Este archivo define una función heurística simple que se puede integrar en otros algoritmos.
-------------------------------------------------------
"""
def heuristica_linea_recta(ciudad_actual, ciudad_destino, coordenadas):
    """
    Estima la distancia entre dos ciudades en línea recta.
    Recibe las coordenadas de cada ciudad como (x, y).
    """
    x1, y1 = coordenadas[ciudad_actual]
    x2, y2 = coordenadas[ciudad_destino]
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Coordenadas ficticias (x, y) de ciudades
mapa_ciudades = {
    'Alfa': (0, 0),
    'Bravo': (2, 3),
    'Charlie': (4, 1),
    'Delta': (6, 4),
    'Eco': (8, 0)
}

# Calcular heurística entre cada ciudad y la meta 'Eco'
for ciudad in mapa_ciudades:
    h = heuristica_linea_recta(ciudad, 'Eco', mapa_ciudades)
    print(f"Heurística de {ciudad} a Eco: {h:.2f}")

"""
-------------------------------------------------------
🚫 BÚSQUEDA INFORMADA - BÚSQUEDA TABÚ (TABU SEARCH)
-------------------------------------------------------

📌 ¿Qué es la búsqueda tabú?
Es una técnica de optimización que permite moverse hacia soluciones peores
temporalmente para **escapar de óptimos locales**, mientras evita volver
a visitar soluciones recientes usando una lista tabú.

📌 ¿Cómo funciona?
- Comienza con una solución inicial.
- En cada paso, se mueve al mejor vecino que no esté en la lista tabú.
- La lista tabú guarda movimientos recientes para evitar ciclos.

📌 ¿Dónde se usa?
- Programación de horarios.
- Optimización de rutas (TSP).
- Planificación compleja.

📌 Ejemplo personalizado:
Una empresa quiere minimizar el costo de entregas a cinco puntos fijos.
Se busca el mejor orden de entrega sin repetir combinaciones ya exploradas recientemente.

-------------------------------------------------------
"""
import random

def costo_ruta(ruta, distancias):
    return sum(distancias.get((ruta[i], ruta[i+1]), 10) for i in range(len(ruta) - 1))

def vecinos(ruta):
    # Genera rutas vecinas intercambiando dos posiciones
    rutas = []
    for i in range(len(ruta)):
        for j in range(i + 1, len(ruta)):
            nueva = list(ruta)
            nueva[i], nueva[j] = nueva[j], nueva[i]
            rutas.append(nueva)
    return rutas

def tabu_search(ciudades, distancias, iteraciones=100, tabu_tam=5):
    actual = random.sample(ciudades, len(ciudades))
    mejor = list(actual)
    mejor_costo = costo_ruta(mejor, distancias)
    tabu = []

    for _ in range(iteraciones):
        candidatos = vecinos(actual)
        candidatos = [r for r in candidatos if r not in tabu]
        if not candidatos:
            break

        candidato = min(candidatos, key=lambda r: costo_ruta(r, distancias))
        costo = costo_ruta(candidato, distancias)

        if costo < mejor_costo:
            mejor = list(candidato)
            mejor_costo = costo

        tabu.append(candidato)
        if len(tabu) > tabu_tam:
            tabu.pop(0)
        actual = candidato

    return mejor, mejor_costo

# Definición de ciudades y distancias simuladas
ciudades = ['A', 'B', 'C', 'D', 'E']
distancias = {
    ('A', 'B'): 4, ('B', 'C'): 2, ('C', 'D'): 7, ('D', 'E'): 3, ('E', 'A'): 6,
    ('A', 'C'): 5, ('B', 'D'): 6, ('C', 'E'): 4, ('D', 'A'): 8, ('E', 'B'): 7
}

mejor_ruta, costo_total = tabu_search(ciudades, distancias)
print("Mejor ruta encontrada (tabú):", mejor_ruta)
print("Costo total


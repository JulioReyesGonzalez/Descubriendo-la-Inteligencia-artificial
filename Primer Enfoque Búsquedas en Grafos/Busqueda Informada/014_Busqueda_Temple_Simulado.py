"""
-------------------------------------------------------
❄️ BÚSQUEDA INFORMADA - TEMPLE SIMULADO (SIMULATED ANNEALING)
-------------------------------------------------------

📌 ¿Qué es el temple simulado?
Es un algoritmo inspirado en el proceso físico de enfriamiento de metales.
Permite aceptar soluciones peores con cierta probabilidad al inicio para
evitar quedar atrapado en óptimos locales.

📌 ¿Cómo funciona?
- Se inicia con una temperatura alta que va disminuyendo.
- Se elige un vecino al azar.
- Si es mejor, se acepta.
- Si es peor, se acepta con una probabilidad p = e^(-Δcosto / temperatura).

📌 Ventajas:
- Útil en espacios de búsqueda complejos.
- Tiene posibilidad de encontrar el óptimo global.

📌 Ejemplo personalizado:
Un sistema de riego quiere encontrar la mejor secuencia de zonas a regar
para minimizar el consumo total de energía. Cada orden tiene un costo energético.

-------------------------------------------------------
"""
import math
import random

def costo_riego(orden, consumos):
    return sum(consumos.get((orden[i], orden[i+1]), 10) for i in range(len(orden) - 1))

def vecino(orden):
    a, b = random.sample(range(len(orden)), 2)
    nueva = list(orden)
    nueva[a], nueva[b] = nueva[b], nueva[a]
    return nueva

def simulated_annealing(zonas, consumos, temp_inicial=100, temp_min=1, alpha=0.95):
    actual = random.sample(zonas, len(zonas))
    costo_act = costo_riego(actual, consumos)
    mejor = list(actual)
    mejor_costo = costo_act
    temp = temp_inicial

    while temp > temp_min:
        candidato = vecino(actual)
        costo_cand = costo_riego(candidato, consumos)
        delta = costo_cand - costo_act

        if delta < 0 or random.random() < math.exp(-delta / temp):
            actual = candidato
            costo_act = costo_cand
            if costo_cand < mejor_costo:
                mejor = list(candidato)
                mejor_costo = costo_cand

        temp *= alpha  # Enfriamiento gradual

    return mejor, mejor_costo

# Zonas de riego y consumo energético entre ellas
zonas = ['Z1', 'Z2', 'Z3', 'Z4', 'Z5']
consumos = {
    ('Z1', 'Z2'): 5, ('Z2', 'Z3'): 4, ('Z3', 'Z4'): 6,
    ('Z4', 'Z5'): 3, ('Z5', 'Z1'): 7, ('Z1', 'Z3'): 6,
    ('Z2', 'Z4'): 5, ('Z3', 'Z5'): 4, ('Z4', 'Z1'): 6, ('Z5', 'Z2'): 5
}

resultado, energia = simulated_annealing(zonas, consumos)
print("Mejor orden de riego:", resultado)
print("Consumo energético total:", energia)


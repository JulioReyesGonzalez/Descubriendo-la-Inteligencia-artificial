"""
-------------------------------------------------------
🧗 BÚSQUEDA INFORMADA - ASCENSIÓN DE COLINAS (HILL CLIMBING)
-------------------------------------------------------

📌 ¿Qué es la ascensión de colinas?
Es una técnica de búsqueda local que, en cada paso, se mueve hacia el vecino
que mejora más la función objetivo (como subir una colina).

📌 Características:
- No mantiene memoria de caminos anteriores.
- Se detiene si no encuentra mejoras.
- Puede quedarse atrapado en óptimos locales.

📌 Tipos comunes:
- Simple
- Con reinicios aleatorios
- Con retroceso o enfriamiento simulado (ver: Simulated Annealing)

📌 Ejemplo personalizado:
Un agente inteligente intenta ajustar el ángulo de una antena parabólica
para maximizar la señal recibida. Cada movimiento representa un cambio
pequeño de ángulo y la "altura" es la intensidad de la señal.

-------------------------------------------------------
"""

import random

def intensidad_senal(angulo):
    # Función objetivo simulada: máxima en 42°
    return -(angulo - 42)**2 + 100  # Parabólica invertida

def ascension_colinas(inicio, max_iteraciones=100, paso=1):
    actual = inicio
    mejor_valor = intensidad_senal(actual)

    for _ in range(max_iteraciones):
        vecino_izq = actual - paso
        vecino_der = actual + paso

        valor_izq = intensidad_senal(vecino_izq)
        valor_der = intensidad_senal(vecino_der)

        if valor_izq > mejor_valor:
            actual = vecino_izq
            mejor_valor = valor_izq
        elif valor_der > mejor_valor:
            actual = vecino_der
            mejor_valor = valor_der
        else:
            break  # No hay mejora, llegó a un máximo local

    return actual, mejor_valor

# Comenzamos con un ángulo aleatorio
angulo_inicial = random.randint(0, 90)
resultado, senal = ascension_colinas(angulo_inicial)

print(f"Ángulo óptimo encontrado: {resultado}°")
print(f"Intensidad de señal: {senal:.2f}")

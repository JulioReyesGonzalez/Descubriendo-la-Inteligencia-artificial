"""
-------------------------------------------------------
🧬 BÚSQUEDA INFORMADA - ALGORITMO GENÉTICO (VERSIÓN II)
-------------------------------------------------------

📌 ¿Qué es un algoritmo genético?
Es un método de búsqueda y optimización inspirado en la evolución natural.
Simula selección, cruce, mutación y supervivencia del más apto.

📌 ¿Diferencia respecto a la versión básica?
En esta versión aplicamos el algoritmo a un problema **de asignación de tareas**
con costos diferentes por empleado. Buscamos una asignación óptima
de empleados a trabajos para minimizar el costo total.

📌 Ejemplo personalizado:
Una empresa tiene 4 tareas y 4 empleados. Cada uno tiene un costo diferente
para cada tarea. Queremos encontrar la mejor combinación posible.

-------------------------------------------------------
"""
import random

# Costos por tarea según empleado [empleado][tarea]
costos = [
    [9, 2, 7, 8],   # Empleado 0
    [6, 4, 3, 7],   # Empleado 1
    [5, 8, 1, 8],   # Empleado 2
    [7, 6, 9, 4]    # Empleado 3
]

def costo_total(asignacion):
    return sum(costos[i][asignacion[i]] for i in range(len(asignacion)))

def mutar(asignacion):
    a, b = random.sample(range(len(asignacion)), 2)
    asignacion[a], asignacion[b] = asignacion[b], asignacion[a]
    return asignacion

def crossover(padre1, padre2):
    corte = random.randint(1, len(padre1)-2)
    hijo = padre1[:corte]
    for gene in padre2:
        if gene not in hijo:
            hijo.append(gene)
    return hijo

def genetico(tamano_pob=10, generaciones=100):
    n = len(costos)
    poblacion = [random.sample(range(n), n) for _ in range(tamano_pob)]
    for _ in range(generaciones):
        poblacion = sorted(poblacion, key=costo_total)
        nueva = poblacion[:2]
        while len(nueva) < tamano_pob:
            padre1, padre2 = random.sample(poblacion[:5], 2)
            hijo = crossover(padre1, padre2)
            if random.random() < 0.3:
                hijo = mutar(hijo)
            nueva.append(hijo)
        poblacion = nueva
    mejor = min(poblacion, key=costo_total)
    return mejor, costo_total(mejor)

mejor_asignacion, costo = genetico()
print("Mejor asignación de tareas:", mejor_asignacion)
print("Costo total:", costo)


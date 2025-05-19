"""
-------------------------------------------------------
🌐 BÚSQUEDA INFORMADA - AO* (AND-OR A ESTRELLA)
-------------------------------------------------------

📌 ¿Qué es AO*?
AO* (AND-OR Star) es una extensión del algoritmo A* diseñada
para resolver **espacios de búsqueda jerárquicos** con nodos tipo:
- OR: una sola acción basta.
- AND: se deben cumplir múltiples subacciones.

📌 ¿Dónde se usa?
- Planificación jerárquica.
- Árboles de decisiones complejos.
- Problemas con acciones compuestas.

📌 ¿Cómo funciona?
- Utiliza una función f(n) = g(n) + h(n).
- Se expande el camino que tiene menor costo estimado.
- Maneja subgrafos AND (composición de soluciones).

📌 Ejemplo personalizado:
Un asistente virtual debe cumplir una tarea compuesta:
“Organizar una reunión” implica enviar correos (AND) y reservar sala (AND),
pero también puede simplemente hacer una llamada (OR).

-------------------------------------------------------
"""
class NodoAO:
    def __init__(self, nombre, es_and=False):
        self.nombre = nombre
        self.sucesores = []  # Lista de pares: ([subnodos], costo)
        self.es_and = es_and
        self.solucionado = False
        self.costo = float('inf')
        self.mejor_opcion = None

    def agregar_sucesor(self, subnodos, costo):
        self.sucesores.append((subnodos, costo))


def ao_star(nodo):
    if not nodo.sucesores:
        nodo.costo = 0
        nodo.solucionado = True
        return 0

    min_cost = float('inf')
    mejor_opcion = None

    for hijos, costo in nodo.sucesores:
        total = costo
        for h in hijos:
            total += ao_star(h)
        if total < min_cost:
            min_cost = total
            mejor_opcion = hijos

    nodo.costo = min_cost
    nodo.mejor_opcion = mejor_opcion
    nodo.solucionado = True
    return nodo.costo


# Crear nodos del ejemplo (planificación de reunión)
organizar_reunion = NodoAO('Organizar reunión', es_and=False)

# Opción 1 (OR): llamada rápida
llamar = NodoAO('Hacer llamada')

# Opción 2 (AND): enviar correos y reservar sala
enviar_correos = NodoAO('Enviar correos')
reservar_sala = NodoAO('Reservar sala')

# Definir el grafo
organizar_reunion.agregar_sucesor([llamar], costo=4)  # Opción simple
organizar_reunion.agregar_sucesor([enviar_correos, reservar_sala], costo=2)  # Opción compuesta

# Ejecutar AO*
costo_total = ao_star(organizar_reunion)

# Mostrar resultado
print("Costo mínimo para resolver:", costo_total)
print("Mejor estrategia:", [n.nombre for n in organizar_reunion.mejor_opcion])


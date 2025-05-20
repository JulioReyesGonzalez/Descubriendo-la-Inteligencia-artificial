"""
-------------------------------------------------------
📈 TEORÍA DE LA UTILIDAD - FUNCIÓN DE UTILIDAD
-------------------------------------------------------

📌 ¿Qué es la Teoría de la Utilidad?
Es un modelo matemático que representa **preferencias bajo incertidumbre**.
Permite a un agente racional tomar decisiones maximizando su utilidad esperada.

📌 ¿Qué es una función de utilidad?
Es una función que asigna un valor numérico (utilidad) a cada posible resultado.
Cuanto mayor es la utilidad, más preferible es el resultado para el agente.

📌 ¿Cómo se usa?
- Se usa en IA para tomar decisiones racionales.
- Se puede aplicar a economía, juegos, agentes inteligentes, etc.

📌 Ejemplo personalizado:
Un agente debe elegir entre 3 trabajos con distintas utilidades esperadas.
Cada trabajo tiene diferentes ingresos y riesgos, y la utilidad refleja
el equilibrio entre ganancia y estabilidad.

-------------------------------------------------------
"""
# Definimos la función de utilidad para un trabajo.
# Considera el salario y un "factor de estabilidad" como penalización.
def utilidad_trabajo(salario, riesgo):
    """
    Calcula la utilidad de un trabajo dado su salario y su nivel de riesgo.
    Se penaliza el riesgo: a mayor riesgo, menor utilidad.
    
    Args:
        salario (float): salario mensual del trabajo.
        riesgo (float): valor entre 0 y 1 donde 1 es máximo riesgo.

    Returns:
        float: utilidad percibida del trabajo.
    """
    return salario * (1 - riesgo)

# Diccionario con diferentes trabajos y sus características
trabajos = {
    'Desarrollador Freelance': {'salario': 5000, 'riesgo': 0.4},
    'Ingeniero en Planta': {'salario': 4500, 'riesgo': 0.1},
    'Startup Fundador': {'salario': 7000, 'riesgo': 0.6}
}

# Evaluamos la utilidad de cada trabajo usando la función
utilidades = {}
for trabajo, datos in trabajos.items():
    salario = datos['salario']
    riesgo = datos['riesgo']
    utilidad = utilidad_trabajo(salario, riesgo)  # calculamos utilidad ajustada
    utilidades[trabajo] = utilidad  # guardamos el resultado
    print(f"Trabajo: {trabajo} | Utilidad: {utilidad:.2f}")

# Encontrar la mejor opción
mejor_trabajo = max(utilidades, key=utilidades.get)
print(f"\n✅ El trabajo con mayor utilidad es: {mejor_trabajo}")


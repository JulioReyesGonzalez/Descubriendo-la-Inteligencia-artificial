"""
-------------------------------------------------------
⏪ SALTO ATRÁS DIRIGIDO POR CONFLICTOS (CONFLICT-DIRECTED BACKJUMPING)
-------------------------------------------------------

📌 ¿Qué es el salto atrás dirigido por conflictos?
Es una optimización del backtracking que, cuando detecta un conflicto al asignar
una variable, **retrocede directamente al origen del conflicto**, en lugar de paso a paso.

📌 ¿Cómo mejora el rendimiento?
- En lugar de hacer backtracking secuencial, **salta al punto relevante** que causó la falla.
- Acelera el proceso descartando múltiples niveles de decisiones erróneas de una sola vez.

📌 ¿Cuándo se usa?
- En CSPs grandes y complejos.
- Cuando la mayoría de restricciones están entre pocas variables (problemas densos).

📌 Ejemplo personalizado:
Un sistema de inscripción trata de asignar materias a estudiantes sin
solapar horarios ni repetir materias obligatorias ya asignadas.

-------------------------------------------------------
"""
def conflict_backjumping(variables, dominios, restricciones):
    return backjump(variables, dominios, restricciones, {}, 0)

def backjump(variables, dominios, restricciones, asignacion, nivel):
    if len(asignacion) == len(variables):
        return asignacion

    var = variables[livel := nivel]
    for valor in dominios[var]:
        asignacion[var] = valor
        conflicto = conflicto_con(asignacion, restricciones, var)
        if not conflicto:
            resultado = backjump(variables, dominios, restricciones, asignacion, nivel + 1)
            if resultado:
                return resultado
        else:
            # Se detectó conflicto, se salta hacia el origen del conflicto
            if conflicto < nivel:
                return None
        asignacion.pop(var)
    return None

def conflicto_con(asignacion, restricciones, var):
    for otro in restricciones.get(var, []):
        if otro in asignacion and asignacion[otro] == asignacion[var]:
            return True  # Conflicto con variable anterior
    return False

# Variables: materias a asignar
variables = ['Matematicas', 'Historia', 'Fisica']
dominios = {
    'Matematicas': ['Lunes', 'Martes'],
    'Historia': ['Lunes', 'Martes'],
    'Fisica': ['Martes', 'Miercoles']
}
# Restricciones de horario
restricciones = {
    'Matematicas': ['Historia'],
    'Historia': ['Matematicas', 'Fisica'],
    'Fisica': ['Historia']
}

solucion = conflict_backjumping(variables, dominios, restricciones)
print("Asignación de materias:", solucion)


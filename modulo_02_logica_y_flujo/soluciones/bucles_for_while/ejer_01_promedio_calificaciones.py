"""
==============================================================================
SOLUCIÓN — MÓDULO 2 — TEMA 2 — EJERCICIO 1: PROMEDIO DE CALIFICACIONES
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Recorremos la lista de notas con un bucle for.
2. Usamos un acumulador 'total_suma += nota' para obtener el total.
3. Usamos contadores 'aprobados_count' y 'reprobados_count' incrementando +1 con if-else.
"""

print("=== ANÁLISIS DE NOTAS FINALES (BUCLE FOR) ===\n")

notas = [45, 82, 90, 35, 60, 51, 100, 48]

total_suma = 0
aprobados_count = 0
reprobados_count = 0

for nota in notas:
    total_suma += nota
    if nota >= 51:
        aprobados_count += 1
    else:
        reprobados_count += 1

promedio = total_suma / len(notas)

print(f"• Lista de notas:             {notas}")
print(f"• Total de estudiantes:       {len(notas)}")
print(f"• Promedio General del Curso: {promedio:.2f} pts.")
print(f"• Estudiantes Aprobados (>=51): {aprobados_count}")
print(f"• Estudiantes Reprobados (<51): {reprobados_count}")
print(f"• Nota Máxima Obtenida:       {max(notas)} pts.")
print(f"• Nota Mínima Obtenida:       {min(notas)} pts.")
print("==============================================")

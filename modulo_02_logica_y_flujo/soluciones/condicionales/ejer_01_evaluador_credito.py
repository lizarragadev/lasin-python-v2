"""
==============================================================================
SOLUCIÓN — MÓDULO 2 — TEMA 1 — EJERCICIO 1: EVALUADOR DE CRÉDITO BANCARIO
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Usamos condicionales if-elif-else jerárquicos combinados con el operador lógico 'and'.
2. La condición preferencial se evalúa primero (Ingreso >= 8000 and Antigüedad >= 3 and sin_deudas).
3. Si no cumple el rango preferencial, evalúa el rango estándar.
"""

print("=== EVALUADOR BANCARIO DE SOLICITUD DE CRÉDITO ===\n")

ingreso = 5500.0
antiguedad = 3
sin_deudas = True

print(f"• Ingreso Mensual:          Bs. {ingreso:,.2f}")
print(f"• Antigüedad Laboral:       {antiguedad} años")
print(f"• ¿Historial Sin Deudas?:   {sin_deudas}")
print("-" * 50)

if ingreso >= 8000.0 and antiguedad >= 3 and sin_deudas:
    print("🟢 DICTAMEN: SOLICITUD APROBADA (Crédito Preferencial Tasa 5%)")
elif ingreso >= 4000.0 and antiguedad >= 2 and sin_deudas:
    print("🟢 DICTAMEN: SOLICITUD APROBADA (Crédito Estándar Tasa 8%)")
elif not sin_deudas:
    print("🔴 DICTAMEN: RECHAZADO (Existe registro de morosidad en el historial)")
else:
    print("🔴 DICTAMEN: RECHAZADO (No cumple ingresos o antigüedad mínima requerida)")
print("==================================================")

"""
==============================================================================
SOLUCIÓN — MÓDULO 3 — TEMA 2 — EJERCICIO 2: PIPELINE DE FILTRADO DE EMPLEADOS
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Función 1: Usamos una list comprehension para filtrar salarios >= min_salario.
2. Función 2: Calculamos sum() y len() para obtener total y promedio de la nómina filtrada.
"""

print("=== PIPELINE MODULAR DE FILTRADO DE NÓMINA ===\n")

nomina = [
    {"id": 1, "nombre": "Carlos Perez", "salario": 4500.0, "cargo": "Analista"},
    {"id": 2, "nombre": "Ana Morales", "salario": 8900.0, "cargo": "Gerente"},
    {"id": 3, "nombre": "Luis Torrez", "salario": 3200.0, "cargo": "Asistente"},
    {"id": 4, "nombre": "Sofia Mendoza", "salario": 12000.0, "cargo": "Director"},
]

def filtrar_empleados_por_salario(dataset: list[dict], min_salario: float) -> list[dict]:
    """Retorna los empleados con salario >= min_salario."""
    return [emp for emp in dataset if emp["salario"] >= min_salario]

def generar_resumen_nomina(empleados_filtrados: list[dict]) -> dict:
    """Calcula suma total y promedio salarial."""
    salarios = [emp["salario"] for emp in empleados_filtrados]
    total = sum(salarios)
    cantidad = len(salarios)
    promedio = total / cantidad if cantidad > 0 else 0.0
    return {"total": total, "cantidad": cantidad, "promedio": promedio}

# Invocación del pipeline con umbral de 5000.0 Bs
MIN_SALARIO_UMBRAL = 5000.0
filtrados = filtrar_empleados_por_salario(nomina, MIN_SALARIO_UMBRAL)
resumen = generar_resumen_nomina(filtrados)

print(f"=== NÓMINA DE EMPLEADOS (SALARIOS >= {MIN_SALARIO_UMBRAL:,.2f} Bs.) ===")
print(f"• Empleados calificados ({resumen['cantidad']} encontrados):")
for emp in filtrados:
    print(f"  - {emp['nombre']} ({emp['cargo']}): Bs. {emp['salario']:,.2f}")
print("-" * 54)
print(f"• Presupuesto Total Requerido: Bs. {resumen['total']:,.2f}")
print(f"• Promedio Salarial Rango:     Bs. {resumen['promedio']:,.2f}")
print("======================================================")

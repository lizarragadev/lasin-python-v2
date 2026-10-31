"""
==============================================================================
SOLUCIÓN — MÓDULO 3 — TEMA 1 — EJERCICIO 2: DEPURADOR DE DUPLICADOS
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Usamos zip() para unir las dos listas paralelas en pares de (cliente, ciudad).
2. Usamos un conjunto o diccionario para preservar clientes únicos.
3. Usamos enumerate() para generar la numeración ordinal [1], [2]...
"""

print("=== LISTA DE CLIENTES ÚNICOS REGISTRADOS ===\n")

formulario_1 = ["Juan Perez", "Maria Gomez", "Carlos Rios", "Maria Gomez"]
formulario_2 = ["La Paz", "Santa Cruz", "Cochabamba", "Santa Cruz"]

# Emparejamos con zip() y eliminamos duplicados manteniendo el orden
vistos = set()
clientes_unicos = []

for cliente, ciudad in zip(formulario_1, formulario_2):
    if cliente not in vistos:
        vistos.add(cliente)
        clientes_unicos.append((cliente, ciudad))

# Imprimimos usando enumerate(..., start=1)
for idx, (cli, ciu) in enumerate(clientes_unicos, start=1):
    print(f"  [{idx}] {cli:<15} (Sede: {ciu})")

print("============================================")

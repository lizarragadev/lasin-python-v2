"""
==============================================================================
SOLUCIÓN — MÓDULO 3 — TEMA 1 — EJERCICIO 1: GESTOR DE INVENTARIO
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Calculamos el valor total sumando (precio * stock) de cada diccionario.
2. Usamos una list comprehension para filtrar los productos con stock < 5.
3. Imprimimos el reporte formateado.
"""

print("=== GESTOR DE INVENTARIO Y STOCK CRÍTICO ===\n")

inventario = [
    {"id": 101, "nombre": "Teclado Mecánico", "precio_bs": 350.0, "stock": 12, "categoria": "Periféricos"},
    {"id": 102, "nombre": "Mouse Inalámbrico", "precio_bs": 120.0, "stock": 3, "categoria": "Periféricos"},
    {"id": 103, "nombre": "Monitor 24 IPS", "precio_bs": 1400.0, "stock": 2, "categoria": "Pantallas"},
    {"id": 104, "nombre": "Auriculares Gamer", "precio_bs": 280.0, "stock": 15, "categoria": "Audio"},
]

# 1. Valor total en almacén
valor_total = sum(item["precio_bs"] * item["stock"] for item in inventario)

# 2. List comprehension para filtrar stock crítico (<5)
stock_critico = [item for item in inventario if item["stock"] < 5]

print(f"• Valor total del almacén: Bs. {valor_total:,.2f}")
print("• Productos con stock crítico (< 5 unidades):")

for prod in stock_critico:
    print(f"  - {prod['nombre']:<20} (Stock: {prod['stock']} u. | Precio: Bs. {prod['precio_bs']:,.2f})")
print("============================================")

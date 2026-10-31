"""
==============================================================================
SOLUCIÓN — MÓDULO 2 — TEMA 1 — EJERCICIO 2: CLASIFICADOR DE CATEGORÍA FISCAL
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Usamos la estructura match-case de Python 3.10+ para evaluar códigos de categorías fijas.
2. Cada case asigna la tasa de retención correspondiente.
3. El caso 'case _:' actúa como comodín por defecto para capturar códigos inválidos.
"""

print("=== CLASIFICACIÓN FISCAL DE PROVEEDOR (MATCH-CASE) ===\n")

codigo_categoria = "CAT-A"
monto_factura = 10000.0

tasa_retencion = 0.0
regimen_nombre = ""

match codigo_categoria:
    case "CAT-A":
        regimen_nombre = "Régimen General (13% IVA + 3% IT)"
        tasa_retencion = 0.16
    case "CAT-B":
        regimen_nombre = "Régimen Simplificado"
        tasa_retencion = 0.05
    case "CAT-C":
        regimen_nombre = "Exento de Impuestos"
        tasa_retencion = 0.0
    case _:
        regimen_nombre = "Categoría No Reconocida"
        tasa_retencion = 0.0

monto_retencion = monto_factura * tasa_retencion
monto_neto = monto_factura - monto_retencion

print(f"• Código Ingresado: {codigo_categoria}")
print(f"• Régimen Asignado: {regimen_nombre}")
print(f"• Monto Factura:    Bs. {monto_factura:,.2f}")
print(f"• Retención ({tasa_retencion*100:.0f}%):  Bs. {monto_retencion:,.2f}")
print(f"• Monto Neto Pago:  Bs. {monto_neto:,.2f}")
print("======================================================")

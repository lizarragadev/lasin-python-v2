"""
==============================================================================
MÓDULO 2 — LECCIÓN 1: OPERADORES DE COMPARACIÓN, LÓGICOS Y ESTRUCTURA IF/ELIF/ELSE
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Operadores de Comparación (Devuelven True o False):
   - == (Igual a)          - != (Diferente de / No igual)
   - >  (Mayor que)         - <  (Menor que)
   - >= (Mayor o igual a)   - <= (Menor o igual a)
   ⚠️ CUIDADO: '=' es ASIGNACIÓN (x = 5), mientras '==' es COMPARACIÓN (x == 5).

2. Operadores Lógicos:
   - and (Y lógico): Retorna True SOLO SI AMBAS condiciones son verdaderas.
   - or  (O lógico): Retorna True SI AL MENOS UNA condición es verdadera.
   - not (NO lógico / Negación): Invierte el valor booleano (not True -> False).

3. Estructura Condicional if / elif / else:
   - Permite que el programa tome caminos o decisiones según se cumplan las condiciones.
   - La sangría (4 espacios o TAB) define qué código pertenece a cada bloque condicional.
==============================================================================
"""

print("=== CONDICIONALES Y OPERADORES LÓGICOS EN PYTHON ===\n")

# Solicitamos datos de prueba para evaluar la transacción
monto_transaccion = float(input("Ingrese el monto de la transacción (Bs.): "))
es_cliente_vip = input("¿El cliente es VIP? (si/no): ").strip().lower() == "si"

# ==============================================================================
# 1. EVALUACIÓN CONDICIONAL CON IF / ELIF / ELSE
# ==============================================================================
# Python evalúa las condiciones de arriba a abajo. Tan pronto como encuentra una
# condición verdadera (True), ejecuta su bloque e ignora las demás.

print("\n--- 1. CLASIFICACIÓN DE MONTO DE TRANSACCIÓN ---")

if monto_transaccion <= 0:
    # Este bloque se ejecuta si el monto es cero o negativo
    print("❌ ERROR: El monto de la transacción debe ser mayor a cero.")

elif monto_transaccion < 100:
    # Se ejecuta si el monto está entre 0.01 y 99.99 Bs.
    print("🟢 Transacción de Nivel BAJO (Operación menor).")

elif monto_transaccion <= 1000:
    # Se ejecuta si el monto está entre 100 y 1000 Bs.
    print("🟡 Transacción de Nivel MEDIO (Operación estándar).")

else:
    # Se ejecuta si ninguna de las condiciones anteriores fue verdadera (monto > 1000 Bs.)
    print("🔴 Transacción de Nivel ALTO (Requiere supervisión o aprobación).")


# ==============================================================================
# 2. EVALUACIÓN DE DESCUENTO CON OPERADORES LÓGICOS (AND, OR, NOT)
# ==============================================================================
print("\n--- 2. VERIFICACIÓN DE REGLA DE NEGOCIO CON OPERADORES LÓGICOS ---")

# REGLA DE NEGOCIO:
# Se otorga un descuento del 10% si:
# 1) El monto es mayor a 500 Bs. Y ADEMÁS el cliente es VIP (monto > 500 and es_cliente_vip)
# 2) O BIEN si el monto supera los 2000 Bs. (independientemente de si es VIP)

tiene_descuento = (monto_transaccion > 500 and es_cliente_vip) or (monto_transaccion > 2000)

print(f"• ¿Es mayor a 500 Bs. Y es VIP?: {monto_transaccion > 500 and es_cliente_vip}")
print(f"• ¿Es mayor a 2000 Bs.?:         {monto_transaccion > 2000}")
print(f"• ¿Aplica descuento final?:      {tiene_descuento}")

if tiene_descuento:
    descuento = monto_transaccion * 0.10
    monto_final = monto_transaccion - descuento
    print(f"  -> Descuento aplicado (10%): Bs. {descuento:.2f}")
    print(f"  -> Monto final a cobrar:    Bs. {monto_final:.2f}")
else:
    print("  -> No aplica descuento para esta transacción.")

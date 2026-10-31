"""
==============================================================================
MÓDULO 2 — LECCIÓN 5: DEMO — ANÁLISIS Y FILTRADO DE TRANSACCIONES SIMULADAS
Curso: Python Nivel Básico - LASIN
==============================================================================

OBJETIVO DIDÁCTICO:
- Demostrar el análisis de un conjunto de datos (lista de transacciones) aplicando
  bucles `for` combinados con la función `enumerate()`, condicionales para clasificar
  montos altos y detección de valores atípicos/fuera de rango.

REGLAS DE NEGOCIO IMPLEMENTADAS:
1. Monto Normal: Entre 0.01 y 999.99 Bs.
2. Monto Alto: Igual o superior a 1,000 Bs. (se contabiliza en lista especial).
3. Datos Fuera de Rango (Atípicos/Inválidos): Montos <= 0 o > 10,000 Bs.
==============================================================================
"""

print("==================================================")
print("     DEMO: ANÁLISIS DE TRANSACCIONES SIMULADAS     ")
print("==================================================\n")

# Colección de prueba con transacciones normales, montos elevados y datos anómalos
transacciones = [120.0, 450.5, 12000.0, 85.0, 350.0, -50.0, 2500.0, 15000.0, 95.0, 0.0]

MONTO_ALTO_UMBRAL = 1000.0      # Límite para clasificar transacciones elevadas
MONTO_MAXIMO_ESPERADO = 10000.0 # Umbral máximo aceptado como normal

# Acumuladores y contadores
total_acumulado = 0.0
total_operaciones_validas = 0
contador_montos_altos = 0
contador_fuera_de_rango = 0

transacciones_altas = []
transacciones_invalidas = []

print(f"Dataset recibido ({len(transacciones)} registros):")
print(transacciones)
print("\nIniciando análisis registro por registro:\n")

# enumerate(secuencia, start=1) devuelve tanto el índice (1, 2, 3...) como el valor (tx)
for i, tx in enumerate(transacciones, start=1):
    
    # REGLA 1: Identificar datos fuera de rango (Negativos, Cero o excesivamente altos > 10,000 Bs)
    if tx <= 0 or tx > MONTO_MAXIMO_ESPERADO:
        contador_fuera_de_rango += 1
        transacciones_invalidas.append(tx)
        print(f"⚠️ Tx N°{i}: Bs. {tx:>9,.2f} -> FUERA DE RANGO (Atípico / Inválido)")
        
        # Si es un monto positivo alto (> 10000), igual se acumula pero se marca la alerta
        if tx > 0:
            total_acumulado += tx
            total_operaciones_validas += 1
        continue

    # REGLA 2: Procesamiento de transacciones normales
    total_acumulado += tx
    total_operaciones_validas += 1

    if tx >= MONTO_ALTO_UMBRAL:
        contador_montos_altos += 1
        transacciones_altas.append(tx)
        print(f"🔴 Tx N°{i}: Bs. {tx:>9,.2f} -> ALTO MONTO (>= {MONTO_ALTO_UMBRAL} Bs.)")
    else:
        print(f"🟢 Tx N°{i}: Bs. {tx:>9,.2f} -> Monto normal")

# Cálculo de promedio sobre operaciones válidas
promedio = total_acumulado / total_operaciones_validas if total_operaciones_validas > 0 else 0

# Despliegue del reporte consolidado
print("\n" + "=" * 55)
print("           REPORTE FINAL DE TRANSACCIONES         ")
print("=" * 55)
print(f"• Registros totales evaluados:         {len(transacciones)}")
print(f"• Operaciones válidas contabilizadas:   {total_operaciones_validas}")
print(f"• Total acumulado procesado:           Bs. {total_acumulado:,.2f}")
print(f"• Promedio por transacción válida:     Bs. {promedio:,.2f}")
print(f"• Transacciones de ALTO MONTO (>=1000): {contador_montos_altos} registros")
print(f"• Registros FUERA DE RANGO / ATÍPICOS:  {contador_fuera_de_rango} registros")
print(f"  -> Valores atípicos: {transacciones_invalidas}")
print("=" * 55)

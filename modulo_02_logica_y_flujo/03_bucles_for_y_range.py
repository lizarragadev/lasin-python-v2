"""
==============================================================================
MÓDULO 2 — LECCIÓN 3: BUCLES DETERMINADOS (for) Y LA FUNCIÓN range()
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Bucle 'for':
   - Estructura repetitiva que se ejecuta un número conocido de veces sobre una secuencia (listas, rangos, cadenas).
   - En cada iteración, la variable de control (ej. 'venta' o 'i') toma automáticamente el valor del elemento actual.

2. Función range(inicio, fin, paso):
   - Genera una secuencia de números enteros.
   - range(5): Genera 0, 1, 2, 3, 4 (el límite superior '5' es EXCLUSIVO y NO se incluye).
   - range(1, 10, 2): Inicia en 1, termina antes de 10, avanzando de 2 en 2 (1, 3, 5, 7, 9).

3. Patrones de Acumuladores y Contadores:
   - Acumulador: Variable que suma valores numéricos en cada paso (ej. total += venta).
   - Contador: Variable que incrementa de 1 en 1 para contar cuántos elementos cumplen una condición (ej. n += 1).
==============================================================================
"""

print("=== BUCLES FOR Y RANGE EN PYTHON ===\n")

# ==============================================================================
# 1. USO BÁSICO DE RANGE(FIN) Y RANGE(INICIO, FIN, PASO)
# ==============================================================================
print("--- 1. SECUENCIA SIMPLE CON RANGE(5) ---")
# Genera números del 0 al 4
for i in range(5):
    print(f"Iteración N°: {i}")

print("\n--- 2. SECUENCIA CON PASO ESPECÍFICO RANGE(10, 50, 10) ---")
# Inicia en 10, avanza de 10 en 10 hasta antes de 50 (10, 20, 30, 40)
for valor in range(10, 50, 10):
    print(f"Evaluando tramo de venta: Bs. {valor}")


# ==============================================================================
# 2. RECORRIDO DE UNA LISTA Y PATRÓN ACUMULADOR / CONTADOR
# ==============================================================================
print("\n--- 3. RECORRIDO DE DATOS DE VENTAS CON BUCLE FOR ---")

# Lista de montos simulados
ventas_diarias = [150.0, 220.5, 80.0, 450.0, 310.25, 95.0]

# Inicializamos las variables del patrón
total_ventas = 0.0          # ACUMULADOR: Sumará todos los montos
ventas_altas_count = 0      # CONTADOR: Contará cuántas ventas superan los 200 Bs.

print("Dataset de ventas a procesar:", ventas_diarias)
print("\nIterando sobre cada elemento de la lista:")

# En cada paso del bucle, la variable 'venta' toma un valor de la lista 'ventas_diarias'
for venta in ventas_diarias:
    # Acumulación: Equivale a total_ventas = total_ventas + venta
    total_ventas += venta

    # Evaluación condicional dentro del bucle
    if venta >= 200.0:
        # Contador: Equivale a ventas_altas_count = ventas_altas_count + 1
        ventas_altas_count += 1
        print(f"  • Venta relevante: Bs. {venta:.2f} (Supera el umbral de 200 Bs.)")

print("\n--- RESUMEN FINAL DEL BUCLE FOR ---")
print(f"• Total acumulado recaudado: Bs. {total_ventas:.2f}")
print(f"• Cantidad de ventas >= 200 Bs.: {ventas_altas_count} registros")

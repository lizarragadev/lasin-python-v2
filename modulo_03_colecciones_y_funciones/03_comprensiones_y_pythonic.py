"""
==============================================================================
MÓDULO 3 — LECCIÓN 3: CÓDIGO PYTHONIC (List Comprehensions, enumerate, zip)
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Código Pythonic: Escribir código siguiendo las convenciones e idiolectos limpios
   propios de Python, haciéndolo más compacto, legible y eficiente.

2. Comprensiones de Listas (List Comprehensions):
   - Construcción sintáctica limpia para filtrar o transformar una lista en UNA SOLA LÍNEA.
   - Sintaxis: [expresion for elemento in iterable if condicion]

3. enumerate(iterable, start=0):
   - Evita tener que crear variables manuales de contador (ej. i = 0; i += 1).
   - Devuelve en cada iteración una tupla con la posición del elemento y el elemento.

4. zip(lista1, lista2, ...):
   - Empareja elementos de múltiples listas en paralelo como si fueran las cremalleras de un cierre.
==============================================================================
"""

print("=== CÓDIGO PYTHONIC: TÉCNICAS ELEGANTES DE ITERACIÓN ===\n")

# ==============================================================================
# 1. LIST COMPREHENSIONS (COMPRENSIONES DE LISTAS)
# ==============================================================================
ventas_raw = [100.0, 250.0, 400.0, 85.0, 1200.0, 30.0]

print("Lista original de ventas:", ventas_raw)

# ------------------------------------------------------------------------------
# Forma Tradicional (Bucle for convencional con 4 líneas de código)
# ------------------------------------------------------------------------------
ventas_altas_trad = []
for v in ventas_raw:
    if v >= 200.0:
        ventas_altas_trad.append(v)

# ------------------------------------------------------------------------------
# Forma Pythonic (List Comprehension en 1 sola línea)
# ------------------------------------------------------------------------------
# Sintaxis: [expresion for elemento in iterable if condicion]
ventas_altas_pythonic = [v for v in ventas_raw if v >= 200.0]

print("\n--- 1. COMPRENSIONES DE LISTAS ---")
print("Ventas >= 200 (Bucle Tradicional):  ", ventas_altas_trad)
print("Ventas >= 200 (Forma Pythonic):      ", ventas_altas_pythonic)

# Ejemplo de TRANSFORMACIÓN: Convertir ventas USD a BOB aplicando tasa en 1 sola línea
TASA_CAMBIO = 11.06
ventas_bob = [round(v * TASA_CAMBIO, 2) for v in ventas_raw]
print("Ventas convertidas a BOB en 1 línea:", ventas_bob)


# ==============================================================================
# 2. ENUMERATE() — OBTENER ÍNDICE Y ELEMENTO SIMULTÁNEAMENTE
# ==============================================================================
print("\n--- 2. USO DE ENUMERATE() ---")
clientes = ["Empresa Alfa", "Comercial Beta", "Servicios Gamma"]

# enumerate() nos da la posición (1, 2, 3...) y el nombre sin manejar contadores manuales
for posicion, cliente in enumerate(clientes, start=1):
    print(f"  • Posición [{posicion}]: {cliente}")


# ==============================================================================
# 3. ZIP() — ITERACIÓN EN PARALELO SOBRE MÚLTIPLES LISTAS
# ==============================================================================
print("\n--- 3. USO DE ZIP() PARA COMBINAR SECUENCIAS EN PARALELO ---")

nombres_clientes = ["Empresa Alfa", "Comercial Beta", "Servicios Gamma"]
montos_pago = [1200.0, 8500.0, 450.0]
ciudades = ["La Paz", "Santa Cruz", "Cochabamba"]

# zip combina las 3 listas elemento por elemento en cada iteración
for cli, monto, ciu in zip(nombres_clientes, montos_pago, ciudades):
    print(f"• Cliente: {cli:<16} | Sede: {ciu:<12} | Pago: Bs. {monto:,.2f}")

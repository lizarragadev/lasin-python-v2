"""
==============================================================================
SOLUCIÓN — MÓDULO 3 — TEMA 2 — EJERCICIO 1: CONVERSOR DE DIVISAS SEGURO
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Definimos la función de conversión con tipos anotados.
2. Capturamos ValueError en el bloque try-except al convertir el texto ingresado.
3. Usamos la cláusula 'else' para mostrar el éxito y 'finally' para la limpieza.
"""

print("=== CONVERSOR DE DIVISAS CON CONTROL DE EXCEPCIONES ===\n")

def convertir_usd_a_bob(monto_usd: float, tasa: float = 11.06) -> float:
    """Convierte un monto en USD a BOB dada una tasa de cambio."""
    if monto_usd < 0:
        raise ValueError("El monto no puede ser negativo.")
    return round(monto_usd * tasa, 2)

# Prueba con captura de errores
entrada_str = input("Ingrese el monto en Dólares ($ USD): ").strip()

try:
    monto_num = float(entrada_str)
    resultado_bob = convertir_usd_a_bob(monto_num)
except ValueError as err:
    print(f"❌ Error de conversión (ValueError): Entradas inválidas ('{entrada_str}'). [{err}]")
else:
    print(f"✓ {monto_num:.2f} USD equivalen a Bs. {resultado_bob:,.2f} BOB.")
finally:
    print("  [Proceso de conversión finalizado]")
print("=======================================================")

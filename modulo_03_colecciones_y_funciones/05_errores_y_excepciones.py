"""
==============================================================================
MÓDULO 3 — LECCIÓN 5: MANEJO DE ERRORES Y EXCEPCIONES (try / except / else / finally)
Curso: Python Nivel Básico - LASIN
==============================================================================

¿POR QUÉ ES VITAL EL MANEJO DE EXCEPCIONES EN PYTHON?
- En un entorno de producción o análisis de datos, un valor inválido (ej. un texto 'N/A'
  donde se esperaba un número) provocará un error de ejecución (Excepción) que
  HARÁ CAER EL PROGRAMA POR COMPLETO si no se captura.

ESTRUCTURA COMPLETA DEL BLOQUE DE CONTROL DE EXCEPCIONES:
1. try: Bloque de código 'arriesgado' donde se intenta ejecutar la operación.
2. except ExcepcionEspecifica: Se ejecuta ÚNICAMENTE SI ocurre un error del tipo indicado.
3. else: Se ejecuta ÚNICAMENTE SI el bloque try finalizó con ÉXITO (sin ningún error).
4. finally: Se ejecuta SIEMPRE, haya ocurrido un error o no (ideal para cerrar archivos/conexiones).
==============================================================================
"""

print("=== MANEJO ROBUSTO DE ERRORES EN PYTHON ===\n")

# ==============================================================================
# 1. CAPTURA DE EXCEPCIÓN ESPECÍFICA (ZeroDivisionError)
# ==============================================================================
def calcular_promedio_seguro(suma_total: float, cantidad_elementos: int) -> float:
    """Calcula el promedio evitando la caída del programa si cantidad_elementos == 0."""
    try:
        resultado = suma_total / cantidad_elementos
        return resultado
    except ZeroDivisionError:
        # Se activa si intentamos dividir entre 0
        print("⚠️ Excepción capturada (ZeroDivisionError): No se puede dividir entre 0. Retornando 0.0")
        return 0.0


print("--- 1. MANEJO DE DIVISIÓN POR CERO (ZeroDivisionError) ---")
print("Promedio válido (1000 / 4):       ", calcular_promedio_seguro(1000.0, 4))
print("Promedio seguro con 0 elementos:  ", calcular_promedio_seguro(1000.0, 0))


# ==============================================================================
# 2. BLOQUE ESTRUCTURADO: TRY - EXCEPT - ELSE - FINALLY
# ==============================================================================
print("\n--- 2. DEMO DE BLOQUE COMPLETO DE MANEJO DE EXCEPCIONES ---")

def procesar_monto_usuario():
    entrada_usuario = input("Ingrese el monto a procesar (ej. 150.50): ").strip()
    
    try:
        # Intentamos convertir la entrada del usuario a float (puede lanzar ValueError si es texto)
        monto_decimal = float(entrada_usuario)
    except ValueError as err:
        # Se ejecuta SOLO si ocurre un ValueError (ej. si el usuario ingresó 'hola')
        print(f"❌ Error de conversión (ValueError): '{entrada_usuario}' no es un número decimal válido.")
        print(f"   Detalle técnico de la excepción: {err}")
    else:
        # Se ejecuta SOLO si el bloque try fue 100% exitoso
        print(f"✓ Éxito total: El monto de Bs. {monto_decimal:.2f} fue procesado correctamente.")
    finally:
        # Se ejecuta SIEMPRE independientemente de si hubo o no error
        print("  [Bloque Finally]: Limpieza y cierre de la operación de validación.\n")

# Ejecutamos la prueba interactiva
procesar_monto_usuario()

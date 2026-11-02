"""
==============================================================================
MÓDULO 3 — LECCIÓN 4: FUNCIONES REUTILIZABLES Y SEPARACIÓN DE RESPONSABILIDADES
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Funciones (def nombre_funcion(parametros):):
   - Bloques de código nombrados diseñados para realizar una tarea específica.
   - Evitan la repetición de código (Principio DRY: Don't Repeat Yourself).

2. Parámetros y Argumentos:
   - Parámetros: Variables declaradas en la definición de la función.
   - Argumentos: Valores reales pasados a la función al llamarla.
   - Valores por defecto: Parámetros opcionales con un valor predeterminado.

3. Retorno de Datos (return):
   - Envía el resultado procesado de vuelta a quien llamó la función y finaliza su ejecución.

4. Ámbito / Scope (Local vs Global):
   - Las variables creadas dentro de una función son LOCALES y se eliminan al terminar la función.
==============================================================================
"""

print("=== FUNCIONES Y MODULARIZACIÓN EN PYTHON ===\n")

# Variable global de configuración fiscal
IMPUESTO_IVA = 0.13  # 13% de IVA en Bolivia


# ==============================================================================
# 1. DEFINICIÓN DE FUNCIONES CON RESPONSABILIDAD ÚNICA
# ==============================================================================

def calcular_impuesto_iva(monto: float, tasa: float = IMPUESTO_IVA) -> float:
    """
    Calcula el impuesto IVA a partir de un monto y una tasa decimal.
    'tasa' tiene un valor por defecto de 0.13 (13%).
    """
    monto_impuesto = monto * tasa
    return monto_impuesto  # Retorna el valor numérico procesado


def clasificar_nivel_riesgo(monto: float) -> str:
    """Clasifica una transacción comercial en un nivel de riesgo."""
    if monto > 10000.0:
        return "ALTO RIESGO"
    elif monto > 2000.0:
        return "RIESGO MODERADO"
    else:
        return "BAJO RIESGO"


def crear_ficha_transaccion(cliente: str, monto: float, ciudad: str = "La Paz") -> dict:
    """
    Función orquestadora: Llama a otras funciones pequeñas y retorna
    un diccionario estructurado completo.
    """
    impuesto = calcular_impuesto_iva(monto)
    riesgo = clasificar_nivel_riesgo(monto)
    
    # Construimos y retornamos un diccionario
    return {
        "cliente": cliente.upper().strip(),
        "monto_bruto": monto,
        "impuesto_iva": impuesto,
        "monto_neto": monto - impuesto,
        "ciudad": ciudad.title().strip(),
        "nivel_riesgo": riesgo
    }


# ==============================================================================
# 2. INVOCACIÓN / LLAMADA A LAS FUNCIONES
# ==============================================================================
print("--- PRUEBAS DE INVOCACIÓN DE FUNCIONES ---")

# Ejemplo 1: Invocación usando el parámetro 'ciudad' por defecto ("La Paz")
ficha1 = crear_ficha_transaccion("Comercial Los Andes", 3500.0)
print("Ficha 1 (Ciudad por defecto):")
print(ficha1)

# Ejemplo 2: Invocación pasando parámetros nombrados (Keyword Arguments)
ficha2 = crear_ficha_transaccion(
    cliente="Importadora El Sol",
    monto=15000.0,
    ciudad="Santa Cruz"
)
print("\nFicha 2 (Parámetros nombrados explícitos):")
print(ficha2)

"""
==============================================================================
MÓDULO 5 — LECCIÓN 4: BUENAS PRÁCTICAS (PEP 8) E IA COMO ASISTENTE
Curso: Python Nivel Básico - LASIN
==============================================================================

NORMAS DE CALIDAD DE CÓDIGO (PEP 8):
1. Convención de nombres:
   - Variables y Funciones: snake_case (ej. calcular_monto_neto)
   - Constantes: MAYÚSCULAS_CON_GUIONES (ej. TASA_CAMBIO)
   - Clases: PascalCase / CamelCase (ej. ProcesadorDatos)

2. Responsabilidad Única: Cada función debe hacer una sola cosa y hacerlo bien.

3. Comentarios Útiles: Explicar el 'por qué' del negocio, no solo el 'qué' del código.

USO RESPONSABLE DE HERRAMIENTAS DE INTELIGENCIA ARTIFICIAL (IA):
- La IA (Gemini, ChatGPT, Antigravity) es un excelente tutor para aprender Python.
- Buenas prácticas al formular preguntas (Prompting):
  1. No pidas el código completo directamente; pide EXPLICACIONES o PISTAS.
  2. Pega el traceback exacto del error que recibes en la terminal.
  3. NUNCA copies y pegues código generado si no entiendes cómo funciona.
==============================================================================
"""

print("=== BUENAS PRÁCTICAS Y USO RESPONSABLE DE LA IA ===\n")

# ==============================================================================
# 1. EJEMPLO COMPARATIVO: CÓDIGO MAL ESCRITO VS CÓDIGO LIMPIO (PEP 8)
# ==============================================================================

print("--- 1. EJEMPLO DE CÓDIGO MAL ESCRITO (POCO LEGIBLE) ---")
# ❌ CÓDIGO MALO: Nombres sin sentido (d, f, x, t), sin espacios ni tipos
d = [100, 200, 300]
def f(x):
    t=0
    for i in x:
        t+=i
    return t/len(x)
print("Promedio (Código sin normas):", f(d))


print("\n--- 2. EJEMPLO DE CÓDIGO LIMPIO CON NORMAS PEP 8 ---")
# ✓ CÓDIGO BUENO: Nombres descriptivos, type hints, docstrings y validación defensiva
dataset_ventas_bolivia = [100.0, 200.0, 300.0]

def calcular_promedio_ventas(ventas: list[float]) -> float:
    """Calcula el promedio de una lista de ventas en Bs. retornando 0.0 si la lista está vacía."""
    if not ventas:
        return 0.0
    return sum(ventas) / len(ventas)

promedio_limpio = calcular_promedio_ventas(dataset_ventas_bolivia)
print(f"Promedio de ventas (Código limpio PEP 8): Bs. {promedio_limpio:.2f}")


# ==============================================================================
# 2. GUÍA PRÁCTICA DE PROMPTS EFECTIVOS PARA DEBUGGING CON IA
# ==============================================================================
print("\n" + "=" * 55)
print("     GUÍA: CÓMO PEDIR AYUDA A UNA IA PARA APRENDER  ")
print("=" * 55)

prompt_ejemplo_error = """
PROMPT DE EJEMPLO RECOMENDADO PARA RESOLVER ERRORES:
------------------------------------------------------------------
"Hola. Estoy en el Módulo 3 de mi curso de Python en LASIN.
Recibí el siguiente error al intentar convertir un dato de un archivo:
'ValueError: could not convert string to float: 'N/A''

Por favor:
1. Explícame de forma sencilla por qué ocurre este ValueError en Python.
2. Dame 2 pistas de cómo puedo manejarlo usando un bloque try-except.
3. No me des la solución completa directamente, prefiero escribir el código yo mismo."
------------------------------------------------------------------
"""

print(prompt_ejemplo_error)

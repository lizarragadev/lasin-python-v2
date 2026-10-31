"""
==============================================================================
MÓDULO 2 — LECCIÓN 2: CONDICIONALES ANIDADOS, OPERADOR TERNARIO Y MATCH-CASE
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Condicionales Anidados: Un bloque 'if' colocado dentro de otro bloque 'if'.
   Útil para validaciones jerárquicas (ej. primero verificar si el usuario existe,
   y luego verificar sus permisos específicos).

2. Operador Ternario (Expresión Condicional Compacta):
   - Permite evaluar una condición y retornar un valor en UNA SOLA LÍNEA de código.
   - Sintaxis: resultado = valor_si_true if condicion else valor_si_false

3. Estructura match-case (Introducida en Python 3.10+):
   - Equivale al 'switch-case' de C/Java. Es la forma más limpia de comparar una
     variable contra múltiples opciones fijas sin encadenar muchos elif.
   - El caso 'case _:' actúa como el caso por defecto (else).
==============================================================================
"""

print("=== CONDICIONALES AVANZADOS EN PYTHON ===\n")

# ==============================================================================
# 1. CONDICIONALES ANIDADOS (VALIDACIÓN DE SEGURIDAD Y PERMISOS)
# ==============================================================================
usuario = input("Ingrese nombre de usuario: ").strip().lower()
rol = input("Ingrese rol (admin / analista / operador): ").strip().lower()

print("\n--- 1. VERIFICACIÓN DE ACCESO ANIDADO ---")

# Nivel 1: Verificar si el usuario está autenticado
if usuario == "admin" or usuario == "gustavo":
    print("✓ Usuario autenticado con éxito.")
    
    # Nivel 2: Condicional anidado dentro de la autenticación para revisar el ROL
    if rol == "admin":
        print("  [Acceso Nivel 1]: Control Total (Crear, Modificar, Eliminar).")
    elif rol == "analista":
        print("  [Acceso Nivel 2]: Lectura y Generación de Reportes.")
    else:
        print("  [Acceso Nivel 3]: Lectura Limitada.")
else:
    print("❌ Acceso denegado: Nombre de usuario no autorizado.")


# ==============================================================================
# 2. OPERADOR TERNARIO (EXPRESIÓN CONDICIONAL DE UNA SOLA LÍNEA)
# ==============================================================================
# Útil cuando deseas asignar un valor simple a una variable basado en una condición rápida

print("\n--- 2. OPERADOR TERNARIO ---")
edad = int(input("Ingrese la edad del usuario: "))

# Sintaxis: variable = valor_si_verdadero if condicion else valor_si_falso
estado_habilitacion = "Habilitado (Mayor de edad)" if edad >= 18 else "Inhabilitado (Menor de edad)"

print(f"Resultado de habilitación: {estado_habilitacion}")


# ==============================================================================
# 3. ESTRUCTURA MATCH-CASE (PATRONES EN PYTHON 3.10+)
# ==============================================================================
# Evalúa el valor de 'codigo_estado' contra casos específicos limpiando el código

print("\n--- 3. ESTRUCTURA MATCH-CASE PARA RESPUESTAS HTTP ---")
codigo_estado = input("Ingrese código de estado HTTP (200, 404, 500): ").strip()

match codigo_estado:
    case "200":
        mensaje = "200 OK: Solicitud procesada correctamente."
    case "201":
        mensaje = "201 Created: Nuevo registro creado en la base de datos."
    case "400":
        mensaje = "400 Bad Request: Error en los parámetros enviados."
    case "404":
        mensaje = "404 Not Found: El recurso o dataset solicitado no existe."
    case "500":
        mensaje = "500 Internal Server Error: Falla interna en el servidor."
    case _:
        # 'case _:' equivale al 'else' final (captura cualquier valor no contemplado)
        mensaje = f"Código {codigo_estado}: Estado HTTP desconocido."

print(f"-> {mensaje}")

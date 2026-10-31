"""
==============================================================================
SOLUCIÓN — MÓDULO 2 — TEMA 2 — EJERCICIO 2: VALIDADOR DE CONTRASEÑA CON WHILE
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Usamos un bucle while que evalúa la condición 'intentos_usados < MAX_INTENTOS'.
2. Solicitamos la clave en cada iteración.
3. Si la clave coincide, imprimimos bienvenida y rompemos el bucle con 'break'.
4. Si agota los intentos, informamos el bloqueo al salir del bucle.
"""

print("=== SISTEMA DE SEGURIDAD Y AUTENTICACIÓN ===\n")

PASSWORD_CORRECTO = "lasin2026"
MAX_INTENTOS = 3

intentos_usados = 0
autenticado = False

while intentos_usados < MAX_INTENTOS:
    intentos_usados += 1
    entrada = input(f"Intento {intentos_usados}/{MAX_INTENTOS} - Ingrese contraseña: ").strip()

    if entrada == PASSWORD_CORRECTO:
        autenticado = True
        print("\n🟢 Acceso concedido al sistema. ¡Bienvenido!")
        break  # Rompe el bucle al autenticarse correctamente
    else:
        intentos_restantes = MAX_INTENTOS - intentos_usados
        if intentos_restantes > 0:
            print(f"❌ Contraseña incorrecta. Te quedan {intentos_restantes} intentos.\n")

if not autenticado:
    print(f"\n🔒 Ha agotado sus {MAX_INTENTOS} intentos. Cuenta bloqueada por seguridad.")
print("===================================")

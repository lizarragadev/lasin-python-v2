"""
==============================================================================
MÓDULO 2 — LECCIÓN 4: BUCLES INDETERMINADOS (while) Y SENTENCIAS BREAK / CONTINUE
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Bucle 'while' (Mientras):
   - Estructura repetitiva indeterminada. Se ejecuta de forma continua MIENTRAS
     su condición sea verdadera (True).
   - Ideal cuando NO sabemos de antemano cuántas veces se repetirá el bucle
     (ej. solicitar datos al usuario hasta que ingrese un valor válido).

2. Sentencia 'break' (Interrupción):
   - Rompe o termina la ejecución del bucle INMEDIATAMENTE, saliendo de él.

3. Sentencia 'continue' (Salto):
   - Omite el resto de las instrucciones de la iteración ACTUAL y salta
     directamente a evaluar la condición del bucle para el siguiente paso.

4. Patrón de Validación de Entradas:
   - Utilizar un bucle while not valido para forzar al usuario a corregir errores.
==============================================================================
"""

print("=== BUCLE WHILE Y VALIDACIÓN DE ENTRADAS ===\n")

# ==============================================================================
# 1. PATRÓN DE VALIDACIÓN DE ENTRADA CON WHILE
# ==============================================================================
# Este bucle se repetirá tantas veces como sea necesario hasta que el usuario ingrese un monto > 0

print("--- 1. VALIDACIÓN INTERACTIVA DE MONTO DE TRANSACCIÓN ---")

monto_valido = False
monto = 0.0

while not monto_valido:
    entrada = input("Ingrese un monto de transacción válido (> 0 Bs.): ").strip()
    
    # Intentamos convertir la entrada a float de manera limpia
    monto = float(entrada) if entrada.replace('.', '', 1).isdigit() else -1.0
    
    if monto > 0:
        monto_valido = True  # Al cambiar a True, la condición 'while not monto_valido' se vuelve False y sale del bucle
        print(f"✓ Monto de Bs. {monto:.2f} verificado y registrado exitosamente.")
    else:
        print("❌ Error: El monto ingresado debe ser estrictamente mayor a 0 Bs. Intente de nuevo.\n")


# ==============================================================================
# 2. PATRÓN CON CONTROL BREAK Y CONTINUE (LECTURA DE SENSORES)
# ==============================================================================
# Simulamos una secuencia de lecturas de sensores de temperatura (°C)
# - Si la temperatura es negativa (< 0), es un dato defectuoso -> Usamos 'continue' para ignorarlo.
# - Si la temperatura es excesiva (> 80°C), es una emergencia -> Usamos 'break' para detener el sistema.

print("\n--- 2. PROCESAMIENTO DE TEMPERATURAS CON BREAK Y CONTINUE ---")

lecturas_temperatura = [22.5, 24.0, -99.0, 25.5, 85.0, 26.0, 23.0]
posicion = 0

print("Secuencia de lecturas recibidas:", lecturas_temperatura)

while posicion < len(lecturas_temperatura):
    temp = lecturas_temperatura[posicion]
    posicion += 1  # Incrementamos la posición para no crear un bucle infinito

    # REGLA 1: Omitir lecturas erróneas con 'continue'
    if temp < 0:
        print(f"⚠️ Alerta: Lectura defectuosa ({temp}°C) ignorada. Continuando con la siguiente...")
        continue  # Salta inmediatamente al inicio del bucle sin ejecutar lo que sigue abajo

    # REGLA 2: Parada de emergencia por sobrecalentamiento con 'break'
    if temp > 80.0:
        print(f"🔥 ALERTA CRÍTICA: Temperatura {temp}°C supera el límite de 80°C. Sistema DETENIDO inmediatamente.")
        break  # Rompe el bucle por completo

    print(f"  • Temperatura dentro de rango normal: {temp}°C")

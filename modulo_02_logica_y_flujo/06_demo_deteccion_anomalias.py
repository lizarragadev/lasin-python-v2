"""
==============================================================================
MÓDULO 2 — LECCIÓN 6: DEMO — DETECCIÓN BÁSICA DE ANOMALÍAS POR REGLAS
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTO FUNDAMENTAL DE DETECCIÓN POR REGLAS:
  Dato de Entrada  --->  Regla de Validación  --->  ¿Cumple?  --->  [ NORMAL / ANOMALÍA ]

¿POR QUÉ USAR ESTE PATRÓN EN PYTHON?
- En sistemas de datos (finanzas, sensores, datos médicos), muchos errores no
  provienen de fallas de sintaxis en el código, sino de 'Datos Atípicos' (ej. un usuario
  que escribe 1500 años de edad por error de tipeo).
- Mediante condicionales 'if-elif', construimos un 'Motor de Reglas' sencillo para
  identificar y aislar estos registros antes de que arruinen los promedios.
==============================================================================
"""

print("==================================================")
print("   DEMO: MOTOR BÁSICO DE DETECCIÓN DE ANOMALÍAS  ")
print("==================================================\n")

print("Flujo conceptual:")
print("  Dato  --->  Regla  --->  ¿Cumple la regla?  --->  [ NORMAL / ANOMALÍA ]\n")

# Datasets simulados con distintos dominios (montos, temperaturas, edades)
registros_evaluar = [
    {"tipo": "monto", "valor": 450.0, "descripcion": "Pago de servicios"},
    {"tipo": "monto", "valor": 55000.0, "descripcion": "Transferencia sospechosa"},
    {"tipo": "temperatura", "valor": 22.5, "descripcion": "Sensor laboratorio 1"},
    {"tipo": "temperatura", "valor": 105.0, "descripcion": "Sensor caldera 2"},
    {"tipo": "edad", "valor": 28, "descripcion": "Registro cliente A"},
    {"tipo": "edad", "valor": 160, "descripcion": "Registro cliente B (Error de tipeo)"},
    {"tipo": "edad", "valor": -5, "descripcion": "Registro cliente C (Negativo)"},
]

total_normales = 0
total_anomalias = 0

print("Evaluando lista de registros:\n")

for i, reg in enumerate(registros_evaluar, start=1):
    tipo = reg["tipo"]
    valor = reg["valor"]
    desc = reg["descripcion"]

    es_anomalia = False
    motivo_anomalia = ""

    # MOTOR DE REGLAS SEGÚN EL TIPO DE DATO EVALUADO
    if tipo == "monto":
        # Regla: Monto mayor a 50.000 Bs o menor/igual a 0 se marca como atípico
        if valor > 50000.0:
            es_anomalia = True
            motivo_anomalia = f"Monto excesivamente alto ({valor:,.2f} Bs. > 50,000 Bs.)"
        elif valor <= 0:
            es_anomalia = True
            motivo_anomalia = "Monto menor o igual a cero (Inválido)"

    elif tipo == "temperatura":
        # Regla: Rango operativo seguro para sensores (-10°C a 60°C)
        if valor < -10.0 or valor > 60.0:
            es_anomalia = True
            motivo_anomalia = f"Temperatura fuera del rango de seguridad ({valor}°C)"

    elif tipo == "edad":
        # Regla: Edad biológica válida entre 0 y 120 años
        if valor < 0 or valor > 120:
            es_anomalia = True
            motivo_anomalia = f"Edad biológicamente imposible o no válida ({valor} años)"

    # RESULTADO DE LA EVALUACIÓN
    if es_anomalia:
        total_anomalias += 1
        print(f"🔴 [ANOMALÍA DETECTADA] Reg N°{i} ({desc}):")
        print(f"   -> Causa Alerta: {motivo_anomalia}")
    else:
        total_normales += 1
        print(f"🟢 [DATO NORMAL] Reg N°{i} ({desc}): Valor {valor} dentro de parámetros.")

print("\n" + "=" * 55)
print("            RESUMEN DE ANOMALÍAS DETECTADAS        ")
print("=" * 55)
print(f"• Registros evaluados en total: {len(registros_evaluar)}")
print(f"• Registros NORMALES:           {total_normales}")
print(f"• ANOMALÍAS identificadas:     {total_anomalias}")
print("=" * 55)

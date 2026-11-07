"""
==============================================================================
MÓDULO 4 — LECCIÓN 7: DEMO INTEGRADORA — DATAFLOW v2 (CSV + JSON + PERSISTENCIA)
Curso: Python Nivel Básico - LASIN
==============================================================================

OBJETIVO DIDÁCTICO DE DATAFLOW v2:
- Integrar en un solo script completo:
  1. Generación y lectura de archivos tabulares CSV (csv.DictReader).
  2. Procesamiento de registros y aplicación de reglas de detección de anomalías.
  3. Persistencia de estados y métricas acumuladas en archivos JSON (json.dump).
  4. Marcas de tiempo dinámicas para trazabilidad.
==============================================================================
"""

import csv
import json
import os
from datetime import datetime

print("==================================================")
print("       DEMO: DATAFLOW v2 - SISTEMA INTEGRADO      ")
print("==================================================\n")

# Directorio seguro de datos
CARPETA_DATOS = "datos_temporales"
os.makedirs(CARPETA_DATOS, exist_ok=True)

RUTA_CSV_ENTRADA = os.path.join(CARPETA_DATOS, "ventas_v2.csv")
RUTA_JSON_SALIDA = os.path.join(CARPETA_DATOS, "dataflow_v2_estado.json")

# ------------------------------------------------------------------------------
# 1. GENERACIÓN DEL DATASET INICIAL EN FORMATO CSV SI NO EXISTE
# ------------------------------------------------------------------------------
dataset_inicial = [
    {"id": "1", "empresa": "Comercial Bolivia", "monto": "2500.00", "ciudad": "La Paz"},
    {"id": "2", "empresa": "Servicios Paititi", "monto": "18000.00", "ciudad": "Santa Cruz"},
    {"id": "3", "empresa": "Constructora Tunari", "monto": "450.00", "ciudad": "Cochabamba"},
    {"id": "4", "empresa": "Minera Altiplano", "monto": "55000.00", "ciudad": "Oruro"},
]

with open(RUTA_CSV_ENTRADA, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "empresa", "monto", "ciudad"])
    writer.writeheader()
    writer.writerows(dataset_inicial)

print(f"1. Dataset CSV de entrada preparado en: {RUTA_CSV_ENTRADA}")


# ------------------------------------------------------------------------------
# 2. PROCESAMIENTO Y PARSEO DEL ARCHIVO CSV EN MEMORIA
# ------------------------------------------------------------------------------
print("2. Leyendo y procesando transacciones desde CSV...")
registros_procesados = []

with open(RUTA_CSV_ENTRADA, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        monto_num = float(fila["monto"])
        # Regla de negocio: Monto atípicamente alto (> 30,000 Bs) se marca como anomalía
        es_anomalia = monto_num > 30000.0
        
        registro = {
            "id": int(fila["id"]),
            "empresa": fila["empresa"],
            "monto": monto_num,
            "ciudad": fila["ciudad"],
            "anomalo": es_anomalia
        }
        registros_procesados.append(registro)


# ------------------------------------------------------------------------------
# 3. PERSISTENCIA DE ESTADOS EN ARCHIVO JSON (SNAPSHOT)
# ------------------------------------------------------------------------------
total_acumulado = sum(r["monto"] for r in registros_procesados)
anomalias_count = sum(1 for r in registros_procesados if r["anomalo"])

dataflow_v2_snapshot = {
    "sistema": "DataFlow v2 Core",
    "timestamp_generacion": datetime.now().isoformat(),
    "total_registros_procesados": len(registros_procesados),
    "monto_total_consolidado_bs": total_acumulado,
    "total_anomalias_detectadas": anomalias_count,
    "registros_detalle": registros_procesados
}

# Escribimos el estado consolidado en el archivo JSON
with open(RUTA_JSON_SALIDA, "w", encoding="utf-8") as f:
    json.dump(dataflow_v2_snapshot, f, indent=4, ensure_ascii=False)

print(f"3. Estado final guardado exitosamente en JSON: {RUTA_JSON_SALIDA}\n")

# ------------------------------------------------------------------------------
# 4. RESUMEN DE EJECUCIÓN POR CONSOLA
# ------------------------------------------------------------------------------
print("=" * 55)
print("            DATAFLOW v2 - RESUMEN EJECUTIVO        ")
print("=" * 55)
print(f"• Registros procesados:     {dataflow_v2_snapshot['total_registros_procesados']}")
print(f"• Monto Total Consolidado:  Bs. {dataflow_v2_snapshot['monto_total_consolidado_bs']:,.2f}")
print(f"• Anomalías detectadas:     {dataflow_v2_snapshot['total_anomalias_detectadas']}")
print("=" * 55)

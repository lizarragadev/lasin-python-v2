"""
==============================================================================
SOLUCIÓN — MÓDULO 4 — TEMA 1 — EJERCICIO 2: FILTRADOR DE ANOMALÍAS CSV A JSON
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Leemos el CSV generado con csv.DictReader.
2. Convertimos el campo monto_bob a float.
3. Filtramos los registros con monto > 10,000.0 Bs.
4. Exportamos el informe en JSON.
"""

import csv
import json
import os

print("=== LECTOR Y PROCESADOR DE CSV A JSON ===\n")

CARPETA = "datos_temporales"
RUTA_CSV = os.path.join(CARPETA, "ventas_exportadas.csv")
RUTA_JSON_INFORME = os.path.join(CARPETA, "informe_anomalias.json")

# Verificar si el CSV existe, sino crearlo temporalmente
if not os.path.exists(RUTA_CSV):
    os.makedirs(CARPETA, exist_ok=True)
    with open(RUTA_CSV, "w", newline="", encoding="utf-8") as f:
        f.write("id,empresa,monto_bob,ciudad\n101,TechBolivia,4500.50,La Paz\n102,Comercial Paititi,28500.00,Santa Cruz\n")

# 1. Leer CSV
registros_leidos = []
with open(RUTA_CSV, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        fila["monto_bob"] = float(fila["monto_bob"])
        registros_leidos.append(fila)

# 2. Filtrar anomalías (> 10000.0 Bs)
anomalias = [r for r in registros_leidos if r["monto_bob"] > 10000.0]

print(f"• Registros leídos desde CSV: {len(registros_leidos)}")
print(f"• Anomalías detectadas (> 10.000 Bs): {len(anomalias)}")
for a in anomalias:
    print(f"  - ID {a['id']} ({a['empresa']}): Bs. {a['monto_bob']:,.2f}")

# 3. Guardar informe JSON
with open(RUTA_JSON_INFORME, "w", encoding="utf-8") as f:
    json.dump({"total_anomalias": len(anomalias), "anomalias": anomalias}, f, indent=4, ensure_ascii=False)

print(f"✓ Informe de anomalías guardado con éxito en: {RUTA_JSON_INFORME}")
print("=========================================")

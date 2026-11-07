"""
==============================================================================
SOLUCIÓN — MÓDULO 4 — TEMA 1 — EJERCICIO 1: EXPORTADOR CSV Y JSON
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Usamos csv.DictWriter para escribir la cabecera y filas del archivo CSV.
2. Usamos json.dump() con indent=4 para guardar el JSON estructurado de forma legible.
"""

import csv
import json
import os

print("=== EXPORTADOR DE DATASETS A FORMATOS CSV Y JSON ===\n")

CARPETA = "datos_temporales"
os.makedirs(CARPETA, exist_ok=True)

RUTA_CSV = os.path.join(CARPETA, "ventas_exportadas.csv")
RUTA_JSON = os.path.join(CARPETA, "ventas_exportadas.json")

ventas = [
    {"id": 101, "empresa": "TechBolivia", "monto_bob": 4500.50, "ciudad": "La Paz"},
    {"id": 102, "empresa": "Comercial Paititi", "monto_bob": 18500.00, "ciudad": "Santa Cruz"},
    {"id": 103, "empresa": "Servicios Tunari", "monto_bob": 890.00, "ciudad": "Cochabamba"},
]

# 1. Exportar a CSV con DictWriter
with open(RUTA_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "empresa", "monto_bob", "ciudad"])
    writer.writeheader()
    writer.writerows(ventas)

print(f"✓ Archivo CSV exportado en: {RUTA_CSV}")

# 2. Exportar a JSON con json.dump()
with open(RUTA_JSON, "w", encoding="utf-8") as f:
    json.dump({"total_registros": len(ventas), "ventas": ventas}, f, indent=4, ensure_ascii=False)

print(f"✓ Archivo JSON exportado en: {RUTA_JSON}")
print("===================================================")

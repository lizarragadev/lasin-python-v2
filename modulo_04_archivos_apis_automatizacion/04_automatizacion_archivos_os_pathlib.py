"""
==============================================================================
MÓDULO 4 — LECCIÓN 4: AUTOMATIZACIÓN DE ARCHIVOS Y DIRECTORIOS CON OS Y PATHLIB
Curso: Python Nivel Básico - LASIN
==============================================================================

LIBRERÍAS DE AUTOMATIZACIÓN EN PYTHON:
1. pathlib (Path):
   - Estándar moderno Orientado a Objetos para manipular rutas de archivos.
   - Permite combinar rutas con el operador '/' (ej. ruta / "subcarpeta") de forma
     compatible tanto con Windows como con Mac/Linux.
   - Métodos útiles: .mkdir(), .exists(), .is_file(), .suffix (extensión), .stem (nombre sin extensión).

2. shutil (Shell Utilities):
   - Módulo de alto nivel para mover (shutil.move) y copiar (shutil.copy) archivos entre carpetas.

3. datetime:
   - Permite generar marcas de tiempo (timestamps) para renombrar archivos sin sobreescribirlos.
==============================================================================
"""

import os
import shutil
from datetime import datetime
from pathlib import Path

print("=== AUTOMATIZACIÓN DE PROCESAMIENTO DE ARCHIVOS ===\n")

# Definición de directorios de trabajo usando Path (Pathlib)
BASE_DIR = Path("datos_temporales") / "sistema_automatizacion"
INBOX_DIR = BASE_DIR / "inbox"
PROCESSED_DIR = BASE_DIR / "procesados"

# Crear estructura de carpetas automáticamente si no existen
# parents=True crea carpetas intermedias; exist_ok=True ignora el error si la carpeta ya existe
INBOX_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------------------
# 1. CREACIÓN DE ARCHIVOS SIMULADOS EN LA CARPETA INBOX
# ------------------------------------------------------------------------------
archivos_prueba = [
    "reporte_ventas_2026.csv",
    "factura_102.txt",
    "backup_config.json",
    "captura_recibo.png"
]

print("1. Colocando archivos simulados de entrada en Inbox...")
for nombre_archivo in archivos_prueba:
    file_path = INBOX_DIR / nombre_archivo
    file_path.write_text(f"Contenido simulado de {nombre_archivo}", encoding="utf-8")

print(f"✓ Archivos listos en carpeta de entrada: {INBOX_DIR}\n")


# ------------------------------------------------------------------------------
# 2. PROCESO AUTOMÁTICO DE CLASIFICACIÓN, RENOMBRADO Y MOVIMIENTO
# ------------------------------------------------------------------------------
print("2. Iniciando proceso automático de clasificación y movimiento...")

archivos_procesados_count = 0
resumen_movimientos = []

# Obtenemos la marca de tiempo actual (ej: "20260918_103000")
fecha_hoy = datetime.now().strftime("%Y%m%d_%H%M%S")

# .iterdir() recorre todos los archivos y carpetas dentro de INBOX_DIR
for archivo in INBOX_DIR.iterdir():
    if archivo.is_file():
        # archivo.suffix obtiene la extensión (ej. '.csv' -> 'csv')
        extension = archivo.suffix.lower().replace(".", "")
        
        # Subcarpeta de destino según la extensión del archivo (ej: procesados/csv/)
        subcarpeta_destino = PROCESSED_DIR / extension
        subcarpeta_destino.mkdir(exist_ok=True)
        
        # Generamos un nuevo nombre adjuntando el timestamp (ej: reporte_20260918_103000.csv)
        nuevo_nombre = f"{archivo.stem}_{fecha_hoy}{archivo.suffix}"
        destino_final = subcarpeta_destino / nuevo_nombre

        # shutil.move mueve el archivo a su nueva ubicación
        shutil.move(str(archivo), str(destino_final))
        
        archivos_procesados_count += 1
        resumen_movimientos.append({
            "original": archivo.name,
            "nuevo": nuevo_nombre,
            "destino": str(subcarpeta_destino.name)
        })

# ------------------------------------------------------------------------------
# 3. RESUMEN FINAL DEL PROCESO DE AUTOMATIZACIÓN
# ------------------------------------------------------------------------------
print("\n" + "=" * 55)
print("       RESUMEN FINAL DEL PROCESO AUTOMÁTICO       ")
print("=" * 55)
print(f"• Total de archivos clasificados y movidos: {archivos_procesados_count}")
for item in resumen_movimientos:
    print(f"  • Archivo '{item['original']}' -> Movido a '/{item['destino']}' como '{item['nuevo']}'")
print("=" * 55)

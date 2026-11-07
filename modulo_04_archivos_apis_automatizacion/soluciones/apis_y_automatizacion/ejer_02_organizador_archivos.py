"""
==============================================================================
SOLUCIÓN — MÓDULO 4 — TEMA 2 — EJERCICIO 2: ORGANIZADOR AUTOMÁTICO DE ARCHIVOS
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Usamos pathlib.Path para manipular directorios.
2. Usamos shutil.move() para mover archivos a subcarpetas clasificadas por extensión.
"""

import shutil
from pathlib import Path

print("=== ORGANIZADOR AUTOMÁTICO DE ARCHIVOS ===\n")

BASE_DIR = Path("datos_temporales") / "descargas_temp"
BASE_DIR.mkdir(parents=True, exist_ok=True)

# Crear archivos simulados para probar la clasificación
(BASE_DIR / "documento.txt").write_text("Texto de prueba", encoding="utf-8")
(BASE_DIR / "foto.png").write_text("Datos imagen", encoding="utf-8")
(BASE_DIR / "reporte.csv").write_text("a,b,c", encoding="utf-8")

archivos_movidos = 0

for archivo in BASE_DIR.iterdir():
    if archivo.is_file():
        ext = archivo.suffix.lower().replace(".", "")
        if not ext:
            continue
        
        destino_dir = BASE_DIR / ext
        destino_dir.mkdir(exist_ok=True)
        destino_final = destino_dir / archivo.name
        
        shutil.move(str(archivo), str(destino_final))
        print(f"✓ Clasificado '{archivo.name}' -> Mover a '{destino_final}'")
        archivos_movidos += 1

print(f"• Total de archivos clasificados: {archivos_movidos}")
print("==========================================")

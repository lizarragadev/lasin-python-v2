"""
==============================================================================
MÓDULO 4 — LECCIÓN 1: LECTURA Y ESCRITURA DE ARCHIVOS DE TEXTO (.txt) Y CSV (.csv)
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Sentencia 'with open(ruta, modo, encoding="utf-8") as archivo:':
   - 'with' es un Gestor de Contexto (Context Manager). Garantiza que el archivo se CIERRE
     automáticamente al salir del bloque, previniendo fuga de memoria o corrupción de archivos.
   - Modos de apertura:
     * 'w' (write): Crea o sobrescribe por completo el archivo.
     * 'r' (read): Abre el archivo en modo de solo lectura.
     * 'a' (append): Anexa contenido al final sin borrar lo existente.
   - encoding="utf-8": Evita errores de caracteres con acentos o la 'ñ'.

2. Módulo nativo 'csv':
   - DictWriter: Permite guardar una lista de diccionarios directamente como filas de una tabla CSV.
   - DictReader: Lee un CSV convirtiendo cada fila en un diccionario donde la clave es el encabezado.
==============================================================================
"""

import csv
import os

print("=== PERSISTENCIA EN ARCHIVOS TXT Y CSV ===\n")

# Directorio de trabajo local seguro
CARPETA_DATOS = "datos_temporales"
os.makedirs(CARPETA_DATOS, exist_ok=True)

RUTA_TXT = os.path.join(CARPETA_DATOS, "bitacora_log.txt")
RUTA_CSV = os.path.join(CARPETA_DATOS, "ventas_dataset.csv")

# ==============================================================================
# 1. ARCHIVOS DE TEXTO PLANO (.txt)
# ==============================================================================
print("--- 1. ESCRITURA Y LECTURA DE ARCHIVOS .TXT ---")

# Escritura en .txt usando 'w'
with open(RUTA_TXT, "w", encoding="utf-8") as archivo_txt:
    archivo_txt.write("BITÁCORA DE SISTEMA - DATAFLOW LASIN\n")
    archivo_txt.write("2026-09-18 10:00:00 - Sistema iniciado correctamente\n")
    archivo_txt.write("2026-09-18 10:05:00 - Procesando 3 registros comerciales\n")

print(f"✓ Archivo TXT escrito exitosamente en: {RUTA_TXT}")

# Lectura de .txt usando 'r'
with open(RUTA_TXT, "r", encoding="utf-8") as archivo_txt:
    contenido = archivo_txt.read()  # .read() carga todo el texto en una variable
    print("\nContenido leído del archivo TXT:")
    print(contenido)


# ==============================================================================
# 2. ARCHIVOS TABULARES (.csv)
# ==============================================================================
print("--- 2. ESCRITURA Y LECTURA DE ARCHIVOS .CSV ---")

dataset_ejemplo = [
    {"id": 101, "empresa": "Comercial Alfa", "monto": 1500.50, "ciudad": "La Paz"},
    {"id": 102, "empresa": "Servicios Beta", "monto": 8500.00, "ciudad": "Santa Cruz"},
    {"id": 103, "empresa": "Importadora Gamma", "monto": 420.00, "ciudad": "Cochabamba"},
]

encabezados = ["id", "empresa", "monto", "ciudad"]

# Escritura con csv.DictWriter
# newline="" evita que en Windows se agreguen líneas en blanco adicionales
with open(RUTA_CSV, "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
    escritor.writeheader()   # Escribe la fila inicial de encabezados (id, empresa, monto, ciudad)
    escritor.writerows(dataset_ejemplo) # Escribe todas las filas de la lista de diccionarios

print(f"✓ Archivo CSV creado exitosamente en: {RUTA_CSV}")

# Lectura con csv.DictReader
print("\nLeyendo registros desde el archivo CSV generado:")
with open(RUTA_CSV, "r", encoding="utf-8") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        # IMPORTANTE: Al leer de un CSV, TODOS los valores se leen como cadenas de texto (str).
        # Para hacer operaciones numéricas con el monto, debemos hacer float(fila["monto"]).
        monto_float = float(fila["monto"])
        print(f"  • ID {fila['id']}: {fila['empresa']} ({fila['ciudad']}) -> Bs. {monto_float:,.2f}")

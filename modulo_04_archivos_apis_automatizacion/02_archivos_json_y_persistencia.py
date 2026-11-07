"""
==============================================================================
MÓDULO 4 — LECCIÓN 2: MANEJO DEL FORMATO JSON Y PERSISTENCIA DE INFORMACIÓN
Curso: Python Nivel Básico - LASIN
==============================================================================

¿QUÉ ES EL FORMATO JSON Y POR QUÉ ES EL ESTÁNDAR MUNDIAL?
- JSON (JavaScript Object Notation) es un formato de texto ligero y universal para
  intercambiar datos entre sistemas, servidores e Internet.
- Su estructura coincide casi perfectamente con los Diccionarios y Listas de Python:
  * Diccionario de Python <---> Objeto JSON { "clave": "valor" }
  * Lista de Python <---> Arreglo JSON [ elemento1, elemento2 ]

FUNCIONES DEL MÓDULO NATIVO 'json':
1. json.dump(objeto, archivo, indent=4, ensure_ascii=False):
   - Escribe un diccionario/lista directamente en un ARCHIVO .json físico.
   - indent=4: Formatea el archivo con 4 espacios de sangría para que sea legible por humanos.
   - ensure_ascii=False: Permite que los caracteres con acento o la 'ñ' se guarden correctamente.

2. json.load(archivo):
   - Lee un archivo .json y lo convierte en una estructura nativa de Python (dict o list).

3. json.dumps() / json.loads():
   - Hacen lo mismo pero sobre CADENAS DE TEXTO (Strings) en memoria en lugar de archivos.
==============================================================================
"""

import json
import os

print("=== ARCHIVOS JSON Y PERSISTENCIA EN PYTHON ===\n")

CARPETA_DATOS = "datos_temporales"
os.makedirs(CARPETA_DATOS, exist_ok=True)
RUTA_JSON = os.path.join(CARPETA_DATOS, "base_datos_dataflow.json")

# Estrutura completa de Python (Diccionario que contiene metadatos y una lista de diccionarios)
sistema_dataflow = {
    "sistema": "DataFlow Core",
    "version": 2.0,
    "ultima_actualizacion": "2026-09-18",
    "registros_analizados": 3,
    "transacciones": [
        {"id": 1, "empresa": "TechBolivia", "monto": 1500.50, "validado": True},
        {"id": 2, "empresa": "Servicios Andes", "monto": 890.00, "validado": True},
        {"id": 3, "empresa": "Constructora Sol", "monto": 45000.00, "validado": False}
    ]
}


# ==============================================================================
# 1. GUARDAR DE PYTHON A ARCHIVO .JSON (json.dump)
# ==============================================================================
print("--- 1. GUARDAR DATOS EN ARCHIVO .JSON ---")

with open(RUTA_JSON, "w", encoding="utf-8") as archivo_json:
    # dump escribe la estructura en el archivo abierto
    json.dump(sistema_dataflow, archivo_json, indent=4, ensure_ascii=False)

print(f"✓ Estructura de datos guardada exitosamente en: {RUTA_JSON}")


# ==============================================================================
# 2. CARGAR Y RECUPERAR DATOS DESDE ARCHIVO .JSON (json.load)
# ==============================================================================
print("\n--- 2. CARGAR Y RECUPERAR DATOS DESDE ARCHIVO .JSON ---")

with open(RUTA_JSON, "r", encoding="utf-8") as archivo_json:
    # load lee el archivo y retorna la estructura como diccionario/lista de Python
    datos_recuperados = json.load(archivo_json)

print("Sistema:", datos_recuperados["sistema"])
print("Versión leída:", datos_recuperados["version"])
print("Transacciones recuperadas del archivo:")

# Iteramos sobre la lista anidada 'transacciones'
for tx in datos_recuperados["transacciones"]:
    estado = "✓ Validado" if tx["validado"] else "⚠️ Pendiente de revisión"
    print(f"  • ID {tx['id']}: {tx['empresa']} -> Bs. {tx['monto']:,.2f} [{estado}]")

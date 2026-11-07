# Módulo 4 — Archivos, Internet, Módulos y Paquetes

En este cuarto módulo aprenderás a guardar información permanente en archivos TXT, CSV y JSON, consumir APIs reales desde Internet, automatizar tareas del sistema de archivos y comprender el flujo del procesamiento de documentos u OCR.

---

## 📚 Lecciones y Archivos de Código

| Archivo | Tema Principal | Conceptos Clave |
| :--- | :--- | :--- |
| [`01_archivos_txt_y_csv.py`](./01_archivos_txt_y_csv.py) | Persistencia en Archivos | Lectura/Escritura de `.txt` y `.csv` con `with open()` y módulo `csv` |
| [`02_archivos_json_y_persistencia.py`](./02_archivos_json_y_persistencia.py) | Formato JSON | `json.dump()`, `json.load()`, serialización de listas y diccionarios |
| [`03_consumo_apis_internet.py`](./03_consumo_apis_internet.py) | Consumo de APIs Web | HTTP, Requests, JSON respuestas de APIs en vivo (`urllib`) |
| [`04_automatizacion_archivos_os_pathlib.py`](./04_automatizacion_archivos_os_pathlib.py) | Automatización del Sistema | Modulos `os`, `pathlib`, `datetime`, renombrado y clasificación de archivos |
| [`05_demo_ocr_procesamiento_documentos.py`](./05_demo_ocr_procesamiento_documentos.py) | **Demo: OCR / Documentos** | Flujo conceptual Imagen/PDF -> Texto -> Datos estructurados |
| [`06_modulos_propios_y_paquetes.py`](./06_modulos_propios_y_paquetes.py) | Módulos y `pip` / `venv` | Creación de módulos propios, importaciones y paquetes externos |
| [`07_demo_dataflow_v2.py`](./07_demo_dataflow_v2.py) | **Demo: DataFlow v2** | Integración de CSV, JSON, APIs y automatización en un solo script |

---

## 💡 Recomendaciones
Todos los scripts que leen o escriben archivos utilizan rutas seguras y temporales o relativas para ejecutarse en cualquier sistema operativo sin fallos.

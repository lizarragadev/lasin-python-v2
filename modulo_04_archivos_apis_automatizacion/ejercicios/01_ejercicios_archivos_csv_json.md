# Ejercicios Módulo 4 — Tema 1: Persistencia en Archivos CSV y JSON

En esta sección practicarás la creación, escritura y lectura de archivos `.csv` (con `csv.DictWriter` y `csv.DictReader`) y archivos `.json` (con `json.dump` y `json.load`).

---

## 📝 Ejercicio 1: Exportador de Dataset de Ventas a CSV y JSON

### Descripción del Problema
Una empresa necesita exportar un dataset en memoria de sus ventas a dos archivos de persistencia: `ventas_exportadas.csv` y `ventas_exportadas.json`.

### Dataset de Ejemplo
```python
ventas = [
    {"id": 101, "empresa": "TechBolivia", "monto_bob": 4500.50, "ciudad": "La Paz"},
    {"id": 102, "empresa": "Comercial Paititi", "monto_bob": 18500.00, "ciudad": "Santa Cruz"},
    {"id": 103, "empresa": "Servicios Tunari", "monto_bob": 890.00, "ciudad": "Cochabamba"},
]
```

### Requerimientos
1. Usa `with open()` y `csv.DictWriter` para guardar el dataset en formato CSV con sus encabezados.
2. Usa `json.dump()` con `indent=4` y `ensure_ascii=False` para guardar la misma información en JSON.
3. Muestra en pantalla la confirmación de archivos generados.

---

## 📝 Ejercicio 2: Lector de CSV y Generador de Informe JSON de Anomalías

### Descripción del Problema
Dado un archivo `transacciones_raw.csv` previamente guardado, debes crear un script que lo lea con `csv.DictReader`, identifique los registros cuyo monto supere los `20,000 Bs.` (Anomalías de riesgo alto), y guarde un informe resumido en formato JSON (`informe_anomalias.json`).

### Ejemplo de Salida Esperada en Consola
```text
=== LECTOR Y PROCESADOR DE CSV A JSON ===
• Registros leídos desde CSV: 3
• Anomalías detectadas (> 20.000 Bs): 1
  - ID 102 (Comercial Paititi): Bs. 18,500.00
✓ Informe de anomalías guardado con éxito en: informe_anomalias.json
=========================================
```

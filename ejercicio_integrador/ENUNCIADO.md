# 📦 Ejercicio Integrador: Sistema de Envíos y Auditoría Logística (LogiFlow)

**Curso de Python — Nivel Básico (LASIN)**  
*Objetivo:* Desarrollar un script en Python modular y resiliente que procese un lote de envíos desde un archivo CSV, modele la información mediante Programación Orientada a Objetos básica, consulte el tipo de cambio oficial desde una API web, persista los datos en SQLite y exporte una auditoría en JSON.

---

## 🎯 Conceptos Evaluados (Alineados con el Avance del Curso)

El ejercicio integra **exclusivamente** las herramientas y buenas prácticas vistas en clase:

* **Módulo 1:** Tipos de datos primitivos (`int`, `float`, `str`), operadores aritméticos y **f-strings con alineación tabular** (`:<`, `:>`, `:,.2f`).
* **Módulo 2:** Estructuras condicionales (`if / elif / else`) para recargos logísticos y bucles de control (`for`).
* **Módulo 3:** Colecciones (`list`, `dict`), **conjuntos (`set`) para deduplicación**, comprensiones de listas, **funciones modulares con retorno** y control de excepciones con **`try / except`**.
* **Módulo 4:** Lectura de archivos **CSV** con `csv.DictReader`, exportación a **JSON** con `json.dump`, y **consumo de APIs en Internet** con `urllib.request` y fallback ante desconexión.
* **Módulo 5:** **Introducción a POO** mediante clases tradicionales (`class`, constructor `__init__`, métodos de instancia) y persistencia relacional con **SQLite** (`sqlite3`, sentencias parametrizadas seguras `?`).
  > *(Nota: No se requiere `@dataclass`, `Enum`, herencia avanzada ni librerías externas).*

---

## 📋 Especificaciones Técnicas

Debes desarrollar el archivo `solucion_ejercicio_integrador.py` implementando las siguientes etapas:

### 1. Modelado con POO Básica (`class Envio`)
Crea una clase tradicional llamada `Envio`:
* **Constructor `__init__(self, id_envio, cliente, peso_kg, costo_base, tipo)`:**
  * Debe almacenar los atributos limpios (`strip()`, tipos convertidos a `float` o `str`, y `tipo` en mayúsculas).
  * **Validaciones:** Lanza un `ValueError` si `peso_kg <= 0` o si `costo_base < 0`.
* **Método `calcular_costo_final(self) -> float`:**
  * Determina el costo final en USD aplicando la tarifa según el tipo de envío:
    * `"EXPRESS"`: recargo del **20%** (`costo_base * 1.20`).
    * `"REFRIGERADO"`: recargo del **35%** (`costo_base * 1.35`).
    * `"ESTANDAR"` (o cualquier otro): **costo base directo** (`costo_base`).
    * Redondear el resultado a 2 decimales.
* **Método `a_diccionario(self) -> dict`:**
  * Retorna un diccionario con las claves: `id_envio`, `cliente`, `peso_kg`, `tipo`, `costo_final_usd`.

---

### 2. Consumo de API Web con Fallback (`urllib.request` y `json`)
Implementa la función `obtener_tipo_cambio() -> float`:
* Realiza una petición `GET` a la API pública de divisas:
  ```text
  https://open.er-api.com/v6/latest/USD
  ```
* Decodifica la respuesta JSON y extrae la tasa de cambio USD a Bolivianos (`rates["BOB"]`).
* **Resiliencia (Manejo de Errores):** Si no hay conexión a Internet, ocurre un timeout o la API falla, captura la excepción con `try-except` y retorna una tasa de contingencia fija por defecto: **`6.96`**.

---

### 3. Ingesta, Deduplicación y Limpieza de Datos (`csv`, `set`, `try-except`)
Implementa la función `cargar_envios(ruta_csv: str) -> list[Envio]`:
* Lee el archivo `datos_envios.csv` utilizando `csv.DictReader`.
* **Deduplicación:** Utiliza un conjunto (`set`) para almacenar los `id_envio` ya leídos. Si un ID ya existe en el conjunto, muestra un aviso por consola (`[AVISO] Omitido por duplicado...`) y omite la fila.
* **Manejo de Excepciones:** Dentro de un bloque `try-except (ValueError, KeyError)`:
  * Instancia el objeto `Envio(...)`.
  * Si la fila tiene peso negativo, costo negativo o tipos de datos corruptos, captura el error, imprime una advertencia y descarta el registro sin interrumpir la ejecución del programa.
* Retorna la lista con los objetos `Envio` válidos.

---

### 4. Persistencia en Base de Datos Relacional (`sqlite3`)
Implementa la función `guardar_en_sqlite(envios: list[Envio], tasa: float, ruta_db: str) -> int`:
* Conéctate a la base de datos `envios.db` usando `sqlite3.connect()`.
* Crea la tabla `envios` si no existe:
  ```sql
  CREATE TABLE IF NOT EXISTS envios (
      id TEXT PRIMARY KEY,
      cliente TEXT NOT NULL,
      tipo TEXT NOT NULL,
      peso_kg REAL NOT NULL,
      costo_usd REAL NOT NULL,
      costo_bob REAL NOT NULL
  )
  ```
* Prepara los registros a insertar (utilizando una comprensión de listas):
  * `(id_envio, cliente, tipo, peso_kg, costo_usd, costo_bob)`.
  * El `costo_bob` se calcula multiplicando el costo final en USD por la tasa obtenida.
* Inserta o actualiza los registros con sentencias parametrizadas seguras (`?`):
  ```sql
  INSERT OR REPLACE INTO envios VALUES (?, ?, ?, ?, ?, ?)
  ```
* Confirma con `commit()`, cierra la conexión y retorna el número de registros guardados.

---

### 5. Exportación de Auditoría a JSON (`json.dump`)
Implementa la función `exportar_resumen_json(envios: list[Envio], tasa: float, ruta_json: str) -> None`:
* Construye un diccionario consolidado que contenga:
  * Nombre del sistema (`"LogiFlow LASIN"`).
  * Cantidad total de envíos procesados (`total_envios`).
  * Tasa de cambio empleada (`tasa_usd_bob`).
  * Sumatoria total en USD (`total_usd`).
  * Sumatoria total en BOB (`total_bob`).
  * Lista detallada de los envíos procesados utilizando el método `e.a_diccionario()`.
* Guarda el diccionario en un archivo `resumen_auditoria.json` usando `json.dump(..., indent=4, ensure_ascii=False)`.

---

### 6. Reporte en Consola con Formato Tabular (f-strings)
Implementa la función `mostrar_reporte(envios: list[Envio], tasa: float) -> None`:
* Imprime una tabla alineada mediante especificadores de formato de cadenas (`f"{valor:<15}"`, `f"{monto:>10,.2f}"`).
* Columnas requeridas: `ID`, `CLIENTE`, `TIPO`, `USD`, `BOB`.
* Muestra al pie de la tabla la cantidad de envíos válidos y la sumatoria total en ambas monedas.

---

### 7. Orquestación del Programa (`main`)
La función principal `main()` debe coordinar el flujo completo:
1. Imprimir encabezado de inicio.
2. Obtener la tasa de cambio mediante la API (o contingencia).
3. Cargar y filtrar los envíos del archivo CSV.
4. Si existen envíos válidos:
   * Mostrar el reporte en consola.
   * Guardar los registros en SQLite (`envios.db`).
   * Exportar el resumen a JSON (`resumen_auditoria.json`).

---

## 📥 Datos de Prueba (`datos_envios.csv`)

El archivo `datos_envios.csv` contiene el siguiente dataset:

```csv
id_envio,cliente,peso_kg,costo_base,tipo
ENV-001,Farmacia Central,12.5,150.0,REFRIGERADO
ENV-002,Distribuidora Norte,45.0,320.0,ESTANDAR
ENV-003,Supermercado Fidalga,120.0,850.0,EXPRESS
ENV-001,Farmacia Central,12.5,150.0,REFRIGERADO
ENV-004,Textiles Andinos,-5.0,200.0,ESTANDAR
ENV-005,Clinica Los Andes,18.0,300.0,REFRIGERADO
```

### Casos de prueba previstos:
1. `ENV-001`: **Válido**. Tipo Refrigerado $\rightarrow 150.00 \times 1.35 = 202.50$ USD.
2. `ENV-002`: **Válido**. Tipo Estándar $\rightarrow 320.00$ USD.
3. `ENV-003`: **Válido**. Tipo Express $\rightarrow 850.00 \times 1.20 = 1,020.00$ USD.
4. `ENV-001`: **Duplicado**. Debe ser detectado por el `set` y omitido.
5. `ENV-004`: **Inválido**. Peso negativo (`-5.0 kg`). El constructor lanza `ValueError` y el bloque `try-except` descarta la fila.
6. `ENV-005`: **Válido**. Tipo Refrigerado $\rightarrow 300.00 \times 1.35 = 405.00$ USD.

---

## 🖥️ Salida Esperada en Consola

```text
=== SISTEMA DE ENVÍOS Y AUDITORÍA LOGIFLOW ===
[API] Tasa obtenida en línea: 1 USD = 6.96 BOB
[AVISO] Omitido por duplicado: ENV-001
[AVISO] Fila descartada (ENV-004): El peso debe ser mayor a 0 kg (recibido: -5.0)

========================================================================
ID         CLIENTE                TIPO                  USD                BOB
------------------------------------------------------------------------
ENV-001    Farmacia Central       REFRIGERADO    $   202.50  Bs.   1,409.40
ENV-002    Distribuidora Norte    ESTANDAR       $   320.00  Bs.   2,227.20
ENV-003    Supermercado Fidalga   EXPRESS        $ 1,020.00  Bs.   7,099.20
ENV-005    Clinica Los Andes      REFRIGERADO    $   405.00  Bs.   2,818.80
------------------------------------------------------------------------
TOTAL: 4 envíos válidos | $ 1,947.50 USD | Bs. 13,554.60 BOB
========================================================================

✓ 4 registros guardados en SQLite ('envios.db').
✓ Resumen consolidado exportado a JSON ('resumen_auditoria.json').
```

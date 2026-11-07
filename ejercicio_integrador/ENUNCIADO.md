# 📦 Ejercicio Integrador: Procesador de Envíos Logísticos

**Curso de Python — Nivel Básico (LASIN)**  
*Objetivo:* Construir un script en Python que procese un lote de envíos desde un archivo CSV, valide los datos mediante POO, enriquezca los costos con una API y guarde los resultados en SQLite.

---

## 📋 Requerimientos del Ejercicio

Crea el script `solucion_ejercicio_integrador.py` que cumpla con los siguientes 4 pasos:

### 1. Modelado con POO (`dataclass` y `Enum`)
* Crea un `Enum` llamado `TipoEnvio` con valores: `ESTANDAR`, `EXPRESS`, `REFRIGERADO`.
* Crea una `@dataclass` llamada `Envio`:
  * Atributos: `id_envio` (str), `cliente` (str), `peso_kg` (float), `costo_base` (float), `tipo` (TipoEnvio).
  * Validación en `__post_init__`: lanzar `ValueError` si `peso_kg <= 0` o `costo_base < 0`.
  * Método `calcular_costo_final() -> float`:
    * `ESTANDAR`: costo base.
    * `EXPRESS`: costo base + 20%.
    * `REFRIGERADO`: costo base + 35%.

### 2. Ingesta y Limpieza (`csv`, `pathlib`, `set`, `try-except`)
* Lee el archivo `datos_envios.csv`.
* Usa un `set` para detectar y omitir registros con `id_envio` duplicado.
* Usa un bloque `try-except` para descartar filas con errores de formato o valores negativos (`ValueError`).

### 3. Enriquecimiento con API Web (`urllib.request`)
* Consulta la tasa de cambio USD a BOB desde `https://open.er-api.com/v6/latest/USD`.
* Si no hay conexión o falla la consulta, usa una tasa de contingencia por defecto (`6.96`).

### 4. Persistencia y Reporte (`sqlite3` y `f-strings`)
* Almacena los envíos válidos en una base de datos SQLite llamada `envios.db` (tabla `envios`).
* Imprime en consola un reporte tabular breve y alineado con los totales generales.

---

## 📥 Datos de Entrada (`datos_envios.csv`)

```csv
id_envio,cliente,peso_kg,costo_base,tipo
ENV-001,Farmacia Central,12.5,150.0,REFRIGERADO
ENV-002,Distribuidora Norte,45.0,320.0,ESTANDAR
ENV-003,Supermercado Fidalga,120.0,850.0,EXPRESS
ENV-001,Farmacia Central,12.5,150.0,REFRIGERADO
ENV-004,Textiles Andinos,-5.0,200.0,ESTANDAR
ENV-005,Clinica Los Andes,18.0,300.0,REFRIGERADO
```

*Filas esperadas:*
* `ENV-001`: Válido (Refrigerado: $150 \times 1.35 = 202.50$ USD).
* `ENV-002`: Válido (Estándar: $320.00$ USD).
* `ENV-003`: Válido (Express: $850 \times 1.20 = 1020.00$ USD).
* `ENV-001`: Omitido por duplicado.
* `ENV-004`: Descartado por peso negativo (-5.0 kg).
* `ENV-005`: Válido (Refrigerado: $300 \times 1.35 = 405.00$ USD).

---

## 🖥️ Salida Esperada en Consola

```text
=== SISTEMA DE ENVÍOS LOGIFLOW ===
[API] Tasa obtenida: 1 USD = 6.96 BOB
[AVISO] Omitido por duplicado: ENV-001
[AVISO] Fila descartada (ENV-004): El peso debe ser mayor a 0 kg

----------------------------------------------------------------------
ID         CLIENTE               TIPO            USD           BOB
----------------------------------------------------------------------
ENV-001    Farmacia Central      REFRIGERADO  $   202.50  Bs.  1,409.40
ENV-002    Distribuidora Norte   ESTANDAR     $   320.00  Bs.  2,227.20
ENV-003    Supermercado Fidalga  EXPRESS      $ 1,020.00  Bs.  7,099.20
ENV-005    Clinica Los Andes     REFRIGERADO  $   405.00  Bs.  2,818.80
----------------------------------------------------------------------
TOTAL: 4 envíos válidos | $ 1,947.50 USD | Bs. 13,554.60 BOB
✓ 4 registros guardados exitosamente en SQLite (envios.db).
```

# Ejercicios Módulo 5 — Tema 1: Bases de Datos SQLite e Información Geoespacial (GeoJSON)

En esta sección practicarás consultas relacionales SQL con `sqlite3` y el manejo de coordenadas latitud/longitud con formatos GeoJSON.

---

## 📝 Ejercicio 1: Gestor de Productos en Base de Datos SQLite

### Descripción del Problema
Escribe un script que administre una tabla `productos` en una base de datos local `inventario.db` usando el módulo `sqlite3`.

### Requerimientos
1. Crea la tabla `productos` con columnas: `id` (INTEGER PRIMARY KEY), `nombre` (TEXT), `precio` (REAL), `stock` (INTEGER).
2. Inserta 3 productos usando `cursor.executemany()` y Parameter Binding (`?`).
3. Realiza una consulta `SELECT` para obtener los productos con `precio > 100.0 Bs.` e imprímelos en consola.
4. Ejecuta un `UPDATE` para incrementar el stock del producto con `id = 1` en 5 unidades adicionales.

### Ejemplo de Salida Esperada
```text
=== GESTOR DE INVENTARIO CON SQLITE ===
✓ Base de datos y tabla 'productos' verificadas.
✓ 3 productos insertados en la base de datos.
• Consulta SELECT (Productos con Precio > 100.00 Bs):
  - ID 1: Laptop Gamer (Precio: Bs. 7,500.00 | Stock: 10 u.)
  - ID 2: Monitor IPS (Precio: Bs. 1,400.00 | Stock: 5 u.)
✓ Stock de ID 1 actualizado en la base de datos.
========================================
```

---

## 📝 Ejercicio 2: Calculador de Distancias Geográficas y Exportador GeoJSON

### Descripción del Problema
Una empresa de logística necesita calcular la distancia en km entre su almacén central en La Paz (`Lat: -16.5000, Lon: -68.1500`) y un punto de entrega en Oruro (`Lat: -17.9833, Lon: -67.1500`) usando la fórmula de Haversine. Luego, debe exportar ambos puntos a un archivo `rutas.geojson` con formato GeoJSON `FeatureCollection`.

### Ejemplo de Salida Esperada
```text
=== CALCULADOR DE RUTA Y GENERADOR GEOJSON ===
• Distancia La Paz -> Oruro: 220.45 km
✓ Archivo GeoJSON generado con éxito en: datos_temporales/rutas.geojson
===============================================
```

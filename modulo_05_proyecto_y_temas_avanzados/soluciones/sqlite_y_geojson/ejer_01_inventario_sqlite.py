"""
==============================================================================
SOLUCIÓN — MÓDULO 5 — TEMA 1 — EJERCICIO 1: GESTOR DE INVENTARIO EN SQLITE
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Conectamos con sqlite3.connect().
2. Ejecutamos CREATE TABLE, INSERT INTO con Parameter Binding (?), SELECT y UPDATE.
3. Llamamos a conexion.commit() y conexion.close().
"""

import os
import sqlite3

print("=== GESTOR DE INVENTARIO CON SQLITE ===\n")

CARPETA = "datos_temporales"
os.makedirs(CARPETA, exist_ok=True)
RUTA_DB = os.path.join(CARPETA, "inventario.db")

conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()

# 1. Crear Tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")
conexion.commit()
print("✓ Base de datos y tabla 'productos' verificadas.")

# 2. Insertar registros
productos_iniciales = [
    ("Laptop Gamer", 7500.00, 10),
    ("Monitor IPS", 1400.00, 5),
    ("Cable USB-C", 45.00, 50)
]
cursor.executemany("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", productos_iniciales)
conexion.commit()
print(f"✓ {cursor.rowcount} productos insertados en la base de datos.")

# 3. Consulta SELECT
print("\n• Consulta SELECT (Productos con Precio > 100.00 Bs):")
cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE precio > 100.0")
for id_p, nom, prec, st in cursor.fetchall():
    print(f"  - ID {id_p}: {nom:<16} (Precio: Bs. {prec:,.2f} | Stock: {st} u.)")

# 4. Actualizar Stock
cursor.execute("UPDATE productos SET stock = stock + 5 WHERE id = 1")
conexion.commit()
print("✓ Stock de ID 1 actualizado en la base de datos.")

conexion.close()
print("========================================")

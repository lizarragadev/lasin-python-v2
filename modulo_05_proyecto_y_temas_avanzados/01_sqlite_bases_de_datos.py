"""
==============================================================================
MÓDULO 5 — LECCIÓN 1: BASES DE DATOS RELACIONALES CON PYTHON Y SQLITE
Curso: Python Nivel Básico - LASIN
==============================================================================

¿QUÉ ES SQLITE Y POR QUÉ USARLO EN PYTHON?
- SQLite es un motor de Base de Datos Relacional de código abierto que viene
  INCORPORADO de forma nativa en Python (a través del módulo sqlite3).
- NO requiere instalar ningún servidor adicional (como MySQL o Postgres); la base
  de datos entera vive en un único archivo con extensión .db en el disco duro.

CONCEPTOS Y SENTENCIAS SQL BÁSICAS:
1. sqlite3.connect(ruta): Conecta con la base de datos (o la crea si no existe).
2. conexion.cursor(): Objeto 'Cursor' que nos permite ejecutar instrucciones SQL.
3. CREATE TABLE: Define el esquema de la tabla, sus columnas y tipos de datos.
4. INSERT INTO: Inserta nuevas filas/registros en la tabla.
   ⚠️ SEGURIDAD: Usamos marcadores de posición (?) para prevenir ataques de SQL Injection.
5. SELECT ... WHERE: Consulta y filtra registros de la tabla.
6. UPDATE ... SET: Modifica valores de registros existentes.
7. conexion.commit(): Guarda los cambios de forma permanente en la base de datos.
==============================================================================
"""

import os
import sqlite3  # Módulo nativo de Python para bases de datos SQLite

print("=== INTRODUCCIÓN A BASES DE DATOS (PYTHON + SQLITE) ===\n")

# Directorio local seguro
CARPETA_DATOS = "datos_temporales"
os.makedirs(CARPETA_DATOS, exist_ok=True)
RUTA_DB = os.path.join(CARPETA_DATOS, "empresa_dataflow.db")

# ==============================================================================
# 1. ESTABLECER CONEXIÓN Y CREAR LA TABLA SQL
# ==============================================================================
# connect() abre la conexión al archivo .db
conexion = sqlite3.connect(RUTA_DB)
cursor = conexion.cursor()

print(f"1. Conexión establecida con la base de datos: {RUTA_DB}")

# Definimos la sentencia SQL para crear la tabla 'transacciones'
sql_crear_tabla = """
CREATE TABLE IF NOT EXISTS transacciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    empresa TEXT NOT NULL,
    monto REAL NOT NULL,
    ciudad TEXT NOT NULL,
    estado TEXT DEFAULT 'PENDIENTE'
)
"""
cursor.execute(sql_crear_tabla)
conexion.commit()  # Guardamos los cambios estructurales en el archivo
print("✓ Tabla 'transacciones' creada / verificada con éxito.")


# ==============================================================================
# 2. INSERTAR REGISTROS (INSERT INTO CON PARAMETER BINDING '?')
# ==============================================================================
print("\n2. Insertando registros de transacciones...")

registros_nuevos = [
    ("Comercial Los Andes", 3500.50, "La Paz"),
    ("Importadora El Sol", 12500.00, "Santa Cruz"),
    ("Servicios Tunari", 890.00, "Cochabamba")
]

# Usamos '?' como comodines de seguridad (Parameter Binding) para evitar Inyección SQL
sql_insert = "INSERT INTO transacciones (empresa, monto, ciudad) VALUES (?, ?, ?)"

# executemany inserta una lista completa de tuplas en una sola llamada
cursor.executemany(sql_insert, registros_nuevos)
conexion.commit()
print(f"✓ {cursor.rowcount} registros insertados en la base de datos.")


# ==============================================================================
# 3. CONSULTAR Y FILTRAR REGISTROS (SELECT CON WHERE)
# ==============================================================================
print("\n3. Consultando transacciones mayores a 1.000 Bs. (SELECT ... WHERE):")

sql_select = "SELECT id, empresa, monto, ciudad, estado FROM transacciones WHERE monto > ?"
cursor.execute(sql_select, (1000.0,))

# fetchall() retorna todas las filas que coincidieron con la consulta como una lista de tuplas
filas = cursor.fetchall()

for id_tx, emp, monto, ciu, est in filas:
    print(f"  • ID {id_tx}: {emp:<20} ({ciu:<10}) -> Bs. {monto:<9,.2f} [{est}]")


# ==============================================================================
# 4. ACTUALIZAR ESTADO DE REGISTROS (UPDATE)
# ==============================================================================
print("\n4. Actualizando estado de transacciones de alto monto (UPDATE)...")

sql_update = "UPDATE transacciones SET estado = 'REVISADO' WHERE monto > 10000.0"
cursor.execute(sql_update)
conexion.commit()

print(f"✓ Registros actualizados a estado 'REVISADO': {cursor.rowcount}")

# Cerramos siempre la conexión para liberar bloqueos del archivo .db
conexion.close()
print("\n✓ Conexión a la base de datos cerrada de forma segura.")

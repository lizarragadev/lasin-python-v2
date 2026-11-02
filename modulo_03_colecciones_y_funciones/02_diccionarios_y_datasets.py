"""
==============================================================================
MÓDULO 3 — LECCIÓN 2: DICCIONARIOS Y REPRESENTACIÓN DE DATASETS TABULARES
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Diccionarios (dict):
   - Estructura basada en pares Clave-Valor: { "clave1": valor1, "clave2": valor2 }.
   - Permiten nombrar los datos (ej. "monto": 4500) en lugar de depender solo de posiciones numéricas.
   - Las claves deben ser únicas (generalmente cadenas de texto).

2. Representación de un Dataset (Lista de Diccionarios):
   - En Ciencia de Datos y Desarrollo de Software, la forma estándar de representar
     una tabla de datos en Python puro es usando una LISTA donde cada elemento es
     un DICCIONARIO que representa una FILA.
==============================================================================
"""

print("=== DICCIONARIOS Y DATASETS EN PYTHON ===\n")

# ==============================================================================
# 1. DICCIONARIO INDIVIDUAL (UN REGISTRO ESTRUCTURADO)
# ==============================================================================
print("--- 1. UN REGISTRO ESTRUCTURADO (DICCIONARIO) ---")

# Creamos un registro de prueba
registro_empresa = {
    "id": 1001,
    "nombre": "TechBolivia SRL",
    "monto": 4500.50,
    "ciudad": "La Paz",
    "activo": True
}

print("Diccionario completo:", registro_empresa)

# Acceso a valores mediante su clave entre corchetes ['clave']
print(f"• ID del Registro:       {registro_empresa['id']}")
print(f"• Nombre de la Empresa:  {registro_empresa['nombre']}")
print(f"• Monto Registrado:      Bs. {registro_empresa['monto']:,.2f}")

# Acceso seguro mediante .get('clave', valor_defecto) -> Evita que el programa se caiga si la clave no existe
categoria = registro_empresa.get("categoria", "Sin Categoría")
print(f"• Categoría (.get()):    {categoria}")

# Modificación de un valor existente
registro_empresa["monto"] = 5200.00

# Adición de una nueva clave-valor al diccionario
registro_empresa["categoria"] = "Tecnología y Software"

print("\nDiccionario actualizado:", registro_empresa)


# ==============================================================================
# 2. REPRESENTACIÓN DE UN DATASET COMPLETO (LISTA DE DICCIONARIOS)
# ==============================================================================
print("\n--- 2. DATASET DE TRANSACCIONES (FILAS DE TABLA EN MEMORIA) ---")

# Dataset representado como lista de diccionarios (equivalente a un Excel o tabla SQL)
dataset_transacciones = [
    {"id": 101, "cliente": "Empresa Alfa", "monto": 1200.0, "ciudad": "La Paz", "riesgo": "Bajo"},
    {"id": 102, "cliente": "Comercial Beta", "monto": 8500.0, "ciudad": "Santa Cruz", "riesgo": "Medio"},
    {"id": 103, "cliente": "Servicios Gamma", "monto": 14500.0, "ciudad": "Cochabamba", "riesgo": "Alto"},
    {"id": 104, "cliente": "Importadora Delta", "monto": 300.0, "ciudad": "La Paz", "riesgo": "Bajo"},
]

print(f"Total de registros cargados en el dataset: {len(dataset_transacciones)}")
print("\nRecorriendo el dataset e imprimiendo la tabla formateada:\n")

# Encabezado de la tabla
print(f"{'ID':<6} | {'CLIENTE':<20} | {'CIUDAD':<12} | {'MONTO (BS)':<12} | {'RIESGO'}")
print("-" * 65)

total_monto = 0.0

# Iteramos sobre la lista de diccionarios fila por fila
for reg in dataset_transacciones:
    total_monto += reg["monto"]
    print(f"{reg['id']:<6} | {reg['cliente']:<20} | {reg['ciudad']:<12} | Bs. {reg['monto']:<9,.2f} | {reg['riesgo']}")

print("-" * 65)
print(f"MONTO TOTAL DEL DATASET CONSOLIDADO: Bs. {total_monto:,.2f}")

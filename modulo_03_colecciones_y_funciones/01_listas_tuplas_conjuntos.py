"""
==============================================================================
MÓDULO 3 — LECCIÓN 1: COLECCIONES BÁSICAS (LISTAS, TUPLAS Y CONJUNTOS)
Curso: Python Nivel Básico - LASIN
==============================================================================

COMPARATIVA DE ESTRUCTURAS DE DATOS EN PYTHON:
1. Listas (list) -> Sintaxis: [elem1, elem2]
   - Propiedades: ORDENADAS, MUTABLES (se pueden agregar/eliminar/modificar), PERMITEN DUPLICADOS.
   - Usos típicos: Datasets que cambian en el tiempo, secuencias de ventas, filas de tablas.

2. Tuplas (tuple) -> Sintaxis: (elem1, elem2)
   - Propiedades: ORDENADAS, INMUTABLES (NO se pueden modificar tras su creación), PERMITEN DUPLICADOS.
   - Usos típicos: Coordenadas geográficas (Lat, Lon), constantes fijas de configuración.

3. Conjuntos (set) -> Sintaxis: {elem1, elem2}
   - Propiedades: DESORDENADOS, MUTABLES, NO PERMITEN DUPLICADOS.
   - Usos típicos: Eliminación instantánea de duplicados, uniones e intersecciones de conjuntos.
==============================================================================
"""

print("=== COLECCIONES EN PYTHON: LISTAS, TUPLAS Y CONJUNTOS ===\n")

# ==============================================================================
# 1. LISTAS (LIST): FLEXIBLES Y MUTABLES []
# ==============================================================================
print("--- 1. LISTAS (Mutables y Ordenadas) ---")
ciudades = ["La Paz", "Santa Cruz", "Cochabamba", "Oruro"]
print("Lista inicial de ciudades:", ciudades)

# .append(valor): Agrega un elemento AL FINAL de la lista
ciudades.append("Sucre")

# .insert(indice, valor): Inserta un elemento en una posición específica (los demás se desplazan)
ciudades.insert(1, "El Alto")
print("Lista tras .append() e .insert():", ciudades)

# .remove(valor): Busca el elemento por su nombre y lo elimina (falla si no existe)
ciudades.remove("Oruro")

# .pop(): Elimina el ÚLTIMO elemento de la lista y lo retorna
ciudad_removida = ciudades.pop()
print(f"Ciudad eliminada con .pop(): {ciudad_removida}")
print("Lista final de ciudades:", ciudades)


# ==============================================================================
# 2. TUPLAS (TUPLE): ESTRUCTURAS INMUTABLES ()
# ==============================================================================
print("\n--- 2. TUPLAS (Inmutables y Fijas) ---")

# Las tuplas protegen los datos contra modificaciones accidentales en el programa
coordenadas_la_paz = (-16.5000, -68.1500)  # (Latitud, Longitud)

print("Coordenadas de La Paz (Lat, Lon):", coordenadas_la_paz)
print("Latitud  [0]:", coordenadas_la_paz[0])
print("Longitud [1]:", coordenadas_la_paz[1])

# Intentar modificar un elemento de una tupla genera un TypeError (descomentar para comprobar):
# coordenadas_la_paz[0] = -17.0000  # TypeError: 'tuple' object does not support item assignment


# ==============================================================================
# 3. CONJUNTOS (SET): ELIMINACIÓN DE DUPLICADOS {}
# ==============================================================================
print("\n--- 3. CONJUNTOS / SETS (Sin elementos duplicados) ---")

# Lista cruda recibida con categorías duplicadas
categorias_raw = ["Ventas", "Servicios", "Ventas", "Alquiler", "Servicios", "Ventas"]
print("Lista original con duplicados:", categorias_raw)

# Convertir la lista a set(lista) elimina automáticamente todos los valores repetidos
categorias_unicas = set(categorias_raw)
print("Conjunto de categorías únicas (set):", categorias_unicas)

# .add(valor): Agrega un nuevo elemento (si ya existe, no hace nada)
categorias_unicas.add("Consultoría")
print("Conjunto actualizado tras .add():", categorias_unicas)


# ==============================================================================
# 4. RESUMEN Y RECOMENDACIÓN DE USO
# ==============================================================================
print("\n--- RESUMEN Y RECOMENDACIÓN DIDÁCTICA ---")
print("• Usa LISTAS [] cuando necesites una secuencia que cambiará con frecuencia (ej. transacciones).")
print("• Usa TUPLAS () para registros de solo lectura (ej. coordenadas lat/lon, pares clave-valor).")
print("• Usa CONJUNTOS {} para filtrar duplicados de una lista de datos en una sola línea.")

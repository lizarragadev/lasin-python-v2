"""
==============================================================================
SOLUCIÓN — MÓDULO 5 — TEMA 1 — EJERCICIO 2: DISTANCIA GEOGRÁFICA Y GEOJSON
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Usamos la fórmula de Haversine con math.radians, math.sin, math.cos, math.atan2.
2. Construimos una estructura GeoJSON FeatureCollection con coordenadas [lon, lat].
3. Guardamos el resultado en un archivo .geojson con json.dump().
"""

import math
import json
import os

print("=== CALCULADOR DE RUTA Y GENERADOR GEOJSON ===\n")

CARPETA = "datos_temporales"
os.makedirs(CARPETA, exist_ok=True)
RUTA_GEOJSON = os.path.join(CARPETA, "rutas.geojson")

def calcular_haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    RADIO_TIERRA_KM = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi, dlam = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(RADIO_TIERRA_KM * c, 2)

# Puntos de interés
la_paz = {"nombre": "La Paz", "lat": -16.5000, "lon": -68.1500}
oruro = {"nombre": "Oruro", "lat": -17.9833, "lon": -67.1500}

distancia = calcular_haversine_km(la_paz["lat"], la_paz["lon"], oruro["lat"], oruro["lon"])
print(f"• Distancia {la_paz['nombre']} -> {oruro['nombre']}: {distancia} km")

# Estructura GeoJSON estándar (OJO: en GeoJSON las coordenadas son [longitud, latitud])
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [la_paz["lon"], la_paz["lat"]]},
            "properties": {"nombre": la_paz["nombre"]}
        },
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [oruro["lon"], oruro["lat"]]},
            "properties": {"nombre": oruro["nombre"]}
        }
    ]
}

with open(RUTA_GEOJSON, "w", encoding="utf-8") as f:
    json.dump(geojson_data, f, indent=4, ensure_ascii=False)

print(f"✓ Archivo GeoJSON generado con éxito en: {RUTA_GEOJSON}")
print("===============================================")

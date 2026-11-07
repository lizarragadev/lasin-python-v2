"""
==============================================================================
MÓDULO 5 — LECCIÓN 2: INTRODUCCIÓN DIDÁCTICA A DATOS GEOESPACIALES Y GEOJSON
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Coordenadas Geográficas (Latitud y Longitud):
   - Latitud: Posición Norte/Sur respecto al Ecuador (-90 a +90).
   - Longitud: Posición Este/Oeste respecto a Greenwich (-180 a +180).
   - Ejemplo: La Paz, Bolivia -> Latitud: -16.5000, Longitud: -68.1500.

2. Fórmula de Haversine:
   - Ecuación matemática que calcula la distancia en el círculo máximo entre dos
     puntos de la superficie terrestre a partir de sus latitudes y longitudes.

3. Formato GeoJSON:
   - Estándar abierto basado en JSON para representar características geográficas.
   - OJO: En GeoJSON, las coordenadas se escriben en el orden [LONGITUD, LATITUD].
==============================================================================
"""

import math
import json

print("=== INTRODUCCIÓN A DATOS GEOESPACIALES CON PYTHON ===\n")

# 1. COLECCIÓN DE COORDENADAS DE SEDES OPERATIVAS EN BOLIVIA
ciudades_bolivia = [
    {"nombre": "La Paz", "lat": -16.5000, "lon": -68.1500},
    {"nombre": "Santa Cruz de la Sierra", "lat": -17.7833, "lon": -63.1833},
    {"nombre": "Cochabamba", "lat": -17.3895, "lon": -66.1568},
    {"nombre": "Oruro", "lat": -17.9833, "lon": -67.1500}
]

print("1. Coordenadas geográficas de sedes registradas:")
for c in ciudades_bolivia:
    print(f"  • {c['nombre']:<24}: Latitud {c['lat']:.4f} | Longitud {c['lon']:.4f}")


# ------------------------------------------------------------------------------
# 2. CÁLCULO DE DISTANCIA GEOGRÁFICA CON FÓRMULA DE HAVERSINE
# ------------------------------------------------------------------------------
def calcular_distancia_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calcula la distancia geodésica en kilómetros entre dos coordenadas en la Tierra."""
    RADIO_TIERRA_KM = 6371.0  # Radio medio de la Tierra en km
    
    # Convertimos los grados decimales a radianes (math.radians)
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Fórmula esférica del seno inverso
    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(RADIO_TIERRA_KM * c, 2)


print("\n2. Distancias aproximadas calculadas desde La Paz:")
d_lp_cbba = calcular_distancia_km(-16.5000, -68.1500, -17.3895, -66.1568)
d_lp_scz = calcular_distancia_km(-16.5000, -68.1500, -17.7833, -63.1833)

print(f"• Distancia La Paz -> Cochabamba:       {d_lp_cbba} km")
print(f"• Distancia La Paz -> Santa Cruz:       {d_lp_scz} km")


# ------------------------------------------------------------------------------
# 3. CONSTRUCCIÓN DE FORMATO GEOJSON ESTÁNDAR
# ------------------------------------------------------------------------------
# Un GeoJSON es una estructura de dict de Python con claves 'type', 'geometry' y 'properties'

geojson_feature_collection = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                # IMPORTANTE: En el estándar GeoJSON el orden es [LONGITUD, LATITUD]
                "coordinates": [c["lon"], c["lat"]]
            },
            "properties": {
                "ciudad": c["nombre"],
                "pais": "Bolivia"
            }
        }
        for c in ciudades_bolivia
    ]
}

print("\n3. Estructura GeoJSON generada por Python (Primer punto):")
print(json.dumps(geojson_feature_collection["features"][0], indent=2))

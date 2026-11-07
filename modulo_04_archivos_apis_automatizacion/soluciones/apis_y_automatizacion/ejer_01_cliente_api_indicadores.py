"""
==============================================================================
SOLUCIÓN — MÓDULO 4 — TEMA 2 — EJERCICIO 1: CLIENTE API DE USUARIOS
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. urllib.request.urlopen() realiza la solicitud GET HTTP.
2. json.loads() decodifica el cuerpo recibido a lista de diccionarios.
"""

import json
import urllib.request
import urllib.error

print("=== CLIENTE API DE USUARIOS DE INTERNET ===\n")

URL_API = "https://jsonplaceholder.typicode.com/users"

try:
    req = urllib.request.Request(URL_API, headers={'User-Agent': 'Python-LASIN/1.0'})
    with urllib.request.urlopen(req, timeout=5) as res:
        data = json.loads(res.read().decode('utf-8'))

    print("=== USUARIOS OBTENIDOS DE LA API WEB ===")
    for user in data[:5]:
        nombre_empresa = user.get("company", {}).get("name", "N/A")
        print(f"• ID {user['id']}: {user['name']} (Email: {user['email']}) | Empresa: {nombre_empresa}")
    print("========================================")

except urllib.error.URLError as err:
    print(f"❌ Error de conexión de red: {err}")

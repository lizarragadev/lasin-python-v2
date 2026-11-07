"""
==============================================================================
MÓDULO 4 — LECCIÓN 3: CONSUMO DE APIS WEB E INTERNET CON PYTHON
Curso: Python Nivel Básico - LASIN
==============================================================================

¿QUÉ ES UNA API REST Y CÓMO FUNCIONA?
- API (Application Programming Interface): Servicio publicado en Internet que
  permite a dos programas comunicarse e intercambiar información estructurada (JSON).
- Arquitectura Cliente-Servidor:
  * Cliente (Nuestro script en Python): Envía una Petición HTTP (Request).
  * Servidor (Servicio en la nube): Procesa la petición y retorna una Respuesta (Response).

CÓDIGOS DE ESTADO HTTP DESTACADOS:
- 200 OK: La petición fue exitosa y el servidor retornó los datos solicitados.
- 404 Not Found: La URL o recurso solicitado no existe en el servidor.
- 500 Internal Server Error: El servidor remoto sufrió un error interno.

FLUJO DEL CONSUMO EN PYTHON:
  1. urllib.request.urlopen(): Envía la petición HTTP a través de la red.
  2. .read().decode('utf-8'): Convierte la respuesta de bytes recibidos a texto.
  3. json.loads(): Convierte el texto JSON a un diccionario/lista ejecutable de Python.
==============================================================================
"""

import json
import urllib.request
import urllib.error

print("=== CONSUMO DE APIS E INTERNET EN PYTHON ===\n")

# URL pública de prueba que devuelve un arreglo JSON de tareas/registros simulados
URL_API = "https://jsonplaceholder.typicode.com/todos"

print(f"Enviando petición HTTP GET a: {URL_API} ...")

try:
    # 1. Creamos la solicitud HTTP incluyendo un encabezado 'User-Agent' para identificarnos profesionalmente
    req = urllib.request.Request(
        URL_API, 
        headers={'User-Agent': 'Python-LASIN-DataEngine/1.0'}
    )
    
    # 2. Conectamos con el servidor remoto especificando un tiempo límite (timeout) de 10 segundos
    with urllib.request.urlopen(req, timeout=10) as respuesta:
        codigo_estado = respuesta.status
        print(f"✓ Respuesta recibida del servidor HTTP. Código de Estado: {codigo_estado}")

        # 3. Leemos los bytes recibidos y los decodificamos a cadena de texto UTF-8
        cuerpo_respuesta_texto = respuesta.read().decode("utf-8")

        # 4. Parseamos el texto JSON a una lista/diccionario nativo de Python
        datos_recibidos = json.loads(cuerpo_respuesta_texto)

    print(f"✓ Se recibieron exitosamente {len(datos_recibidos)} registros desde la API.\n")

    # 5. Análisis y filtrado de la información recibida de Internet
    print("--- ANÁLISIS DE DATOS OBTENIDOS DE LA API ---")
    # Filtramos las primeras 5 tareas que tienen el estado "completed": True
    completadas = [item for item in datos_recibidos if item.get("completed") is True][:5]

    for item in completadas:
        print(f"  • ID Registro: {item['id']:<4} | Estado: [COMPLETADO] -> Título: '{item['title']}'")

except urllib.error.URLError as err:
    # Se activa si no hay conexión a Internet o la URL es inaccesible
    print(f"❌ Error de red al conectar a la API: {err}")
except json.JSONDecodeError:
    # Se activa si la respuesta del servidor no era un formato JSON válido
    print("❌ Error: La respuesta recibida no es un formato JSON válido.")

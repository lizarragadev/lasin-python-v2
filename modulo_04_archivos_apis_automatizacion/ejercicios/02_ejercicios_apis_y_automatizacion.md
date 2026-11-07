# Ejercicios Módulo 4 — Tema 2: Consumo de APIs de Internet y Automatización de Archivos

En esta sección practicarás el consumo de servicios web HTTP JSON con `urllib.request` y la automatización de la estructura de archivos con `pathlib` y `shutil`.

---

## 📝 Ejercicio 1: Cliente API de Datos de Usuarios / Tareas

### Descripción del Problema
Escribe un script que consuma la API pública `https://jsonplaceholder.typicode.com/users`.
1. Realiza la petición HTTP GET usando `urllib.request`.
2. Convierte el JSON recibido con `json.loads()`.
3. Extrae e imprime una tabla de los primeros 5 usuarios con: `id`, `name`, `email` y `company.name`.

### Ejemplo de Salida Esperada
```text
=== USUARIOS OBTENIDOS DE LA API WEB ===
• ID 1: Leanne Graham (Email: Sincere@april.biz) | Empresa: Romaguera-Crona
• ID 2: Ervin Howell (Email: Shanna@melissa.tv) | Empresa: Deckow-Crist
• ID 3: Clementine Bauch (Email: Nathan@yesenia.net) | Empresa: Romaguera-Jacobson
========================================
```

---

## 📝 Ejercicio 2: Organizador Automático de Documentos por Extensión

### Descripción del Problema
Crea un script de automatización que escanee una carpeta llamada `descargas_temp/`, identifique los archivos por su extensión (`.txt`, `.pdf`, `.png`, `.csv`) y los mueva automáticamente a subcarpetas clasificadas (`descargas_temp/txt/`, `descargas_temp/pdf/`, etc.) usando `pathlib.Path` y `shutil.move()`.

### Ejemplo de Salida Esperada
```text
=== ORGANIZADOR AUTOMÁTICO DE ARCHIVOS ===
✓ Clasificado 'documento.txt' -> Mover a 'descargas_temp/txt/documento.txt'
✓ Clasificado 'foto.png'      -> Mover a 'descargas_temp/png/foto.png'
• Total de archivos clasificados: 2
==========================================
```

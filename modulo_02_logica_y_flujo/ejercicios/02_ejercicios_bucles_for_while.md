# Ejercicios Módulo 2 — Tema 2: Bucles (for, while) y Patrones de Lógica

En esta sección practicarás la iteración con bucles `for`, la acumulación de datos, el filtrado condicional y la validación de entradas con bucles `while`, `break` y `continue`.

---

## 📝 Ejercicio 1: Filtro de Calificaciones y Promedio de Exámenes

### Descripción del Problema
Un profesor tiene una lista de notas finales de 8 estudiantes (escala 0 a 100). Debes escribir un programa que recorra la lista con un bucle `for` y determine:
1. La suma total y el promedio general de todas las notas.
2. La cantidad de estudiantes que **Aprobaron** (Nota >= 51).
3. La cantidad de estudiantes que **Reprobaron** (Nota < 51).
4. La nota más alta (`max()`) y la más baja (`min()`).

### Ejemplo de Datos de Entrada
- `notas = [45, 82, 90, 35, 60, 51, 100, 48]`

### Salida Esperada en Consola
```text
=== ANÁLISIS DE NOTAS FINALES (BUCLE FOR) ===
• Lista de notas:             [45, 82, 90, 35, 60, 51, 100, 48]
• Total de estudiantes:       8
• Promedio General del Curso: 70.25 pts.
• Estudiantes Aprobados (>=51): 5
• Estudiantes Reprobados (<51): 3
• Nota Máxima Obtenida:       100 pts.
• Nota Mínima Obtenida:       35 pts.
==============================================
```

---

## 📝 Ejercicio 2: Validador de Contraseña con Límite de Intentos

### Descripción del Problema
Crea un sistema de autenticación por consola que solicite al usuario ingresar una contraseña secreta. El programa debe usar un bucle `while` y permitir un **máximo de 3 intentos**.
- Contraseña correcta: `"lasin2026"`
- Si ingresa la contraseña correcta, muestra un mensaje de bienvenida y rompe el bucle con `break`.
- Si ingresa una contraseña errónea, le descuenta un intento y le avisa cuántos le quedan.
- Si agota los 3 intentos sin éxito, muestra un mensaje de cuenta bloqueada.

### Ejemplo de Salida Esperada
```text
=== SISTEMA DE SEGURIDAD LASIN ===
Intento 1/3 - Ingrese contraseña: admin
❌ Contraseña incorrecta. Te quedan 2 intentos.

Intento 2/3 - Ingrese contraseña: lasin2026
🟢 Acceso concedido al sistema. ¡Bienvenido!
===================================
```

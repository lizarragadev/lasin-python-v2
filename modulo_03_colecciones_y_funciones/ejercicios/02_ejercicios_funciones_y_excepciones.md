# Ejercicios Módulo 3 — Tema 2: Funciones Reutilizables y Control de Excepciones

En esta sección practicarás la modularización mediante funciones `def`, definición de parámetros con tipo (`type hints`), retornos de datos `return` y el manejo de errores en bloques `try-except-else-finally`.

---

## 📝 Ejercicio 1: Conversor Seguro de Divisas con Captura de Errores

### Descripción del Problema
Crea una función llamada `convertir_usd_a_bob(monto_usd: float, tasa: float = 11.06) -> float` que convierta un monto de dólares a bolivianos.

Debes envolver la llamada de la función dentro de un bloque `try-except` para capturar:
1. `ValueError`: Si el usuario ingresa un texto no numérico.
2. `ZeroDivisionError` / `TypeError`: Si la tasa o el monto es un valor inválido.

### Ejemplo de Entrada y Salida
- **Entrada 1:** `monto_str = "150.50"` -> `✓ 150.50 USD equivalen a Bs. 1,664.53`
- **Entrada 2:** `monto_str = "ABC"` -> `❌ Error: 'ABC' no es un número decimal válido.`

---

## 📝 Ejercicio 2: Pipeline de Filtrado de Empleados por Rango Salarial

### Descripción del Problema
Escribe dos funciones desacopladas:
1. `filtrar_empleados_por_salario(dataset: list[dict], min_salario: float) -> list[dict]`: Retorna una lista con los empleados cuyo salario sea `>= min_salario`.
2. `generar_resumen_nomina(empleados_filtrados: list[dict]) -> dict`: Retorna un diccionario con la suma total y el promedio salarial de la lista filtrada.

### Dataset de Ejemplo
```python
nomina = [
    {"id": 1, "nombre": "Carlos Perez", "salario": 4500.0, "cargo": "Analista"},
    {"id": 2, "nombre": "Ana Morales", "salario": 8900.0, "cargo": "Gerente"},
    {"id": 3, "nombre": "Luis Torrez", "salario": 3200.0, "cargo": "Asistente"},
    {"id": 4, "nombre": "Sofia Mendoza", "salario": 12000.0, "cargo": "Director"},
]
```

### Ejemplo de Salida (Filtro Salario >= 5000 Bs)
```text
=== NOMINA DE EMPLEADOS (SALARIOS >= 5,000.00 Bs.) ===
• Empleados calificados (2 encontrados):
  - Ana Morales (Gerente): Bs. 8,900.00
  - Sofia Mendoza (Director): Bs. 12,000.00
------------------------------------------------------
• Presupuesto Total Requerido: Bs. 20,900.00
• Promedio Salarial Rango:     Bs. 10,450.00
======================================================
```

# Ejercicios Módulo 2 — Tema 1: Operadores Lógicos y Condicionales (if, elif, else, match-case)

En esta sección practicarás la evaluación de reglas de negocio utilizando condicionales `if-elif-else`, el operador ternario y la estructura `match-case`.

---

## 📝 Ejercicio 1: Evaluador de Solicitudes de Crédito Bancario

### Descripción del Problema
Un banco necesita evaluar automáticamente solicitudes de crédito personal basadas en 3 criterios de riesgo:
1. **Ingreso Mensual Mínimo:** Debe ser mayor o igual a `4,000 Bs.`
2. **Antigüedad Laboral:** Debe ser mayor o igual a `2 años`.
3. **Historial Crediticio Sin Deudas Mando:** Debe ser un valor booleano `True` (Sin deudas mora).

### Reglas de Decisión
- **Aprobado con Crédito Preferencial:** Ingreso >= 8,000 Bs, Antigüedad >= 3 años y Sin Deudas (`True`).
- **Aprobado con Crédito Estándar:** Ingreso >= 4,000 Bs, Antigüedad >= 2 años y Sin Deudas (`True`).
- **Rechazado:** Si no cumple alguno de los criterios mínimos o si tiene deudas en mora (`False`).

### Ejemplo de Entrada y Salida
- **Entrada:** `ingreso = 5500.0`, `antiguedad = 3`, `sin_deudas = True`
- **Salida esperada:**
```text
=== EVALUADOR BANCARIO DE SOLICITUD DE CRÉDITO ===
• Ingreso Mensual:          Bs. 5,500.00
• Antigüedad Laboral:       3 años
• ¿Historial Sin Deudas?:   Verdadero (True)
--------------------------------------------------
🟢 DICTAMEN: SOLICITUD APROBADA (Crédito Estándar)
==================================================
```

---

## 📝 Ejercicio 2: Clasificador de Categoría Impositiva (match-case)

### Descripción del Problema
El departamento de contabilidad de una empresa clasifica sus proveedores según un **Código de Categoría Fiscal** usando la estructura `match-case` (Python 3.10+).

### Tabla de Categorías
- `"CAT-A"`: Régimen General (Retención 13% IVA + 3% IT).
- `"CAT-B"`: Régimen Simplificado (Retención fija de 5%).
- `"CAT-C"`: Exento de Impuestos (0% Retención).
- Cualquier otro código: Categoría No Reconocida (Requiere Auditoría).

### Ejemplo de Entrada y Salida
- **Entrada:** `codigo_categoria = "CAT-A"`, `monto_factura = 10000.0`
- **Salida esperada:**
```text
=== CLASIFICACIÓN FISCAL DE PROVEEDOR (MATCH-CASE) ===
• Código Ingresado: CAT-A
• Régimen Asignado: Régimen General
• Monto Factura:    Bs. 10,000.00
• Retención (16%):  Bs. 1,600.00
• Monto Neto Pago:  Bs. 8,400.00
======================================================
```

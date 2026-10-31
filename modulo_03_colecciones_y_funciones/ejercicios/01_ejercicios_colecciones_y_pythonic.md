# Ejercicios Módulo 3 — Tema 1: Colecciones (Listas, Tuplas, Diccionarios, Sets) y Código Pythonic

En esta sección practicarás la manipulación de listas de diccionarios (datasets), eliminación de duplicados con `set()`, iteración con `enumerate()` y `zip()`, y expresiones *List Comprehension*.

---

## 📝 Ejercicio 1: Gestor de Inventario de Tienda (Dataset de Diccionarios)

### Descripción del Problema
Una tienda de tecnología maneja su inventario mediante un Dataset (lista de diccionarios). Cada producto tiene: `id`, `nombre`, `precio_bs`, `stock`, `categoria`.

Debes escribir un programa que:
1. Muestre el valor total del inventario (`suma de precio * stock`).
2. Filtre los productos que tienen **stock crítico** (menos de 5 unidades) usando una *List Comprehension*.
3. Busque un producto por su `id` y muestre sus detalles.

### Dataset de Ejemplo
```python
inventario = [
    {"id": 101, "nombre": "Teclado Mecánico", "precio_bs": 350.0, "stock": 12, "categoria": "Periféricos"},
    {"id": 102, "nombre": "Mouse Inalámbrico", "precio_bs": 120.0, "stock": 3, "categoria": "Periféricos"},
    {"id": 103, "nombre": "Monitor 24 IPS", "precio_bs": 1400.0, "stock": 2, "categoria": "Pantallas"},
    {"id": 104, "nombre": "Auriculares Gamer", "precio_bs": 280.0, "stock": 15, "categoria": "Audio"},
]
```

### Salida Esperada
```text
=== GESTOR DE INVENTARIO Y STOCK CRÍTICO ===
• Valor total del almacén: Bs. 11,560.00
• Productos con stock crítico (<5 unidades):
  - Mouse Inalámbrico (Stock: 3 u.)
  - Monitor 24 IPS (Stock: 2 u.)
============================================
```

---

## 📝 Ejercicio 2: Depurador de Lista de Clientes Duplicados (`set`, `zip`, `enumerate`)

### Descripción del Problema
Una empresa tiene dos listas paralelas de clientes capturados en dos formularios web diferentes.
- `formulario_1 = ["Juan Perez", "Maria Gomez", "Carlos Rios", "Maria Gomez"]`
- `formulario_2 = ["La Paz", "Santa Cruz", "Cochabamba", "Santa Cruz"]`

Debes:
1. Eliminar los nombres duplicados usando `set()`.
2. Iterar sobre los datos usando `enumerate()` y `zip()` para imprimir un listado unificado de clientes únicos con su ciudad sede.

### Salida Esperada
```text
=== LISTA DE CLIENTES ÚNICOS REGISTRADOS ===
  [1] Juan Perez (Sede: La Paz)
  [2] Maria Gomez (Sede: Santa Cruz)
  [3] Carlos Rios (Sede: Cochabamba)
============================================
```

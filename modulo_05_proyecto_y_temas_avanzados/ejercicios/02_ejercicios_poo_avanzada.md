# Ejercicios Módulo 5 — Tema 2: POO Avanzada (Herencia, Polimorfismo, Dataclasses y Enums)

En esta sección practicarás la definición de jerarquías de clases con herencia y polimorfismo, el uso de `@dataclass` (Python 3.7+) y la creación de constantes categóricas con `Enum`.

---

## 📝 Ejercicio 1: Sistema de Cálculo de Nómina Polimórfica

### Descripción del Problema
Crea un sistema de nómina empresarial en POO que maneje dos tipos de empleados:
1. **Superclase `Empleado`:** Atributos `nombre` y `id_emp`. Método `calcular_salario()` que lanza `NotImplementedError`.
2. **Subclase `EmpleadoTiempoCompleto`:** Atributos adicionales `salario_mensual_base`. Implementa `calcular_salario()`.
3. **Subclase `EmpleadoContratista`:** Atributos adicionales `horas_trabajadas` y `tarifa_por_hora`. Implementa `calcular_salario()`.

Itera sobre una lista polimórfica de empleados mezclados e imprime el salario final calculado de cada uno.

### Ejemplo de Salida Esperada
```text
=== SISTEMA DE NÓMINA POLIMÓRFICA ===
• Empleado Tiempo Completo: Juan Perez (ID: 101) -> Salario: Bs. 8,500.00
• Empleado Contratista: Maria Gomez (ID: 102) [120 hrs x 50.00 Bs/hr] -> Salario: Bs. 6,000.00
------------------------------------------------------
• TOTAL NOMINA A PAGAR: Bs. 14,500.00
======================================================
```

---

## 📝 Ejercicio 2: Modelado de Pedidos con Dataclasses y Enums

### Descripción del Problema
Escribe un script que utilice:
1. Un `Enum` llamado `EstadoPedido` con valores `PENDIENTE`, `EN_PROCESO`, `ENTREGADO`.
2. Un `Enum` llamado `Prioridad` con valores `BAJA`, `MEDIA`, `ALTA`.
3. Una `@dataclass` llamada `Pedido` con atributos: `id_pedido: int`, `cliente: str`, `monto_total: float`, `prioridad: Prioridad`, `estado: EstadoPedido`.

### Ejemplo de Salida Esperada
```text
=== MODELADO DE PEDIDOS CON DATACLASSES Y ENUMS ===
• Pedido ID 501 (Cliente: Comercial Alfa):
  - Monto Total:  Bs. 4,500.00
  - Prioridad:    ALTA (Prioridad Alta)
  - Estado:       PENDIENTE (Pendiente de Despacho)
===================================================
```

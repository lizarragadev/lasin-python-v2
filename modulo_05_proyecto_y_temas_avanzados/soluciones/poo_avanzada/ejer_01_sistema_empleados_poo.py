"""
==============================================================================
SOLUCIÓN — MÓDULO 5 — TEMA 2 — EJERCICIO 1: NÓMINA POLIMÓRFICA EN POO
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Superclase Empleado define el contrato abstracto calcular_salario().
2. Subclases EmpleadoTiempoCompleto y EmpleadoContratista heredan de Empleado con super().__init__().
3. Demostración de Polimorfismo recorriendo una lista unificada de empleados.
"""

print("=== SISTEMA DE NÓMINA POLIMÓRFICA ===\n")

class Empleado:
    def __init__(self, id_emp: int, nombre: str):
        self.id_emp = id_emp
        self.nombre = nombre.strip().title()

    def calcular_salario(self) -> float:
        raise NotImplementedError("Las subclases deben implementar calcular_salario().")

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, id_emp: int, nombre: str, salario_mensual_base: float):
        super().__init__(id_emp, nombre)
        self.salario_base = salario_mensual_base

    def calcular_salario(self) -> float:
        return self.salario_base

class EmpleadoContratista(Empleado):
    def __init__(self, id_emp: int, nombre: str, horas_trabajadas: float, tarifa_por_hora: float):
        super().__init__(id_emp, nombre)
        self.horas = horas_trabajadas
        self.tarifa = tarifa_por_hora

    def calcular_salario(self) -> float:
        return self.horas * self.tarifa

# Lista polimórfica de empleados
nomina_empleados: list[Empleado] = [
    EmpleadoTiempoCompleto(id_emp=101, nombre="Juan Perez", salario_mensual_base=8500.0),
    EmpleadoContratista(id_emp=102, nombre="Maria Gomez", horas_trabajadas=120.0, tarifa_por_hora=50.0),
    EmpleadoTiempoCompleto(id_emp=103, nombre="Carlos Rios", salario_mensual_base=4200.0)
]

total_nomina = 0.0

for emp in nomina_empleados:
    salario = emp.calcular_salario()
    total_nomina += salario
    print(f"• [{type(emp).__name__}] ID {emp.id_emp}: {emp.nombre:<16} -> Salario: Bs. {salario:,.2f}")

print("-" * 55)
print(f"• TOTAL NÓMINA A PAGAR CONSOLIDADO: Bs. {total_nomina:,.2f}")
print("======================================================")

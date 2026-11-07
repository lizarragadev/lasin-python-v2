"""
==============================================================================
SOLUCIÓN — MÓDULO 5 — TEMA 2 — EJERCICIO 2: DATACLASSES Y ENUMS PARA PEDIDOS
Curso: Python Nivel Básico - LASIN
==============================================================================

EXPLICACIÓN DE LA SOLUCIÓN:
1. Definimos las enumeraciones Prioridad y EstadoPedido con Enum.
2. Definimos la Dataclass Pedido con @dataclass.
"""

from dataclasses import dataclass
from enum import Enum

print("=== MODELADO DE PEDIDOS CON DATACLASSES Y ENUMS ===\n")

class Prioridad(Enum):
    BAJA = "Baja"
    MEDIA = "Media"
    ALTA = "Alta"

class EstadoPedido(Enum):
    PENDIENTE = "Pendiente de Despacho"
    EN_PROCESO = "En Preparación"
    ENTREGADO = "Entregado a Cliente"

@dataclass
class Pedido:
    id_pedido: int
    cliente: str
    monto_total: float
    prioridad: Prioridad = Prioridad.MEDIA
    estado: EstadoPedido = EstadoPedido.PENDIENTE

# Instanciación
pedido1 = Pedido(
    id_pedido=501,
    cliente="Comercial Alfa",
    monto_total=4500.00,
    prioridad=Prioridad.ALTA,
    estado=EstadoPedido.PENDIENTE
)

print(f"• Pedido ID {pedido1.id_pedido} (Cliente: {pedido1.cliente}):")
print(f"  - Monto Total:  Bs. {pedido1.monto_total:,.2f}")
print(f"  - Prioridad:    {pedido1.prioridad.name} ({pedido1.prioridad.value})")
print(f"  - Estado:       {pedido1.estado.name} ({pedido1.estado.value})")
print("===================================================")

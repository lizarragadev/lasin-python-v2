"""
==============================================================================
MÓDULO 5 — LECCIÓN 3C: POO MODERNA — DATACLASSES Y ENUMERACIONES (ENUMS)
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Enumeraciones (Enum):
   - Módulo nativo `enum` introducido para definir conjuntos de constantes nombradas.
   - Evita el uso de cadenas "mágicas" propensas a errores de tipeo (ej. usar `NivelRiesgo.ALTO`
     en lugar de escribir a mano "Alto", "alto", "ALTO").

2. Dataclasses (@dataclass):
   - Decorador nativo introducido en Python 3.7 (`from dataclasses import dataclass`).
   - Genera automáticamente métodos especiales como `__init__()`, `__repr__()` y `__eq__()`.
   - Reduce drásticamente el código repetitivo (boilerplate) al crear clases enfocadas en almacenar datos.
==============================================================================
"""

from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

print("=== POO MODERNA: DATACLASSES Y ENUMS EN PYTHON ===\n")

# ==============================================================================
# 1. ENUMERACIONES (ENUMS) PARA CONSTANTES CATEGÓRICAS
# ==============================================================================
class NivelRiesgo(Enum):
    """Enumeración de niveles de riesgo de transacciones."""
    BAJO = "Riesgo Bajo"
    MEDIO = "Riesgo Medio"
    ALTO = "Riesgo Alto (Supervisión Requerida)"
    CRITICO = "Riesgo Crítico (Bloqueado)"


class EstadoTransaccion(Enum):
    """Enumeración de estados de procesamiento."""
    PENDIENTE = "Pendiente"
    APROBADO = "Aprobado"
    RECHAZADO = "Rechazado"


# ==============================================================================
# 2. DATACLASSES PARA ALMACENAMIENTO ESTRUCTURADO DE DATOS
# ==============================================================================
# El decorador @dataclass crea automáticamente el __init__ con anotaciones de tipo (Type Hints)

@dataclass
class TransaccionData:
    """Dataclass que representa un registro comercial completo de datos."""
    id_registro: int
    empresa: str
    monto_bob: float
    ciudad: str
    riesgo: NivelRiesgo = NivelRiesgo.BAJO              # Valor por defecto usando Enum
    estado: EstadoTransaccion = EstadoTransaccion.PENDIENTE  # Valor por defecto usando Enum
    fecha: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def es_monto_elevado(self) -> bool:
        """Método dentro de una dataclass."""
        return self.monto_bob > 20000.0

    def calcular_comision(self, tasa_pct: float = 1.5) -> float:
        """Calcula la comisión de servicio sobre el monto."""
        return round(self.monto_bob * (tasa_pct / 100), 2)


# ==============================================================================
# 3. DEMOSTRACIÓN PRÁCTICA
# ==============================================================================
if __name__ == "__main__":
    print("--- 1. CREACIÓN DE REGISTROS CON DATACLASSES Y ENUMS ---")

    # Instanciamos registros usando la Dataclass (Observe cómo __init__ es generado automáticamente)
    tx1 = TransaccionData(
        id_registro=101,
        empresa="Comercial Los Andes",
        monto_bob=3500.50,
        ciudad="La Paz",
        riesgo=NivelRiesgo.BAJO,
        estado=EstadoTransaccion.APROBADO
    )

    tx2 = TransaccionData(
        id_registro=102,
        empresa="Minera Altiplano",
        monto_bob=55000.00,
        ciudad="Oruro",
        riesgo=NivelRiesgo.ALTO,
        estado=EstadoTransaccion.PENDIENTE
    )

    # Imprimir dataclass directamente muestra una representación limpia (__repr__ automático)
    print("Objeto 1 (Dataclass):", tx1)
    print("Objeto 2 (Dataclass):", tx2)

    print("\n--- 2. ACCESO A DATOS Y ENUMS ---")
    print(f"• ID Tx 1:       {tx1.id_registro}")
    print(f"• Empresa Tx 1:  {tx1.empresa}")
    print(f"• Estado Enum:   {tx1.estado.name} -> Descripción: '{tx1.estado.value}'")
    print(f"• Riesgo Enum:   {tx2.riesgo.name} -> Descripción: '{tx2.riesgo.value}'")
    print(f"• ¿Es elevado?:  {tx2.es_monto_elevado()}")
    print(f"• Comisión (1.5%): Bs. {tx1.calcular_comision()}")

    print("\n--- 3. COMPARACIÓN AUTOMÁTICA ENTRE OBJETOS DATACLASS ---")
    # Dataclass genera __eq__ automáticamente, comparando si los valores de los atributos coinciden
    tx3 = TransaccionData(id_registro=101, empresa="Comercial Los Andes", monto_bob=3500.50, ciudad="La Paz", riesgo=NivelRiesgo.BAJO, estado=EstadoTransaccion.APROBADO)
    print("¿Objeto 1 es igual al Objeto 3 en contenido?:", tx1 == tx3)

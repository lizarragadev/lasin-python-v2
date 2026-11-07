"""
==============================================================================
MÓDULO 5 — LECCIÓN 3B: POO — HERENCIA Y POLIMORFISMO
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Herencia (Inheritance):
   - Mecanismo que permite crear nuevas clases (Subclases o Clases Hijas) que heredan
     los atributos y métodos de una clase existente (Superclase o Clase Padre).
   - Reutilización de código y jerarquías claras.
   - super().__init__(...): Invoca el constructor de la clase Padre desde la subclase.

2. Polimorfismo (Polymorphism = 'Muchas Formas'):
   - Capacidad de diferentes clases de responder al MISMO nombre de método, pero
     cada una ejecutando su propia implementación específica (Sobrescritura de Métodos).
   - Permite iterar sobre una lista de objetos mixtos (ej. diferentes métodos de pago)
     y llamar a .procesar_pago() en todos ellos sin importar de qué subclase concreta son.
==============================================================================
"""

print("=== POO AVANZADO: HERENCIA Y POLIMORFISMO EN PROCESAMIENTO ===\n")

# ==============================================================================
# 1. CLASE PADRE (SUPERCLASE): MetodoPago
# ==============================================================================
class MetodoPago:
    """Clase base genérica para cualquier forma de pago."""

    def __init__(self, moneda: str = "BOB"):
        self.moneda = moneda

    def procesar_pago(self, monto: float) -> bool:
        """
        Método base que será SOBRESCRITO por cada subclase (Polimorfismo).
        Lanza una excepción si una subclase olvida implementarlo.
        """
        raise NotImplementedError("Las subclases deben implementar su propio método procesar_pago().")


# ==============================================================================
# 2. SUBCLASES HIJAS (HERENCIA Y SOBRESCRITURA DE MÉTODOS)
# ==============================================================================

# Subclase 1: Pago en Efectivo
class PagoEfectivo(MetodoPago):
    """Subclase para pagos en efectivo en caja."""

    def __init__(self, nro_caja: int, moneda: str = "BOB"):
        super().__init__(moneda)
        self.nro_caja = nro_caja

    def procesar_pago(self, monto: float) -> bool:
        """Implementación específica para Efectivo."""
        print(f"💵 [EFECTIVO]: Cobro de {self.moneda} {monto:,.2f} procesado en Caja N°{self.nro_caja}.")
        return True


# Subclase 2: Pago con Tarjeta de Crédito/Débito
class PagoTarjeta(MetodoPago):
    """Subclase para pagos procesados mediante POS / Tarjeta."""

    def __init__(self, num_tarjeta_enmascarado: str, comision_pct: float = 2.0, moneda: str = "BOB"):
        super().__init__(moneda)
        self.num_tarjeta = num_tarjeta_enmascarado
        self.comision_pct = comision_pct

    def procesar_pago(self, monto: float) -> bool:
        """Implementación específica para Tarjeta (calcula comisión de POS)."""
        comision = monto * (self.comision_pct / 100)
        monto_neto = monto - comision
        print(f"💳 [TARJETA ({self.num_tarjeta})]: Monto: {self.moneda} {monto:,.2f} | Comision POS ({self.comision_pct}%): {self.moneda} {comision:,.2f} | Neto: {self.moneda} {monto_neto:,.2f}")
        return True


# Subclase 3: Pago vía Transferencia QR / Bancaria
class PagoQR(MetodoPago):
    """Subclase para pagos mediante código QR / Transferencia bancaria rápida."""

    def __init__(self, id_transaccion_qr: str, banco_destino: str, moneda: str = "BOB"):
        super().__init__(moneda)
        self.id_qr = id_transaccion_qr
        self.banco_destino = banco_destino

    def procesar_pago(self, monto: float) -> bool:
        """Implementación específica para Transferencia QR."""
        print(f"📱 [TRANSFERENCIA QR]: Pago de {self.moneda} {monto:,.2f} acreditado instantáneamente a {self.banco_destino} (Ref QR: {self.id_qr}).")
        return True


# ==============================================================================
# 3. DEMOSTRACIÓN DE POLIMORFISMO
# ==============================================================================
if __name__ == "__main__":
    print("--- DEMOSTRACIÓN DE POLIMORFISMO ---")
    print("Procesando una lista de cobros con métodos de pago polimórficos:\n")

    # Lista heterogénea de objetos de distintas subclases
    pasarela_pagos: list[tuple[MetodoPago, float]] = [
        (PagoEfectivo(nro_caja=1), 150.0),
        (PagoTarjeta(num_tarjeta_enmascarado="****-4589", comision_pct=2.5), 1200.0),
        (PagoQR(id_transaccion_qr="QR-990412", banco_destino="Banco Nacional"), 450.50),
        (PagoEfectivo(nro_caja=2), 85.0)
    ]

    total_procesado = 0.0

    # Iteramos sobre los objetos llamando a .procesar_pago() de forma unificada
    for metodo, monto in pasarela_pagos:
        # POLIMORFISMO EN ACCIÓN: No importa cuál subclase es 'metodo', Python
        # ejecutará la versión correcta de .procesar_pago() correspondiente al objeto.
        exito = metodo.procesar_pago(monto)
        if exito:
            total_procesado += monto

    print("-" * 65)
    print(f"TOTAL COBRADO CON ÉXITO MEDIANTE PASARELA POLIMÓRFICA: Bs. {total_procesado:,.2f}")

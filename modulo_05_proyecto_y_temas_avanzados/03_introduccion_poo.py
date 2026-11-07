"""
==============================================================================
MÓDULO 5 — LECCIÓN 3: INTRODUCCIÓN A LA PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE DE POO:
1. Clase (Class):
   - Es el plano, molde o plantilla que define las propiedades (atributos) y
     comportamientos (métodos) que tendrán los objetos creados a partir de ella.

2. Objeto (Instancia):
   - Es un elemento concreto construido en la memoria RAM usando el molde de la Clase.

3. Atributos y el Método Constructor __init__(self, ...):
   - Atributos: Variables asociadas a cada objeto (ej. titular, saldo, num_cuenta).
   - __init__: Método especial que se ejecuta automáticamente al instanciar un objeto.
   - 'self': Referencia obligatoria dentro de la clase que apunta a la instancia actual.

4. Encapsulamiento y Propiedades (@property):
   - Protege los atributos internos de un objeto contra modificaciones indebidas.
   - Atributos protegidos: Se nombran con un guión bajo inicial `_saldo`.
   - `@property` (Getter) y `@property.setter` (Setter): Permiten leer y validar
     cambios en los atributos de forma controlada.
==============================================================================
"""

print("=== INTRODUCCIÓN A LA POO: CLASES, OBJETOS Y ENCAPSULAMIENTO ===\n")

# ==============================================================================
# 1. DEFINICIÓN DE LA CLASE 'CuentaBancaria'
# ==============================================================================
class CuentaBancaria:
    """Clase que representa una cuenta bancaria con saldo protegido y validaciones."""

    def __init__(self, titular: str, num_cuenta: str, saldo_inicial: float = 0.0):
        # Atributos públicos de la instancia
        self.titular = titular.strip().title()
        self.num_cuenta = num_cuenta.strip()

        # Atributo protegido (comienza con '_'): Indica que NO se debe modificar directamente desde fuera
        self._saldo = saldo_inicial if saldo_inicial >= 0 else 0.0

    # --------------------------------------------------------------------------
    # ENCAPSULAMIENTO CON PROPIEDADES (@property -> GETTER Y SETTER)
    # --------------------------------------------------------------------------
    @property
    def saldo(self) -> float:
        """GETTER: Permite consultar el saldo de forma segura como si fuera un atributo."""
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_monto: float):
        """SETTER: Valida que el nuevo saldo no sea negativo antes de asignarlo."""
        if nuevo_monto >= 0:
            self._saldo = nuevo_monto
            print(f"✓ Saldo actualizado correctamente a: Bs. {self._saldo:,.2f}")
        else:
            print("❌ ERROR: El saldo no puede ser un valor negativo.")

    # --------------------------------------------------------------------------
    # MÉTODOS DE INSTANCIA (COMPORTAMIENTO)
    # --------------------------------------------------------------------------
    def depositar(self, monto: float):
        """Incrementa el saldo si el monto ingresado es positivo."""
        if monto > 0:
            self._saldo += monto
            print(f"✓ Depósito exitoso de Bs. {monto:,.2f} en cuenta {self.num_cuenta}.")
            print(f"  -> Nuevo Saldo Disponible: Bs. {self._saldo:,.2f}")
        else:
            print("❌ Error: El monto a depositar debe ser mayor a 0 Bs.")

    def retirar(self, monto: float) -> bool:
        """Descuenta saldo si existen fondos suficientes."""
        if monto <= 0:
            print("❌ Error: El monto a retirar debe ser mayor a 0 Bs.")
            return False

        if monto <= self._saldo:
            self._saldo -= monto
            print(f"✓ Retiro exitoso de Bs. {monto:,.2f} de cuenta {self.num_cuenta}.")
            print(f"  -> Saldo Remanente: Bs. {self._saldo:,.2f}")
            return True
        else:
            print(f"❌ Fondos insuficientes en cuenta {self.num_cuenta}. Saldo actual: Bs. {self._saldo:,.2f}")
            return False

    def __str__(self) -> str:
        """Método especial para representación bonita en texto con print(objeto)."""
        return f"Cuenta {self.num_cuenta} [{self.titular}] - Saldo: Bs. {self._saldo:,.2f}"


# ==============================================================================
# 2. INSTANCIACIÓN DE OBJETOS Y PRUEBAS
# ==============================================================================
if __name__ == "__main__":
    print("--- 1. INSTANCIACIÓN DE OBJETOS Y OPERACIONES ---")

    # Creamos un objeto concreto en memoria
    cuenta_juan = CuentaBancaria(titular="Juan Perez", num_cuenta="CTA-1001", saldo_inicial=1500.0)
    
    # Invocamos __str__() implícitamente al imprimir
    print(cuenta_juan)

    # Invocación de métodos
    cuenta_juan.depositar(500.0)
    cuenta_juan.retirar(300.0)
    cuenta_juan.retirar(5000.0)  # Intento de retiro por encima del saldo

    print("\n--- 2. PRUEBA DE PROPIEDADES ENCAPSULADAS (@property) ---")
    # Lectura a través del Getter
    print(f"Saldo consultado vía Getter (@property): Bs. {cuenta_juan.saldo:,.2f}")

    # Asignación a través del Setter
    cuenta_juan.saldo = 2500.0   # Asignación válida
    cuenta_juan.saldo = -500.0   # Asignación bloqueada por validación del Setter

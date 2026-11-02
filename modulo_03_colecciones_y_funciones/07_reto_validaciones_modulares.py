"""
==============================================================================
MÓDULO 3 — LECCIÓN 7: RETO — EXTENSIÓN MODULAR DE REGLAS DE VALIDACIÓN
Curso: Python Nivel Básico - LASIN
==============================================================================

RETO INTEGRADOR DE MODULARIDAD:
- Demostrar la ventaja práctica de diseñar funciones pequeñas: Poder agregar una
  nueva regla de validación empresarial (ej. verificar si la ciudad pertenece a
  la lista de sedes autorizadas) SIN tener que reescribir ni romper las funciones
  existentes del programa.
==============================================================================
"""

def regla_validar_ciudad_autorizada(ciudad: str, sedes_permitidas: list = None) -> bool:
    """
    Regla desacoplada independiente: Retorna True si la ciudad está en la lista autorizada.
    Si no se pasa la lista de sedes, utiliza una lista por defecto de sedes troncales.
    """
    if sedes_permitidas is None:
        sedes_permitidas = ["La Paz", "Santa Cruz", "Cochabamba", "El Alto"]
    
    return ciudad.strip().title() in sedes_permitidas


def evaluar_registro_extensible(registro: dict) -> list[str]:
    """
    Función que evalúa múltiples reglas de validación sobre un registro
    acumulando cualquier fallo detectado en una lista de advertencias.
    """
    fallos_detectados = []

    # Regla 1: Monto excesivo (> 30.000 Bs)
    if registro["monto"] > 30000.0:
        fallos_detectados.append(f"Monto de Bs. {registro['monto']:,.2f} excede el límite de 30.000 Bs.")

    # Regla 2: Ciudad no autorizada (Invocamos la función independiente)
    if not regla_validar_ciudad_autorizada(registro["ciudad"]):
        fallos_detectados.append(f"Ciudad '{registro['ciudad']}' fuera de las sedes troncales autorizadas.")

    # Regla 3: Nombre de empresa sospechoso (menos de 3 caracteres)
    if len(registro["empresa"].strip()) < 3:
        fallos_detectados.append("Nombre de empresa demasiado corto o inválido.")

    return fallos_detectados


# DEMOSTRACIÓN DE EJECUCIÓN DEL RETO
if __name__ == "__main__":
    print("=== RETO: VALIDACIÓN EXTENSIBLE Y MODULAR ===\n")
    
    dataset_prueba = [
        {"empresa": "TechCorp Bolivia", "monto": 15000.0, "ciudad": "La Paz"},
        {"empresa": "GlobalTrade", "monto": 45000.0, "ciudad": "Tarija"},  # Viola Regla 1 y Regla 2
        {"empresa": "X", "monto": 500.0, "ciudad": "Santa Cruz"},          # Viola Regla 3
    ]

    for i, reg in enumerate(dataset_prueba, start=1):
        errores = evaluar_registro_extensible(reg)
        print(f"Evaluando Registro N°{i} ({reg['empresa']} - {reg['ciudad']}):")
        if errores:
            for err in errores:
                print(f"  ❌ Regla violada: {err}")
        else:
            print("  🟢 Registro 100% Válido y Autorizado")
        print("-" * 55)

"""
==============================================================================
MÓDULO 3 — LECCIÓN 6: DEMO — PROCESADOR MODULAR DE DATOS (PIPELINE)
Curso: Python Nivel Básico - LASIN
==============================================================================

ARQUITECTURA DE UN PIPELINE MODULAR DE DATOS:
  cargar_datos()  --->  limpiar_datos()  --->  analizar_datos()  --->  detectar_anomalias()  --->  mostrar_resultados()

¿POR QUÉ CONSTRUIR CÓDIGO CON ESTA ESTRUCTURA?
- En lugar de escribir un único script gigante de 200 líneas difíciles de entender,
  dividimos el problema en funciones independientes con una sola responsabilidad.
- Esto facilita la reutilización de código, las pruebas y la localización rápida de errores.
==============================================================================
"""

print("==================================================")
print("     DEMO: PROCESADOR MODULAR DE DATOS (MÓDULO 3)  ")
print("==================================================\n")


# ------------------------------------------------------------------------------
# PASO 1: CARGAR DATOS
# ------------------------------------------------------------------------------
def cargar_datos() -> list[dict]:
    """Simula la carga inicial de un dataset con datos crudos e imperfecciones."""
    return [
        {"id": 1, "empresa": "  Comercial Alfa ", "monto": "1500.50", "ciudad": "La Paz"},
        {"id": 2, "empresa": "Servicios Beta", "monto": "-200.00", "ciudad": "Santa Cruz"},
        {"id": 3, "empresa": "Tech Gamma", "monto": "INVALIDO", "ciudad": "Cochabamba"},
        {"id": 4, "empresa": "Importadora Delta", "monto": "45000.00", "ciudad": "La Paz"},
        {"id": 5, "empresa": " Alquileres Epsilon ", "monto": "350.00", "ciudad": "El Alto"},
    ]


# ------------------------------------------------------------------------------
# PASO 2: LIMPIAR Y CONVERTIR DATOS
# ------------------------------------------------------------------------------
def limpiar_datos(datos_crudos: list[dict]) -> list[dict]:
    """
    Recorre el dataset crudo, aplica .strip() y .title() a textos,
    y convierte los montos a float capturando errores con try-except.
    """
    datos_limpios = []
    
    for reg in datos_crudos:
        monto_float = None
        try:
            monto_float = float(reg["monto"])
        except ValueError:
            print(f"⚠️ Registro ID {reg['id']}: Monto '{reg['monto']}' no convertible a float. Registro ignorado.")
            continue  # Salta al siguiente registro sin añadirlo a la lista limpia

        registro_nuevo = {
            "id": reg["id"],
            "empresa": reg["empresa"].strip().title(),
            "monto": monto_float,
            "ciudad": reg["ciudad"].strip()
        }
        datos_limpios.append(registro_nuevo)
        
    return datos_limpios


# ------------------------------------------------------------------------------
# PASO 3: ANALIZAR Y CALCULAR ESTADÍSTICAS
# ------------------------------------------------------------------------------
def analizar_datos(datos_limpios: list[dict]) -> dict:
    """Calcula totales, promedios, valores máximos y mínimos sobre el dataset limpio."""
    montos_validos = [r["monto"] for r in datos_limpios if r["monto"] > 0]
    
    total = sum(montos_validos)
    cantidad = len(montos_validos)
    promedio = total / cantidad if cantidad > 0 else 0.0
    maximo = max(montos_validos) if montos_validos else 0.0
    minimo = min(montos_validos) if montos_validos else 0.0

    return {
        "total": total,
        "cantidad": cantidad,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo
    }


# ------------------------------------------------------------------------------
# PASO 4: DETECTAR ANOMALÍAS SEGÚN REGLAS
# ------------------------------------------------------------------------------
def detectar_anomalias(datos_limpios: list[dict]) -> list[tuple]:
    """Evalúa reglas de negocio (monto negativo o excesivamente alto > 20,000 Bs)."""
    anomalias = []
    for r in datos_limpios:
        if r["monto"] <= 0:
            anomalias.append((r["id"], r["empresa"], r["monto"], "Monto menor o igual a cero (Inválido)"))
        elif r["monto"] > 20000.0:
            anomalias.append((r["id"], r["empresa"], r["monto"], "Monto excesivamente alto (> 20,000 Bs.)"))
    return anomalias


# ------------------------------------------------------------------------------
# PASO 5: MOSTRAR RESULTADOS
# ------------------------------------------------------------------------------
def mostrar_resultados(stats: dict, anomalias: list[tuple]):
    """Imprime por consola el informe ejecutivo final."""
    print("\n" + "=" * 50)
    print("      RESUMEN FINAL DE EJECUCIÓN DEL PIPELINE     ")
    print("=" * 50)
    print(f"• Registros analizados exitosamente: {stats['cantidad']}")
    print(f"• Monto Total Procesado:             Bs. {stats['total']:,.2f}")
    print(f"• Promedio por transacción:          Bs. {stats['promedio']:,.2f}")
    print(f"• Monto Máximo:                      Bs. {stats['maximo']:,.2f}")
    print(f"• Monto Mínimo:                      Bs. {stats['minimo']:,.2f}")
    print("-" * 50)
    print(f"• Anomalías detectadas ({len(anomalias)} en total):")
    for id_reg, emp, monto, motivo in anomalias:
        print(f"  ❌ ID {id_reg} ({emp}): Bs. {monto:,.2f} -> Causa: {motivo}")
    print("=" * 50)


# ==============================================================================
# EJECUCIÓN DEL PIPELINE SECUENCIAL
# ==============================================================================
if __name__ == "__main__":
    crudos = cargar_datos()
    limpios = limpiar_datos(crudos)
    estadisticas = analizar_datos(limpios)
    lista_anomalias = detectar_anomalias(limpios)
    mostrar_resultados(estadisticas, lista_anomalias)

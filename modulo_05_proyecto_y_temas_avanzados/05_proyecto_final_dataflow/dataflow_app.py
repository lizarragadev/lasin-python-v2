"""
==============================================================================
                 PROYECTO FINAL: DATAFLOW v1.0
          Sistema Integrado de Procesamiento y Análisis de Datos
                 Curso Python Nivel Básico - LASIN
==============================================================================

ARQUITECTURA Y MAPEO DE CONTENIDOS DEL CURSO:
- MÓDULO 1: Variables, Constantes, Tipos Primarios, Casting y f-strings.
- MÓDULO 2: Condicionales (if-elif-else), Bucles (while/for), Contadores y Menús CLI.
- MÓDULO 3: Listas de Diccionarios (Datasets), List Comprehensions, Funciones y try-except.
- MÓDULO 4: Lectura de CSV, Persistencia en JSON y Consumo de APIs HTTP.
- MÓDULO 5: Clasificación por Nivel de Riesgo, Anomalías, PEP 8 y Buenas Prácticas.
==============================================================================
"""

import csv
import json
import os
import urllib.request
import urllib.error
from datetime import datetime

# Constantes de Configuración de Negocio (Módulo 1: PEP 8)
RUTA_CSV = "datos_ejemplo.csv"
RUTA_JSON = "reporte_dataflow.json"
UMBRAL_RIESGO_MEDIO = 5000.0
UMBRAL_RIESGO_ALTO = 20000.0


# ==============================================================================
# 1. MÓDULO DE CARGA Y LECTURA DE ARCHIVOS TABULARES (CSV)
# ==============================================================================
def cargar_dataset_csv(ruta: str) -> list[dict]:
    """
    Lee los registros de un archivo CSV usando csv.DictReader y convierte
    el campo 'monto' a float capturando errores de conversión con try-except.
    """
    dataset = []
    if not os.path.exists(ruta):
        print(f"⚠️ Archivo '{ruta}' no encontrado. Se iniciará con dataset vacío.")
        return dataset

    # Módulo 4: Gestor de contexto 'with open' para lectura segura
    with open(ruta, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, fila in enumerate(reader, start=1):
            # Módulo 3: Control de Excepciones para montos defectuosos
            try:
                monto = float(fila["monto"])
            except ValueError:
                monto = 0.0
                print(f"⚠️ Fila {idx}: Monto no numérico en '{fila.get('empresa')}'. Asignado 0.0 Bs.")

            # Módulo 3: Diccionario que representa la fila cargada
            registro = {
                "id": int(fila["id"]) if fila.get("id") else idx,
                "empresa": fila["empresa"].strip(),
                "monto": monto,
                "ciudad": fila["ciudad"].strip()
            }
            dataset.append(registro)

    return dataset


# ==============================================================================
# 2. MÓDULO DE CLASIFICACIÓN DE RIESGO Y ANOMALÍAS (RETO FINAL DE CURSO)
# ==============================================================================
def clasificar_nivel_riesgo(monto: float) -> str:
    """
    RETO FINAL: Evalúa el monto y retorna la categoría de riesgo del registro.
    - Riesgo Bajo:  <= 5,000 Bs.
    - Riesgo Medio: 5,000 a 20,000 Bs.
    - Riesgo Alto:  > 20,000 Bs.
    """
    if monto <= 0:
        return "INVÁLIDO / ANOMALÍA"
    elif monto <= UMBRAL_RIESGO_MEDIO:
        return "BAJO"
    elif monto <= UMBRAL_RIESGO_ALTO:
        return "MEDIO"
    else:
        return "ALTO"


def procesar_y_enriquecer_dataset(dataset: list[dict]) -> list[dict]:
    """
    Recorre el dataset e incorpora las nuevas claves 'nivel_riesgo' y 'es_anomalia'
    a cada registro en memoria.
    """
    dataset_procesado = []
    for reg in dataset:
        riesgo = clasificar_nivel_riesgo(reg["monto"])
        # Regla de anomalía: Monto no válido (<= 0) o atípicamente elevado (> 50,000 Bs)
        es_anomalia = (reg["monto"] <= 0) or (reg["monto"] > 50000.0)

        reg_nuevo = reg.copy()
        reg_nuevo["nivel_riesgo"] = riesgo
        reg_nuevo["es_anomalia"] = es_anomalia
        dataset_procesado.append(reg_nuevo)

    return dataset_procesado


# ==============================================================================
# 3. MÓDULO DE ANÁLISIS ESTADÍSTICO DE DATOS
# ==============================================================================
def calcular_estadisticas(dataset: list[dict]) -> dict:
    """
    Utiliza List Comprehensions y funciones nativas sum(), len(), min(), max()
    para generar el resumen cuantitativo del dataset.
    """
    # Módulo 3: List Comprehension para filtrar solo montos positivos válidos
    validos = [r["monto"] for r in dataset if r["monto"] > 0]
    total = sum(validos)
    cantidad = len(validos)
    promedio = total / cantidad if cantidad > 0 else 0.0

    # Contador de registros por nivel de riesgo
    contadores_riesgo = {"BAJO": 0, "MEDIO": 0, "ALTO": 0, "INVÁLIDO / ANOMALÍA": 0}
    for r in dataset:
        r_nivel = r.get("nivel_riesgo", "BAJO")
        contadores_riesgo[r_nivel] = contadores_riesgo.get(r_nivel, 0) + 1

    return {
        "total": total,
        "cantidad": cantidad,
        "promedio": promedio,
        "maximo": max(validos) if validos else 0.0,
        "minimo": min(validos) if validos else 0.0,
        "distribucion_riesgo": contadores_riesgo
    }


# ==============================================================================
# 4. MÓDULO DE CONSUMO DE API EXTERNA EN INTERNET
# ==============================================================================
def verificar_conexion_api() -> str:
    """Módulo 4: Realiza una solicitud HTTP GET de prueba a una API pública para verificar estado."""
    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        req = urllib.request.Request(url, headers={'User-Agent': 'DataFlow/1.0'})
        with urllib.request.urlopen(req, timeout=4) as res:
            if res.status == 200:
                return "ONLINE (API Conectada)"
    except Exception:
        pass
    return "OFFLINE (Modo Local)"


# ==============================================================================
# 5. MÓDULO DE PERSISTENCIA EN ARCHIVO JSON
# ==============================================================================
def guardar_reporte_json(dataset: list[dict], stats: dict, ruta_salida: str):
    """Módulo 4: Serializa el informe consolidado y lo escribe en un archivo .json físico."""
    reporte = {
        "aplicacion": "DataFlow LASIN Core",
        "fecha_generacion": datetime.now().isoformat(),
        "estadisticas_generales": stats,
        "registros_analizados": dataset
    }
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=4, ensure_ascii=False)
    print(f"✓ Reporte consolidado guardado exitosamente en: {ruta_salida}")


# ==============================================================================
# 6. INTERFAZ DE CONSOLA INTERACTIVA (MENÚ CLI PRINCIPAL)
# ==============================================================================
def ejecutar_dataflow():
    print("==================================================")
    print("    DATAFLOW v1.0 — PROCESADOR DE DATOS (LASIN)   ")
    print("==================================================\n")

    estado_red = verificar_conexion_api()
    print(f"Estado del Sistema: [{estado_red}]")
    print("Cargando dataset inicial desde CSV...")

    dataset_crudo = cargar_dataset_csv(RUTA_CSV)
    dataset_actual = procesar_y_enriquecer_dataset(dataset_crudo)
    print(f"✓ {len(dataset_actual)} registros procesados y listos para análisis.\n")

    ejecutando = True

    # Módulo 2: Bucle interactivo while
    while ejecutando:
        print("\n" + "=" * 50)
        print("                MENÚ DE OPERACIONES               ")
        print("=" * 50)
        print("1. Ver tabla completa de registros y niveles de riesgo")
        print("2. Mostrar estadísticas generales (Total, Promedio)")
        print("3. Filtrar registros de ALTO RIESGO (> 20.000 Bs.)")
        print("4. Ver anomalías detectadas en el sistema")
        print("5. Guardar reporte consolidado en archivo JSON")
        print("6. Salir de la aplicación")
        print("=" * 50)

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            print("\n--- 📊 DATASET PROCESADO ---")
            print(f"{'ID':<6} | {'EMPRESA':<22} | {'MONTO (BS)':<12} | {'RIESGO':<8} | {'ANOMALÍA'}")
            print("-" * 65)
            for r in dataset_actual:
                anom_str = "❌ SÍ" if r["es_anomalia"] else "🟢 NO"
                print(f"{r['id']:<6} | {r['empresa']:<22} | Bs. {r['monto']:<9,.2f} | {r['nivel_riesgo']:<8} | {anom_str}")

        elif opcion == "2":
            stats = calcular_estadisticas(dataset_actual)
            print("\n--- 📈 ESTADÍSTICAS DEL DATASET ---")
            print(f"• Registros válidos:   {stats['cantidad']}")
            print(f"• Monto Total:         Bs. {stats['total']:,.2f}")
            print(f"• Promedio:            Bs. {stats['promedio']:,.2f}")
            print(f"• Valor Máximo:        Bs. {stats['maximo']:,.2f}")
            print(f"• Valor Mínimo:        Bs. {stats['minimo']:,.2f}")
            print("\nDistribución por Nivel de Riesgo:")
            for nivel, cant in stats["distribucion_riesgo"].items():
                print(f"  - Riesgo {nivel}: {cant} registros")

        elif opcion == "3":
            print("\n--- 🔴 REGISTROS DE ALTO RIESGO (> 20,000 Bs.) ---")
            altos = [r for r in dataset_actual if r["nivel_riesgo"] == "ALTO"]
            if altos:
                for r in altos:
                    print(f"  • ID {r['id']} - {r['empresa']} ({r['ciudad']}): Bs. {r['monto']:,.2f}")
            else:
                print("  ✓ No se encontraron registros de alto riesgo.")

        elif opcion == "4":
            print("\n--- ⚠️ REGISTROS ANÓMALOS ---")
            anomalias = [r for r in dataset_actual if r["es_anomalia"]]
            if anomalias:
                for r in anomalias:
                    print(f"  • ID {r['id']} - {r['empresa']}: Bs. {r['monto']:,.2f} (Datos atípicos/defectuosos)")
            else:
                print("  ✓ No se detectaron anomalías.")

        elif opcion == "5":
            stats = calcular_estadisticas(dataset_actual)
            guardar_reporte_json(dataset_actual, stats, RUTA_JSON)

        elif opcion == "6":
            print("\n👋 ¡Gracias por utilizar DataFlow! Cerrando aplicación...")
            ejecutando = False

        else:
            print("❌ Opción inválida. Ingrese un número del 1 al 6.")


# Módulo 4: Cláusula de ejecución principal
if __name__ == "__main__":
    ejecutar_dataflow()

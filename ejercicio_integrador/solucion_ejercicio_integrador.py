"""
========================================================================================
LOGIFLOW — SISTEMA DE ENVÍOS LOGÍSTICOS Y AUDITORÍA
Solución Oficial del Ejercicio Práctico Integrador (LASIN - Curso Python Básico)
========================================================================================
Integra los conceptos esenciales vistos en el curso:
 - Módulo 1: Tipos de datos, operadores matemáticos y f-strings tabulares.
 - Módulo 2: Lógica condicional (if-elif-else) y bucles de iteración.
 - Módulo 3: Conjuntos (set), listas, diccionarios, comprensiones, funciones y try-except.
 - Módulo 4: Lectura de archivos CSV, exportación JSON y consumo de API web con fallback.
 - Módulo 5: Introducción a POO (clases tradicionales) y persistencia relacional con SQLite.
========================================================================================
"""

import csv
import json
import sqlite3
import urllib.request
import urllib.error
import os


# --------------------------------------------------------------------------------------
# 1. MODELADO CON POO BÁSICA (Módulo 5: Clase tradicional con __init__ y métodos)
# --------------------------------------------------------------------------------------

class Envio:
    """Clase que representa un envío logístico individual con validaciones básicas."""

    def __init__(self, id_envio: str, cliente: str, peso_kg: float, costo_base: float, tipo: str):
        # Validación de integridad física de los datos con excepciones (Módulos 3 y 5)
        if peso_kg <= 0:
            raise ValueError(f"El peso debe ser mayor a 0 kg (recibido: {peso_kg})")
        if costo_base < 0:
            raise ValueError(f"El costo base no puede ser negativo (recibido: {costo_base})")

        self.id_envio = id_envio.strip()
        self.cliente = cliente.strip()
        self.peso_kg = float(peso_kg)
        self.costo_base = float(costo_base)
        self.tipo = tipo.strip().upper()

    def calcular_costo_final(self) -> float:
        """Aplica recargos comerciales según el tipo de envío (Módulo 2)."""
        if self.tipo == "EXPRESS":
            return round(self.costo_base * 1.20, 2)
        elif self.tipo == "REFRIGERADO":
            return round(self.costo_base * 1.35, 2)
        else:
            return round(self.costo_base, 2)

    def a_diccionario(self) -> dict:
        """Convierte los datos del envío a formato de diccionario (Módulo 3 y 4)."""
        return {
            "id_envio": self.id_envio,
            "cliente": self.cliente,
            "peso_kg": self.peso_kg,
            "tipo": self.tipo,
            "costo_final_usd": self.calcular_costo_final()
        }


# --------------------------------------------------------------------------------------
# 2. CONSUMO DE API EXTERNA (Módulo 4: urllib + json)
# --------------------------------------------------------------------------------------

def obtener_tipo_cambio() -> float:
    """Consulta la tasa USD/BOB desde API web con respaldo por defecto ante fallas."""
    url = "https://open.er-api.com/v6/latest/USD"
    tasa_defecto = 6.96

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "LASIN-Python/1.0"})
        with urllib.request.urlopen(req, timeout=4) as resp:
            if resp.status == 200:
                datos = json.loads(resp.read().decode("utf-8"))
                tasa = float(datos.get("rates", {}).get("BOB", tasa_defecto))
                print(f"[API] Tasa obtenida en línea: 1 USD = {tasa:.2f} BOB")
                return tasa
    except (urllib.error.URLError, TimeoutError, Exception) as error:
        print(f"[API] Conexión no disponible ({error}). Usando tasa de contingencia: 1 USD = {tasa_defecto:.2f} BOB")

    return tasa_defecto


# --------------------------------------------------------------------------------------
# 3. INGESTA Y LIMPIEZA DE DATOS (Módulo 3 y 4: CSV, Set, Try-Except)
# --------------------------------------------------------------------------------------

def cargar_envios(ruta_csv: str) -> list[Envio]:
    """Lee el CSV, deduplica con set y descarta filas con errores usando try-except."""
    if not os.path.exists(ruta_csv):
        print(f"[ERROR] No existe el archivo: {ruta_csv}")
        return []

    envios: list[Envio] = []
    ids_vistos: set[str] = set()

    with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            id_envio = fila.get("id_envio", "").strip()

            # Deduplicación con conjunto (set)
            if id_envio in ids_vistos:
                print(f"[AVISO] Omitido por duplicado: {id_envio}")
                continue

            # Validación y captura de datos erróneos con try-except
            try:
                nuevo = Envio(
                    id_envio=id_envio,
                    cliente=fila.get("cliente", ""),
                    peso_kg=float(fila.get("peso_kg", 0)),
                    costo_base=float(fila.get("costo_base", 0)),
                    tipo=fila.get("tipo", "ESTANDAR")
                )
                ids_vistos.add(id_envio)
                envios.append(nuevo)
            except (ValueError, KeyError) as err:
                print(f"[AVISO] Fila descartada ({id_envio}): {err}")

    return envios


# --------------------------------------------------------------------------------------
# 4. PERSISTENCIA EN SQLITE (Módulo 5: sqlite3)
# --------------------------------------------------------------------------------------

def guardar_en_sqlite(envios: list[Envio], tasa: float, ruta_db: str) -> int:
    """Guarda los envíos válidos en SQLite mediante sentencias parametrizadas seguras."""
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS envios (
            id TEXT PRIMARY KEY,
            cliente TEXT NOT NULL,
            tipo TEXT NOT NULL,
            peso_kg REAL NOT NULL,
            costo_usd REAL NOT NULL,
            costo_bob REAL NOT NULL
        )
    """)

    # Comprensión de listas (Módulo 3)
    registros = [
        (
            e.id_envio,
            e.cliente,
            e.tipo,
            e.peso_kg,
            e.calcular_costo_final(),
            round(e.calcular_costo_final() * tasa, 2)
        )
        for e in envios
    ]

    cursor.executemany("INSERT OR REPLACE INTO envios VALUES (?, ?, ?, ?, ?, ?)", registros)
    conexion.commit()
    conexion.close()
    return len(registros)


# --------------------------------------------------------------------------------------
# 5. EXPORTACIÓN DE AUDITORÍA A JSON (Módulo 4: json.dump)
# --------------------------------------------------------------------------------------

def exportar_resumen_json(envios: list[Envio], tasa: float, ruta_json: str) -> None:
    """Exporta un reporte estructurado en formato JSON con métricas consolidadas."""
    total_usd = sum(e.calcular_costo_final() for e in envios)
    total_bob = round(total_usd * tasa, 2)

    resumen = {
        "sistema": "LogiFlow LASIN",
        "total_envios": len(envios),
        "tasa_usd_bob": tasa,
        "total_usd": round(total_usd, 2),
        "total_bob": total_bob,
        "envios": [e.a_diccionario() for e in envios]
    }

    with open(ruta_json, mode="w", encoding="utf-8") as archivo:
        json.dump(resumen, archivo, indent=4, ensure_ascii=False)


# --------------------------------------------------------------------------------------
# 6. REPORTE EN CONSOLA CON F-STRINGS (Módulo 1: Formato tabular)
# --------------------------------------------------------------------------------------

def mostrar_reporte(envios: list[Envio], tasa: float) -> None:
    """Imprime una tabla formateada y los totales del lote."""
    ancho = 72
    print("\n" + "=" * ancho)
    print(f"{'ID':<10} {'CLIENTE':<22} {'TIPO':<14} {'USD':>10} {'BOB':>18}")
    print("-" * ancho)

    total_usd = sum(e.calcular_costo_final() for e in envios)
    total_bob = total_usd * tasa

    for e in envios:
        c_usd = e.calcular_costo_final()
        c_bob = c_usd * tasa
        txt_usd = f"$ {c_usd:>8,.2f}"
        txt_bob = f"Bs. {c_bob:>10,.2f}"
        print(f"{e.id_envio:<10} {e.cliente:<22} {e.tipo:<14} {txt_usd}  {txt_bob}")

    print("-" * ancho)
    print(f"TOTAL: {len(envios)} envíos válidos | $ {total_usd:,.2f} USD | Bs. {total_bob:,.2f} BOB")
    print("=" * ancho + "\n")


# --------------------------------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# --------------------------------------------------------------------------------------

def main() -> None:
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(directorio_actual, "datos_envios.csv")
    ruta_db = os.path.join(directorio_actual, "envios.db")
    ruta_json = os.path.join(directorio_actual, "resumen_auditoria.json")

    print("=== SISTEMA DE ENVÍOS Y AUDITORÍA LOGIFLOW ===")
    tasa = obtener_tipo_cambio()
    envios = cargar_envios(ruta_csv)

    if envios:
        mostrar_reporte(envios, tasa)
        guardados = guardar_en_sqlite(envios, tasa, ruta_db)
        print(f"✓ {guardados} registros guardados en SQLite ('{os.path.basename(ruta_db)}').")

        exportar_resumen_json(envios, tasa, ruta_json)
        print(f"✓ Resumen consolidado exportado a JSON ('{os.path.basename(ruta_json)}').\n")


if __name__ == "__main__":
    main()

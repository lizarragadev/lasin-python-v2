"""
==============================================================================
MÓDULO 4 — LECCIÓN 6: MODULARIZACIÓN PROPIA Y PAQUETES (pip Y venv)
Curso: Python Nivel Básico - LASIN
==============================================================================

CONCEPTOS CLAVE:
1. Módulos Propios:
   - Un archivo .py puede ser importado desde otros archivos usando la palabra clave 'import'.
   - Permite reutilizar funciones de cálculo o validación en múltiples proyectos.

2. La Cláusula if __name__ == "__main__":
   - Variable especial '__name__':
     * Si corres el archivo DIRECTAMENTE (python mi_script.py), __name__ vale "__main__".
     * Si el archivo es IMPORTADO desde otro script, __name__ vale el nombre del archivo.
   - Colocar el código de prueba dentro de 'if __name__ == "__main__":' evita que
     las pruebas se ejecuten cuando alguien importa tu archivo como módulo.

3. Entornos Virtuales (venv) y Administrador de Paquetes (pip):
   - pip: Herramienta de comandos para descargar e instalar librerías externas de PyPI (ej. pandas, requests).
   - venv: Entorno aislado para que cada proyecto tenga sus propias versiones de paquetes.
==============================================================================
"""

from datetime import datetime

print("=== MODULARIZACIÓN Y PAQUETES DE PYTHON ===\n")

# ==============================================================================
# 1. FUNCIONES REUTILIZABLES DEL MÓDULO
# ==============================================================================

def obtener_timestamp_actual() -> str:
    """Devuelve la fecha y hora actual en formato estándar YYYY-MM-DD HH:MM:SS."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calcular_porcentaje_participacion(parte: float, total: float) -> float:
    """Calcula el porcentaje de representación de una parte sobre un total."""
    if total <= 0:
        return 0.0
    return round((parte / total) * 100, 2)


# ==============================================================================
# 2. BLOQUE DE PRUEBA EXCLUSIVO (if __name__ == "__main__")
# ==============================================================================
if __name__ == "__main__":
    print("--- PRUEBA DE EJECUCIÓN DIRECTA DEL MÓDULO ---")
    print("Fecha y hora actual:", obtener_timestamp_actual())
    print("Porcentaje de 250 sobre 1000:", calcular_porcentaje_participacion(250, 1000), "%")
    
    print("\n" + "=" * 55)
    print("       GUÍA DE COMANDOS PARA PIP Y VENV (ENTORNOS)   ")
    print("=" * 55)
    print("1. Crear un entorno virtual aislado en la carpeta 'venv':")
    print("   python -m venv venv")
    print("\n2. Activar el entorno virtual:")
    print("   • En Mac / Linux:   source venv/bin/activate")
    print("   • En Windows (CMD): venv\\Scripts\\activate.bat")
    print("\n3. Instalar paquetes externos mediante pip:")
    print("   pip install requests pandas matplotlib")
    print("=" * 55)

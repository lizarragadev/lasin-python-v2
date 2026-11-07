"""
==============================================================================
MÓDULO 4 — LECCIÓN 5: DEMO INTRODUCTIVA — FLUKO DE OCR Y PROCESAMIENTO DE DOCUMENTOS
Curso: Python Nivel Básico - LASIN
==============================================================================

¿QUÉ ES OCR (OPTICAL CHARACTER RECOGNITION)?
- Reconocimiento Óptico de Caracteres: Tecnología que escanea una imagen o PDF
  y extrae el texto contenido en ella.

ARQUITECTURA DE UN SISTEMA DE PROCESAMIENTO DE DOCUMENTOS:
  1. Documento Físico / Escaneado (Imagen PNG / PDF)
        ↓
  2. Motor OCR (ej. Tesseract OCR, EasyOCR, Amazon Textract)
        ↓
  3. Texto Plano (String crudo con saltos de línea e imperfecciones)
        ↓
  4. Extracción con Python (Regex / Parseo de Cadenas)
        ↓
  5. Datos Estructurados (Diccionario / JSON)
        ↓
  6. Análisis de Negocio / Guardado en Base de Datos

NOTA DIDÁCTICA: Esta lección muestra cómo Python toma el texto ruidoso entregado
por un motor OCR y usa Expresiones Regulares (re) para extraer campos clave.
==============================================================================
"""

import re  # Módulo nativo 're' para Expresiones Regulares (búsqueda avanzada de patrones de texto)

print("=== DEMO INTRODUCTIVA: OCR Y PROCESAMIENTO DE DOCUMENTOS ===\n")

# 1. TEXTO PLANO CRUDO ENTREGADO SIMULADAMENTE POR UN MOTOR OCR AL ESCANEAR UN RECIBO
texto_ocr_bruto = """
========================================
       SUPERMERCADO LOS ANDES S.A.
       NIT: 1020304050 - LA PAZ
========================================
FECHA: 18/09/2026 14:30
NRO FACTURA: 0045892

PRODUCTOS COMPRADOS:
- LECHE ENTERA 1L ........ Bs.  7.50
- PAN INTEGRAL ........... Bs. 12.00
- ACEITE VEGETAL 1L ...... Bs. 16.50
- CAFE MOLIDO 250G ....... Bs. 28.00

TOTAL A PAGAR: Bs. 64.00
GRACIAS POR SU COMPRA!
========================================
"""

print("1. Texto sin formato extraído del recibo escaneado por el motor OCR:")
print("-" * 45)
print(texto_ocr_bruto.strip())
print("-" * 45)


# ------------------------------------------------------------------------------
# 2. FUNCIÓN DE EXTRACCIÓN Y PARSEO DE CAMPOS CLAVE CON EXPRESSIONES REGULARES
# ------------------------------------------------------------------------------
def parsear_texto_recibo(texto: str) -> dict:
    """
    Utiliza patrones de Expresiones Regulares (re.search) para extraer
    automáticamente: Fecha, Nro de Factura y Total a pagar del texto OCR.
    """
    
    # Extraemos la razón social (Primera línea limpia del texto)
    lineas = [l.strip() for l in texto.split("\n") if l.strip()]
    empresa = lineas[0].replace("=", "").strip()

    # Patron para fecha: \\d{2}/\\d{2}/\\d{4} busca 2 dígitos / 2 dígitos / 4 dígitos (ej: 18/09/2026)
    coincidencia_fecha = re.search(r"\d{2}/\d{2}/\d{4}", texto)
    fecha = coincidencia_fecha.group(0) if coincidencia_fecha else "No encontrada"

    # Patron para Nro de Factura: Busca 'NRO FACTURA:' seguido de dígitos \\d+
    coincidencia_factura = re.search(r"NRO FACTURA:\s*(\d+)", texto)
    factura = coincidencia_factura.group(1) if coincidencia_factura else "N/A"

    # Patron para Total: Busca 'TOTAL A PAGAR: Bs.' seguido de un número decimal
    coincidencia_total = re.search(r"TOTAL A PAGAR:\s*Bs\.\s*([\d\.]+)", texto)
    total_monto = float(coincidencia_total.group(1)) if coincidencia_total else 0.0

    # Retornamos los datos limpios estructurados como un Diccionario
    return {
        "empresa": empresa,
        "fecha": fecha,
        "nro_factura": factura,
        "total_bs": total_monto,
        "moneda": "BOB"
    }


# ------------------------------------------------------------------------------
# 3. RESULTADO DEL PROCESAMIENTO
# ------------------------------------------------------------------------------
datos_recibo = parsear_texto_recibo(texto_ocr_bruto)

print("\n2. Registro estructurado obtenido por Python a partir del texto OCR:")
print(datos_recibo)

print("\n3. Resumen listo para ser guardado en la Base de Datos:")
print(f"• Empresa Emisora:   {datos_recibo['empresa']}")
print(f"• N° Factura:        {datos_recibo['nro_factura']}")
print(f"• Fecha de Emisión:  {datos_recibo['fecha']}")
print(f"• Monto Contabilizado: Bs. {datos_recibo['total_bs']:.2f}")

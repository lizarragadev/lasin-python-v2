# Proyecto Final — DataFlow (Procesador y Analizador de Datos)

**DataFlow** es el proyecto transversal integrador del curso **Python Nivel Básico (LASIN)**. 

---

## 🎯 Funcionalidades Integradas
1. **Carga y Lectura:** Lectura automatizada desde archivos CSV (`datos_ejemplo.csv`) y persistencia en JSON.
2. **Validación y Limpieza:** Conversión de tipos con manejo de excepciones `try-except` e identificación de montos defectuosos.
3. **Análisis Estadístico:** Cálculo de totales acumulados, promedios, valores máximos y mínimos.
4. **Clasificación por Nivel de Riesgo (Reto Final):**
   - 🟢 **Riesgo Bajo:** Monto $\le 5,000$ Bs.
   - 🟡 **Riesgo Medio:** $5,000$ Bs. $<$ Monto $\le 20,000$ Bs.
   - 🔴 **Riesgo Alto:** Monto $> 20,000$ Bs.
5. **Consumo de APIs de Internet:** Verificación de estado de conexión o sincronización de tipo de cambio.
6. **Persistencia del Estado:** Guardado y recuperación del reporte consolidado en archivos JSON.

---

## 🚀 Cómo ejecutar la aplicación

```bash
cd modulo_05_proyecto_y_temas_avanzados/05_proyecto_final_dataflow
python dataflow_app.py
```

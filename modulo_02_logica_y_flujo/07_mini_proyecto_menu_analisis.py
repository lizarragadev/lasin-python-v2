"""
==============================================================================
MÓDULO 2 — LECCIÓN 7: MINI PROYECTO — SISTEMA INTERACTIVO CON MENÚ CLI
Curso: Python Nivel Básico - LASIN
==============================================================================

OBJETIVO DIDÁCTICO DEL MINI PROYECTO:
- Consolidar todo el Módulo 2 integrando un bucle principal `while ejecutando:`
  que mantiene la aplicación activa, un menú desplegable con opciones (1-6),
  estructuras `if-elif-else` para dirigir cada opción, iteraciones `for` para buscar
  y filtrar datos, y condicionales para detectar anomalías.
==============================================================================
"""

print("==================================================")
print("  MINI PROYECTO: SISTEMA INTERACTIVO DE ANÁLISIS  ")
print("==================================================\n")

# Dataset básico de montos de transacciones registrado en el sistema
datos_ventas = [150.0, 320.0, 450.50, 1200.0, 85.0, 9500.0, 210.0, -45.0, 3500.0]

ejecutando = True

# Bucle principal que mantiene la consola interactiva encendida hasta elegir la opción 6
while ejecutando:
    print("\n" + "=" * 45)
    print("           MENÚ PRINCIPAL DE OPCIONES        ")
    print("=" * 45)
    print("1. Ver datos registrados")
    print("2. Calcular estadísticas (Total, Promedio, Max, Min)")
    print("3. Buscar un monto en el sistema")
    print("4. Filtrar ventas superiores a un monto")
    print("5. Detectar anomalías por reglas")
    print("6. Salir del sistema")
    print("=" * 45)

    opcion = input("Seleccione una opción (1-6): ").strip()

    if opcion == "1":
        print("\n--- 📊 1. LISTA DE DATOS REGISTRADOS ---")
        for idx, monto in enumerate(datos_ventas, start=1):
            print(f"  [{idx}] Monto: Bs. {monto:,.2f}")

    elif opcion == "2":
        print("\n--- 📈 2. ESTADÍSTICAS BÁSICAS ---")
        # List comprehension para filtrar montos positivos válidos
        validos = [m for m in datos_ventas if m > 0]
        total = sum(validos)
        prom = total / len(validos) if validos else 0
        
        print(f"• Registros válidos:            {len(validos)}")
        print(f"• Suma total acumulada:         Bs. {total:,.2f}")
        print(f"• Promedio general:             Bs. {prom:,.2f}")
        print(f"• Venta máxima (max()):         Bs. {max(validos):,.2f}")
        print(f"• Venta mínima (min()):         Bs. {min(validos):,.2f}")

    elif opcion == "3":
        print("\n--- 🔍 3. BÚSQUEDA DE MONTO EN SISTEMA ---")
        busqueda_str = input("Ingrese el monto a buscar (Bs.): ").strip()
        busqueda = float(busqueda_str) if busqueda_str.replace('.', '', 1).isdigit() else 0.0
        encontrado = False
        
        for idx, monto in enumerate(datos_ventas, start=1):
            if monto == busqueda:
                print(f"✓ Monto de Bs. {busqueda:.2f} encontrado en el registro [{idx}].")
                encontrado = True
                break
        
        if not encontrado:
            print(f"❌ El monto de Bs. {busqueda:.2f} no existe en el dataset.")

    elif opcion == "4":
        print("\n--- 🎯 4. FILTRAR INFORMACIÓN ---")
        corte_str = input("Mostrar ventas mayores a (Bs.): ").strip()
        corte = float(corte_str) if corte_str.replace('.', '', 1).isdigit() else 0.0
        filtrados = [m for m in datos_ventas if m > corte]
        
        print(f"Ventas mayores a Bs. {corte:.2f} ({len(filtrados)} encontradas):")
        for m in filtrados:
            print(f"  -> Bs. {m:,.2f}")

    elif opcion == "5":
        print("\n--- ⚠️ 5. DETECCIÓN DE ANOMALÍAS ---")
        anomalias = []
        for idx, m in enumerate(datos_ventas, start=1):
            if m <= 0:
                anomalias.append((idx, m, "Monto menor o igual a cero (Inválido)"))
            elif m > 5000.0:
                anomalias.append((idx, m, "Monto atípicamente alto (> 5,000.00 Bs.)"))
        
        if anomalias:
            print(f"Se encontraron {len(anomalias)} registros anómalos:")
            for pos, val, motivo in anomalias:
                print(f"  • Posición [{pos}]: Bs. {val:,.2f} -> Causa: {motivo}")
        else:
            print("✓ No se detectaron anomalías en el dataset.")

    elif opcion == "6":
        print("\n👋 Saliendo del sistema de análisis interactivo. ¡Hasta luego!")
        ejecutando = False  # Rompe el bucle while principal

    else:
        print("\n❌ Opción no válida. Por favor elija un número del 1 al 6.")

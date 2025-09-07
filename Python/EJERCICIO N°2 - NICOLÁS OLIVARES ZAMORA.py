# EJERCICIO2
entradas = 50
#contador = 0
resta = None
while True:
    print("\n***** Cine Estrella *****")
    print("Bienvenido al sistema de venta de entradas del Cine Estrella")
    print("1. Ver cuantas entradas quedan")
    print("2. Comprar una cantidad de entradas")
    print("3. Devolver entradas")
    print("4. Salir del sistema")

    op = input("Selecciona una opcción (1-4): ")

    try:
        if op == '1':
            print(f"Entradas disponibles {entradas}")
            continue
            #print(f"Entradas disponibles: {NvsEntradas}")
        elif op == '2':
            if entradas == 50:
                compra = int(input("Cuantas entradas deseas comprar: "))
                NvsEntradas = entradas - compra
                print(f"Gracias por comprar una entrada, quedan {NvsEntradas} disponibles")
                continue
            elif compra > 50:
                    print("No puedes comprar más de 50 entradas...")
            else:
                print("No quedan entradas disponibles")
                break
        elif op == '3':
            devolver = int(input("¿Cuantas entradas desea devolver?: "))
            NvsEntradas2 = NvsEntradas + devolver
            print(f"Se han devuelto {devolver}. Total disponible: {NvsEntradas2}")
            continue
        elif op == '4':
            print("Gracias por usar el sistema de ventas del Cine Estrella. ¡Hasta pronto!...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
    except:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4. ")
        continue

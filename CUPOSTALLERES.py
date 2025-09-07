cuposTallerProgramacion = 10
cuposTallerBaseDeDatos = 10
cuposTallerCostura = 10

while True:
    print("Menu de taller")
    print("1. Taller de programación")
    print("2. Taller de base de datos")    
    print("3. Taller de costura")
    print("4. Ver todos los cupos disponibles")
    print("5. Salir")

    opcion = int(input("INgresa una opción (1-5): "))

    #Si presiono 1
    if opcion == 1:
        while True:
            print("Taller de programación")
            print("1. Inscribirse al taller")
            print("2. Volver al menú principal")
            subOpcion = int(input("Seleccione una opción (1-2): "))
            if subOpcion == 1:
                if cuposTallerProgramacion > 0:
                    cuposTallerProgramacion -= 1
                    print("Inscripción con exito")
                else:
                    print("No quedan cupos del taller de programación.")
                    break
            elif subOpcion == 2:
                break
    elif opcion == 2:
        while True:
            print("Taller de base de datos")
            print("1. Inscribirse al taller")            
            print("2. Volver al menú principal")
            subOpcion2 = int(input("Seleccione una opción (1-2): "))
            if subOpcion2 == 1:
                if cuposTallerBaseDeDatos > 0:
                    cuposTallerBaseDeDatos -= 1
                    print("Inscripción en el taller de base de datos con éxito.")
                else:
                    print("No quedan cupos disponibles.")
                    break
            elif subOpcion2 == 2:
                break
    elif opcion == 3:
        while True:
            print("TALLER DE COSTURA")
            print("1. Inscribirse al taller")
            print("2. Volver al menú principal")
            subOpcion3 = int(input("SELECCIONE UNA OPCIÓN (1-2): "))
            if subOpcion3 == 1:
                if cuposTallerCostura > 0:
                    cuposTallerCostura -= 1
                    print("Inscripción en el taller de costura con éxito.")
                else:
                    print("NO QUEDAN CUPOS DISPONIBLES")
                    break
            elif subOpcion3 == 2:
                break
    if opcion == 4:
        totalCupos = cuposTallerCostura + cuposTallerBaseDeDatos + cuposTallerProgramacion
        print(f"Este es el número acutal de cupos disponibles: {totalCupos}")   
    elif opcion == 5:
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
        continue
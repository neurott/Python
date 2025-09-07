
# Ejercicio de inscripción a talleres
cupos_taller_programacion = 10
cupos_taller_base_de_datos = 10
cupos_taller_costura = 10

while True:
    print("\n--- Menú de Talleres ---")
    print("1. Taller de programación")
    print("2. Taller de base de datos")
    print("3. Taller de costura")
    print("4. Ver cupos disponibles")
    print("5. Salir")
    opcion = int(input("Selecciona una opción (1-5): "))

    # Menú para Taller de Programación
    if opcion == 1:
        while True:
            print("\n--- Taller de programación ---")
            print("1. Inscribirse")
            print("2. Volver al menú principal")
            subOpcion = input("Selecciona una opción (1-2): ")
            if subOpcion == "1":
                if cupos_taller_programacion > 0:
                    cupos_taller_programacion -= 1
                    print("¡Inscripción exitosa en Taller de programación! Cupos restantes:", cupos_taller_programacion)
                    break
                else:
                    print("No quedan cupos en Taller de programación.")
            elif subOpcion == "2":
                break
            else:
                print("Opción no válida.")
    
    # Menú para Taller de Base de Datos
    elif opcion == 2:
        while True:
            print("\n--- Taller de base de datos ---")
            print("1. Inscribirse")
            print("2. Volver al menú principal")
            subOpcion = input("Selecciona una opción (1-2): ")
            if subOpcion == "1":
                if cupos_taller_base_de_datos > 0:
                    cupos_taller_base_de_datos -= 1
                    print("¡Inscripción exitosa en Taller de base de datos! Cupos restantes:", cupos_taller_base_de_datos)
                else:
                    print("No quedan cupos en Taller de base de datos.")
            elif subOpcion == "2":
                break
            else:
                print("Opción no válida.")

    # Menú para Taller de Costura
    elif opcion == 3:
        while True:
            print("\n--- Taller de costura ---")
            print("1. Inscribirse")
            print("2. Volver al menú principal")
            subOpcion = input("Selecciona una opción (1-2): ")
            if subOpcion == "1":
                if cupos_taller_costura > 0:
                    cupos_taller_costura -= 1
                    print("¡Inscripción exitosa en Taller de costura! Cupos restantes:", cupos_taller_costura)
                else:
                    print("No quedan cupos en Taller de costura.")
            elif subOpcion == "2":
                break
            else:
                print("Opción no válida.")

    elif opcion == 4:
        print("\nCupos disponibles:")
        print("Taller de programación:", cupos_taller_programacion)
        print("Taller de base de datos:", cupos_taller_base_de_datos)
        print("Taller de costura:", cupos_taller_costura)

    elif opcion == 5:
        print("¡Gracias por usar el sistema de inscripción de talleres!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")


# Ejercicio de inscripción a talleres con match-case
cupos_taller_programacion = 10
cupos_taller_base_de_datos = 10
cupos_taller_costura = 10

while True:
    print("\n--- Menú de Talleres ---")
    print("1. Taller de programación ")
    print("2. Taller de base de datos ")
    print("3. Taller de costura ")
    print("4. Ver cupos disponibles")
    print("5. Salir")

   
    opcion = int(input("Selecciona una opción (1-5): "))


    match opcion:
        case 1:
            while True:
                print("\n--- Taller de programación ---")
                print("1. Inscribirse")
                print("2. Volver al menú principal")
                subopcion = input("Selecciona una opción (1-2): ")
                match subopcion:
                    case "1":
                        if cupos_taller_programacion > 0:
                            cupos_taller_programacion -= 1
                            print("¡Inscripción exitosa en Taller de programación! Cupos restantes:", cupos_taller_programacion)
                        else:
                            print("No quedan cupos en Taller de programación.")
                    case "2":
                        break
                    case _:
                        print("Opción no válida.")
        case 2:
            while True:
                print("\n--- Taller de base de datos ---")
                print("1. Inscribirse")
                print("2. Volver al menú principal")
                subopcion = input("Selecciona una opción (1-2): ")
                match subopcion:
                    case "1":
                        if cupos_taller_base_de_datos > 0:
                            cupos_taller_base_de_datos -= 1
                            print("¡Inscripción exitosa en Taller de base de datos! Cupos restantes:", cupos_taller_base_de_datos)
                        else:
                            print("No quedan cupos en Taller de base de datos.")
                    case "2":
                        break
                    case _:
                        print("Opción no válida.")
        case 3:
            while True:
                print("\n--- Taller de costura ---")
                print("1. Inscribirse")
                print("2. Volver al menú principal")
                subopcion = input("Selecciona una opción (1-2): ")
                match subopcion:
                    case "1":
                        if cupos_taller_costura > 0:
                            cupos_taller_costura -= 1
                            print("¡Inscripción exitosa en Taller de costura! Cupos restantes:", cupos_taller_costura)
                        else:
                            print("No quedan cupos en Taller de costura.")
                    case "2":
                        break
                    case _:
                        print("Opción no válida.")
        case 4:
            print("\nCupos disponibles:")
            print("Taller de programación:", cupos_taller_programacion)
            print("Taller de base de datos:", cupos_taller_base_de_datos)
            print("Taller de costura:", cupos_taller_costura)
        case 5:
            print("¡Gracias por usar el sistema de inscripción de talleres!")
            break
        case _:
            print("Opción no válida. Intente nuevamente.")

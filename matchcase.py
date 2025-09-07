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
                print("\nTaller de programación")
                print("1. Inscribirse")
                print("2. Volver al menú principal")
                subopcion = input("Seleccione una opción (1-2): ")
                match subopcion:
                    case "1":
                        if cupos_taller_programacion > 0:
                            cupos_taller_programacion -= 1
                            print(F"Inscripción con éxito!!! CUPOS RESTANTES: {cupos_taller_programacion}")
                        else:
                            print("No quedan cupos para este taller!")
                    case "2":
                        break
                    case _:
                        print("Opción no válida.")
        case 2:
            while True:            
                print("\nTaller de base de datos")
                print("1. Inscribirse")
                print("2. Volver al menú principal")
                subopcion = input("Seleccione una opción (1-2): ")
                match subopcion:
                    case "1":
                        if cupos_taller_base_de_datos > 0:
                            cupos_taller_base_de_datos -= 1
                            print(f"Inscripción con éxito!!! CUPOS RESTANTES: {cupos_taller_base_de_datos}")
                        else:
                            print("No quedan cupos para este taller!")
                    case "2":
                        break
                    case _:
                        print("Opción no válida.")

        case 3:
            while True:            
                print("\nTaller de costura")
                print("1. Inscribirse")
                print("2. Volver al menú principal")
                subopcion = input("Seleccione una opción (1-2): ")
                match subopcion:
                    case "1":
                        if cupos_taller_costura > 0:
                            cupos_taller_costura -= 1
                            print(f"Inscripción con éxito!!! CUPOS RESTANTES: {cupos_taller_costura}")
                        else:
                            print("No quedan cupos para este taller!")
                    case "2":
                        break
                    case _:
                        print("Opción no válida.")

        case 4:
            print("\nCUPOS DISPONIBLES: ")
            print(f"TALLER DE PROGRAMACIÓN: {cupos_taller_programacion}")
            print(f"TALLER DE BASE DE DATOS: {cupos_taller_base_de_datos}")
            print(f"TALLER DE COSTURA: {cupos_taller_costura}")
        case 5:
            print("Gracias por usar el sistema de inscripción de talleres.")
            break
        case _:
            print("OPCIÓN NO VÁLIDA. INTENTA NUEVAMENTE...")
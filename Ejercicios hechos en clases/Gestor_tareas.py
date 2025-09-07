tareas = {}

while True:
    print("\n ---- Menú de tareas ----")
    print("1. Agregar tarea")
    print("2. Mostrar tereas")
    print("3. Salir")

    opcion = input("Escoja una opción (1-3): ")

    if opcion == "1":
        nombre_tarea = input("Ingrese el nombre de la tarea: ")
        estado_tarea = input("Ingrese el estado de la tarea: ")

        if estado_tarea not in ["completada", "pendiente"]:
            print("Estado no válido. Debe ser 'completada' o 'pendiente'")
        else:
            tareas[nombre_tarea] = estado_tarea
            print("Tarea agregada correctamente.")
                                
    elif opcion == "2":
        if tareas:
            print("\nLista de tareas: ")
            for nombre_tarea, estado_tarea in tareas.items():
                print(f"{nombre_tarea} - Estado: {estado_tarea}")
        else:
            print("No hay tareas guardadas.")

    elif opcion == "3":
        print("¡hasta pronto!")
        break
    
    else:
        print("Opción no válida. Intente de nuevo")
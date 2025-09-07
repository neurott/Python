tareas = []

while True:
    print("\nMenú")
    print("1. Agregar tareas")
    print("2. Ver tareas")
    print("3. Eliminar tareas ")
    print("4. Salir")

    try:
        op = int(input("Seleccione una opción (1-4): "))
    except:
        print("Error")

    if op == 1:
        tarea = input("Ingrese una nueva tarea: ")
        if tarea:
            tareas.append(tarea)
            print("Tarea agregada con éxito...")
        else:
            print("No se puede agregar una tarea vacía¿")
    
    elif op == 2:
        if not tareas:
            print("No hay tareas en la lista.")
        else:
            print("\nLista de tareas:")
            for i in range(len(tareas)):
                print(f"{i + 1}. {tareas[i]}")

    elif op == 3:
        if not tareas:
            print("No hay tareas para eliminar.")
        else:
            print("\nLista de tareas")
            for i in range(len(tareas)):
                print(f"{i + 1}. {tareas[i]}")
            try:
                num = int(input("Ingresa el número de la tarea a eliminar: "))
                if 1 <= num <= len(tareas):
                    TareaEliminada = tareas.pop(num - 1)
                    print(f'Tarea "{TareaEliminada}" eliminada.')
                else:
                    print("Número inválido.")
            except ValueError:
                print("Debes ingresar un número válido.")
    
    elif op == 4:
        print("Saliendo...")
        break

    else:
        print("OPCIÓN INVÁLIDA...")
    
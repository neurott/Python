def mostrar_menu():
    print("\n--- MENÚ DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar_tarea(tareas):
    tarea = input("Escribe la nueva tarea: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def ver_tareas(tareas):
    contador = 0
    if tareas:
        print("\nLista de tareas:")
        for tarea in tareas:
            contador += 1
            print(f"\n {contador} {tarea}")
    else:
        print("No hay tareas registradas.")

def eliminar_tarea(tareas):
    ver_tareas(tareas)
    if tareas:
        try:
            num = int(input("Número de tarea a eliminar: "))
            if 1 <= num <= len(tareas):
                eliminada = tareas.pop(num - 1)
                print(f"Tarea '{eliminada}' eliminada.")
            else:
                print("Número fuera de rango.")
        except:
            print("Entrada inválida. Debe ser un número.")
# Programa principal
tareas = []
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_tarea(tareas)
    elif opcion == "2":
        ver_tareas(tareas)
    elif opcion == "3":
        eliminar_tarea(tareas)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
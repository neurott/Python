def mostrar_menu():
    print("Menú de tareas")
    print("1. Agregar tareas")
    print("2. Ver tareas")
    print("3. Eliminar tareas")
    print("4. Salir")

def agregar_tareas(tareas):
    tarea = input("Ingrese la tarea que desea agregar: ")
    tareas.append(tareas)
    print(f"Se ha agregado la tarea {tarea}")

def ver_tareas(tareas):
#    print(tareas)
    if tareas:
        print("Lista de tareas: ")
        for tarea in tareas:
            contador += 1
            print(f"Tarea {contador} {tarea}")

def eliminar_tarea(tareas):
    ver_tareas(tareas) #llamo una función para ver las tareas
    if tareas:
        try:
            num = int(input("Número de tarea a eliminar: "))
            if 1 <= num >= len(tareas):
                eliminada = tareas.pop(num - 1)
                print(f"Tarea {eliminada} eliminada.")
            else:
                print("Tarea no existe")
        except:
            print("OPCIÓN INVÁLIDA. Debe ser un número")

tareas = []

while True:
    mostrar_menu()
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        agregar_tareas(tareas)
    elif opcion == 2:
        ver_tareas(tareas)
    elif opcion == 3:
        eliminar_tarea(tareas)
    elif opcion == 4:
        print("Adíos")
        break
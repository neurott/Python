def mostrar_menu():
    print("\nMenú de tareas")
    print("1. Agregar tareas")
    print("2. Ver tareas")
    print("3. Eliminar tareas")
    print("4. Eliminar tareas 2")
    print("5. Salir")

def agregar_tarea(tarea):
    tarea = input("Ingrese la tarea que desea agregar: ").strip().capitalize()
    tareas.append(tarea)
    print(f"Se agregó la tarea: {tarea}")

def ver_tareas(tarea):
    contador = 0
    if tarea:
        print("\nLista de tareas: ")
        for i in tareas:
            contador += 1
            print(f"{contador}. {i}")

def eliminar_tarea(tarea):
    ver_tareas(tarea)
    if tareas:
        try:
            n = int(input("\nNúmero de tarea a eliminar"))
            if 1 <= n <= len(tareas):
                eliminar = tareas.pop(n - 1)
                print(f"Tarea {eliminar} eliminada")
            else:
                print(f"Tarea no existe")
            
        except:
            print("ERROR: Opción no válida. Debe ser un número.")

def eliminar_tarea2(tarea):
    ver_tareas(tarea)
    if tarea:
        eliminada = input("Ingrese la tarea que deseas eliminar: ").strip().capitalize()
        if eliminada in tarea:
            tarea.remove(eliminada)
            print(f"Se eliminó la tarea: {eliminada} de la lista")
        else:
            print("No existe")

tareas = [] 

def main():
    while True:
        mostrar_menu()
        op = int(input("Seleccione una opción (1-5): "))

        if op == 1:
            agregar_tarea(tareas)
        elif op == 2:
            ver_tareas(tareas)
        elif op == 3:
            eliminar_tarea(tareas)
        elif op == 4:
            eliminar_tarea2(tareas)
        elif op == 5:
            print("Saliendo.....")
            break
        else:
            print("ERROR")

main()
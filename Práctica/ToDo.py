def menu():
    print("\nMenú de tareas")
    print("1. Agregar tareas")
    print("2. Ver tareas")
    print("3. Eliminar tareas")
    print("4. Eliminar tareas 2")
    print("5. Salir")

def agregar_tarea(tarea):
        tarea = input("Ingrese la tarea que desea agregar: ").strip().upper()
        tareas.append(tarea)
        print(f"Se agregó la tarea: {tarea} con éxito.")

def ver_tareas(tarea):
    contador = 0
    if tarea:
        print("-"*20)
        print("Lista de tareas:")
        for t in tareas:
            contador += 1
            print(f"{contador}. {t}")

def eliminar_tarea(tarea):
    ver_tareas(tarea)
    if tareas:
        try:
            n = int(input("\nNúmero de tarea a eliminar: "))
            if 1 <= n <= len(tareas):
                eliminar = tareas.pop(n - 1)
                print(f"Tarea {eliminar} eliminada.")
            else:
                print(f"Tarea no existe")
        except:
            print("ERROR: OPCIÓN NO VÁLIDA. DEBE SER UN NÚMERO.")

def eliminar_tarea2(tarea):
    ver_tareas(tarea)
    if tarea:
        eliminada = input("Ingresa la tarea que deseas eliminar: ").strip().upper()
        if eliminada in tarea:
            tarea.remove(eliminada)
            print(f"Se eliminó la tarea: {eliminada} de la lista")
        else:
            print("No existe...")
            
tareas = []

def main():
    while True:
        menu()
        opcion = int(input("Seleccione una opción (1-5): "))
      
        if opcion == 1:
            agregar_tarea(tareas)
        elif opcion == 2:
            ver_tareas(tareas)
        elif opcion == 3:
            eliminar_tarea(tareas)
        elif opcion == 4:
            eliminar_tarea2(tareas)
        elif opcion == 5:
            print("Saliendo....")
            break
        else:
            print("Error: Ingresó un número fuera del rango o escribió un string")

main()

#crear un programa que permita a un usuario gestionar tareas (TO DO)
#menu de opcione
#1 Agregar una nueva tarea
#2 Visualizar todas las tareas
#3 Eliminar una tarea
#4 Salir

#pop
#for
#append
tareas = []
def mostrar_menu():
    print("1. Agregar una nueva tarea ")
    print("2. Visualizar todas las tareas")
    print("3. Eliminar una tarea")
    print("4. Salir")

    op = int(input("Seleccione una opción (1-4): "))
    if op == 1:
        tarea = input("Ingrese la tarea a agregar: ")
        tareas.append(tarea)
        print(f"Se añadió: {tarea} con éxito")
    elif op == 2:
        print(tareas)
    elif op == 3:
        tareas.pop

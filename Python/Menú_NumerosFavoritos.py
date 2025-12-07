#CREAR UN MENÜ DONDE PUEDA GUARDAR MIS NÚMEROS FAVORITOS EN UNA LISTA
#EL MENÚ DEBE
#1 AGREGAR UN NÚMERO FAVORITO
#2 MOSTRAR TODOS LOS NÚMEROS
#3 mOSTRAR LA CANTIDAD DE NÚMEROS GUARDADOS
#4 vACIAR LA LISTA DE  NÚMEROS
#5 Salir
milista = []
while True:
    print("\nMenú...")
    print("1. Agregar un número favorito")
    print("2. Mostrar todos los números")
    print("3. Mostrar la cantidad de números guardados")
    print("4. Vaciar la lista de números")
    print("5. Salir")
    try:
        op = int(input("Seleccione una opción (1-5): "))
    except ValueError:
        print("Número inválido.")
    try:
        if op == 1:
            print("Ingrese el número que desea agregar a la lista: ")
            num = int(input())
            milista.append(num)
            print(f"\nSe agregó el número: {num}")
        elif op == 2:
            if len(milista) <= 0:
                print("\nTu lista esta vacía")       
            else:
                print(f"\nLISTA NUMEROS FAVORITOS: {milista}")
        elif op == 3:
            print(f"\nLa cantidad de números es {len(milista)}")
        elif op == 4:
            milista.clear()
            print("\nLista eliminada")
        elif op == 5:
            break
    except ValueError:
        print("Inválido")
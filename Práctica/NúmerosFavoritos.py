numeros_favoritos = []

while True:
    print("\nNúmeros favoritos")
    print("1. Agregar un número favorito")
    print("2. Mostrar todos los números favoritos")
    print("3. Mostrar la cantidad de números guardados")
    print("4. Vaciar la lista de números.")
    print("5. Salir")

    op = int(input("Seleccione una opción (1-5): "))

    if op == 1:
        num = int(input("\n INgresa el número que deseas agregar: "))
        numeros_favoritos.append(num)
        print(f"Se agregó el número: {num} con éxito a la lista")
    elif op == 2:
        print(f"\nLista de tus números favoritos: {numeros_favoritos}")
    elif op == 3:
        print(f"Tienes en total: {len(numeros_favoritos)}")
    elif op == 4:
        numeros_favoritos.clear()
        print("\nLista vaciada")
    elif op == 5:
        print("Saliendo del programa....")
        break
    else:
        print("Error: Opción inválida")
        
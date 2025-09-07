nums_favoritos = []

while True:
    print("\nMENÚ DE NÚMEROS FAVORITOS..")
    print("1. Agregar un número favorito..")
    print("2. Mostrar todos los números favoritos.")
    print("3. Mostrar la cantidad de números guardados")
    print("4. Vaciar la lista de números")
    print("5. Salir")

    op = int(input("\nElige una opción: "))

    if op == 1:
        try:
            num = int(input("\nIngresa un número para agregarlo a la lista: "))
            nums_favoritos.append(num)
            print(f"\n¡Número agregado!: {num}")
        except:
            print("\nDebes ingresar un número entero.")
    elif op == 2:
        print(f"\nTus números favoritos son: {nums_favoritos}")
    elif op == 3:
        print("\nTienes", len(nums_favoritos), "número(s) guardado(s)")
    elif op == 4:
        nums_favoritos.clear()
        print("\nLista vaciada")
    elif op == 5:
        break
    else:
        print("\nOpción inválida.")
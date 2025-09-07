numeros_favoritos = []

while True:
    print("\n--- Menú Números Favoritos ---")
    print("1. Agregar un número favorito")
    print("2. Mostrar todos los números favoritos")
    print("3. Mostrar la cantidad de números guardados")
    print("4. Vaciar la lista de números")
    print("5. Salir")
    opcion = input("\nElige una opción: ")

    if opcion == "1":
        try:
            numero = int(input("\nIngresa un número para agregar: "))
            numeros_favoritos.append(numero)
            print("\n¡Número agregado!")
        except:
            print("\nDebes ingresar un número entero.")
    elif opcion == "2":
        print("\nTus números favoritos son:", numeros_favoritos)
    elif opcion == "3":
        print("\nTienes", len(numeros_favoritos), "número(s) guardado(s).")
    elif opcion == "4":
        numeros_favoritos.clear()
        print("\nLista vaciada.")
    elif opcion == "5":
        print("\n¡Hasta luego!")
        break
    else:
        print("\nOpción inválida.")

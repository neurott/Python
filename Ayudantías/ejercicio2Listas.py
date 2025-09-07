canciones = []

while True:
    print("\n--- Menú Canciones Favoritas ---")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Mostrar todas las canciones")
    print("4. Salir")
    opcion = input("\nElige una opción: ")

    if opcion == "1":
        nombre = input("\nNombre de la canción para agregar: ")
        canciones.append(nombre)
        print("\n¡Canción agregada!")
    elif opcion == "2":
            if not canciones:
                print("No hay canciones en la lista.")
            else:
                print("Tus canciones favoritas:")
                contador = 1
                for i in range(len(canciones)):
                    print(str(contador) + ". " + canciones[i]+".mp3")
                    contador += 1

                try:
                    pos = int(input("¿Qué número de canción quieres eliminar? (0 para no eliminar ninguna): "))
                    if pos == 0:
                        print("No se eliminó ninguna canción.")
                    elif 1 <= pos <= len(canciones):
                        eliminada = canciones.pop(pos-1)
                        print(f"¡Canción '{eliminada}' eliminada!")
                    else:
                        print("Número fuera de rango.")
                except:
                    print("Debes ingresar un número válido.")
    elif opcion == "3":
        print("\nTus canciones favoritas:")
        for cancion in canciones:
            print(cancion+".mp3")
        if not canciones:
            print("\n(Lista vacía)")
    elif opcion == "4":
        print("\n¡Hasta luego!")
        break
    else:
        print("\nOpción inválida.")

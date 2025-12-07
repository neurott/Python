# Diccionario vacío para almacenar los Pokémon
pokedex = {}

while True:
    print("\n---- Menú de Pokédex ----")
    print("1. Agregar Pokémon")
    print("2. Mostrar Pokémon")
    print("3. Buscar Pokémon")
    print("4. Salir")

    opcion = input("Escoja una opción (1-4): ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del Pokémon: ")
            tipo = input("Ingrese el tipo del Pokémon (por ejemplo: Fuego, Agua, Eléctrico, Metal, Tenebroso): ")
            nivel = input("Ingrese el nivel del Pokémon: ")

            
            # Agregar el Pokémon al diccionario
            pokedex[nombre] = {
                'tipo': tipo,
                'nivel': int(nivel)
            }
            print(f"Pokémon {nombre} agregado correctamente.")

        case "2":
            if pokedex:
                print("\nLista de Pokémon registrados:")
                for nombre, datos in pokedex.items():
                    print(f"{nombre} - Tipo: {datos['tipo']} - Nivel: {datos['nivel']}")
            else:
                print("No hay Pokémon registrados en la Pokédex.")

        case "3":
            nombre_buscar = input("Ingrese el nombre del Pokémon a buscar: ")
            if nombre_buscar in pokedex:
                datos = pokedex[nombre_buscar]
                print(f"{nombre_buscar} - Tipo: {datos['tipo']} - Nivel: {datos['nivel']}")
            else:
                print(f"El Pokémon {nombre_buscar} no está registrado en la Pokédex.")

        case "4":
            print("¡Hasta luego!")
            break

        case _:
            print("Opción no válida. Intente de nuevo.")

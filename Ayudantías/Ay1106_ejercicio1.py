#Diccionario vacío para los contactos
contactos = {}  # Creamos un diccionario donde guardaremos los contactos: clave=nombre, valor=teléfono

while True:  # Bucle principal, se repite hasta que el usuario decida salir
    print("\n--- Menú de Contactos ---")  # Imprime un título para el menú
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Salir")
    opcion = input("Elige una opción: ")  # Solicita al usuario elegir una opción

    if opcion == "1":  # Si la opción es 1, agregamos un contacto
        nombre = input("Nombre del contacto: ")  # Pide el nombre
        telefono = input("Teléfono: ")           # Pide el teléfono
        contactos[nombre] = telefono             # Lo guarda en el diccionario diccionario[clave] = valor de existir clave, actualiza su valor
        print("Contacto agregado exitosamente.")

    elif opcion == "2":  # Si la opción es 3, mostramos todos los contactos
        if contactos:                    # Si el diccionario está vacío
            print("\nLista de contactos:")   # Imprime cada contacto con su teléfono
            for nombre, telefono in contactos.items():
                print(f"{nombre}: {telefono}")
        else:
            print("No hay contactos guardados.")

    elif opcion == "3":  # Si la opción es 4, salimos del programa
        print("¡Hasta luego!")
        break  # Sale del bucle while y termina el programa

    else:
        print("Opción no válida. Intenta de nuevo.")  # Si la opción no es válida, avisa al usuario
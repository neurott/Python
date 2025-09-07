inventario = {}  # Creamos el diccionario para el inventario, clave=nombre producto, valor=diccionario con precio y cantidad

while True:  # Bucle principal
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Vender producto")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":  # Agregar producto
        nombre = input("Nombre del producto: ").lower()    # Nombre del producto
        if nombre in inventario:                      # Verifica si ya existe
            print("El producto ya existe.")
        else:
            precio = float(input("Precio del producto: "))    # Pide precio y lo convierte a float
            cantidad = int(input("Cantidad disponible: "))    # Pide cantidad y la convierte a entero
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}  # Guarda los datos como un diccionario interno
            print("Producto agregado.")

    elif opcion == "2":  # Mostrar inventario
        if inventario: #si tiene claves
            print("\nInventario de productos:")
            print(inventario)
            for producto, datos in inventario.items():  # datos es el diccionario interno
                print(f"{producto} - Precio: ${datos['precio']} - Cantidad: {datos['cantidad']}")
        else: # Si está vacío
            print("No hay productos en el inventario.")

    elif opcion == "3":  # Vender producto
        nombre = input("Nombre del producto a vender: ").lower()
        if nombre in inventario:
            cantidad_vender = int(input("¿Cuántos quieres vender?: "))
            if cantidad_vender <= inventario[nombre]["cantidad"]:  # Hay suficiente stock
                inventario[nombre]["cantidad"] -= cantidad_vender  # Descuenta el stock
                print(f"Venta realizada. Quedan {inventario[nombre]['cantidad']} unidades de {nombre}.")
                if inventario[nombre]["cantidad"] == 0:
                    print("¡Producto agotado!")
            else:
                print("No hay suficiente stock para esa venta.")
        else:
            print("El producto no existe.")

    elif opcion == "4":  # Salir
        print("¡Hasta luego!")
        break  # Termina el programa

    else:
        print("Opción no válida. Intenta de nuevo.")  # Si la opción no existe, avisa
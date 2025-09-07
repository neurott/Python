#Ejercicio 2: Sistema de Inventario de Productos
#Enunciado:
#Crea un programa en Python que permita gestionar un inventario de productos. El programa debe permitir al usuario:
#Agregar producto: Pide el nombre del producto, su precio y la cantidad disponible. Si el producto ya existe en el inventario,
#muestra un mensaje informando de ello. Guarda los datos en un diccionario donde cada clave es el nombre del producto y
#el valor es otro diccionario con las claves "precio" y "cantidad".
#Mostrar inventario: Muestra todos los productos en el inventario junto con su precio y cantidad disponible. 
#Si no hay productos, muestra un mensaje adecuado.
#Vender producto: Solicita el nombre del producto y la cantidad que se desea vender. 
#Verifica si el producto existe y si hay suficiente stock. Si es así, descuenta la cantidad vendida.
#Si no hay suficiente, muestra un mensaje de advertencia. 
#Si al vender se agota el stock, muestra un mensaje informando que el producto está agotado.
#Salir: Termina el programa.
#El programa debe repetirse continuamente hasta que el usuario elija salir. También debe validar que las opciones seleccionadas sean válidas.
inventario = {}

while True:
    print("\nSistema de Inventario de Productos")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Vender producto")
    print("4. Salir")
    op = int(input("Seleccione una opción (1-4): "))

    if op == 1:
        nombre = input("El nombre del producto: ").lower()
        if nombre in inventario:
            print("Ya existe el producto..")
        else:
            precio = int(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            inventario[nombre] = {"Precio": precio, "Cantidad": cantidad}
            print("Producto agregado...")
    elif op == 2:
        if inventario:
            print("Inventario: ")
            for producto, datos in inventario.items():
                print(f"{producto} - Precio ${precio} - Cantidad{datos['cantidad']}")
        else:
            print("No hay datos en el inventario.")
    elif op == 3:
        nombre = input("Ingrese el nombre del producto: ").lower()
        if nombre in inventario:
            cantidad_vendida = int(input("¿Cuantos productos quiere llevar?: "))
            if cantidad_vendida <= inventario[nombre]["cantidad"]:
                inventario[nombre]['cantidad'] -= cantidad_vendida
                print("Venta realizada")
            else:
                print("No hay suficientes producots")
    elif op == 4:
        print("Saliendo...")
        break
    else:
        print("Ingrese un valor valido")


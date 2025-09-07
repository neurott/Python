productos = ["Arroz", "Aceite", "Azucar"]
precios = [1000, 2500, 1500]
carritos = []

while True:
    print("\n1. Ver productos disponibles")
    print("2. Agregar productos al carrito")
    print("3. Eliminar productos")
    print("4. Ver el total de su lista.")
    print("5. Salir")
    op = int(input("Seleccione una opción (1-5): "))

    if op == 1: # usa for
        print(f"\nLISTA DE PRODUCTOS DISPONIBLES: ")
        print(f"1. {productos[0]} - ${precios[0]}")
        print(f"2. {productos[1]} - ${precios[1]}")
        print(f"3. {productos[2]} - ${precios[2]}")
    elif op == 2:
        agregar = input("QUE PRODUCTOS DESEA AGREGAR AL CARRITO: ")
        carritos.append(agregar)
        print(f"Se agregaron los siguientes productos al carrito: {carritos}")
    elif op == 3:
        print()
    elif op == 4:
        break
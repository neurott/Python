precioPikachu = 4500
PrecioOtaku = 5000
PrecioPulpo = 5200
PrecioAnguila = 4800

cantidadPikachu = 0
CantidadOtaku = 0
CantidadPulpo = 0
CantidadAnguila = 0

while True:
    opcion = int(input("Seleccione 6 para salir o cualquier otro número para seguir: "))
    if opcion == 6:
        print("Saliendo..")
        break
    while True:
        print("\Seleccione el roll de sushi que dese agregar a su pedido:")
        print("1. Pikachu Roll - $4500")
        print("2. Otaku Roll - $5000")
        print("3. Pulpo Venenoso Roll - $5200")
        print("4. Anguila Eléctrica Roll - $4800")
        print("5. Salir del pedido") 

        try:
            op = int(input("Ingrese la opción (1-5): "))

            if op == 1:
                cantidadPikachu += 1
            elif op == 2:
                CantidadOtaku += 1
            elif op == 3:
                CantidadPulpo += 1       
            elif op == 4:
                CantidadAnguila += 1
            elif op == 5:
                print("Saliendo del pedido...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 5")
                continue
            continuar = input("Dese agregar otro roll? si/no: ").lower().strip()
            if continuar != 'si':
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    print("\nDetalle de su pedido:")
    print(f"Pikachu roll: {cantidadPikachu}")
    print(f"Otaku Roll: {CantidadOtaku}")
    print(f"Pulpo Venenoso Roll: {CantidadPulpo}")
    print(f"Anguila eléctrica Roll: {CantidadAnguila}")

    subtotal = (cantidadPikachu * precioPikachu + CantidadOtaku * PrecioOtaku + CantidadPulpo * PrecioPulpo + CantidadAnguila * PrecioAnguila)

    descuento = 0
    while True:
        codigoDescuento = input("Tiene algun codigo de descuento (Si/No): ").lower().strip()

        if codigoDescuento == "si":
            while True:
                codigo = input("Ingrese el código de descuento: ")
                if codigo == 'soyotaku':
                    descuento = subtotal * 0.10
                    print(f"Descuento aplicado: ${descuento}")
                    break
                elif codigo == 'x':
                    descuento = 0
                    break
                else:
                    print("Código no válida, intente nuevamente o ingrese 'X' para cancelar")
        elif codigoDescuento == 'no':
            descuento = 0
            break
        else:
            print("Respuesta no válida. Por favor ingrese 'si' o 'no'.")
    total = subtotal - descuento
    print("*"*30)
    print(F"Subtotal por pagar: ${subtotal}")
    print(F"Descuento por código: ${subtotal}")
    print(f"Total: ${total}")
    print("*"*30)

    otro_pedido = input("¿Desea realizar otro pedido? (si/no): ").strip().lower()
    if otro_pedido != 'si':
        print("Gracias por su pedido. Hasta pronto")
        break
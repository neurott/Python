# Precios de los rolls
precio_pikachu_roll = 4500
precio_otaku_roll = 5000
precio_pulpo_roll = 5200
precio_anguilla_roll = 4800

# Variables para contar la cantidad de cada tipo de roll
cantidad_pikachu_roll = 0
cantidad_otaku_roll = 0
cantidad_pulpo_roll = 0
cantidad_anguilla_roll = 0

# Comienza el ciclo principal
while True:
    # Menú de selección de rolls
    while True:
        print("\nSeleccione el roll de sushi que desea agregar a su pedido:")
        print("1. Pikachu Roll - $4500")
        print("2. Otaku Roll - $5000")
        print("3. Pulpo Venenoso Roll - $5200")
        print("4. Anguila Eléctrica Roll - $4800")
        print("5. Salir del pedido")
        
        try:
            opcion = int(input("Ingrese la opción (1-5): "))
            match opcion:
                case 1:
                    cantidad_pikachu_roll += 1
                case 2:
                    cantidad_otaku_roll += 1
                case 3:
                    cantidad_pulpo_roll += 1
                case 4:
                    cantidad_anguilla_roll += 1
                case 5:
                    break
                case _:
                    print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")
                    continue

            # Preguntar si desea agregar otro roll
            continuar = input("¿Desea agregar otro roll? (sí/no): ").lower()
            if continuar != "sí":
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Mostrar el resumen del pedido
    print("\n******************************")
    print("Detalle de su pedido:")
    print(f"Pikachu Roll : {cantidad_pikachu_roll}")
    print(f"Otaku Roll : {cantidad_otaku_roll}")
    print(f"Pulpo Venenoso Roll : {cantidad_pulpo_roll}")
    print(f"Anguila Eléctrica Roll : {cantidad_anguilla_roll}")
    print("******************************")

    # Calcular el subtotal
    subtotal = (cantidad_pikachu_roll * precio_pikachu_roll + 
                cantidad_otaku_roll * precio_otaku_roll + 
                cantidad_pulpo_roll * precio_pulpo_roll + 
                cantidad_anguilla_roll * precio_anguilla_roll)

    # Aplicar descuento si corresponde
    descuento = 0
    while True:
        codigo_descuento = input("¿Tiene un código de descuento? (sí/no): ").lower()
        match codigo_descuento:
            case "sí":
                while True:
                    codigo = input("Ingrese el código de descuento: ")
                    match codigo:
                        case "soyotaku":
                            descuento = subtotal * 0.10
                            print(f"Descuento aplicado: ${descuento}")
                            break
                        case "x":
                            descuento = 0
                            break
                        case _:
                            print("Código no válido, intente nuevamente o ingrese 'X' para cancelar.")
            case "no":
                descuento = 0
                break
            case _:
                print("Respuesta no válida. Por favor ingrese 'sí' o 'no'.")

    # Calcular el total después del descuento
    total = subtotal - descuento

    # Mostrar el detalle final
    print("\n******************************")
    print(f"Subtotal por pagar: ${subtotal}")
    print(f"Descuento por código: ${descuento}")
    print(f"TOTAL: ${total}")
    print("******************************")

    # Preguntar si desea realizar otro pedido
    otro_pedido = input("¿Desea realizar otro pedido? (sí/no): ").lower()
    if otro_pedido != "sí":
        print("Gracias por su pedido. ¡Hasta pronto!")
        break

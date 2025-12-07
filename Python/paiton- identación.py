#PRECIOS
precioPikachuRoll = 4500
precioOtakuRoll = 5000
precioPulpoVenenosoRoll = 5200
precioAnguilaRoll = 4800

# Variables para contar la cantidad de cada roll
cantidadPikachuRoll = 0
cantidadOtakuRoll = 0
cantidadPulpoRoll = 0
cantidadAnguilaRoll = 0

#Comienza ciclo principal
while True:
    #Menú seleccion de rolls
    while True:
        print("\nSeleccione el roll de sushi que desea agregar a su pedido: ")
        print("1. Pikachu Roll - $4500")
        print("2. Otaku Roll - $5000")
        print("3. Pulpo Venenoso Roll - $5200")
        print("4. Anguila Eléctrica Roll - $4800")
        print("5. Salir") 

        try:
            opcion = int(input("Ingrese una opción (1-5): "))
            match opcion:
                case 1:
                    cantidadPikachuRoll += 1 
                case 2:
                    cantidadOtakuRoll +=1
                case 3:
                    cantidadPulpoRoll += 1
                case 4:
                    cantidadAnguilaRoll += 1
                case 5:
                    break
                case _:
                    print("OPCIÓN NO VÁLIDA. POR FAVOR, SELECCIONE UNA OPCIÓN ENTRE 1-5")
                    continue
            # Preguntamos si desea agregar otro roll
            continuar = input("¿Desea agregar otro roll? (Y/N): ").lower
            if continuar != "y":
                break
        except ValueError:
            print("Por favor ingrese un número válido.")

    #Mostramos el resumen del pedido

    print("\n********************")
    print("Detalle de su pedido: ")
    print(f"Pikachu Roll : {cantidadPikachuRoll}")
    print(f"Otaku Roll: {cantidadOtakuRoll}")
    print(f"Pulpo Venenoso Roll: {cantidadPulpoRoll}")
    print(f"Anguila Eléctrica Roll: {cantidadAnguilaRoll}")
    print("**********************************************")


    #Calculamos el subtotal
    subtotal = (cantidadPikachuRoll * precioPikachuRoll +
                cantidadOtakuRoll * precioOtakuRoll +
                cantidadPulpoRoll * precioPulpoVenenosoRoll +
                cantidadAnguilaRoll * precioAnguilaRoll)
    
    #Aplicamcos descuento si corresponde
    descuento = 0
    while True:
        codigo_descuento = input("¿Tiene algun código de descuento? (Y/N): ").lower
        match codigo_descuento:
            case "y":
                while True:
                    codigo = input("Ingrese el codigo de descuento: ")
                    match codigo:
                        case "soyotaku":
                            descuento = subtotal * 0.10
                            print(f"Descuento aplicado: {descuento}")
                            break
                        case "x":
                            descuento = 0
                            break
                        case _:
                            print("Código no válido. Intente nuevamente o ingrese 'x' para cancelar")
            case "n":
                descuento = 0
                break
            case _:
                print("Respuesta no válida. Ingrese Y/N")

#Calculamos el total después del descuento                  
    total = subtotal - descuento

#Mostrar el detalle final

    print("\n ************************************")
    print(f"Subtotal por pagar: ${subtotal}")
    print(f"Descuento por código promocional: ${descuento}")
    print(f"TOTAL A PAGAR: ${total}")
#Preguntar si desea realizar otro pedido

    otro_pedido = input("¿Desea realizar otro pedido? (Y/N): ").lower()
    if otro_pedido != "y":
        print("Gracias por su pedido.")
        break
mayor = None
menor = None

while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Ingresar número.")
    print("2. Mostrar mayor.")
    print("3. Mostrar menor.")
    print("4. Terminar programa.\n")

    opcion = input("Elija una opción: ")

    match opcion:
        case "1":
            while True:
                entrada = input("Ingrese número entre 0 y 100: ")
                try:
                    num = int(entrada)
                except ValueError:
                    print("Debe ingresar un número entero.")
                    continue

                if 0 <= num <= 100:
                    if mayor is None or num > mayor:
                        mayor = num
                    if menor is None or num < menor:
                        menor = num
                    print ("Ingreso exitoso")
                    break
                else:
                    print("Debe ingresar un número entre 0 y 100.")
        case "2":
            if mayor is None:
                print("No se han ingresado números.")
            else:
                print(f"El númeor mayor hasta el momento es: {mayor}")
        case "3":
            if menor is None:
                print("No se han ingresado números.")
            else:
                print(f"El número menor hasta el momento es: {menor}")
        case "4":
            print("Fin del programa.")
            break
        case _:
            print("Debe ingresar una opción válida.")

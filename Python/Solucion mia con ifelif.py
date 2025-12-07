mayor = None
menor = None

while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Ingresar número.")
    print("2. Mostrar mayor.")
    print("3. Mostrar menor.")
    print("4. Terminar programa.\n")

    op = int(input("Seleccione una opción: "))

    if op == 1:
        while True:
            entrada = input("Ingrese un número entre 0 y 100: ")
            try:
                num = int(entrada)
            except ValueError:
                print("Ingresa un número entero")
                continue

            if 0 <= num <= 100:
                if mayor is None or num > mayor:
                    mayor = num
                if menor is None or num < menor:
                    menor = num
                print(f"\nIngreso exitoso, se ingresó el número: {num}")

                break
            else:
                print("Debe de ingresar un número entre 0 y 100")
    elif op == 2:
        if mayor is None:
            print("No se han ingresado números")
        else:
            print(f"NUMERO MAYOR {mayor}")
    elif op == 3:
        if menor is None:
            print("No se ha ingresado ningún número que sea menor.")
        else:
            print(f"NÚMERO MENOR: {menor}")
    elif op == 4:
        print("Saliendo...")
        break
    
    
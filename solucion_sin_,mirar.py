mayor = None
menor = None

while True:
    print("\nMenú Principal")
    print("1. Ingresar el número")
    print("2. Mostrar mayor")
    print("3. Mostrar menor")
    print("4. Salir del programa")

    op = int(input("Seleccione una opción: "))

    if op == 1:
        while True:
            entrada = input("Ingrese un número entre el 0 y el 100: ")
            try:
                num = int(entrada)
            except ValueError:
                print("Ingrese un número entero.")
                continue
            if 0 <= num <= 100:
                if mayor is None or num > mayor:
                    mayor = num
                if menor is None or num < menor:
                    menor = num
                    print("Ingreso exitoso")
                break
            else:
                print("Debe ingresar un númeor entre 0 y 100")
    
    elif op == 2:
        if mayor is None:
            print("No se ingreso ningún número...")
        else:
            print(f"El número mayor es: {mayor}")
    elif op == 3:
        if menor is None:
            print("No se ingreso ningun número menor...")
        else:
            print(f"El número menor es: {menor}")        
    elif op == 4:
        print("Saliendo....")
        break
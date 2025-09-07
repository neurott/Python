mayor = -1
menor = 101

while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Ingresar número.")
    print("2. Mostrar mayor.")
    print("3. Mostrar menor.")
    print("4. Terminar programa.")

    op = input("Elija una opción: ")

    if op == '1':
        while True:
            try:
                n = int(input("Ingrese un número entre 0 y 100: "))
                if n >= 0 and n <= 100:
                    print("Ingreso exitoso!")
                    break
                else:
                    print("Debe ingresar un número entre 0 y 100...")
            except:
                print("Debe ingresar un número entero...")
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n #Esto lo q hace es guardar la variable
 #   if op == '2':
  #      print(mayor)
   # elif op == '3':
    #    print(menor)
    #elif op == '4':
     #   break
    elif op == '2':
        if mayor == -1:
            print("No se han ingresado números.")
        else:
            print(f"El número mayor hasta el momento: {mayor}")
    elif op == '3':
        if menor == 101:
            print("No se han ingresado números.")
        else:
            print(f"El número menor hasta el momento es: {menor}")
    elif op == '4':
        print("Fin del programa...")
        break
    else:
        print("Debe ingresar una opción válida.")
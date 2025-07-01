comprobar = True

while comprobar == True:
    n = int(input("Ingrese un número entero positivo: "))
    x = (n * i)
    if n > 0:   
       for i in range (1,11):
        #print(n, "por", i, "es igual a:", n*i)
        print(f"{n} * {i} = {x}")
        comprobar = False  
    else:
        print("El número ingresado no es correcto. Inténtelo nuevamente")

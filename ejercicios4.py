#ejercicio 4:
#Ingrese un número entero mayora  cero por teclado e indique si es o no "perfecto".
n = int(input("INGRESA EL NÚMERO MAYOR A CERO: "))
if n <= 0:
    print("El número debe ser mayor a cero.")
else:
    suma_divisores = 0

    for i in range (1,n):
        if n % i == 0:
            suma_divisores += i
    if suma_divisores == n:
        print(f"{n} es un número perfecto.")
    else:
        print(f"{n} no es un número perfecto.")
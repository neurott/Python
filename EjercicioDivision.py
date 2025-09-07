#Escriba un programa donde se realicen 3 intentos de dividir dos números aleatorios generados entre -3 y 3.
#Si la división resulta en 1, se felicita al usuario y termina el programa. 
#Si el resultado es distinto de 1 o -1, el programa continuará hasta completar los 3 intentos o encontrar el resultado deseado.
#También se debe manejar el error de división por cero con una excepción.

import random as randomint

#Realizar la división

for i in range(3):
    num1 = randomint.randint(-3, 3)
    num2 = randomint.randint(-3, 3)
    print("intento" , i+1)
    print("El numero 1 es",num1)
    print("El numero 2 es",num2)
    try:
        resultado = num1 / num2
        print("El resultado de la division es en el intento ",i+1," es " , resultado)
        if resultado == 1:
            print("Felicidades, has obtenido el resultado deseado")
            break
        else:
            print("El resultado es distinto de 1 o -1")
    except ZeroDivisionError:
        print("El valor del numero 2 en el intento",i+1, "es 0 y no se puede dividir entre cero")

print("Su suerte no ha sido la mejor, para la proxima sera")       
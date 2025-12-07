#MUESTRE POR PANTALLA EL RESULTADO DEL FACTORIAL DE UN NÚMERO
# 5! = 120
#import random
#numero = random.randint(1,10)
numero = int(input("INGRESA UN NÚMERO: "))

factorial = 1

for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial del {numero} es: {factorial}")
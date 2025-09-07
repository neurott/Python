n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

if n1 == n2 == n3:
    print("Todos los números son iguales.")
elif n1 >= n2 and n1 >= n3:
    print(f"El número mayor es: {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"El número mayor es: {n2}")
else:
    print(f"El número mayor es: {n3}")


#Esto cubre los siguientes casos:

#Todos iguales

 #   Dos iguales y mayores
#
 #   Uno mayor claramente    


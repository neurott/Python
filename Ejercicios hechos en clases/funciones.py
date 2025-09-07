#Función que saluda
def saludar():
    print("Hola, Bienvenido a tu primera funcnión en py")
saludar()


#Función que suma dos números
def sumar():
    resultado = 2 + 3
    print("La suma es: ", resultado)
sumar()


#Función con parámetros (recibe datos)
def saludar_a(nombre):
    print("Hola, ", nombre + "!")
saludar_a("Ignacio")
saludar_a("Rafael de las Flores")


#Función que devuelve un resultado (return)
def multiplicar_por_dos(numero):
    return numero * 2
resultado = multiplicar_por_dos(5)
print("El resultado es: ", resultado)


#Función que suma dos números ingresados por usuario
def sumar_dos_num():
    n1 = int(input("Ingrese el primer num: "))
    n2 = int(input("Ingrese el segundo num: "))
    suma = n1 + n2
    print("La suma es: ", suma)
sumar_dos_num()


#Función que verifica si un número es par o impar
def par_o_impar(num):
    if num % 2 == 0:
        print("El num es par")
    else:
        print("El num es impar")
par_o_impar(4)
par_o_impar(7)


#Función que calcula el área de un rectángulo
def area_rectangulo(base, altura):
    area = base * altura
    return area
resultado = area_rectangulo(5,3)
print("El area es: ", resultado)


#Función que recibe una lista de números y dice el mayor
def mayor_de_lista(lista):
    mayor = max(lista)
    print("El num mayor es: ", mayor)
mayor_de_lista([3, 7, 9, 2, 17, 1])


#Función que calcular el promedio de notas
def prom_notas(notas):
    total = sum(notas)
    cantidad = len(notas)
    promedio = total/cantidad
    return promedio
notas = [5.5, 6.0, 1.0, 7.0, 4.8]
prom = prom_notas(notas)
print("El prom de notas es: ", prom)


#Función con un buble que imprima un num N veces
def contar_hasta(n):
    for i in range(1, n + 1):
        print(i)
contar_hasta(100)


#Función que muestra un menú simple
def menu():
    print("1. Saludar.")
    print("2. Despedirse.")
    op = input("Elige una opción: ")

    if op == "1":
        print("¡Hola!")
    elif op == "2":
        print("¡Chao!")
    else:
        print("Opción no válida.")
    
menu()
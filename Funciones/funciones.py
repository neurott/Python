#def saludo():
#    print("Hola")
#saludo()
#Funcion que saluda
def saludar():
    print("Hola")
saludar()

#Funcion que sume dos números
def sumar():
    resultado = 2 + 3
    print(f"La suma es: {resultado}")
sumar()

#función con parametros (recibe datos)
def saludar_a(nombre):
    print("Hola, ", nombre + "!")

saludar_a("Nicolás")
saludar_a("Pedrito Pascal")

#Función que devuelve un resultado (return)
def multiplicar_por_dos(numero):
    return numero * 2
resultado = multiplicar_por_dos(5)
print(f"RESULTADO: {resultado}")

#Función que sume dos numeros ingresado por el usuario 
def sumar_dos_nums():
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    suma = num1 + num2
    print(f"La suma es: {suma}")
sumar_dos_nums()

#Función que verifique si un número es par o impar
def verificar_par_impar():
    num = int(input("Número: "))
    if num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
verificar_par_impar()

#Lo mismo pero del profe
def par_o_impar(num):
    if num % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
par_o_impar(4)
par_o_impar(7)

#Función para calcular el area de un rectángulo
def area_rectangulo():
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    resultado = base * altura
    print(f"El area de cuadrado es: {resultado}")
area_rectangulo()

#profe
def area_rectangulo_profe(base, altura):
    area = base * altura
    return area
resultado = area_rectangulo_profe(5, 3)
print(f"El area es: {resultado}")

#Función que reciba una lista de números e indique cual es el mayor.

#def mayor_de_lista(lista):
    #estamalomayor = max(lista)
    #print(f"El número mayor es: {mayor}")
#mayor_de_lista(3, 8, 9, 17, 1)

#Función que calcule el promedio de notas de un alumno
#Muy largo
def promedio_notas():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    n3 = int(input("Número 3: "))
    promedio = (n1 + n2 +n3) / 3
    print(f"El promedio de notas es: {promedio}")
promedio_notas()


#profe

def prom_notas(notas):
    total = sum(notas)
    cantidad = len(notas)
    promedio = total / cantidad
    return promedio
notas = [5.5, 6.8, 1.0, 4.0, 3.6]
prom = prom_notas(notas)
print("El prom de notas es : ", prom)

#funcion que imprima un numero n veces # prueba quitarle el 1 al n+1
def contar_hasta(n):
    for i in range(1,n+1):
        print(i)
contar_hasta(20)

def menu():
    print("1. Saludar")
    print("2. Despedirse")
    op = input("Elige una opción: ")

    if op == "1":
        print("Hola")
    elif op == "2":
        print("Chao")
    else:
        print("Opción no válida")
menu()
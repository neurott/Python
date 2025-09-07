'''Realiza un programa con menú para registrar temperaturas diarias (lista) y 
luego calcular promedio, máximo y mínimo con funciones.'''

def mostrar_menu():
    print("\n--- REGISTRO DE TEMPERATURAS ---")
    print("1. Ingresar nueva temperatura")
    print("2. Mostrar promedio")
    print("3. Mostrar temperatura máxima")
    print("4. Mostrar temperatura mínima")
    print("5. Mostrar todas las temperaturas")
    print("6. Salir")

def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else "Sin datos"

def mostrar_maximo(lista):
    if lista:
        print("Máxima:", max(lista))
    else:
        print("Sin datos")

def mostrar_minimo(lista):
    if lista:
        print("Mínima:", min(lista))
    else:
        print("Sin datos")

def mostrar_todas(lista):
    if lista:
        print("Temperaturas registradas:", lista)
    else:
        print("Sin datos")

def main():
    temperaturas = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                temp = float(input("Ingresa la temperatura: "))
                temperaturas.append(temp)
                print("Temperatura registrada.")
            except ValueError:
                print("Debes ingresar un número válido.")

        elif opcion == "2":
            print("Promedio:", calcular_promedio(temperaturas))

        elif opcion == "3":
            mostrar_maximo(temperaturas)

        elif opcion == "4":
            mostrar_minimo(temperaturas)

        elif opcion == "5":
            mostrar_todas(temperaturas)

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")

main()

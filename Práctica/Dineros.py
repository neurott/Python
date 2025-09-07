dineros = {}

def deposito():
    objetivo = 50000
    mes = input("Mes: ")
    dinerotransf = int(input("Cuanto: "))   
    restante = (objetivo - dinerotransf)
    dineros[mes] = {
        "Objetivo": objetivo,
        "Dinero": dinerotransf,
        "Restante": restante,
    }

def gasto():
    obj = 50000
    gastoss = int(input("Cuanto gastaste: "))
    restante = (obj - gastoss)
    print(f"Gastaste {gastoss}, ahora te quedan: {restante}")

def datosactuales():
    print("Datos actualizados para el mes en cuestión: ")
    for mes, datos in dineros.items():
        print(f"\nMes: {mes}")
        print(f"Objetivo: {datos['Objetivo']}")
        print(f"Dinero: {datos['Dinero']}")
        print(f"Restante: {datos['Restante']}")    

def main():
    while True:
        print("\nMenú que hice para cuando mis padres me den dineros...")
        print("1. Cuanto me deposistaron")
        print("2. Cuanto gasté")
        print("3. Datos actualizados")
        print("4. Salir")

        op = int(input("Opción: "))

        if op == 1:
            deposito()
        elif op == 2:
            gasto()
        elif op == 3:
            datosactuales()
        elif op == 4:
            print("Saliendo...")
            break

main()
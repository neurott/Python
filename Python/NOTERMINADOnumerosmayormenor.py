mayor = 1
menor = 100

while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Ingresar número.")
    print("2. Mostrar mayor.")
    print("3. Mostrar menor.")
    print("4. Terminar programa.")

    try:
        op = int(input("Elija una opción: "))
    except ValueError:
        print("Debe ingresar un número!")
        continue
    if op == '1':
        n = int(input("Ingrese el número: "))
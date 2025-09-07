usuarios = []
passwd = []

while True:
    print("\nMENÚ")
    print("1. Inicio sesión")
    print("2. Registrar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

    try:
        op = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Opción inválida...")


    try:
        if op == 1:
            print("INICIAR SESIÓN....")

            usuario = input("INGRESA EL USUARIO: ")
            contrasena = input("INGRESA LA CONTRASEÑA: ")
        elif op == 2:

        elif op == 3:

        elif op == 4:
            break
    except:
        print("?")
lista_usuarios = []
lista_passwords = []

while True:
    print("""\nMenú Usuario:
        1) Inicio sesión.
        2) Registrar usuario.
        3) Eliminar usuario.
        4) Salir.""")
    
    try:
        opc = int(input("Ingrese una opción: "))

        match opc:

            case 1:
                if len(lista_usuarios) != 0:
                    nombreUsuario = input("Ingrese nombre de usuario: ")
                    if nombreUsuario in lista_usuarios:
                        index = lista_usuarios.index(nombreUsuario)
                        contrasennaUsuario = input("Ingrese contraseña: ")
                        if contrasennaUsuario == lista_passwords[index]:
                            print("Inicio de sesión exitoso.")
                        else:
                            print("Contraseña inválida.")
                    else:
                        print("Usuario no registrado.")
                else:
                    print("No hay usuarios registrados.")

            case 2:
                nombre = input("Ingrese nombre de usuario: ")
                contrasenna = input("Ingrese contraseña: ")
                if nombre not in lista_usuarios:
                    lista_usuarios.append(nombre)
                    lista_passwords.append(contrasenna)
                    print(f"Usuario {nombre} registrado exitosamente.")
                else:
                    print("El usuario ya está registrado.")

            case 3:
                if len(lista_usuarios) != 0:
                    nombreUsuario = input("Ingrese nombre de usuario a eliminar: ")
                    if nombreUsuario in lista_usuarios:
                        index = lista_usuarios.index(nombreUsuario)
                        contrasennaUsuario = input("Ingrese contraseña para confirmar: ")
                        if contrasennaUsuario == lista_passwords[index]:
                            lista_usuarios.remove(nombreUsuario)
                            print(f"Usuario {nombreUsuario} eliminado.")
                        else:
                            print("Contraseña incorrecta.")
                    else:
                        print("El usuario no existe.")
                        
                else:
                    print("No hay usuarios registrados.")

            case 4:
                print("Saliendo...")
                break

            case _:
                print("Ingrese 1, 2, 3 o 4.")

    except ValueError:
        print("Ingrese un número.")
usuarios = []        # Lista para almacenar los nombres de usuario
contrasenas = []     # Lista para almacenar las contraseñas correspondientes

while True:
    print("\nMenú:")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        usuario = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")

        if usuario in usuarios:
            indice = usuarios.index(usuario)
            if contrasenas[indice] == contrasena:
                print("Inicio de sesión exitoso.")
            else:
                print("Contraseña incorrecta.")
        else:
            print("El usuario no existe.")

    elif opcion == "2":
        nuevo_usuario = input("Nuevo nombre de usuario: ")
        if nuevo_usuario in usuarios:
            print("El usuario ya existe.")
        else:
            nueva_contrasena = input("Nueva contraseña: ")
            usuarios.append(nuevo_usuario)
            contrasenas.append(nueva_contrasena)
            print("Usuario registrado correctamente.")

    elif opcion == "3":
        usuario_a_eliminar = input("Nombre de usuario a eliminar: ")

        if usuario_a_eliminar in usuarios:
            indice = usuarios.index(usuario_a_eliminar)
            contrasena_confirmacion = input("Ingrese la contraseña para confirmar: ")
            if contrasenas[indice] == contrasena_confirmacion:
                usuarios.pop(indice)
                contrasenas.pop(indice)
                print("Usuario eliminado correctamente.")
            else:
                print("Contraseña incorrecta. No se pudo eliminar el usuario.")
        else:
            print("El usuario no existe.")

    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

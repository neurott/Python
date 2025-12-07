# Variables iniciales de usuarios y contraseñas
usuario1, usuario2, usuario3 = None, None, None
contrasena1, contrasena2, contrasena3 = None, None, None

# Menú principal
while True:
    # Mostrar opciones del menú principal
    print("\n1) Iniciar sesión")
    print("2) Registrar usuario")
    print("3) Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            # Verificar si hay usuarios registrados
            if usuario1 is None and usuario2 is None and usuario3 is None:
                print("No hay usuarios registrados. Por favor regístrese primero.")
                continue  # Volver al menú principal

            # Solicitar usuario y contraseña
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")

            # Validar el usuario y contraseña
            if (usuario == usuario1 and contrasena == contrasena1) or \
               (usuario == usuario2 and contrasena == contrasena2) or \
               (usuario == usuario3 and contrasena == contrasena3):
                print(f"Bienvenido, {usuario}!")

                # Menú después de iniciar sesión
                while True:
                    print("\n1) Realizar llamada")
                    print("2) Enviar correo electrónico")
                    print("3) Cerrar sesión")

                    try:
                        opcion_usuario = int(input("Seleccione una opción: "))
                        if opcion_usuario == 1:
                            # Realizar llamada
                            while True:
                                numero = input("Ingrese un número celular (debe comenzar con 9 y ser de 8 dígitos): ")
                                if len(numero) == 8 and numero[0] == '9' and numero.isdigit():
                                    print(f"Llamada realizada al número {numero}.")
                                    break
                                else:
                                    print("Número inválido. Debe comenzar con 9 y ser de 8 dígitos.")
                        elif opcion_usuario == 2:
                            # Enviar correo electrónico
                            while True:
                                correo = input("Ingrese el correo electrónico: ")
                                if "@" in correo:
                                    break
                                else:
                                    print("Correo inválido. Debe contener al menos un '@'.")
                            
                            mensaje = input("Ingrese el mensaje a enviar: ")
                            print(f"Correo enviado a {correo} con el mensaje: {mensaje}")
                        elif opcion_usuario == 3:
                            # Cerrar sesión
                            print("Cerrando sesión...")
                            break  # Volver al menú principal
                        else:
                            print("Opción no válida. Intente nuevamente.")
                    except ValueError:
                        print("Por favor ingrese un número válido.")
            else:
                print("Usuario o contraseña incorrectos.")
        
        elif opcion == 2:
            # Registrar usuario
            for i in range(1, 4):
                usuario = input(f"Ingrese el nombre de usuario {i}: ")
                contrasena = input(f"Ingrese la contraseña para {usuario}: ")
                
                if i == 1:
                    usuario1, contrasena1 = usuario, contrasena
                elif i == 2:
                    usuario2, contrasena2 = usuario, contrasena
                elif i == 3:
                    usuario3, contrasena3 = usuario, contrasena

        elif opcion == 3:
            # Salir
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
    
    except ValueError:
        print("Por favor ingrese un número válido.")

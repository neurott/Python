'''Crear un programa de validación de usuario y contraseña 
(consultar usuario y contraseña),
 los únicos dos usuarios conectados son:
User1: pedro   	Contraseña1: 1234
User2: angel		Contraseña2: a4s1

user1 = "pedro"
user2 = "angel"

contrasena1 = "1234"
contrasena2 = "a4s1"

usuario = input("Ingrese el usuario: ").strip()
contraseña = input("Ingrese la contraseña: ").strip()

if (usuario ==user1 and contraseña == contrasena1) or (usuario == user2 and contraseña == contrasena2):
    print(f"Ha ingreasdo con éxito: {usuario}")
else:
    print("Error")'''
# diccionario
usuarios = {
    "pedro": "1234",
    "angel": "a4s1"
}

while True:
    try:
        usuario = input("Ingrese el usuario: ").strip()
        contraseña = input("Ingrese la contraseña: ").strip()

        # validación directa en el diccionario
        if usuario in usuarios and usuarios[usuarios] == contraseña:
            print(F"HA INGRESADO CON ÉXITO {usuario}")
        else:
            print("ERROR: USUARIO NO ENCONTRADO\n")

    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        break
    except Exception as e:
        print(f"Ha ocurrido un error inesperado : {e}")
        break

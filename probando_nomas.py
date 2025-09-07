#TECH SECURE

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu Apellido Materno: ")
cedula = input("Ingresa tu cedula de identidad: ")
nacimiento = input("Ingresa tu fecha de nacimiento (DD/MM/YYYY): ")
pais = input("Ingresa tu país de residencia:")

print(f"Contraseña:",nombre[0:2],apellido[0::3],cedula[0::3],nacimiento[2])
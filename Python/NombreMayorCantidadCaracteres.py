#Mostrar nombre que tenga mayor cantidad de caracteres en un mensaje de salida por pantalla
lista = []
nombreLargo = ""
print("\nSOLO 3.....")
for i in range(3):
    nombre = input(f"Ingresa el nombre {i+1}: ")
    lista.append(nombre)

    if len(nombre) > len(nombreLargo):
        nombreLargo = nombre

print(f"LISTA CON LOS NOMBRES: {lista}")
print(f"El nombre más largo es: {nombreLargo}")

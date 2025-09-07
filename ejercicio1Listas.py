listaNombres = []
nombreLargo = ""

for i in range(3):
    nombre = input(f"Ingrese nombre {i+1}: ")
    listaNombres.append(nombre)

    if len(nombre) > len(nombreLargo):
        nombreLargo = nombre

print(f"El nombre más largo es: {nombreLargo}")
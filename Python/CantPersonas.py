cantPersonas = 0

while cantPersonas < 1:
    try:
        cantPersonas = int(input("Ingrese la cantidad de personas que han rendido la prueba de conducir: "))
        if cantPersonas < 1:
            print("Debe ingresar un número mayor a 0")
    except:
        print("Debe ser un número")

contAprobado = 0
contIncompleto = 0

for i in range(cantPersonas):
    noValido = True
    while noValido:
        try:
            examRendidos = int(input(f"Ingrese la cantidad de exámenes rendidos de persona N°{i+1}: "))
            noValido = False
        except:
            print("Exámenes rendidos debe ser un número")
    if examRendidos >= 3:
        print("Curso aprobado, exámenes completos")
        contAprobado += 1
    else:
        print("Curso no aprobado, exámenes incompletos")
        contIncompleto += 1

print(f"Aprobaron {contAprobado}...")
print(f"Reprobaron {contIncompleto}...b")
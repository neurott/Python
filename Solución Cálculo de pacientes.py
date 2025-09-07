while True:
    try:
        cantidad = int(input("Ingrese la cantidad de pacientes a registrar: "))
        break
    except:
        print("Debe ingresar un número entero.")

mayores = 0
menores_o_iguales = 0

for _ in range(cantidad):
    nombre = input("Ingrese el nombre del paciente: ")
    
    while True:
        try:
            edad = int(input(f"Ingrese la edad de {nombre}: "))
            break
        except:
            print("Debe ingresar un número entero.")
    
    if edad > 60:
        print("Mayor de 60 años.")
        mayores += 1
    else:
        print("60 años o menos.")
        menores_o_iguales += 1

print(f"\nSe registraron {mayores} pacientes mayores de 60 años.")
print(f"Se registraron {menores_o_iguales} pacientes de 60 años o menos.")
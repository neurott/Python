edad = int(input("Ingrese su edad: "))
promedio = int(input("Ingrese su promedio de notas"))
print("1 - VIVE FUERA DE LA CIUDAD, 0 - VIVE EN LA CIUDAD.")
lugarResidencia = int(input("Vive fuera o vive en la ciudad (1/0): "))
print("1 - ESTA TRABAJANDO, 0 - NO ESTA TRABAJANDO")
situacionLaboral = int(input("Cual es su situación de trabajo? (1/0)"))

#Reglas para otorgar beneificos
#Beneficio total se entrega si el estudiatne
if edad < 25 and promedio >= 80 and lugarResidencia == 1 and situacionLaboral == 0:
    print("Beneficio total otorgado")
elif edad < 25 and promedio >=80 and lugarResidencia == 1 and situacionLaboral == 1:
    print("Benficio parcial A otorgado")
elif promedio >= 60 and lugarResidencia == 1:
    print("Beneficio parcial B otorgado")
else:
    print("No se otorga ningun beneficio")

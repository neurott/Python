print("--- Sistema de Entrega de Beneficios Estudiantiles ---")

edad = int(input("Ingrese su edad (número entero): "))
promedio = int(input("Ingrese su promedio de notas (entre 1 y 100): "))
residencia = int(input("Ingrese 1 si vive fuera de la ciudad, 0 si vive en la ciudad: "))
laboral = int(input("Ingrese 1 si actualmente está trabajando, 0 si no trabaja: "))

if edad < 25 and promedio >= 80 and residencia == 1 and laboral == 0:
    print("Beneficio otorgado: Beneficio total")
elif edad < 25 and promedio >= 80 and residencia == 1 and laboral == 1:
    print("Beneficio otorgado: Beneficio parcial A")
elif promedio >= 60 and residencia == 1:
    print("Beneficio otorgado: Beneficio parcial B")
else:
    print("No se otorga ningún beneficio")

print("--- Fin del Sistema ---")
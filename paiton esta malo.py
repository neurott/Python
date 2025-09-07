##Datos a solicitar:
##• Rol del usuario ("investigador" o "estudiante").
##• Número de proyectos activos.
##• Puntaje de seguridad (rango de 0 a 100).
print("INVESTIGADOR O ESTUDIANTE\n")
rol = input("ROL: ")
proyectos = int(input("NÚMEROS DE PROYECTOS ACTIVOS: "))
puntaje = int(input("PUNTAJE DE SEGURIDAD: "))

if rol == ("investigador") and proyectos >= 3 and puntaje == 90 or puntaje > 90:
    print("ACCESO PRIORITARIO")
elif rol == ("estudiante") and proyectos >= 1 or puntaje >= 70 or puntaje == 89:
    print("ACCESO CON ACOMPAÑANTE")
else:
    print("ACCESO DENEGADO.")
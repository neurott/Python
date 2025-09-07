#Solicitar datos al usuario
rol = input("Ingrese su rol (investigador o estudiante): ").lower()
proyectos = int(input("Ingrese el número de proyectos activos: "))
puntaje = int(input("Ingrese su puntaje de seguridad (0 a 100): "))

#Evaluar las condiciones
if rol == "investigador" and proyectos > 3 and puntaje >= 90:
    print("Acceso prioritario: Use la puerta norte.")
elif rol == "estudiante" and (proyectos >= 1 or (70 <= puntaje <=89)):
    print("Acceso con acompañante: Diríjase a recepción")
elif puntaje < 70 or not (rol == "investigador" and proyectos > 3 and puntaje >= 90) or (rol == "estudiante" and (proyectos >= 1 or (70 <= puntaje <=89))):
    print("Acceso denegado: No cumple con los requisitos de ingreso.")
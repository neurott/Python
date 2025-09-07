n1 = float(input("PRIMERA NOTA: "))
n2 = float(input("SEGUNDA NOTA: "))
n3 = float(input("TERCERA NOTA: "))

promedio = (n1 + n2 + n3 ) / 3

print(f"PROMEDIOS: {promedio} ")

if promedio >= 4.0:
    print("APROBADO.")
else:
    print("Reprobado.")
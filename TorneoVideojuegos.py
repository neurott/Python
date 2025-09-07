print("--- Sistema de Clasificación del Torneo Nacional de Videojuegos ---")

edad = int(input("Ingrese su edad (número entero): "))
experiencia = int(input("Ingrese sus años de experiencia en videojuegos (entero): "))
rendimiento = int(input("Ingrese su promedio de rendimiento (entre 0 y 100): "))
participado = int(input("¿Ha participado anteriormente en torneos? (1 para sí, 0 para no): "))
recomendacion = int(input("¿Cuenta con recomendación oficial de un club? (1 para sí, 0 para no): "))

if 16 <= edad <= 25 and experiencia >= 3 and rendimiento >= 85:
    print("Clasificación obtenida: Clasificado directamente")
elif (16 <= edad <= 25 and participado == 1) or (edad > 25 and recomendacion == 1):
    print("Clasificación obtenida: Clasificado bajo revisión")
else:
    print("Clasificación obtenida: No clasificado")

print("--- Fin del Sistema ---")
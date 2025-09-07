try:
    numero = int(input("Ingresa el número para la tabla de multiplicar: "))

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print("No valido, intenta denuevo")
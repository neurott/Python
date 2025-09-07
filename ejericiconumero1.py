#Ingresar por teclado 5 números enteros, luego debe indicar:
#Cuántos números son mayores a cero
#Cuántos números son menores a cero
#Cuántos números son iguales a cero

#inicializamos los contadores
mayores_cero = 0
menores_cero = 0
iguales_cero = 0

print("Ingrese 5 números enteros:")

#bucle pedimos los 5 numeros
for i in range(5):
    while True:
        try:
            n = int(input(f"Número {i+1}: ")) # f-string para mostrar el número de entrada
            if n > 0:
                mayores_cero += 1
            elif n < 0:
                menores_cero += 1
            else:
                iguales_cero += 1     
            break # Salimos del while si el número es válido

        except ValueError:
            print("AWEONAO ESCRIBE UN NÚMERO.")
         #Clasificamos el número
        if n > 0:
            mayores_cero += 1
        elif n < 0:
            menores_cero += 1
        else:
            iguales_cero += 1

# mostramos los resultados
print("\nResultados:")
print(f"Números mayores a cero: {mayores_cero}")
print(f"Números menos a cero: {menores_cero}")
print(f"Números iguales a cero: {iguales_cero}")
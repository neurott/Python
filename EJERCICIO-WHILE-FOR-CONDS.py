 #Ejercicio 2:
#Ingrese por teclado 10 letras, indique cuántas de ellas son vocales y cuántas
#son consonantes.
#Iniciamos los contadores en cero
vocales = 0
consonantes = 0

print("VAMOS A INGRESAR 10 LETRAS:")

for i in range (10):
    while True:
        # Pedimos una letra
        letra = input(f"Ingresa la letra {i+1}: ")
        # Verioficamos que sea solo una letra
        if len(letra) == 1 and letra.isalpha():
            # Convertimos a minusucla para simplificar
            letra = letra.lower()
            if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
                vocales += 1
            else:
                consonantes += 1
            break
        else:
            print("Error. Debe ser una sola letra (a-z).")
#Mostramos los resultados
print("\n Resultados")
print(f"Vocales: {vocales}")
print(f"Consonates: {consonantes}")
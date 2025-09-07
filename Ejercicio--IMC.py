peso = float(input("INGRESA TU PESO: "))
altura = float(input("INGRESA TU ALTURA: "))

imc = (peso / altura **2)

print(f"TU IMC ES : {imc}")

if imc <= 18.5 or imc <= 24.9:
    print("NORMAL")
elif imc >= 25.0:
    print("SOBREPESO")
elif imc < 18.5:
    print("PESO INFERIOR AL NORMAL")
elif imc >= 30:
    print("OBESIDAD CLASE 1")
elif imc >= 35.0 or imc <= 39.9:
    print("OBESIDAD CLASE 2")
elif imc >= 40.0:
    print("OBESIDAD CLASE 3")
else:
    print("ERROR")
def restar(valor1, valor2):
    resultado = valor1 - valor2
    print(f"{valor1} - {valor2} = {resultado}")

while True:
    try:
        a = int(input("Primer valor: "))
        b = int(input("Segundo valor: "))
        break
    except:
        print("ingresar solamente números!!")

restar(a,b)
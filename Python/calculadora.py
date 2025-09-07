operator = input("Introduce un operador (+ - * /): ")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} no es un operador valido po")

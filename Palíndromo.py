def fahrenheit_a_celsius(f):
    c = (f - 32) * 5 / 9
    return round(c, 2)

def es_palindromo(numero):
    numero_str = str(numero).replace(".", "")
    return numero_str == numero_str[::-1]

fahrenheit = float(input("Ingresa los grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)

if es_palindromo(celsius):
    print(f"La conversión de {fahrenheit}°F es {celsius}°C y es un palíndromo.")
else:
    print(f"La conversión de {fahrenheit}°F es {celsius}°C y no es un palíndromo.")
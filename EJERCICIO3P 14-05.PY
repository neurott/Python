 # Verificar si el divisor es cero
try:
    numerador = float(input("NUMERADOR: "))
    divisor = float(input("DIVISOR: "))
 
    resultado = numerador / divisor
 
    print(f"El resultado de la división es: {resultado}")

except ValueError as ve:
    print(f"Error:{ve}")
except ZeroDivisionError:
    print("NO SE PUEDE DIVIDIR POR CERO")
finally:
    print("FINALIZA EL PROGRAMA.")
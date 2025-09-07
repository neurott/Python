#CON ARGUMENTOS Y CON RETORNO

def multiplicar(x,z):
    return x * z

while True:
    try:
        x= int(input("x : "))
        z= int(input("z : "))
        break
    except:
        print("Ingresar solamente numeros")

print(f"El resultado de {x} x {z} es: {multiplicar(x,z)}")
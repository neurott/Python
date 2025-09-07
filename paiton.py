palabra = input("ingrese palara secreta: ")

if len(palabra) > 5 and palabra[0].isupper() and palabra[-1].isdigit():
    print("ACEPTADA")
else:
    print("RECHAZADA")
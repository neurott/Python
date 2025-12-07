#Solicitamos la palabra secreta al usuario
palabra = input("Ingrese palabra secreta: ")

#Verificamos las condiciones
if len(palabra) > 5 and palabra[0].isupper() and palabra[-1].isdigit():
    print("Palabra aceptada")
else:
    print("Palabra rechazada")

    
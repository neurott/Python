#averigue si la letra dada por el usuario se encuentra en la cadena de la palabra murcielago
#ademas agregue en que posición se encuentra.
letra = input("INGRESA UNA LETRA: ")
palabra = 'Murcielago'

p = 0

#for caracter in palabra:
#   if 
for i in palabra:
    if i == letra.lower():
        print("La letra se encuentra en la palabra y esta en la posición", p)
        break       
    p += 1
else:
    print("La letra no se encuentra en la palabra.")

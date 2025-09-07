especiales = '-_*!?#$%'

while True:
    try:
        contraseña = input("Ingrese contraseña: ")

        if contraseña == '1':
            break

        #largo entre 8 y 16
        if len(contraseña) < 8 or len(contraseña) > 16:
            print("Contraseña inválida.")
            continue

        #Sin espacios
        if ' ' in contraseña:
            print("Contraseña inválida")
            continue

        #No puede terminar en caracter especial
        if contraseña[-1] in especiales:
            print("Contraseña inválida.")
            continue

        tiene_numero = False
        tiene_letra = False
        tiene_especial = False
        contador_especiales = 0
        valido = True

#        i = 0
#        while i < len(contraseña):
#            c = contraseña[i]
#            if c.isdigit():
#                tiene_numero = True
#            elif c.isalpha():
#                tiene_letra = True
#            elif c in especiales:
#                contador_especiales += 1
#                if contador_especiales > 1:
 #                   valido = False
  #                  break
   #             tiene_especial = True
    ##           valido = False
      #          break
       #     i += 1
        for c in contraseña:
            if c.isdigit():
                tiene_numero = True
            elif c.isalpha():
                tiene_letra = True
            elif c in especiales:
                contador_especiales += 1
                if contador_especiales > 1:
                    valido = False
                    break
                tiene_especial = True
            else:
                valido = False
                break



        if tiene_numero and tiene_letra and tiene_especial and valido:
            print("Contraseña válida")
        else:
            print("Contraseña inválida.")
    except:
        print("Ocurrió un error")

    print(f"{contraseña}")
cond1 = False
cond2 = False
cond3 = False
cond4 = False
cond5 = False
cond6 = False

cont_simbolos = 0

while True:
    #Condición 1 
    contraseña = input("Ingrese su contraseña: ")

    if len(contraseña) >= 8 or len(contraseña) <= 16:
        cond1 = True
    for i in contraseña:
    #condición 2
        if i in "0123456789":
            cond2 = True
    #condicion 3
        if i in "qwertyuiopasdfghjklñzxcvbnm":
            cond3 = True
    #condición 4
        if i in "_-*!#$?.%":
            cont_simbolos += 1
        if cont_simbolos <= 1:
            cond4 = True
    #Condición 5
        if i not in " ":
            cond5 = True
    #Condición 6
        if contraseña[-1] not in "_-*!#$?.%":
            cond6 = True
    if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
        print("Contraseña válida")
        break
    else:
        print("Contraseña invalida.")
        #  if cond1 == False:
        #   print("")
    
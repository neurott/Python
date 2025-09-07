cond1 = False
cond2 = False
cond3 = False
cond4 = False
cond5 = False
cond6 = False
cont_simbolos = 0

while True:
    #condición 1
    contrasenna = input("Ingrese contraseña: ")
    if len(contrasenna) >= 8 and len(contrasenna) <= 16:
        cond1 = True
            
    for _ in contrasenna:
        #condición 2
        if _ in '0123456789':
            cond2 = True
  
        #condición 3
        if _ in 'qwertyuiopasdfghjklñzxcvbnm':
            cond3 = True

        #condición 4
        if _ in '-_*.!?#$%':
            cont_simbolos +=1
        if cont_simbolos <= 1:
            cond4 = True
            
        #condición 5
        if _ not in ' ':
            cond5 = True
            
        #condicion 6
        if contrasenna[-1] not in '-_*.!?#$%':
            cond6 = True       
        

    if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
        print("Contraseña válida.")
        break
    else:
        if cond1 == False:
            print("La contraseña debe ser de mínimo 8 caracteres y máximo 16.")
        if cond2 == False:
            print("La contraseña debe contener al menos un número.")
        if cond3 == False:
            print("La contraseña debe contener al menos una letra.")
        if cond4 == False:
            print("La contraseña debe tener como máximo un caracter especial.")
        if cond5 == False:
            print("La contraseña no puede tener espacios en blanco")
        if cond6 == False:
            print("La contraseña no puede terminar con un caracter especial")  
        print("Reintente.")
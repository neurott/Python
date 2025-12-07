from random import randint

dado1 = randint(1,6)
dado2 = randint(1,6)
suma = dado1 + dado2


while True:
    flag = True

    i1 = int(input('Primer inteno para adivinar la suma de los dados: '))
    if 12 <i1 or i1< 2:
        print('Error, la suma de los dados no puede ser menor a 2 o mayor a 12.')
        flag = False

    if flag:
        if suma == i1:
            print('Adivinaste la suma!.')
            flag = False
        elif suma % 2 == 0  :
            print('Incorrecto,Una pista: la suma de los número es par.')
        else:
            print('Incorrecto,Una pista: la suma de los números es impar.')

   
    if flag:
        i2 = int(input('Intente por segunda vez: '))

        if 12 < i2 or i2 < 2:  
            print('Error, la suma de los dados no puede ser menor a 2 o mayor a 12.')
            flag = False
        elif i2 == suma:
            print('Adivinaste la suma!.')
        else:
            print('No adivinaste, la suma secreta')
            print('El número era:', suma)
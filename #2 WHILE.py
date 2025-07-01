#Escribe un programa que eprmita generar la tabla de multiplicar de un número entero
#positivo N,comenzando desde 1.
#Si el usuario escribe un número incorrecto, el prgorama no se ejecuta. En cambio,
#pregunta de nuevo por la ifnormación hasta que el dato ingresado sea correcto.
comprobar = True

while comprobar == True:
    try:
        n = int(input("Ingrese un número entero positivo: "))
        if n > 0:
            i = 1
            while i < 11:
                print(f"{n} x {i} = {n*i}")
                i += 1
            comprobar = False
        else:
            print("El número ingresado no es correcto. Inténtelo nuevamente")
    except ValueError:
        print("Ingrese un número, no letras.")
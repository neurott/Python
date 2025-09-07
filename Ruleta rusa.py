#While te odio con toda mi alma porfavor no me tortures mas 
import random
usuario = None
edad = None
contador = 0

while True:
    
    print ("-----------------------------------")
    print ("|                                 |")
    print ("|     <---RULETA 🔫 RUSA--->      |")
    print ("|                                 |")
    print ("|        1) JUGAR                 |")
    print ("|        2) REGISTRARSE           |")
    print ("|        3) SALIR                 |")
    print ("|                                 |")
    print ("|---------------------------------|")

    menu = int(input("Ingrese a una de las opciones ingresando un numero: "))
    if menu == 1:
            while True:
                if usuario != None:
                    print (f"!Bienvenido {usuario}¡ ¿Listo para jugar? (Cantidad de dinero = ${contador})")
                    print ("  1) JUGAR ")
                    print ("  2) SALIR ")
                    menu2 = int(input("Ingrese a una de las opciones ingresando un numero: "))
                    if menu2 == 1:
                        lucky = random.randint(1,100)
                        if lucky >= 50:
                            contador += 100
                            print ("---!!BANG¡¡...SOBREVIVISTE AL DUELO---")
                            print ("(GANASTE $100)")
                
                
                        else:
                            usuario = None
                            contador = 0
                            print ("---!!BANG¡¡...NO SOBREVIVISTE AL DUELO---")
                            print ("---GAME OVER---")

                            break
                    if menu2 == 2:
                        print ("---Saliendo del segundo menu---")
                        break
                else:
                    print ("---Primero debes de ingresar un nuevo usuario---")
                    break
                
                    

    elif menu == 2:
            usuario = input("Ingresa tu nombre: ")        
            edad = int(input("Ingresa tu edad: "))
            if edad >= 18:
                print ("---Registro de usuario exitoso---")

            else:
                usuario = None
                edad = None
                print ("---Usted no cumple con la edad requerida para poder entrar (SOLO PARA +18)---")
        

    elif menu == 3:
        print ("---¿Estas seguro que quieres salir del juego?---")
        print ("    1) SI")
        print ("    2) NO")
        D = int(input("Ingrese a una de las opciones ingresando un numero: "))
        if D == 1:
             exit("---Saliendo del juego---")
        elif D == 2:
             print ("---Volviendo al juego---")
        else:
             print ("Ingrese uno de los numeros que salga en pantalla...")
import random 
#Número aleatorio entre 1 y 50
numero_secreto = random.randint(1,50)
intentos = 5

print("¡Bienvenido al juego de las adivinanzas!")
print(f"Estoy pensando entre un numero entre 1 y 50. Tienes {intentos} intentos para adivinarlo.")

while intentos > 0:
    #Pide al usuario un intento
    intento = input(f"Te quedan {intentos} intentos. Introduce tu número: ")
    
    try:
        #Intenta convertir la entrada a un número entero
        intento = int(intento)

        #Compara el intento con el número secreto
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta con un número mayor.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta con un número menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
            break #Sale del bucle si adivina correctamente
    except ValueError:
        print("¡ERROR! Debes introducir un número válido.")
    
    #Disminuye el número de intentos después de cada intento
    intentos -= 1

#Si los intentos se acaban sin adivinar, se muestra el número secreto

if intentos == 0:
    print(f"Lo siento, se te acabaron los intentos. El núemro secreto era {numero_secreto}.")
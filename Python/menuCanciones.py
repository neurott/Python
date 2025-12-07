#CREAR UN MENÚ PARA UNA LISTA DE CNACIONES
#LA OPCIÓN 1 AGREGA CANCIONES
#LA OPCIÓN 2 ELIMINA UNA CANCIÓN EN BASE A SU POSICIÓN
#LA OPCIÓN 3 MUESTRA TODAS LAS CANCIONES
#LA OPCION 4 SALIR
canciones = []
while True:
    print("\nMENUUUUU")
    print("1. Agrega canciones")
    print("2. Elimina una canción en base a su posición")
    print("3. Muestra todas las canciones")
    print("4. Salir")
    try:
        op = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Ingresa un número entero positivo (1-5)")
    try:
        if op == 1:
           cancion = input("Escribe aquí la canción que deseas agregar a la lista: ")
           canciones.append(cancion)
           print(f"\nSe agregó la canción: {cancion}")
        elif op == 2:
            print("Tus canciones: ")
            contador = 1
            for i in range (len(canciones)):
                print(f"{contador} {canciones[i]}.mp3")
                contador += 1
                try:
                    pos = int(input("\n¿Qué canción deseas eliminar? (0 PARA SALIR): "))
                    if pos == 0:
                        print("No se eliminó ninguna canción")
                    elif 1 <= pos <= len(canciones):
                        eliminada = canciones.pop(pos-1)
                        print(f"Canción {eliminada} eliminada...")
        
                    else:
                        print("OPCIÓN INVÁLIDA")
                except:
                    print("El número no existe en la lista...")              
        elif op == 3: # AQUÍ USO UN FO
            if len(canciones) <= 0:
                print("\nTu lista esta vacía")
            else:
                print(f"Las canciones que se encuentran en tu lista son {canciones}")
        elif op == 4:
            break
    except ValueError:
        print("Opción no válida")
#Diccionario de jugadores
jugadores = {}
#Función para validar num camiseta
def validar_numero(numero):
    return 1<= numero <= 99

#Función para ingresar nuevo jugador
def ingresar_jugador():
    nombre = input("Inrgese el nombre del jugador: ")
    if nombre in jugadores:
        print("El jugador ya existe!")
        return
    
    posicion = input("Ingrese la posición (Delantero, Defensor, Centrocampo, Portero): ").capitalize()
    if posicion not in ["Delantero", "Defensor", "Centrocampo", "Portero"]:
        print("Posición no válida.")
        return
    
    numero = int(input("Ingrese el número de camiseta (1-99): "))
    if not validar_numero(numero):
        print("Número de camiseta no válido.")
        return
    
    jugadores[nombre] = {"Posición": posicion, "Número": numero}
    print(f"Jugador {nombre} ingresado con éxito!")

#Función para buscar un jugador
def buscar_jugador():
    nombre = input("Ingrese el nombre del jugador a buscar: ")
    if nombre in jugadores:
        datos = jugadores[nombre]
        print(f"Jugador encontrado: \nNombre: {nombre}\nPosición: {datos['Posición']}\nNúmero de camiseta: {datos['Número']}")
    else:
        print("El jugador no se encuentra registrado")

#Función para eliminar un jugador
def eliminar_jugador():
    nombre = input("Ingrese el nombre del jugador a eliminar: ")
    if nombre in jugadores:
        del jugadores[nombre]
        print(f"Jugador {nombre} eliminado con éxito!")
    else:
        print("No se pudo eliminar el jugador. Jugador no existe")

#Función principal o main
def main():
    while True:
        print("\nMenú Principal")
        print("1. Ingresar jugador")
        print("2. Buscar jugador")
        print("3. Eliminar jugador")
        print("4. Salir")
        
        opcion = input("Ingrese opción (1-4): ")

        if opcion == "1":
            ingresar_jugador()
        elif opcion == "2":
            buscar_jugador()
        elif opcion == "3":
            eliminar_jugador()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida.")

#Ejecutar el programa
main()

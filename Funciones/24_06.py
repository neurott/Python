#Totem
#Lo va a subir al ava.
def comprar_entrada(stock, compradores_partido):
    print("\nComprar entradas para partido")
    nombre = input("Nombre del comprador: ")
    if nombre in compradores_partido:
        print("El nombre ya existe, ya compró una entrada")
        return stock
    
    print("Seleccione partido: ")
    print("1. Clásico día domingo (150 Entradas)")
    print("2. Final día miércoles (180 entradas)")
#Esto no lo puso con int
    opcion = input("Partido 1 o 2: ")
    if opcion not in ('1','2'):
        print("Error: Opción de partido no válida")
        return stock

    key = "p" + opcion
    if stock[key] <= 0:
        print(f"Error no hay entradas disponibles: {opcion}")
        return stock
    stock[key] -= 1

    compradores_partido[nombre] = opcion
    print(f"Entrada registrada correctamente en el partido: {opcion}! Stocks restantes:\n"
          f" Partido 1 (Domingo): {stock["p1"]}\n"
          f" Partido 2 (Miércoles): {stock['p2']}")
    return stock
    
def cambio_partido(stock, compradores_partido):
    print("\nCambio de paritido")
    nombre = input("Nombre del comprador: ").strip()
    if nombre not in compradores_partido:
        print("Error: comprador no encontrado.")
        return stock
    
    actual = compradores_partido[nombre]
    nuevo = "2" if actual == "1" else "1"
    key_nuevo = 'p' + nuevo
    if stock[key_nuevo] <= 0:
        print(f"Error: no hay stock disponible para el partido {nuevo}.")
        return stock
    
    confirm = input(f"Cambiar de partido {actual} a {nuevo}? (Si/No): ").strip().upper()
    if confirm != 'S':
        print("Cambio cancelado")
        return stock
    
    key_actual = 'p' + actual
    stock[key_actual] += 1
    stock[key_nuevo] -= 1
    compradores_partido[nombre] = nuevo
    print(f"Cambio exitoso. Ahora está en partido {nuevo}.")
    return stock



def mostrar_stock(stock):
    print("\nStock partidos")
    vendidos_p1 = 150 - stock["p1"]
    vendidos_p2 = 180 - stock["p2"]
    print(f"Partido 1 (Domingo): Disponibles {stock["p1"]}, Vendidas {vendidos_p1}")
    print(f"Partido 2 (Miércoles): DIsponibles {stock["p2"]}, Vendidas {vendidos_p2}")

def main():
    stock = {"p1": 150, "p2": 180}
    compradores_partido = {}

    while True:
        print("\nMenú Principal")
        print("1. Comprar entrada para partido")
        print("2. Cambio de partido")
        print("3. Mostrar stock de partidos")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            stock = comprar_entrada(stock,compradores_partido)
        elif opcion == 2:
            stock = cambio_partido(stock, compradores_partido)
        elif opcion == 3:
            mostrar_stock(stock)
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción inválida....")

main()
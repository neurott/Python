def comprar_entrada(stock, compradores_partido):
    print("\n-- Comprar entrada para partido --")
    nombre = input("Nombre del comprador: ").strip()
    if nombre in compradores_partido:
        print("Error: el nombre ya existe.")
        return stock

    print("Seleccione partido:")
    print("1. Clásico Día Domingo (150 entradas)")
    print("2. Final Día Miércoles (180 entradas)")
    opcion = input("Partido (1 ó 2): ").strip()
    if opcion not in ('1', '2'):
        print("Error: opción de partido inválida.")
        return stock

    key = 'p' + opcion
    if stock[key] <= 0:
        print(f"Error: no hay stock disponible para el partido {opcion}.")
        return stock
    stock[key] -= 1

    compradores_partido[nombre] = opcion
    print(f"Entrada registrada en partido {opcion}! Stock restantes:\n"
          f"  Partido 1 (Domingo): {stock['p1']}\n"
          f"  Partido 2 (Miércoles): {stock['p2']}")
    return stock


def cambio_partido(stock, compradores_partido):
    print("\n-- Cambio de partido --")
    nombre = input("Nombre del comprador: ").strip()
    if nombre not in compradores_partido:
        print("Error: comprador no encontrado.")
        return stock

    actual = compradores_partido[nombre]
    nuevo = '2' if actual == '1' else '1'
    key_nuevo = 'p' + nuevo
    if stock[key_nuevo] <= 0:
        print(f"Error: no hay stock disponible para el partido {nuevo}.")
        return stock

    confirm = input(f"Cambiar de partido {actual} a {nuevo}? (S/N): ").strip().upper()
    if confirm != 'S':
        print("Cambio cancelado.")
        return stock

    key_actual = 'p' + actual
    stock[key_actual] += 1
    stock[key_nuevo] -= 1
    compradores_partido[nombre] = nuevo
    print(f"Cambio exitoso. Ahora está en partido {nuevo}.")
    return stock


def mostrar_stock(stock):
    print("\n-- Stock de Partidos --")
    vendidos_p1 = 150 - stock['p1']
    vendidos_p2 = 180 - stock['p2']
    print(f"Partido 1 (Domingo): Disponibles {stock['p1']}, Vendidas {vendidos_p1}")
    print(f"Partido 2 (Miércoles): Disponibles {stock['p2']}, Vendidas {vendidos_p2}")


def main():
    stock = {'p1': 150, 'p2': 180}
    compradores_partido = {}

    while True:
        print("\nTOTEM AUTOATENCIÓN ESTADIO GOLAZO")
        print("1.- Comprar entrada para partido.")
        print("2.- Cambio de partido.")
        print("3.- Mostrar stock de partidos.")
        print("4.- Salir.")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            stock = comprar_entrada(stock, compradores_partido)
        elif opcion == '2':
            stock = cambio_partido(stock, compradores_partido)
        elif opcion == '3':
            mostrar_stock(stock)
        elif opcion == '4':
            print("\nPrograma terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

main()
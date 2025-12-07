lista_compradores = []


def comprar_entrada(nombre, tipoEntrada, codigoConfirmacion):
    buyer = {
        "nombre": nombre,
        "tipoEntrada": tipoEntrada,
        "codigoConfirmacion": codigoConfirmacion
    }

    is_valido = True

    for k, v in buyer.items():
        if k == "nombre":
            for existing_buyer in lista_compradores:
                if existing_buyer["nombre"] == v:
                    print(f"Error el nombre {v} ya esta registrado.")
                    is_valido = False
                    break
        if k == "tipoEntrada":
            if v.lower() in ["G", "V"]:
                is_valido = True
            else:
                is_valido = False
                print(f"Solo se permite el tipo de entrada 'G' (General) O 'V' (VIP)")

        if k == "codigoConfirmacion":
            if len(codigoConfirmacion) >= 6 and any(letra.isupper() for letra in codigoConfirmacion) and any(c.isdigit() for c in codigoConfirmacion) and not any(c.isspace() for c in codigoConfirmacion):
                is_valido = True

    if is_valido:
        lista_compradores.append(buyer)
        print("Entrada comprada con éxito")
    else:
        print("ERROR AL COMPRAR LA ENTRADA")


def menu():
    print("~"*20)
    print("\nMenú Principal")
    print("Concierto de Trap con el Conejo Simpático")
    print("1. Comprar entrada")
    print("2. Consultar comprador")
    print("3. Cancelar compra")
    print("4. Salir")


def main():
    while True:
        menu()
        try:
            op = int(input("OPCIÓN: "))
            match op:
                case 1:
                    nombre = input("INGRESA UN NOMBRE: ")
                    tipoEntrada = input("INGRESA UN TIPO DE ENTRADA: ")
                    codigoConfirmacion = input(
                        "INGRESAR CÓDIGO DE CONFIRMACIÓN: ")

                    comprar_entrada(nombre, tipoEntrada,
                                    codigoConfirmacion)

                case 4:
                    print("SALIENDO.....")
                    break
        except Exception as e:
            print(F"ERROR {e}")


main()

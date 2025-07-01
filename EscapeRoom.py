PRIMER_ACERTIJO_RESPUESTA = "579"
SEGUNDO_ACERTIJO_RESPUESTA = "888+88+8+8+8"
TECER_ACERTIJO_RESPUESTA = "6"

PRIMER_ACERTIJO_PISTA = "Es el resultado de sumar 123 y 456"
SEGUNDO_ACERTIJO_PISTA = "Usando sólo la suma, agregue ocho 8 para obtener el número 1.000"
TERCER_ACERTIJO_PISTA = "Soy un número par entre 1 y 10, y el doble de 3. ¿Quién soy?"

def resolver_primer_acertijo():
    
    print("\n **Primer acertijo**: Para desbloquear el candado, necesitas un código de 3 dígitos.")
    print(f'Pista: {PRIMER_ACERTIJO_PISTA} ')

    while True:
        respuesta = input('Introduce el código')
        if respuesta == PRIMER_ACERTIJO_RESPUESTA:
            print("¡Correcto! El candado se abre.")
            break
        else:
            print("Respuesta incorrecta.")


def resolver_segundo_acertijo():
    print("\n **Segundo acertijo**: Resuelve este desafío lógico para avanzar.")
    print(f'Pista: {SEGUNDO_ACERTIJO_PISTA}')

    while True:
        respuesta = input('Introduce la operación: ').replace(' ', "")
        if respuesta == SEGUNDO_ACERTIJO_RESPUESTA:
            print("¡Correcto!")
            break
        else:
            print("Incorrecto jaja")

def resolver_tercer_acertijo():
    print("\nLa salida está bloqueda por una caja fuerte")
    print(f'La caja tiene un acertijo: {TERCER_ACERTIJO_PISTA}')

    while True:
        respuesta = input('Introduce el número: ')
        if respuesta == TECER_ACERTIJO_RESPUESTA:
            print("Correcto")
            break
        else:
            print("Incorrecto")

def escape_room():
    print("Bienvendio al Escape Room!")
    print("Estás atrapado en una habitación y ves una puerta cerrada con un candado.")
    resolver_primer_acertijo()
    resolver_segundo_acertijo()
    resolver_tercer_acertijo()
    print("\nFelicitaciones! Has escapado del Escape room")

if __name__ == '__main__':
    escape_room()


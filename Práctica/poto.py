contactos = {}

def mostrar_menu():
    print("\nMenú")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Salir")

def agregar_contactos():
    nombre = input("Nombre: ")
    telefono = input("Télefono: ")
    contactos[nombre] = telefono
    print("Contacto agregado extisoamente")

def mostrar_contactos():
    if not contactos:
        print("No existe ningun contacto registrado...")
    else:
        print("\nLista de contactos: ")
        for nombre, telefono in contactos.items():
            print(f"{nombre} : {telefono}")

def main():
    while True:
        mostrar_menu()
        op = int(input("Seleccione una opción (1-3): "))

        if op == 1:
            agregar_contactos()
        elif op == 2:
            mostrar_contactos()
        elif op == 3:
            print("Saliendo...")
            break
        else:
            print("ERROR")
main()
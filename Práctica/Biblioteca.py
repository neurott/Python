def agregar_libro():
    titulo = input("Ingrese el título: ").capitalize().strip()
    autor = input("Ingrese el autor: ").capitalize().strip()
    while True:
        try:
            año = int(input("Ingrese el año de publicación: "))
            if año <= 0:
                print("El año debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Debe ingresar un número válido")
    
    genero = input("Ingrese el género: ").capitalize().strip()

    if titulo in biblioteca:
        print("Este libro ya existe en la biblioteca")
        return
    
    biblioteca[titulo] = {
        "Autor": autor,
        "Año": año,
        "Género": genero
    }
    print(f"\nSe agregó el libro: {titulo} con éxito")


def ver_libros():
    if len(biblioteca) == 0:
        print("La biblioteca esta vacía...")
    else:
        print("\nLibros en la biblioteca:")
        for titulo, datos in biblioteca.items():
            print(f"Título: {titulo}")
            print(f"Autor: {datos['Autor']}")
            print(f"Año: {datos['Año']}")
            print(f"Género: {datos['Género']}")

biblioteca = {}

def main():
    while True:
        print("\nMenú")
        print("1. Agregar un libro")
        print("2. Ver todos los libros")
        print("3. Salir")

        op = int(input("Seleccione una opción: "))
    
        if op == 1:
            agregar_libro()
        elif op == 2:
            ver_libros()
        elif op == 3:
            print("Saliendo...")
            break
main()

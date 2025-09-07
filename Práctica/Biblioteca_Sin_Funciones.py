#Ejercicio: Menú interactivo para agregar libros a la biblioteca. Enunciado:
#Crea un programa que permita a un usuario gestionar una biblioteca de libros. El programa debe tener un menú con las siguientes opciones:
#Agregar un libro: El usuario ingresará el título, el autor, el año y el género del libro.
#Ver todos los libros: El programa mostrará todos los libros en la biblioteca (diccionario).
#Salir: Termina el programa.
#El diccionario biblioteca debe almacenar los libros como clave (el título del libro) y los valores como otro diccionario que contenga:
#Autor
#Año de publicación
#Género literario
biblioteca = {}

while True:
    print("\nMenú")
    print("1. Agregar un libro")
    print("2. Ver todos los libros")
    print("3. Salir")

    try:
        op = int(input("Seleccione una opción: "))
    except:
        print("ERROR")
        continue

    if op == 1:
        titulo = input("Título: ").capitalize()
        autor = input("Autor: ").capitalize()
        año = int(input("Año de publicación: "))
        genero = input("Género: ").capitalize()
        
        biblioteca[titulo] = {
            "Autor": autor,
            "Año": año,
            "Género": genero
        }
        print(f"\nSe agregó el libro: {titulo} con éxito.")

    elif op == 2:
        if len(biblioteca) == 0:
            print("La biblioteca esta vacía...")
        else:
            print("\nLibros en la biblioteca: ")
            
            for titulo, datos in biblioteca.items():
                print(f"\nTítulo: {titulo}")
                print(f"Autor: {datos['Autor']}")
                print(f"Año: {datos['Año']}")
                print(f"Género: {datos['Género']}")
    elif op == 3:
        print("Saliendo...")
        break
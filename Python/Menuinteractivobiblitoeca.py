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
        op = int(input("Seleccione una opción (1-3):"))

    except:
        print("Error")
        continue

    if op == 1:
        titulo = input("Título: ")
        autor = input("Autor: ")
        año = int(input("Año de publicación: "))
        genero = input("Género: ")

        biblioteca[titulo] = {
            "autor": autor,
            "año": año,
            "genero": genero
        }
        print("\nSe agregó el libro con éxito.")

    elif op == 2: #Se me borraron los comentarios?
        if len(biblioteca) == 0:
            print("Biblioteca esta vacía")
        else:
            print("\nLibros en biblioteca: ")
            for titulo, datos in biblioteca.items():
                print(f"\nTítulo: {titulo}")
                print(f"Autor: {datos['autor']}")
                print(f"Año: {datos['año']}")
                print(f"Género: {datos['genero']}")
    elif op == 3:
        break
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
    print("\nMenú interactivo")
    print("1. Agregar un libro")
    print("2. Ver todos los libros")
    print("3. Salir")

    try:
        op = int(input("Seleccione una opción (1-3): "))
    except:
        print("Error")
        continue
#Revisar if 1 en la casa    
    if op == 1:
        titulo = input("Título: ")
        autor = input("Autor: ")
        try:
            año = int(input("Año de publicacon: "))

        except ValueError:
            print("Error")
            continue
        genero = input("Género: ")

        biblioteca[titulo] = {
            "autor": autor,
            "año": año,
            "género": genero
        }
        print("\nSe agregó el libro con éxito")

    elif op == 2:
        #if not biblioteca:
        if len(biblioteca) == 0:
            print("Biblioteca vacía...")
        else:
            print("\nLibros que se encuentran en la biblioteca:")
            #print(biblioteca)
            for titulo, datos in biblioteca.items():
                print(f"\nTítulo: {titulo}")
                print(f"Autor: {datos['autor']}")
                print(f"Año: {datos['año']}")
                print(f"Género: {datos['género']}")
    elif op == 3:
        print("Saliendo....")
        break
    else:
        print("ERRORRR")



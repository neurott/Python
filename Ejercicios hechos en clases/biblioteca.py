#crear diccionario vacío
biblioteca = {}

#agregamos libros con diccionarios
biblioteca["Don Quijote"] = {
    "autor": "Miguel de Cervantes",
    "año": 1605,
    "género": "Novela"
}

biblioteca["La Odisea"] = {
    "autor": "Homero",
    "año": -800,
    "género": "Épica"
}

biblioteca["1984"] = {
    "autor": "George Orwell",
    "año": 1949,
    "género": "Distopía"
}

#imprimir todo el diccionario
print("Diccionario completo: ")
print(biblioteca)

#imprimir solo claves (títulos)
print("\nTítulos de los libros:" )
print(biblioteca.keys())

#imprimir sólo los valores (datos de libros)
print("\nDatos de los libros: ")
print(biblioteca.values())

#imprimir las parejas (clave, valor)
print("\nLibros con sus datos (items): ")
print(biblioteca.items())

#obtener el autor de "Don Quijote con get()"
autor_don_quijote = biblioteca.get("Don Quijote", {}).get("autor", "Autor no encontrador")
print(f"\nAutor de Don Quijote: {autor_don_quijote}")

#eliminar el libro 1984
libro_eliminado = biblioteca.pop("1984", None)
print(f"\nLibro eliminado: {libro_eliminado}")
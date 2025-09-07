biblioteca = {}
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


#imprimir solo claves (títulos)
print("\nTítulos de los libros: ")
print(biblioteca.keys())

#imprimir los valores (datos de libros)
print("\nVALORES: ")
print(biblioteca.values())

#Imprimir las parejas (clave:valor)
print("\nLibros con sus datos:")
print(biblioteca.items())

#Eliminar un elemento de la biblioteca

borrar_libro = biblioteca.pop("1984", None)
print(f"\nLibro eliminado: {borrar_libro}")
print("\nBibloteca: ", biblioteca)
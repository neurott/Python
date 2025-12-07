def mostrar_menu():
    print("\n--- MENÚ DE COMPRAS ---")
    print("1. Agregar artículo")
    print("2. Ver lista de compras")
    print("3. Eliminar artículo")
    print("4. Salir")

def agregar_articulo(lista):
    articulo = input("¿Qué artículo quieres agregar? ").strip()
    if articulo:
        lista.append(articulo)
        print(f"Artículo '{articulo}' agregado a la lista.")
    else:
        print("No se ingresó ningún artículo.")

def ver_lista(lista):
    contador = 0
    if lista:
        print("\nArtículos en la lista:")
        for item in lista:
            contador += 1
            print(f"{contador}. {item}")
        
    else:
        print("La lista de compras está vacía.")

def eliminar_articulo(lista):
    ver_lista(lista)
    if lista:
        articulo = input("Nombre del artículo a eliminar: ").strip()
        if articulo in lista:
            lista.remove(articulo)
            print(f"Artículo '{articulo}' eliminado.")
        else:
            print("Ese artículo no está en la lista.")

# Programa principal
lista_compras = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_articulo(lista_compras)
    elif opcion == "2":
        ver_lista(lista_compras)
    elif opcion == "3":
        eliminar_articulo(lista_compras)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intenta nuevamente.")
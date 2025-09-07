def mostrar_menu():
    print("\nMenú")
    print("1. Agregar articulos a la lista. ")
    print("2. Ver articulos de la lista.")
    print("3. Eliminar articulos de la lista.")
    print("4. Salir.")

def agregar_articulo(lista):
    articulo = input("¿Qué artículo desea agregar?: ").strip().lower()
    if articulo:
        lista.append(articulo)
        print(f"El artículo: {articulo} se agregó con éxito")
    else:
        print("ERROR; intente denuevo o escriba algo")

def ver_lista(lista):
    contador = 0
    if lista:
        print("\nLista: ")
        for item in lista:
            contador += 1
            print(f"{contador}. {item}")
    else:
        print("La lista esta vacía.")

def eliminar_articulo(lista):
    ver_lista(lista)
    if lista:
        articulo = input("Ingrese el articulo que desea eliminar: ").strip().lower()
        if articulo in lista:
            lista.remove(articulo)
            print(f"Se elimino el artículo: {articulo} de la lista..")
        else:
            print("No se encuentra en la lista de compras.")

lista_compras= []
def main():
    while True:
        mostrar_menu()
        try:
            op = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Seleccione una opción o ingrese un número entero (1-4)")
        if op == 1:
            agregar_articulo(lista_compras)
        elif op == 2:
            ver_lista(lista_compras)
        elif op == 3:
            eliminar_articulo(lista_compras)  
        elif op == 4:
            print("Saliendo...")
            break
        else:
            print("error")

main()



    

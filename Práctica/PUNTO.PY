personas = {}

def ingresar_persona():
    print("\nIngresar una nueva persona...")
    rut = input("Ingrese el rut: ")
    if rut in personas:
        print("El rut ya esta registrado")
        return
    
    nombre = input("Ingrese el nombre: ").capitalize()
    apellido = input("Ingrese apellido: ").capitalize()
    #Bucle para controlar la edad con excepciones
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad <= 0:
                print("La edad debe ser un número positivo")
                continue
            break
        except ValueError:
            print("ERROR: Debe ingresar un número válido.")
    #Luego nacionalidad
    nacionalidad = input("Ingrese la nacionalidad: ").capitalize()

    personas[rut] = {'nombre': nombre, 'apellido': apellido, "edad": edad, 'nacionalidad': nacionalidad}
    print("Persona ingresada exitosamente...")

def eliminar_persona():
    print("\nEliminar persona")
    rut = input("Ingrese el rut de l-a persona a eliminar: ")
    if rut in personas:
        del personas[rut]
        print(f"Persona con el rut: {rut} ha sido eliminada")
    else:
        print("Rut no registrado en el sistema.")
#
def consultar_persona():
    print("\nConsultar persona")
    rut = input("Ingrese el rut que desea consultar: "  )
    if rut in personas:
        persona = personas[rut]
        print(f"Nombre: {persona['nombre']}")
        print(f"Apellido: {persona['apellido']}")
        print(f"Edad: {persona['edad']}")
        print(f"Nacionalidad: {persona['nacionalidad']}")
    else:
        print("RUT NO REGISTRADO")
#
def listar_personas():
    print("\nListar todas las personas: ")
    if not personas:
        print("No hay personas registradas")
    else:
        for rut, datos in personas.items():
            print(f"Rut: {rut}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Apellido: {datos['apellido']}")
            print(f"Edad: {datos['edad']}")
            print(f"Nacionalidad: {datos['nacionalidad']}")
            print("~"*20)

def main():
    while True:
        print("\nMenú")
        print("1. Ingresar persona")
        print("2. Eliminar persona")
        print("3. Consultar persona")
        print("4. Listar todas las personas")
        print("5. Salir")

        try:
            op = int(input("Seleccione una opción: "))

            if op == 1:
                ingresar_persona()
            elif op == 2:
                eliminar_persona()
            elif op == 3:
                consultar_persona()
            elif op == 4:
                listar_personas()                
            elif op == 5:
                print("Saliendo....")
                break
            else:
                print("Opcion no válida, intente nuevamente.")
        except ValueError:
            print("ERROR")
main()
personas = {}

def ingresar_persona():
    print("\nIngresar nueva persona")
    rut = input("Ingrese el rut de la persona: ")
    if rut in personas:
        print("La persona con ese rut ya esta registrada")
        return
    
    nombre = input("Ingrese el nombre:").capitalize().strip()
    apellido = input("Ingrese el apellido: ").capitalize().strip()

    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad <= 0:
                print("La edad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")

    nacionalidad = input("Ingrese la nacionalidad: ")

    personas[rut] = {
        "Nombre" : nombre,
        "Apellido": apellido,
        "Edad" : edad,
        "Nacionalidad": nacionalidad,
    }
    print("Persona ingresada exitosamente")

def eliminar_persona():
    print("")
    rut = input("Ingrese el rut de la persona que desea eliminar: ")
    if rut in personas:
        del personas[rut]
        print(f"Persona con RUT {rut} eliminada exitosamente")

def consultar_persona():
    print("")
    rut = input("Ingrese el RUT de la persona a consultar: ")
    if rut in personas:
        persona = personas[rut]
        print(F"Nombre: {persona['Nombre']}")
        print(f"Apellido: {persona['Apellido']}")
        print(f"Edad: {persona['Edad']}")
        print(F"Nacionalidad: {persona['Nacionalidad']}") 
    else:
        print("No se encontró un persona con ese RUT.")

def listar_personas():
    print("listar")
    if not personas:
        print("No hay personas registradas")
    else:
        for rut, datos in personas.items():
            print(f"RUT: {rut}")
            print(f"Nombre: {datos['Nombre']}")
            print(f"Apellido: {datos['Apellido']}")
            print(f"Edad: {datos['Edad']}")
            print(f"Nacionalidad: {datos['Nacionalidad']}")

def main():
    while True:
        print("\n--- MENÚ ---")
        print("1) Ingresar persona")
        print("2) Eliminar persona")
        print("3) Consultar persona")
        print("4) Listar todas las personas")
        print("5) Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                ingresar_persona()
            elif opcion == 2:
                eliminar_persona()
            elif opcion == 3:
                consultar_persona()
            elif opcion == 4:
                listar_personas()
            elif opcion == 5:
                print("Hassta luego")
                break
            else:
                print("Opción no válida. Intente nuevamente")
        except ValueError:
            print("Por favor, ingrese una opción no válida.")

main()
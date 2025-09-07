# Diccionario para almacenar los datos de las personas
personas = {}

# Función para ingresar una nueva persona
def ingresar_persona():
    print("\n--- Ingresar nueva persona ---")
    rut = input("Ingrese el RUT de la persona: ")
    if rut in personas:
        print("¡La persona con ese RUT ya está registrada!")
        return
    
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    
    # Controlar la edad con excepciones
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
    numeroVuelo = input("Ingrese su número de vuelo: ")
    
    # Guardar los datos en el diccionario
    personas[rut] = {"nombre": nombre, "apellido": apellido, "edad": edad, "nacionalidad": nacionalidad, "vuelo": numeroVuelo}
    print("Persona ingresada exitosamente.")

# Función para eliminar una persona por RUT
def eliminar_persona():
    print("\n--- Eliminar persona ---")
    rut = input("Ingrese el RUT de la persona a eliminar: ")
    if rut in personas:
        del personas[rut]
        print(f"Persona con RUT {rut} eliminada exitosamente.")
    else:
        print("No se encontró una persona con ese RUT.")

# Función para consultar los datos de una persona por RUT
def consultar_persona():
    print("\n--- Consultar persona ---")
    rut = input("Ingrese el RUT de la persona a consultar: ")
    if rut in personas:
        persona = personas[rut]
        print(f"Nombre: {persona['nombre']}")
        print(f"Apellido: {persona['apellido']}")
        print(f"Edad: {persona['edad']}")
        print(f"Nacionalidad: {persona['nacionalidad']}")
        print(f"Número de vuelo: {persona['vuelo']}")
    else:
        print("No se encontró una persona con ese RUT.")

# Función para listar todas las personas registradas
def listar_personas():
    print("\n--- Listar todas las personas ---")
    if not personas:
        print("No hay personas registradas.")
    else:
        for rut, datos in personas.items():
            print(f"RUT: {rut}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Apellido: {datos['apellido']}")
            print(f"Edad: {datos['edad']}")
            print(f"Nacionalidad: {datos['nacionalidad']}")
            print(f"Número de vuelo: {datos['vuelo']}")
            print("-----------------------------")

# Función principal que muestra el menú y ejecuta las opciones
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
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese una opción válida.")
            
# Ejecutar el programa
main()

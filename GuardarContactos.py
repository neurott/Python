#DICCIONARIOS
#GUARDAR CONTACTOS DE CELULAR
#CREAR UN MENÚ QUE TENGA LAS SIGUIENTES OPCIONES
#AGREGAR UN CONTACTO NOMBRE:NUMERO
#MOSTRAR TODOS LOS CONTACTOS
#SALIR
contactos = {}

while True:
    print("\nMenú")
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Salir")

    try:
        op = int(input("Seleccione una opción (1-3):"))
    except:
        print("Error")
        continue

    if op == 1:
        nombre = input("Nombre: ")
       #número = int(input("Ingrese el número celular: "))
        telefono = input("Télefono: ")
        contactos[nombre] = telefono
        print("Contacto agregado exitosamente")

        #contactos[nombre] ={
       #    "nombre": nombre,
       #     "fono": número
       # }
        ## NO LO HIZO ASÍ
#Muestren algo, for, o contar algo
    elif op == 2:
        if not contactos:
            print("Esta vacía")
        else:
            print("\nLista de contactos")
        
        for nombre, telefono in contactos.items():
            print(f"{nombre}:{telefono}")
    elif op == 3:
        print("Saliendo....")
        break
    else:
        print("Error")




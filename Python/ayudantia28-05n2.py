#Hacer un menu de inscripcion a talleres
# cada taller tiene un cupo inicial de 10 personas
#Opción 1 inscribir a taller de programación
#Opción 2 inscribir a taller de base de datos
#Opción 3 inscribir a taller de costura
#Opción 4 ver todos los cupos disponibles
#Opción 5 Salir

#Cada opción tiene su propio menú con 2 opciones
#subopcion 1 Inscribir (se debe descontar un cupo, se debe mostar si no hay cupos)
#Subopcion 2 Volver al menu principal

cupos = 10
#cupos -= 1

while True:
    print('*** MENÚ PRINCIPAL ***')
    print("1. Inscribir a taller de programación.")
    print("2. Inscribir a taller de base de datos")
    print("3. Inscribir a taller de costura")
    print("4. Ver todos los cupos disponibles")
    print("5.Salir")
    
    try:
        op = int(input("Ingrese la opción: "))
        if op == 1:
            cupos -= 1
        elif op == 2:
            cupos -= 1
        elif op == '3':
            cupos -= 1x
        elif op == '4':
            print(cupos)
        else:
            print("caca")
    except ValueError:
        print("Opción no válida")
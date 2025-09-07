# EJERCICIO 1 NICOLÁS OLIVARES
# NO SUPE HACER EL CASO EN EL CUAL EL USUARIO INGRESARA UN STRING, CONTINUARA EN EL MISMO BUCLE
# 
contadorPMayor = 0
contadorPMenor = 0
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de libros prestados: "))
        for _ in range (cantidad):
            titulo = input("Ingrese el título del libro: ")
            prestamo = int(input(f'Ingrese los días de préstamo para "{titulo}": '))
            if prestamo > 15:
                print("Prestamo por más de 15 días")
                contadorPMayor += 1
                prestamoMayorAQuince = contadorPMayor
                continue
            #contador += 1
            elif prestamo < 15:
                print("Prestamo por 15 días o menos.")
                contadorPMenor += 1
                prestamoMenorAQuince = contadorPMenor
                continue
            else:
                print("Ingresa un número entero por favor.")
                
        print(f"\nSe registraron {prestamoMayorAQuince} libros con préstamo mayor a 15 días.")
        print(f"Se registraron {prestamoMenorAQuince} libros con préstamo menor a 15 días.")
        break
    
    except ValueError:
        print("OPCION NO VÁLIDA.. Debe ingresar un número entero...")                       
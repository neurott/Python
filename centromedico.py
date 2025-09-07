print("CENTRO MÉDICO PENELOPE")

rut=None
nombre=None
direccion=None
correo=None
edad=None
sexo=None
ps=None
registros=None

while True:
    try:
        print("1. Registrar al paciente")
        print("2. Atención al paciente")
        print("3.Consultar del datos del paciente")
        print("4. Salir")
        opcion = int(input("Ingrese su opción (1-4): "))

        if opcion == 1:
            while True:
                try:
                    rut = int(input("Ingrese el rut sin dígito verificador, ni puntos: "))
                    if rut>=5000000 and rut<= 99999999:
                        break
                    else:
                        print("Vuelve a ingresar, rut invalido.")
                except ValueError:
                    print("Vuelve a ingresar, rut invalido (except)")
            nombre = input("Ingrese el nombre del paciente: ")
            direccion =  input("Ingrese la dirección del paciente: ")
            contador_arrobas = 0
            while True:
                correo = input("Ingrese correo: ")
                for caracter in correo:
                    if caracter == "@":
                        contador_arrobas +=1
                if contador_arrobas == 0:
                    print("No contiene ningún arroba, vuelve ingresar. ")
                elif contador_arrobas == 1:
                    break
            while True:
                try:
                    edad = int(input("Ingrese la edad del paciente: "))
                    if edad >= 0 and edad <= 110:
                        break
                    else:
                        print("Edad invalida, vuelve a ingresar la edad.")
                except:
                    print("Dato mal ingresado, intente nuevamente")
            while True:
                sexo = input("Ingrese su sexo (F o M): ").lower()
                if sexo == "f" or sexo == "m":
                    break
                else:
                    print("Sexo invalido, intentelo nuevamente, ignrese un voiaslflasfd")
            while True:
                ps= input("Ingrese plan de salud (ISAPRE/FONASA): ").lower()
                if ps == "isapre" or ps =="fonasa":
                    break
                else:
                    print("Su plan de salud esta mal ingresado, intentelo denuevo")
        elif opcion == 2:
            while True:
                solicitar_rut = int(input("Ingrese el rut del paciente que viene a visitar: "))
                if rut != None:
                    if solicitar_rut== rut:
                        fecha= input("Ingrese fecha: ")
                        obs = input("Ingrese la observación: ")
                        registros = fecha + obs
                        break
                    elif solicitar_rut != rut:
                        print("PACIENTE NO ESTA REGISTRADO, SOLICITAR RUT NUEVAMENTE")
                elif rut == None:
                    print("No hay ningun paciente registrado...")
                    break
        elif opcion == 3:
            print("*******************")
            print("DATOS DEL PACIENTE")
            print(F"RUT: {rut}")
            print(f"NOMBRE: {nombre}")
            print(f"DIRECCIÓN: {direccion}")
            print(f"CORREO: {correo}")
            print(f"EDAD: {edad}")
            print(f"SEXO: {sexo}")
            print(F"PLAN DE SALUD: {ps}")
            print(f"REGISTROS: {registros}")
            print("*********************")
        elif opcion == 4:
            print("SALIENDO......")
            break
        else:
            print("Opción invalida. VUELVE A INGRESAR.")
    except:
        print("Opción invalida")        
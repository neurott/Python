#Prueba
 
print("Centro Médico DUOC")

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
        print("1.Registrar Paciente")
        print("2.Atención Paciente")
        print("3.Consultar Datos Paciente")
        print("4 Salir")

        opcion=int(input("Ingrese opcion :"))

        if opcion==1:
            while True:
                try:
                    rut=int(input("Ingrese rut sin dígito verificador ni puntos :"))
                    if rut>=5000000 and rut<= 99999999:
                        break
                    else:
                        print("Vuelve a ingresar,rut invalido")
                except:
                    print("Vuelve igresar,rut invalido")
            nombre=input("Ingrese nombre del paciente: ")
            direccion=input("Ingrese direccion del paciente: ")
            contador_de_arrobas=0
            while True:
                correo=input("Ingrese correo:")
                for caracter in correo:
                    if caracter =="@":
                        contador_de_arrobas+=1
                if contador_de_arrobas==0:
                    print("No contiene ningun arroba,vuelve a ingresar")
                elif contador_de_arrobas==1:
                    break
            while True:
                try:
                    edad=int(input("Ingrese edad del paciente : "))
                    if edad>=0 and edad<=110:
                        break
                    else:
                        print("Edad invalida,vuelva a ingresar")
                except:
                    print("Dato mal ingresado,vuelve a ingresar")
            while True:
                sexo=input("Ingrese sexo [f o m] :")
                if sexo=="F" or sexo =="f" or sexo=="M" or sexo=="m":
                    break
                else:
                    print("Sexo invalido,vuelva a ingresar")
            while True:
                ps=input("Ingrese plan de salud [ISAPRE/FONASA]: ")
                if ps=="ISAPRE" or ps=="FONASA":
                    break
                else:
                    print("Ps mal ingresado,vuelva a ingresar")
        elif opcion== 2:
                while True:
                    solicitar_rut=int(input("Ingrese rut del paciente que viene a visitar :"))
                    if rut!=None:
                        if solicitar_rut==rut:
                            fecha=input("Ingrese fecha:")
                            obs=input("Ingrese observacion:")
                            registros=fecha+obs
                            break
                        elif solicitar_rut!=rut:
                            print("Paciente no registrado,solicite el rut nuevamente ")
                    elif rut==None:
                        print("No hay ningun paciente registrado")
                        break
        elif opcion==3:
            print("****************")
            print("DATOS DEL PACIENTE")
            print("RUT: ",rut)
            print("Nombre: ",nombre)
            print("Direccion :",direccion)
            print("Correo: ",correo)
            print("Edad:" ,edad)
            print("Sexo:",sexo)
            print("Ps:",ps)
            print("Registros:",registros)
            print("****************")
        elif opcion== 4:
            print("Salir del Sistema")
            break
        else:
            print("Opcion invalida,vuelve a ingresar")
    except:
        print("Opcion invalida")
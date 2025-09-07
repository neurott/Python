#Solicitar el ingreso de 3 notas por pantalla,
#  luego calcular el promedio de las 3 notas (cada nota tiene la misma ponderación),
#  finalmente indicar con una salida de pantalla “Aprobado” en el caso de que el
#  promedio sea igual o mayor a 4.0.
n1 = float(input("Primera nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Tercera nota: "))

prom = (n1+n2+n3) / 3

if prom >= 4.0:
    print("aprobado")
else:
    print("reprobado")
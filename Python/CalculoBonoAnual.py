print (" -- Cálculo de Bono Anual -- ")

salario = int(input("Ingrese su salario actual: "))
desempeno = int(input("Ingrese su nota de desempeño (del 1 al 10): "))
antiguedad = int(input("Ingrese sus años de antiguedad en la empresa: "))

if (desempeno == 9 or desempeno == 10) and antiguedad > 5:
    bono = salario * 0.20
    print(f"Felicitaciones, su bono es del 20%: ${bono:.0f}")
elif (desempeno == 7 or desempeno == 8) or antiguedad == 5:
    bono = salario * 0.10
    print(f"Su bono es del 10%: ${bono:.0f}")
elif desempeno == 6 and antiguedad < 5:
    bono = salario * 0.05
    print(f"Su bono es del 5%: ${bono:.0f}")
else:
    print("Lo sentimos, no aplica para bono este año.")

print (" -- Fin del cálculo de bono -- ")
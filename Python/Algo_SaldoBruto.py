#Cuánto ganaron en el mes (saldo bruto).
#Cuántas horas trabajaron.
saldo = int(input("Ingrese su saldo bruto: "))
horas = int(input("Ingrese las horas que trabajó: "))

if saldo > 1500000 and horas >180:
    bono = saldo * 0.02
    print("Bono del 2% aplicado.")   
elif saldo > 1000000 and 150 <= horas <= 180:
    bono = saldo * 0.03
    print("Bono del 3% aplicado.")
elif saldo > 800000 and horas >= 120:
    bono = saldo * 0.04
    print("Bono del 4% aplicado.")
else:
    bono = 0
    print("No se aplicó ningún bono.")
if saldo < 0:
    print("Error: SALDO INVÁLIDO")

SaldoConBono = saldo + bono
print(f"Saldo con bono: {SaldoConBono}")
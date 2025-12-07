monto = float(input("Ingresa el monto total de la compra: "))

if monto >= 200:
    descuento = monto * 0.20
elif monto >= 100:
    descuento = monto * 0.10
else:
    descuento = 0

total = monto - descuento
print(f"Descuento aplicado: {descuento:.2f}")
print(f"Total a pagar: {total:.2f}")
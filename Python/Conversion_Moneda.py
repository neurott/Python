#Ingrese por teclado un valor en dólares y muestre su conversión en euros.
print("\nCONVERSIÓN DE MONEDA")

print("INGRESAR NÚMERO PARA CONVERTIR: \n"\
"\n1. DOLARES A EUROS" \
"\n2. EUROS A DOLARES" \
"\n3. DOLARES A CLPS" \
"\n4. CLPS A DOLARES")
valor = int(input("\nINGRESAR NÚMERO: "))
if valor == 1:
    dls = float(input("INGRESA LOS DÓLARES: "))
    convert = (dls * 0.88475)
    print(f"{dls} a euros es: {convert:0.1f}")
elif valor == 2:
    eur = float(input("INGRESA LOS EUROS: "))
    convert = (eur * 1.13)
    print(f"{eur} en dolares es: {convert:0.1f}")
elif valor == 3:
    usd = float(input("INGRESE LOS DOLARES QUE DESEA CONVERTIR: "))
    convert = (usd * 939.04)
    print(f"{usd} en pesos chilenos es: {convert:0.1f}")
elif valor == 4:
    clp = float(input("INGRESE LOS PESOS CHILENOS: "))
    convert = (clp * 0.0011)
    print(f"{clp} en dolares es: {convert}")
else:
    print("INGRESA UN VALOR VÁLIDO")
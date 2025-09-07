#quintil
arancel = 1800000
matricula = 90000

promedio = float(input("INGRESA EL PROMEDIO DE NOTAS: "))
quintil = int(input("INGRESA EL QUINTIL (1, 2, 3,4 ): "))

descuento_arancel = 0

if promedio > 6.0:
    if quintil == 1 or quintil == 2:
        descuento_arancel = 0.20
    elif quintil == 3 or quintil == 4:
        descuento_arancel = 0.15
elif promedio > 5.0 and promedio <= 6.0:
    if quintil == 1 or quintil == 2:
        descuento_arancel = 0.13
    elif quintil == 3 or quintil == 4:
        descuento_arancel = 0.10


#descuento matricula
descuento_matricula = 0

if quintil == 1 or quintil == 2 or quintil == 3:
    descuento_matricula = 0.10
    if promedio <= 5.5:
        descuento_matricula += 0.05 #5% adicional


#calculos finales

arancel_final = int(arancel * (1 - descuento_arancel))
matricula_final = int(matricula * (1 - descuento_matricula))

print("")
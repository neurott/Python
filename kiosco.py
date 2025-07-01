print("\nINICIO : $5.000\n")

def calcular_total():
    ##transbank = int(input("TRANSBANK: ")) ##Actualización no hay transbank, por lo cual la variable la borré xd
    transferencia = int(input("TRANSFERENCIA: "))
    m_100 = int(input("MONEDAS DE 100: "))
    m_50 = int(input("MONEDAS DE 50: "))
    m_500 = int(input("MONEDAS DE 500: "))
    billetes = int(input("BILLETES: "))
    
    totalmonedas = m_100 + m_50 + m_500
    
    total = transferencia + billetes + m_100 + m_50 + m_500

    print("\n--- RESULTADO ---")
    print(f"TOTAL MONEDAS: ${totalmonedas:,}".replace(",", "."))
    print(f"TOTAL INGRESADO: ${total:,}".replace(",", "."))
    print(f"TOTAL - 20.000 <- (+INICIO) = ${total - 20000:,}".replace(",", "."))

    with open("resultado.txt", "w", encoding="utf-8") as file:
        file.write(f"\nInicio: $5.000")
        file.write(f"TRANSFERENCIA: ${transferencia}".replace(",", ".") + "\n")
        file.write(f"TOTAL MONEDAS: ${totalmonedas:,}".replace(",", ".") + "\n")
        file.write(f"BILLETES: ${billetes}".replace(",", ".") + "\n")
        file.write(f"\nTOTAL INGRESADO: ${total:,}".replace(",", ".") + "\n")
        file.write(f"TOTAL INGRESADO - 20.000 <- (+ INICIO) = ${total - 20000:,}".replace(",", ".") + "\n")

    print("\nEl resultado ha sido guardardo en el archivo de texto: 'resultado.txt'")
calcular_total()
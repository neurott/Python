print("\nINICIO : $5.000\n")


def calcular_total():
    transferencia = int(input("TRANSFERENCIA: "))
    m_100 = int(input("MONEDAS DE 100: "))
    m_50 = int(input("MONEDAS DE 50: "))
    m_500 = int(input("MONEDAS DE 500: "))
    billetes = int(input("BILLETES: "))

    totalmonedas = sum(m_100, m_50, m_500)

    total = sum(transferencia,billetes,m_100,m_50,m_500)

    print("\n--- RESULTADO ---")
    print(f"TOTAL MONEDAS: ${totalmonedas:,}")
    print(f"TOTAL INGRESADO: ${total}")
    print(f"TOTAL - 20.000 <- (+INICIO) = ${total - 20000:_}")

    with open("resultado.txt", "w", encoding="utf-8") as file:
        file.write(f"\nInicio: $5.000")
        file.write(f"TRANSFERENCIA: ${transferencia}" + "\n")
        file.write(f"TOTAL MONEDAS: ${totalmonedas:,}" + "\n")
        file.write(f"\nBILLETES: ${billetes}" + "\n")
        file.write(f"\nTOTAL INGRESADO: ${total:,}" + "\n")
        file.write(
            f"TOTAL INGRESADO - 20.000 <- (+ INICIO) = ${total - 20000:,}" + "\n")
    print("\nEl resultado ha sido guardardo en el archivo de texto: 'resultado.txt'")


calcular_total()

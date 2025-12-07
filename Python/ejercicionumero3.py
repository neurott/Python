while True:
    try:
        n = int(input("ingresa el fucking numero: "))
        if n > 0:
            break
        else:
            print("El número debe ser mayor a cero.")
    except ValueError:
        print("debe ingresar un núemro entero valido")
# caso especial para el nuemro 1 (no es primo)
if n == 1:
    print("El 1 NO es un número primo")
else:
    es_primo = True
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"El número {n} SI es primo")
    else:
        print(f"El número {n} NO es primo")
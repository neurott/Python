palabra = input("Ingrese una palabra: ").lower()
vocales = 'aeiou'
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1

print(f"La palabra contiene un total de: {contador} de vocal(es)")

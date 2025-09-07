palabra = input("Ingrese una palabra: ") ## perro
invertida = ""

for letra in palabra:
    invertida = letra + invertida
    
print(f"La palabra invertida es: {invertida}")
#Contar vocales de una palabra
palabra = input("Ingrese una palabra: ").lower()
contador = 0
vocales = 'aeiou'
for x in palabra:
    if x in vocales:
        contador += 1
print(f"La palabra tiene {contador} vocal(es)")
#Recorrer la palabra letra por letra
#Si es asi, contador + 1
#La letra es una vocal?
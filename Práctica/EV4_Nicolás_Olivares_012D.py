def comprar_entrada():
    nombre = input("Ingrese nombre de comprador: ")
    if nombre in comprador:
        print("Este nombre ya existe")
    else:
        comprador['Nombre'] = nombre

    tipoEntrada = input("Ingrese tipo de entrada [G: General / V: Vip]: ").upper()  
    if tipoEntrada == 'G' or tipoEntrada == 'V':
        comprador['Tipo'] = tipoEntrada  
    else:
        print("Error: Ingrese un tipo de entrada válido. Intentar nuevamente")

    codigo_acceso = input("Ingrese código de confirmación: ").strip()

    if len(codigo_acceso) >= 6:
        comprador['Codigo'] = codigo_acceso
        print("Código validado. ¡Entrada registrada con éxito!")
    else:
        print("Código no válido. Intente otra vez.")
   
def consultar_comprador():
    Comprador = input("Ingrese el nombre de comprador a buscar: ")

    if Comprador in comprador: #Esta parte de acá estará bien? in comprador['nombre']. lo borré
        for Comprador in comprador: #¿Por qué cuando lo ejecuto itera tanto en un solo comprador?
            print(f"Tipo de entrada: {comprador['Tipo']},Código: {comprador['Codigo']}")
    else:
        print("El comprador no se encuentra") # esto no funciona correctamente, ingreso el comprador y aunque exista, dice que no se encuentra

def cancelar_compra():
    #nombre = input("Ingrese nombre de comprador a cancelar: ")
    #no terminé
    return
#Lista o Diccionario?
#[] tipo arbitrario
#{
# Clave:Valor}
comprador = {}
def main():
    while True:
        print("~"*20)
        print("\nMenú Principal")
        print("Concierto de Trap con el Conejo Simpático")
        print("1. Comprar entrada")
        print("2. Consultar comprador")
        print("3. Cancelar compra")
        print("4. Salir")
        try:
            op = int(input("Seleccione una opción: "))
                
            if op == 1:
                comprar_entrada()
            elif op == 2:
                consultar_comprador()
            elif op == 3:
                cancelar_compra()
            elif op == 4:
                print("Programa terminado...")
                break
            else:
                print("\nDebe ingresar una opción válida!!")
        except:
            print("ERROR")
main()
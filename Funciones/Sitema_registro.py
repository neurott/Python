#Ssitema de regsitro
registros_aduana = {
    "A001": ["Luis Pérez", "Perú", "03-01-2024"],
    "A002": ["Ana Gómez", "Bolivia", "11-02-2024"],
    "A003": ["Carlos Silva", "Brasil", "25-03-2024"],
    "B001": ["Lucía Fernández", "Argentina", "05-04-2024"],
    "B002": ["Miguel Soto", "Paraguay", "20-03-2024"],
    "B003": ["Laura Díaz", "Brasil", "17-01-2024"],
    "C001": ["David Rojas", "Argentina", "09-12-2023"],
    "C002": ["Camila Herrera", "Perú", "15-03-2024"],
    "C003": ["Sofía Cáceres", "Colombia", "08-05-2024"]
}
def menu():
    print("\nMenú principal - control aduana")
    print("1. Personas por país")
    print("2. Ingresos por mes")
    print("3. Eliminar registro")
    print("4. Mostrar registros")
    print("5. Salir")

def personasPorPais(pais):
    encontrados = []
    for clave in registros_aduana:
        if registros_aduana[clave][1].lower() == pais.lower():
            encontrados.append(registros_aduana[clave][0])
    if encontrados:
        print(encontrados)
    else:
        print("No hay registros de personas que sean de ese país")

def ingresosPorMes(mes):
    meses = ["enero", "febrero", "marzo", "abril", "mayo",
     "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
 
    total = 0
    cantidad = 0

    for clave in registros_aduana:
        total += 1
        fecha = registros_aduana[clave][2]
        mes_fecha = int(fecha.split("-")[1])
        if mes_fecha == mes:
            cantidad += 1
        nombre_mes = meses[mes -1]
        porcentaje = (cantidad / total) * 100

        print(f"El porcentaje de ingresos en {nombre_mes} es {porcentaje:.1f}% del total.")

def eliminar_registro():
    nombre = input("Ingrese el nombre completo de la persona que desea eliminar: ").lower()
    claveEliminar = None
    for clave, datos in registros_aduana.items():
        if datos[0].lower() == nombre:
            claveEliminar = clave
            break

    if claveEliminar:
        del registros_aduana[claveEliminar]
        print("Registro eliminado con éxito")
    else:
        print("Persona no encontrada. No se pudo eliminar.")

def mostrar_registros():
    if not registros_aduana:
        print("No hay registros en la aduana")
        return
    for clave, datos in registros_aduana.items():
        nombre, pais, fecha = datos
        print(f"Clave: {clave} | Nombre: {nombre} | País: {pais} | Fecha: {fecha}")

def main():
    while True:
        menu()
        try:
            op = int(input("Seleccione una opción (1-4): "))
        except ValueError:
            print("Debe seleccionar una opción válida del menú.")
            continue
        if op == 1:
            pais_ingresado = input("Ingrese país a buscar: ")
            personasPorPais(pais_ingresado)
        elif op == 2:
            while True:
                try:
                    mes_ingresado = int(input("Ingrese mes a consultar: "))
                    if 1 <= mes_ingresado <= 12:
                        ingresosPorMes(mes_ingresado)
                        break
                    else:
                        print("Debe ingresar un número entre 1 y 12. Inténtelo nuevamente")

                except ValueError:
                    print("Debe ingresar un número válido")      
        elif op == 3:
            eliminar_registro()
        elif op == 4:
            mostrar_registros()
        elif op == 5:
            print("Saliendo....")
            break
        else:
            print("ERROR; INTÉNTELO NUEVAMENTE")
main()
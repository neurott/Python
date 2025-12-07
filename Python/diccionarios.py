persona = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Quilpué"
}

print(persona["nombre"])

#diccionario[clave] --> acceder a un valor
#diccionario[clave] = nuevo_valor --> agregar o cambiar un valor

auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2001
}

#imprimir diccionario
print(auto)

#Mostrar el modelo del auto
print(auto["modelo"])

#Cambiar el año del auto
auto["año"] = 2005

#Agregar una nueva clave "color" con el valor "blanco"
auto["color"] = "blanco"

#imprimir el diccionario
print(auto)
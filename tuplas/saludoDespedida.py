'''Crea 2 funciones saludo y despedida que reciban un nombre como parámetro y crea una tupla con ambas funciones.
solicita el nombre al usuario y si quiere saludar o despedirse e invoca la función correspondiente desde la tupla
si el usuario introduce una opción no válida, muestra un mensaje de error.'''

def saludo(nombre): 
    return f"Hola, {nombre}! Bienvenido/a."

def despedida(nombre):
    return f"Adiós, {nombre}! Hasta luego."

nombre=input("Introduce tu nombre: ")
opcion=input("¿Quieres saludar o despedirte? (s/d): ").lower()

funciones = (saludo, despedida)

if opcion == "s":
    print(funciones[0](nombre))
elif opcion == "d":
    print(funciones[1](nombre))
else:
    print("Opción no válida.")
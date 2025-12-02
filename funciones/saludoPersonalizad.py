'''Crea una función llamada saludar que reciba dos argumentos por palabra clave:
- nombre (str)
- saludo (str), con valor por defecto "Hola"
La función debe devolver una cadena con el saludo seguido del nombre.'''

def saludar(nombre, saludo="Hola"):
    print (f"{saludo}, {nombre}")
while(True):
    nombreIntroducido= input("Introduce tu nombre: \n")
    if nombreIntroducido=="":
        print("No has introducido un nombre")
    elif nombreIntroducido.isdigit():
        print ("No has introducido un texto, has introducido un número")
    else:
        saludar(nombreIntroducido)
        print(f"Adiós, {nombreIntroducido}")
        break

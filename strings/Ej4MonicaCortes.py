''''Crea una función que reciba un argumento string y conviertelo a minusculas '''
def convertir_minusculas(cadena):
    cadena=cadena.lower()
    return cadena

print(convertir_minusculas("JUAn"))
'''Crea una función quer reciba un argumento string que compruebe si todos los 
carácteres son mayúsculas'''

def es_mayusculas(cadena):
    cadena=cadena.isupper()
    cadena_comprobada=cadena
    return cadena_comprobada

print(es_mayusculas("Monica"))
print(es_mayusculas("ALBERTO"))


def es_mayusculas1(cadena):
    return "MAYÚSCULAS" if cadena.isupper() else "minúsculas"
print(es_mayusculas1("Monica"))
print(es_mayusculas1("ALBERTO"))

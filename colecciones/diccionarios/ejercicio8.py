'''Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un 
diccionario con las palabras y sus traducciones. Después pedirá una frase en español y 
utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el 
diccionario debe dejarla sin traducir.'''
traductor={}
while True:
    palabra= input("Introduce la lista de palabras y traducciones en formato palabra:traducción \
    separadas por comas Ej.: casa:house,grande:big,perro:dog (o X para terminar): ")
    if palabra.upper() =="X":
        break
    pares=palabra.split(",")
    for par in pares:
        if ":" in par:
            esp,ing=par.split(":")
            traductor[esp.strip()]=ing.strip()
        else:
            print(f"Formato incorrecto en: {par}")

frase=input("Introduce una frase: ")
palabras=frase.split()

traduccion = []

for p in palabras:
    if p in traductor:
        traduccion.append(traductor[p])
    else:
        traduccion.append(p)

print("Traducción:", " ".join(traduccion))


'''diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave.strip().lower()] = valor.strip().lower()
frase = input('Introduce una frase en español: ')
for i in frase.split():
    palabra = i.lower() 
    if palabra in diccionario:
        print(diccionario[palabra], end=' ')
    else:
        print(i, end=' ')'''

coleccion = ["pera", "manzana", "uva", "pera", "kiwi", "pera"]
coleccion.sort()  # Aseguramos que esté ordenada

elemento = input("Introduce un elemento: ")

# Buscar todas las posiciones donde aparece
posiciones = [i for i, x in enumerate(coleccion) if x == elemento]

if posiciones:
    print(f"El elemento '{elemento}' aparece en las posiciones: {posiciones}")
else:
    print(f"El elemento '{elemento}' no está en la colección.")
    # Insertarlo manteniendo el orden
    coleccion.append(elemento)
    coleccion.sort()
    nueva_pos = [i for i, x in enumerate(coleccion) if x == elemento]
    print(f"Se ha añadido '{elemento}' en la posición {nueva_pos[0]}.")

print("\nColección actualizada:")
print(coleccion)



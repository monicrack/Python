'''Ejercicio 1: Crea una función calcular_estadisticas(numeros) que reciba una lista de 
números y devuelva una tupla con: 
● El valor mínimo. 
● El valor máximo. 
● La media aritmética. '''

def calcular_estadisticas(numeros):
    minimo=min(numeros)
    maximo=max(numeros)
    media=sum(numeros)/len(numeros)
    return (minimo, maximo, media)

numeros=[10, 20, 30, 40, 50]
minimo, maximo, media = calcular_estadisticas(numeros)#desempaquetar la tupla
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Media:", media)

'''Ejercicio 2: Crea una función distancia(p1, p2) que reciba dos tuplas representando 
puntos en el plano (x, y) y devuelva la distancia entre ellos usando la fórmula: 
distancia = √((x2 - x1)² + (y2 - y1)²)'''

def distancia(p1, p2):
    import math
    x1, y1 = p1
    x2, y2 = p2
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist 

punto1 = (2, 3)
punto2 = (5, 7) 
d = distancia(punto1, punto2)
print("Distancia entre los puntos:", d)

'''Ejercicio 3: Crea una función analizar_texto(texto) que devuelva una tupla con: 
● Número total de caracteres. 
● Número de palabras. 
● Primera palabra del texto. '''

def analizar_texto(texto):
    num_caracteres = len(texto)
    palabras = texto.split()
    num_palabras = len(palabras)
    primera_palabra = palabras[0] 
    return (num_caracteres, num_palabras, primera_palabra)

texto = "Hola clase, este es un texto de ejemplo para practicar tuplas con Python."
num_caracteres, num_palabras, primera_palabra = analizar_texto(texto)
print("Número total de caracteres:", num_caracteres)
print("Número de palabras:", num_palabras)  
print("Primera palabra del texto:", primera_palabra)

'''Ejercicio 4: Crea una función convertir_temperatura(celsius) que reciba una 
temperatura en grados Celsius y devuelva una tupla con: 
● La temperatura en Fahrenheit. 
● La temperatura en Kelvin. '''
def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return (fahrenheit, kelvin)

celsius = 25
fahrenheit, kelvin = convertir_temperatura(celsius)
print(f"Temperatura en Celsius: {celsius}°C")   
print(f"Temperatura en Fahrenheit: {fahrenheit}°F")
print(f"Temperatura en Kelvin: {kelvin}K")

'''Ejercicio 5: Crea una función analizar_numeros(numeros) que reciba una lista de 
enteros y devuelva una tupla con: 
● El número de elementos pares. 
● El número de elementos impares. 
● La suma total. '''
def analizar_numeros(numeros):
    pares = sum(1 for n in numeros if n % 2 == 0)
    impares = sum(1 for n in numeros if n % 2 != 0)
    suma_total = sum(numeros)
    return (pares, impares, suma_total)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares, suma_total = analizar_numeros(numeros)
print("Número de elementos pares:", pares)
print("Número de elementos impares:", impares)
print("Suma total:", suma_total)

'''Ejercicio 6: Crea una función procesar_cadena(cadena) que devuelva una tupla con: 
● La cadena en mayúsculas. 
● La cadena en minúsculas. 
● La longitud de la cadena.'''
def procesar_cadena(cadena):
    mayusculas = cadena.upper()
    minusculas = cadena.lower()
    longitud = len(cadena)
    return (mayusculas, minusculas, longitud)
cadena = "Hola Mundo"
mayusculas, minusculas, longitud = procesar_cadena(cadena)
print("Cadena en mayúsculas:", mayusculas)
print("Cadena en minúsculas:", minusculas)
print("Longitud de la cadena:", longitud)

'''Adivina en qué posición está el nº n (aleatorio 1-10) en una tupla'''

import random
tupla_numeros = (1, 3, 5, 7, 9, 2, 4, 6, 8, 10)
numero_aleatorio = random.randint(1, 10)   
print("Número aleatorio generado:", numero_aleatorio)
if numero_aleatorio in tupla_numeros:
    posicion = tupla_numeros.index(numero_aleatorio)
    print(f"El número {numero_aleatorio} está en la posición {posicion} de la tupla.")
else:
    print(f"El número {n} no está en la tupla.")    

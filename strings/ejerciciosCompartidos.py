''' Ejercicio 1 (Sebastian Becerra) 
Modifica la cadena “      este ejercicio es muy complicado            ” para que el ejercicio 
sea facilísimo  y cada una de las palabras comience en mayúsculas y sin espacios y luego 
imprimelo invertido, ademas busca el indice de la palabra complicado.'''
def transformar_cadena(cadena):
    # 1. Reemplazar "complicado" por "facilísimo" Sustituye todas las apariciones de old por new en la cadena.
    cadena_modificada = cadena.replace("complicado", "facilísimo")
    # 2. Convertir cada palabra para que empiece en mayúscula
    palabras = cadena_modificada.split()#Divide la cadena en una lista de palabras usando espacios por defecto
    resultado = []
    for p in palabras:
     resultado.append(p.capitalize())
    #Convierte la primera letra a mayúscula y el resto a minúsculas.
    # 3. Unirlas sin espacios
    cadena_sin_espacios = "".join(resultado)
    #Une los elementos de un iterable en una sola cadena usando el separador dado
    # 4. Invertir la cadena
    cadena_invertida = cadena_sin_espacios[::-1]
    #Crea una nueva cadena con los caracteres en orden inverso
    # 5. Buscar el índice de la palabra "complicado" en la cadena original
    indice = cadena.find("complicado")
    #Devuelve el índice de la primera aparición de sub; si no existe, devuelve -1
    # Retornar resultados
    return cadena_invertida, indice
# Ejemplo de uso
texto = "   este ejercicio es muy complicado    "
resultado, indice = transformar_cadena(texto)
print("Cadena invertida:", resultado)
print("Índice de 'complicado':", indice)

''' Ejercicio 2  (Ana López) 
Vamos a definir una cadena y la vamos a pasar a minúsculas, eliminar los espacios
 y las letras pares las vamos a cambiar por asteriscos'''
def convertir_minusculas(cadena):
   #1.convertir a minúsculas
   cadena_minusculas=cadena.lower()
   # 2. Eliminar espacios
   cadena_sin_espacios = cadena_minusculas.replace(" ", "")
   # 3. Recorrer la cadena y sustituir letras en posiciones pares
   resultado = ""
   for i, caracter in enumerate(cadena_sin_espacios):
       if i % 2 == 0:   # índice par= letra impar mantener la letra
           resultado += caracter
       else:            # índice impar = letra par sustituir por *
           resultado += "*"
   return resultado
# Ejemplo de uso
texto = "Este Ejercicio Es Muy Complicado"
print(convertir_minusculas(texto))
    
''' EJERCICIO 3 (Alejandro Malpelo): Clasificador de palabras
 Escribe un programa en Python que pida al usuario un texto y clasifique sus palabras según estas 
reglas:- Palabras que empiezan por vocal.- Palabras que terminan en consonante.
- Palabras que contienen  algún número.  
- El programa debe:- Separar el texto en palabras.
 - Detectar cuáles cumplen cada condición.
 - Guardarlas en un diccionario con tres listas.
 - Mostrar un informe final indicando las palabras encontradas en cada categoría
 y cuántas hay en cada una.'''
def clasificar_palabras(texto):
    # Separar el texto en palabras
    palabras = texto.split() 
    # Diccionario con las tres categorías
    clasificacion = {
        "empiezan_vocal": [],
        "terminan_consonante": [],
        "contienen_numero": []
    }
    # Definir vocales y consonantes
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"
    # Recorrer cada palabra y clasificar
    for palabra in palabras:
        if palabra[0] in vocales:  # empieza por vocal
            clasificacion["empiezan_vocal"].append(palabra)
        
        if palabra[-1] in consonantes:  # termina en consonante
            clasificacion["terminan_consonante"].append(palabra)
        
        if any(char.isdigit() for char in palabra):  # contiene número
            clasificacion["contienen_numero"].append(palabra)
    
    return clasificacion

# Programa principal
texto_usuario = input("Introduce un texto: ")
resultado = clasificar_palabras(texto_usuario)

# Informe final
print("\n--- Informe de clasificación ---")
for categoria, lista in resultado.items():
    print(f"{categoria}: {lista} (total: {len(lista)})")

'''EJERCICIO 5 (Alejandro Pacheco):
A través de una función, introduciendo una cadena por parámetro, devolver la longitud, devolver 
la cadena en minúsculas y devolver las ultimas 5 letras de la cadena.'''
def analizar_cadena(cadena):
    cadena_longitud=len(cadena)
    cadena_minusculas=cadena.lower()
    ultimas_5 = cadena[-5:]
    #obtiene un slice desde la quinta letra contando desde el final hasta el fina
    return cadena_longitud, cadena_minusculas, ultimas_5
# Ejemplo de uso
texto = "Programación En Python"
longitud, minusculas, ultimas_5 = analizar_cadena(texto)

print("Longitud:", longitud)
print("En minúsculas:", minusculas)
print("Últimas 5 letras:", ultimas_5)
'''EJERCICIO 6 (Alberto Llera):
 Recoger un email por consola introducido por el usuario. En una función se debe comprobar que 
el correo introducido por el usuario contenga “@” y acabe en “.com” o “.es”.  Además, el usuario 
solo tendrá tres oportunidades para validar el correo.'''

'''EJERCICIO 7 (Manuel Moreno)
 Pedir por teclado una cadena de texto y “analizarla” con distintas funciones.
 Deberá contar la longitud total, contar las letras (mirar isaplha()), contar los números, contar los 
caracteres especiales y contar los espacios'''

''' EJERCICIO 8 (Rafael Cosquillo)
 Pida al usuario una frase. 
Elimine los espacios al inicio y al final (strip()).
 Muestre: La frase en minúsculas (lower()). 
La frase en mayúsculas (upper()). 
La frase con la primera letra en mayúscula (capitalize()). 
Reemplace todas las comas por puntos (replace()). 
Cuente cuántas veces aparece una palabra que el usuario ingresa (count()). 
Verifique si la frase empieza con una vocal (startswith()). 
Muestre cuántas palabras tiene la frase (split()).'''

'''EJERCICIO 9 (Franco Benavides)
Pide al usuario una oración completa y el programa debe decir cuántas
palabras tiene esa oración.
Si ese número es par, convierte las letras pares a mayúsculas y las impares a
minúsculas y devuelve esa frase convertida.
Si el número es impar, devuelve la frase con las palabras con el orden
invertido.
frase = "Estoy estudiando Python y no quiero suspender'''

'''Crea una lista con los nombres de cinco países y muestra el tercer país de la lista.'''
paises=["España","Italia","Francia","Irlanda","Grecia"]
print(paises[2])
print("**********************")
'''Dada una lista de números [10, 20, 30, 40, 50], imprime el primer y el último elemento.'''
numeros=["10","20","30","40","50"]
print(numeros[0])
print(numeros[-1])
print("**********************")
'''Crea una lista con tus comidas favoritas y muestra la segunda, tercera y la cuarta.'''
comidas=['lentejas','paella','albondigas','patatas asadas','sopa']
print(comidas[1:4])
print("**********************")
'''Dada la lista frutas = ["manzana", "banana", "pera", "uva"], cambia el segundo elemento por "naranja".'''
frutas = ["manzana", "banana", "pera", "uva"]
frutas[1]="naranja"
print(frutas)
print("**********************")
'''Crea una lista con cinco colores y reemplaza el último color por "negro"'''
colores=['rojo','verde','azul','blanco','morado','rosa']
colores[5]="negro"
print (colores)
print("**********************")
'''Dada la lista [1, 2, 3, 4, 5], cambia el valor del tercer elemento por 100'''
lista_numeros=[1, 2, 3, 4, 5]
lista_numeros[2]=100
print(lista_numeros)
print("**********************")
'''Crea una lista vacía y agrega tres números usando .append()'''
lista_vacia=[]
lista_vacia.append("100")
lista_vacia.append("200")
lista_vacia.append("300")
print(lista_vacia)
print("**********************")
'''Dada la lista animales = ["perro", "gato"], agrega "conejo" al final.'''
animales=["perro", "gato"]
animales.append("conejo")
print(animales)
print("**********************")
'''Crea una lista con tres deportes y añade uno más en la posición 2 usando .insert().'''
deportes=["baloncesto","patinaje artístico","natación sincronizada"]
deportes.insert(1, "rugby")
print(deportes)
print("**********************")
'''Dada la lista numeros = [1, 2, 3, 4, 5], elimina el primer elemento usando .pop(0).'''
listado_numeros= [1, 2, 3, 4, 5]
numero_eliminado=listado_numeros.pop(0)
print(listado_numeros)
print("**********************")
'''Crea una lista con cinco frutas y elimina "pera" usando .remove().'''
lista_frutas=["manzana", "banana", "pera", "uva","melón"]
fruta_eliminada=lista_frutas.pop(2)
print(lista_frutas)
print("**********************")
'''Dada la lista [10, 20, 30, 40], borra el último elemento con .pop().'''
list=[10, 20, 30, 40]
elemento_eliminado=list.pop()
print(list)
'''Crea una lista con cinco nombres y recórrela con un for para imprimir cada uno.'''
nombres=["María","Juan","Jorge","Pedro","Almudena"]
for nombre in nombres:
    print(nombre)
print("**********************")
'''Dada la lista [2, 4, 6, 8], usa un bucle para imprimir el doble de cada número.'''
doble_numeros=[2, 4, 6, 8]
for doble in doble_numeros:
    print(doble*2)
print("**********************")
'''Crea una lista con palabras y usa un bucle para mostrar cuántas letras tiene cada palabra.'''
palabras=["María","Juan","Jorge","Pedro","Almudena"]
for palabra in palabras:
    print (len(palabra))
print("**********************")    
''' Dada una lista de números cuenta cuantas veces aparece un número concreto y ordena la lista de mayor a menor'''
numeros_en_lista=[1,2,3,4,2,5,2,6,7,2,8,9,2,10]
numero=2
contar_numero=numeros_en_lista.count(numero)
if (contar_numero == 1):
    print(f"El número {numero}  aparece:",contar_numero, "vez")
else: print(f"El número {numero} aparece:",contar_numero, "veces")
lista_ordenada = sorted(numeros_en_lista, reverse=True)
print("Lista ordenada de mayor a menor:", lista_ordenada)

'''que número de letra le corresponde al año feliz 20262026 para calcularlo necesito
la suma de cada digito calculando la letra oficial obtenida
con la fórmula del DNI (número % 23 usando la cadena "TRWAGMYFPDXBNJZSQVHLCKE").'''

numero = input("Introduce un número: ")

# 1. Sumar los dígitos
suma_digitos = 0 
for d in numero: 
    if d.isdigit(): suma_digitos += int(d)
'''suma_digitos = sum(int(d) for d in numero if d.isdigit())'''

# 2. Cadena oficial de letras del DNI
letras = "TRWAGMYFPDXBNJZSQVHLCKE"

# 3. Calcular la letra usando la fórmula del DNI
indice = suma_digitos % 23
letra = letras[indice]

print("Número introducido:", numero)
print("Suma de dígitos:", suma_digitos)
print("Índice (suma % 23):", indice)
print("Letra correspondiente:", letra)



'''dada una lista de años comprueba si son años felices, un numero feliz es cuando la suma de sus cuadrados
de sus cifras el resultado es 1'''
anios_felices=[2026,2000,1998,1996,1974,1967,1918,2012]


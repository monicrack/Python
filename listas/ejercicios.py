#Ejercicio 1
'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas 
por el usuario.'''

asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas=[]
for asignatura in asignaturas:
    nota=input(f"¿Qué nota has sacado en {asignatura}? ")
    notas.append(nota)
for i in range (len(asignaturas)):
    print (f"En la asignatura {asignaturas[i]} has sacado {notas[i]}")

print("********************************")
#Ejercicio 2
'''Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.'''
numeros_ganadores = [] 
for i in range(6):  
    numero = int(input("Introduce un número ganador: ")) 
    numeros_ganadores.append(numero)
numeros_ganadores.sort() 
print(f"Los números ganadores son: {numeros_ganadores}")
print(f"Los números ganadores son: {sorted(numeros_ganadores)}")

print("********************************")
#Ejercicio 3

'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física,
 Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura 
 y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
 asignaturas que el usuario tiene que repetir.'''

print("********************************")
#Ejercicio 4
'''Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras 
que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''

abecedario = list("abcdefghijklmnopqrstuvwxyz")

resultado = []
for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:
        resultado.append(abecedario[i])

print(resultado)

print("********************************")
#Ejercicio 5
'''Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.'''


print("********************************")
#Ejercicio 6
'''Escribir un programa que almacene las matrices
 
 A=(1 2 3)(4 5  6) y B(-1 0)(0 1)(1 1)

en una lista y muetre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila 
en una lista.'''
#examen
'''haz un programa que cuente de una frase cuantas vocales de cada tiene'''

'''haz un programa que haz una colección en la que incluyas palabras o números busca la posición de 
cada elemento si un elemento no está incluido en la colección añadelo en la posición que le corresponda '''
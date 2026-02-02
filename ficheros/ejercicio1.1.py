'''Escribe un programa que abra un fichero de texto llamado datos.txt, 
lea todo su contenido y lo muestre por pantalla.'''
print("************************Ejercicio 1 ************************")

f=open("ficheros/datos.txt")
print(f.read())


print("************************Ejercicio 2 ************************")

'''Escribe un programa que abra un fichero datos.txt y cuente cuántas líneas tiene el archivo.'''
f=open("ficheros/datos.txt")
cantidad=f.readlines()
print (f"El fichero tiene: {len(cantidad)} líneas")


print("************************Ejercicio 3 ************************")

'''Crea un programa que lea el fichero datos.txt y cuente cuántas veces aparece una palabra específica 
que el usuario introduce. 
Solicita al usuario la palabra a buscar.
Usa read() para leer todo el contenido del fichero.
Usa el método count() para contar las ocurrencias de la palabra.'''

with open ("ficheros/datos.txt") as f:
    palabra=input("¿Qué palabra quieres buscar en el fichero?: ")
    fichero=f.read()
    cantidad = fichero.count(palabra)
    print(f"Hay {cantidad} {palabra} en el fichero"  )

print("************************Ejercicio 4 ************************")
'''Escribe un programa que cree un fichero nuevo.txt y escriba en él varias líneas de texto introducidas
por el usuario.
Instrucciones:
Usa open() en modo escritura ('w').
Solicita al usuario varias líneas de texto.
Escribe cada línea en el fichero.
Cierra el fichero al finalizar.'''
with open ("ficheros/nuevo.txt", "w") as f:
    for i in range (3):
        linea=input("Escribe una línea de texto para el fichero: ")
        f.write(linea + "\n")
print("************************Ejercicio 5 ************************")
'''Escribe un programa que abra un fichero datos.txt y permita al usuario añadir nuevas líneas 
de texto al final.
Instrucciones:
    Usa open() en modo agregar (‘a’).
    Solicita al usuario las líneas a añadir.
    Escribe cada línea en el fichero.
    Cierra el fichero.
'''
with open ("ficheros/datos.txt", "a") as f:
    for i in range (2):
        linea=input("Escribe una línea de texto para añadir al fichero: ")
        f.write(linea + "\n")
print("************************Ejercicio 6 ************************ ")
'''Escribe un programa que copie el contenido de un fichero datos.txt a un nuevo fichero llamado 
copia.txt.
Instrucciones:
    Abre el fichero original en modo lectura.
    Abre el nuevo fichero en modo escritura.
    Copia el contenido de un fichero al otro.
    Cierra ambos ficheros.
'''
with open ("ficheros/datos.txt") as f:
    contenido=f.read()      
with open ("ficheros/copia.txt", "w") as f2:
    f2.write(contenido)
print("Fichero copiado con éxito.")
print("************************Ejercicio 7 ************************ ")
'''Crea un programa que lea un fichero datos.txt e invierta el orden de sus líneas, 
guardando el resultado en un nuevo fichero invertido.txt.
Instrucciones:
    Usa readlines() para leer todas las líneas.
    Invierte el orden de la lista de líneas.
    Escribe las líneas invertidas en el nuevo fichero.
'''
with open ("ficheros/datos.txt") as f:
    lineas=f.readlines()    
lineas_invertidas=lineas[::-1]
with open ("ficheros/invertido.txt", "w") as f2:
    f2.writelines(lineas_invertidas)
    
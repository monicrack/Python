'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido 
del diccionario.'''
datos={}
nombre=input("Introduce tu nombre: ").capitalize()
datos["nombre"]=nombre
print(datos)
edad=int(input("Escribe tu edad: "))
datos["edad"]=edad
print(datos)
sexo=input("Introduce tu sexo F/M: ").upper()
datos["sexo"]=sexo
print(datos)

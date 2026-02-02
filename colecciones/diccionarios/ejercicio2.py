'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''
datos={"nombre":"","edad":"","direccion":"","telefono":""}

nombre=input("¿Cuál es tu nombre? ").capitalize()
edad=int(input ("¿Cuál es tu edad? "))
direccion=input("¿Cuál es tu dirección? ").capitalize()
telefono=int(input("¿Cuál es tu telefóno? "))

datos[nombre]=nombre
datos[edad]=edad
datos[direccion]=direccion
datos[telefono]=telefono

print(f"{datos[nombre]} tiene {datos[edad]} años, vive en {datos[direccion]} y su número de teléfono es {datos[telefono]} ")
  

'''modulo calculos con 3 funciones area  circulo, area cuadrado, area triangulo
 si no se ha introducido alguno de los valores, el valor por defecto sera 8'''
#función area circulo
import math
def area_circulo(radio=8):
    return math.pi * radio * radio
#función area cuadrado
def area_cuadrado(lado=8):
    return lado * lado  
#función area triangulo
def area_triangulo(base=8, altura=8):
    return (base * altura) / 2  
print("hola") #no hacer
      

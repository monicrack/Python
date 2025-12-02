#Llamar al modulo completo 
#import moduloCalcularArea
#print(f"El área del círculo es: {moduloCalcularArea.area_circulo(5)}") #llamada a la funcion area_circulo del modulo calculaArea
#print(f"El área del círculo es: {moduloCalcularArea.area_circulo()}") #llamada a la funcion area_circulo del modulo calculaArea con valor por defecto


#alias para archivo moduloCalcularArea
import moduloCalcularArea as c
print(f"El área del cuadrado es: {c.area_cuadrado(3)}") #llamada a la funcion area_cuadrado del moduloCalcularArea usando alias
print(f"El área del cuadrado es: {c.area_cuadrado()}") #llamada a la funcion area_cuadrado del moduloCalcularArea usando alias con valor por defecto

#llamar solo a una funcion del moduloCalcularArea

from moduloCalcularArea import area_triangulo
print(f"El área del triángulo es: {area_triangulo(4, 6)}") #llamada a la funcion area_triangulo del moduloCalcularArea
print(f"El área del triángulo es: {area_triangulo()}") #llamada a la funcion area_triangulo del moduloCalcularArea con valores por defecto
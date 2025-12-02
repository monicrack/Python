
#importa el modulo calcula completo
'''import calcula

print(calcula.suma(5, 7)) #llamada a la funcion suma del modulo calcula
print(calcula.resta(10, 3)) #llamada a la funcion resta del modulo calcula
'''

#alias para archivo calcula
'''import calcula as c
print(c.suma(2, 3)) #llamada a la funcion suma del modulo calcula usando alias
print(c.resta(8, 5)) #llamada a la funcion resta del modulo calcula usando alias'''

#llamar solo a una funcion del modulo calcula

from calcula import suma, resta
print(suma(4, 6)) #llamada a la funcion suma del modulo calcula
print(resta(9, 2)) #llamada a la funcion resta del modulo calcula

'''modulo calculos con 3 funciones area  circulo, area cuadrado, area triangulo
 si no se ha introducido alguno de los valores, el valor por defecto sera 8'''
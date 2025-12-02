def mi_funcion(saludo, *nombres):
    for nombre in nombres:
        print(saludo, nombre)
    print(nombres[0] )

mi_funcion("Hola", "Ana", "Luis", "María")  # Llamada con 3 argumentos


def mi_funcion2(*numeros):
    total=0
    for numero in numeros:
        total+=numero
    return total

'''print(mi_funcion2(1,2,3,4,5))  # Llamada con 5 argumentos
print(mi_funcion2(10,20))      # Llamada con 2 argumentos   
print(mi_funcion2(5))           # Llamada con 1 argumento            
print(mi_funcion2())            # Llamada sin argumentos'''

'''def mi_funcion3(*numeros):
    if len(numeros)==0:
        max_num =numeros[0]
        for numero in numeros:
            if numero>max_num:
                max_num=numero
        return max_num
print(mi_funcion3(3,5,2,8,1))  # Llamada con varios argumentos
print(mi_funcion3())           # Llamada sin argumentos'''

'''def mi_funcion4(multiplicador,*numeros):
    total=0
    for numero in numeros:
        total+=numero
        total*=multiplicador
    return total

print(mi_funcion4(3,5))  # Llamada con 5 argumentos'''


'''def mi_funcion4(multiplicador,*numeros):
    total=0
    total_multiplicado=0
    for numero in numeros:
        total=numero*multiplicador
        total_multiplicado+=total 
    return total_multiplicado

print(mi_funcion4(3,1,2)) '''

'''def make_pizza(tamaño, *ingredientes):
    print(f"\nHaciendo una pizza de {tamaño} porciones con los siguientes ingredientes:")
    for ingrediente in ingredientes:
        print (ingrediente, end =",")

make_pizza(1, "pepperoni")
make_pizza(5, "jamón", "piña", "extra queso", "tomate", "atún")'''



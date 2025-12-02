'''Funcion ganador y devuelve un ganador aleatoriamente de una lista de participantes'''
import random
#ejemplo sin usar funciones
def ganador_aletorio(*participantes):
    numero_aleatorio = random.randint(0, len(participantes)-1)
    return participantes[numero_aleatorio]
print(ganador_aletorio("Ana", "Luis", "María", "Carlos"))


#argumento regular * puede recibir un número variable de argumentos que se agrupan en una tupla
def ganador(*participantes):
    return random.choice(participantes)
#devuelve un elemento aleatorio de una secuencia, como una lista, tupla o cadena
print(ganador("Ana", "Luis", "María", "Carlos"))

def ganador2(*participantes):
    return random.sample(participantes, 2)
#devuelve una lista con el número especificado de elementos distintos seleccionados aleatoriamente de la secuencia dada
print(ganador2("Ana", "Luis", "María", "Carlos"))

def ganador3(*participantes):
    return random.choices(participantes, k=3)
#devuelve una lista con el número especificado de elementos seleccionados aleatoriamente de la secuencia dada, permitiendo repeticiones
print(ganador3("Ana", "Luis", "María", "Carlos"))
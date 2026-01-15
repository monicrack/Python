'''En una tupla con números del 1 al 10, cuenta cuántos números impares hay de cada uno y muestra el resultado.'''
numeros=(1,1,2,3,4,5,5,5,6,7,8,9,9,10)
contador=0
contar_unos=numeros.count(1)
contar_tres=numeros.count(3)    
contar_cinco=numeros.count(5)
contar_siete=numeros.count(7)
contar_nueve=numeros.count(9)
print("Del número 1 hay: ",contar_unos)
print("Del número 3 hay: ",contar_tres)          
print("Del número 5 hay: ",contar_cinco)
print("Del número 7 hay: ",contar_siete)
print("Del número 9 hay: ",contar_nueve) 
contador=contar_unos+contar_tres+contar_cinco+contar_siete+contar_nueve
print("En total hay ",contador," números impares")

'''Crea una función llamada `filtrar_pares` que reciba una lista de números
enteros y devuelva una nueva lista solo con los números pares.'''
def filtrar_pares(numeros):
    pares=[]
    contador=0
    for numero in numeros:
        if numero%2==0:
            pares.append(numero)
            contador+=1
    print("Total de números pares: ", contador)
    return(f"Todos los pares de la lista: {pares}")
    

lista_introducida = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = filtrar_pares(lista_introducida)
print(resultado)


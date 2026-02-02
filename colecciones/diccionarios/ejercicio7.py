'''Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra 
y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste'''
cesta={}
while True:
    terminar="X".lower()
    print("Para terminar pulsa X")
    articulo=input("Introduce un artículo en la cesta: ").capitalize()
    if articulo == "X":
        break
    precio=float(input("Introduce el precio del artículo: "))
    
    cesta[articulo]=precio
print("Lista de la compra") 
total = 0 
for articulo, precio in cesta.items(): 
    print(f"{articulo}\t{precio} €") 
    total += precio 
print(f"Total\t{total} €")

'''print("*************************")
cesta_compra = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta_compra[item] = precio
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
coste = 0
print('Lista de la compra')
for item, precio in cesta_compra.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)'''
    

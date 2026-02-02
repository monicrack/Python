'''Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura 
y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una 
nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará 
por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura 
se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación 
el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente 
de cobro.'''
'''facturas = {}
cobrado = 0
pendiente = 0
more = ''
while more != 'T':
    if more == 'A':
        clave = input('Introduce el número de la factura: ')
        coste = float(input('Introduce el coste de la factura: '))
        facturas[clave] = coste
        pendiente += coste
    if more == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste
    print('Recaudado:', cobrado)
    print('Pendiente de cobro: ', pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')'''

facturas = {}
cobrado = 0

while True:
    print("\n¿Qué deseas hacer?")
    print("1. Añadir factura")
    print("2. Pagar factura")
    print("3. Terminar")
    opcion = input("Elige una opción (1/2/3): ")

    if opcion == "1":
        numero = input("Introduce el número de factura: ")
        coste = float(input("Introduce el coste de la factura: "))
        facturas[numero] = coste
        print(f"Factura {numero} añadida correctamente.")

        # Mostrar totales tras la operación
        pendiente = sum(facturas.values())
        print(f"Cantidad cobrada hasta el momento: {cobrado}")
        print(f"Cantidad pendiente de cobro: {pendiente}")

    elif opcion == "2":
        numero = input("Introduce el número de factura a pagar: ")
        if numero in facturas:
            cobrado += facturas[numero]
            del facturas[numero]
            print(f"Factura {numero} pagada correctamente.")
        else:
            print("La factura no existe.")

        # Mostrar totales tras la operación
        pendiente = sum(facturas.values())
        print(f"Cantidad cobrada hasta el momento: {cobrado}")
        print(f"Cantidad pendiente de cobro: {pendiente}")

    elif opcion == "3":
        print("Programa terminado.")
        break

    else:
        print("Opción no válida.")

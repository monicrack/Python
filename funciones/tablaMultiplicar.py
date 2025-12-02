'''Crea una función llamada `tabla_multiplicar` que reciba:
- numero (int)
- hasta (int), como argumento por palabra clave, con valor por defecto 10
La función debe devolver una lista con la tabla de multiplicar del número
hasta el valor indicado.'''
def tabla_multiplicar(numero, hasta=10):
    lista = []
    for i in range(1, hasta + 1):   # desde 1 hasta 'hasta'
        lista.append(f"{numero} * {i} = {numero * i}")
    return lista

tabla_introducida=int(input("Qué tablas deseas: "))

resultado = tabla_multiplicar(tabla_introducida)
print("La tabla es:")
for linea in resultado:
    print(linea)

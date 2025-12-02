'''Crea una función llamada `calcular_descuento` que reciba:
- precio_original (float)
- descuento (float), como argumento por palabra clave, con valor por defecto 10
La función debe devolver el precio final tras aplicar el descuento.'''
def calcular_descuento(precio_original,descuento=10):
    precio_final= precio_original-descuento
    return (f"El precio con descuento es: {precio_final}")

print(calcular_descuento(100))
print(calcular_descuento(100,descuento=30))
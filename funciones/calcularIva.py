'''Crea una función llamada `calcular_precio` que reciba:
- precio_base (float)
- iva (float), como argumento por palabra clave, con valor por defecto 21
La función debe devolver el precio final con el IVA aplicado.'''

def calcular_precio(precio_base,iva=21):
    iva=float(21*precio_base)/100
    precio_total= precio_base + iva
    print(f"El precio total con IVA es: {precio_total:.2f} ")

precio_Introducido=calcular_precio(200,iva=10)
precio_Introducido=calcular_precio(200)


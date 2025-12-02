'''funcion calcular precio_entrada ademas del precio normal de la entrada que por defecto 10
la edad del asistente y si es estudiante si es menor de 18 o estudiante descuento del 50%
dtos no acumulables'''
def precio_entrada(edad, precio=10 , estudiante=False):
    descuento = (50*precio)/100
    precio_descuento = precio - descuento
    
    if edad < 18 or estudiante:
        return precio_descuento
    else:
        return precio
    
print (f"El precio de la entrada es: {precio_entrada(22,estudiante=False)}")
    

'''Crea una función llamada `formatear_nombre` que reciba:
- nombre (str)
- apellido (str)
- orden (str), con valor por defecto "nombre_apellido" 
(el otro valor que podría tomar sería apellido_nombre)
La función debe devolver el nombre completo en el orden indicado.'''
def formatear_nombre(nombre,apellido, orden="nombre_apellido"):
    if nombre=="":
        return("No has introducido nada")
    elif nombre.isdigit():
        return("Has introducido un valor númerico en el nombre")
    elif apellido=="":
        return("No has introducido ningún apellido")
    elif apellido.isdigit():
        return("Has introducido números en el apellido")
    else:
        if orden=="nombre_apellido":
            return f"{nombre} {apellido}"
        elif orden=="apellido_nombre":
            return f"{apellido} {nombre}"
        else:
            return "Orden no válido"

print(formatear_nombre("", "Cortés"))
print("*********")
print(formatear_nombre("Monica", ""))
print("*************")
print(formatear_nombre("1234", "Cortés"))
print("************")
print(formatear_nombre("Monica", "1234"))
print("**************")
print(formatear_nombre("Monica", "Cortés"))
print("**************")
print(formatear_nombre("Monica", "Cortés", "apellido_nombre"))
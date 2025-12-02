'''Crea una función llamada `crear_usuario` que reciba los 
siguientes argumentos por palabra clave:
- nombre (str)
- email (str)
- activo (bool), con valor por defecto True
La función debe devolver una lista sólo de los usuarios activos 
con los datos del usuario en el orden: [nombre, email, activo].'''

def crear_usuario (nombre, email, activo=True):
   if activo:
    return [nombre, email,activo]
   return[]
   

usuario1 = crear_usuario(nombre="Mónica", email="monica@gmail.com",activo=True)
usuario2 = crear_usuario(nombre="Juan", email="juan@gmail.com", activo=False)
print(usuario1)
print(usuario2)
    
'''usuario_Introducido=input("Introduce el usuario: ")
usuarioIntroducido=usuario_Introducido.lower()
email_Introducido=input("Introduce el email:")
email_Introducido=email_Introducido.lower()
usuario_activo=input("El usuario está activo: si/ no ")
if usuario_activo.lower()=="si":
  usuario_activo=True
elif usuario_activo.lower()=="no":
  usuario_activo=False

usuario=crear_usuario(usuario_Introducido,email_Introducido,usuario_activo)

print("Usuario: ",usuario)'''

# Mostrar el resultado con formato
'''if usuario:  # si la lista no está vacía
    if usuario[2]:
        estado = "sí"
    else:
        estado = "no"
    print(f"Usuario: Nombre: {usuario[0]} | Correo: {usuario[1]} | Usuario activo: {estado}")
else:
    print("Usuario inactivo, no se guarda información.")'''


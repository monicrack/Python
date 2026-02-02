'''Escribir un programa que guarde en una variable el diccionario
 {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa
  y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''
moneda={"Euro":"€", "Dollar":"$", "Yen":"¥"}
divisa=input("¿Qué divisa quieres? ").capitalize()
if divisa in moneda:
    print(moneda[divisa])
else:
    print("La divisa no esta en el diccionario")


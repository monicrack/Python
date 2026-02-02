frase = input("Introduce una frase: ").lower()

vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "á":0, "é":0, "í":0, "ó":0,"ú":0 }

for letra in frase:
    if letra in vocales:
        vocales[letra] += 1

print("Cantidad de cada vocal:")
for vocal, cantidad in vocales.items():
    print(f"{vocal}: {cantidad}")
###################################################
frase = input("Introduce una frase: ").lower()

vocales = {
    "a": 0, "e": 0, "i": 0, "o": 0, "u": 0
}

equivalencias = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u"
}

for letra in frase:
    if letra in vocales:
        vocales[letra] += 1
    elif letra in equivalencias:
        vocales[equivalencias[letra]] += 1

print("\nTotal de vocales (agrupando tildes):")
for vocal, cantidad in vocales.items():
    print(f"{vocal}: {cantidad}")

##############################33
coleccion = ["pera", "manzana", "uva", "pera", "kiwi", "pera"]
coleccion.sort()  # Aseguramos que esté ordenada

elemento = input("Introduce un elemento: ")

# Buscar todas las posiciones donde aparece
posiciones = [i for i, x in enumerate(coleccion) if x == elemento]

if posiciones:
    print(f"El elemento '{elemento}' aparece en las posiciones: {posiciones}")
else:
    print(f"El elemento '{elemento}' no está en la colección.")
    # Insertarlo manteniendo el orden
    coleccion.append(elemento)
    coleccion.sort()
    nueva_pos = [i for i, x in enumerate(coleccion) if x == elemento]
    print(f"Se ha añadido '{elemento}' en la posición {nueva_pos[0]}.")

print("\nColección actualizada:")
print(coleccion)

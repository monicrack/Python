'''que número de letra le corresponde al año feliz 20262026 para calcularlo necesito
la suma de cada digito calculando la letra oficial obtenida
con la fórmula del DNI (número % 23 usando la cadena "TRWAGMYFPDXBNJZSQVHLCKE").'''

numero = input("Introduce tu número de DNI (sin letra): ")

numero_int = int(numero) 

letras = "TRWAGMYFPDXBNJZSQVHLCKE"

indice = numero_int % 23
letra = letras[indice]

print("Número DNI:", numero_int)
print("Índice:", indice)
print("Letra oficial DNI:", letra)


'''dada una lista de años comprueba si son años felices, un numero feliz es cuando la suma de sus cuadrados
de sus cifras el resultado es 1'''
def es_feliz(numero):
    while numero != 1 and numero != 4:
        suma = 0
        for digitos in str(numero):
            suma += int(digitos) ** 2
        numero = suma
    return numero == 1

anios_felices = [2026, 2000, 1998, 1996, 1974, 1967, 1918, 2012]

for anio in anios_felices:
    if es_feliz(anio):
        print(anio, "Es un año feliz")
    else:
        print(anio, "NO es un año feliz")

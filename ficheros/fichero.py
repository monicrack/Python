'''try:
    f = open("ficheros/demofile.txt")
    print(f.read()) #solo lectura
except FileNotFoundError:
    print("El fichero no existe")'''
#import os
#print("Carpeta actual:", os.getcwd()) #comprobar la carpeta donde esta el fichero
#print("¿Existe el archivo?", os.path.exists("demofile.txt")) #devuelve true o false
'''with open("ficheros/demofile.txt") as f:
  print(f.read(5))'''

'''with open ("ficheros/demofile.txt") as f:
    print(f.readline())
    print(f.readline())'''
'''with open("ficheros/demofile.txt", "a") as f:
  f.write("Ahora el archivo tiene más contenido")
with open ("ficheros/demofile.txt") as f:
   print(f.read())'''
with open("ficheros/demofile.txt", "w") as f:
  f.write("sobre escribe el archivo")
with open ("ficheros/demofile.txt") as f:
    print(f.read())
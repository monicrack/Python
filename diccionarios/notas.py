diccionario = {
    "alumno_1":{
        "nombre":"Juan",
        "nota":3
    },
    "alumno_2":{
        "nombre":"Pedro",
        "nota":5
    },
    "alumno_3":{
        "nombre":"Rosa",
        "nota":2
    },
    "alumno_4":{
        "nombre":"Raúl",
        "nota":1
    },
    "alumno_3":{
        "nombre":"Ramón",
        "nota":5
    }
}
print(diccionario)
for alumno, notas in diccionario.items():
    if notas["nota"]<5:
        notas["nota"]=5
print(diccionario)
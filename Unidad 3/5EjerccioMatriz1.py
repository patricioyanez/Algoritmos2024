matriz = [
    [3,10,4,16],
    [1,7,8,-7],
    [9,-1,3,9]
]

datos = ""
for fila in matriz:
    for valor in fila:
#        datos += "  " if columna < 10 and columna > -1 else " "
        if valor > -1 and valor < 10:
            datos += "  "
        else: 
            datos += " "
        datos += str(valor)
    datos += "\n"

print(datos) 
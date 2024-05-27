matriz = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16],
            [17,18,19,20],
            [21,22,23,24],
            [25,26,27,28],
            [29,30,31,32],
            [33,34,35,36],
            [37,38,39,40]
        ]



filas = 10
columnas = 10
valor = 1
matriz = [[valor + j + i*columnas for j in range(columnas)] for i in range(filas)]

datos = ""
for fila in matriz:
    for indice in range(len(fila)):
        if fila[indice] < 10:
            datos += " "
        datos += str(fila[indice])

        if indice == 1:
            datos += "   "
        else:
            datos += " " 
    datos += "\n"

print(datos) 

# generar automaticamente los numeros del 1 al 40 para
# completar la matriz
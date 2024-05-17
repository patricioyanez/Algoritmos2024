
lista = [1,2,3, 'p', 'a','z', 60]

matriz = [
            [1,3,5,7],
            ['a', 'b', 'g', 50]
        ]
# recorrer la filas de la matriz
for x in matriz:
    print(x)

# mostrar un valor de la matriz
print("el valor es:", matriz[1][2])

# cambiar un valor de la matriz
matriz[1][2] = 'pashe'
print("el valor es:", matriz[1][2])
# obtener cada valor de una lista de la matriz
for x in matriz:
    print("valor:", x[0])
    print("valor:", x[1])
    print("valor:", x[2])
    print("valor:", x[3])

print("=== Uso de 2 for para recorrer matriz")
for fila in matriz:
    for columna in fila:        
        print("valor:", columna)


# matriz de 3 dimensiones
matriz3D = [
                [
                    [1,2,3,4],
                    [4,2,1,6],
                ],
                [
                    [1,2,3,4],
                    [4,2,1,'a'],
                ],
                [
                    [1,2,3,4],
                    [4,2,1,6],
                ],
            ]
# tamaño de la matriz: 3,2,4
print("El valor de la m3d:", matriz3D[1][1][3])
matriz3D[2][1][3] = "te pille"

#Ejercicio: recorer la matriz 3d anterior:
print("=== *** ejercicio")
for dimension in matriz3D:
    for fila in dimension:
        for columna in fila:
            print("EL valor es:", columna)



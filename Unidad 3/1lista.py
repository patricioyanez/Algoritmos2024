nombres = [] # es una lista sin valores

#lista con numeros
numeros = [1,2,3,4,5,6,7]

# acceder a un valor de la lista mediante
# indice
# el indice inicia del cero
print("El numero es:", numeros[3])

# recorrer
for temporal in numeros:
    print(temporal)

# permite agregar elementos a la lista
numeros.append(10)
numeros.append(12)
numeros.append(15)
numeros.append("pashe pashe pashe")

# mostrar todos los valores de la lista
print("*** Mostrar nuevos valores ***")
for temporal in numeros:
    print(temporal)

# ver contenido de la lista
print(numeros)

# eliminar un elemento
print("=== Eliminar un elemento ===")
numeros.remove("pashe pashe pashe")
print(numeros)

numeros.append(14)
numeros.reverse()
print(numeros)

numeros.sort()
print(numeros)

# agregar un 8 y ordenar 
# de mayor a menor y mostrar

numeros.append(8)
numeros.sort()
numeros.reverse()
print(numeros)

# crear una aplicación
# que permita almacenar las
# notas que el usuario
# determine
# dar la opcion de ingreso,
# promediar y salir
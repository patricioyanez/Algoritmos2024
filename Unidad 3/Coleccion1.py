# crea una lista
lista = ["academica", "administrativa", "contabilidad", "1", "1"]
# crea una tupla
tupla = ("academica", "administrativa", "contabilidad", "1", "1")

print(lista)
print(tupla)
print(lista[1])
print(tupla[1])

# recorrer
for valor in tupla:
    print("valor: ",valor)

miConjunto = {1,2,3,4,5,6, 1,2,3,4,5,6}
print("**** Conjunto ****")
print(miConjunto)
# agregar elementos
miConjunto.add(7)
miConjunto.add(1)

# eliminar elementos
miConjunto.remove(5)
miConjunto.pop()
print(miConjunto)
miConjunto.discard(10)

for valor in miConjunto:
    print("valor set: ",valor)


# diccionario
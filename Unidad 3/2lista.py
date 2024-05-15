lista = ["a", "b", "10", "maría", "ignacia", 50, 60]

print(lista)

print("**** recorrer lista *****")
for valor in lista:
    print("El valor es:", valor)


lista.insert(2, "Nuevo")
print(lista)

item = lista.index(50) # devuelve el indice del valor buscado
print("El valor fue encontrado en el indice:" , item)
#item = lista.index(150) ## error al no encontrar el elemento dentro de la lista
#print("El valor fue encontrado en el indice:" , item)

print("=== Eliminar datos ===")
lista.remove("10")
print(lista)

lista.pop() # elimina el último elemento
print(lista)
lista.pop(0) # elimina el elemento del indice indicado
print(lista)


print("************** Agregar otro elemento **********************")
nombres = ["Juan", "Pedro", "Diego", 30, 40, 100]
# unir 2 listas
lista.extend(nombres)
print(lista)

nombre = "Juan Pablo"

for letra in nombre:
    print(letra)


for letra in "Patricio p":
    print(letra, ord(letra)) # Ñ ñ @ \  codigo ascii

lista.append(100)
print("Contar elementos que estan en la lista")
indice = lista.count(100)
print(lista)
print(f"Cantidad de elementos: {indice}")
indice = lista.count('maría')
print(f"Cantidad de elementos: {indice}")
indice = lista.count('ma')
print(f"Cantidad de elementos: {indice}")


lista2 = lista
print(lista)
print(lista2)
lista.clear() # limpiar la lista o la vacia
print(lista)
print(lista2)
a = 1
b = a
a = 0
print(b)
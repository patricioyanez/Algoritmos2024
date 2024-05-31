print("**** Ingrese 3 nombres: ")
lista=[]
lista.append(input("nombre 1:"))
lista.append(input("nombre 2:"))
lista.append(input("nombre 3:"))

nombre = lista[0]
for n in lista:
    if len(nombre)< len(n):
        nombre = n

nombreLargo = max(lista, key=len)
print("El nombre con más letras es:", nombre)
print("El nombre con más letras es:", nombreLargo)
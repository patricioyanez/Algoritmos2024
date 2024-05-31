nombres = ["Luis", "Ana", "Diego"]
apellidos=["Perez", "Diaz", "Inostroza"]

nombresAux = nombres.copy() # duplica la lista
apellidosAux = [] # guarda los apellidos ordenados según el nombre de la persona
nombresAux.sort() # ordena la lista de nombres duplicada no altera la lista original
print(nombres)
print(apellidos)


for x in nombresAux:
    indice = nombres.index(x) # busca indice de nombre original
    apellidosAux.append(apellidos[indice])# segun el indice ordena el apellido

for indice in range(len(nombresAux)):
    print(f"nombre:{nombresAux[indice]} {apellidosAux[indice]}")
import os
opcion = ""
nombres = []
while opcion.upper() != "NO":
    os.system("cls")
    print("==== ingreso de nombre ====")
    nombre = input("Ingrese un nombre:")
    nombres.append(nombre)
    opcion = input("Presione enter para continuar o escriba no para salir:")

print(nombres)
# luis, ana, pedro, alejandro
nombre = nombres[0] # entregar el 1er nombre de la lista
for aux in nombres:
#    print("-",nombre,"-", aux)
    if len(aux) < len(nombre): # compara la cantidad de caracteres
        nombre = aux

nombres.remove(nombre) # elimina el nombre con menor cantidad de caractes
print(nombres)
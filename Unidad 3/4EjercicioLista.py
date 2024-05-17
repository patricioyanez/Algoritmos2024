nombres = []
print("==== INGRESE NOMBRES ====")
nombre = input("Ingrese 1er nombre:")
nombres.append(nombre)
nombre = input("Ingrese 2do nombre:")
nombres.append(nombre)
nombre = input("Ingrese 3er nombre:")
nombres.append(nombre)

nombreAuxiliar = ""
for nombre in nombres:
    if len(nombre) > len(nombreAuxiliar):
        nombreAuxiliar = nombre
print(f"{nombreAuxiliar} es el nombre con más caracteres")

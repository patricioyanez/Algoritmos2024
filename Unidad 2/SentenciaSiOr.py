# Solicitar nombre y apellido 
# saludar al usuario si ingresa nombre o apellido

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

print("\n\n**** usando OR  *******")
if nombre != "" or apellido != "":
    print(f"Hola {nombre} {apellido}")
else:
    print("or: No ingreso los datos solicitados")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

if nombre != "" and apellido != "":
    print(f"Hola {nombre} {apellido}")
    print("Hola", nombre, apellido)
else:
    print("and: No ingreso los datos solicitados")

print("\n\n**** usando OR  *******")
if nombre != "" or apellido != "":
    print(f"Hola {nombre} {apellido}")
else:
    print("or: No ingreso los datos solicitados")


## ejercicios:
# para controlar la entrada a la sala de clases
# preguntar al alumno si esta matriculado
# y si inscribio en la asignatura
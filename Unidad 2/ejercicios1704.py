print("*****  Bienvenido al mundo de la programación *****")
print("Ingrese su nombre:")
nombre = input()
print(f"Hola {nombre}")

x = input("Ingrese el valor de x: ")
x = int(x) # convierte el str en  un entero para poder operar con él.
resultado = (x**2 + 3*x + 1) / 4
print(f"El resultado es: {resultado}")

# Crear una app, que permita registrar productos de una tienda de abarrotes
# Los requisitos son:
# crear menu con las siguientes opciones:
# 
# Crear archivo con formato csv
# Ingresar productos (codigo de barra, nombre, marca, precio, stock)
# Listar productos
# Eliminar producto
# Modificar stock actual
# 
# Usar funciones, listas y librerias vistas en clases.
# Crear repositorio en github y guardar los cambios


import csv
import os

def crearArchivo():
    with open('RegistroDeProducto.csv', 'w', newline='') as doc:
        csv.writer(doc)
        print("==========> Archivo creado")

opcion = ""
while opcion != "6":
    os.system("cls")
    print("******* Menú *******")
    print("1.- Crear archivo")
    print("2.- Ingresar producto")
    print("3.- Listar producto")
    print("4.- Eliminar producto")
    print("5.- Modificar Stock")
    print("6.- Salir")
    opcion = input("Ingrese opción:")

    if opcion not in ("1","2","3","4","5","6"):
        print("La opción ingresada no es válida")    

    if opcion == "6":
        break

    if opcion == "1":
        crearArchivo()

    input("Presionen enter para continuar....")
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

def ingresarProducto():
    print("======= INGRESO DE PRODUCTO ==========")
    codigo = input("Codigo de barra : ")

    if not codigo.isdigit():
        print("============> Error: Codigo de barra no es númerico")
        return 
    
    nombre = input("Nombre          : ")

    if len(nombre.strip()) == 0:        
        print("============> Error: El nombre no fue especificado")
        return 

    marca  = input("Marca           : ")
    if len(marca.strip()) == 0:        
        print("============> Error: La marca no fue especificada")
        return
    
    precio = input("Precio          : ")
    if not precio.isdigit():
        print("============> Error: Valor del precio no es válido")
        return 
    
    stock  = input("Stock           : ")
    if not stock.isdigit():
        print("============> Error: Valor del stock no es válido")
        return 
# crea la lista para guardar en el archivo
    fila = [codigo, nombre, marca, precio, stock]

# guardar la lista en el archivo
    with open('RegistroDeProducto.csv', 'a', newline='') as doc:
        escribir = csv.writer(doc)
        escribir.writerow(fila)        
        print("==========> Datos guardados!!!")

def listarProducto():
    print("==== Listado de productos ====")   
    with open('RegistroDeProducto.csv', 'r', newline='') as documento: 
        datosDocumento = csv.reader(documento)
        for fila in datosDocumento:
            print("------------------------------")
            print("Codigo   : ", fila[0])
            print("Nombre   : ", fila[1])
            print("Marca    : ", fila[2])
            print("Precio   : ", fila[3])
            print("Stock    : ", fila[4])
            print("------------------------------")

def modificarStock():
    print("==== Modificar stock de productos ====")
    filasDocumento = []
    with open('RegistroDeProducto.csv', 'r', newline='') as documento: 
        datosDocumento = csv.reader(documento)
        for fila in datosDocumento:
            filasDocumento.append( fila)

    codigo = input("Ingrese Codigo de barra : ")

    if not codigo.isdigit():
        print("============> Error: Codigo de barra no es númerico")
        return 
#987654321
    for fila in filasDocumento:
        if fila[0] == codigo:
            stock = int(input("ingresar nuevo stock: "))
            fila[4] = stock
            print("=========> stock modificado")

    with open('RegistroDeProducto.csv', 'w', newline='') as documento: 
        escribir = csv.writer(documento)
        escribir.writerows(filasDocumento) # guarda la matriz

def eliminarProducto():
    pass

opcion = ""
while opcion != "6":
    os.system("cls")
    print("******* Menú *******")
    print("1.- Crear archivo")
    print("2.- Ingresar producto")
    print("3.- Listar producto")
    print("4.- Modificar Stock")
    print("5.- Eliminar producto")
    print("6.- Salir")
    opcion = input("Ingrese opción:")

    if opcion not in ("1","2","3","4","5","6"):
        print("La opción ingresada no es válida")    

    if opcion == "6":
        break

    if opcion == "1":
        crearArchivo()
    elif opcion == "2":
        ingresarProducto()
    elif opcion == "3":
        listarProducto()
    elif opcion == "4":
        modificarStock()
    elif opcion == "5":
        eliminarProducto()

    input("Presionen enter para continuar....")
# EJERCICIO PARA HOY:
# Crear una aplicación que permita registrar los ingresos a un recinto
# para el ingreso se requiere el rut, validar si esta bueno, antes de permitir
# el ingreso
#  2.- Todas las personas deben registrar su rut, nombre y edad. 
#       Si existe dar la bienvenida 
# mencionando su nombre.
# los datos deben ser almacenados en un archivo .csv
# Otras opciones a realizar: 
#   3.- listar las personas que han ingresado.
#   1.- Creación de archivo
#   4.- Mostrar estadisticas según rango etario que ha entrado al recinto.
#   usar funciones para cada opcion y para la validación del rut

import os
import csv
opcion = ""

def crearArchivo():
    print("*******************************************")
    print("|========== Creación de archivo ==========|")
    print("*******************************************")
    with open('9FuncionesEjercicio3.csv', 'w',newline='') as documento:
        escribir = csv.writer(documento)
        print("=====> Documento creado")

def registrar():
    print("*******************************************")
    print("|==========  Registrar Ingreso  ==========|")
    print("*******************************************")
    print("Ingrese los siguientes datos:")
    rut = input("rut:")
    nombre = input("nombre:")
    anio = input("año de nacimiento:")
    fila = [rut,nombre,anio]
    with open('9FuncionesEjercicio3.csv', 'a', newline='') as documento:
        escribir = csv.writer(documento)
        escribir.writerow(fila)
        print("Datos guardados")
        input("Presionene enter para continuar...")
def listar():
    pass
def estadisticas():
    pass

while opcion != "5":
    os.system("cls")
    print(""" **** Menú ****
          1.- Crear archivo
          2.- RegistrarIngreso
          3.- Listar
          4.- Estadisticas
          5.- Salir""")
    opcion = input("Ingrese opción: ")

    if opcion not in ['1','2','3','4','5']:
        print("Opción no válida")
    
    if opcion == "5":
        print("Aplicación Cerrada")
        break

    if opcion == "1":
        crearArchivo()
    elif opcion == "2":
        registrar()
    elif opcion == "3":
        listar()
    elif opcion == "4":
        estadisticas()
    
    input("Presione enter para continuar...")
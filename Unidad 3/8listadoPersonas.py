# Ejercicios:
# 
# Crear una aplicación que permita:
# 
# 1.- Crear archivo
# 2.- Guardar el rut, nombre y año de nacimiento en un archivo CSV
# 3.- Mostrar todos los datos almacenados
# 4.- Calcular la edad de nacimiento del rut seleccionado y mostrar sus datos
# 5.- salir

import os
import csv
opcion = ""
while opcion != "5":
    os.system('cls')
    print(""" ************ MENÚ ************
        1.- Crear archivo
        2.- Ingresar datos
        3.- Listar datos
        4.- Ver edad según rut
        5.- Salir""")
    opcion = input("Ingresar opción:")

    if opcion == "1":        
        print("==== Creación de archivos ====")
        with open('8listadoPersonas.csv', 'w', newline='') as documento:
            escribir = csv.writer(documento)

            print("Archivo creado")
            input("Presionene enter para continuar...")
    elif opcion == "2":
        print("==== Guardar datos ====")
        print("Ingrese los siguientes datos:")
        rut = input("rut:")
        nombre = input("nombre:")
        anio = input("año de nacimiento:")
        fila = [rut,nombre,anio]
        with open('8listadoPersonas.csv', 'a', newline='') as documento:
            escribir = csv.writer(documento)
            escribir.writerow(fila)
            print("Datos guardados")
            input("Presionene enter para continuar...")
    elif opcion == "3":
        print("==== Listar datos ====")   
        with open('8listadoPersonas.csv', 'r', newline='') as documento: 
            datosDocumento = csv.reader(documento)
            for fila in datosDocumento:
                print(f"Rut : {fila[0]} Nombre: {fila[1]} Año de Nacimiento: {fila[2]} ")
        print("Datos guardados")
        input("Presionene enter para continuar...")
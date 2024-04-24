import os
opcion = ""

while opcion != "0":
    os.system("cls")
    print("***** Menú Principal ****")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("0.- Salir")

    opcion = input("Ingrese la opción")

    if opcion not in ["0", "1", "2","3", "4"]:
        print("La opción no es válida")
    else:
        # opciones correctas
        # pedir los numeros y verificar que sean int
        

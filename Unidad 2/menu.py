import os
opcion = ""

while opcion != "0":
    os.system("cls")
    print("***** Menú Principal ****")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- factor")
    print("0.- Salir")

    opcion = input("Ingrese la opción: ")

    if opcion not in ["0", "1", "2","3", "4", "5"]:
        print("La opción no es válida")
    else:
        # opciones correctas
        # pedir los numeros y verificar que sean int
        try:
            numero1 = int(input("Ingrese primer valor   : "))
            numero2 = int(input("Ingrese segundo valor  : "))
        except:
            print("Valor ingresado no es valido")
            input("Presione enter para continuar....")
            continue

        if opcion == "1":
            resultado = numero1 + numero2
            print("El resultado es: ", resultado )
        elif opcion == "2":
            resultado = numero1 - numero2
            print("El resultado es: ", resultado )
        elif opcion == "3":
            resultado = numero1 * numero2
            print("El resultado es: ", resultado )
        if opcion == "4":
            resultado = numero1 / numero2
            print("El resultado es: ", resultado )

    input("Presione enter para continuar....")
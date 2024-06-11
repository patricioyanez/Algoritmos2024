# crear calculadora usando funciones que
# reciben 2 numeros
# devolver el resultado y mostrar en pantalla
# las operaciones a usar son:
# +,-,* y /

import os
opcion = ""

def sumar(numero1, numero2):
    return numero1 + numero2
def restar(numero1, numero2):
    return numero1 - numero2
def multiplicar(numero1, numero2):
    return numero1 * numero2
def dividir(numero1, numero2):
    if numero2 == 0:
        print("Error, no se puede dividir por cero")
        return 0
    return numero1 / numero2

while opcion != "5":
    os.system("cls")
    print(""" **** Menú ****
          1.- Sumar
          2.- Restar
          3.- Multiplicar
          4.- Dividir
          5.- Salir""")
    opcion = input("Ingrese opción: ")

    if opcion not in ['1','2','3','4','5']:
        print("Opción no válida")
        input("Presione enter para continuar...")
    
    if opcion == "5":
        print("Aplicación Cerrada")
        break

    try:
        numero1 = int(input("Ingrese 1er numero: "))
        numero2 = int(input("Ingrese 2do numero: "))
    except:
        print("Numero no es valido")
        input("Presione enter para continuar...")
        continue

    resultado = 0
    if opcion == "1":
        resultado = sumar(numero1, numero2)
    elif opcion == "2":
        resultado = restar(numero1, numero2)
    elif opcion == "3":
        resultado = multiplicar(numero1, numero2)
    elif opcion == "4":
        resultado = dividir(numero1, numero2)
    
    print("El resultado es:", resultado)
    input("Presione enter para continuar...")
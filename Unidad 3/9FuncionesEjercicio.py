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
    print(""" **** Menú ****
          1.- Sumar
          2.- Restar
          3.- Multiplicar
          4.- Dividir
          5.- Salir
          """)
    opcion = input("Ingrese opción")

    if opcion not in ['1','2','3','4','5']:
        print("Opción no válida")
        input("Presione enter para continuar...")
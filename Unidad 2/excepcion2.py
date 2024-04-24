print("***** Maquina para dividir *****")
dividendo = input("Ingrese el dividendo: ")
divisor   = input("Ingrese el dividor  : ")

try:
    dividendo = int(dividendo)
    divisor = int(divisor)
    cociente = dividendo / divisor
    print("El resultado es: ", cociente )
except ZeroDivisionError:
    print("No se puede dividir por cero")
except TypeError:
    print("Ocurrio un error al concatenar")
except ValueError:
    print("Ocurrio un error de conversión")
else:
    print("Operación realizada")
finally:
    print("Adios querido usuario.")

print("****** Fin de aplicación ********")
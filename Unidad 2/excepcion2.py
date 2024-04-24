print("***** Maquina para dividir *****")
dividendo = input("Ingrese el dividendo: ")
divisor   = input("Ingrese el dividor  : ")

try:
    dividendo = int(dividendo)
    divisor = int(divisor)
    cociente = dividendo / divisor
    print("El resultado es: ", cociente1 )
except NameError: # se Ejecuta cuando la variable no fue definida
     print("La variable no existe")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except TypeError:
    print("Ocurrio un error al concatenar")
except ValueError:
    print("Ocurrio un error de conversión")
except: # se ejecuta cuando la excepción NO esta definida
    print("Error en alguna parte...")
else: # se ejecuta cuando no hay excepción
    print("Operación realizada")
finally: # se ejecuta siempre
    print("Adios querido usuario.")

print("****** Fin de aplicación ********")
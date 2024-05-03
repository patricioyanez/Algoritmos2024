import os
opcion = ""
sumaEdad = 0
cantidadPersonas = 0
cantidadHombres = 0
cantidadMujeres = 0
cantidadOtros = 0
cantidadNino = 0
cantidadJoven= 0
cantidadAdulto=0
# agregar opcion de mostrar resultados
# agregar validación de genero
# resetear los valores ingresados

while opcion != "0":
    os.system("cls") # clean screen
    # opciones del programa
    print("***** Gym El Mamado *****")
    print("1.- Ingreso de datos") 
    print("2.- Mostrar resultados") 
    print("3.- Resetear datos") 
    print("0.- Salir")
    # solicitar al usuario opción a ejecutar
    opcion = input("Ingrese la opción: ")
    
    # validar si la opción ingresada es correcta
    if opcion not in ["0","1","2", "3"]:
        print("La opción no es válida :(")
        input("Presione enter para continuar....")

    else:
        if opcion == "0":
            break
        elif opcion == "1":
            print("==== Ingrese los siguietes datos ====")
            edad = input("EDAD: ")
            genero= input("Seleccione género:\n (1)Hombre\n (2)Mujer\n (3)Otro\n Ingrese opción: ")

            try:
                edad = int(edad)
            except:
                print("La edad no es válida")
                input("Presione enter para continuar...")
                continue # se devuelve al menú
    #
    # 1.- Validar que las opciones del genero sean valida. Enviar mensaje si no es correcto
    #
            if genero not in ["1", "2", "3"]:
                print("La opción no es válida :(")
                input("Presione enter para continuar....")
                continue # se devuelve al menú

            # la edad fue ingresada correctamente
            if edad >= 10 and edad <= 17:            
                cantidadNino = cantidadNino + 1 # contador
            elif edad <= 29:
                cantidadJoven += 1 # contador
            elif edad <= 50:
                cantidadAdulto += 1 # contador
            else:
                print("La edad ingresada esta fuera del rango")
                input("Presione enter para continuar...")
                continue

            # sumar las edades y contar cantidad de personas 
            # dentro del rango etario
            sumaEdad = sumaEdad + edad # acumulador
            cantidadPersonas += 1  

            if genero == "1":
                cantidadHombres += 1
            elif genero == "2":
                cantidadMujeres += 1
            elif genero == "3":
                cantidadOtros += 1

#
# 2.- Agregar una opción que permita ver los resultados capturados hasta el momento
#
        elif opcion == "2":
            print("El promedio de edad es: ", round((sumaEdad/cantidadPersonas), 1))
            print("Cantidades por genero:")
            print("Hombres  : ", cantidadHombres)
            print("Mujeres  : ", cantidadMujeres)
            print("Otros    : ", cantidadOtros)
            
            print("Cantidades por rango etario:")
            print("Niño     : ", cantidadNino)
            print("Joven    : ", cantidadJoven)
            print("Adulto   : ", cantidadAdulto)
            input("Presione enter para continuar....")

#
# 3.- Resetear los valores registrados por las variables
#
        elif opcion == "3":
            sumaEdad = 0
            cantidadPersonas = 0
            cantidadHombres = 0
            cantidadMujeres = 0
            cantidadOtros = 0
            cantidadNino = 0
            cantidadJoven= 0
            cantidadAdulto=0
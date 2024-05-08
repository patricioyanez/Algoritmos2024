import os
opcion = ""

patente = ""
marca = ""
modelo = ""
anioFabricacion = 0
tipoCombustible = ""
registros = ""

while opcion != "4":
    os.system("cls")
    print("====== Menú ======")
    print("1.- Registrar automovil")
    print("2.- Mantenimiento de automovil")
    print("3.- Consultar automovil")
    print("4.- Salir")
    opcion = input("Ingrese opción valida: ")

    # validar si la opcion es correcta
    if opcion not in ["1","2","3","4"]:
        print("===> El valor ingresado no es válido")
        input("presione enter para continuar...")
        continue
    
    # la opcion que ingreso el usuario es correcta, osea es 1,2,3 o 4
    if opcion == "1":
        print("***** INGRESO DE  AUTOMOVIL *****")
        patente = input("Ingrese la patente         : ")

        if len(patente) != 6:
            print("===> Patente ingresada no es válida")
            input("presione enter para continuar...")
            continue
        
        anioFabricacion = input("Ingrese año de fabricación : ")
        try:
            anioFabricacion = int(anioFabricacion) # convertir de str a int
        except:
            print("===> El año de fabricación no es válida")
            input("presione enter para continuar...")
            continue
        
        # el año de fabricación es un numero (int)
        if anioFabricacion < 1900 or anioFabricacion > 2024:            
            print("===> El año de fabricación esta fuera del rango")
            input("presione enter para continuar...")
            continue
        
        print("Ingrese el tipo de combustible:")
        print("b.- Bencina")
        print("d.- Diesel")
        print("e.- Eléctrico")
        print("h.- Hibrído")
        tipoCombustible = input("Ingrese opción: ")
        tipoCombustible = tipoCombustible.upper() # conviente el texto en mayúscula
        if tipoCombustible not in ["B","D","E","H"]:
            print("===> El tipo de combustible no es válido")
            input("presione enter para continuar...")
            continue
        
        marca = input("Ingrese la marca          : ")

        if len(marca) == 0:            
            print("===> No especifico marca")
            input("presione enter para continuar...")
            continue

        modelo = input("Ingrese la modelo         : ")

        if len(modelo) == 0:            
            print("===> No especifico modelo")
            input("presione enter para continuar...")
            continue
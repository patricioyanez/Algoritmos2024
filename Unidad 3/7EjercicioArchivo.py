opcion = ""
menu = """ ****** Menú *******
1.- Ingresar Nombre
2.- Listar
3.- Salir
"""
# crear archivo donde se guardará la información
with open("7EjercicioArchivo.txt", "w") as archivo:
    archivo.write("")


while opcion != "3":
    print(menu)
    opcion = input("Ingresar opción: ")

    if opcion not in ["1", "2", "3"]:
        print("Opción no valida. Vuelva a intentar.")
        input("Presione enter para continuar....")
        continue

    if opcion == "1":
        print("******* Ingreso de nombre **********")
        nombre = input("Ingrese nombre: ")

        if len(nombre.strip()) < 1:
            print("------> ERROR: No especifico el nombre. Vuelva a intentar.")
            input("Presione enter para continuar....")
            continue

        with open("7EjercicioArchivo.txt", "a") as archivo:
            archivo.write(nombre + "\n")
        

    elif opcion == "2":
        print("=============  Listado de nombres  ===============")
        with open("7EjercicioArchivo.txt", "r") as archivo:
            for parrafo in archivo:
                print("parrafo:" , parrafo.replace('\n',''))
            
            input("Presione enter para continuar....")
    
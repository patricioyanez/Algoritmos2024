import os
opcion = ""
usuarios = [] # si es una colección definir nombre en plural
claves = []
while opcion != "5":
    os.system("cls")
    print("=== Menú ===")
    print("1.- Iniciar sesión")
    print("2.- Registrar usuario")
    print("3.- Eliminar usuario")
    print("4.- Listar usuario")

    print("5.- Salir")
    opcion = input("Ingrese opción:")

    if opcion not in ["1", "2", "3", "4", "5"]:
        print("Opción no valida. Vuelva a intentar.")
        input("Presione enter para continuar....")
        continue

    if opcion == "1":
        print("|********* Login *********|")
        usuario = input("Ingrese nombre de usuario:")
        clave   = input("Ingrese clave del usuario:")
        estaElUsuarioRegistrado = False
        for indice in range(len(usuarios)):
            if usuario == usuarios[indice]:
                if clave == claves[indice]:
                    estaElUsuarioRegistrado = True

        if estaElUsuarioRegistrado:
            print(f"=========> Bienvenido {usuario} :)")
        else:
            print("Error: Usuario y/o clave no son válidos")
        
        input("Presione enter para continuar....")

    if opcion == "2":
        print("*** Ingreso de usuarios ***")
        usuario = input("Ingrese nombre de usuario:")
        clave   = input("Ingrese clave del usuario:")
        # strip elimina los espacios de los costados del string
        if len(usuario.strip()) == 0 or len(clave.strip()) == 0:
            print("Opción no valida. Vuelva a intentar.")
            input("Presione enter para continuar....")
            continue

        usuarios.append(usuario)
        claves.append(clave)
        print("El Usuario fue guardado con éxito")
        input("Presione enter para continuar....")

    if opcion == "4": # len permite contar la cantidad de caracteres
        for i in range(len(usuarios)): # range es para entregar una secuencia numerica
            print(f"Usuario: {usuarios[i]}, Clave: { claves[i]}")
        input("Presione enter para continuar....")
        continue
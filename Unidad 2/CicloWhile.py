# Importar el módulo os
import os
numero = 1
while numero <= 10:
    print(f"Valor {numero}")
    numero += 1 # es igual => numero = numero + 1



# Limpiar la consola
valor = 0
while valor <= 10:
    os.system("cls")
    x = input("Ingrese un valor: ")
    x = int(x)
    resto = x % 2
    if resto == 0:
        print(f"{x} Es par")
    else:
        print(f"{x} Es impar")
    valor += 1
    input("Presione Enter para continuar...")
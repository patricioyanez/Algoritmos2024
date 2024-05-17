# crear una aplicación      # que permita almacenar las
# notas que el usuario      # determine
# dar la opcion de ingreso, # promediar, 
# mostrar o listar todas las notas ingresadas y salir


print("Ingreso de notas")
cantidad = input("Cantidad de notas a ingresar: ")
try:
    cantidad = int(cantidad)
except:
    print("Valor no se puede convertir")
    # continue
contador = 0
notas = []
print("==== Ingreso de notas ====")
while contador < cantidad:
    
    nota = input("Ingrese nota:")
    try:
        nota = int(nota)
        contador += 1
        notas.append(nota)
    except:
        print("Valor no es valido")
        input("presione enter para continar...")

print(notas)

## recorrer una lista
print("***** Listado de notas ******")
for nota in notas:
    print("nota: ", nota)

print("***** Listado de notas 2 ******")
for con in range(len(notas)):
    print(f"nota {con+1}: {notas[con]}")


resultado = 0
for nota in notas:
    resultado += nota
print("El promedio es:", round(resultado/cantidad))
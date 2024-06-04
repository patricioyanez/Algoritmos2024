datos = "Hola Como Están Uds?"

# creación de archivo en modo escritura (Write)
# si existe lo SOBRE ESCRIBE
with open("7ManejoDeArchivo.txt", "w") as archivo:
    archivo.write(datos)

# agregar datos al archivo 'a' (append)
with open("7ManejoDeArchivo.txt", "a") as archivo:
    archivo.write("\nNuevo valor")

with open("7ManejoDeArchivo.txt", "a") as archivo:
    archivo.write("\nNuevo valor 2")
# lectura de un archivo. 'r' de read
documento = open('7ManejoDeArchivo2.txt', 'r')
contenido = documento.read()
print(contenido)
documento.close()

print("\n\n******** usando With **************")
contenido = ''
with open("7ManejoDeArchivo.txt",'r') as documento:
    contenido = documento.read()

print(contenido)
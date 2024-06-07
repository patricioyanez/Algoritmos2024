import csv
# lectura de archivo con formato CSV
nuevosDatos = [] # almacenara los datos con la nueva columna
with open('8listadoRutEmpresa.csv', 'r', newline='') as documento:
    datosDocumento = csv.reader(documento)

    for fila in datosDocumento:
        # agrega la nueva columna
        if int(fila[2]) < 100000000:
            fila.append("Pequeño Contribuyente")
        elif int(fila[2]) <= 200000000:
            fila.append("Mediano Contribuyente")
        else:            
            fila.append("Gran Contribuyente")
        
        # almacena la fila con la nueva columna
        nuevosDatos.append(fila)

# crea y guarda los nuevos datos generados
with open('8listadoRutEmpresa1.csv', 'w', newline='') as documento:
    escribir = csv.writer(documento)
    escribir.writerows(nuevosDatos)

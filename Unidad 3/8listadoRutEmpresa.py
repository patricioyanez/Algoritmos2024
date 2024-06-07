import csv
# lectura de archivo con formato CSV
nuevosDatos = []
with open('8listadoRutEmpresa.csv', 'r', newline='') as documento:
    datosDocumento = csv.reader(documento)

    for fila in datosDocumento:
        if int(fila[2]) < 100000000:
            fila.append("Pequeño Contribuyente")
        elif int(fila[2]) <= 200000000:
            fila.append("Mediano Contribuyente")
        else:            
            fila.append("Gran Contribuyente")
        
        nuevosDatos.append(fila)

with open('8listadoRutEmpresa1.csv', 'w', newline='') as documento:
    escribir = csv.writer(documento)
    escribir.writerows(nuevosDatos)

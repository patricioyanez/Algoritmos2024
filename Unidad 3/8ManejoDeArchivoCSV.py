import csv

with open('8ManejoDeArchivoCSV.csv', 'w', newline='') as documento:
    escribir = csv.writer(documento)

    #agregar primera fila. usar lista
    fila = ['20100200-k','Juan Díaz', 'Maipú']
    escribir.writerow(fila)

    # agregar más de una fila. usar matriz
    filas =[
                ['10-k', 'Ana Perez', 'Cerrillos'],
                ['11-1', 'Luisito Arias', 'Talagante'],
                ['12-2', 'Inés Aros', 'Providencia'],
                ['13-3', 'Al Bondi', 'PAC'],
            ]

    escribir.writerows(filas)

# lectura de archivo con formato CSV
with open('8ManejoDeArchivoCSV.csv', 'r', newline='') as documento:
    datosDocumento = csv.reader(documento)

    for fila in datosDocumento:
        print("parrafo:", fila) 
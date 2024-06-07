import json

persona = {
    "rut"       : "20100300-k",
    "nombre"    : "Juan Carlos Jason",
    "apellido"  : "Guatero",
    "comuna"    : "Isla de Pascua",
    "Carrera"   : "Parvulo"
}

with open('8ManejoDeArchivoJSON.json', 'w') as documento:
    json.dump(persona, documento)

# leer el documento completos
with open('8ManejoDeArchivoJSON.json', 'r') as documento:
    datos = json.load(documento)
    print(datos)

# obtener los datos de cada fila
with open('8ManejoDeArchivoJSON.json', 'r') as documento:
    datos = json.load(documento)
    print("Nombre completo:", datos["nombre"], datos["apellido"])
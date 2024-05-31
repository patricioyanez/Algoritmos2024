producto = {
    "codigoBarra"   : 78000123456,
    "nombre"        : "CocaCola",
    "cantidad"      : "2lts",
    "precioCompra"  : 1000,
    "precioVenta"   : 1500,
    "stock"         : 50,
    "Habilitado"    : True
}

print(producto)

# obtener valor según llave
print("Nombre de producto   :", producto["nombre"])
print("El valor es          :", producto["precioVenta"])

# agregar elemento al diccionario
producto["fecha"] = "31-05-2024"
producto["x"] = "xxxxxxxxxxxxxxxxxx"

# REcorrer
for valor in producto:
    print(valor)

for valor in producto:
    print(producto[valor])

# eliminar elemento
del producto["x"] 

# recorrer usando llave - valor
for key, valor in producto.items():
    print(key,":", valor)
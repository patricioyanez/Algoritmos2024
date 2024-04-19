numero = 20

if numero == 100: # si
    print("El número es cien")
    print("y estoy seguro....")

if numero < 100: # si
    print("Es menor que cien")
else: # sino
    print("Es igual o mayor que cien")
    
# operadores
# <, >, <=, >=, != (distinto) y == (igualdad)

if  numero != 50:
    print("No es cincuenta")


nota = 30

if nota == 70: # si
    print("Excelente!")
elif nota > 39: # sino si condicion se evalua otra condicion
    print("azul")
else:
    print("rojo, malito :(")

### solicitar la edad a un usuario
### señalar rango etario
### bebe, niño, adolescente, adulto
### tercera edad, 4ta edad (85)

edad = input("Ingrese su edad: ")
edad = int(edad) # convierte de str a int
if edad < 3:
    print("es bebe")
elif edad <= 12:
    print("es niño")
elif edad <= 18:
    print("es adolescente")
elif edad <= 65:
    print("es adulto")
elif edad <= 85:
    print("es de la 3ra edad")
else:
    print("es de la cuarta edad")






print("Fin de la aplicación")
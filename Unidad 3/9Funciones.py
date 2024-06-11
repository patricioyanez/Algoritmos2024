# funcion simple
def sumar():
    resultado = 1+1
    print("El resultado es:", resultado)

# funcion con retorno de valor
def sumar2():
    return 1+1
# funcion con parametros
def sumar3(n1, n2):
    total = n1+n2
    return total

sumar()
x = sumar2()
print("el valor es:",x )

x = sumar3(10,50)
print("El valor es:",x )

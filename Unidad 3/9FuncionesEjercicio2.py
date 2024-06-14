

def verificarLista(valores):  # 10 20 50 700 60 50 
    global nuevaLista
    nuevaLista = valores.split() 
    for valor in nuevaLista:
        if not valor.isnumeric():
            return -1 # hay valores no numerico
    return 1 # todos los valores son numeros  

def separarNumeros(lista): #[10,20,50,700,60,50]
    global listaPares
    global listaImpares
    listaPares = []
    listaImpares = []
    for valor in lista:
        if int(valor) % 2 == 0:
            listaPares.append(valor)
        else:
            listaImpares.append(valor)

numeros = input("Ingrese lista de valores:")
resultado = verificarLista(numeros)

if resultado == -1:
    print("Hay error en los valores ingresados")
else:
    separarNumeros(nuevaLista)
    print(listaPares)
    print(listaImpares)





        
        
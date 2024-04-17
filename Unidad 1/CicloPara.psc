Algoritmo sin_titulo
	Definir numero Como Entero
	Para numero<-1 Hasta 5 Hacer
		Escribir 'Numero ',numero
	FinPara
	// numeros pares que hay entre el 0 al 20
	Definir numero2 Como Entero
	Para numero2<-0 Hasta 20 Con Paso 2 Hacer
		Escribir 'Valor: ',numero2
	FinPara
	// numeros impares que hay entre el 0 al 20
	Definir numero3 Como Entero
	Para numero3<-1 Hasta 20 Con Paso 2 Hacer
		Escribir 'Valor: ',numero3
	FinPara
	// solicitar numero al usuario y mostrar los pares
	Definir valorMaximo Como Entero
	Definir contador Como Entero
	contador <- 0
	Escribir '*************************'
	Escribir 'Ingrese valor para ver sus pares'
	Leer valorMaximo
	Para numero2<-0 Hasta valorMaximo Con Paso 2 Hacer
		Escribir 'Valor par: ',numero2
		contador <- contador+1
	FinPara
	Escribir 'Se ejecuto ',contador,' veces'
FinAlgoritmo

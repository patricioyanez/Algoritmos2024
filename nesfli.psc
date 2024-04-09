Algoritmo nesfli
	Definir opc Como Entero
	Definir plan1, plan2, plan3 Como Entero
	opc = -1
	
	Mientras opc <> 0 Hacer
		Limpiar Pantalla
		Escribir "*** Nesfli ***"
		Escribir "1.- Ingresar precios de planes"
		Escribir "2.- Contratación"
		Escribir "3.- Cierre de turno"
		Escribir "0.- Salir"
		Escribir "Ingrese la opción"
		leer opc
		
		si opc == 1 Entonces
			Limpiar Pantalla
			Escribir "***** Ingresar precios de planes *****"
			Escribir "precio para plan 2 pantallas HD:"
			leer plan1
			Escribir "precio para plan 5 pantallas Full HD:"
			leer plan2
			Escribir "precio para plan ilimitado Full HD:"
			leer plan3
			Escribir "=====> Los precios fueron guardados"
			Escribir "Presiones cualquier tecla para continuar...."
			Esperar Tecla
		FinSi
	FinMientras
	
	
FinAlgoritmo

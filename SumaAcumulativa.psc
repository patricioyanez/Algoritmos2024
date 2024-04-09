Algoritmo SumaAcumulativa
	Definir total, num Como Entero
	Escribir "Ingrese un numero:"
	Leer num
	total = 0
	
	Mientras num <> 0 Hacer
		// acumulador
		total = total + num
		Escribir "Ingrese un numero:"
		Leer num
		
		Escribir "El total es:", (num+total)
	FinMientras
	
FinAlgoritmo

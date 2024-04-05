Algoritmo cobrarFotocopias
	Definir cantidad, total Como Entero
	Escribir "***** Calculo de cobro de fotocopias MR *****"
	Escribir "Ingrese cantidad de fotocopias"
	Leer cantidad
	
	si cantidad < 1 Entonces
		Escribir "La cantidad no es válida"
	SiNo
		total = cantidad * 20		
		si cantidad > 30 Entonces
			total = total * .9
		FinSi		
		Escribir "El total a pagar es: ", total 		
	FinSi
	
FinAlgoritmo

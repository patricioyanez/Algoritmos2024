Algoritmo mayorQueDosNumeros
	Escribir 'Ingrese el 1er número:'
	Leer numero1
	Escribir 'Ingrese el 2do número:'
	Leer numero2
	Escribir 'Ingrese el 3er número:'
	Leer numero3
	Si numero1>numero2 Entonces
		Si numero1>numero3 Entonces
			Escribir 'El numero ',numero1,' es mayor'
		SiNo
			Escribir 'El número ',numero3,' es mayor'
		FinSi
	SiNo
		Si numero2 > numero3 Entonces
			Escribir 'El número ', numero2,' es mayor'
		SiNo
			Escribir 'El numero ',numero3,' es mayor'
		FinSi
	FinSi
FinAlgoritmo

Algoritmo mayorQueDosNumeros
	Escribir 'Ingrese el 1er n�mero:'
	Leer numero1
	Escribir 'Ingrese el 2do n�mero:'
	Leer numero2
	Escribir 'Ingrese el 3er n�mero:'
	Leer numero3
	Si numero1>numero2 Entonces
		Si numero1>numero3 Entonces
			Escribir 'El numero ',numero1,' es mayor'
		SiNo
			Escribir 'El n�mero ',numero3,' es mayor'
		FinSi
	SiNo
		Si numero2 > numero3 Entonces
			Escribir 'El n�mero ', numero2,' es mayor'
		SiNo
			Escribir 'El numero ',numero3,' es mayor'
		FinSi
	FinSi
FinAlgoritmo

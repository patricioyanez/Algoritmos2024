Algoritmo NumeroAleatorio
	Definir numeroAdivinar Como Entero
	Definir intento Como Entero
	Definir intentoUsuario Como Entero
	Definir acertado Como Logico
	
	// entrega un valor al azar o ramdom
	numeroAdivinar = aleatorio(1, 100)
	acertado = falso
	// Escribir "Numero entregado: ", numeroAdivinar
	Escribir "Ingrese cantidad de intentos"
	Leer intento
	
	Mientras intento > 0 Hacer
		Escribir "Ingrese un numero:"
		Leer intentoUsuario
		
		si intentoUsuario = numeroAdivinar Entonces
			Escribir "Felicidades, le achunto"
			intento = 0
			acertado = Verdadero
		SiNo
			Escribir "No es correcto"
			Escribir "Intente de nuevo"
			intento = intento - 1
		FinSi		
	FinMientras
	si no acertado Entonces
		Escribir "El numero es ", numeroAdivinar
	FinSi
	
	
FinAlgoritmo

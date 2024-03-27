Algoritmo sin_titulo
	
	// solicitar edad y asociarlo a un rango etario
	//niño, adolescente, adulto, 3ra edad
	Definir edad Como Entero
	Escribir "Ingrese su edad"
	Leer edad
	
	si edad < 13 Entonces
		Escribir "Ud. es un niño"
	SiNo
		si edad < 18 Entonces
			Escribir "Ud. es Adolescente"
		sino
			si edad < 65 Entonces
				Escribir "Ud. es adulto"
			SiNo
				Escribir "Ud. es de la 3ra edad"
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo

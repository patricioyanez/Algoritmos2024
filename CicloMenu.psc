Algoritmo CicloMenu
	Definir respuesta Como Entero
	Definir numero1, numero2 Como Entero
	Definir resultado Como Real
	
	respuesta = -1 // <- 
	
	Mientras respuesta <> 0 Hacer // !=    <>
		Limpiar Pantalla
		Escribir "***** Super Calculadora *****"
		Escribir "1.- Sumar"
		Escribir "2.- Restar"
		Escribir "3.- Multiplicar"
		Escribir "4.- Dividir"
		Escribir "0.- Salir"
		Escribir "Escriba una opción:"
		Leer respuesta
		si respuesta < 0 o respuesta > 4 Entonces
			Escribir ""
			Escribir "==== Opción no válida ===="
			Escribir "Presione enter para continuar..."
			Esperar Tecla
		SiNo
			si respuesta == 1 Entonces
				Escribir "+++++++ Sumar ++++++++"
				Escribir "Ingrese 1er número"
				Leer numero1
				Escribir "Ingrese 2do número"
				Leer numero2
				resultado = numero1 + numero2
				Escribir "El resultado es: ", resultado
				Escribir "Presione enter para continuar... "
				Esperar Tecla				
			FinSi
			si respuesta == 2 Entonces
				Escribir "+++++++ Restar ++++++++"
				Escribir "Ingrese 1er número"
				Leer numero1
				Escribir "Ingrese 2do número"
				Leer numero2
				resultado = numero1 - numero2
				Escribir "El resultado es: ", resultado
				Escribir "Presione enter para continuar... "
				Esperar Tecla				
			FinSi
			si respuesta == 3 Entonces
				Escribir "+++++++ Multiplicar ++++++++"
				Escribir "Ingrese 1er número"
				Leer numero1
				Escribir "Ingrese 2do número"
				Leer numero2
				resultado = numero1 * numero2
				Escribir "El resultado es: ", resultado
				Escribir "Presione enter para continuar... "
				Esperar Tecla				
			FinSi
			
			si respuesta == 4 Entonces
				Escribir "+++++++ Restar ++++++++"
				Escribir "Ingrese 1er número"
				Leer numero1
				Escribir "Ingrese 2do número"
				Leer numero2
				
				si numero2 = 0 Entonces
					Escribir "No se puede dividir por cero"
				sino	
					resultado = numero1 / numero2
					Escribir "El resultado es: ", resultado				
				FinSi
				
				Escribir "Presione enter para continuar... "
				Esperar Tecla				
			FinSi
			// + - * /
		FinSi
	FinMientras
	
FinAlgoritmo

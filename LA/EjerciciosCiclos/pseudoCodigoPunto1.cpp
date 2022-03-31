/*
Desarrollar un algoritmo que permita ingresar 
al usuario tantos números como quiera. 
Cuando el usuario decida terminar de ingresar los números, 
reportar cuántos números fueron ingresados en total, 
luego cuántos números pares, cuántos números impares y 
el promedio de los valores ingresados. 
Solamente incluir valores positivos en el promedio, 
aunque el usuario podría ingresar valores negativos.
 */ 
Algoritmo PrimerPunto
Variables: 	numero, n, pares, impares, positivos, 
			sumatoria, promedio:numéricas
Inicio
	n = 0
	pares = 0
	impares = 0
	positivos = 0
	sumatoria = 0
	Mientras 1 == 1:
		Escriba "Ingrese un número o la letra n para terminar"
		Lea numero
		Si numero == "n":
			//Cómputos finales, reporte y salida
			promedio = sumatoria / positivos
			Escriba "El promedio es: " promedio
			Escriba "Ingresaron " pares " pares y " impares "impares"
			break;
		Si_no:
			//Actualización de variables
			n = n + 1//Actualizar conteo total
			//Actualizar  conteo de pares
			Si numero % 2 == 0:
				pares = pares + 1
			Si_no:
				impares = impares + 1
			Fin_Si
			//Actualizar conteo de positivos y sumatoria
			Si numero > 0:
				positivos = positivos + 1
				sumatoria = sumatoria + numero
			Fin_Si
		Fin_Si
	Fin_Mientras
Fin







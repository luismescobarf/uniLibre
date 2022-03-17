Algoritmo: ClasificacionPuntos
Inicio
	//Lectura puntos
	Lea X1,Y1
	Lea X2,Y3
	Lea X3,Y3
	////////////////////////////////////////
	//Clasificar el primer punto ingresado
	////////////////////////////////////////
	//Revisar si está en el primer cuadrante
	Si X1 > 0 and Y1 > 0:
		Asignar color Amarillo
		Dibujar en X1,Y1
	Si_no:
		//Revisar si está en el segundo cuadrante
		Si X1 < 0 and Y1 > 0:
			Asignar color Rojo
			Dibujar en X1,Y1
		Si_no:
			//Revisar si está en el tercer cuadrante
			Si X1 < 0 and Y1 < 0:
				Asignar color Azul
				Dibujar en X1,Y1
			Si_no:
				//Si está en el cuarto o en la frontera
				Asignar color Verde
				Dibujar en X1,Y1
			Fin_Si
		Fin_Si
	Fin_Si
	
	////////////////////////////////////////
	//Clasificar el segundo punto ingresado
	////////////////////////////////////////
	//Revisar si está en el primer cuadrante
	Si X2 > 0 and Y2 > 0:
		Asignar color Amarillo
		Dibujar en X2,Y2
	Si_no:
		//Revisar si está en el segundo cuadrante
		Si X2 < 0 and Y2 > 0:
			Asignar color Rojo
			Dibujar en X2,Y2
		Si_no:
			//Revisar si está en el tercer cuadrante
			Si X2 < 0 and Y2 < 0:
				Asignar color Azul
				Dibujar en X2,Y2
			Si_no:
				//Si está en el cuarto o en la frontera
				Asignar color Verde
				Dibujar en X2,Y2
			Fin_Si
		Fin_Si
	Fin_Si


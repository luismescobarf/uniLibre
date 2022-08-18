package main

//Importado de librerías
import (
	"fmt"
	"math/rand"
	"time"
)

//Límites del fragmento
type RangosFragmento struct {
	fila_a    int
	fila_b    int
	columna_a int
	columna_b int
}

//Mecanismo de sincronización
//var wg sync.WaitGroup

//Declaración de funciones
//////////////////////////

//Función para generar una matriz con valores aleatorios
func generarMatrizCuadradaAleatoria(tamanio int) [][]int {

	//Crear la matriz (declaración y reserva de memoria)
	matriz := make([][]int, tamanio)
	for i := range matriz {
		matriz[i] = make([]int, tamanio)
	}

	//Llenar la matriz con valores aleatorios
	for i := range matriz {
		for j := range matriz[i] {
			//Generar aleatorios sobre un rango que disminuya probabilidade sde repetición
			matriz[i][j] = rand.Intn(tamanio * tamanio)
		}
	}

	//Retornar la matriz construida
	return matriz

}

//Función para imprimir matriz línea por línea
func mostrarMatriz(matriz [][]int) {
	for i := range matriz {
		for j := range matriz[i] {
			fmt.Printf("%d ", matriz[i][j])
		}
		fmt.Println(" ")
	}

}

//Busqueda secuencial del mayor elemento
func busquedaST_MayorElemento(matriz [][]int) int {

	//Inicializar variable que recibe el mayor elemento
	mayorElemento := -1

	//Recorrer todos los elementos de la matriz
	for i := range matriz {
		for j := range matriz[i] {
			if matriz[i][j] > mayorElemento {
				mayorElemento = matriz[i][j]
			}
		}
	}

	//Retornar la variable que contiene la incumbente del proceso
	return mayorElemento

}

//Extraer una submatriz con límites inferiores y superiores para filas y columnas respectivamente
func obtenerSubMatriz(fila_a int, fila_b int, columna_a int, columna_b int, matriz [][]int) [][]int {

	//Calcular dimensiones de la submatriz a partir de los intervalos
	numeroFilas := fila_b - fila_a + 1
	numeroColumnas := columna_b - columna_a + 1

	//Crear/Declarar la submatriz
	subMatriz := make([][]int, numeroFilas)
	for i := range subMatriz {
		subMatriz[i] = make([]int, numeroColumnas)
	}

	//Cargar los elementos en la submatriz
	contadorFilasSubMatriz := 0
	contadorColumnasSubMatriz := 0
	for i := fila_a; i <= fila_b; i++ {
		for j := columna_a; j <= columna_b; j++ {
			subMatriz[contadorFilasSubMatriz][contadorColumnasSubMatriz] = matriz[i][j]

			// //Salidas de diagnóstico
			// fmt.Println("Contador Filas Submatriz: ", contadorFilasSubMatriz)
			// fmt.Println("Contador Columnas Submatriz: ", contadorColumnasSubMatriz)
			// fmt.Println("i (matOriginal): ", i)
			// fmt.Println("j (matOriginal): ", j)
			// fmt.Println("-------------------")

			contadorColumnasSubMatriz++
		}
		//fmt.Println("Termina Fila!!!")
		contadorColumnasSubMatriz = 0
		contadorFilasSubMatriz++
	}

	//Retornar la submatriz
	return subMatriz
}

//Búsqueda en fragmento concurrente (conectado a canal)
func busquedaMayorSubmatriz(canalFragmentosTrabajo chan [][]int, canalMayores chan int) {

	//Avisar finalización del trabajo
	//defer wg.Done()

	fragmentoTrabajo := <-canalFragmentosTrabajo

	// //Salida de diagnóstico de la distribución
	// fmt.Println("Fragmento recibido: ")
	// mostrarMatriz(fragmentoTrabajo)
	// fmt.Println("ºººººººººººººººººº")

	incumbente := -1
	for i := range fragmentoTrabajo {
		for j := range fragmentoTrabajo[i] {
			if fragmentoTrabajo[i][j] > incumbente {
				incumbente = fragmentoTrabajo[i][j]
			}
		}
	}
	//Envío de la respuesta
	canalMayores <- incumbente
}

//Mayor de un vector
func mayorElementoVector(vector []int) int {
	incumbente := -1
	for _, elemento := range vector {
		if elemento > incumbente {
			incumbente = elemento
		}
	}
	return incumbente
}

//Sección principal
func main() {

	fmt.Println("---- Búsqueda de Mayor Elemento en Una Matriz ----")

	//Generar matriz aleatoria
	var tamanioMatriz int = 100000
	matrizLlena := generarMatrizCuadradaAleatoria(tamanioMatriz)

	// //Mostrar el contenido de la matriz generada
	// fmt.Println("Matriz generada: ")
	// mostrarMatriz(matrizLlena)

	// //Diagnóstico del fragmentado de la matriz
	// fmt.Println("Pedazo de matriz: ")
	// // fragmento := obtenerSubMatriz(0, 1, 0, 1, matrizLlena)
	// fragmento := obtenerSubMatriz(1, 3, 2, 3, matrizLlena)
	// fmt.Println()
	// mostrarMatriz(fragmento)
	// fmt.Println()

	//Realizar la búsqueda secuencial
	tiempoInicial := time.Now() //Iniciar la toma de tiempo
	mayorElemento := busquedaST_MayorElemento(matrizLlena)
	tiempoTranscurrido := time.Since(tiempoInicial)
	fmt.Println("-----------------------------------------")
	fmt.Println("Tiempo transcurrido ST = ", tiempoTranscurrido)
	fmt.Println("Mayor elemento encontrado ST = ", mayorElemento)
	fmt.Println("-----------------------------------------")

	//Realizar la búsqueda distribuída

	// //Pruebas de división entera
	// divisionEntera := int(5 / 2)
	// fmt.Println("Division entera: ", divisionEntera)

	//Canal para envío del trabajo para las goroutines
	canalFragmentosTrabajo := make(chan [][]int, 4)
	//Canal para recolección de respuestas (valores mayores encontrados)
	canalMayores := make(chan int, 4)

	//División del trabajo
	infoFragmentos := make([]RangosFragmento, 4)

	//Puntos de división de la matriz
	mitadMatriz := int(tamanioMatriz/2) - 1
	despuesMitad := mitadMatriz + 1
	maxSubIndice := tamanioMatriz - 1

	//Primera sub matriz
	infoFragmentos[0].columna_a = 0
	infoFragmentos[0].columna_b = mitadMatriz
	infoFragmentos[0].fila_a = 0
	infoFragmentos[0].fila_b = mitadMatriz

	//Segunda sub matriz
	infoFragmentos[1].columna_a = despuesMitad
	infoFragmentos[1].columna_b = maxSubIndice
	infoFragmentos[1].fila_a = 0
	infoFragmentos[1].fila_b = mitadMatriz

	//Tercera sub matriz
	infoFragmentos[2].columna_a = 0
	infoFragmentos[2].columna_b = mitadMatriz
	infoFragmentos[2].fila_a = despuesMitad
	infoFragmentos[2].fila_b = maxSubIndice

	//Cuarta sub matriz
	infoFragmentos[3].columna_a = despuesMitad
	infoFragmentos[3].columna_b = maxSubIndice
	infoFragmentos[3].fila_a = despuesMitad
	infoFragmentos[3].fila_b = maxSubIndice

	//Preparar contenedor para las respuestas de las rutinas go
	var mayoresEncontrados []int

	//Colección con los fragmentos de trabajo
	coleccionFragmentos := make([][][]int, len(infoFragmentos))

	//Coleccionar cada fragmento
	for i := 0; i < len(infoFragmentos); i++ {
		coleccionFragmentos[i] = obtenerSubMatriz(
			infoFragmentos[i].columna_a,
			infoFragmentos[i].columna_b,
			infoFragmentos[i].fila_a,
			infoFragmentos[i].fila_b,
			matrizLlena)
	}

	tiempoInicial = time.Now() //Iniciar la toma de tiempo de la versión MT

	//Por cada fragmento de trabajo realizar un llamado de búsqueda
	for i := 0; i < len(infoFragmentos); i++ {
		//wg.Add(1)
		canalFragmentosTrabajo <- coleccionFragmentos[i]
		go busquedaMayorSubmatriz(canalFragmentosTrabajo, canalMayores)
	}

	// //Llamado de ejemplo
	// busquedaMayorSubmatriz(obtenerSubMatriz(1, 3, 2, 3, matrizLlena), canalFragmentosTrabajo, canalMayores)

	//Recoger información del canal con buffer que almacenará los mayores
	for i := 0; i < len(infoFragmentos); i++ {
		mayoresEncontrados = append(mayoresEncontrados, <-canalMayores)
	}

	//Esperar que todas las rutinas hayan acabado
	//wg.Wait()

	// //Mostrar el contenido (diagnóstico de recopilado)
	// fmt.Println("Mayores encontrados en los pedazos")
	// fmt.Println(mayoresEncontrados)

	//Trabajo de la rutina coordinadora -> encontrar el mayor de los mayores
	mayorMayores := mayorElementoVector(mayoresEncontrados)

	//Toma de tiempo al finalizar el proceso
	tiempoTranscurrido = time.Since(tiempoInicial)
	fmt.Println("-----------------------------------------")
	fmt.Println("Tiempo transcurrido MT = ", tiempoTranscurrido)
	fmt.Println("Mayor elemento encontrado ST = ", mayorMayores)
	fmt.Println("-----------------------------------------")

}

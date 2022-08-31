#########Diseño ejercicios parcial
#0) Crear un archivo de configuración vacío por cada 
# uno de los usuarios que tienen procesos activos en un directorio separado


#1) Diseñar una rutina por lotes para identificar los scripts de python del directorio descargado 
# y en todos sus subdirectorios (solamente un nivel de profundización), para luego ejecutarlos 
# por lote y capturar sus salidas para almacenarlas en un archivo. 
# - Quitar los permisos a todos los archivos por lotes generados en el proceso.
# - El script principal debe ejecutarse desde afuera de la carpeta resultante de la descompresión.
# - El resultado debe quedar almacenado en un archivo por fuera de la carpeta que se denomine salida.out
# - Redireccionar los errores que se generen a un archivo que se llame erroresLote.out


#2) Desarrollar un script que descargue el archivo del numeral 1 y genere un archivo comprimido
# con todos los archivos .txt y .pdf que estén en la carpeta generada por el directorio descargado y en los subdirectorios
# asociados (un sólo nivel de profundidad). Adicionalmente, generar un informe (archivo de texto)
# que incluya
# - Fecha del momento en el que se realizó la copia de seguridad.
# - ¿Cuánto tiempo se demoró realizando todo el proceso?
# - Listado de los archivos comprimidos

#3) Escribir una rutina que cree un directorio llamado accesosDirectos en el home del usuario 
# con los enlaces simbólicos a todos los archivos de la carpeta descargada, y archivos de sus 
# subdirectorios.

#4) De la base de datos publicada en:
# https://raw.githubusercontent.com/luismescobarf/uniLibre/main/bank.csv
# Desarrollar un script que descargue la base de datos y muestre:
# - El intervalo de edades de la base de datos: Menor edad - Mayor edad
# - ¿Cuántos valores diferentes tiene cada uno de los campos de la base de datos?
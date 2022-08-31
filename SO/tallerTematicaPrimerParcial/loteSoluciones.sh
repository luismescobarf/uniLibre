#Activar y desactivar las líneas del lote que se quieran utilizar

# #1) Generar un archivo con el listado de procesos que está activos acualmente.
# ps -ef > procesosActivosActualmente.txt

# #2) ¿Cuántos pacientes había en el estudio de cáncer?
# grep -v provincia cancer_progresion.txt | wc -l

# #3) ¿De cuántos pacientes no tenemos datos de progresión?
# grep desconocido cancer_progresion.txt | wc -l 

# # 5) Convertir la separación de comas de la tabla de doble ciego a tabuladores.
# cat cancer_ciego.txt | tr ',' '\t' > cancer_ciego_tab.txt
 

# # 6) Unir la tabla de los resultados de la terapia con la del doble ciego.
# join cancer_progresion.txt cancer_ciego_tab.txt > estudioAmpliado.txt
 

# # 7) ¿Cómo les ha ido a los pacientes según el tipo de tratamiento? (Placebo está escrito con mayúsculas y minúsculas)
# #Consultar pacientes tratados con placebo y guardarlos en el archivo
# echo "Placebo
# " > consultaTratamientos.txt
# grep -i placebo estudioAmpliado.txt >> consultaTratamientos.txt
# echo "
# 1mg
# " >> consultaTratamientos.txt
# grep -i 1mg estudioAmpliado.txt >> consultaTratamientos.txt
# echo "
# 2mg
# " >> consultaTratamientos.txt
# grep -i 2mg estudioAmpliado.txt >> consultaTratamientos.txt

 

# 8) Establecer una rutina que descargue el libro la odisea en formato de texto plano. Y obtener:
# - Listado de líneas donde aparece la palabra 'which' y generar un archivo ocurrenciasWhich.txt con el resultado.
# - Número de veces que aparece la palabra 'shall' y guardar el resultado en un fichero.

 

# 9) Escribir un archicho .sh por lotes que descargue el archivo comprimido ubicado en:
 
# https://github.com/luismescobarf/uniLibre/raw/main/paquete.tar.gz

# - Generar un archivo con los enlaces simbólicos presentes en el directorio.
# - ¿Cuántos directorios hay en el directorio descargado?
# - Copiar todos los scripts de Python y generar una carpeta en el home del usuario actual llamada rutinasPython,
#     dejando esos archivos con permisos de ejecución únicamente para el grupo.
# - Copiar todos los archivos .txt a una carpeta en el home que se denomine BackUP_TXT con todos estos archivos comprimidos.

# wget https://github.com/luismescobarf/uniLibre/raw/main/paquete.tar.gz
# tar -xzf paquete.tar.gz
# ls -al compresion/ | grep ^l > listadoEnlacesSimbolicos.txt
# echo "Número de directorios en el directorio descargado: " > conteoDirectorios.txt
# ls -al compresion/ | grep ^d | wc -l >> conteoDirectorios.txt 
# mkdir /Users/luismiguelescobar/rutinasPython
# cp compresion/*.py /Users/luismiguelescobar/rutinasPython/
# chmod 010 /Users/luismiguelescobar/rutinasPython/*.py
# mkdir /Users/luismiguelescobar/BackUP_TXT
# cp compresion/*.txt /Users/luismiguelescobar/BackUP_TXT/
# rm compresion/bancos.txt
# cp compresion/*.txt /Users/luismiguelescobar/BackUP_TXT/
# tar -cvzf /Users/luismiguelescobar/BackUP_TXT/ArchivosTXT.tar.gz /Users/luismiguelescobar/BackUP_TXT/*.txt
# rm /Users/luismiguelescobar/BackUP_TXT/*.txt
 

# # 10) Generar un script o un pipe o una mezcla de ambas, para dejar en un archivo el informe de cuántas
# # veces se ha utilizado el comando tar y en cuáles líneas.
# echo "Número de veces que se ha utilizado tar: " > informeComando_tar.txt 
# cat /Users/luismiguelescobar/.bash_history | grep -n tar | tr ':' '\t'| cut -f 1 | wc -l >> informeComando_tar.txt
# echo "Líneas del historial involucrando el comando: " >> informeComando_tar.txt 
# cat /Users/luismiguelescobar/.bash_history | grep -n tar | tr ':' '\t'| cut -f 1 >> informeComando_tar.txt

#########Diseño ejercicios parcial
# Crear un archivo de configuración por cada uno de los usuarios que tienen procesos activos en un directorio separado

# #Versión inicial
# mkdir directorio
# ps -ef | tr -s ' ' | tr ' ' '\t' | cut -f 1,2 | sort | uniq | grep -v UID | sed 's/\t/touch /' > ./directorio/crearArchivos.sh
# chmod 110 directorio/crearArchivos.sh
# cd directorio
# ./crearArchivos.sh

# #Versión completa
# mkdir directorio
# ps -ef | tr -s ' ' | tr ' ' '\t' | cut -f 1,2 | sort | uniq | grep -v UID | sed 's/\t/touch /' | sed 's/$/.txt/' > ./directorio/crearArchivos.sh
# chmod 777 directorio/crearArchivos.sh
# cd directorio
# ./crearArchivos.sh

#####Ejercicios Parcial/Taller Clase

#1) Diseñar una rutina por lotes para identificar los scripts de python del directorio descargado 
# y en todos sus subdirectorios (solamente un nivel de profundización), para luego ejecutarlos 
# por lote y capturar sus salidas para almacenarlas en un archivo. 
# - Quitar los permisos a todos los archivos por lotes generados en el proceso.
# - El script principal debe ejecutarse desde afuera de la carpeta resultante de la descompresión.
# - El resultado debe quedar almacenado en un archivo por fuera de la carpeta que se denomine salida.out
# - Redireccionar los errores que se generen a un archivo que se llame erroresLote.out


#Desarrollo:
#Iniciar el lote de ejecuciones de python
cd compresion
ls -hl *.py | tr -s ' ' | tr ' ' '\t' | cut -f 9 |  sed 's/^/python3 /' >> ejecucionPython.sh
chmod 777 ejecucionPython.sh
# echo "Ubicación: "
# pwd
ls -hl | grep ^d | tr -s ' ' | tr ' ' '\t' | cut -f 9 | sed 's/^/ls -hl /' | sed "s/$/\/*.py 2>> ..\/erroresLote.out /" >> directoriosIdentificados.sh
chmod 777 directoriosIdentificados.sh
./directoriosIdentificados.sh | tr -s ' ' | tr ' ' '\t' | cut -f 9 |  sed 's/^/python3 /' >> ejecucionPython.sh
./ejecucionPython.sh >> ../salidaPython.out
cd ../
rm compresion/ejecucionPython.sh compresion/directoriosIdentificados.sh


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






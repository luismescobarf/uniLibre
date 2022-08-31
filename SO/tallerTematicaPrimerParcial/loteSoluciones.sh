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



 

# 10) Generar un script o un pipe o una mezcla de ambas, para dejar en un archivo el informe de cuántas
# veces se ha utilizado el comando tar y en cuáles líneas.


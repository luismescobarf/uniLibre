#Espacio para solicitudes a las clases
from Nota import Nota
from Materia import Materia


# #Instanciar o crear una nota
# nota1 = Nota(descripcion="Primer Parcial",escala5=2.5)
# nota1.mostrarNotaConsola()

# #nota1.escala100 = 45
# nota1.setEscala100(45)

# print("Solicitar nota en escala de 100: ",nota1.getEscala100())

#Probar Materia con el requerimiento base
#materia = Materia(nota1=40,nota2=50,nota3=39,nota4=76,nota5=96)
materia = Materia(notas=[40,float(2.5),39,76,96])
materia.calcularPromedioAjustado()
materia.mostrarPromedioAjustado()
#Lógica general del requerimiento trabajado

from Nota import Nota

class Materia:
    
    def __init__(self,nombre="Sin asignar",nota1=None, nota2=None, nota3=None, nota4=None, nota5=None):
        self.__nombre = nombre
        self.__nota1 = Nota(escala100 = nota1)
        self.__nota2 = Nota(escala100 = nota2)
        self.__nota3 = Nota(escala100 = nota3)
        self.__nota4 = Nota(escala100 = nota4)
        self.__nota5 = Nota(escala100 = nota5)
        self.__promedio = Nota()
        self.__promedioAjustado = Nota()
        
    def calcularPromedio(self):
        sumatoriaEscala100 = self.__nota1.getEscala100()
        sumatoriaEscala100 += self.__nota2.getEscala100()
        sumatoriaEscala100 += self.__nota3.getEscala100()
        sumatoriaEscala100 += self.__nota4.getEscala100()
        sumatoriaEscala100 += self.__nota5.getEscala100()
        
        self.__promedio = Nota(escala100 = round(sumatoriaEscala100 / 5, 2) )
        
    def calcularPromedioAjustado(self):
        
        valoresEscala100 = [
            self.__nota1.getEscala100(),
            self.__nota2.getEscala100(),
            self.__nota3.getEscala100(),
            self.__nota4.getEscala100(),
            self.__nota5.getEscala100()
        ]
        
        self.__promedioAjustado = Nota(escala100 = round (( sum(valoresEscala100) - min(valoresEscala100) )/4,2)) 
    
    def mostrarPromedioAjustado(self):
        self.__promedioAjustado.mostrarNotaConsola()
    
        
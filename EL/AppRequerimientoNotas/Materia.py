#Lógica general del requerimiento trabajado

from Nota import Nota

class Materia:
    
    #def __init__(self,nombre="Sin asignar",nota1=None, nota2=None, nota3=None, nota4=None, nota5=None):
    def __init__(self,nombre="Sin asignar", notas = []):
        
        self.__nombre = nombre
        self.__notas = []
        
        for nota in notas:
            if nota != None and isinstance(nota, int):
                self.__notas.append(Nota(escala100 = nota)) 
            elif nota != None and isinstance(nota, float):
                self.__notas.append(Nota(escala5 = nota))
            else:
                self.__notas.append(Nota())
        self.__promedio = Nota()
        self.__promedioAjustado = Nota()
        
    def calcularPromedio(self):
        valoresEscala100 = [ nota.getEscala100() for nota in self.__notas ]
        sumatoriaEscala100 = sum(valoresEscala100)       
        self.__promedio = Nota(escala100 = round(sumatoriaEscala100 / len(valoresEscala100), 2) )
        
    def calcularPromedioAjustado(self):        
        valoresEscala100 = [ nota.getEscala100() for nota in self.__notas ]
        self.__promedioAjustado = Nota(escala100 = round (( sum(valoresEscala100) - min(valoresEscala100) )/ (len(valoresEscala100)-1),2)) 
    
    def mostrarPromedioAjustado(self):
        self.__promedioAjustado.mostrarNotaConsola()
    
        
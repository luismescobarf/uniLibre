#Clase (Molde -> Notas)

from datetime import datetime 


class Nota:
    
    #Atributos -> Llegan al constructor
    
    
    #Consutuctor (lógica para instanciar un objeto de la clase)
    def __init__(self, escala5=None, escala100=None, aprobada=None, descripcion = 'Sin descripción' ):
        #Creción de atributos
        self.escala5 = escala5
        self.__escala100 = escala100
        self.aprobada = aprobada
        self.descripcion = descripcion
        self.fechaRegistro = datetime.now()
        #Lógica de las escalas
        if escala100 != None:
            self.escala5 = escala100 / 20
            if escala100 >= 60:
               self.aprobada = 'Aprobada'
            else:
                self.aprobada = 'Reprobada'               
        elif escala5 != None:
            self.__escala100 = escala5 * 20
            if escala5 >= 2.96:
               self.aprobada = 'Aprobada'
            else:
                self.aprobada = 'Reprobada'       
    
    #Métodos
    
    #Mostrar en pantalla el contenido de la nota (dunder method)
    def mostrarNotaConsola(self):
        print("--------------------")
        print(f"Descripción: {self.descripcion}")
        print(f"Escala100: {self.__escala100}")
        print(f"Escala5: {self.escala5}")
        print(f"Cualitativa: {self.aprobada}")
        print(f"Fecha Registro: {self.fechaRegistro}")
        print("--------------------")
    
    #Getters
    def getEscala100(self):
        return self.__escala100
    
    #Setters
    def setEscala100(self,nuevaEscala100):
        self.__escala100 = nuevaEscala100
    
    
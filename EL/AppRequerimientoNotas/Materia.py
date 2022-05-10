#Librerías de soporte
import pprint as pp
import json

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
        
    #Dunder method
    def __str__(self):
        streamMateria = str()
        streamMateria += "------------------\n"
        streamMateria += "Nombre: "+self.__nombre + "\n"
        streamMateria += "Promedio: "+ str(self.__promedio.getEscala100()) + "\n"
        streamMateria += "Promedio Ajustado: "+ str(self.__promedioAjustado.getEscala100()) + "\n"
        for nota in self.__notas:
            streamMateria += "******************\n"
            streamMateria += "Descripción: " + nota.descripcion + "\n"
            streamMateria += "Escala100: " + str(nota.getEscala100()) + "\n"
            streamMateria += "Escala5: " + str(nota.getEscala5()) + "\n"
            streamMateria += "Cualitativa: "+ nota.aprobada + "\n"
            streamMateria += "Fecha Registro:" + str(nota.fechaRegistro) + "\n"
            streamMateria += "******************\n"            
        streamMateria += "------------------\n"
        return streamMateria
    
    def cargarMateria(self,rutaArchivoJSON):
        pass
    
    def guardarMateria(self,rutaArchivoJSON):
        
        #Guardar en un diccionario (serialización)
        atributosMateria = dict()       
        
        atributosMateria['nombre'] = self.__nombre
        atributosMateria['promedio'] = self.__promedio.getEscala100()                
        atributosMateria['promedioAjustado'] = self.__promedioAjustado.getEscala100()        
        
        atributosMateria['notas'] = list()
        
        for nota in self.__notas:            
            atributosMateria['notas'].append(
                {
                    'descripcion' : nota.descripcion,
                    'escala100': nota.getEscala100(),
                    'escala5': nota.getEscala5(),
                    'cualitativa': nota.aprobada,
                    'fechaRegistro': str(nota.fechaRegistro)
                }
            )
            
        try:
            with open(rutaArchivoJSON,'w') as f:
                json.dump(atributosMateria,f)
        except:
            print("Fallo guardando la materia!!")
        
            
            
            
            
        
        
        
        
        
    
    
        
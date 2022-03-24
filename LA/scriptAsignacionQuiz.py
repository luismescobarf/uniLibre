#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:22:07 2020

@author: luismiguelescobarfalcon
"""

#Impresión incremental
def cadenaDecremental(cadena):
    decremento_general = 0
    for i in range(len(cadena)+1 - decremento_general):
        incremento_palabra = 0
        for j in range(len(cadena)+1 - decremento_general):                        
            for k in range(incremento_palabra):
                print(cadena[k],end='')
            print(' ',end='')
            incremento_palabra += 1
        print()
        decremento_general += 1

#Impresión decremental
def cadenaIncremental(cadena):
    limitador_palabras = len(cadena)    
    for i in range(len(cadena)+1):
        limitador_letras = 0               
        for j in range(len(cadena)+1 - limitador_palabras):             
            for k in range(limitador_letras):
                print(cadena[k],end='')
            limitador_letras += 1
            print(' ',end='')
        print()
        limitador_palabras -= 1   
    

cadena = 'carro'
cadenaDecremental(cadena)
print()
cadenaIncremental(cadena)


palabra=str(input('Ingrese la palabra: '))
x=0
letra=1

while x<len(palabra):
    print(palabra[0:letra],end="")
    letra=letra+1
    x=x+1

cadena1 = 'hola'
cadena2 = 'mundo'
print(cadena1,end='')
print(' ',cadena2,end='')




    
    

            
            
            
        
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:20:02 2020

@author: Usuario
"""
import numpy as np


#Posiciones que varian en el rango de 0 a 5 para la muestra de (0, 30)
   
def mutate(bits):
    bits_nuevo = ''
    cont = 0
    for bit in bits:
        cont = cont + 1                
        sorteo = np.random.random()
        if sorteo >0.5 and 0 <= cont <= len(bits) :            
            if bit=='1':                
                bits_nuevo += '0'
            else:                
                bits_nuevo += '1'
        else:
            bits_nuevo += bit
    return bits_nuevo      

def reproduction(parent1, parent2):
    div = np.random.randint(0, len(parent1))
    if div == len(parent1):
        offspring1 = parent1
        offspring2 = parent2
    else:
        offspring1 = parent1[:div] + parent2[(div-len(parent1)):]
        offspring2 = parent2[:(div-len(parent1))] + parent1[div:]
    return offspring1, offspring2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:07:44 2020

@author: Usuario
"""
import numpy as np
import pandas as pd
import fitness as ft
import herramientas as hr

        
def generate_population(popsize):    
    Population = pd.DataFrame(columns=['Var_Ind_P_1','Bits_VI1', 'Propelente','Tipo_tobera',
                                       'Cromosoma', 'Aptitud'])
    while len(Population) < popsize:
        P_1_Camara = np.random.randint(10,150) + np.random.random() # Ajuste presion inicial
        Propelente = [1,2,3,4,5] #LOXH o LOXK , LOXM, etc.
        Tobera_tipo = [0,1] # conica o de campana
        
        spec = {'Var_Ind_P_1' : P_1_Camara, 'Bits_VI1' : 1, 'Propelente' : 1, 'Tipo_tobera' : 1, 
                'Cromosoma' : 1, 'Aptitud' : 1}
        
        spec['Bits_VI1'] = hr.float_to_bin(spec['Var_Ind_P_1'])
        spec['Propelente'] = np.binary_repr(np.random.choice(Propelente), width=4)
        spec['Tipo_tobera'] = np.binary_repr(np.random.choice(Tobera_tipo), width=1)            
        spec['Cromosoma'] = spec['Bits_VI1'] + spec['Propelente'] + spec['Tipo_tobera']
        spec['Aptitud'] = ft.fitness(spec['Cromosoma'])
        spec = pd.Series(spec)        
        Population = Population.append(spec, ignore_index = True)
    else:
        Population['Sel_prob'] = hr.prob_list(Population, 'Aptitud')
        return Population
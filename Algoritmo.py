# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:21:11 2020

@author: Usuario
"""
import datetime
import generadores
import fitness as ft
import evolvers as ev
import pandas as pd
import numpy as np
import herramientas as hr

np.random.seed(2)

Population = generadores.generate_population(50)
subset = Population.sort_values(['Aptitud'], ascending = False)
cont = 0
startTime = datetime.datetime.now()
timeDiff = startTime

while cont < 100: 
    
    'lista para seleccion de parejas ajustadas para poblacion = 50, crea parejas en funcion de la probabilidad y elimina los progenitores'
    val = np.linspace(0,9,10) 

    
    for i in val:
        
        cand1 = subset.index[20::2].tolist()
        cand2 = subset.index[20+1::2].tolist()
                
        par1, par2 = np.random.choice(subset['Cromosoma'], 2, replace=False, p=subset['Sel_prob'])
        offs1, offs2 = ev.reproduction(par1[32:], par2[32:])    
        offspring1 = {'Var_Ind_P_1' : hr.bin_to_float(par1[:32]), 'Bits_VI1' : par1[:32], 'Propelente' : offs1[:-1],
                      'Tipo_tobera' : offs1[4:], 'Cromosoma' : par1, 'Aptitud' : ft.fitness(par1)}
        offspring2 = {'Var_Ind_P_1' : hr.bin_to_float(par2[:32]), 'Bits_VI1' : par2[:32], 'Propelente' : offs2[:-1],
                      'Tipo_tobera' : offs2[4:], 'Cromosoma' : par2, 'Aptitud' : ft.fitness(par2)}
        new_spec1 = pd.Series(offspring1)
        new_spec2 = pd.Series(offspring2)
        subset = subset[subset.index != cand1[int(i)]]
        subset = subset[subset.index != cand2[int(i)]]
        subset = subset.append(offspring1, ignore_index = True)
        subset = subset.append(offspring2, ignore_index = True)
        
        subset['Sel_prob'] = hr.prob_list(subset,'Aptitud')
        
    
    subset = subset.sort_values(['Aptitud'], ascending = False)
    mut_pos = -np.random.randint(1,39) # muto un valor aleatorio
    mut_esp = subset['Cromosoma'].iloc[mut_pos]  
    esp_mut = ev.mutate(mut_esp[32:]) 
    
    muted_esp = {'Var_Ind_P_1' : np.random.randint(120, 249) + np.random.random(), 'Bits_VI1' : 1,
                 'Propelente' : esp_mut[:-1], 'Tipo_tobera' : esp_mut[4:], 'Cromosoma' : 1, 'Aptitud' : 1}
    
    muted_esp['Bits_VI1'] = hr.float_to_bin(muted_esp['Var_Ind_P_1'])
    muted_esp['Cromosoma'] = muted_esp['Bits_VI1'] + esp_mut
    muted_esp['Aptitud'] = ft.fitness(muted_esp['Cromosoma'])
    muted_esp = pd.Series(muted_esp)
    subset = subset[subset.Cromosoma != subset['Cromosoma'].iloc[mut_pos]]
    subset = subset.append(muted_esp, ignore_index = True)
        
    if len(subset) < 50:
        new = generadores.generate_population(50 - len(subset))
        subset = subset.append(new, ignore_index = True)

    subset['Sel_prob'] = hr.prob_list(subset,'Aptitud')
    subset = subset.sort_values(['Aptitud'], ascending = False)
    
    cont = cont + 1
    
    if subset['Aptitud'].sum() > 17500:
            print(subset)
            print(str(datetime.datetime.now() - startTime), cont)
            break
    
    print(subset['Aptitud'].sum())    
   
else:
    print(subset)
    print(str(datetime.datetime.now() - startTime), cont)      
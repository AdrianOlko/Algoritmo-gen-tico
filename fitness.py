# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:09:27 2020

@author: Usuario
"""
import herramientas as hr
import Prop_Comb as pc
import numpy as np


P_SL = 101325 # Pa
g0 = 9.8066 # m/s^2 gravedad a SL
F_m = 200 #kg/s Asumo un flujo masico de ejemplo, en el calculo del impulso especifico no afecta
t_c = 175 #s tiempo de quemado
          
def fitness(specimen):
    
    P_1 = hr.bin_to_float(specimen[:32]) 
    Prop = int(specimen[32:-1], 2)
    Tipo = int(specimen[36:], 2)
        
    if Prop == 1:
        Mezcla = pc.MR_LOXH(P_1)
        T_1_Camara = pc.adT_1_LOXH(P_1, Mezcla)
        MM = pc.MW_LOXH(P_1, Mezcla)
        gamma = pc.gamma_LOXH(P_1, Mezcla)
    if Prop == 2:
        Mezcla = pc.MR_LOXM(P_1)
        T_1_Camara = pc.adT_1_LOXM(P_1, Mezcla)
        MM = pc.MW_LOXM(P_1, Mezcla)
        gamma = pc.gamma_LOXM(P_1, Mezcla)
    if Prop == 3:
        Mezcla = pc.MR_LOXE(P_1)
        T_1_Camara = pc.adT_1_LOXE(P_1, Mezcla)
        MM = pc.MW_LOXE(P_1, Mezcla)
        gamma = pc.gamma_LOXE(P_1, Mezcla)
    if Prop == 4:
        Mezcla = pc.MR_LOXU(P_1)
        T_1_Camara = pc.adT_1_LOXU(P_1, Mezcla)
        MM = pc.MW_LOXU(P_1, Mezcla)
        gamma = pc.gamma_LOXU(P_1, Mezcla) 
    else:
        Mezcla = pc.MR_LOXK(P_1, 1) #Presion de salida = 1 atm, ajustable (0.1 a 1)
        T_1_Camara = pc.adT_1_LOXK(P_1, Mezcla)
        MM = pc.MW_LOXK(P_1, Mezcla)
        gamma = pc.gamma_LOXK(P_1, Mezcla)
    
    #V_1 = hr.V_esp(MM, T_1_Camara, P_1*101325)
    #V_t = hr.V_esp_t(V_1, gamma)
    #T_throat = hr.T_t(T_1_Camara, gamma)
    v_t = hr.v_crit(T_1_Camara, gamma, MM)
    A_t = hr.Area_throat(P_1*101325, MM, T_1_Camara, gamma, F_m) #en metro^2
    A_rela = hr.A_rel_term(P_SL, P_1*101325, gamma) #relaccion de areas para presion de salida igual a PSL A_t/A_y
    A_2 = A_t/A_rela
    v_2 = hr.v_y(v_t, P_SL, P_1*101325, gamma)
    # e = 1/A_rela # relacion de minimos para psl entre A_2/A_t
    
    if Tipo == 0:
        v_2 = 0.9830*v_2 # Valor fijo para tobera conica 15º
    else:
        v_2 = 0.992*v_2 # valor fijo para tobera campana 100% longitud conica
    
    t = np.linspace(0, t_c, 1000)
    E_t = 0
    
    
    for i in t:
        E_t = E_t + hr.Empuje(hr.Altitude_time(i),F_m,A_2,v_2)
    
    I_S = (E_t/1000)/(F_m*g0) # Impulso especifico, con el Empuje total medio a lo largo de una ruta diseño 
                              # con un tiempo de combustion t_c
        
    return I_S




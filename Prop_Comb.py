# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:36:59 2020

@author: Usuario
"""
import numpy as np

""" LOX LH """

def MR_LOXH(P_1_atm): #Mixture ratio Oxidante/Fuel en funcion de la presion de la camara
    if P_1_atm < 125:
        return 0.00000001*P_1_atm**4 - 0.000003*P_1_atm**3 + 0.0002*P_1_atm**2 + 0.01526*P_1_atm + 4.3851        
    else:
        return 6.0
    
def adT_1_LOXH(P_1_atm, Mixture_ratio): # Devuelve la temperatura de combustion adiabatica en funcion de  
    if Mixture_ratio < 5.5:             # la presion de la camara y la mezcla entre 5.0 y 6.0
        low_mix = 80.916*np.log(P_1_atm) + 2959.4
        mid_mix = 99.833*np.log(P_1_atm) + 2994.5
        return low_mix + ((mid_mix - low_mix)/0.5)*abs(5-Mixture_ratio)
    else:
        high_mix = 116.74*np.log(P_1_atm) + 3008.2
        mid_mix = 99.833*np.log(P_1_atm) + 2994.5
        return mid_mix + ((high_mix - mid_mix)/0.5)*abs(5.5-Mixture_ratio)
        
def MW_LOXH(P_1_atm, Mixture_ratio):        # Devuelve la masa molecular del gas mezcla en funcion de  
    if Mixture_ratio < 5.5:  # la presion de la camara y la mezcla entre 5.0 y 6.0
        low_mix = 0.0816*np.log(P_1_atm) + 11.454
        mid_mix = 0.1114*np.log(P_1_atm) + 12.171
        return low_mix + ((mid_mix - low_mix)/0.5)*abs(5-Mixture_ratio)
    else:
        high_mix = 0.1392*np.log(P_1_atm) + 12.851
        mid_mix = 0.1114*np.log(P_1_atm) + 12.171
        return mid_mix + ((high_mix - mid_mix)/0.5)*abs(5.5-Mixture_ratio)

            
def gamma_LOXH(P_1_atm, Mixture_ratio):      # Devuelve la gamma del gas mezcla en funcion de  
    if Mixture_ratio < 5.5:   # la presion de la camara y la mezcla entre 5.0 y 6.0
        low_mix = -0.003*np.log(P_1_atm) + 1.2184
        mid_mix = -0.0036*np.log(P_1_atm) + 1.2164
        return low_mix - ((low_mix - mid_mix)/0.5)*abs(5-Mixture_ratio)
    else:
        high_mix = -0.004*np.log(P_1_atm) + 1.215
        mid_mix = -0.0036*np.log(P_1_atm) + 1.2164
        return mid_mix - ((mid_mix - high_mix)/0.5)*abs(5.5-Mixture_ratio)
    
""" LOX LK """    

def MR_LOXK(P_1_atm, P_2_atm): # presiones de salida entre 0.1 y 1 atmosferas
    low_P = 0.0906*np.log(P_1_atm) + 1.9536
    high_P = 0.0925*np.log(P_1_atm) + 1.903
    return high_P + ((low_P - high_P)/0.9)*abs(1-P_2_atm)

def adT_1_LOXK(P_1_atm, Mixture_ratio):   
    if Mixture_ratio < 2.3:            
        low_mix = 97.532*np.log(P_1_atm) + 3047
        mid_mix = 112.47*np.log(P_1_atm) + 3052.9
        return low_mix + ((mid_mix - low_mix)/0.1)*abs(2.2-Mixture_ratio)
    else:
        high_mix = 124.34*np.log(P_1_atm) + 3055.5
        mid_mix = 112.47*np.log(P_1_atm) + 3052.9
        return mid_mix + ((high_mix - mid_mix)/0.1)*abs(2.3-Mixture_ratio)
    
def MW_LOXK(P_1_atm, Mixture_ratio):   
    if Mixture_ratio < 2.3:             
        low_mix = 0.1762*np.log(P_1_atm) + 20.41
        mid_mix = 0.2107*np.log(P_1_atm) + 20.73
        return low_mix + ((mid_mix - low_mix)/0.1)*abs(2.2-Mixture_ratio)
    else:
        high_mix = 0.2426*np.log(P_1_atm) + 21.027
        mid_mix = 0.2107*np.log(P_1_atm) + 20.73
        return mid_mix + ((high_mix - mid_mix)/0.1)*abs(2.3-Mixture_ratio)
            
def gamma_LOXK(P_1_atm, Mixture_ratio):       
    if Mixture_ratio < 2.3:   
        low_mix = -0.0029*np.log(P_1_atm) + 1.2355
        mid_mix = -0.0033*np.log(P_1_atm) + 1.234
        return low_mix - ((low_mix - mid_mix)/0.1)*abs(2.2-Mixture_ratio)
    else:
        high_mix = -0.00358*np.log(P_1_atm) + 1.2328
        mid_mix = -0.0033*np.log(P_1_atm) + 1.234
        return mid_mix - ((mid_mix - high_mix)/0.1)*abs(2.3-Mixture_ratio)
    
""" LOX LM """

def MR_LOXM(P_1_atm): 
    return  0.1115*np.log(P_1_atm) + 2.3002

def adT_1_LOXM(P_1_atm, Mixture_ratio):  
    if Mixture_ratio < 2.8:             
        low_mix = 82.367*np.log(P_1_atm) + 2983.8
        mid_mix = 93.668*np.log(P_1_atm) + 2996.5
        return low_mix + ((mid_mix - low_mix)/0.1)*abs(2.7-Mixture_ratio)
    else:
        high_mix = 104.17*np.log(P_1_atm) + 3001.6
        mid_mix = 93.668*np.log(P_1_atm) + 2996.5
        return mid_mix + ((high_mix - mid_mix)/0.1)*abs(2.8-Mixture_ratio)
    
def MW_LOXM(P_1_atm, Mixture_ratio): 
    if Mixture_ratio < 2.8:             
        low_mix = 0.1395*np.log(P_1_atm) + 18.71
        mid_mix = 0.1641*np.log(P_1_atm) + 19.002
        return low_mix + ((mid_mix - low_mix)/0.1)*abs(2.7-Mixture_ratio)
    else:
        high_mix = 0.1866*np.log(P_1_atm) + 19.282
        mid_mix = 0.1641*np.log(P_1_atm) + 19.002
        return mid_mix + ((high_mix - mid_mix)/0.1)*abs(2.8-Mixture_ratio)    
    
def gamma_LOXM(P_1_atm, Mixture_ratio):       
    if Mixture_ratio < 2.8:   
        low_mix = -0.0026*np.log(P_1_atm) + 1.2218
        mid_mix = -0.0028*np.log(P_1_atm) + 1.2207
        return low_mix - ((low_mix - mid_mix)/0.1)*abs(2.7-Mixture_ratio)
    else:
        high_mix = -0.00315*np.log(P_1_atm) + 1.2199
        mid_mix = -0.0028*np.log(P_1_atm) + 1.2207
        return mid_mix - ((mid_mix - high_mix)/0.1)*abs(2.8-Mixture_ratio)    
    
""" LOXE """    

def MR_LOXE(P_1_atm): 
    return 0.0398*np.log(P_1_atm) + 1.1251

def adT_1_LOXE(P_1_atm, Mixture_ratio): 
    if Mixture_ratio < 1.29:             
        low_mix = 74.098*np.log(P_1_atm) + 2816.8
        mid_mix = 82.894*np.log(P_1_atm) + 2815.2
        return low_mix + ((mid_mix - low_mix)/0.04)*abs(1.25-Mixture_ratio)
    else:
        high_mix = 89.31*np.log(P_1_atm) + 2815.5
        mid_mix = 82.894*np.log(P_1_atm) + 2815.2
        return mid_mix + ((high_mix - mid_mix)/0.04)*abs(1.29-Mixture_ratio)
    
def MW_LOXE(P_1_atm, Mixture_ratio): 
    if Mixture_ratio < 1.29:             
        low_mix = 0.1544*np.log(P_1_atm) + 22.432
        mid_mix = 0.176*np.log(P_1_atm) + 22.608
        return low_mix + ((mid_mix - low_mix)/0.04)*abs(1.25-Mixture_ratio)
    else:
        high_mix = 0.1953*np.log(P_1_atm) + 22.772
        mid_mix = 0.176*np.log(P_1_atm) + 22.608
        return mid_mix + ((high_mix - mid_mix)/0.04)*abs(1.29-Mixture_ratio)
    
def gamma_LOXE(P_1_atm, Mixture_ratio):      
    if Mixture_ratio < 1.29:   
        low_mix = -0.00225*np.log(P_1_atm) + 1.1989
        mid_mix = -0.00254*np.log(P_1_atm) + 1.1987
        return low_mix - ((low_mix - mid_mix)/0.04)*abs(1.25-Mixture_ratio)
    else:
        high_mix = -0.00275*np.log(P_1_atm) + 1.1986
        mid_mix = -0.00254*np.log(P_1_atm) + 1.1987
        return mid_mix - ((mid_mix - high_mix)/0.04)*abs(1.29-Mixture_ratio)
    
""" LOXU """  

def MR_LOXU(P_1_atm): 
    return 0.0658*np.log(P_1_atm) + 1.1032

def adT_1_LOXU(P_1_atm, Mixture_ratio): 
    if Mixture_ratio < 1.39:             
        low_mix = 89.407*np.log(P_1_atm) + 3016
        mid_mix = 100.6*np.log(P_1_atm) + 3026.9
        return low_mix + ((mid_mix - low_mix)/0.06)*abs(1.33-Mixture_ratio)
    else:
        high_mix = 110.36*np.log(P_1_atm) + 3033
        mid_mix = 100.6*np.log(P_1_atm) + 3026.9
        return mid_mix + ((high_mix - mid_mix)/0.06)*abs(1.39-Mixture_ratio)
    
def MW_LOXU(P_1_atm, Mixture_ratio): 
    if Mixture_ratio < 1.39:             
        low_mix = 0.1452*np.log(P_1_atm) + 18.873
        mid_mix = 0.1693*np.log(P_1_atm) + 19.145
        return low_mix + ((mid_mix - low_mix)/0.06)*abs(1.33-Mixture_ratio)
    else:
        high_mix = 0.1869*np.log(P_1_atm) + 19.437
        mid_mix = 0.1693*np.log(P_1_atm) + 19.145
        return mid_mix + ((high_mix - mid_mix)/0.06)*abs(1.39-Mixture_ratio)
    
def gamma_LOXU(P_1_atm, Mixture_ratio):      
    if Mixture_ratio < 1.39:   
        low_mix = -0.003*np.log(P_1_atm) + 1.2389
        mid_mix = -0.003*np.log(P_1_atm) + 1.2376
        return low_mix - ((low_mix - mid_mix)/0.04)*abs(1.33-Mixture_ratio)
    else:
        high_mix = -0.003*np.log(P_1_atm) + 1.2365
        mid_mix = -0.003*np.log(P_1_atm) + 1.2376
        return mid_mix - ((mid_mix - high_mix)/0.04)*abs(1.39-Mixture_ratio)    
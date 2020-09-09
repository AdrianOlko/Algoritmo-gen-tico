# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:13:12 2020

@author: Usuario

"""
import struct
import numpy as np
import matplotlib.pyplot as plt

#Formato en 32 bits para numeros segun la norma IEEE 754-2008

def float_to_bin(num):
    return bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:].zfill(32)

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def prob_list(df, column):
    Sel_prob = []
    for i in df.index:
        Sel_prob.append(df[column][i]/df[column].sum())
    return Sel_prob


""" ISA """


T_SL = 273.15 + 15 # K
P_SL = 101325 # Pa
g0 = 9.8066 # m/s^2 gravedad a SL
Ru = 8314.3 # J/kg-mol-k R constante universal de los gases o R'
Ru = 8314.3 # J/kg-mol-k R constante universal de los gases o R'
M_C = 12.0107 #u - carbono
M_H = 1.00784  #u - hidrógeno
M_O = 15.999 #u - oxígeno
M_N = 14.0067 #u -  nitrógeno
M_Ar = 39.948  #u -  Argón
Maire = 0.21*2*M_O + 0.78*2*M_N + 0.01*M_Ar
R_aire_at = Ru/Maire

def T_at(h_metros):
    if 0 <= h_metros <= 11000:
        return T_SL - 6.5*(h_metros/1000)
    if 11000 < h_metros <= 20000:
        return 216.65 
    if 20000 < h_metros <= 32000:
        return 216.65 + 1*((h_metros-20000)/1000)
    if 32000 < h_metros <= 47000:
        return 228.65 + 2.8*((h_metros-32000)/1000)
    if 47000 < h_metros <= 51000:
        return 270.65
    if 51000 < h_metros <= 71000:
        return 270.65 - 2.8*((h_metros-51000)/1000)   
    if 71000 < h_metros <= 84852:
        return 214.65 - 2*((h_metros-71000)/1000)
    else:
        return 'Error'

def P_at(h_metros):
    if 0 <= h_metros <= 11000:
        return P_SL*(1+(-6.5/1000)*h_metros/T_SL)**(-g0/R_aire_at/(-6.5/1000))
    if 11000 < h_metros <= 20000:
        return P_at(11000)*np.e**((-g0/R_aire_at/T_at(h_metros))*(h_metros-11000)) 
    if 20000 < h_metros <= 32000:
        return P_at(20000)*(1+(1/1000)*(h_metros-20000)/T_at(20000))**(-g0/R_aire_at/(1/1000))
    if 32000 < h_metros <= 47000:
        return P_at(32000)*(1+(2.8/1000)*(h_metros-32000)/T_at(32000))**(-g0/R_aire_at/(2.8/1000))
    if 47000 < h_metros <= 51000:
        return P_at(47000)*np.e**((-g0/R_aire_at/T_at(h_metros))*(h_metros-47000))
    if 51000 < h_metros <= 71000:
        return P_at(51000)*(1+(-2.8/1000)*(h_metros-51000)/T_at(51000))**(-g0/R_aire_at/(-2.8/1000))   
    if 71000 < h_metros <= 84852:
        return P_at(71000)*(1+(-2/1000)*(h_metros-71000)/T_at(71000))**(-g0/R_aire_at/(-2/1000))   
    else:
        return 0


""" Relaciones Termodinamicas"""


def Altitude_time(t): # Ruta
    return 1.0007*t**2.1616 

def V_esp(MM, T, P_Pa): # Volumen especifico
    return ((Ru/MM)*T)/P_Pa

def V_esp_t(V_esp, gamma):
    return V_esp*((gamma + 1)/2)**(1/(gamma - 1))

def T_t(T_1, gamma):
    return 2*T_1/(gamma + 1)

def v_crit(T_1, gamma, MM): 
    return np.sqrt((2*gamma*(Ru/MM)*T_1)/(gamma + 1))

def Area_throat(P_1_Pa, MM, T_1, gamma, Flujo_masico): 
    return (Flujo_masico/P_1_Pa)*np.sqrt(((Ru/MM)*T_1)/(gamma*(2/(gamma+1))**((gamma+1)/(gamma-1))))

def A_rel_term(P_y, P_1, gamma):
    return (((gamma+1)/2)**(1/(gamma-1)))*((P_y/P_1)**1/gamma)*np.sqrt(((gamma+1)/(gamma-1))*(1-(P_y/P_1)**((gamma-1)/gamma)))

def v_y(v_t, P_y, P_1, gamma):
    return v_t*np.sqrt(((gamma+1)/(gamma-1))*(1-(P_y/P_1)**((gamma-1)/gamma)))

def Empuje(h, mf, A_2, V_2): 
    return mf*V_2 + (P_SL - P_at(h))*A_2 

""" Rendimiento tipo """

def lamda_cone(alpha): # factor de correccion teorico, se aplica en el calculo de la fuerza, angulo total 2*alpha(15º para cono de 30ª)
    return 0.5*(1 + np.cos(alpha*(np.pi/180)))


def lamda_Bell(per, e_rel):
    if e_rel >= 40:
        if per == 60:
            return 0.973
        if per == 70:
            return 0.9825
        if per == 80:
            return 0.9875
        if per == 90:
            return 0.992
        if per >= 100:
            return 0.9925       
    else:
        if per == 60:
            return 0.9625 + ((0.973 - 0.9625)/30)*abs(10-e_rel)
        if per == 70:
            return 0.9755 + ((0.9825 - 0.9755)/30)*abs(10-e_rel)
        if per == 80:
            return 0.985 + ((0.9875 - 0.985)/30)*abs(10-e_rel)
        if per == 90:
            return 0.992
        if per >= 100:
            return 0.992 
        
""" Diseño """ 

def conicalfifteen(R_2, R_t, alpha): 
    return (R_2-R_t)/np.tan(alpha*(np.pi/180))

def pre_t(theta, R_t):
    return 1.5*R_t*np.sin(theta*(np.pi/(180))) + 1.5*R_t + R_t

def post_t(theta, R_t):
    return 0.4*R_t*np.sin(theta*(np.pi/(180))) + 0.4*R_t + R_t

def bezier(t, N_y, Q_y, E_y):
    return ((1-t)**2)*N_y + 2*(1-t)*t*Q_y + (t**2)*E_y

def theta_e(A_rel, percent): # angulo de salida de la tobera aproximada a campana(0,6-1)
    if percent == 1.0: 
        return 10.826*A_rel**-0.234
    if percent == 0.9:
        return 14.7*A_rel**-0.224
    if percent == 0.8:
        return 17.496*A_rel**-0.22
    if percent == 0.7:
        return 23.529*A_rel**-0.237
    else:
        return 26.989*A_rel**-0.207
    
def theta_i(A_rel, percent): # angulo de entrada de la tobera aproximada a campana(0,6-1)
    if percent == 1.0: 
        return 24.161*A_rel**0.1251
    if percent == 0.9:
        return 25.749*A_rel**0.1181
    if percent == 0.8:
        return 27.529*A_rel**0.1112
    if percent == 0.7:
        return 30.282*A_rel**0.1032
    else:
        return 34.124*A_rel**0.091

def plot_tobera_bell(percent, e_rel):#porcentaje de contorno de campana (0,6-1), relacion de areas para psl
    
    thet_n = theta_i(e_rel, 1) # valor fijo a pesar de la funcion que se usa en la bibliografia y da mejores resultados
    thet_e = theta_e(e_rel, percent)
    r_t = 1
    L_equiv_cone = conicalfifteen(np.sqrt(e_rel), r_t, 15)
    Ex = L_equiv_cone*percent  
    Ey = np.sqrt(e_rel)
    m_1 = np.tan(thet_n*(np.pi/(180)))
    m_2 = np.tan(thet_e*(np.pi/(180)))
    Ny = post_t(thet_n-90, r_t)
    Nx = 0.4*r_t*np.cos((thet_n-90)*(np.pi/(180)))
    C_1 = Ny-m_1*Nx
    C_2 = Ey-m_2*Ex
    #Qx = (C_2-C_1)/(m_1-m_2)
    Qy = (C_2*m_1-m_2*C_1)/(m_1-m_2)

    t_x = 1.5*r_t*np.cos(-135*(np.pi/(180)))

    tob_tot = abs(t_x) + Ex

    pre_ind = int(abs(t_x)*(10000/tob_tot))
    post_ind = int(abs(Nx)*(10000/tob_tot))
    tob_ind = int(abs(Ex)*(10000/tob_tot))
    
    x = np.linspace(t_x, Ex, pre_ind+post_ind+tob_ind)

    a = []

    j = np.linspace(-135, -90, pre_ind)
    for i in j:
        a.append(pre_t(i, r_t))

    k = np.linspace(-90, thet_n-90, post_ind)
    for i in k:
        a.append(post_t(i, r_t))    

    z = np.linspace(0, 1, tob_ind)
    for i in z:
        a.append(bezier(i,Ny,Qy,Ey))    

    fig, tb = plt.subplots()

    tb.set_xlabel('L')
    tb.set_ylabel('R(Garganta=unidad)')
    tb.set_ylim(0, Ey +1)
    tb.plot(x, a)
    tb.grid(True)
    plt.fill_between(x, a, color='black', alpha='0.5')
    
    return plt.show
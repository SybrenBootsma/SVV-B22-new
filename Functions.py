# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:32:36 2019

@author: Sybren
"""
from math import *
import numpy as np
import subprocess
import time

def velocity(V_IAS,hp,Tm):
    p0 = 101325             #Pa ISA
    rho0 = 1.225            #Kg/m3
    lapse = -6.5 * 10**(-3)     #deg C/m
    T0 = 288.15
    R = 287.057
    g0= 9.80665
    gamma = 1.4
    TAT = Tm + 273.15
    hp = hp * 0.3048
    Vc = (V_IAS - 2)*0.514444
    p = p0 * (1 + (lapse * hp)/T0)**(-g0/(lapse*R))
    M = np.sqrt(2/(gamma - 1) * ((1+(p0/p)*((1+(gamma-1)/(2*gamma) * (rho0/p0)*Vc**2.)**(gamma/(gamma-1)) - 1))**((gamma - 1)/gamma) - 1))
    T = TAT / (1 + (gamma-1)/2 * M*M)
    a = np.sqrt(gamma*R*T)
    Vt = M*a
    rho = rho0 * (T/T0)**(-(g0/(lapse*R) + 1))
    Ve = Vt * np.sqrt(rho/rho0)
    b = 1.458*10**(-6)
    S = 110.4
    mu = b * T**(3/2) / (T+S)
    Re = rho * Vt * 2.0569 / mu
    return Vc, M, a, Vt, Ve, rho, Re

def thrust(hp,IAS,TAT,FFr,FFl): #hp in feet, TAT in Kelvin, FFr/l in lbs/hr
    
    #Pressure alt. (hp)
    hplist = hp
    hplist = [i * 0.3048 for i in hplist] #convert feet to meters
    
    #Mach number
    Mlist = velocity(IAS, hp, TAT)[1]
    
    #Deltatemp use Kelvin for this part!
    TATlist = TAT
    for i in range(len(TATlist)):
        TATlist[i] = TATlist[i] + 273.15 #convert Celsius to Kelvin
    
    TISAlist = []
    for i in range(len(hplist)):
        TISA = 288.15 - (0.0065*hplist[i]) #Kelvins!
        TISAlist.append(TISA)
        
    Dtemplist = TATlist - TISAlist
    
    #Fuelflow
    FFllist = FFr #Left in [lbs/hr]
    FFrlist = FFl #Right
    
    FFllist = FFllist * 0.45359237/3600 #convert lbs/hr to kg/s
    FFrlist = FFrlist * 0.45359237/3600
    
    #Make file for nonstandart thrust
    matlab = open('matlab.dat','w+')
    for i in range(len(hp)):
         matlab.write(str(int(round(hplist[i],0))) +' '+ str(Mlist[i]) +' '+ str(round(Dtemplist[i],4)) +' '+ str(round(FFllist[i],5)) +' '+ str(round(FFrlist[i],5)) + "\n")
    matlab.close()
    
    #Run thrust.exe and wait untill it has created matlab.dat
    #print('Running thrust.exe for nonstandart thrust')
    subprocess.run('thrust.exe')
    #print('Done')
    time.sleep(0.5)
    
    #Output is thrust.dat, sum both engine thrusts together
    Tp = np.sum(np.genfromtxt('thrust.dat', dtype = 'float'), axis = 1)
    
    #Make file for standard thrust
    mdot_fs = 0.048 #mfs = 0.048 for standard thrust
    matlab = open('matlab.dat','w+')
    for i in range(len(hp)): 
         matlab.write(str(int(round(hplist[i],0))) +' '+ str(Mlist[i]) +' '+ str(round(Dtemplist[i],4)) +' '+ str(mdot_fs) +' '+ str(mdot_fs) + "\n")
    matlab.close()
    
    #Run thrust.exe and wait untill it has created matlab.dat
    #print('Running thrust.exe for standart thrust')
    subprocess.run('thrust.exe')
    #print('Done')
    time.sleep(0.5)
    
    #Output is thrust.dat, sum both engine thrusts togeter
    Tps = np.sum(np.genfromtxt('thrust.dat', dtype = 'float'), axis = 1)
    
    #Calculate (non)standard thrust coefficients
    d = 0.686 #characteristic diameter JT15D-4B
    Tc  = Tp / (0.5 * velocity(IAS,hp,TAT)[5] * velocity(IAS,hp,TAT)[3]**2 * d**2)
    Tcs = Tps / (0.5 * velocity(IAS,hp,TAT)[5] * velocity(IAS,hp,TAT)[3]**2 * d**2)
    
    return(Tp,Tps,Tc,Tcs)

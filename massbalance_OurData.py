# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:16:59 2019

@author: Sybren
"""

import numpy as np
import matplotlib.pyplot as plt

lbskg = 0.453592

Fmom = [298.16, 591.18, 879.08, 1165.42, 1448.40, 1732.53, 2014.80, 2298.84, 2581.92, 2866.30, 3150.18, 3434.52, 3718.52, 4003.23, 4287.76, 4572.24, 4856.56, 5141.16, 5425.64, 5709.90, 5994.04, 6278.47, 6562.82, 6846.96, 7131.00, 
7415.33, 7699.60, 7984.34, 8269.06, 8554.05, 8839.04, 9124.80, 9410.62, 9696.97, 9983.40, 10270.08, 10556.84, 10843.87, 11131.00, 11418.20, 11705.50, 11993.31, 12281.18, 12569.04, 12856.86, 13144.73, 13432.48, 13720.56, 14008.46, 14320.34]
Fmlist = list(np.arange(100., 5000., 100.)) + [5008.]
Ftot = 2600.

MP1 = 89./lbskg
MP2 = 92./lbskg
MCL = 79.5/lbskg
MCR = 79.5/lbskg
M1L = 85./lbskg
M1R = 72./lbskg
M2L = 61./lbskg
M2R = 86./lbskg
M3L = 68./lbskg  
M3R = 87./lbskg
xP = 131.
xC = 170.
x1 = 214.
x2 = 251.
x3 = 288.
BEM = 9165. 
xB = 292.18
g0 = 9.80665
inmet = 0.0254

tb_bolle = 2170.
te_bolle = 2292.

t = np.genfromtxt("matlab/Test-data/time.csv", dtype="float")
FUR = np.genfromtxt("matlab/Test-data/rh_engine_FU.csv", dtype="float")
FUL = np.genfromtxt("matlab/Test-data/lh_engine_FU.csv", dtype="float")


# enter time as a list
def massbalance(t):
    xcg = []
    W = []
    for i in range(len(t)):
        Fm = Ftot - (FUR[i] + FUL[i])
        if t[i] >= tb_bolle and t[i] <= te_bolle:
            Mom = BEM*xB + (MP1+MP2+M3R)*xP + (MCL+MCR)*xC + (M1L+M1R)*x1 + (M2L+M2R)*x2 + M3L*x3 + (np.interp(Fm, Fmlist, Fmom))*100.
        else:
            Mom = BEM*xB + (MP1+MP2)*xP + (MCL+MCR)*xC + (M1L+M1R)*x1 + (M2L+M2R)*x2 + (M3L+M3R)*x3 + (np.interp(Fm, Fmlist, Fmom))*100.
        # Weight in lbs
        Wi = BEM + MP1 + MP2 + MCL + MCR + M1L + M1R + M2L + M2R + M3L + M3R + Fm 
        # xcg in m w.r.t. LEMAC
        xcg.append(((Mom/Wi)-261.45)*inmet)
        # Weight list in N
        W.append(Wi*lbskg*g0)
    return (xcg, W)

plt.plot(t, massbalance(t)[1])
plt.show()

def massbalance_gewichthajo(t):
    #import time table
    #Time 1: Steady flight 2 -> measurement 6 before shift Hajo
    #Time 2: Steady flight 2 -> measurement 7 shift Hajo
    T1 = 2170.
    T2 = 2292.
    
    i = np.where(t == T1)
    j = np.where(t == T2)
    
    Fuel_used1 = 674
    Fuel_used2 = 702
    
    Fm1 = Ftot - Fuel_used1
    Fm2 = Ftot - Fuel_used2
    
    Mom1 = BEM*xB + (MP1+MP2)*xP + (MCL+MCR)*xC + (M1L+M1R)*x1 + (M2L+M2R)*x2 + (M3L+M3R)*x3 + (np.interp(Fm1, Fmlist, Fmom))*100.
    Mom2 = BEM*xB + (MP1+MP2+M3R)*xP + (MCL+MCR)*xC + (M1L+M1R)*x1 + (M2L+M2R)*x2 + M3L*x3 + (np.interp(Fm2, Fmlist, Fmom))*100.
                
    # Weight in lbs
    Wi1 = BEM + MP1 + MP2 + MCL + MCR + M1L + M1R + M2L + M2R + M3L + M3R + Fm1
    Wi2 = BEM + MP1 + MP2 + MCL + MCR + M1L + M1R + M2L + M2R + M3L + M3R + Fm2
    
    xcg1 = ((Mom1/Wi1)-261.45)*inmet
    xcg2 = ((Mom2/Wi2)-261.45)*inmet
    
    delta_cg = xcg2 - xcg1
    return delta_cg

delta_cg = massbalance_gewichthajo(t)
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:01:51 2019

@author: Anique
"""
import numpy as np
import matplotlib.pyplot as plt
from Velocity_calc import velocity
from massbalance import massbalance_gewichthajo
from math import *
t = np.genfromtxt("matlab/time.csv", dtype="float")

# Standard values used for calculation
P0 = 101325 #Pa
rho0 = 1.225 #kg/m^3
T0 = 288.15 #K
R = 287.057 # m^2/s^2*K
g0 = 9.80665 #m/s^2
lapse = -0.0065 #degC/m
S = 30.0 #m^2
BEW = 9165.0 #lbs
T = 0   #Thrust in Newton
Tcs = 5
Tc = 5

# Data from Stationary Measurement to calculate Cl, CD
hp1 = np.array([5010, 5020, 5020, 5030, 5020, 5110]) #Pressure Altitude in ft
IAS1 = np.array([249, 221, 192, 163, 130, 118]) #Indicated Airspeed in knots
AOA1 = np.array([1.7, 2.4, 3.6, 5.4, 8.7, 10.6]) #Angle of Attack in deg
FFL1 = np.array([798, 673, 561, 463, 443, 474]) #Fuel Flow Left in lbs/hr
FFR1 = np.array([813, 682, 579, 484, 467, 499]) #Fuel Flow Right in lbs/hr
Fused1 = np.array([360, 412, 447, 478, 532, 570]) #Fuel used in lbs
TAT1 = np.array([12.5, 10.5, 8.8, 7.2, 6, 5.2]) #Total air temperature in Celsius


# Data from Stationary Measurement to calculate Cmalpha, Cmdelta
hp2 = np.array([6060, 6350, 6550, 6880, 6160, 5810, 5310]) #Pressure Altitude in ft
IAS2 = np.array([161, 150, 140, 130, 173, 179, 192]) #Indicated Airspeed in knots
AOA2 = np.array([5.3, 6.3, 7.3, 8.5, 4.5, 4.1, 3.4]) #Angle of Attack in deg
Deltae2 = np.array([0, -0.4, -0.9, -1.5, 0.4, 0.6, 1]) #Elevator Deflection in deg
Deltaetr2 = np.array([2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8]) #Elevator trim tab Deflection in deg
StickF2 = np.array([0, -23, -29, -46, 26, 40, 83]) #Stick Force in Newton
FFL2 = np.array([462, 458, 454, 449, 465, 472, 482]) #Fuel Flow Left in lbs/hr
FFR2 = np.array([486, 482, 477, 473, 489, 496, 505]) #Fuel Flow Right in lbs/hr
Fused2 = np.array([664, 694, 730, 755, 798, 825, 846]) #Fuel used in lbs
TAT2 = np.array([5.5, 4.5, 3.5, 2.5, 5.0, 6.2, 8.2]) #Total air temperature in Celsius


# Data from shift in Center of Gravity
hp3 = np.array([5730, 5790]) #Pressure Altitude in ft
IAS3 = np.array([161, 161]) #Indicated Airspeed in knots
AOA3 = np.array([5.3, 5.3]) #Angle of Attack in deg
Deltae3 = np.array([0, -0.5]) #Elevator Deflection in deg
Deltatr3 = np.array([2.8, 2.8]) #Elevator trim tab Deflection in deg
StickF3 = np.array([0, -30]) #Stick Force in Newton
FFL3 = np.array([471, 468]) #Fuel Flow Left in lbs/hr
FFR3 = np.array([493, 490]) #Fuel Flow Right in lbs/hr
Fused3 = np.array([881, 910]) #Fuel used in lbs
TAT3 = np.array([5.0, 5.0]) #Total air temperature in Celsius


# Calculation of Cl and Cd, plot Cl-alpha, Cd-alpha, Cl-Cd graphs (Measurement 1)
def Cl_Cd(BEW, Fused, Vt, rho, S, T):
    
    Mfuel = 4050 #lbs
    Mperson = 695 #kg
    
    Mtotal = BEW*0.453592 + Mfuel*0.453592 + Mperson - Fused*0.453592 #Total mass in kg
    W = Mtotal*9.80665     #Weight in Newton
    
    Cl = W/(0.5*rho*Vt**2*S)
    Cd = T/(0.5*rho*Vt**2*S)        # Thrust based on Measurement 1
    
    return Cl, Cd, W

# Calculation graphs with results from test 1
vel1 = velocity(IAS1, hp1, TAT1)  #Output: Vc, M, a, Vt, Ve, rho
ClCd1 = Cl_Cd(BEW, Fused1, vel1[3], vel1[5], S, T)
#plt.plot(AOA1, ClCd1[0])              #Cl-alpha graph
#plt.plot(AOA1, ClCd1[1])              #Cd-alpha graph
#plt.plot(ClCd1[1], ClCd1[0])            #Cl-Cd graph
CLalpha = np.polyfit(AOA1, ClCd1[0], 1)
print(CLalpha)

#Calculation of Cmalpha, Cmdelta (Measurement 2 + CG shift)
vel2 = velocity(IAS2, hp2, TAT2) #Output: Vc, M, a, Vt, Ve, rho
ClCd2 = Cl_Cd(BEW, Fused2, vel2[3], vel2[5], S, T) #Output: Cl, Cd

vel3 = velocity(IAS3, hp3, TAT3) #Output: Vc, M, a, Vt, Ve, rho
ClCd3 = Cl_Cd(BEW, Fused3, vel3[3], vel3[5], S, T) #Output: Cl, Cd

mass = massbalance_gewichthajo(t)

def Cmdelta(BEW, Fused, Ve, Deltae, Cl, Tcs, Tc, mass, StickF):
    
    Ws = 60500      #Newton
    Mfuel = 4050 #lbs
    Mperson = 695 #kg
    Mtotal = BEW*0.453592 + Mfuel*0.453592 + Mperson - Fused*0.453592 #Total mass in kg
    W = Mtotal*9.80665     #Weight in Newton
    
    Vetilde = Ve*np.sqrt(Ws/W)
    Deltad  = Deltae[1] - Deltae[0] # Deltae based on data 3!
    Clavg = (Cl[0] + Cl[1])/2   # Cl based on data 3!
    cbar      = 2.0569	          # mean aerodynamic cord [m]
    DeltaCG = mass
    
    Cmdelta = -(1/Deltad)*Clavg*(DeltaCG/cbar)
    
    Cmtc = -0.0064      # Clean Cruise dimensionless thrust moment arm 
    Destar = Deltae - (1/Cmdelta)*Cmtc*(Tcs - Tc) #Calculate Reduced Elevator Deflection
    
    Stick = StickF*(Ws/W)
    
    return Vetilde, Cmdelta, Destar, Stick

Cmdelta1 = Cmdelta(BEW, Fused2, vel2[4], Deltae2, ClCd3[0], Tcs, Tc, mass, StickF2)
plt.plot(Cmdelta1[0], Cmdelta1[2])  #Ve - Delta eq star plot
plt.plot(Cmdelta1[0], Cmdelta1[3])  #Ve - Stick force plot
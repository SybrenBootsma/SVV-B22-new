# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:01:51 2019

@author: Anique
"""
import numpy as np
import matplotlib.pyplot as plt
from Functions import velocity, thrust
from massbalance import massbalance_gewichthajo
from math import *
t = np.genfromtxt("matlab/Test-data/time.csv", dtype="float")

# Standard values used for calculation
P0 = 101325 #Pa
rho0 = 1.225 #kg/m^3
T0 = 288.15 #K
R = 287.057 # m^2/s^2*K
g0 = 9.80665 #m/s^2
lapse = -0.0065 #degC/m
S = 30.0 #m^2
BEW = 9165.0 #lbs
gamma = 1.4
b = 15.911	#m
A = b**2/S


# Data from Stationary Measurement to calculate Cl, CD
hp1 = np.array([9000, 8990, 9000, 8980, 9000, 8990]) #Pressure Altitude in ft
IAS1 = np.array([251, 220, 193, 159, 133, 115]) #Indicated Airspeed in knots
AOA1 = np.array([1.2, 2, 2.9, 5, 7.6, 10.5]) #Angle of Attack in deg
FFL1 = np.array([776, 652, 605, 445, 429, 428]) #Fuel Flow Left in lbs/hr
FFR1 = np.array([826, 673, 635, 487, 467, 467]) #Fuel Flow Right in lbs/hr
Fused1 = np.array([372, 411, 439, 466, 484, 503]) #Fuel used in lbs
TAT1 = np.array([6.2, 3.6, 2, 0.5, -0.8, -1.2]) #Total air temperature in Celsius
T1 = thrust(hp1, IAS1, TAT1, FFR1, FFL1) #Tp,Tps,Tc,Tcs
TAT1 = np.array([6.2, 3.6, 2, 0.5, -0.8, -1.2]) #Total air temperature in Celsius


# Data from Stationary Measurement to calculate Cmalpha, Cmdelta
hp2 = np.array([7980, 8300, 8560, 7980, 7510]) #Pressure Altitude in ft
IAS2 = np.array([160, 150, 140, 171, 181]) #Indicated Airspeed in knots
AOA2 = np.array([4.8, 5.6, 6.7, 4.1, 3.5]) #Angle of Attack in deg
Deltae2 = np.array([-0.4, -0.8, -1.3, 0.1, 0.4]) #Elevator Deflection in deg
Deltaetr2 = np.array([2.1, 2.1, 2.1, 2.1, 2.1]) #Elevator trim tab Deflection in deg
StickF2 = np.array([1, -13, -26, 19, 40]) #Stick Force in Newton
FFL2 = np.array([426, 421, 413, 425, 433]) #Fuel Flow Left in lbs/hr
FFR2 = np.array([475, 470, 462, 475, 484]) #Fuel Flow Right in lbs/hr
Fused2 = np.array([558, 592, 610, 630, 652]) #Fuel used in lbs
TAT2 = np.array([1.5, 0.5, 0.2, 2.5, 3.8]) #Total air temperature in Celsius


# Data from shift in Center of Gravity
hp3 = np.array([7790, 7830]) #Pressure Altitude in ft
IAS3 = np.array([162, 162]) #Indicated Airspeed in knots
AOA3 = np.array([4.7, 4.7]) #Angle of Attack in deg
Deltae3 = np.array([-0.3, -0.8]) #Elevator Deflection in deg
Deltatr3 = np.array([2.3, 2.3]) #Elevator trim tab Deflection in deg
StickF3 = np.array([1, -25]) #Stick Force in Newton
FFL3 = np.array([426, 425]) #Fuel Flow Left in lbs/hr
FFR3 = np.array([477, 475]) #Fuel Flow Right in lbs/hr
Fused3 = np.array([674, 702]) #Fuel used in lbs
TAT3 = np.array([2.2, 2.5]) #Total air temperature in Celsius


# Calculation of Cl and Cd, plot Cl-alpha, Cd-alpha, Cl-Cd graphs (Measurement 1)
def Cl_Cd(BEW, Fused, Vt, rho, S, T):
    
    Mfuel = 2600 #lbs
    Mperson = 799 #kg
    
    Mtotal = BEW*0.453592 + Mfuel*0.453592 + Mperson - Fused*0.453592 #Total mass in kg
    W = Mtotal*9.80665     #Weight in Newton
    
    Cl = W/(0.5*rho*Vt**2*S)
    Cd = T/(0.5*rho*Vt**2*S)        # Thrust based on Measurement 1
    
    return Cl, Cd, W

# Calculation graphs with results from test 1
vel1 = velocity(IAS1, hp1, TAT1)  #Output: Vc, M, a, Vt, Ve, rho
ClCd1 = Cl_Cd(BEW, Fused1, vel1[3], vel1[5], S, T1[0])
plt.figure(1)
plt.subplots_adjust(top=0.957,bottom=0.07,left=0.064,right=0.987,hspace=0.239,wspace=0.14)
plt.subplot(221)
plt.title("$C_L - \\alpha$ curve")
plt.xlabel('$\\alpha$ [deg]')
plt.ylabel('$C_L$ [-]')
plt.grid(True)
plt.plot(AOA1, ClCd1[0])              #Cl-alpha graph
#plt.figure(2)
#plt.xlabel('Alpha')
#plt.ylabel('Cd')
#plt.plot(AOA1, ClCd1[1])              #Cd-alpha graph
#plt.figure(3)
plt.subplot(222)
plt.title("$C_L - C_D$ curve")
plt.xlabel('$C_D$ [-]')
plt.ylabel('$C_L$ [-]')
plt.grid(True)
plt.plot(ClCd1[1], ClCd1[0])            #Cl-Cd graph
CLalpha = np.polyfit(AOA1, ClCd1[0], 1)[0]
print('CL Alpha is ', CLalpha*180/pi)

Update = np.polyfit(ClCd1[0]**2, ClCd1[1], 1)
print('Cd0 is', Update[1])
print('e is', 1/(Update[0]*pi*A))

#Calculation of Cmalpha, Cmdelta (Measurement 2 + CG shift)
T2 = thrust(hp2, IAS2, TAT2, FFR2, FFL2) #Tp,Tps,Tc,Tcs
TAT2 = np.array([1.5, 0.5, 0.2, 2.5, 3.8]) #Total air temperature in Celsius
vel2 = velocity(IAS2, hp2, TAT2) #Output: Vc, M, a, Vt, Ve, rho
ClCd2 = Cl_Cd(BEW, Fused2, vel2[3], vel2[5], S, T2[0]) #Output: Cl, Cd

T3 = thrust(hp3, IAS3, TAT3, FFR3, FFL3) #Tp,Tps,Tc,Tcs
TAT3 = np.array([2.2, 2.5]) #Total air temperature in Celsius
vel3 = velocity(IAS3, hp3, TAT3) #Output: Vc, M, a, Vt, Ve, rho
ClCd3 = Cl_Cd(BEW, Fused3, vel3[3], vel3[5], S, T3[0]) #Output: Cl, Cd

mass = massbalance_gewichthajo(t)

def Cmdelta(BEW, Fused, Ve, Deltae, Cl, Tcs, Tc, mass, StickF):
    
    Ws = 60500   #Newton
    Mfuel = 2600 #lbs
    Mperson = 799 #kg
    Mtotal = BEW*0.453592 + Mfuel*0.453592 + Mperson - Fused*0.453592 #Total mass in kg
    W = Mtotal*9.80665     #Weight in Newton
    
    Vetilde = Ve*np.sqrt(Ws/W)
    Deltad  = Deltae[1] - Deltae[0] # Deltae based on data 3!
    Clavg = (Cl[0] + Cl[1])/2       # Cl based on data 3!
    cbar      = 2.0569	            # mean aerodynamic cord [m]
    DeltaCG = mass
    
    Cmdelta = -(1/Deltad)*Clavg*(DeltaCG/cbar)
    
    Cmtc = -0.0064      # Clean Cruise dimensionless thrust moment arm 
    Destar = Deltae - (1/Cmdelta)*Cmtc*(Tcs - Tc) #Calculate Reduced Elevator Deflection
    
    Stick = StickF*(Ws/W)
    
    return Vetilde, Cmdelta, Destar, Stick

Cmdelta1 = Cmdelta(BEW, Fused2, vel2[4], Deltae2, ClCd3[0], T2[3], T2[2], mass, StickF2)
#plt.figure(4)
plt.subplot(223)
plt.title("$\delta_e^{\star} - \\tilde{V}_e$ curve")
plt.grid(True)
plt.xlabel("$\\tilde{V}_e$ [m/s]")
plt.ylabel("$\delta_e^{\star}$ [deg]")
plt.plot(Cmdelta1[0], Cmdelta1[2])  #Ve - Delta eq star plot

#plt.figure(5)
plt.subplot(224)
plt.title("$F_e^{\star} - \\tilde{V}_e$ curve")
plt.xlabel("$\\tilde{V}_e$ [m/s]")
plt.ylabel("$F_e^{\star} [N]$")
plt.grid(True)
plt.plot(Cmdelta1[0], Cmdelta1[3])  #Ve - Stick force plot
print('CM Delta is ', Cmdelta1[1]*180/pi)

Cmalpha = np.polyfit(AOA2, Cmdelta1[2], 1)[0] * -Cmdelta1[1]
print('CM Alpha is ', Cmalpha*180/pi)
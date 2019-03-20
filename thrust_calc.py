#Thrust calculator
import numpy as np
import subprocess
import time
from Velocity_calc import velocity
#uncomment for testing
hp1 = np.array([5010, 5020, 5020, 5030, 5020, 5110]) #Pressure Altitude in ft
IAS1 = np.array([249, 221, 192, 163, 130, 118]) #Indicated Airspeed in knots
AOA1 = np.array([1.7, 2.4, 3.6, 5.4, 8.7, 10.6]) #Angle of Attack in deg
FFL1 = np.array([798, 673, 561, 463, 443, 474]) #Fuel Flow Left in lbs/hr
FFR1 = np.array([813, 682, 579, 484, 467, 499]) #Fuel Flow Right in lbs/hr
Fused1 = np.array([360, 412, 447, 478, 532, 570]) #Fuel used in lbs
TAT1 = np.array([12.5, 10.5, 8.8, 7.2, 6, 5.2]) #Total air temperature in Celsius

#%% Define function

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

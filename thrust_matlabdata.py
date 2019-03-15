#Thrust calculator
import numpy as np
import subprocess
import time
#%% Define functions
#Takes pressure altitude in meters and returns ISA temperature in Kelvins
def hp2TISA(hp):
    T0 = 288.15
   
    if hp<=11000:                #Troposhere
        t = T0+(-0.0065*hp)    
    
    if 11000<hp<=20000:
        t = 216.65
    return t

#%%Specify data paths, note that this .py script should be 
#in same directory as the matlab folder and thrust.exe
hploc  = 'matlab/Dadc1_alt.csv'
Mloc   = 'matlab/Dadc1_mach.csv'
TATloc = 'matlab/Dadc1_tat.csv'
FFlloc = 'matlab/lh_engine_FMF.csv'
FFrloc = 'matlab/rh_engine_FMF.csv'
t0 = 26000 #index of starting point of calculation
t1 = 27000 #index of endpoint of calculation

#%% Create matlab.dat [height M deltatemp FFl FFr]
#Pressure alt. (hp)
hplist = np.genfromtxt(hploc, dtype = 'float')
hplist = [round(i * 0.3048, 4) for i in hplist] #convert feet to meters

#Mach number
Mlist = np.genfromtxt(Mloc, dtype = 'float')

#Deltatemp
TATlist = np.genfromtxt(TATloc, dtype = 'float')
for i in range(len(TATlist)):
    TATlist[i] = TATlist[i] + 275.15 #convert Celsius to Kelvin

TISAlist = []
for i in range(len(hplist)):
    TISA = hp2TISA(hplist[i])
    TISAlist.append(TISA)
    
Dtemplist = TATlist - TISAlist

#Fuelflow
FFllist = np.genfromtxt(FFlloc, dtype = 'float') #Left in [lbs/hr]
FFrlist = np.genfromtxt(FFrloc, dtype = 'float') #Right

FFllist = FFllist * 0.45359237/3600 #convert lbs/hr to kg/s
FFrlist = FFrlist * 0.45359237/3600

#%% Create thrust files
#Make file for nonstandart thrust
matlab = open('matlab.dat','w+')
for i in range(t0,t1):
     matlab.write(str(int(round(hplist[i],0))) +' '+ str(format(Mlist[i], '.4f')) +' '+ str(round(Dtemplist[i],4)) +' '+ str(round(FFllist[i],5)) +' '+ str(round(FFrlist[i],5)) + "\n")
matlab.close()

#Run thrust.exe and wait untill it has created matlab.dat
print('Running thrust.exe for nonstandart thrust')
subprocess.run('thrust.exe')
print('Done')
time.sleep(0.5)

#Output is thrust.dat, sum both engine thrusts together
Tc = np.sum(np.genfromtxt('thrust.dat', dtype = 'float'), axis = 1)

#Make file for standard thrust
mdot_fs = 0.048 #mfs = 0.048 for standard thrust
matlab = open('matlab.dat','w+')
for i in range(t0,t1): 
     matlab.write(str(int(round(hplist[i],0))) +' '+ str(format(Mlist[i], '.4f')) +' '+ str(round(Dtemplist[i],4)) +' '+ str(mdot_fs) +' '+ str(mdot_fs) + "\n")
matlab.close()

#Run thrust.exe and wait untill it has created matlab.dat
print('Running thrust.exe for standart thrust')
subprocess.run('thrust.exe')
print('Done')
time.sleep(0.5)

#Output is thrust.dat, sum both engine thrusts together
Tcs = np.sum(np.genfromtxt('thrust.dat', dtype = 'float'), axis = 1)

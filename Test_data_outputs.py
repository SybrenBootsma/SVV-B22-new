import numpy as np
import matplotlib.pyplot as plt


time_ref = np.genfromtxt("matlab/Test-data/time.csv", dtype="float")

delta_e_ref = np.genfromtxt("matlab/Test-data/delta_e.csv", dtype="float")

tas_ref = np.genfromtxt("matlab/Test-data/Dadc1_tas.csv", dtype="float")
alpha_ref = np.genfromtxt("matlab/Test-data/vane_AOA.csv", dtype="float") #body
pitch_ref = np.genfromtxt("matlab/Test-data/Ahrs1_Pitch.csv", dtype="float")
pitch_rate_ref = np.genfromtxt("matlab/Test-data/Ahrs1_bPitchRate.csv", dtype="float")

hp_ref = np.genfromtxt("matlab/Test-data/Dadc1_alt.csv", dtype="float")

#tat_ref = np.genfromtxt("matlab/Ref-data/Dadc1_tat.csv", dtype="float")

delta_a_ref = np.genfromtxt("matlab/Test-data/delta_a.csv", dtype="float")
delta_r_ref = np.genfromtxt("matlab/Test-data/delta_r.csv", dtype="float")

beta_ref = np.genfromtxt("matlab/Test-data/Fms1_trueHeading.csv", dtype="float")
roll_ref = np.genfromtxt("matlab/Test-data/Ahrs1_Roll.csv", dtype="float")
roll_rate_ref = np.genfromtxt("matlab/Test-data/Ahrs1_bRollRate.csv", dtype="float")
yaw_rate_ref = np.genfromtxt("matlab/Test-data/Ahrs1_bYawRate.csv", dtype="float")

left_FU = np.genfromtxt("matlab/Test-data/lh_engine_FU.csv", dtype="float")
right_FU = np.genfromtxt("matlab/Test-data/rh_engine_FU.csv", dtype="float")

mass_ref = []                       
mass_init = 6136
for i in range(len(time_ref)):
    mass_ref.append(5000-left_FU[i]*0.453592- right_FU[i]*0.453592)


for i in range(len(time_ref)):
    
    pitch_rate_ref[i] = np.deg2rad(pitch_rate_ref[i])
    delta_e_ref[i] = np.deg2rad(delta_e_ref[i])
    alpha_ref[i] = np.deg2rad(alpha_ref[i])
    pitch_ref[i] = np.deg2rad(pitch_ref[i])
    delta_a_ref[i] = np.deg2rad(delta_a_ref[i])
    delta_r_ref[i] = np.deg2rad(delta_r_ref[i])
    beta_ref[i] = np.deg2rad(beta_ref[i])
    roll_ref[i] = np.deg2rad(roll_ref[i])
    roll_rate_ref[i] = np.deg2rad(roll_rate_ref[i])
    yaw_rate_ref[i] = np.deg2rad(yaw_rate_ref[i])

def Pheugoid_init():
    
    for i in range(len(time_ref)):
        if time_ref[i] == 2490.-5.:
            begin_idx = i
        if time_ref[i] == 2490.:
            end_idx = i
    mass = mass_ref[begin_idx]
    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_e0 = np.mean(delta_e_ref[begin_idx:end_idx])
    return mass, hp0, Vt0, alpha0, th0, delta_e0




def Pheugoid():
    delta_e0 = Pheugoid_init()[-1]
    #print (delta_e0)
    #pheugoid 250 sec
    for i in range(len(time_ref)):
        if time_ref[i] == 2490.:
            begin_idx = i
        if time_ref[i] == 2630.:
            end_idx = i
    #pheugoid lists
    time = time_ref[begin_idx:end_idx]
    pitch_rate = pitch_rate_ref[begin_idx:end_idx]
    delta_e = delta_e_ref[begin_idx:end_idx]
    alpha = alpha_ref[begin_idx:end_idx]
    pitch = pitch_ref[begin_idx:end_idx]
    u = tas_ref[begin_idx:end_idx]
    for i in range(len(time)):

        delta_e[i]= delta_e[i]-delta_e0
        
    return time, pitch_rate, delta_e, alpha, pitch, u



def Short_period_init():
    
    for i in range(len(time_ref)):
        if time_ref[i] == 2441.-5.:
            begin_idx = i
        if time_ref[i] == 2441:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_e0 = np.mean(delta_e_ref[begin_idx:end_idx])   
    return mass, hp0, Vt0, alpha0, th0, delta_e0


def Short_period():
    delta_e0 = Short_period_init()[-1]
    for i in range(len(time_ref)):
        if time_ref[i] == 2441.:
            begin_idx = i
        if time_ref[i] == 2475.:
            end_idx = i
    
    #shortperiod lists
    time = time_ref[begin_idx:end_idx]
    pitch_rate = pitch_rate_ref[begin_idx:end_idx]
    delta_e = delta_e_ref[begin_idx:end_idx]
    alpha = alpha_ref[begin_idx:end_idx]
    pitch = pitch_ref[begin_idx:end_idx]
    u = tas_ref[begin_idx:end_idx]
    for i in range(len(time)):
        delta_e[i]= delta_e[i]-delta_e0

    return time, pitch_rate, delta_e, alpha, pitch, u


def Dutch_roll_init():
 
    for i in range(len(time_ref)):
        if time_ref[i] == 2712.-5.:
            begin_idx = i
        if time_ref[i] == 2712.:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_r0 = np.mean(delta_r_ref[begin_idx:end_idx])
    delta_a0 = np.mean(delta_a_ref[begin_idx:end_idx])
    roll0 = np.mean(roll_ref[begin_idx:end_idx])
    roll_rate0 = np.mean(roll_rate_ref[begin_idx:end_idx])
    yaw_rate0 = np.mean(yaw_rate_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0, roll0, roll_rate0, yaw_rate0  


def Dutch_roll():
    delta_r0 = Dutch_roll_init()[5]
    #print (delta_r0)
    delta_a0 = Dutch_roll_init()[6]
    for i in range(len(time_ref)):
        if time_ref[i] == 2712.:
            begin_idx = i
        if time_ref[i] == 2737.:
            end_idx = i
    
    #shortperiod lists
    time = time_ref[begin_idx:end_idx]
    delta_r = delta_r_ref[begin_idx:end_idx]
    delta_r_2 = delta_r_ref[begin_idx:end_idx]
    delta_a = delta_a_ref[begin_idx:end_idx]
    beta = beta_ref[begin_idx:end_idx]
    roll = roll_ref[begin_idx:end_idx]
    roll_rate = roll_rate_ref[begin_idx:end_idx]
    yaw_rate = yaw_rate_ref[begin_idx:end_idx]
    
    for i in range(len(time)):
        #print(delta_r[i])
        delta_r[i] = delta_r[i]-delta_r0
        delta_a[i] = delta_a[i]-delta_a0
        #print(delta_r[i])
        #print()
    #print(delta_r)     


    return time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate

#time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate = Dutch_roll()



def Dutch_roll_YD_init():
 
    for i in range(len(time_ref)):
        if time_ref[i] == 2765.-5.:
            begin_idx = i
        if time_ref[i] == 2765:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_r0 = np.mean(delta_r_ref[begin_idx:end_idx])
    delta_a0 = np.mean(delta_a_ref[begin_idx:end_idx])
    roll0 = np.mean(roll_ref[begin_idx:end_idx])
    roll_rate0 = np.mean(roll_rate_ref[begin_idx:end_idx])
    yaw_rate0 = np.mean(yaw_rate_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0, roll0, roll_rate0, yaw_rate0


def Dutch_roll_YD():
    delta_r0 = Dutch_roll_YD_init()[5]
    delta_a0 = Dutch_roll_YD_init()[6]
    for i in range(len(time_ref)):
        if time_ref[i] == 2765.:
            begin_idx = i
        if time_ref[i] == 2780.:
            end_idx = i
    
    #shortperiod lists
    time = time_ref[begin_idx:end_idx]
    
    delta_r = delta_r_ref[begin_idx:end_idx]
    delta_a = delta_a_ref[begin_idx:end_idx]
    beta = beta_ref[begin_idx:end_idx]
    roll = roll_ref[begin_idx:end_idx]
    roll_rate = roll_rate_ref[begin_idx:end_idx]
    yaw_rate = yaw_rate_ref[begin_idx:end_idx]
    for i in range(len(time)):
        delta_r[i] = delta_r[i]-delta_r0
        delta_a[i] = delta_a[i]-delta_a0
    

    return time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate    
    


def Aperiodic_roll_init():
 
    for i in range(len(time_ref)):
        if time_ref[i] == 2380.-5.:
            begin_idx = i
        if time_ref[i] == 2380:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_r0 = np.mean(delta_r_ref[begin_idx:end_idx])
    delta_a0 = np.mean(delta_a_ref[begin_idx:end_idx])
    roll0 = np.mean(roll_ref[begin_idx:end_idx])
    roll_rate0 = np.mean(roll_rate_ref[begin_idx:end_idx])
    yaw_rate0 = np.mean(yaw_rate_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0, roll0, roll_rate0, yaw_rate0


def Aperiodic_roll():
    delta_r0 = Aperiodic_roll_init()[5]
    delta_a0 = Aperiodic_roll_init()[6]
    
    for i in range(len(time_ref)):
        if time_ref[i] == 2380.:
            begin_idx = i
        if time_ref[i] == 2400.:
            end_idx = i
    
    #shortperiod lists
    time = time_ref[begin_idx:end_idx]
    
    delta_r = delta_r_ref[begin_idx:end_idx]
    delta_a = delta_a_ref[begin_idx:end_idx]
    beta = beta_ref[begin_idx:end_idx]
    roll = roll_ref[begin_idx:end_idx]
    roll_rate = roll_rate_ref[begin_idx:end_idx]
    yaw_rate = yaw_rate_ref[begin_idx:end_idx]
    for i in range(len(time)):
        delta_r[i] = delta_r[i]-delta_r0
        delta_a[i] = delta_a[i]-delta_a0
    

    return time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate    
    
def Spiral_init():

    for i in range(len(time_ref)):
        if time_ref[i] == 2845-5.:
            begin_idx = i
        if time_ref[i] == 2845:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_r0 = np.mean(delta_r_ref[begin_idx:end_idx])
    delta_a0 = np.mean(delta_a_ref[begin_idx:end_idx])
    roll0 = np.mean(roll_ref[begin_idx:end_idx])
    roll_rate0 = np.mean(roll_rate_ref[begin_idx:end_idx])
    yaw_rate0 = np.mean(yaw_rate_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0, roll0, roll_rate0, yaw_rate0


def Spiral():
    
    delta_r0 = Spiral_init()[5]
    delta_a0 = Spiral_init()[6]
    
    for i in range(len(time_ref)):
        if time_ref[i] == 2845.:
            begin_idx = i
        if time_ref[i] == 3050.:
            end_idx = i
    
    #shortperiod lists
    time = time_ref[begin_idx:end_idx]
    
    delta_r = delta_r_ref[begin_idx:end_idx]
    delta_a = delta_a_ref[begin_idx:end_idx]
    beta = beta_ref[begin_idx:end_idx]
    roll = roll_ref[begin_idx:end_idx]
    roll_rate = roll_rate_ref[begin_idx:end_idx]
    yaw_rate = yaw_rate_ref[begin_idx:end_idx]
    for i in range(len(time)):
        delta_r[i] = delta_r[i]-delta_r0
        delta_a[i] = delta_a[i]-delta_a0
    

    return time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate    
    


#mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0 = Spiral_init()
#time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate = Spiral() 
#
#plt.plot(time,delta_r, label = "Roll input")
#plt.plot(time,delta_a, label = 'Yaw input')
#plt.plot(time, beta, label = 'Beta')
#plt.plot(time, roll, label = 'roll')
#plt.plot(time, roll_rate, label = 'roll rate')
#plt.plot(time, yaw_rate, label = 'yaw rate')
#plt.legend()
#plt.show()

##mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0 = Dutch_roll_init()
#time, pitch_rate, delta_e, alpha, pitch, u = Short_period() 
#
##plt.plot(time,pitch_rate, label = "pitch rate")
#plt.plot(time,delta_e, label = 'delta e')
#plt.plot(time, alpha, label = 'alpha')
#plt.plot(time,pitch , label = 'pitch')
##plt.plot(time, u, label = 'u')
#plt.legend()
#plt.show()


#

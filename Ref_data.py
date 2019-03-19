import numpy as np
import matplotlib.pyplot as plt


time_ref = np.genfromtxt("matlab/Ref-data/time.csv", dtype="float")

delta_e_ref = np.genfromtxt("matlab/Ref-data/delta_e.csv", dtype="float")

tas_ref = np.genfromtxt("matlab/Ref-data/Dadc1_tas.csv", dtype="float")
alpha_ref = np.genfromtxt("matlab/Ref-data/vane_AOA.csv", dtype="float") #body
pitch_ref = np.genfromtxt("matlab/Ref-data/Ahrs1_Pitch.csv", dtype="float")
pitch_rate_ref = np.genfromtxt("matlab/Ref-data/Ahrs1_bPitchRate.csv", dtype="float")

hp_ref = np.genfromtxt("matlab/Ref-data/Dadc1_alt.csv", dtype="float")

#tat_ref = np.genfromtxt("matlab/Ref-data/Dadc1_tat.csv", dtype="float")

delta_a_ref = np.genfromtxt("matlab/Ref-data/delta_a.csv", dtype="float")
delta_r_ref = np.genfromtxt("matlab/Ref-data/delta_r.csv", dtype="float")

beta_ref = np.genfromtxt("matlab/Ref-data/Fms1_trueHeading.csv", dtype="float")
roll_ref = np.genfromtxt("matlab/Ref-data/Ahrs1_Roll.csv", dtype="float")
roll_rate_ref = np.genfromtxt("matlab/Ref-data/Ahrs1_bRollRate.csv", dtype="float")
yaw_rate_ref = np.genfromtxt("matlab/Ref-data/Ahrs1_bYawRate.csv", dtype="float")

left_FU = np.genfromtxt("matlab/Ref-data/lh_engine_FU.csv", dtype="float")
right_FU = np.genfromtxt("matlab/Ref-data/rh_engine_FU.csv", dtype="float")

mass_ref = []                       
mass_init = 6689
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
        if time_ref[i] == 3223.:
            begin_idx = i
        if time_ref[i] == 3228.:
            end_idx = i
    mass = mass_ref[begin_idx]
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0

range(len(time_ref))


def Pheugoid():
      
    #pheugoid 250 sec
    for i in range(len(time_ref)):
        if time_ref[i] == 3220.:
            begin_idx = i
        if time_ref[i] == 3457.:
            end_idx = i
    #pheugoid lists
    time = time_ref[begin_idx:end_idx]
    pitch_rate = pitch_rate_ref[begin_idx:end_idx]
    delta_e = delta_e_ref[begin_idx:end_idx]
    alpha = alpha_ref[begin_idx:end_idx]
    pitch = pitch_ref[begin_idx:end_idx]
    u = tas_ref[begin_idx:end_idx]
    
    return time, pitch_rate, delta_e, alpha, pitch, u



def Short_period_init():
    
    for i in range(len(time_ref)):
        if time_ref[i] == 3633.-5.:
            begin_idx = i
        if time_ref[i] == 3633:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0


def Short_period():
    
    for i in range(len(time_ref)):
        if time_ref[i] == 3630.:
            begin_idx = i
        if time_ref[i] == 3650.:
            end_idx = i
    
    #shortperiod lists
    time = time_ref[begin_idx:end_idx]
    pitch_rate = pitch_rate_ref[begin_idx:end_idx]
    delta_e = delta_e_ref[begin_idx:end_idx]
    alpha = alpha_ref[begin_idx:end_idx]
    pitch = pitch_ref[begin_idx:end_idx]
    u = tas_ref[begin_idx:end_idx]
    return time, pitch_rate, delta_e, alpha, pitch, u


def Dutch_roll_init():
 
    for i in range(len(time_ref)):
        if time_ref[i] == 3716.-5.:
            begin_idx = i
        if time_ref[i] == 3716:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_r0 = np.mean(delta_r_ref[begin_idx:end_idx])
    delta_a0 = np.mean(delta_a_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0   


def Dutch_roll():
    
    for i in range(len(time_ref)):
        if time_ref[i] == 3716.:
            begin_idx = i
        if time_ref[i] == 3757.:
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

def Dutch_roll_YD_init():
 
    for i in range(len(time_ref)):
        if time_ref[i] == 3766.-5.:
            begin_idx = i
        if time_ref[i] == 3766:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_r0 = np.mean(delta_r_ref[begin_idx:end_idx])
    delta_a0 = np.mean(delta_a_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0 


def Dutch_roll_YD():
    
    for i in range(len(time_ref)):
        if time_ref[i] == 3766.:
            begin_idx = i
        if time_ref[i] == 3796.:
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
        if time_ref[i] == 3545.-5.:
            begin_idx = i
        if time_ref[i] == 3545:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_r0 = np.mean(delta_r_ref[begin_idx:end_idx])
    delta_a0 = np.mean(delta_a_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0


def Aperiodic_roll():
    
    for i in range(len(time_ref)):
        if time_ref[i] == 3545.:
            begin_idx = i
        if time_ref[i] == 3580.:
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
        if time_ref[i] == 3545.-5.:
            begin_idx = i
        if time_ref[i] == 3545:
            end_idx = i
    mass = mass_ref[begin_idx]    
    hp0 = np.mean(hp_ref[begin_idx:end_idx]*0.3048)
    Vt0 = np.mean(tas_ref[begin_idx:end_idx])
    alpha0 = np.mean(alpha_ref[begin_idx:end_idx])
    th0 = np.mean(pitch_ref[begin_idx:end_idx])
    delta_r0 = np.mean(delta_r_ref[begin_idx:end_idx])
    delta_a0 = np.mean(delta_a_ref[begin_idx:end_idx])
    
    return mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0 


def Spiral():
    
    for i in range(len(time_ref)):
        if time_ref[i] == 3900.:
            begin_idx = i
        if time_ref[i] == 4200.:
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
    

mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0 = Spiral_init()
time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate = Spiral() 

plt.plot(time,delta_r, label = "Roll input")
plt.plot(time,delta_a, label = 'Yaw input')
plt.plot(time, beta, label = 'Beta')
plt.plot(time, roll, label = 'roll')
plt.plot(time, roll_rate, label = 'roll rate')
plt.plot(time, yaw_rate, label = 'yaw rate')
plt.legend()
plt.show()



#
#plt.subplot(121)
#plt.plot(time_p,pitch_rate_p, label = 'pitch rate')
#plt.plot(time_p,delta_e_p, label = 'delta e')
#plt.plot(time_p,alpha_p, label = 'alpha')
#plt.legend()
#
#plt.subplot(122)
#plt.plot(time_s,pitch_rate_s, label = 'pitch rate')
#plt.plot(time_s,delta_e_s, label = 'delta e')
#plt.plot(time_s,alpha_s, label = 'alpha')
#plt.legend()
#plt.show()
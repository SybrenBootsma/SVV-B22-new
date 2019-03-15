import numpy as np
import matplotlib.pyplot as plt
time = np.genfromtxt("matlab/time.csv", dtype="float")
pitch_rate = np.genfromtxt("matlab/Ahrs1_bPitchRate.csv", dtype="float")
delta_e = np.genfromtxt("matlab/delta_e.csv", dtype="float")
alpha = np.genfromtxt("matlab/vane_AOA.csv", dtype="float") #body
hp = np.genfromtxt("matlab/Dadc1_alt.csv", dtype="float")
pitch = np.genfromtxt("matlab/Ahrs1_Pitch.csv", dtype="float")
tat = np.genfromtxt("matlab/Dadc1_tat.csv", dtype="float")
tas = np.genfromtxt("matlab/Dadc1_tas.csv", dtype="float")


for i in range(len(time)):
    
    pitch_rate[i] = np.deg2rad(pitch_rate[i])
    delta_e[i] = np.deg2rad(delta_e[i])
    alpha[i] = np.deg2rad(alpha[i])
    pitch[i] = np.deg2rad(pitch[i])

def Pheugoid_init():
    
    for i in range(len(time)):
        if time[i] == 3223.:
            begin_p = i
        if time[i] == 3228.:
            end_p = i
    
    hp0_p = np.mean(hp[begin_p:end_p]*0.3048)
    tas_p = np.mean(tas[begin_p:end_p])
    alpha0_p = np.mean(alpha[begin_p:end_p])
    pitch0_p = np.mean(pitch[begin_p:end_p])
    
    return hp0_p, tas_p, alpha0_p, pitch0_p


def Pheugoid():
      
    #pheugoid 250 sec
    for i in range(len(time)):
        if time[i] == 3220.:
            begin_p = i
        if time[i] == 3457.:
            end_p = i
    #pheugoid lists
    time_p = time[begin_p:end_p]
    pitch_rate_p = pitch_rate[begin_p:end_p]
    delta_e_p = delta_e[begin_p:end_p]
    alpha_p = alpha[begin_p:end_p]
    pitch_p = pitch[begin_p:end_p]
    u_p = tas[begin_p:end_p]
    
    return time_p, pitch_rate_p, delta_e_p, alpha_p, pitch_p, u_p


def Short_period():
    
    #short period 15 sec
    for i in range(len(time)):
        if time[i] == 3630.:
            begin_s = i
        if time[i] == 3650.:
            end_s = i
    
    #shortperiod lists
    time_s = time[begin_s:end_s]
    pitch_rate_s = pitch_rate[begin_s:end_s]
    delta_e_s = delta_e[begin_s:end_s]
    alpha_s = alpha[begin_s:end_s]
    
    return time_s, pitch_rate_s, delta_e_s, alpha_s


time_p, pitch_rate_p, delta_e_p, alpha_p, pitch_p, u_p = Pheugoid()


#plt.subplot(121)
plt.plot(time_p,pitch_rate_p, label = 'pitch rate')
plt.plot(time_p,delta_e_p, label = 'delta e')
#plt.plot(time_p,alpha_p, label = 'alpha')
plt.legend()
#
#plt.subplot(122)
#plt.plot(time_s,pitch_rate_s, label = 'pitch rate')
#plt.plot(time_s,delta_e_s, label = 'delta e')
#plt.plot(time_s,alpha_s, label = 'alpha')
#plt.legend()
#plt.show()
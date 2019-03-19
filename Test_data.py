# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:41:49 2019

@author: Sybren
"""

import matplotlib.pyplot as plt
import math
import numpy as np

time = np.genfromtxt("matlab/test-data/time.csv", dtype="float")
pitch_rate = np.genfromtxt("matlab/test-data/Ahrs1_bPitchRate.csv", dtype="float")
delta_e = np.genfromtxt("matlab/test-data/delta_e.csv", dtype="float")
alpha = np.genfromtxt("matlab/test-data/vane_AOA.csv", dtype="float") #body
hp = np.genfromtxt("matlab/test-data/Dadc1_alt.csv", dtype="float")
pitch = np.genfromtxt("matlab/test-data/Ahrs1_Pitch.csv", dtype="float")
tat = np.genfromtxt("matlab/test-data/Dadc1_tat.csv", dtype="float")
tas = np.genfromtxt("matlab/test-data/Dadc1_tas.csv", dtype="float")


for i in range(len(time)):
    pitch_rate[i] = np.deg2rad(pitch_rate[i])
    delta_e[i] = np.deg2rad(delta_e[i])
    alpha[i] = np.deg2rad(alpha[i])
    pitch[i] = np.deg2rad(pitch[i])
    
#phugoid 250 sec
for i in range(len(time)):
    if time[i] == (41*60+28):
        begin_p = i
    elif time[i] == (43*60+50):
        end_p = i

#phugoid lists
time_p = time[begin_p:end_p]
pitch_rate_p = pitch_rate[begin_p:end_p]
delta_e_p = delta_e[begin_p:end_p]
alpha_p = alpha[begin_p:end_p]


#short period 10 sec
for i in range(len(time)):
    if time[i] == (40*60+42):
        begin_s = i
    elif time[i] == (40*60+42+10):
        end_s = i

#shortperiod lists
time_s = time[begin_s:end_s]
pitch_rate_s = pitch_rate[begin_s:end_s]
delta_e_s = delta_e[begin_s:end_s]
alpha_s = alpha[begin_s:end_s]

#Dutch roll without damping
for i in range(len(time)):
    if time[i] == (45*60+14):
        begin_d = i
    elif time[i] == (45*60+14+20):
        end_d = i

#Dutch roll lists
time_d = time[begin_d:end_d]
pitch_rate_d = pitch_rate[begin_d:end_d]
delta_e_d = delta_e[begin_d:end_d]
alpha_d = alpha[begin_d:end_d]

#Dutch roll with damping
for i in range(len(time)):
    if time[i] == (46*60+7):
        begin_dd = i
    elif time[i] == (46*60+7+20):
        end_dd = i

#Dutch roll lists
time_dd = time[begin_dd:end_dd]
pitch_rate_dd = pitch_rate[begin_dd:end_dd]
delta_e_dd = delta_e[begin_dd:end_dd]
alpha_dd = alpha[begin_dd:end_dd]


plt.subplot(221)
plt.plot(time_p,pitch_rate_p, label = 'pitch rate')
plt.plot(time_p,delta_e_p, label = 'delta e')
plt.plot(time_p,alpha_p, label = 'alpha')
plt.legend()

plt.subplot(222)
plt.plot(time_s,pitch_rate_s, label = 'pitch rate')
plt.plot(time_s,delta_e_s, label = 'delta e')
plt.plot(time_s,alpha_s, label = 'alpha')
plt.legend()
plt.show()

plt.subplot(223)
plt.plot(time_d,pitch_rate_d, label = 'pitch rate')
plt.plot(time_d,delta_e_d, label = 'delta e')
plt.plot(time_d,alpha_d, label = 'alpha')
plt.legend()
plt.show()

plt.subplot(224)
plt.plot(time_dd,pitch_rate_dd, label = 'pitch rate')
plt.plot(time_dd,delta_e_dd, label = 'delta e')
plt.plot(time_dd,alpha_dd, label = 'alpha')
plt.legend()
plt.show()



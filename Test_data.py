# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:41:49 2019

@author: Sybren
"""

import matplotlib.pyplot as plt
import math
import numpy as np

time = np.genfromtxt("matlab/Our-data/time.csv", dtype="float")
pitch_rate = np.genfromtxt("matlab/Our-data/Ahrs1_bPitchRate.csv", dtype="float")
delta_e = np.genfromtxt("matlab/Our-data/delta_e.csv", dtype="float")
alpha = np.genfromtxt("matlab/Our-data/vane_AOA.csv", dtype="float") #body
hp = np.genfromtxt("matlab/Our-data/Dadc1_alt.csv", dtype="float")
pitch = np.genfromtxt("matlab/Our-data/Ahrs1_Pitch.csv", dtype="float")
tat = np.genfromtxt("matlab/Our-data/Dadc1_tat.csv", dtype="float")
tas = np.genfromtxt("matlab/Our-data/Dadc1_tas.csv", dtype="float")


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


#short period 15 sec
for i in range(len(time)):
    if time[i] == (40*60+42):
        begin_s = i
    elif time[i] == (40*60+42+15):
        end_s = i

#shortperiod lists
time_s = time[begin_s:end_s]
pitch_rate_s = pitch_rate[begin_s:end_s]
delta_e_s = delta_e[begin_s:end_s]
alpha_s = alpha[begin_s:end_s]

#Dutch roll without damping
for i in range(len(time)):
    if time[i] == (40*60+42):
        begin_d = i
    elif time[i] == (40*60+42+15):
        end_d = i

#shortperiod lists
time_d = time[begin_d:end_d]
pitch_rate_d = pitch_rate[begin_d:end_]
delta_e_d = delta_e[begin_d:end_d]
alpha_d = alpha[begin_d:end_d]



plt.subplot(121)
plt.plot(time_p,pitch_rate_p, label = 'pitch rate')
plt.plot(time_p,delta_e_p, label = 'delta e')
plt.plot(time_p,alpha_p, label = 'alpha')
plt.legend()

plt.subplot(122)
plt.plot(time_s,pitch_rate_s, label = 'pitch rate')
plt.plot(time_s,delta_e_s, label = 'delta e')
plt.plot(time_s,alpha_s, label = 'alpha')
plt.legend()
plt.show()



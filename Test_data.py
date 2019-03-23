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
roll_rate = np.genfromtxt("matlab/test-data/Ahrs1_bRollRate.csv", dtype="float")
yaw_rate = np.genfromtxt("matlab/test-data/Ahrs1_bYawRate.csv", dtype="float")
delta_e = np.genfromtxt("matlab/test-data/delta_e.csv", dtype="float")
alpha = np.genfromtxt("matlab/test-data/vane_AOA.csv", dtype="float") #body
hp = np.genfromtxt("matlab/test-data/Dadc1_alt.csv", dtype="float")
pitch = np.genfromtxt("matlab/test-data/Ahrs1_Pitch.csv", dtype="float")
roll = np.genfromtxt("matlab/test-data/Ahrs1_Roll.csv", dtype="float")
tat = np.genfromtxt("matlab/test-data/Dadc1_tat.csv", dtype="float")
tas = np.genfromtxt("matlab/test-data/Dadc1_tas.csv", dtype="float")


for i in range(len(time)):
    pitch_rate[i] = np.deg2rad(pitch_rate[i])
    delta_e[i] = np.deg2rad(delta_e[i])
    alpha[i] = np.deg2rad(alpha[i])
    pitch[i] = np.deg2rad(pitch[i])
    

""" Phugoid """
#phugoid
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
tas_p = tas[begin_p:end_p]

plt.figure(1, figsize=(13,5))
plt.subplot(121)
#plt.plot(time_p,pitch_rate_p, label = 'Pitch rate')
#plt.plot(time_p,delta_e_p, label = 'Elevator deflection')
plt.plot(time_p,alpha_p, label = 'Angle of attack')
plt.title("Phugoid")
plt.xlabel("t [sec]")
plt.grid(True)

plt.subplot(122)
plt.plot(time_p,tas_p)
plt.title("Phugoid Velocity")
plt.ylabel("True Airspeed [m/s]")
plt.xlabel("t [sec]")
plt.grid(True)

"""Short Period"""
#short period 10 sec
for i in range(len(time)):
    if time[i] == (40*60+42):
        begin_sp = i
    elif time[i] == (40*60+42+9):
        end_sp = i

#shortperiod lists
time_sp = time[begin_sp:end_sp]
pitch_rate_sp = pitch_rate[begin_sp:end_sp]
delta_e_sp = delta_e[begin_sp:end_sp]
alpha_sp = alpha[begin_sp:end_sp]
tas_sp = tas[begin_sp:end_sp]

plt.figure(2, figsize=(13,5))
plt.subplot(121)
#plt.plot(time_sp,pitch_rate_sp, label = 'Pitch rate')
#plt.plot(time_sp,delta_e_sp, label = 'Elevator deflection')
plt.plot(time_sp,alpha_sp, label = 'Angle of attack')
plt.grid(True)
plt.title("Short Period")
plt.xlabel("t [sec]")

plt.subplot(122)
plt.plot(time_sp,tas_sp)
plt.title("Short Period Velocity")
plt.ylabel("True Airspeed [m/s]")
plt.xlabel("t [sec]")
plt.grid(True)

""" Dutch roll """
#Dutch roll without damping
for i in range(len(time)):
    if time[i] == (45*60+14):
        begin_d = i
    elif time[i] == (45*60+14+20):
        end_d = i

#Dutch roll lists
time_d = time[begin_d:end_d]
yaw_rate_d = yaw_rate[begin_d:end_d]
roll_rate_d = roll_rate[begin_d:end_d]
roll_d = roll[begin_d:end_d-1]
yaw_integration = []
yaw_pos = 0
for i in (range(len(time_d)-1)):
    yaw_pos = yaw_pos + (yaw_rate_d[i]*(time_d[i + 1]-time_d[i]))
    yaw_integration.append(yaw_pos) 

#Dutch roll with damping
for i in range(len(time)):
    if time[i] == (46*60+7):
        begin_dd = i
    elif time[i] == (46*60+7+15):
        end_dd = i

#Dutch roll damping lists
time_dd = time[begin_dd:end_dd]
yaw_rate_dd = yaw_rate[begin_dd:end_dd]
roll_rate_dd = roll_rate[begin_dd:end_dd]

plt.figure(3, figsize=(13,5))
plt.subplot(131)
plt.plot(time_d,roll_rate_d, label = 'Roll rate')
plt.title("Dutch roll, roll rate")
plt.xlabel("t [sec]")
plt.grid(True)

plt.subplot(132)
plt.plot(time_d,yaw_rate_d, label = 'Yaw rate')
plt.title("Dutch roll, yaw rate")
plt.xlabel("t [sec]")
plt.grid(True)

plt.subplot(133)
plt.plot(yaw_integration,roll_d)
plt.title("Dutch roll, yaw vs roll")
plt.xlabel("Relative yaw angle [deg]")
plt.ylabel("Roll angle [deg]")
plt.grid(True)

plt.figure(4, figsize=(13,5))
plt.subplot(121)
plt.plot(time_dd,roll_rate_dd, label = 'Roll rate')
plt.title("Dutch roll damped, roll rate")
plt.xlabel("t [sec]")
plt.grid(True)

plt.subplot(122)
plt.plot(time_dd,yaw_rate_dd, label = 'Yaw rate')
plt.title("Dutch roll damped, yaw rate")
plt.xlabel("t [sec]")
plt.grid(True)


""" Aperiodic roll """
#Aperiodic roll
for i in range(len(time)):
    if time[i] == (39*60+45):
        begin_a = i
    elif time[i] == (39*60+45+14):
        end_a = i

#Aperiodic roll lists
time_a = time[begin_a:end_a]
roll_rate_a = roll_rate[begin_a:end_a]
roll_a = roll[begin_a:end_a]

plt.figure(5, figsize=(13,5))
plt.subplot(121)
plt.plot(time_a,roll_rate_a, label = 'Roll rate [deg/s]')
plt.plot(time_a,roll_a, label = 'Roll angle')
plt.legend()
plt.title("Aperiodic roll")
plt.xlabel("t [sec]")
plt.grid(True)
plt.ylabel("[deg]")

""" Spiral """
#Spiral
for i in range(len(time)):
    if time[i] == (47*60+33):
        begin_s = i
    elif time[i] == (47*60+33+175):
        end_s = i

#Spiral lists
time_s = time[begin_s:end_s]
roll_rate_s = roll_rate[begin_s:end_s]
roll_s = roll[begin_s:end_s]

plt.subplot(122)
plt.plot(time_s,roll_rate_s, label = 'Roll rate [deg/s]')
plt.plot(time_s,roll_s, label = 'Roll angle')
plt.legend()
plt.title("Spiral")
plt.xlabel("t [sec]")
plt.ylabel("[deg]")
plt.grid(True)
plt.show

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:52:21 2019

@author: Max
"""
from scipy.signal import find_peaks
import numpy as np
from Test_data_outputs import *
from scipy.optimize import curve_fit
from Cit_par_Our_data import c, b



def Phugoid(time, pitch, th0):    
    t0 = time[0]
    
    time = time - t0
    pitch=pitch-th0
    time_ext = np.arange(0,300,0.1)
    
    
    peaks, _ = find_peaks(pitch, distance = 25, height=0.0)
    peaks = np.delete(peaks,[0])
    
    x = time[peaks]
    y = pitch[peaks]

    def func(x, a, c):
        return a*np.exp(-c*x)
    
    popt, pcov = curve_fit(func, x, y, p0=(1, 0.1))
    amp = func(time_ext,popt[0],popt[1])
    
    a0 = amp[0]
    a_half = (a0)/2

    for i in range(len(amp)):
        if amp[i]<=a_half:
            t_half = time_ext[i]
            break
      
    sum_period=0
    for i in range(len(x)-1):
        sum_period = sum_period + x[i+1]-x[i]
    period = sum_period/(len(x)-1)
    
    xi = (np.log(1/2))/(t_half)
    eta = (2.*np.pi)/(period)
    print("Phugoid: " , xi,' i', eta)
    plt.subplot(312)
    plt.title("Phugoid")
    plt.plot(time, pitch, label = 'Pitch data', color = 'darkblue')
    plt.plot(time_ext,amp, label = "Amplitude curve", color = 'orange')
    plt.plot(x,y, 'x', label = 'Peaks', color = 'red')
    plt.plot(t_half,a_half, 'o', label = 'Half amplitude point', color = 'green')
    plt.legend()
    plt.xlabel('time(s)')
    plt.ylabel("$\\theta$ (rad)")
    plt.grid()
    plt.show()



mass, hp0, Vt0, alpha0, th0, delta_e0 = Pheugoid_init()
time, pitch_rate, u_s, alpha, pitch, u = Pheugoid()    
Phugoid(time, pitch, th0)
    
    

    
def DR(time, yaw_rate):

    
    t0 = time[0]
    time = time - t0
    
    peaks, _ = find_peaks(yaw_rate, distance = 25, height=0.015)
#    peaks = np.delete(peaks,[0])
    x = time[peaks]
    y = yaw_rate[peaks]

    def func(x, a, c, d):
        return a*np.exp(-c*x)+d
    
    popt, pcov = curve_fit(func, x, y, p0=(1, 0.1, 1))
    amp = func(time,popt[0],popt[1], (popt[2]))
    
    a0 = amp[0]
    a_half = (amp[0]-popt[2])/2
    for i in range(len(amp)):
        if amp[i]<=a_half:
            t_half = time[i]
            break
      
    sum_period=0
    for i in range(len(x)-1):
        sum_period = sum_period + x[i+1]-x[i]
    period = sum_period/(len(x)-1)
    
    xi = (np.log(1/2))/(t_half)
    eta = (2.*np.pi)/(period)
    print("Dutch roll: " , xi,' i', eta)
    
    
    plt.subplot(313)
    plt.title("Dutch roll")
    plt.plot(time,yaw_rate, label = 'Yaw rate data', color = 'darkblue')
    plt.plot(time,amp, label = "Amplitude curve", color = 'orange')
    plt.plot(x,y, 'x', label = 'Peaks', color = 'red')
    plt.plot(t_half,a_half, 'o', label = 'Half amplitude point', color = 'green')
    plt.legend()
    plt.xlabel('time(s)')
    plt.ylabel("r (rad/s)")
    plt.grid()
    plt.show()


mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0 ,roll0, roll_rate0, yaw_rate0= Dutch_roll_init()
time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate = Dutch_roll()  

DR(time, yaw_rate)



    
def SP(time, pitch_rate):

    
    t0 = time[0]
    time = time - t0
    
    peaks, _ = find_peaks(pitch_rate, height=0)

    peaks = np.delete(peaks,[0])
    peaks = np.append(peaks, 64)
    x = time[peaks]
    y = pitch_rate[peaks]

    def func(x, a, c, d):
        return a*np.exp(-c*x)+d
    
    popt, pcov = curve_fit(func, x, y, p0=(1, 0.1, 1))
    amp = func(time,popt[0],popt[1], (popt[2]))
    
    a0 = amp[0]
    a_half = (a0-popt[2])/2
    for i in range(len(amp)):
        if amp[i]<=a_half:
            t_half = time[i]
            break
      
    sum_period=0
    for i in range(len(x)-1):
        sum_period = sum_period + x[i+1]-x[i]
    period = sum_period/(len(x)-1)
    
    xi = (np.log(1/2))/(t_half)
    eta = (2.*np.pi)/(period)
    print("Short period: " , xi,' i', eta)
    
    
    plt.subplot(311)
    plt.title("Short period")
    plt.plot(time,pitch_rate, label = 'Pitch rate data', color = 'darkblue')
    plt.plot(time,amp, label = "Amplitude curve", color = 'orange')
    plt.plot(x,y, 'x', label = 'Peaks', color = 'red')
    plt.plot(t_half,a_half, 'o', label = 'Half amplitude point', color = 'green')
    plt.legend()
    plt.xlabel('time(s)')
    plt.ylabel("q (rad/s)")
    plt.grid()
    plt.show()

mass, hp0, Vt0, alpha0, th0, delta_e0 = Short_period_init()
time, pitch_rate, u_s, alpha, pitch, u = Short_period()

SP(time, pitch_rate)
    



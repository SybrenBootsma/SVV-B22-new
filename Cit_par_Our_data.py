import numpy as np
from Test_data_outputs import *
#Citation 550 - Linear simulation

#symmetric
#mass, hp0, Vt0, alpha0, th0, delta_e0 = Pheugoid_init()
#time, pitch_rate, u_s, alpha, pitch, u = Pheugoid()

mass, hp0, Vt0, alpha0, th0, delta_e0 = Short_period_init()
time, pitch_rate, u_s, alpha, pitch, u = Short_period()
## 
#assymetric
#
#mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0 ,roll0, roll_rate0, yaw_rate0= Spiral_init()
#time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate = Spiral()

#mass, hp0, Vt0, alpha0, th0, delta_r0, delta_a0 ,roll0, roll_rate0, yaw_rate0= Dutch_roll_init()
#time, delta_r, delta_a, beta, roll, roll_rate, yaw_rate = Dutch_roll()



#data lists of state variables


#Stationary flight condition
#values guessed for first itteration
#hp0    =   hp0_p 	     # pressure altitude in the stationary flight condition [m]
#Vt0     =  tas_p        # true airspeed in the stationary flight condition [m/sec]
#alpha0 =  alpha0     # angle of attack in the stationary flight condition [rad]
#th0    =  pitch0       # pitch angle in the stationary flight condition [rad]

#time = time_p

# Aircraft mass
m = mass         # mass [kg]

# aerodynamic properties
#e      = 0.8         # Oswald factor [ ]
#CD0    = 0.04       # Zero lift drag coefficient [ ]

#Updated (ref)
#CLa= np.rad2deg(0.08654461339642183)
#Cma = np.rad2deg(-0.01632838447633989)
#Cmde = np.rad2deg(-0.03406932679756723)
#e = 
#CD0 =

#Updates (own flight data)
CLa= np.rad2deg(0.0798823703555718) #lower
Cma = np.rad2deg(-0.013491768165584162) #lower
Cmde = np.rad2deg(-0.024993703453834035)*0.6 #lower


e =  0.7164777033104905 
CD0 = 0.024915931667482297


# Longitudinal stability
#CLa    = 5.084       # Slope of CL-alpha curve [ ] 
#Cma    = -0.5626       # longitudinal stabilty [ ]
#Cmde   = -1.1642      # elevator effectiveness [ ]
#e      = 0.8         # Oswald factor [ ]
#CD0    = 0.04       # Zero lift drag coefficient [ ]

# Aircraft geometry

S      = 30.00	          # wing area [m^2]
Sh     = 0.2 * S         # stabiliser area [m^2]
Sh_S   = Sh / S	          # [ ]
lh     = 0.71 * 5.968    # tail length [m]
c      = 2.0569	          # mean aerodynamic cord [m]
lh_c   = lh / c	          # [ ]
b      = 15.911	          # wing span [m]
bh     = 5.791	          # stabilser span [m]
A      = b ** 2 / S      # wing aspect ratio [ ]
Ah     = bh ** 2 / Sh    # stabilser aspect ratio [ ]
Vh_V   = 1	          # [ ]
ih     = -2 * np.pi / 180   # stabiliser angle of incidence [rad]
xcg = 0.25 * c

# Constant values concerning atmosphere and gravity

rho0   = 1.2250          # air density at sea level [kg/m^3] 
Lambda = -0.0065         # temperature gradient in ISA [K/m]
Temp0  = 288.15          # temperature at sea level in ISA [K]
R      = 287.05          # specific gas constant [m^2/sec^2K]
g      = 9.81            # [m/sec^2] (gravity constant)


# air density [kg/m^3]  
rho    = rho0 * np.power( ((1+(Lambda * hp0 / Temp0))), (-((g / (Lambda*R)) + 1)))   
W      = m * g            # [N]       (aircraft weight)

# Constant values concerning aircraft inertia

muc    = m / (rho * S * c)
mub    = m / (rho * S * b)
KX2    = 0.019
KZ2    = 0.042
KXZ    = 0.002
KY2    = 1.25 * 1.114

# Aerodynamic constants

Cmac   = 0                      # Moment coefficient about the aerodynamic centre [ ]
CNwa   = CLa                    # Wing normal force slope [ ]
CNha   = 2 * np.pi * Ah / (Ah + 2) # Stabiliser normal force slope [ ]
depsda = 4 / (A + 2)            # Downwash gradient [ ]

# Lift and drag coefficient

CL = 2 * W / (rho * Vt0 ** 2 * S)              # Lift coefficient [ ]
CD = CD0 + (CLa * alpha0) ** 2 / (np.pi * A * e) # Drag coefficient [ ]

# Stabiblity derivatives

CX0    = W * np.sin(th0) / (0.5 * rho * Vt0 ** 2 * S)
CXu    = -0.02792*0.8
CXa    = -0.47966*0.8
CXadot = +0.08330
#CXq    = -0.28170
CXq    = -0.28170#*2
CXde   = -0.03728#*2

CZ0    = -W * np.cos(th0) / (0.5 * rho * Vt0 ** 2 * S)
CZu    = -0.37616#*2
#CZu    = -0.27616
CZa    = -5.74340*0.75
CZadot = -0.00350
CZq    = -5.66290
CZde   = -0.69612

Cm0    = +0.0297 #added from C.2
Cmu    = +0.06990
Cmadot = +0.17800
Cmq    = -8.79415

CYb    = -0.7500 #minor influence
CYbdot =  0     
CYp    = -0.0304 #no influence
CYr    = +0.8495 #no influence
CYda   = -0.0400 #no influence
CYdr   = +0.2300 #minor influence

Clb    = -0.10260*0.75
Clp    = -0.71085*2
Clr    = +0.23760*0.5
Clda   = -0.23088#*0.8
Cldr   = +0.03440

Cnb    =  +0.1348*0.5
Cnbdot =   0     
Cnp    =  -0.0602
Cnr    =  -0.2061
Cnda   =  -0.0120*2
Cndr   =  -0.0939

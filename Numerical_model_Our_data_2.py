from Cit_par_Our_data import *
import control as ctr
import numpy as np
import matplotlib.pyplot as plt



t_start = 0.
t_end = 15.
dt = 0.01

t = np.arange(t_start, t_end + dt,dt)


C1_s = np.array([[-2*muc*(c/(Vt0**2)), 0, 0, 0],
                 [0, (CZadot -2*muc)*(c/Vt0), 0, 0],
                 [0, 0, -(c/Vt0), 0],
                 [0, Cmadot*(c/Vt0), 0, -2*muc*KY2*(c/Vt0)**2]])

C2_s = np.array([[CXu*(1/Vt0), CXa, CZ0, CXq*(c/Vt0)],
                 [CZu*(1/Vt0), CZa, -CX0, (CZq+2*muc)*(c/Vt0)],
                 [0,0,0,(c/Vt0)],
                 [Cmu*(1/Vt0), Cma, 0, Cmq*(c/Vt0)]])

C3_s = np.array([[CXde],
                 [CZde],
                 [0],
                 [Cmde]])


C1_a = np.array([[(CYbdot - 2* mub) *(b/Vt0),0,0,0],
                 [0,-0.5*(b/Vt0),0,0],
                 [0,0,-2*mub*KX2*(b/Vt0)**2, 2*mub*KXZ*(b/Vt0)**2],
                 [Cnbdot*(b/Vt0), 0 , 2*mub*KXZ*(b/Vt0)**2 , -2*mub*KZ2*(b/Vt0)**2]])
C2_a = np.array([[CYb,CL,CYp*(b/(2*Vt0)), (CYr -4*mub)*(b/(2*Vt0))],
                 [0,0,(b/(2*Vt0)),0],
                 [Clb,0,Clp*(b/(2*Vt0)), Clr*(b/(2*Vt0))],
                 [Cnb,0,Cnp*(b/(2*Vt0)), Cnr*(b/(2*Vt0))]])
C3_a = np.array([[CYda,CYdr],
                 [0,0],
                 [Clda,Cldr],
                 [Cnda,Cndr]])

A_s = np.matmul(-np.linalg.inv(C1_s),C2_s)
B_s = np.matmul(-np.linalg.inv(C1_s),C3_s)
C_s = np.array([[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]])
D_s = np.array([[0],
       [0],
       [0],
       [0]])

A_a = np.matmul(-np.linalg.inv(C1_a),C2_a)
B_a = np.matmul(-np.linalg.inv(C1_a),C3_a)
C_a = np.array([[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]])
D_a = np.array([[0,0],
       [0,0],
       [0,0],
       [0,0]])

sys_s = ctr.ss(A_s, B_s, C_s, D_s)
sys_a = ctr.ss(A_a, B_a, C_a, D_a)



def Symmetric_plot():
#    for i in range(len(time)):
#        u_s[i]= u_s[i]/2
    t_s, y_s, xouts = ctr.forced_response(sys_s,time, u_s, X0=0)
    damp_s = ctr.damp(sys_s)
    for i in range(len(time)):
        y_s[0][i]= y_s[0][i] + Vt0
        y_s[1][i]= y_s[1][i] + alpha0
        y_s[2][i]= y_s[2][i] + th0

    plt.subplot(321)
    plt.title("Elevator input")
    plt.plot(time, u_s, color = "darkblue" )
    plt.xlabel("Time (s)")
    plt.ylabel('$\\delta_e$ (rad)')
    plt.grid()


    plt.subplot(323)
    plt.title("Forward speed")
    
    plt.plot(time, u, color = "darkblue"  , label = 'u data')
    plt.plot(time, y_s[0], color = "orange" , label = 'u numerical model')
    plt.xlabel("Time (s)")
    plt.ylabel('$u$ (m/s)')
    plt.grid()
    plt.legend()
    
    plt.subplot(324)
    plt.title("Angle of attack")
    
    plt.plot(time, alpha, color = "darkblue"  , label = 'AoA data')
    plt.plot(time, y_s[1],color = "orange" , label = 'AoA numerical model')
    plt.xlabel("Time (s)")
    plt.ylabel('$\\alpha$ (rad)')
    plt.grid()
    plt.legend()
    
    plt.subplot(325)
    plt.title('Pitch angle')
    
    plt.plot(time, pitch,color = "darkblue" , label = 'Pitch angle  data')
    plt.plot(time, y_s[2],color = "orange" , label = 'Pitch angle numerical model')
    plt.xlabel("Time (s)")
    plt.ylabel("$\\theta$ (rad)")
    plt.grid()
    plt.legend()
    
    plt.subplot(326)
    plt.title("Pitch rate")
    
    plt.plot(time, pitch_rate,color = "darkblue" , label = 'Pitch rate data')
    plt.plot(time, y_s[3],color = "orange" , label = 'Pitch rate numerical model')
    plt.xlabel("Time (s)")
    plt.ylabel('$q$ (rad/s)')
    plt.grid()
    plt.legend()
    plt.show()
    
    
def Asymmetric_plot():
    u_a = []
#    Rudder is wrongly defined, corrected with a minus sign
    for i in range(len(time)):
        delta_r[i]= delta_r[i]
        delta_a[i]= delta_a[i]
        roll[i] = roll[i]-roll0
        roll_rate[i] = roll_rate[i]-roll_rate0
        yaw_rate[i] = yaw_rate[i] - yaw_rate0
        
    u_a.append(delta_a)
    u_a.append(delta_r)
    
    t_a, y_a, xout = ctr.forced_response(sys_a,time, u_a, X0=0.)
    damp_a = ctr.damp(sys_a)
    
    plt.subplot(321)
    plt.title("Aileron input")
    plt.plot(time, delta_a, color = "darkblue")
    plt.xlabel("Time (s)")
    plt.ylabel('$\\delta_a$ (rad)')
    plt.grid()
    
    plt.subplot(322)
    plt.title("Rudder input")
    plt.plot(time, delta_r, color = "darkblue" )
    plt.xlabel("Time (s)")
    plt.ylabel('$\\delta_r$ (rad)')
    plt.grid()
    
    plt.subplot(323)
    plt.title("Side Slip")
    plt.plot(time, y_a[0], color = "orange" ,label = 'Side slip numerical model')
    plt.xlabel("Time (s)")
    plt.ylabel('$\\beta$ (rad)')
    plt.grid()
    plt.legend()
    
    plt.subplot(324)
    plt.title("Roll")
    plt.plot(time, roll, color = "darkblue" ,label = 'Roll data')
    plt.plot(time, y_a[1], color = "orange" ,label = 'Roll numerical model')
    plt.xlabel("Time (s)")
    plt.ylabel('$\\phi$ (rad)')
    plt.grid()
    plt.legend()
    
    plt.subplot(325)
    plt.title("Roll rate")

    plt.plot(time, roll_rate , color = "darkblue" , label = 'Roll rate data')
    plt.plot(time, y_a[2], color = "orange" ,label = 'Roll rate numerical model')
    plt.xlabel("Time (s)")
    plt.ylabel('$p$ (rad/s)')
    plt.grid()
    plt.legend()
    plt.subplot(326)
    
    plt.title("Yaw rate")
    plt.plot(time, yaw_rate,color = "darkblue" , label = 'Yaw rate data')
    plt.plot(time, y_a[3], color = "orange" ,label = 'Yaw rate numerical model')
    plt.xlabel("Time (s)")
    plt.ylabel("$r$ (rad/s)")
    plt.grid()
    plt.legend()
    plt.show()


Asymmetric_plot()



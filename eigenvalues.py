# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:48:44 2019

@author: Hidde Jansen
"""
from Cit_par import *
import numpy as np

#------------------------------------------------------------------------------

# Short period first simplification

A_sp1 = 2.*muc*KY2*(2.*muc-CZadot)
B_sp1 = -2.*muc*KY2*CZa-(2.*muc+CZq)*Cmadot-(2.*muc-CZadot)*Cmq
C_sp1 = CZa*Cmq-(2.*muc+CZq)*Cma

# Short period second simplification

A_sp2 = 4.*muc**2*KY2
B_sp2 = -2.*muc*(KY2*CZa+Cmadot+Cmq)
C_sp2 = CZa*Cmq-2.*muc*Cma

# Short period third simplification

A_sp3 = -2.*muc*KY2
B_sp3 = Cmadot+Cmq
C_sp3 = Cma

#------------------------------------------------------------------------------

# Phugoid coarse approximation

A_ph1 = -4.*muc**2
B_ph1 = 2.*muc*CXu
C_ph1 = -CZu*CZ0

# Phugoid refined approximation

A_ph2 = 2.*muc*(CZa*Cmq-2.*muc*Cma)
B_ph2 = 2.*muc*(CXu*Cma-Cmu*CXa)+Cmq*(CZu*CXa-CXu*CZa)
C_ph2 = CZ0*(Cmu*CZa-CZu*Cma)

#------------------------------------------------------------------------------

# Aperiodic roll

A_ar = 0.
B_ar = -4.*mub*KX2
C_ar = Clp

#------------------------------------------------------------------------------

# Dutch roll first simplification

A_dr1 = 8.*mub**2*KZ2
B_dr1 = -2*mub*(Cnr+2.*KZ2*CYb)
C_dr1 = 4.*mub*Cnb+CYb*Cnr

# Dutch roll second simplification

A_dr2 = -2.*mub*KZ2
B_dr2 = 0.5*Cnr
C_dr2 = -Cnb

#------------------------------------------------------------------------------

# Aperiodic spiral

A_as = 0.
B_as = Clp*(CYb*Cnr+4.*mub*Cnb)-Cnp*(CYb*Clr+4.*mub*Clb)
C_as = -2*CL*(Clb*Cnr-Cnb*Clr)

# -----------------------------------------------------------------------------

# Eigenvalue function for symmetric motions

def eigensym(A, B, C):
    lam_c_1 = (-B+1j*np.sqrt(4.*A*C-B**2))/(2.*A)
    lam_c_2 = (-B-1j*np.sqrt(4.*A*C-B**2))/(2.*A)

    lam_1 = lam_c_1*Vt0/c
    lam_2 = lam_c_2*Vt0/c

    xi_c = np.real(lam_c_1)
    eta_c = np.imag((lam_c_1))

    xi = -xi_c/(np.sqrt((xi_c)**2+(eta_c)**2))
    om_0 = np.sqrt((xi_c)**2+(eta_c)**2)*Vt0/c
    
    print("Eig 1", lam_1)
    print("Eig 2", lam_2)
    print("Damping", xi)
    print("Nat freq", om_0)
    
    return

#------------------------------------------------------------------------------

# Eigenvalue function for assymetric motions

def eigenasym(A, B, C):
    if A == 0.:
        lam_b_1 = -C/B
        
        lam_1 = lam_b_1*Vt0/b
        lam_2 = "NA"
        
    else:
        lam_b_1 = (-B+1j*np.sqrt(4.*A*C-B**2))/(2.*A)
        lam_b_2 = (-B-1j*np.sqrt(4.*A*C-B**2))/(2.*A)
        
        lam_1 = lam_b_1*Vt0/b
        lam_2 = lam_b_2*Vt0/b
        
    xi_b = np.real(lam_b_1)
    eta_b = np.imag((lam_b_1))

    xi = -xi_b/(np.sqrt((xi_b)**2+(eta_b)**2))
    om_0 = np.sqrt((xi_b)**2+(eta_b)**2)*Vt0/b
    
    print("Eig 1", lam_1)
    print("Eig 2", lam_2)
    print("Damping", xi)
    print("Nat freq", om_0)
    
    return(lam_1, lam_2)

##------------------------------------------------------------------------------
#
## Dutch roll and aperiodic roll
#
#A_x = 4.*mub**2*(KX2*KZ2-KXZ**2)
#B_x = -mub*((Clr+Cnp)*KXZ+Cnr*KX2+Clp*KZ2)
#C_x = 2.*mub*(Clb*KXZ+Cnb*KX2)+0.25*(Clp*Cnr-Cnp*Clr)
#D_X = 0.5*(Clb*Cnp-Cnb*Clp)
#
#eigenasym(A_as,B_as,C_as)
#
#eigenasym(A_as, B_as, C_as)
#
#
#eigensym(A_)




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



# -----------------------------------------------------------------------------

# Eigenvalue function

def eigen(A, B, C):
    lam_c_2 = (-B+1j*np.sqrt(4.*A*C-B**2))/(2.*A)
    lam_c_1 = (-B-1j*np.sqrt(4.*A*C-B**2))/(2.*A)

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


eigen(A_ph2, B_ph2, C_ph2)












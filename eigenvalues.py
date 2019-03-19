# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:48:44 2019

@author: Hidde
"""
from Cit_par import *
import numpy as np

#------------------------------------------------------------------------------

# Short period first simplification

A_sp1 = 2.*muc*KY2*(2.*muc-CZadot)
B_sp1 = -2.*muc*KY2*CZa-(2.*muc+CZq)*Cmadot-(2.*muc-CZadot)*Cmq
C_sp1 = CZa*Cmq-(2.*muc+CZq)*Cma

lam_c_sp1 = (-B_sp1+1j*np.sqrt(4.*A_sp1*C_sp1-B_sp1**2))/(2.*A_sp1)
lam_c_sp2 = (-B_sp1-1j*np.sqrt(4.*A_sp1*C_sp1-B_sp1**2))/(2.*A_sp1)

lam_sp1 = lam_c_sp1*Vt0/c
lam_sp2 = lam_c_sp2*Vt0/c

xi_c_sp1 = np.real(lam_c_sp1)
eta_c_sp1 = np.imag((lam_c_sp1))

xi_sp1 = -xi_c_sp1/(np.sqrt((xi_c_sp1)**2+(eta_c_sp1)**2))
om_0_sp1 = np.sqrt((xi_c_sp1)**2+(eta_c_sp1)**2)*Vt0/c
om_n_sp1 = om_0_sp1*np.sqrt(1.-(xi_sp1)**2)

print("Eig 1", lam_sp1)
print("Eig 2", lam_sp2)
print("Damping", xi_sp1)
print("Nat freq", om_n_sp1)

# Short period second simplification

A_sp2 = 4.*muc**2*KY2
B_sp2 = -2.*muc*(KY2*CZa+Cmadot+Cmq)
C_sp2 = CZa*Cmq-2.*muc*Cma

lam_c_sp3 = (-B_sp2+1j*np.sqrt(4.*A_sp2*C_sp2-B_sp2**2))/(2.*A_sp2)
lam_c_sp4 = (-B_sp2-1j*np.sqrt(4.*A_sp2*C_sp2-B_sp2**2))/(2.*A_sp2)

lam_sp3 = lam_c_sp3*Vt0/c
lam_sp4 = lam_c_sp4*Vt0/c

#print(lam_sp3, lam_sp4)

# Short period third simplification

A_sp3 = -2.*muc*KY2
B_sp3 = Cmadot+Cmq
C_sp3 = Cma

lam_c_sp5 = (-B_sp3+1j*np.sqrt(4.*A_sp3*C_sp3-B_sp3**2))/(2.*A_sp3)
lam_c_sp6 = (-B_sp3-1j*np.sqrt(4.*A_sp3*C_sp3-B_sp3**2))/(2.*A_sp3)

lam_sp5 = lam_c_sp5*Vt0/c
lam_sp6 = lam_c_sp6*Vt0/c

#print(lam_sp5, lam_sp6)

#------------------------------------------------------------------------------

# Phugoid coarse approximation

A_ph1 = -4.*muc**2
B_ph1 = 2.*muc*CXu
C_ph1 = -CZu*CZ0

lam_c_ph1 = (-B_ph1+1j*np.sqrt(4.*A_ph1*C_ph1-B_ph1**2))/(2.*A_ph1)
lam_c_ph2 = (-B_ph1-1j*np.sqrt(4.*A_ph1*C_ph1-B_ph1**2))/(2.*A_ph1)

lam_ph1 = lam_c_ph1*Vt0/c
lam_ph2 = lam_c_ph2*Vt0/c

#print(lam_ph1, lam_ph2)

# Phugoid refined approximation

A_ph2 = 2.*muc*(CZa*Cmq-2.*muc*Cma)
B_ph2 = 2.*muc*(CXu*Cma-Cmu*CXa)+Cmq*(CZu*CXa-CXu*CZa)
C_ph2 = CZ0*(Cmu*CZa-CZu*Cma)

lam_c_ph3 = (-B_ph2+1j*np.sqrt(4.*A_ph2*C_ph2-B_ph2**2))/(2.*A_ph2)
lam_c_ph4 = (-B_ph2-1j*np.sqrt(4.*A_ph2*C_ph2-B_ph2**2))/(2.*A_ph2)

lam_ph3 = lam_c_ph3*Vt0/c
lam_ph4 = lam_c_ph4*Vt0/c

#print(lam_ph3, lam_ph4)

















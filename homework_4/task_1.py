### PURPOSE: ASTP 720 (Computational Methods) HW #4
### Task 1 -

#Import Statements

import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

##############################################################################
## Constants
##############################################################################

G = 6.67E-8  #cm^3/g/s^2
K = 1E13 / 2**(5/3) #for white dwarf

#range of critical densities (d_c); P_c is critical pressures
#d_c = np.linspace(10E4, 10E6, 10)
d_c = [1E4]
P_c = [K * i**(5/3) for i in d_c]

# radial slices to solve at
# terminating radius is ~ 3 earth radii
slices = np.linspace(0, 1.92E9, 1000)



##############################################################################
## Hydrostatic Equilibrium Differential Equations
##############################################################################



def equil(y, r):
    press, menc = y
    dens = K * press**(5/3)
    dPdr = -G * menc * dens / r**2
    dMdr = 4 * np.pi * dens * r**2
    dydr = [dPdr, dMdr]
    return(dydr)



for i in P_c:
    y0 = [i, 0]
    sol = odeint(equil, y0, slices)
    print(sol)

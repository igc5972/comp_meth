### PURPOSE: ASTP 720 (Computational Methods) HW #4
### Task 1 -

##############################################################################
## Import Statements
##############################################################################

import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from ode_library import rk4


##############################################################################
## For Pretty Plotting later on
##############################################################################

params = {'font.family':  'serif',
         'legend.fontsize': 'large',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}

plt.rcParams.update(params)



##############################################################################
## Constants
##############################################################################

G = 6.678E-8  #cm^3/g/s^2
c = 3E10 #cm s^-1



##############################################################################
## Hydrostatic Equilibrium Differential Equations
##############################################################################

small = 1E-4 #[cm] for radius or [g] for mass_enclosed

def equil(r, y):
    press, menc = y
    dens = (press / K)**(3/5)
    dMdr = 4 * np.pi * dens * r**2
    dPdr = 0
    if r > small or menc > small:
        dPdr = -G * menc * dens / r**2
    dydr = [dPdr, dMdr]
    return(dydr)

#TOV Equation

def tov(r, y):
    press, menc = y
    dens = (press / K)**(3/5)
    dMdr = 4 * np.pi * dens * r**2
    dPdr = 0
    if r > small or menc > small:
        dPdr = -((G*(dens + press/c**2))/r**2) * (menc + (4*np.pi*r**3*press)/(c**2))*(1-(2*G*menc)/(r*c**2))**(-1)
    dydr = [dPdr, dMdr]
    return(dydr)


##############################################################################
## White Dwarf Code and Plotting
##############################################################################
'''
K = 1E13 / (2**(5/3)) #for white dwarf
d_c = np.linspace(1E4, 1E6, 20) #for white Dwarf
P_c = [K * i**(5/3) for i in d_c]


#terminating radius ~3 solar radii
slices = np.linspace(1E-4, 1.1E9, 100)

masses = []
radii = []
for P in P_c:
    y0 = [P, 0]

    press, m_enc = rk4(equil, y0, slices)

    for m, p in zip(m_enc, press):
        if p < 0.1 * P :

            masses.append(m)
            radii.append(slices[press.tolist().index(p)])
            break

#Plotting


radii_in_earth = [r / 6.37E8 for r in radii]
masses_in_sun = [m / 1.98E33 for m in masses]
plt.scatter(radii_in_earth, masses_in_sun, color = 'k')

plt.xlabel(r'$Radius \ [R_{\oplus}]$')
plt.ylabel(r'$Mass \ [M_{\odot}]$')
plt.title('Mass-Radius Curve for White Dwarf')
plt.savefig('white_dwarf_plt.eps')
plt.show()
'''

##############################################################################
## Neutron Star Code and Plotting
##############################################################################

K = 5.4E9 #for neutron star
d_c = np.linspace(1E14, 1E16, 20) #for neutron star
P_c = [K * i**(5/3) for i in d_c]

#terminating radius 10's of km
slices = np.linspace(1E-4, .5E6, 100)

masses = []
radii = []
for P in P_c:
    y0 = [P, 0]

    press, m_enc = rk4(tov, y0, slices)

    for m, p in zip(m_enc, press):
        if p < 0.1 * P :

            masses.append(m)
            radii.append(slices[press.tolist().index(p)])
            break



#Plotting
radii_in_km = [r / 100000 for r in radii]
masses_in_sun = [m / 1.98E33 for m in masses]
plt.scatter(radii_in_km, masses_in_sun, color = 'k')

plt.xlabel(r'$Radius \ [km]$')
plt.ylabel(r'$Mass \ [M_{\odot}]$')
plt.title('Mass-Radius Curve for Neutron Star')
plt.savefig('neutron_star_plt.eps')
plt.show()



##############################################################################
## Task 3
##############################################################################

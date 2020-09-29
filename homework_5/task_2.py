### PURPOSE: ASTP 720 (Computational Methods) HW #5 Pt. 2

################################################################################
### Import Statements
################################################################################

import numpy as np
from matplotlib import pyplot as plt
import math

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


################################################################################
### Information about Clumps
################################################################################

#central position of clumps
c1x, c1y = 7, 7
c2x, c2y = 8, 2

#radii of clumps
r1 = 3
r2 = 2

#raddi of clumps in units of cm (to match up with units of constant below [cgs])
r1cm = r1 * 3.086E24
r2cm = r2 * 3.086E24

#masses of clumps
mass = 1.988E46 #g = 10E12 solar masses
m1 = 400 * mass
m2 = 255 * mass

#densities of clumps
p1 = m1 / (np.pi * r1cm**2)
p2 = m2 / (np.pi * r2cm**2)

#constant that encapsulates 4 * pi * G (in cgs units)
constant = 8.38E-7

################################################################################
### Setup Grid
################################################################################

x = np.arange(0, 10, 0.1)
y = np.arange(0, 10, 0.1)
X, Y = np.meshgrid(x, y)

rho = np.ones_like(X) #holder for densities everywhere in square
pot = np.ones_like(X)
#enforce boundary conditions given in problem
pot[:][0] = 0
pot[:][-1] = 0
pot[0][:] = 0
pot[-1][:] = 0

#constrain positions of disks
disk1, disk2 = np.zeros_like(X), np.zeros_like(X)
disk1 = (X-c1x)**2+(Y-c1y)**2 <= r1**2
disk2 = (X-c2x)**2+(Y-c2y)**2 <= r2**2

rho[disk1] = p1
rho[disk2] = p2


################################################################################
### Calculate potentials everywhere
################################################################################

pot = np.copy(rho) #initalize it as the same as rho

step = 200
for iter in range(0, 1):
    for i in range(1, len(x)-1):
        for j in range(1, len(y)-1):
            num = pot[i+1][j] + pot[i][j+1] + pot[i-1][j] + pot[i][j-1]
            den = (4*constant*step*step*rho[i][j])
            pot[i][j] = num / den


fig, ax = plt.subplots(figsize = (6, 6))
ax.imshow(pot)
plt.show()
#plt.show()

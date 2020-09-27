### PURPOSE: ASTP 720 (Computational Methods) HW #5 Pt. 2

################################################################################
### Import Statements
################################################################################

import numpy as np
from matplotlib import pyplot as plt
import random

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
### Option 1 for generating clumps
################################################################################

#first clump, centered @ (7, 7)
n1 = 400
angles1 = np.linspace(0, 2*np.pi, n1)
x1, y1 = (7, 7)
r1 = 3
xs1, ys1 = x1 + r1*np.cos(angles1), y1 + r1*np.sin(angles1)

#second clump, centered @ (8, 2)
n2 = 255
angles2 = np.linspace(0, 2*np.pi, n1)
x2, y2 = (8, 2)
r2 = 2
xs2, ys2 = x2 + r2*np.cos(angles2), y2 + r2*np.sin(angles2)


plt.scatter(xs1, ys1, c = 'red', s=5)  # plot points
plt.scatter(xs2, ys2, c = 'blue', s=5)  # plot points
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.title('Option 1')
plt.show()


################################################################################
### Option 2 for generating clumps
################################################################################

#first clump, centered @ (7, 7)
n1 = 400
r1 = 3
x1, y1 = (7, 7)
xs1, ys1 = [], []
for n in range(n1):
    R1 = r1 * np.sqrt(random.random())
    theta1 = random.random() * 2 * np.pi
    xs1.append(x1 + R1 * np.cos(theta1))
    ys1.append(y1 + R1 * np.sin(theta1))

#second clump, centered @ (8, 2)
r2 = 2
x2, y2 = (8, 2)
xs2, ys2 = [], []
for n in range(n1):
    R2 = r2 * np.sqrt(random.random())
    theta2 = random.random() * 2 * np.pi
    xs2.append(x2 + R2 * np.cos(theta2))
    ys2.append(y2 + R2 * np.sin(theta2))


plt.scatter(xs1, ys1, c = 'red', s=5)  # plot points
plt.scatter(xs2, ys2, c = 'blue', s=5)  # plot points
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.title('Option 2')
plt.show()

################################################################################
### Plotting
################################################################################

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (10, 5))

ax1.scatter(xcrds, ycrds)
ax1.set_xlabel('(x (Mpc)')
ax1.set_ylabel('(y (Mpc)')
ax1.set_title('Start (t = 0)')

plt.show()

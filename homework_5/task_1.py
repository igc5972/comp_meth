### PURPOSE: ASTP 720 (Computational Methods) HW #5 Pt. 1

################################################################################
### Import Statements
################################################################################

import numpy as np
from matplotlib import pyplot as plt


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
### Open data of galaxy's initial position
################################################################################

file = 'galaxies0.npy'

array = np.load(file)

xcrds = array[:, 0]
ycrds = array[: ,1]




################################################################################
### Plotting
################################################################################

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (10, 5))

ax1.scatter(xcrds, ycrds)
ax1.set_xlabel('(x (Mpc)')
ax1.set_ylabel('(y (Mpc)')
ax1.set_title('Start (t = 0)')

plt.show()

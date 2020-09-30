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

#xcrds = array[:, 0] #for testing
#ycrds = array[: ,1]


################################################################################
### Recursively break sections into 4 cells until each galaxy is alone in cell
################################################################################

class Divide:


    def __init__(self, points, ll, ur, amt):
        self.amt = amt

        self.cells = []

        self.ll = ll
        self.ur = ur

        xmin, ymin = self.ll[0], self.ll[1]
        xmax, ymax = self.ur[0], self.ur[1]

        xmid, ymid = (xmin + xmax)/2, (ymin + ymax)/2


        #minimum number of points in a cell constrant
        if self.amt == 1:
            return

        if self.amt > 1:

            #get the points in each potential sub-cell
            nw_points = points[(points[:, 0] < xmid) & (points[:, 1] > ymid)]
            ne_points = points[(points[:, 0] > xmid) & (points[:, 1] > ymid)]
            se_points = points[(points[:, 0] > xmid) & (points[:, 1] < ymid)]
            sw_points = points[(points[:, 0] < xmid) & (points[:, 1] < ymid)]


            #if there are more than 1 points in that sub-cell, recursively divide
            if len(nw_points) > 0:
                self.cells.append(Divide(nw_points, [xmin, ymid], [xmid, ymax], \
                                  len(nw_points)))

            if len(ne_points) > 0:
                self.cells.append(Divide(ne_points, [xmid, ymid], [xmax, ymax], \
                                  len(ne_points)))

            if len(sw_points) > 0:
                self.cells.append(Divide(sw_points, [xmin, ymin], [xmid, ymid], \
                                  len(sw_points)))

            if len(se_points) > 0:
                self.cells.append(Divide(se_points, [xmid, ymin], [xmax, ymid], \
                                  len(se_points)))


    def draw(self, ax):
        if self.amt == 1:
            print('cat')
            ax.plot([self.ll[0], self.ur[0], self.ur[0], self.ll[0], self.ll[0]], \
                    [self.ll[1], self.ll[1], self.ur[1], self.ur[1], self.ll[1]], \
                    color = 'red', zorder = 100)
        for cell in self.cells:
            cell.draw(ax)

Celled = Divide(array, [0, 0], [10, 10], len(array))

################################################################################
### Plotting
################################################################################

fig, ax = plt.subplots(1, 1, figsize  = (7, 7))

ax.scatter(array[:, 0], array[:, 1], s = 3, color = 'k')
Celled.draw(ax)
fig.show()

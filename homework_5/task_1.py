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


array *= 3.086E22

#xcrds = array[:, 0] #for testing
#ycrds = array[: ,1]



################################################################################
### Helper Functions
################################################################################

#Get the position (coordinates) of a galaxy
def position(xmin, xmax, ymin, ymax, points):
    '''
    Accepts:
    points -- array of points to plot
    xmin -- array of values of lower lef corner y-position of cells
    ymin -- array of values of lower lef corner y-position of cells
    xmax -- array of values of upper right corner x-position of cells
    ymax -- array of values of upper right corner y-position of cells

    Returns:
    point in points matching the galaxy in that cell bound by xmin, xmax, etc.
    '''

    position = None
    for p in points:
        if xmin < p[0] < xmax and ymin < p[1] < ymax:
            position = p
    return(position)


#Determine distance between two points
def distance(pos1, pos2):
    return(((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5)


def points_in_cell(xmin, xmax, ymin, ymax, points):
    '''
    Accepts:
    points -- array of points to plot
    xmin -- array of values of lower lef corner y-position of cells
    ymin -- array of values of lower lef corner y-position of cells
    xmax -- array of values of upper right corner x-position of cells
    ymax -- array of values of upper right corner y-position of cells

    Returns:
    positions of points within a parent cell
    '''

    po = []
    for p in points:
        if xmin < p[0] < xmax and ymin < p[1] < ymax:
            po.append(p)
    return(po)


################################################################################
### Recursively break sections into 4 cells until each galaxy is alone in cell
################################################################################

#will hold: xmin, xmax, ymin, ymax of base case cells
baseList = [[], [], [], []]

#will hold: xmin, xmax, ymin, ymax, depth, amt of cells (all cells)
treeList = [[], [], [], [], [], []]


def Tree(points, ll = [0,0], ur=[10*3.086E22,10*3.086E22], amt=655):

    #make lists callable outside of function
    global baseList
    global treeList

    size = ur[0] - ll[0]                       #size of cell
    xmin, ymin = ll[0],  ll[1]                 #lower-left x and y values
    xmax, ymax = ur[0], ur[1]                  #upper right x and y values
    xmid, ymid = (xmin+xmax)/2, (ymin+ymax)/2  #x, y midpoint of cell

    cells = []

    depth = int(10*3.086E22 / size) #how many leaves deep we are


    #need to recursively recall function in this case
    if amt > 1:

        treeList[0].append(xmin)
        treeList[1].append(xmax)
        treeList[2].append(ymin)
        treeList[3].append(ymax)
        treeList[4].append(depth)
        treeList[5].append(amt)


        #points in four cardinal sub-cells
        nw_points = points[(points[:, 0] < xmid) & (points[:, 1] > ymid)]
        ne_points = points[(points[:, 0] > xmid) & (points[:, 1] > ymid)]
        se_points = points[(points[:, 0] > xmid) & (points[:, 1] < ymid)]
        sw_points = points[(points[:, 0] < xmid) & (points[:, 1] < ymid)]

        if len(nw_points) > 0:
            cells.append(Tree(nw_points, [xmin, ymid], [xmid, ymax], \
                              len(nw_points)))

        if len(ne_points) > 0:
            cells.append(Tree(ne_points, [xmid, ymid], [xmax, ymax], \
                              len(ne_points)))

        if len(sw_points) > 0:
            cells.append(Tree(sw_points, [xmin, ymin], [xmid, ymid], \
                              len(sw_points)))

        if len(se_points) > 0:
            cells.append(Tree(se_points, [xmid, ymin], [xmax, ymid], \
                              len(se_points)))


    #base case, fill in list initialized above
    if amt == 1:

        treeList[0].append(xmin)
        treeList[1].append(xmax)
        treeList[2].append(ymin)
        treeList[3].append(ymax)
        treeList[4].append(depth)
        treeList[5].append(amt)

        baseList[0].append(xmin)
        baseList[1].append(xmax)
        baseList[2].append(ymin)
        baseList[3].append(ymax)

        return


################################################################################
### Determine forces on a particle
################################################################################

def Forces(array, txmin, txmax, tymin, tymax, theta):
    accels = []

    for p in array:

        #intialize x,y accel. on p
        #will be added to based on contribution of each particle (close) / cell (far)
        p_accel_x = 0
        p_accel_y = 0

        #go through each cell, including parent cells and leaves
        for cellxi, cellxf, cellyi, cellyf in zip(txmin, txmax, tymin, tymax):

            #get the points inside this cell
            pts_in_cell = points_in_cell(cellxi, cellxf, cellyi, cellyf, array)

            #amt of points inside the cell
            amt = len(pts_in_cell)

            total_mass = massof1 * amt

            #get the COM of each cell
            x_com = sum([massof1 * p[0] for p in pts_in_cell]) / total_mass
            y_com = sum([massof1 * p[1] for p in pts_in_cell]) / total_mass
            com = [x_com, y_com]

            #size of current cell
            cell_size = cellxf - cellxi

            #distance from current point to current cell
            dist = distance(p, com)

            #case where p == point in leaf making up COM
            if cell_size / dist < 1E-5:
                break

            #Case for summing individual forces
            elif cell_size / dist > theta:
                for i in pts_in_cell:

                    #distance between p and individual point (i) in cell
                    d = distance(p, i)

                    #do not look at case of where p is point being considered
                    if d > 1E-5:

                        #calculate components and vector form of acceleration
                        #on p due to i
                        p_accel_x += G * massof1 * (i[0] - p[0]) / d**3
                        p_accel_y += G * massof1 * (i[1] - p[1]) / d**3



            #Case for using COM of cluster
            elif cell_size / dist < theta:

                #distance between p and COM of cell
                d = distance(p, com)

                if d > 1E-5:

                    #calculate components and vector form of acceleration
                    #on p due to COM of current cell
                    p_accel_x += G * massof1 * (com[0] - p[0]) / d**3
                    p_accel_y += G * massof1 * (com[1] - p[1]) / d**3

        #append x,y accels. for this point to master list for all points
        accels.append([p_accel_x, p_accel_y])
        return(accels)


################################################################################
### Run the simulation
################################################################################

#constants
theta = 1
massof1 = 1E12 * 1.989E30    # mass of a single galaxy (point) in [kg]
G = 1E9                     # [m^3 kg^-1 s^-2]


#build the tree
Tree(array)

#info of all cells in tree (parents and leaves)
txmin, txmax, tymin, tymax, tdepth, tamt = treeList

#info of only leaf cells
bxmin, bxmax, bymin, bymax = baseList

#calculate accel. components for each particle
accels = Forces(array, txmin, txmax, tymin, tymax, theta = theta)



################################################################################
### Function to draw current state of galaxies in grid with cells overlaid
################################################################################

def draw(ax, array, xmin, xmax, ymin, ymax):
    '''
    Accepts:
    points -- array of points to plot
    xmin -- array of values of lower lef corner y-position of cells
    ymin -- array of values of lower lef corner y-position of cells
    xmax -- array of values of upper right corner x-position of cells
    ymax -- array of values of upper right corner y-position of cells

    What it does:
    plots the points and draws the cells around them found in tree
    '''

    #plot the actual galaxy points
    ax.scatter(array[:, 0], array[:, 1], s = 7, color = 'k')

    #plot the boundaries of the cells
    for xi, yi, xf, yf in zip(xmin, ymin, xmax, ymax):
        ax.plot([xi, xf, xf, xi, xi], [yi, yi, yf, yf, yi], color = 'red')

    plt.show()

fig, ax = plt.subplots(figsize = (6, 6))
draw(ax, array, bxmin, bxmax, bymin, bymax)

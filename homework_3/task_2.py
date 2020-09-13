### PURPOSE: ASTP 720 (Computational Methods) HW #3
### Task 2 -

import numpy as np #for exp

###############################################################################
#Read in data from table and set constants
###############################################################################

ls, us, As = np.loadtxt('A_coefficients.dat', delimiter = ',', \
                     skiprows = 1, unpack = True)


N = 1 #units = cm^{-3}
freq = 1.5E9 #Hz
c = 3E8 #m/s
h = 6.62E-34 #m^2 kg / s
freq_0 = 1.24E9 #Hz
k = 1.38E-23 #J/K
T = 100 #K


###############################################################################
#Generate B_ul and B_lu values from A_ul values
###############################################################################

aul_values  = []
bulJ_values = []
bluJ_values = []


for u, l, A in zip(us, ls, As):

    constant = 2 * h * freq**3 / c**2

    J = (2 * h * freq_0**2 / c**2) * (1 / np.exp(h*freq_0/(k*T)) -1 )

    g_l = 2*l**2
    g_u = 2*u**2

    bul = constant * A
    blu = bul * g_u / g_l

    bulJ = bul*J
    bluJ = blu*J

    aul_values.append(A)
    bulJ_values.append(bulJ)
    bluJ_values.append(bluJ)


###############################################################################
#Populate Matrix
###############################################################################

matrix = np.zeros((3, 3))

matrix[0][0] = bluJ_values[0] + bluJ_values[1]
matrix[0][1] = - (aul_values[0] + bulJ_values[0])
matrix[0][2] = - (aul_values[1] + bulJ_values[1])
matrix[1][0] = - (bluJ_values[0])
matrix[1][1] = (bulJ_values[0] + aul_values[0] + bulJ_values[2])
matrix[1][2] = - (bulJ_values[2] + aul_values[2])
matrix[2][0] = - (bluJ_values[1])
matrix[2][1] = - (bluJ_values[2])
matrix[2][2] = (bulJ_values[1] + aul_values[1] + bulJ_values[2] + aul_values[2])


###############################################################################
#System of Equations to solve
###############################################################################

matrix = matrix
n = np.zeros((3,1))
s = np.zeros((3,1))


###############################################################################
#Plot number densities as as function of temperature
###############################################################################

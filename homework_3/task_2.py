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
bul_values = []
blu_values = []


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
    bul_values.append(bulJ)
    blu_values.append(bluJ)

###############################################################################
# Setup system of Equations to solve in matrix form
###############################################################################


def value(list, l, u):
    '''
    Parameters:
    list -- list of coefficients (aul_values/bul_values/blu_values)
    l    -- index of lower term
    u    -- index of upper term

    Returns:
    value --
    '''
    return [pair[2] for pair in zip(ls, us, list) if pair[0] == l and pair[1] ==u][0]


matrix = np.zeros((9, 9))

for r in range(9):
    for c in range(9):

        if r == 0 and c == 0:
            matrix[r][c] = value(blu_values, 1, 2) + value(blu_values, 1, 3)

        #not working because cases like
        if r < c:
            matrix[r][c] = -(value(bul_values, r, c) + values(aul_values, r, c))
'''
        elif r > c:
            matrix[r][c] = -(value(blu_values, c, r))

        elif r == c:
            sum = 0

            for j in range(0, 9 -1):
                sum += value(aul_values, r, j)
                sum += value(bul_values, r, j)
                sum += value(blu_values, r, j)

            matrix[r][c] = sum



'''
print(matrix)
###############################################################################
#Plot number densities as as function of temperature
###############################################################################

### PURPOSE: ASTP 720 (Computational Methods) HW #3 Pt. 3


import numpy as np
import  copy
from matplotlib import pyplot as plt


###############################################################################
# Euler's Method
###############################################################################

def euler(function, guess, times):

    '''
    Input:

    f -- function
    guess - initial guess
    t -- list of times to solve at

    Returns:

    y --
    '''

    y = np.zeros(len(t)) #initialize list to hold solutions
    y[0] = guess

    for i in range(0, len(t) - 1):
        step = t[i+1] - t[i]
        y[i+1] = y[i] + step * f(t[i], y[i])

    return(y)



###############################################################################
# Heun's Method
###############################################################################

def heuns(function, guess, times):

    '''
    Input:

    f -- function
    guess - initial guess
    t -- list of times to solve at

    Returns:

    y --
    '''

    y = np.zeros(len(t)) #initialize list to hold solutions
    y[0] = guess

    for i in range(0, len(t) - 1):
        step = t[i+1] - t[i]
        y_tilde = y[i] + step * f(t[i], y[i])
        y[i+1] = y[i] + 0.5 * step * (f(t[i], y[i]) + f(t[i+1], y_tilde))

    return(y)


###############################################################################
# Explicit RK45
###############################################################################

def rk4(function, guess, times):

    '''
    Input:

    f -- function
    guess - initial guess
    t -- list of times to solve at

    Returns:

    y --
    '''

    y = np.zeros(len(t)) #initialize list to hold solutions
    y[0] = guess

    for i in range(0, len(t) - 1):

        step = t[i+1] - t[i]

        k1 = step * f(t[i], y[i])
        k2 = step * f(t[i] + step/2, y[i] + k1/2)
        k3 = step * f(t[i] + step/2, y[i] + k2/2)
        k4 = step * f(t[i] + step, y[i] + k3)

        y[i+1] = y[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

    return(y)

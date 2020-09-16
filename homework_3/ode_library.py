### PURPOSE: ASTP 720 (Computational Methods) HW #3 Pt. 3


import numpy as np
import  copy
from matplotlib import pyplot as plt


###############################################################################
# Euler's Method
###############################################################################

def euler(dydt, guess, t, dt = False):

    y1 = np.zeros(len(t)) #initialize list to hold solutions
    y1[0] = guess[0]

    for i in range(0, len(times) - 1):
        step = None
        if dt == True:
            step = dt
        else:
            step = t[i+1] - t[i]

        y1[i+1] = y1[i] + step * dydt(t[i], y1[i])

    return(y1)




###############################################################################
# Heun's Method
###############################################################################

def heuns(dydt, guess, times):

    y = np.zeros(len(t)) #initialize list to hold solutions
    y[0] = guess

    for i in range(0, len(times) - 1):
        step = times[i+1] - times[i]
        y_tilde = y[i] + step * f(times[i], y[i])
        y[i+1] = y[i] + 0.5 * step * (dydt(times[i], y[i]) + dydt(times[i+1], y_tilde))

    return(y)


###############################################################################
# Explicit RK45
###############################################################################

def rk4(dydt, guess, times):

    guesses = []

    step = times[1] - times[0]

    for t in range(0, len(times) - 1):

        step = times[i+1] - times[i]

        k1 = step * dydt(times[t], y[t])
        k2 = step * dydt(times[t] + step/2, y[t] + k1/2)
        k3 = step * dydt(times[t] + step/2, y[t] + k2/2)
        k4 = step * dydt(times[t] + step, y[t] + k3)

        y[t+1] = y[t] + (k1 + 2*k2 * 2*k3 + k4)/6

    return(y)

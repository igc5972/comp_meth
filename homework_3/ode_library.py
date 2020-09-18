### PURPOSE: ASTP 720 (Computational Methods) HW #3 Pt. 3


import numpy as np
import  copy
from matplotlib import pyplot as plt


###############################################################################
# Euler's Method
###############################################################################

def euler(dydt, guess, t, dt = False):

    '''
    Parameters:
    dydt -- function of d/dt(y1) or d/dt(y1, y2) that should return a list (array)
            for 2 variable or a single value for 1 variable case
    guess -- initial guess(es), should be in list form
    t -- list of times of which to evaluate at
    dt -- False if using spacing btwn points, number specified otherwise

    Returns:
    y1, (y2) -- will return None for y2 if only one variable
    '''

    y1 = np.zeros(len(t)) #initialize list to hold solutions
    y1[0] = guess[0]

    y2 = None
    if len(guess) > 1: #2 variable case
        y2 = np.zeros(len(t))
        y2[0] = guess[1]


    for i in range(0, len(t) - 1):
        step = None
        if dt != False:
            step = dt
        else:
            step = t[i+1] - t[i]

        if y2 is not None: #2 variable case
            y1[i+1] = y1[i] + step * (dydt(t[i], [y1[i], y2[i]]))[0]
            y2[i+1] = y2[i] + step * (dydt(t[i], [y1[i], y2[i]]))[1]


        elif y2 is None: #1 variable case
            y1[i+1] = y1[i] + step * (dydt(t[i], y1[i]))

    return(y1, y2)


###############################################################################
# Heun's Method
###############################################################################

def heuns(dydt, guess, t, dt = False):

    '''
    Parameters:
    dydt -- function of d/dt(y1) or d/dt(y1, y2) that should return a list (array)
            for 2 variable or a single value for 1 variable case
    guess -- initial guess(es), should be in list form
    t -- list of times of which to evaluate at
    dt -- False if using spacing btwn points, number specified otherwise

    Returns:
    y1, (y2) -- will return None for y2 if only one variable
    '''

    y1 = np.zeros(len(t)) #initialize list to hold solutions
    y1[0] = guess[0]

    y2 = None
    if len(guess) > 1: #2 variable case
        y2 = np.zeros(len(t))
        y2[0] = guess[1]


    for i in range(0, len(t) - 1):
        step = None
        if dt != False:
            step = dt
        else:
            step = t[i+1] - t[i]

        if y2 is not None: #2 variable case
            y1tilde = y1[i] + step * dydt(t[i], [y1[i], y2[i]])[0]
            y2tilde = y2[i] + step * dydt(t[i], [y1[i], y2[i]])[1]

            y1[i+1] = y1[i] + 0.5 * step * dydt(t[i], [y1[i], y2[i]])[0] \
             + dydt(t[i], [y1tilde, y2tilde])[0]
            y2[i+1] = y2[i] + 0.5 * step * dydt(t[i], [y1[i], y2[i]])[1] \
             + dydt(t[i], [y1tilde, y2tilde])[1]


        elif y2 is None:
            ytilde = y1[i] + step * dydt(t[i], y1[i])
            y1[i+1] = y1[i] + 0.5 * step * dydt(t[i], y1[i]) + dydt(t[i], ytilde)


    return(y1, y2)


###############################################################################
# Explicit RK45
###############################################################################

def rk4(dydt, guess, t, dt = False):

    '''
    Parameters:
    dydt -- function of d/dt(y1) or d/dt(y1, y2) that should return a list (array)
            for 2 variable or a single value for 1 variable case
    guess -- initial guess(es), should be in list form
    t -- list of times of which to evaluate at
    dt -- False if using spacing btwn points, number specified otherwise

    Returns:
    y1, (y2) -- will return None for y2 if only one variable
    '''

    y1 = np.zeros(len(t)) #initialize list to hold solutions
    y1[0] = guess[0]

    y2 = None
    if len(guess) > 1: #2 variable case
        y2 = np.zeros(len(t))
        y2[0] = guess[1]

    for i in range(0, len(t) - 1):
        step = None
        if dt != False:
            step = dt
        else:
            step = t[i+1] - t[i]


        if y2 is not None: #2 variable case

            k11 = step * dydt(t[i], [y1[i], y2[i]])[0]
            k12 = step * dydt(t[i], [y1[i], y2[i]])[1]

            k21 = step * dydt(t[i] + step/2, [y1[i] + k11/2, y2[i] + k12/2])[0]
            k22 = step * dydt(t[i] + step/2, [y1[i] + k11/2, y2[i] + k12/2])[1]

            k31 = step * dydt(t[i] + step/2, [y1[i] + k21/2, y2[i] + k22/2])[0]
            k32 = step * dydt(t[i] + step/2, [y1[i] + k21/2, y2[i] + k22/2])[1]

            k41 = step * dydt(t[i] + step, [y1[i] + k31, y2[i] + k32])[0]
            k42 = step * dydt(t[i] + step, [y1[i] + k31, y2[i] + k32])[1]

            y1[i+1] = y1[i] + (k11 + 2*k21 + 2*k31 + k41)/6
            y2[i+1] = y2[i] + (k12 + 2*k22 + 2*k32 + k42)/6


        elif y2 is None: #1 variable case

            k1 = step * dydt(t[i], y1[i])
            k2 = step * dydt(t[i] + step/2, y1[i] + k1/2)
            k3 = step * dydt(t[i] + step/2, y1[i] + k2/2)
            k4 = step * dydt(t[i] + step, y1[i] + k3)

            y1[i+1] = y1[i] + (k1 + 2*k2 + 2*k3 + k4)/6

    return(y1, y2)

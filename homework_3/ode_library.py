### PURPOSE: ASTP 720 (Computational Methods) HW #3 Pt. 3


import numpy as np
import  copy
from matplotlib import pyplot as plt


###############################################################################
# Euler's Method
###############################################################################

def euler(function, guess, times, dt = False):

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

    for i in range(0, len(times) - 1):
        step = None

        if dt == True:
            step = dt
        else:
            step = t[i+1] - t[i]

        y[i+1] = y[i] + step * function(t[i], y[i])

    return(y)


def euler(times, guess):

    var1 = np.zeros(len(times))
    var1[0] = guess[0]

    #cases of two variables
    var2 = None
    if len(guess) > 1:
        var2 = np.zeros(len(times))
        var2[0] = guess[1]

    for t in range(0, len(times) - 1):
        step = times[t+1] - times[t]
        var1[t+1] = var1[t] + step * f(times[t], var1[t])
        if type(var2) != 'NoneType': #if second variable
            var2[t+1] = var2[t] + step * f(times[t], var2[t])

    return(var1, var2)


times = np.arange(0, 40, 0.5)
a, b = euler(times, np.array([0.5, 0]))




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

    var1 = []
    var2 = []

    step = times[1] - times[0]
    for t in times:

        var1.append(guess[0])

        if len(guess) > 1:
            var2.append(guess[1])

        k1 = step*f(guess, t)
        k2 = step*f(guess+k1/2.0, t+step/2.0)
        k3 = step*f(guess+k2/2.0, t+step/2.0)
        k4 = step*f(guess+k3, t+step)

        #append new values of r (contains theta and omega) to the "r" array
        guess = float(guess)
        guess += float((k1+2.0*k2+2.0*k3+k4)/6.0)

    return var1, var2


t = np.linspace(0,2,21)
y0 = np.array([1])
f = lambda y,t: y
y = rk4(f,y0,t)
y_true = np.exp(t)
plt.plot(t,y,'b.-',t,y_true,'r-')
plt.legend(['Euler','True'])
plt.axis([0,2,0,9])
plt.grid(True)
plt.title("Solution of $y'=y , y(0)=1$")
plt.show()

### PURPOSE: ASTP 720 (Computational Methods) HW #3
### Task 4 -

#Import Statements

import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from ode_library import euler, heuns, rk4

###############################################################################
#Setup for damped pendulum problem
###############################################################################
# (setup from scipy documentation)

def pendulum(y, t, b=0.25, c=5.0):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

#pendulum starts nearly vertical (theta argument) and at rest (omega argument)
y0 = [np.pi - 0.1, 0.0]


#generate time span to look at solutions for
t = np.linspace(0, 10, 101)



###############################################################################
#Solve with Scipy ODE solver
###############################################################################

sol = odeint(pendulum, y0, t, args = (b, c))


###############################################################################
#Solve with MY ODE solver
###############################################################################

me = rk4(pendulum, y0, t)


###############################################################################
#Plotting
###############################################################################

plt.plot(t, sol[:, 0], 'b.', label = 'Theta (scipy)')
plt.plot(t, sol[:, 1], 'r.', label = 'Omega (scipy)')


plt.plot(t, me[:, 0], 'b', label = 'Theta (mine)')
plt.plot(t, me[:, 1], 'r', label = 'Omega (mine)')


plt.xlabel('Time')

plt.legend()
plt.show()

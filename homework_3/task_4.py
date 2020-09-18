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

#pendulum starts nearly vertical (theta argument) and at rest (omega argument)
y0 = [np.pi - 0.1, 0.0]

#generate time span to look at solutions for
t = np.linspace(0, 10, 101)



###############################################################################
#Solve with Scipy ODE solver
###############################################################################

def pendulum(y, t, b=0.25, c=5.0):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

sol = odeint(pendulum, y0, t)


###############################################################################
#Solve with MY ODE solver
###############################################################################

def pendulum2(t, y, b=0.25, c=5.0): #my variables are swapped
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

t_euler, o_euler = euler(pendulum2, y0, t, dt = 0.1)
t_heuns, o_heuns = heuns(pendulum2, y0, t)
t_rk4, o_rk4 = rk4(pendulum2, y0, t)


###############################################################################
#Plotting
###############################################################################

# Plotting Parameters for pretty plots

params = {'font.family':  'serif',
         'legend.fontsize': 'large',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}

plt.rcParams.update(params)


fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, \
                        sharex=True, sharey=True, figsize = (10, 4))


l1, l2 = None, None
for ax in [ax1, ax2, ax3]:
    l1 = ax.plot(t, sol[:, 0], 'b.')[0]
    l2 = ax.plot(t, sol[:, 1], 'r.')[0]
    ax.set_xlabel('Time')

ax1.set_title('Euler Method')
l3 = ax1.plot(t, t_euler, 'b')[0]
l4 = ax1.plot(t, o_euler, 'r')[0]

ax2.set_title('Heuns Method')
ax2.plot(t, t_heuns, 'b')
ax2.plot(t, o_heuns, 'r')

ax3.set_title('RK4 Method')
ax3.plot(t, t_rk4, 'b')
ax3.plot(t, o_rk4, 'r')

labels = ['Theta (scipy)', 'Omega (scipy)', 'Theta (mine)', 'Omega (mine)']
fig.legend([l1, l2, l3, l4],     # The line objects
           labels=labels,   # The labels for each line
           loc="center right",   # Position of legend
           borderaxespad=0.1,    # Small spacing around legend box
           )

plt.subplots_adjust(right=0.85)

plt.show()

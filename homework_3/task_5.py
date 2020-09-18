### PURPOSE: ASTP 720 (Computational Methods) HW #3
### Task 4 -

#Import Statements

import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from ode_library import euler, heuns, rk4


###############################################################################
#Solve STIFF Eq. with MY ODE solver
###############################################################################


l = 12

def stiff(t, y, l = 12): #my variables are swapped
    dydt = - l * (y - np.cos(t))
    return dydt

def sol(t, l = 12):
    y = (l**2 / (1+l**2))*np.exp(-l * t)  \
      + (l / (1+l**2))*np.sin(t) \
      + (l**2 / (1+l**2))*np.cos(t)
    return(y)

y0 = [0]

times = np.linspace(1, 20, 201)

ysol_euler, none = euler(stiff, y0, times)
ysol_heuns, none = heuns(stiff, y0, times, dt = 0.08)
ysol_rk4, none = rk4(stiff, y0, times)


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


l1 = None
for ax in [ax1, ax2, ax3]:
    l1 = ax.plot(times, sol(times), 'b.', zorder = 0)[0]
    ax.set_xlabel('t')
    ax.set_ylim(-1, 1)
ax1.set_ylabel('y(t)')

ax1.set_title('Euler Method')
l2 = ax1.plot(times, ysol_euler, 'r', zorder = 10000)[0]

ax2.set_title('Heuns Method')
ax2.plot(times, ysol_heuns, 'r', zorder = 10000)

ax3.set_title('RK4 Method')
ax3.plot(times, ysol_rk4, 'r', zorder = 10000)


labels = ['Exact Sol.', 'My Sol.']
fig.legend([l1, l2],     # The line objects
           labels=labels,   # The labels for each line
           loc="center right",   # Position of legend
           borderaxespad=0.1,    # Small spacing around legend box
           )

plt.subplots_adjust(right=0.85)



plt.show()

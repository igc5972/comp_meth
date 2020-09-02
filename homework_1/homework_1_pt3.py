### PURPOSE: ASTP 720 (Computational Methods) HW #1 Pt. 3
### Solve lens equation  for values of x-prime for Gaussian lens
### [Isabella Cox, Aug. 2020]

# Import Statements
from matplotlib import pyplot as plt
import numpy as np
from root_library import bisection
import math ##for pi
from decimal import Decimal ##for formatting numbers for printing


# Setup for plotting later
params = {'font.family':  'serif',
         'legend.fontsize': 'small',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'medium',
         'ytick.labelsize':'medium'}

plt.rcParams.update(params)



### TASK 3: Gaussian Lens

# Lens Parameters
factor = 0.016747 #numerically calcuated based on values of constants
a = 1.496E13
D = 3.086E21

#xprime = np.linspace(0, 2, 10)
xprime = [0, 1, 2]
xprime = [x * 1.496E13 for x in xprime]  #convert AU to cm


xplain = [] #to hold the x(unprimed) values

for p in xprime:
    func = lambda x: x * (1 + factor*math.exp(-x/a)**2) - p #lens eq.

    out, no_iter = bisection(func, 0.5*p, 2*p)
    xplain.append(out)

print([x/a for x in xplain])
print([p/a for p in xprime])

for i in [x/a for x in xprime]:
    print(i)

# Ray tracing plotting for Task 3

idx = 1

xp = (xprime[idx]/a)

xplain1 = [xplain[idx], 1]
xplain2 = [xplain[idx], 0]

xprime1 = [xplain[idx], 0]
xprime2 = [xprime[idx], -1]


xxvalues = [xplain1[0], xplain2[0]]
yxvalues = [xplain1[1], xplain2[1]]

xpvalues = [xprime1[0], xprime2[0]]
ypvalues = [xprime1[1], xprime2[1]]

plt.axhline(0, label = 'lens plane')
plt.plot(xxvalues, yxvalues, 'k', label = 'x [cm]')
plt.plot(xpvalues, ypvalues, 'r', label = 'x\' [cm]')

plt.yticks([])

plt.title('Ray Tracing Diagram for Gaussian Lens: x\' = ' + str(xp) + ' AU')
plt.legend()
plt.savefig('big_view_ray'+str(idx)+'.eps')

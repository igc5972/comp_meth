### PURPOSE: ASTP 720 (Computational Methods) HW #1 Pt. 4
### Solve lens equation  for values of x-prime for pseudo-isothermal lens
### [Isabella Cox, Aug. 2020]

# Import Statements
from matplotlib import pyplot as plt
import numpy as np
from root_library import bisection
import math ##for pi


# Setup for plotting later
params = {'font.family':  'serif',
         'legend.fontsize': 'small',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'medium',
         'ytick.labelsize':'medium'}

plt.rcParams.update(params)

# Lens Parameters
factor = 0.008235
rc = 1.496E13

#xprime = np.linspace(0, 2, 10)
xprime = [0, 1, 2]
xprime = [x * 1.496E13 for x in xprime]  #convert AU to cm

xplain = [] #to hold the x(unprimed) values

for p in xprime:
    func = lambda x: x * (1 + factor * (1 + (x/rc)**2)**(-3/2)) - p #lens eq.
    print(func(0))


    out, no_iter = bisection(func, 0.1*p, 3*p) #with initial bounds guesses
    print(out)
    xplain.append(out)



print([x/a for x in xplain])
print([p/a for p in xprime])

for i in [x/a for x in xprime]:
    print(i)

# Ray tracing plotting

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

plt.title('Ray Tracing Diagram for Pseudo-Iso Lens: x\' = ' + str(xp) + ' AU')
plt.legend()

#plt.savefig('big_view_ray4'+str(idx)+'.eps')
#plt.show()

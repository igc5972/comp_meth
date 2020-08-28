### PURPOSE: ASTP 720 (Computational Methods) HW #1 Pt 2.
### [Isabella Cox, Aug. 2020]

# Import Statements
import numpy as np
from matplotlib import pyplot as plt
from interpolate import interpolate


### [Task 6]


# Set up universal plotting formats (text size and such)

params = {'font.family':  'serif',
         'legend.fontsize': 'small',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'medium',
         'ytick.labelsize':'medium'}

plt.rcParams.update(params)



# Open the data points from a text file and save them as arrays

x, N = np.loadtxt('lens_density.txt', delimiter = ',', unpack = True, skiprows = 1)



# Visualize the data

plt.scatter(x, N, color = 'k', label = 'Raw Data')
plt.xlabel('x')
plt.ylabel(r'$N_e (x)$')
#plt.title('Raw Data')
#plt.show()



# Perform interpolation on the data

func = interpolate(x, N)
halfs = np.arange(1.5, x[-1], 1)

new_ys = func(halfs)

plt.scatter(halfs, new_ys, color = 'r', label = 'Interpolated')
plt.xlabel('x')
plt.ylabel(r'$N_e (x)$')
#plt.title('Interpolated Data')
plt.legend()
plt.show()
